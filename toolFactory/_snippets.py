import ast
from typing import cast


overloadName = ast.Name('overload')
staticmethodName = ast.Name('staticmethod')
typing_TypeAliasName: ast.expr = cast(ast.expr, ast.Name('typing_TypeAlias'))
