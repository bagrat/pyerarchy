__author__ = 'bagrat'

from nose.tools import *
import os

from pyerarchy.core.node import Node


def test_node():
    node = Node(os.path.join(os.path.dirname(__file__), 'static'))

    ls = node.ls()

    ok_(node.isdir)
    ok_(not node.isfile)
    ok_(len(ls) == 2)
    ok_('file' in ls)
    ok_('anotherdir' in ls)

    node = Node(os.path.join(os.path.dirname(__file__), 'static/file'))

    ok_(node.isfile)
    ok_(not node.isdir)

    raises_not_exists = False
    try:
        node = Node(os.path.join(os.path.dirname(__file__), 'notexistingnode'))
    except:
        raises_not_exists = True

    ok_(raises_not_exists)