"""Tests for the _toolkitAST module using parametrized tests and DRY principles."""
from __future__ import annotations

from astToolkit.filesystem import parseLogicalPath2astModule
import ast
import pytest

@pytest.mark.parametrize("logicalPath", ["ast", "os.path", "pathlib"])
def testParseLogicalPathStandardLibrary(logicalPath: str) -> None:
	"""Test parseLogicalPath2astModule with standard library modules using common modules."""
	resultModule = parseLogicalPath2astModule(logicalPath)

	assert resultModule is not None, f"parseLogicalPath2astModule should parse '{logicalPath}'"
	assert isinstance(resultModule, ast.Module), f"Result should be ast.Module for '{logicalPath}'"
	assert len(resultModule.body) > 0, f"Module body should not be empty for '{logicalPath}'"

def testParseLogicalPathWithTypeComments() -> None:
	"""Test parseLogicalPath2astModule with type_comments parameter."""
	resultModule = parseLogicalPath2astModule("ast", type_comments=True)

	assert resultModule is not None, "parseLogicalPath2astModule should parse with type_comments=True"
	assert isinstance(resultModule, ast.Module), "Result should be ast.Module"
