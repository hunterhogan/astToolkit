from typing import cast
import ast

astName_overload = ast.Name('overload')
astName_staticmethod = ast.Name('staticmethod')
astName_typing_TypeAlias: ast.expr = cast(ast.expr, ast.Name('typing_TypeAlias'))
