from typing import cast
import ast

astName_overload = ast.Name('overload')
astName_staticmethod = ast.Name('staticmethod')
astName_typing_TypeAlias: ast.expr = cast(ast.expr, ast.Name('typing_TypeAlias'))

# The `format` method continues to disappoint me.
# The type hint hover is merely: (*args: LiteralString, **kwargs: LiteralString) -> LiteralString
# I want to use these format templates to remind me which identifiers to use.
format_hasDOTIdentifier: str = "hasDOT{attribute}"
formatTypeAliasSubcategory: str = "{hasDOTIdentifier}_{TypeAliasSubcategory}"
