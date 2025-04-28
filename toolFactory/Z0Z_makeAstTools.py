import typeshed_client.finder
from toolFactory import FREAKOUT, pathTypeshed, Z0Z_typesSpecial
from toolFactory.astFactory import makeTools
from pathlib import Path
import ast

# TODO I think there is a way to generalize this to all antecedents using a class analogous to Grab

"""
	@staticmethod
	def isAugAssignAndTargetIs(targetPredicate: Callable[[ast.expr], TypeGuard[ast.expr] | bool]) -> Callable[[ast.AST], TypeGuard[ast.AugAssign] | bool]:
		def workhorse(node: ast.AST) -> TypeGuard[ast.AugAssign] | bool:
			return Be.AugAssign(node) and targetPredicate(DOT.target(node))
		return workhorse

findThis = Be.AnnAssign and Be.checkAttribute_target(IfThis.isName_Identifier(self.name))
"""

if __name__ == "__main__":
	search_context = typeshed_client.finder.get_search_context(typeshed=pathTypeshed if pathTypeshed.exists() else None)
	pathFilenameStubFile: Path | None = typeshed_client.finder.get_stub_file("_ast", search_context=search_context)
	if pathFilenameStubFile is None: raise FREAKOUT
	astStubFile: ast.Module = ast.parse(pathFilenameStubFile.read_text())
	Z0Z_typesSpecial(astStubFile)

	pathFilenameStubFile: Path | None = typeshed_client.finder.get_stub_file("ast", search_context=search_context)
	if pathFilenameStubFile is None: raise FREAKOUT
	astStubFile: ast.Module = ast.parse(pathFilenameStubFile.read_text())

	logicalPathInfix: str | None = None

	makeTools(astStubFile)
