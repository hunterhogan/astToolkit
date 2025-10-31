"""Tests for the _toolkitAST module using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import extractClassDef, extractFunctionDef, parseLogicalPath2astModule, parsePathFilename2astModule, Make
from pathlib import Path
from typing import Any
import ast
import pytest

class TestExtractClassDef:
	"""Test suite for extractClassDef function."""
	
	@pytest.mark.parametrize("identifierClass,shouldFind", [
		("ClassGamma", True),
		("ClassEpsilon", True),
		("ClassNonexistent", False),
	])
	def testExtractClassDefFromModule(self, identifierClass: str, shouldFind: bool, pathFilenameSampleModule: Path) -> None:
		"""Test extractClassDef with various class identifiers using sample module."""
		astModule = parsePathFilename2astModule(pathFilenameSampleModule)
		resultExtracted = extractClassDef(astModule, identifierClass)
		
		if shouldFind:
			assert resultExtracted is not None, f"extractClassDef should find class '{identifierClass}'"
			assert isinstance(resultExtracted, ast.ClassDef), f"Result should be ast.ClassDef for '{identifierClass}'"
			assert resultExtracted.name == identifierClass, f"ClassDef name should match '{identifierClass}'"
		else:
			assert resultExtracted is None, f"extractClassDef should return None for nonexistent class '{identifierClass}'"
	
	def testExtractClassDefFromSimpleAST(self) -> None:
		"""Test extractClassDef with manually constructed AST."""
		nodeClassDef = Make.ClassDef(name="ClassTheta", bases=[], body=[Make.Pass()])
		astModule = Make.Module(body=[nodeClassDef])
		
		resultExtracted = extractClassDef(astModule, "ClassTheta")
		assert resultExtracted is not None, "extractClassDef should find ClassTheta"
		assert resultExtracted.name == "ClassTheta", "ClassDef name should be ClassTheta"
	
	def testExtractClassDefWithMultipleClasses(self) -> None:
		"""Test extractClassDef when multiple classes exist."""
		listClassDefs = [
			Make.ClassDef(name="ClassIota", bases=[], body=[Make.Pass()]),
			Make.ClassDef(name="ClassKappa", bases=[], body=[Make.Pass()]),
			Make.ClassDef(name="ClassLambda", bases=[], body=[Make.Pass()]),
		]
		astModule = Make.Module(body=listClassDefs)
		
		resultExtracted = extractClassDef(astModule, "ClassKappa")
		assert resultExtracted is not None, "extractClassDef should find ClassKappa"
		assert resultExtracted.name == "ClassKappa", "ClassDef name should be ClassKappa"

class TestExtractFunctionDef:
	"""Test suite for extractFunctionDef function."""
	
	@pytest.mark.parametrize("identifierFunction,shouldFind", [
		("functionAlpha", True),
		("functionBeta", True),
		("functionNonexistent", False),
	])
	def testExtractFunctionDefFromModule(self, identifierFunction: str, shouldFind: bool, pathFilenameSampleModule: Path) -> None:
		"""Test extractFunctionDef with various function identifiers using sample module."""
		astModule = parsePathFilename2astModule(pathFilenameSampleModule)
		resultExtracted = extractFunctionDef(astModule, identifierFunction)
		
		if shouldFind:
			assert resultExtracted is not None, f"extractFunctionDef should find function '{identifierFunction}'"
			assert isinstance(resultExtracted, ast.FunctionDef), f"Result should be ast.FunctionDef for '{identifierFunction}'"
			assert resultExtracted.name == identifierFunction, f"FunctionDef name should match '{identifierFunction}'"
		else:
			assert resultExtracted is None, f"extractFunctionDef should return None for nonexistent function '{identifierFunction}'"
	
	def testExtractFunctionDefFromSimpleAST(self) -> None:
		"""Test extractFunctionDef with manually constructed AST."""
		nodeFunctionDef = Make.FunctionDef(name="functionMu", body=[Make.Pass()])
		astModule = Make.Module(body=[nodeFunctionDef])
		
		resultExtracted = extractFunctionDef(astModule, "functionMu")
		assert resultExtracted is not None, "extractFunctionDef should find functionMu"
		assert resultExtracted.name == "functionMu", "FunctionDef name should be functionMu"
	
	def testExtractFunctionDefWithMultipleFunctions(self) -> None:
		"""Test extractFunctionDef when multiple functions exist."""
		listFunctionDefs = [
			Make.FunctionDef(name="functionNu", body=[Make.Pass()]),
			Make.FunctionDef(name="functionXi", body=[Make.Pass()]),
			Make.FunctionDef(name="functionOmicron", body=[Make.Pass()]),
		]
		astModule = Make.Module(body=listFunctionDefs)
		
		resultExtracted = extractFunctionDef(astModule, "functionXi")
		assert resultExtracted is not None, "extractFunctionDef should find functionXi"
		assert resultExtracted.name == "functionXi", "FunctionDef name should be functionXi"
	
	def testExtractFunctionDefNestedInClass(self, pathFilenameSampleModule: Path) -> None:
		"""Test extractFunctionDef finding method within a class."""
		astModule = parsePathFilename2astModule(pathFilenameSampleModule)
		resultExtracted = extractFunctionDef(astModule, "methodDelta")
		
		assert resultExtracted is not None, "extractFunctionDef should find methodDelta even when nested in class"
		assert resultExtracted.name == "methodDelta", "FunctionDef name should be methodDelta"

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

class TestParsePathFilename2astModule:
	"""Test suite for parsePathFilename2astModule function."""
	
	def testParsePathFilenameSampleModule(self, pathFilenameSampleModule: Path) -> None:
		"""Test parsePathFilename2astModule with sample module file."""
		resultModule = parsePathFilename2astModule(pathFilenameSampleModule)
		
		assert resultModule is not None, "parsePathFilename2astModule should parse sample module"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"
		assert len(resultModule.body) > 0, "Module body should not be empty"
		
		# Verify we can extract expected functions and classes
		functionAlpha = extractFunctionDef(resultModule, "functionAlpha")
		assert functionAlpha is not None, "Should find functionAlpha"
		
		classGamma = extractClassDef(resultModule, "ClassGamma")
		assert classGamma is not None, "Should find ClassGamma"
	
	def testParsePathFilenameWithPathLike(self, pathFilenameSampleModule: Path) -> None:
		"""Test parsePathFilename2astModule accepts PathLike objects."""
		resultModule = parsePathFilename2astModule(pathFilenameSampleModule)
		
		assert resultModule is not None, "parsePathFilename2astModule should accept Path objects"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"
	
	def testParsePathFilenameWithStringPath(self, pathFilenameSampleModule: Path) -> None:
		"""Test parsePathFilename2astModule accepts string paths."""
		pathAsString = str(pathFilenameSampleModule)
		resultModule = parsePathFilename2astModule(pathAsString)
		
		assert resultModule is not None, "parsePathFilename2astModule should accept string paths"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"
	
	def testParsePathFilenameWithTypeComments(self, pathFilenameSampleModule: Path) -> None:
		"""Test parsePathFilename2astModule with type_comments parameter."""
		resultModule = parsePathFilename2astModule(pathFilenameSampleModule, type_comments=True)
		
		assert resultModule is not None, "parsePathFilename2astModule should parse with type_comments=True"
		assert isinstance(resultModule, ast.Module), "Result should be ast.Module"

class TestIntegrationScenarios:
	"""Test suite for integration scenarios combining multiple functions."""
	
	def testParseAndExtractFunctionFromLogicalPath(self) -> None:
		"""Test parsing a module by logical path and extracting a function."""
		resultModule = parseLogicalPath2astModule("astToolkit._toolkitAST")
		functionExtracted = extractFunctionDef(resultModule, "parsePathFilename2astModule")
		
		assert functionExtracted is not None, "Should extract parsePathFilename2astModule function"
		assert functionExtracted.name == "parsePathFilename2astModule", "Function name should match"
	
	def testParseAndExtractClassFromFile(self, pathFilenameSampleModule: Path) -> None:
		"""Test parsing a file and extracting a class."""
		resultModule = parsePathFilename2astModule(pathFilenameSampleModule)
		classExtracted = extractClassDef(resultModule, "ClassGamma")
		
		assert classExtracted is not None, "Should extract ClassGamma"
		assert classExtracted.name == "ClassGamma", "Class name should match"
		assert len(classExtracted.body) > 0, "Class should have body"
	
	def testExtractMultipleItemsFromSameModule(self, pathFilenameSampleModule: Path) -> None:
		"""Test extracting multiple functions and classes from same module."""
		resultModule = parsePathFilename2astModule(pathFilenameSampleModule)
		
		functionAlpha = extractFunctionDef(resultModule, "functionAlpha")
		functionBeta = extractFunctionDef(resultModule, "functionBeta")
		classGamma = extractClassDef(resultModule, "ClassGamma")
		classEpsilon = extractClassDef(resultModule, "ClassEpsilon")
		
		assert functionAlpha is not None, "Should find functionAlpha"
		assert functionBeta is not None, "Should find functionBeta"
		assert classGamma is not None, "Should find ClassGamma"
		assert classEpsilon is not None, "Should find ClassEpsilon"
		
		# Verify all have correct names
		assert functionAlpha.name == "functionAlpha"
		assert functionBeta.name == "functionBeta"
		assert classGamma.name == "ClassGamma"
		assert classEpsilon.name == "ClassEpsilon"
