# -*- coding: utf-8 -*-

import time
from exceptions import NotImplementedError

class ItemBase(object):

    def __init__(self, **kwargs):
        self.init(**kwargs)
        if kwargs:
            self.__dict__.update(kwargs)

    def init(self, **kwargs):
        raise NotImplementedError

    @property
    def dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, d):
        c = cls()
        c.__dict__.update(d)
        return c

    @classmethod
    def load_value(cls, data):
        raise NotImplementedError

    def time(self):
        return int(time.time())