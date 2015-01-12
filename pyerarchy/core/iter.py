__author__ = 'bagrat'


class NodeIterator(object):
    def __init__(self, node):
        super(NodeIterator, self).__init__()

        self.nodes = node.children()
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.nodes):
            raise StopIteration

        return self.nodes[self.i]

    def next(self):
        return self.__next__()