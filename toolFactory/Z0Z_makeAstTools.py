import typeshed_client.finder
from toolFactory import FREAKOUT, pathTypeshed, Z0Z_typesSpecial, makeTools
from pathlib import Path
import ast

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
