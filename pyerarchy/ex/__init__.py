__author__ = 'bagrat'


class PyerarchyError(Exception):
    pass


class NotDirectoryError(PyerarchyError):
    pass


class BadValueError(PyerarchyError):
    pass