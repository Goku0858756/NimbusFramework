__author__ = 'N05F3R4TU'
import itertools
import builtins


class Chainable(object):
    def __init__(self, data, method=None):
        self.data = data
        self.method = method

    def __getattr__(self, name):
        try:
            method = getattr(self.data, name)
        except AttributeError:
            try:
                method = getattr(builtins, name)
            except AttributeError:
                method = getattr(itertools, name)

        return Chainable(self.data, method)

    def __call__(self, *args, **kwargs):
        try:
            return Chainable(list(self.method(self.data, *args, **kwargs)))
        except TypeError:
            return Chainable(list(self.method(args[0], self.data, **kwargs)))

if __name__ == '__main__':
    chainable_list = Chainable([3, 1, 2, 0])
    print((chainable_list.chain([11,8,6,7,9,4,5]).sorted().reversed().data))