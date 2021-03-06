"""
This file defines class BaseReward.

@author: Clemens Rosenbaum :: cgbr@cs.umass.edu
@created: 6/8/18
"""
import abc
import torch.nn as nn


class BaseReward(nn.Module, metaclass=abc.ABCMeta):
    """
    Class BaseReward defines the base function for all final reward functions.
    """

    def __init__(self, scale=1.):
        nn.Module.__init__(self)
        self._scale = scale

    @abc.abstractmethod
    def forward(self, loss, yest, ytrue): pass
