import torch
import math
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, PackedSequence
from functools import partial
from acouspike.models.surrogate.surrogate import SurrogateGradient
from acouspike.models.neuron.lif import RLIF

class PositionalEncoding(nn.Module):
    r"""Inject some information about the relative or absolute position of the tokens in the sequence.
        The positional encodings have the same dimension as the embeddings, so that the two can be summed.
        Here, we use sine and cosine functions of different frequencies.
    .. math:
        \text{PosEncoder}(pos, 2i) = sin(pos/10000^(2i/d_model))
        \text{PosEncoder}(pos, 2i+1) = cos(pos/10000^(2i/d_model))
        \text{where pos is the word position and i is the embed idx)
    Args:
        d_model: the embed dim (required).
        dropout: the dropout value (default=0.1).
        max_len: the max. length of the incoming sequence (default=5000).
    Examples:
        >>> pos_encoder = PositionalEncoding(d_model)
    """

    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        r"""Inputs of forward function
        Args:
            x: the sequence fed to the positional encoder model (required).
        Shape:
            x: [sequence length, batch size, embed dim]
            output: [sequence length, batch size, embed dim]
        Examples:
            >>> output = pos_encoder(x)
        """

        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)

def SDSA3(
        q,
        k,
        v,
        attn_mask=None,
        dropout_p=0.0,
        scale=0.125
):
    assert attn_mask is None
    # assert dropout_p == 0.0
    T, B, Nt, E = q.shape
    # q = q / math.sqrt(E)
    if True:
        attn = k.transpose(-2, -1) @ v
        # print(f"attn: {attn.size()}")
        # if dropout_p > 0.0:
        #     attn = nn.functional.dropout(attn, p=dropout_p)
        output = (q @ attn) * scale
    else:
        # q = q / math.sqrt(E)
        attn = q @ k.transpose(-2, -1)
        # attn = nn.functional.softmax(attn, dim=-1)
        # print(f"attn: {attn.size()}")
        # print(f"q: {q.size()}")
        output = (attn @ v) * scale

    # print(f"attn output: {output.size()}")
    return output, attn


def _in_projection_packed(
        q,
        k,
        v,
        w,
        b=None,
):
    r"""
    Performs the in-projection step of the attention operation, using packed weights.
    Output is a triple containing projection tensors for query, key and value.

    Args:
        q, k, v: query, key and value tensors to be projected. For self-attention,
            these are typically the same tensor; for encoder-decoder attention,
            k and v are typically the same tensor. (We take advantage of these
            identities for performance if they are present.) Regardless, q, k and v
            must share a common embedding dimension; otherwise their shapes may vary.
        w: projection weights for q, k and v, packed into a single tensor. Weights
            are packed along dimension 0, in q, k, v order.
        b: optional projection biases for q, k and v, packed into a single tensor
            in q, k, v order.

    Shape:
        Inputs:
        - q: :math:`(..., E)` where E is the embedding dimension
        - k: :math:`(..., E)` where E is the embedding dimension
        - v: :math:`(..., E)` where E is the embedding dimension
        - w: :math:`(E * 3, E)` where E is the embedding dimension
        - b: :math:`E * 3` where E is the embedding dimension

        Output:
        - in output list :math:`[q', k', v']`, each output tensor will have the
            same shape as the corresponding input tensor.
    """
    E = q.size(-1)
    if k is v:
        if q is k:
            # self-attention
            return nn.functional.linear(q, w, b).chunk(3, dim=-1)
        else:
            # encoder-decoder attention
            w_q, w_kv = w.split([E, E * 2])
            if b is None:
                b_q = b_kv = None
            else:
                b_q, b_kv = b.split([E, E * 2])
            return (nn.functional.linear(q, w_q, b_q),) + nn.functional.linear(k, w_kv, b_kv).chunk(2, dim=-1)
    else:
        w_q, w_k, w_v = w.chunk(3)
        if b is None:
            b_q = b_k = b_v = None
        else:
            b_q, b_k, b_v = b.chunk(3)
        return nn.functional.linear(q, w_q, b_q), nn.functional.linear(k, w_k, b_k), nn.functional.linear(v, w_v, b_v)

def spk_multi_head_attention_forward(
        query,
        key,
        value,
        embed_dim_to_check,
        num_heads,
        in_proj_weight,
        in_proj_bias,
        bias_k,
        bias_v,
        dropout_p,
        out_proj_weight,
        out_proj_bias,
        q_lif=None,
        k_lif=None,
        v_lif=None,
        attn_lif=None,
        training=True,
        key_padding_mask=None,
        need_weights=True,
        attn_mask=None,
):
    r"""
    Args:
        query, key, value: map a query and a set of key-value pairs to an output.
            See "Attention Is All You Need" for more details.
        embed_dim_to_check: total dimension of the model.
        num_heads: parallel attention heads.
        in_proj_weight, in_proj_bias: input projection weight and bias.
        bias_k, bias_v: bias of the key and value sequences to be added at dim=0.
        add_zero_attn: add a new batch of zeros to the key and
                       value sequences at dim=1.
        dropout_p: probability of an element to be zeroed.
        out_proj_weight, out_proj_bias: the output projection weight and bias.
        training: apply dropout if is ``True``.
        key_padding_mask: if provided, specified padding elements in the key will
            be ignored by the attention. This is an binary mask. When the value is True,
            the corresponding value on the attention layer will be filled with -inf.
        need_weights: output attn_output_weights.
        attn_mask: 2D or 3D mask that prevents attention to certain positions. A 2D mask will be broadcasted for all
            the batches while a 3D mask allows to specify a different mask for the entries of each batch.
        use_separate_proj_weight: the function accept the proj. weights for query, key,
            and value in different forms. If false, in_proj_weight will be used, which is
            a combination of q_proj_weight, k_proj_weight, v_proj_weight.
        q_proj_weight, k_proj_weight, v_proj_weight, in_proj_bias: input projection weight and bias.
        static_k, static_v: static key and value used for attention operators.


    Shape:
        Inputs:
        - query: :math:`(L, N, E)` where L is the target sequence length, N is the batch size, E is
          the embedding dimension.
        - key: :math:`(S, N, E)`, where S is the source sequence length, N is the batch size, E is
          the embedding dimension.
        - value: :math:`(S, N, E)` where S is the source sequence length, N is the batch size, E is
          the embedding dimension.
        - key_padding_mask: :math:`(N, S)` where N is the batch size, S is the source sequence length.
          If a ByteTensor is provided, the non-zero positions will be ignored while the zero positions
          will be unchanged. If a BoolTensor is provided, the positions with the
          value of ``True`` will be ignored while the position with the value of ``False`` will be unchanged.
        - attn_mask: 2D mask :math:`(L, S)` where L is the target sequence length, S is the source sequence length.
          3D mask :math:`(N*num_heads, L, S)` where N is the batch size, L is the target sequence length,
          S is the source sequence length. attn_mask ensures that position i is allowed to attend the unmasked
          positions. If a ByteTensor is provided, the non-zero positions are not allowed to attend
          while the zero positions will be unchanged. If a BoolTensor is provided, positions with ``True``
          are not allowed to attend while ``False`` values will be unchanged. If a FloatTensor
          is provided, it will be added to the attention weight.
        - static_k: :math:`(N*num_heads, S, E/num_heads)`, where S is the source sequence length,
          N is the batch size, E is the embedding dimension. E/num_heads is the head dimension.
        - static_v: :math:`(N*num_heads, S, E/num_heads)`, where S is the source sequence length,
          N is the batch size, E is the embedding dimension. E/num_heads is the head dimension.

        Outputs:
        - attn_output: :math:`(L, N, E)` where L is the target sequence length, N is the batch size,
          E is the embedding dimension.
        - attn_output_weights: :math:`(N, L, S)` where N is the batch size,
          L is the target sequence length, S is the source sequence length.
    """

    # set up shape vars
    T, tgt_len, bsz, embed_dim = query.shape
    T, src_len, _, _ = key.shape
    assert embed_dim == embed_dim_to_check, \
        f"was expecting embedding dimension of {embed_dim_to_check}, but got {embed_dim}"
    if isinstance(embed_dim, torch.Tensor):
        # embed_dim can be a tensor when JIT tracing
        head_dim = embed_dim.div(num_heads, rounding_mode='trunc')
    else:
        head_dim = embed_dim // num_heads
    assert head_dim * num_heads == embed_dim, f"embed_dim {embed_dim} not divisible by num_heads {num_heads}"

    assert key.shape == value.shape, f"key shape {key.shape} does not match value shape {value.shape}"

    #
    # compute in-projection
    #
    q, k, v = _in_projection_packed(query, key, value, in_proj_weight, in_proj_bias)
    q = q_lif(q)
    k = k_lif(k)
    v = v_lif(v)
    # print(f"q: {q.size()}, k: {k.size()}, v: {v.size()}")
    # prep attention mask
    assert attn_mask is None, "Not implemented!"

    # prep key padding mask
    assert key_padding_mask is None, "Not implemented"

    # add bias along batch dimension (currently second)

    assert bias_k is None
    assert bias_v is None

    #
    # reshape q, k, v for multihead attention and make em batch first
    #
    q = q.contiguous().view(T, tgt_len, bsz * num_heads, head_dim).transpose(1, 2)
    k = k.contiguous().view(T, k.shape[1], bsz * num_heads, head_dim).transpose(1, 2)
    v = v.contiguous().view(T, v.shape[1], bsz * num_heads, head_dim).transpose(1, 2)
    # print(f"****q: {q.size()}, k: {k.size()}, v: {v.size()}")

    # add zero attention along batch dimension (now first)

    # update source sequence length after adjustments
    src_len = k.size(2)

    # merge key padding and attention masks
    assert key_padding_mask is None

    # convert mask to float

    # adjust dropout probability
    if not training:
        dropout_p = 0.0

    #
    # (deep breath) calculate attention and out projection
    #
    attn_output, attn_output_weights = SDSA3(q, k, v, attn_mask, dropout_p)
    # print(f"attn_output: {attn_output.size()}")

    attn_output = attn_output.transpose(1, 2).contiguous().view(T, tgt_len, bsz, embed_dim)
    attn_output = attn_lif(attn_output)
    attn_output = nn.functional.linear(attn_output, out_proj_weight, out_proj_bias)

    if need_weights:
        # average attention weights over heads
        attn_output_weights = attn_output_weights.view(T, bsz, num_heads, tgt_len, src_len)
        return attn_output, attn_output_weights.sum(dim=2) / num_heads
    else:
        return attn_output, None


class SpkMultiheadAttention(nn.Module):
    r"""Allows the model to jointly attend to information
    from different representation subspaces.
    See `Attention Is All You Need <https://arxiv.org/abs/1706.03762>`_.

    .. math::
        \text{MultiHead}(Q, K, V) = \text{Concat}(head_1,\dots,head_h)W^O

    where :math:`head_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)`.

    Args:
        embed_dim: Total dimension of the model.
        num_heads: Number of parallel attention heads. Note that ``embed_dim`` will be split
            across ``num_heads`` (i.e. each head will have dimension ``embed_dim // num_heads``).
        dropout: Dropout probability on ``attn_output_weights``. Default: ``0.0`` (no dropout).
        bias: If specified, adds bias to input / output projection layers. Default: ``True``.
        add_bias_kv: If specified, adds bias to the key and value sequences at dim=0. Default: ``False``.
        add_zero_attn: If specified, adds a new batch of zeros to the key and value sequences at dim=1.
            Default: ``False``.
        kdim: Total number of features for keys. Default: ``None`` (uses ``kdim=embed_dim``).
        vdim: Total number of features for values. Default: ``None`` (uses ``vdim=embed_dim``).
        batch_first: If ``True``, then the input and output tensors are provided
            as (batch, seq, feature). Default: ``False`` (seq, batch, feature).

    Examples::

        >>> multihead_attn = nn.MultiheadAttention(embed_dim, num_heads)
        >>> attn_output, attn_output_weights = multihead_attn(query, key, value)
    """
    __constants__ = ['batch_first']

    # bias_k: Optional[torch.Tensor]
    # bias_v: Optional[torch.Tensor]

    def __init__(self, embed_dim, num_heads, dropout=0., bias=True,
                 batch_first=False, spiking_neuron=None, device=None, dtype=None) -> None:
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(SpkMultiheadAttention, self).__init__()
        self.embed_dim = embed_dim
        self.kdim = embed_dim
        self.vdim = embed_dim
        self._qkv_same_embed_dim = True

        self.num_heads = num_heads
        self.dropout = dropout
        self.batch_first = batch_first
        self.head_dim = embed_dim // num_heads
        assert self.head_dim * num_heads == self.embed_dim, "embed_dim must be divisible by num_heads"

        self.in_proj_weight = nn.Parameter(torch.empty((3 * embed_dim, embed_dim), **factory_kwargs))
        self.register_parameter('q_proj_weight', None)
        self.register_parameter('k_proj_weight', None)
        self.register_parameter('v_proj_weight', None)

        if bias:
            self.in_proj_bias = nn.Parameter(torch.empty(3 * embed_dim, **factory_kwargs))
        else:
            self.register_parameter('in_proj_bias', None)
        self.out_proj = nn.Linear(embed_dim, embed_dim, bias=bias, **factory_kwargs)

        self.bias_k = self.bias_v = None

        self._reset_parameters()

        assert spiking_neuron is not None
        self.scale = 0.125
        self.head_lif = spiking_neuron()
        self.q_lif = spiking_neuron()
        self.k_lif = spiking_neuron()
        self.v_lif = spiking_neuron()
        self.attn_lif = spiking_neuron()

    def _reset_parameters(self):

        nn.init.xavier_uniform_(self.in_proj_weight)

        if self.in_proj_bias is not None:
            nn.init.constant_(self.in_proj_bias, 0.)
            nn.init.constant_(self.out_proj.bias, 0.)

    # def __setstate__(self, state):
    #     # Support loading old MultiheadAttention checkpoints generated by v1.1.0
    #     if '_qkv_same_embed_dim' not in state:
    #         state['_qkv_same_embed_dim'] = True
    #
    #     super(MultiheadAttention, self).__setstate__(state)

    def forward(self, query, key, value, key_padding_mask=None,
                need_weights=True, attn_mask=None):
        r"""
    Args:
        query: Query embeddings of shape :math:`(L, N, E_q)` when ``batch_first=False`` or :math:`(N, L, E_q)`
            when ``batch_first=True``, where :math:`L` is the target sequence length, :math:`N` is the batch size,
            and :math:`E_q` is the query embedding dimension ``embed_dim``. Queries are compared against
            key-value pairs to produce the output. See "Attention Is All You Need" for more details.
        key: Key embeddings of shape :math:`(S, N, E_k)` when ``batch_first=False`` or :math:`(N, S, E_k)` when
            ``batch_first=True``, where :math:`S` is the source sequence length, :math:`N` is the batch size, and
            :math:`E_k` is the key embedding dimension ``kdim``. See "Attention Is All You Need" for more details.
        value: Value embeddings of shape :math:`(S, N, E_v)` when ``batch_first=False`` or :math:`(N, S, E_v)` when
            ``batch_first=True``, where :math:`S` is the source sequence length, :math:`N` is the batch size, and
            :math:`E_v` is the value embedding dimension ``vdim``. See "Attention Is All You Need" for more details.
        key_padding_mask: If specified, a mask of shape :math:`(N, S)` indicating which elements within ``key``
            to ignore for the purpose of attention (i.e. treat as "padding"). Binary and byte masks are supported.
            For a binary mask, a ``True`` value indicates that the corresponding ``key`` value will be ignored for
            the purpose of attention. For a byte mask, a non-zero value indicates that the corresponding ``key``
            value will be ignored.
        need_weights: If specified, returns ``attn_output_weights`` in addition to ``attn_outputs``.
            Default: ``True``.
        attn_mask: If specified, a 2D or 3D mask preventing attention to certain positions. Must be of shape
            :math:`(L, S)` or :math:`(N\cdot\text{num\_heads}, L, S)`, where :math:`N` is the batch size,
            :math:`L` is the target sequence length, and :math:`S` is the source sequence length. A 2D mask will be
            broadcasted across the batch while a 3D mask allows for a different mask for each entry in the batch.
            Binary, byte, and float masks are supported. For a binary mask, a ``True`` value indicates that the
            corresponding position is not allowed to attend. For a byte mask, a non-zero value indicates that the
            corresponding position is not allowed to attend. For a float mask, the mask values will be added to
            the attention weight.

    Outputs:
        - **attn_output** - Attention outputs of shape :math:`(L, N, E)` when ``batch_first=False`` or
          :math:`(N, L, E)` when ``batch_first=True``, where :math:`L` is the target sequence length, :math:`N` is
          the batch size, and :math:`E` is the embedding dimension ``embed_dim``.
        - **attn_output_weights** - Attention output weights of shape :math:`(N, L, S)`, where :math:`N` is the batch
          size, :math:`L` is the target sequence length, and :math:`S` is the source sequence length. Only returned
          when ``need_weights=True``.
        """
        assert self.batch_first is False
        # if self.batch_first:
        #     query, key, value = [x.transpose(1, 0) for x in (query, key, value)]

        attn_output, attn_output_weights = spk_multi_head_attention_forward(
            query, key, value, self.embed_dim, self.num_heads,
            self.in_proj_weight, self.in_proj_bias,
            self.bias_k, self.bias_v,
            self.dropout, self.out_proj.weight, self.out_proj.bias,
            q_lif=self.q_lif, k_lif=self.k_lif, v_lif=self.v_lif, attn_lif=self.attn_lif,
            training=self.training,
            key_padding_mask=key_padding_mask, need_weights=need_weights,
            attn_mask=attn_mask)
        if self.batch_first:
            return attn_output.transpose(1, 0), attn_output_weights
        else:
            return attn_output, attn_output_weights



class SpkTransformerEncoderLayer(nn.Module):
    r"""TransformerEncoderLayer is made up of self-attn and feedforward network.
    This standard encoder layer is based on the paper "Attention Is All You Need".
    Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
    Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In Advances in
    Neural Information Processing Systems, pages 6000-6010. Users may modify or implement
    in a different way during application.

    Args:
        d_model: the number of expected features in the input (required).
        nhead: the number of heads in the multiheadattention models (required).
        dim_feedforward: the dimension of the feedforward network model (default=2048).
        dropout: the dropout value (default=0.1).
        activation: the activation function of the intermediate layer, can be a string
            ("relu" or "gelu") or a unary callable. Default: relu
        layer_norm_eps: the eps value in layer normalization components (default=1e-5).
        batch_first: If ``True``, then the input and output tensors are provided
            as (batch, seq, feature). Default: ``False``.
        norm_first: if ``True``, layer norm is done prior to attention and feedforward
            operations, respectivaly. Otherwise it's done after. Default: ``False`` (after).

    Examples::
        >>> encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
        >>> src = torch.rand(10, 32, 512)
        >>> out = encoder_layer(src)

    Alternatively, when ``batch_first`` is ``True``:
        >>> encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8, batch_first=True)
        >>> src = torch.rand(32, 10, 512)
        >>> out = encoder_layer(src)
    """
    __constants__ = ['batch_first', 'norm_first']

    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1, activation=torch.nn.functional.relu,
                 layer_norm_eps=1e-5, batch_first=False, norm_first=False, spiking_neuron=None,
                 device=None, dtype=None) -> None:
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(SpkTransformerEncoderLayer, self).__init__()
        self.self_attn = SpkMultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first,
                                               spiking_neuron=spiking_neuron,
                                               **factory_kwargs)
        # Implementation of Feedforward model
        self.head_lif = spiking_neuron()
        self.fc1_lif = spiking_neuron()
        self.linear1 = nn.Linear(d_model, dim_feedforward, **factory_kwargs)
        self.dropout = nn.Dropout(dropout)
        self.fc2_lif = spiking_neuron()
        self.linear2 = nn.Linear(dim_feedforward, d_model, **factory_kwargs)

        self.norm_first = norm_first
        self.norm1 = nn.LayerNorm(d_model, eps=layer_norm_eps, **factory_kwargs)
        self.norm2 = nn.LayerNorm(d_model, eps=layer_norm_eps, **factory_kwargs)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

        # Legacy string support for activation function.
        # if isinstance(activation, str):
        #     self.activation = _get_activation_fn(activation)
        # else:
        self.activation = activation

    # def __setstate__(self, state):
    #     if 'activation' not in state:
    #         state['activation'] = F.relu
    #     super(TransformerEncoderLayer, self).__setstate__(state)

    def forward(self, src, src_mask=None, src_key_padding_mask=None, is_causal=False):
        r"""Pass the input through the encoder layer.

        Args:
            src: the sequence to the encoder layer (required).
            src_mask: the mask for the src sequence (optional).
            src_key_padding_mask: the mask for the src keys per batch (optional).

        Shape:
            see the docs in Transformer class.
        """

        # see Fig. 1 of https://arxiv.org/pdf/2002.04745v1.pdf

        x = src
        x = self.head_lif(x)
        # print(f"head_lif: {x.size()}")
        assert self.norm_first is False
        # if self.norm_first:
        #     x = x + self._sa_block(self.norm1(x), src_mask, src_key_padding_mask)
        #     x = x + self._ff_block(self.norm2(x))
        # else:
        x = self.norm1(x + self._sa_block(x, src_mask, src_key_padding_mask))
        # print(f"norm1: {x.size()}")
        x = self.norm2(x + self._ff_block(x))
        # print(f"norm2: {x.size()}")

        return x

    # self-attention block
    def _sa_block(self, x,
                  attn_mask, key_padding_mask):
        x = self.self_attn(x, x, x,
                           attn_mask=attn_mask,
                           key_padding_mask=key_padding_mask,
                           need_weights=False)[0]
        return self.dropout1(x)

    # feed forward block
    def _ff_block(self, x):
        x = self.fc1_lif(x)
        x = self.linear1(x)
        x = self.fc2_lif(x)
        x = self.linear2(x)
        # x = self.linear2(self.dropout(self.activation(self.linear1(x))))
        return x


class SpkTransformerNet(nn.Module):
    def __init__(self,
                 input_size,
                 hidden_size,
                 nhead,
                 batch_first=True, 
                 num_hidden_layers=1,
                 dropout=0,
                 surrogate='triangle',
                 alpha=1.0,
                 decay=0.5,
                 threshold=0.5,
                 recurrent=False,
                 time_window=512,
                 T=4,
                 ):
        super(SpkTransformerNet, self).__init__()

        
        self.encoder = nn.Linear(input_size, hidden_size)
        self.batch_first = batch_first
        surro_grad = SurrogateGradient(func_name=surrogate, a=alpha)
        exec_mode = "serial"
        spiking_neuron = partial(RLIF,
                                 decay=decay,
                                 threshold=threshold,
                                 time_step=time_window,
                                 surro_grad=surro_grad,
                                 exec_mode=exec_mode,
                                 recurrent=recurrent,
                                 learning_rule='stbp',
                                 )

        encoder_layer = SpkTransformerEncoderLayer(d_model=hidden_size, nhead=nhead, dim_feedforward=hidden_size * 4,
                                                   dropout=dropout, spiking_neuron=spiking_neuron
                                                   )
        encoder_norm = nn.LayerNorm(hidden_size)
        custom_encoder = nn.TransformerEncoder(encoder_layer, num_hidden_layers, encoder_norm)
        self.transformer = nn.Transformer(d_model=hidden_size, nhead=nhead, dim_feedforward=hidden_size * 4,
                                          num_encoder_layers=num_hidden_layers, dropout=dropout,
                                          custom_encoder=custom_encoder).encoder
        self.time_window = T

        self.pos_encoder = PositionalEncoding(hidden_size, dropout=0.)


    def flatten_parameters(self):
            # Ensure all parameters are contiguous in memory for efficiency
            pass

    def forward(self, x, hidden=None):
        is_packed = isinstance(x, PackedSequence)
        assert hidden is None, "Not allowed to pass previous states in the current imple."
        if is_packed:
            x, lengths = pad_packed_sequence(x, batch_first=self.batch_first)
        # print(f"x: {x.size()}") # [90, 101, 2560]
        # print(f"max lengths: {lengths.max()}") # [90]
        
        if self.batch_first:
            batch_size, seq_len, _ = x.size()
            x = x.transpose(0, 1)  # Convert to (seq_len, batch_size, input_size)
        else:
            seq_len, batch_size, _ = x.size()
            x = x     
        x = self.encoder(x)
        x = self.pos_encoder(x)
        x = (x.unsqueeze(0)).repeat(self.time_window, 1, 1, 1)
        x = self.transformer(x)  # input should have dimension (N, C, L)

        output = x.mean(0)
        
        if self.batch_first:
            output = output.transpose(0, 1)  # Convert to (batch_size, seq_len, num_directions * hidden_size)
        
        if is_packed:
            output = pack_padded_sequence(output, lengths, batch_first=self.batch_first)
        
        # print(f"h_n: {h_n.size()}")

        return output, (None, None)
    