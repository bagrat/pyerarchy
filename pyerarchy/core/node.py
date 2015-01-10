import os
from pyerarchy.ex import NotDirectoryError, BadValueError

__author__ = 'bagrat'


class Node(object):
    def __init__(self, path, create=False):
        """Creates node object to walk through filesystem using attributes.

        :param path: The path to set the object to.
        :param create: If set to True, the specified path will be created if it does not exist.
        :return:
        """
        p = path
        p = os.path.abspath(p)
        p = os.path.expanduser(p)
        p = os.path.realpath(p)
        # TODO: add expandvars expansion, if needed

        if not os.path.exists(p):
            if not create:
                raise IOError('Path does not exist: %(path)'.format(path=p))
            else:
                os.makedirs(p, mode=0o755)

        self.path = p
        self.isfile = os.path.isfile(p)
        self.isdir = os.path.isdir(p)

    def ls(self):
        """List the children entities of the directory.

        Raises exception if the object is a file.

        :return:
        """
        if self.isfile:
            raise NotDirectoryError('Cannot ls() on non-directory node')

        return os.listdir(self.path)

    def mkdir(self, children, mode=0o0755, return_node=True):
        """Creates child entities in directory.

        Raises exception if the object is a file.

        :param children: The list of children to be created.
        :return: The child object, if one child is provided. None, otherwise.
        """
        result = None

        if isinstance(children, (str, unicode)):
            if os.path.isabs(children):
                raise BadValueError('Cannot mkdir an absolute path')

            rel_path = os.path.join(self.path, children)
            os.makedirs(rel_path, mode)

            if return_node:
                result = Node(rel_path)
        else:
            for child in children:
                self.mkdir(child, mode, False)

        return result
