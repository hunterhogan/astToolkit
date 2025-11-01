"""Tests for the _toolkitAST module using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import (
	extractClassDef, extractFunctionDef, Make, parseLogicalPath2astModule, parsePathFilename2astModule)
from pathlib import Path
from typing import Any
import ast
import pytest

class TestParseLogicalPath2astModule:
	"""Test suite for parseLogicalPath2astModule function."""

	@pytest.mark.parametrize("logicalPath", [
		"ast",
		"os.path",
		"pathlib",
	])
	def testParseLogicalPathStandardLibrary(self, logicalPath: str) -> None:
		"""Test parseLogicalPath2astModule with standard library modules using common modules."""
		resultModule = parseLogicalPath2astModule(logicalPath)

		assert resultModule is not None, f"parseLogicalPath2astModule should parse '{logicalPath}'"
		assert isinstance(resultModule, ast.Module), f"Result should be ast.Module for '{logicalPath}'"
		assert len(resultModule.body) > 0, f"Module body should not be empty for '{logicalPath}'"

	def testParseLogicalPathProjectModule(self) -> None:
		"""Test parseLogicalPath2astModule with project's own module."""
		resultModule = parseLogicalPath2astModule("astToolkit._toolkitAST")

		assert resultModule is not None, "parseLogicalPath2astModule should parse astToolkit._toolkitAST"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"
		assert len(resultModule.body) > 0, "Module body should not be empty"

		# Verify we can find the functions we know exist in _toolkitAST
		functionExtractClassDef = extractFunctionDef(resultModule, "extractClassDef")
		assert functionExtractClassDef is not None, "Should find extractClassDef function"

		functionExtractFunctionDef = extractFunctionDef(resultModule, "extractFunctionDef")
		assert functionExtractFunctionDef is not None, "Should find extractFunctionDef function"

	def testParseLogicalPathWithTypeComments(self) -> None:
		"""Test parseLogicalPath2astModule with type_comments parameter."""
		resultModule = parseLogicalPath2astModule("ast", type_comments=True)

		assert resultModule is not None, "parseLogicalPath2astModule should parse with type_comments=True"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"

