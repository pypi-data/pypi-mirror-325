from abc import abstractmethod
from typing import Callable
import torch

import torch
import torch.nn as nn
import copy
import torch.nn.functional as F


class MemoryModule(nn.Module):
    def __init__(self):
        """
        * :ref:`API in English <MemoryModule.__init__-en>`

        .. _MemoryModule.__init__-cn:

        ``MemoryModule`` 是SpikingJelly中所有有状态（记忆）模块的基类。

        * :ref:`中文API <MemoryModule.__init__-cn>`

        .. _MemoryModule.__init__-en:

        ``MemoryModule`` is the base class of all stateful modules in SpikingJelly.

        """
        super().__init__()
        self._memories = {}
        self._memories_rv = {}

    def register_memory(self, name: str, value):
        """
        * :ref:`API in English <MemoryModule.register_memory-en>`

        .. _MemoryModule.register_memory-cn:

        :param name: 变量的名字
        :type name: str
        :param value: 变量的值
        :type value: any

        将变量存入用于保存有状态变量（例如脉冲神经元的膜电位）的字典中。这个变量的重置值会被设置为 ``value``。每次调用 ``self.reset()``
        函数后， ``self.name`` 都会被重置为 ``value``。

        * :ref:`中文API <MemoryModule.register_memory-cn>`

        .. _MemoryModule.register_memory-en:

        :param name: variable's name
        :type name: str
        :param value: variable's value
        :type value: any

        Register the variable to memory dict, which saves stateful variables (e.g., the membrane potential of a
        spiking neuron). The reset value of this variable will be ``value``. ``self.name`` will be set to ``value`` after
        each calling of ``self.reset()``.

        """
        assert not hasattr(self, name), f'{name} has been set as a member variable!'
        self._memories[name] = value
        self.set_reset_value(name, value)

    def reset(self):
        """
        * :ref:`API in English <MemoryModule.reset-en>`

        .. _MemoryModule.reset-cn:

        重置所有有状态变量为默认值。

        * :ref:`中文API <MemoryModule.reset-cn>`

        .. _MemoryModule.reset-en:

        Reset all stateful variables to their default values.
        """
        for key in self._memories.keys():
            self._memories[key] = copy.deepcopy(self._memories_rv[key])

    def set_reset_value(self, name: str, value):
        self._memories_rv[name] = copy.deepcopy(value)

    def __getattr__(self, name: str):
        if '_memories' in self.__dict__:
            memories = self.__dict__['_memories']
            if name in memories:
                return memories[name]

        return super().__getattr__(name)

    def __setattr__(self, name: str, value) -> None:
        _memories = self.__dict__.get('_memories')
        if _memories is not None and name in _memories:
            _memories[name] = value
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name in self._memories:
            del self._memories[name]
            del self._memories_rv[name]
        else:
            return super().__delattr__(name)

    def __dir__(self):
        module_attrs = dir(self.__class__)
        attrs = list(self.__dict__.keys())
        parameters = list(self._parameters.keys())
        modules = list(self._modules.keys())
        buffers = list(self._buffers.keys())
        memories = list(self._memories.keys())
        keys = module_attrs + attrs + parameters + modules + buffers + memories

        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)

    def memories(self):
        """
        * :ref:`API in English <MemoryModule.memories-en>`

        .. _MemoryModule.memories-cn:

        :return: 返回一个所有状态变量的迭代器
        :rtype: Iterator

        * :ref:`中文API <MemoryModule.memories-cn>`

        .. _MemoryModule.memories-en:

        :return: an iterator over all stateful variables
        :rtype: Iterator
        """
        for name, value in self._memories.items():
            yield value

    def named_memories(self):
        """
        * :ref:`API in English <MemoryModule.named_memories-en>`

        .. _MemoryModule.named_memories-cn:

        :return: 返回一个所有状态变量及其名称的迭代器
        :rtype: Iterator

        * :ref:`中文API <MemoryModule.named_memories-cn>`

        .. _MemoryModule.named_memories-en:

        :return: an iterator over all stateful variables and their names
        :rtype: Iterator
        """

        for name, value in self._memories.items():
            yield name, value

    # def detach(self):
    #     """
    #     * :ref:`API in English <MemoryModule.detach-en>`
    #
    #     .. _MemoryModule.detach-cn:
    #
    #     从计算图中分离所有有状态变量。
    #
    #     .. tip::
    #
    #         可以使用这个函数实现TBPTT(Truncated Back Propagation Through Time)。
    #
    #
    #     * :ref:`中文API <MemoryModule.detach-cn>`
    #
    #     .. _MemoryModule.detach-en:
    #
    #     Detach all stateful variables.
    #
    #     .. admonition:: Tip
    #         :class: tip
    #
    #         We can use this function to implement TBPTT(Truncated Back Propagation Through Time).
    #
    #     """
    #
    #     for key in self._memories.keys():
    #         if isinstance(self._memories[key], torch.Tensor):
    #             self._memories[key].detach_()

    def _apply(self, fn):
        for key, value in self._memories.items():
            if isinstance(value, torch.Tensor):
                self._memories[key] = fn(value)
        # do not apply on default values
        # for key, value in self._memories_rv.items():
        #     if isinstance(value, torch.Tensor):
        #         self._memories_rv[key] = fn(value)
        return super()._apply(fn)

    def _replicate_for_data_parallel(self):
        replica = super()._replicate_for_data_parallel()
        replica._memories = self._memories.copy()
        return replica


class BaseNode(MemoryModule):
    def __init__(self,
                 threshold: float = 1.,
                 surrogate_function=None,
                 hard_reset: bool = False,
                 detach_reset: bool = False):

        assert isinstance(threshold, float)
        assert isinstance(hard_reset, bool)
        assert isinstance(detach_reset, bool)
        super().__init__()

        self.register_memory('v', 0.)

        self.threshold = threshold

        self.hard_reset = hard_reset
        self.detach_reset = detach_reset

        self.surrogate_function = surrogate_function

    def forward(self, x: torch.Tensor):
        self.v_float_to_tensor(x)
        self.neuronal_charge(x)
        spike = self.neuronal_fire()
        self.neuronal_reset(spike)
        return spike

    @abstractmethod
    def neuronal_charge(self, x: torch.Tensor):
        raise NotImplementedError

    def neuronal_fire(self):
        return self.surrogate_function(self.v - self.threshold)

    def neuronal_reset(self, spike):
        if self.detach_reset:
            spike_d = spike.detach()
        else:
            spike_d = spike

        if self.hard_reset:
            self.v = self.v * (1. - spike_d)
        else:
            self.v = self.v - spike_d * self.threshold

    def extra_repr(self):
        return f'threshold={self.threshold}, detach_reset={self.detach_reset}, hard_reset={self.hard_reset}'

    def v_float_to_tensor(self, x: torch.Tensor):
        if isinstance(self.v, float):
            v_init = self.v
            self.v = torch.full_like(x.data, v_init)


class LIFNode(BaseNode):
    def __init__(self,
                 decay_factor=0.5,
                 threshold=1.,
                 neuron_num=1,
                 surrogate_function=None,
                 hard_reset=False,
                 detach_reset=False,
                 detach_mem=False,
                 recurrent=False
                 ):
        super().__init__(threshold, surrogate_function, hard_reset, detach_reset)
        self.decay_factor = torch.tensor(decay_factor).float()
        self.detach_mem = detach_mem
        # self.num_trace = num_trace
        # for trace_id in range(self.num_trace):
        #     self.register_memory(f'e_trace_{trace_id}', 0.)

    def extra_repr(self):
        return super().extra_repr() + f', decay_factor={self.decay_factor:.2f}, detach_mem={self.detach_mem}, '

    def neuronal_charge(self, x: torch.Tensor):
        if self.detach_mem:
            self.v = self.v.detach() * self.decay_factor + x
        else:
            self.v = self.v * self.decay_factor + x

    def neuronal_fire(self):
        return self.surrogate_function(self.v - self.threshold)

    def forward(self, x):
        self.v_float_to_tensor(x)
        self.neuronal_charge(x)
        spike = self.neuronal_fire()
        self.neuronal_reset(spike)
        return spike


class SLTT_LIFNode(LIFNode):
    def __init__(self,
                 decay_factor=0.5,
                 v_threshold=1.,
                 surrogate_function=None,
                 hard_reset=False,
                 ):
        super().__init__(decay_factor, v_threshold, surrogate_function, hard_reset, detach_reset=True, detach_mem=True)

class OTTT_LIFNode(LIFNode):
    def __init__(self,
                 decay_factor=0.5,
                 v_threshold=1.,
                 surrogate_function=None,
                 hard_reset=False,
                 ):
        super().__init__(decay_factor, v_threshold, surrogate_function, hard_reset, detach_reset=True, detach_mem=True)
        self.register_memory('trace', 0.)

    @staticmethod
    def track_trace(spike, trace, decay_factor):
        with torch.no_grad():
            trace = trace * decay_factor + spike
        return trace

    def trace_float_to_tensor(self, x: torch.Tensor):
        if isinstance(self.trace, float):
            trace_init = self.trace
            self.trace = torch.full_like(x.data, trace_init)

    def forward(self, x):
        self.v_float_to_tensor(x)
        if self.training:
            self.trace_float_to_tensor(x)
        self.neuronal_charge(x)
        spike = self.neuronal_fire()
        self.neuronal_reset(spike)
        if self.training:
            self.trace = self.track_trace(spike, self.trace, self.decay_factor)
            return [spike, self.trace]
        else:
            return spike

