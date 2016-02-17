import sys
import _ast
# from rope.base import ast

PY2 = sys.version_info[0] == 2
PY27 = sys.version_info[0:2] >= (2, 7)
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0:2] >= (3, 4)

try:
    str = unicode
except NameError:  # PY3

    str = str
    string_types = (str,)
    ast_arg_type = _ast.arg

    def get_ast_arg_arg(node):
        if isinstance(node, string_types):  # TODO: G21: Understand the Algorithm (Where it's used?)
            return node
        return node.arg

else:  # PY2

    string_types = (basestring,)
    ast_arg_type = _ast.Name

    def get_ast_arg_arg(node):
        if isinstance(node, string_types):  # Python2 arguments.vararg, arguments.kwarg
            return node
        return node.id
