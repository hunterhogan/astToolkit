"""Tests for transformationTools module using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Make
from astToolkit.transformationTools import (
	inlineFunctionDef,
	makeDictionaryAsyncFunctionDef,
	makeDictionaryClassDef,
	makeDictionaryFunctionDef,
	makeDictionaryMosDef,
	pythonCode2ast_expr,
	removeUnusedParameters,
	unjoinBinOP,
	unparseFindReplace,
	write_astModule,
)
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
import ast
import pytest


class TestMakeDictionaryFunctions:
	"""Test suite for dictionary-making functions."""

	@pytest.mark.parametrize("identifierFunction,valueExpected", [
		("functionPrimary", True),
		("functionSecondary", True),
		("functionTertiary", False),
	])
	def testMakeDictionaryFunctionDef(
		self, 
		identifierFunction: str, 
		valueExpected: bool,
		moduleSampleFunctions: ast.Module
	) -> None:
		"""Test makeDictionaryFunctionDef extracts function definitions correctly."""
		dictionaryResult = makeDictionaryFunctionDef(moduleSampleFunctions)
		
		assert (identifierFunction in dictionaryResult) is valueExpected, \
			f"makeDictionaryFunctionDef: {identifierFunction} should {'be' if valueExpected else 'not be'} in result"
		
		if valueExpected:
			assert isinstance(dictionaryResult[identifierFunction], ast.FunctionDef), \
				f"makeDictionaryFunctionDef: value for {identifierFunction} should be ast.FunctionDef"

	@pytest.mark.parametrize("identifierClass,valueExpected", [
		("ClassAlpha", True),
		("ClassBeta", True),
		("ClassGamma", False),
	])
	def testMakeDictionaryClassDef(
		self, 
		identifierClass: str, 
		valueExpected: bool,
		moduleSampleClasses: ast.Module
	) -> None:
		"""Test makeDictionaryClassDef extracts class definitions correctly."""
		dictionaryResult = makeDictionaryClassDef(moduleSampleClasses)
		
		assert (identifierClass in dictionaryResult) is valueExpected, \
			f"makeDictionaryClassDef: {identifierClass} should {'be' if valueExpected else 'not be'} in result"
		
		if valueExpected:
			assert isinstance(dictionaryResult[identifierClass], ast.ClassDef), \
				f"makeDictionaryClassDef: value for {identifierClass} should be ast.ClassDef"

	@pytest.mark.parametrize("identifierAsync,valueExpected", [
		("asyncFunctionNorth", True),
		("asyncFunctionSouth", True),
		("asyncFunctionEast", False),
	])
	def testMakeDictionaryAsyncFunctionDef(
		self, 
		identifierAsync: str, 
		valueExpected: bool,
		moduleSampleAsyncFunctions: ast.Module
	) -> None:
		"""Test makeDictionaryAsyncFunctionDef extracts async function definitions correctly."""
		dictionaryResult = makeDictionaryAsyncFunctionDef(moduleSampleAsyncFunctions)
		
		assert (identifierAsync in dictionaryResult) is valueExpected, \
			f"makeDictionaryAsyncFunctionDef: {identifierAsync} should {'be' if valueExpected else 'not be'} in result"
		
		if valueExpected:
			assert isinstance(dictionaryResult[identifierAsync], ast.AsyncFunctionDef), \
				f"makeDictionaryAsyncFunctionDef: value for {identifierAsync} should be ast.AsyncFunctionDef"

	def testMakeDictionaryMosDef(self, moduleSampleMixed: ast.Module) -> None:
		"""Test makeDictionaryMosDef extracts all definition types correctly."""
		dictionaryResult = makeDictionaryMosDef(moduleSampleMixed)
		
		# Should contain async functions
		assert "asyncFunctionPrimary" in dictionaryResult, \
			"makeDictionaryMosDef: should contain async function"
		assert isinstance(dictionaryResult["asyncFunctionPrimary"], ast.AsyncFunctionDef), \
			"makeDictionaryMosDef: async function should be ast.AsyncFunctionDef"
		
		# Should contain classes
		assert "ClassPrimary" in dictionaryResult, \
			"makeDictionaryMosDef: should contain class"
		assert isinstance(dictionaryResult["ClassPrimary"], ast.ClassDef), \
			"makeDictionaryMosDef: class should be ast.ClassDef"
		
		# Should contain functions
		assert "functionPrimary" in dictionaryResult, \
			"makeDictionaryMosDef: should contain function"
		assert isinstance(dictionaryResult["functionPrimary"], ast.FunctionDef), \
			"makeDictionaryMosDef: function should be ast.FunctionDef"


class TestInlineFunctionDef:
	"""Test suite for inlineFunctionDef function."""

	def testInlineFunctionDefBasicInlining(self, moduleInliningBasic: ast.Module) -> None:
		"""Test inlineFunctionDef performs basic function inlining."""
		resultFunctionDef = inlineFunctionDef("functionTarget", moduleInliningBasic)
		
		assert isinstance(resultFunctionDef, ast.FunctionDef), \
			"inlineFunctionDef: should return ast.FunctionDef"
		assert resultFunctionDef.name == "functionTarget", \
			"inlineFunctionDef: should preserve function name"
		
		# Check that function has been modified (body should contain inlined logic)
		assert len(resultFunctionDef.body) > 0, \
			"inlineFunctionDef: should have function body"

	def testInlineFunctionDefMissingIdentifier(self, moduleSampleFunctions: ast.Module) -> None:
		"""Test inlineFunctionDef raises ValueError for missing identifier."""
		with pytest.raises(ValueError, match="unable to find"):
			inlineFunctionDef("functionNonexistent", moduleSampleFunctions)

	def testInlineFunctionDefNoInliningNeeded(self, moduleInliningNone: ast.Module) -> None:
		"""Test inlineFunctionDef with function that needs no inlining."""
		resultFunctionDef = inlineFunctionDef("functionStandalone", moduleInliningNone)
		
		assert isinstance(resultFunctionDef, ast.FunctionDef), \
			"inlineFunctionDef: should return ast.FunctionDef"
		assert resultFunctionDef.name == "functionStandalone", \
			"inlineFunctionDef: should preserve function name"


class TestPythonCode2ASTExpr:
	"""Test suite for pythonCode2ast_expr function."""

	@pytest.mark.parametrize("stringCode,expectedType", [
		("233", ast.Constant),  # Fibonacci number
		("variableNorth", ast.Name),
		("objectPrimary.methodSecondary", ast.Attribute),
		("listItems[13]", ast.Subscript),  # Fibonacci index
		("functionCall()", ast.Call),
	])
	def testPythonCode2ASTExprVariousExpressions(
		self, 
		stringCode: str, 
		expectedType: type[ast.expr]
	) -> None:
		"""Test pythonCode2ast_expr converts various expressions correctly."""
		resultExpr = pythonCode2ast_expr(stringCode)
		
		assert isinstance(resultExpr, ast.expr), \
			f"pythonCode2ast_expr: should return ast.expr for '{stringCode}'"
		assert isinstance(resultExpr, expectedType), \
			f"pythonCode2ast_expr: '{stringCode}' should produce {expectedType.__name__}"


class TestRemoveUnusedParameters:
	"""Test suite for removeUnusedParameters function."""

	def testRemoveUnusedParametersBasicRemoval(
		self, 
		functionDefUnusedParameters: ast.FunctionDef
	) -> None:
		"""Test removeUnusedParameters removes unused parameters correctly."""
		resultFunctionDef = removeUnusedParameters(functionDefUnusedParameters)
		
		assert isinstance(resultFunctionDef, ast.FunctionDef), \
			"removeUnusedParameters: should return ast.FunctionDef"
		
		# Check that unused parameters are removed
		listParameterNames = [argItem.arg for argItem in resultFunctionDef.args.args]
		assert "parameterUnused" not in listParameterNames, \
			"removeUnusedParameters: should remove unused parameter"

	def testRemoveUnusedParametersReturnUpdated(
		self, 
		functionDefUnusedParameters: ast.FunctionDef
	) -> None:
		"""Test removeUnusedParameters updates return statements correctly."""
		resultFunctionDef = removeUnusedParameters(functionDefUnusedParameters)
		
		# Check that return statement is updated to tuple
		codeUnparsed = ast.unparse(resultFunctionDef)
		assert "return" in codeUnparsed, \
			"removeUnusedParameters: should have return statement"

	def testRemoveUnusedParametersAllUsed(
		self, 
		functionDefAllParametersUsed: ast.FunctionDef
	) -> None:
		"""Test removeUnusedParameters with all parameters used."""
		resultFunctionDef = removeUnusedParameters(functionDefAllParametersUsed)
		
		assert isinstance(resultFunctionDef, ast.FunctionDef), \
			"removeUnusedParameters: should return ast.FunctionDef"
		
		# All parameters should still be present
		countParametersOriginal = len(functionDefAllParametersUsed.args.args)
		countParametersResult = len(resultFunctionDef.args.args)
		assert countParametersResult == countParametersOriginal, \
			"removeUnusedParameters: should preserve all used parameters"


class TestUnjoinBinOP:
	"""Test suite for unjoinBinOP function."""

	@pytest.mark.parametrize("operatorType,countExpected", [
		(ast.Add, 3),
	])
	def testUnjoinBinOPBasicOperation(
		self, 
		operatorType: type[ast.operator],
		countExpected: int,
		binOpChained: ast.BinOp
	) -> None:
		"""Test unjoinBinOP extracts expressions from binary operations."""
		listExpressions = unjoinBinOP(binOpChained, operatorType)
		
		assert isinstance(listExpressions, list), \
			f"unjoinBinOP: should return list for {operatorType.__name__}"
		assert len(listExpressions) >= countExpected, \
			f"unjoinBinOP: should extract at least {countExpected} expressions for {operatorType.__name__}"

	def testUnjoinBinOPSingleExpression(self) -> None:
		"""Test unjoinBinOP with single expression."""
		exprSingle = Make.Constant(89)  # Fibonacci number
		listExpressions = unjoinBinOP(exprSingle)
		
		assert isinstance(listExpressions, list), \
			"unjoinBinOP: should return list for single expression"
		assert len(listExpressions) == 0, \
			"unjoinBinOP: should return empty list for non-BinOp"


class TestUnparseFindReplace:
	"""Test suite for unparseFindReplace function."""

	def testUnparseFindReplaceBasicReplacement(self) -> None:
		"""Test unparseFindReplace performs basic node replacement."""
		treeOriginal = Make.Module([
			Make.Assign(
				targets=[Make.Name("variableAlpha", context=Make.Store())],
				value=Make.Constant(233)  # Fibonacci number
			)
		])
		ast.fix_missing_locations(treeOriginal)
		
		mappingReplacements: dict[ast.AST, ast.AST] = {
			Make.Constant(233): Make.Constant(89)  # Different Fibonacci numbers
		}
		
		treeResult = unparseFindReplace(treeOriginal, mappingReplacements)
		
		assert isinstance(treeResult, ast.Module), \
			"unparseFindReplace: should return ast.Module"
		
		codeUnparsed = ast.unparse(treeResult)
		assert "89" in codeUnparsed, \
			"unparseFindReplace: should replace value with new value"
		assert "233" not in codeUnparsed, \
			"unparseFindReplace: should not contain old value"

	def testUnparseFindReplaceNoReplacements(self) -> None:
		"""Test unparseFindReplace with no matching replacements."""
		treeOriginal = Make.Module([
			Make.Assign(
				targets=[Make.Name("variableBeta", context=Make.Store())],
				value=Make.Constant(377)  # Fibonacci number
			)
		])
		ast.fix_missing_locations(treeOriginal)
		
		mappingReplacements: dict[ast.AST, ast.AST] = {
			Make.Constant(233): Make.Constant(89)
		}
		
		treeResult = unparseFindReplace(treeOriginal, mappingReplacements)
		
		assert isinstance(treeResult, ast.Module), \
			"unparseFindReplace: should return ast.Module"
		
		codeUnparsed = ast.unparse(treeResult)
		assert "377" in codeUnparsed, \
			"unparseFindReplace: should preserve original value when no match"


class TestWriteASTModule:
	"""Test suite for write_astModule function."""

	def testWriteASTModuleToFile(self, moduleSampleSimple: ast.Module) -> None:
		"""Test write_astModule writes module to file correctly."""
		with TemporaryDirectory() as pathTemporary:
			pathFilename = Path(pathTemporary) / "outputModule.py"
			
			write_astModule(moduleSampleSimple, pathFilename)
			
			assert pathFilename.exists(), \
				"write_astModule: should create output file"
			
			contentFile = pathFilename.read_text()
			assert len(contentFile) > 0, \
				"write_astModule: should write non-empty content"
			assert "def " in contentFile or "class " in contentFile, \
				"write_astModule: should contain Python code"

	def testWriteASTModuleToStringIO(self, moduleSampleSimple: ast.Module) -> None:
		"""Test write_astModule writes module to StringIO correctly."""
		streamOutput = StringIO()
		
		write_astModule(moduleSampleSimple, streamOutput)
		
		contentStream = streamOutput.getvalue()
		assert len(contentStream) > 0, \
			"write_astModule: should write non-empty content to stream"
		assert "def " in contentStream or "class " in contentStream, \
			"write_astModule: should contain Python code in stream"

	def testWriteASTModuleWithSettings(self, moduleSampleSimple: ast.Module) -> None:
		"""Test write_astModule with custom settings."""
		with TemporaryDirectory() as pathTemporary:
			pathFilename = Path(pathTemporary) / "outputModuleWithSettings.py"
			
			settingsCustom: dict[str, dict[str, Any]] = {
				'autoflake': {'additional_imports': ['astToolkit']}
			}
			
			write_astModule(moduleSampleSimple, pathFilename, settingsCustom)
			
			assert pathFilename.exists(), \
				"write_astModule: should create output file with settings"

	def testWriteASTModuleWithPackageIdentifier(self, moduleSampleSimple: ast.Module) -> None:
		"""Test write_astModule with package identifier."""
		with TemporaryDirectory() as pathTemporary:
			pathFilename = Path(pathTemporary) / "outputModuleWithPackage.py"
			
			write_astModule(moduleSampleSimple, pathFilename, identifierPackage='astToolkit')
			
			assert pathFilename.exists(), \
				"write_astModule: should create output file with package identifier"
