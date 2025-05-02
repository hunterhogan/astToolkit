from collections.abc import Callable, Sequence
import typeshed_client.finder
from toolFactory import FREAKOUT, pathTypeshed, Z0Z_typesSpecial, makeTools
from pathlib import Path
from typing import Any, TypeAlias as typing_TypeAlias, TypeVar as typing_TypeVar
import ast

ast_expr_Slice: typing_TypeAlias = ast.expr
ast_Identifier: typing_TypeAlias = str
str_nameDOTname: typing_TypeAlias = str

个 = typing_TypeVar('个', bound = ast.AST, covariant = True)
NodeORattribute = typing_TypeVar('NodeORattribute', bound = ast.AST | ast_expr_Slice | ast_Identifier | str_nameDOTname | bool | Any | None, covariant = True)

# TODO Some `DOT` methods return lists, notably DOT.targets, which is an attribute of ast.Assign.
# But, none or almost none of the other functions and methods accept a list as input.
# This is most obviously a problem in `ClassIsAndAttribute.targetsIs` because the user needs to pass
# a function that can take list[ast.expr] as a parameter.
# I don't know if the following works, but it is interesting.
# ClassIsAndAttribute.targetsIs(ast.Assign, lambda list_expr: any([IfThis.isSubscript_Identifier('foldGroups')(node) for node in list_expr]))

class cleverName:
    @staticmethod
    def index(at: int) -> Callable[[Sequence[NodeORattribute]], NodeORattribute]:
        def workhorse(zzz: Sequence[NodeORattribute]) -> NodeORattribute:
            node = zzz[at]
            return node
        return workhorse

if __name__ == "__main__":
	search_context = typeshed_client.finder.get_search_context(typeshed=pathTypeshed if pathTypeshed.exists() else None)

	# pathFilenameStubFile: Path | None = typeshed_client.finder.get_stub_file("_ast", search_context=search_context)
	# if pathFilenameStubFile is None: raise FREAKOUT
	# astStubFile: ast.Module = ast.parse(pathFilenameStubFile.read_text())
	# Z0Z_typesSpecial(astStubFile)

	pathFilenameStubFile: Path | None = typeshed_client.finder.get_stub_file("ast", search_context=search_context)
	if pathFilenameStubFile is None: raise FREAKOUT
	astStubFile: ast.Module = ast.parse(pathFilenameStubFile.read_text())

	makeTools(astStubFile)
