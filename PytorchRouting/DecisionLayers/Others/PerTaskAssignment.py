"""
This file defines class PerTaskAssignment.

@author: Clemens Rosenbaum :: cgbr@cs.umass.edu
@created: 6/12/18
"""
"""
This file defines class REINFORCE.

@author: Clemens Rosenbaum :: cgbr@cs.umass.edu
@created: 6/7/18
"""
import torch

from ..Decision import Decision


class PerTaskAssignment(Decision):
    """
    This simple class translates task assignments stored in the meta-information objects to actions.
    """
    def __init__(self, *args, **kwargs):
        Decision.__init__(self, None, None, )

    @staticmethod
    def _loss(self, is_terminal, state, next_state, action, next_action, reward, cum_return, final_reward):
        return torch.zeros(1).to(action.device)

    def _construct_policy_storage(self, _1, _2, _3, _4):
        return []

    def _forward(self, xs, prior_action): pass

    def forward(self, xs, mxs, _=None, __=None):
        actions = torch.LongTensor([m.task for m in mxs]).to(xs.device)
        return xs, mxs, actions
