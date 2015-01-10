import os
from types import ModuleType
from pyerarchy import Node
from pyerarchy.ex import BadValueError

__author__ = 'bagrat'


class ModuleNode(Node):
    def __init__(self, module):
        if not isinstance(module, ModuleType):
            if not isinstance(module, (str, unicode)):
                raise BadValueError('Not a module or module name: {module}'.format(module=module))
            else:
                module = __import__(module)

        path = os.path.dirname(module.__file__)

        super(ModuleNode, self).__init__(path, create=False, strict=True)