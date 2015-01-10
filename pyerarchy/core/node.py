import os

__author__ = 'bagrat'


class Node():
    def __init__(self, path):
        p = path
        p = os.path.abspath(p)
        p = os.path.expanduser(p)
        p = os.path.realpath(p)
        # TODO: add expandvars expansion, if needed

        if not os.path.exists(p):
            pass  # TODO: raise it :)

        self.path = p
        self.isfile = os.path.isfile(p)
        self.isdir = os.path.isdir(p)

    def ls(self):
        if self.isfile:
            pass  # TODO: raise it :)

        return os.listdir(self.path)
