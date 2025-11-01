from collections.abc import Callable
from typing_extensions import TypeIs
import ast

class Be:
    class _Name(type):
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Name]:
            return isinstance(node, ast.Name)

    class Name(metaclass=_Name):
        @staticmethod
        def idIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST | None], TypeIs[ast.Name] | bool]:
            """`Be.Name.idIs`, matches `class` `ast.Name` and checks the `id` attribute."""
            def workhorse(node: ast.AST | None) -> TypeIs[ast.Name] | bool:
                if node is None or not isinstance(node, ast.Name):
                    return False
                return attributeCondition(node.id)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST | None], TypeIs[ast.Name] | bool]:
            """`Be.Name.ctxIs`, matches `class` `ast.Name` and checks the `ctx` attribute."""
            def workhorse(node: ast.AST | None) -> TypeIs[ast.Name] | bool:
                if node is None or not isinstance(node, ast.Name):
                    return False
                return attributeCondition(node.ctx)
            return workhorse
