"""Tests for transformationTools module using parametrized tests and DRY principles."""
from __future__ import annotations

from astToolkit import Make
from astToolkit.changeDef import (
	inlineFunctionDef, makeDictionaryAsyncFunctionDef, makeDictionaryClassDef, makeDictionaryFunctionDef, makeDictionaryMosDef,
	removeUnusedParameters)
from astToolkit.filesystem import write_astModule
from astToolkit.transformationTools import pythonCode2ast_expr, unjoinBinOP, unparseFindReplace
from copy import deepcopy
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
import ast
import pytest

@pytest.mark.parametrize(
	'identifierFunction,valueExpected', [('functionPrimary', True), ('functionSecondary', True), ('functionTertiary', False)]
)
def testMakeDictionaryFunctionDef(identifierFunction: str, valueExpected: bool, moduleSampleFunctions: ast.Module) -> None:
	"""Test makeDictionaryFunctionDef extracts function definitions correctly."""
	dictionaryResult = makeDictionaryFunctionDef(moduleSampleFunctions)

	assert (identifierFunction in dictionaryResult) is valueExpected, (
		f'makeDictionaryFunctionDef: {identifierFunction} should {"be" if valueExpected else "not be"} in result'
	)

	if valueExpected:
		assert isinstance(dictionaryResult[identifierFunction], ast.FunctionDef), (
			f'makeDictionaryFunctionDef: value for {identifierFunction} should be ast.FunctionDef'
		)

@pytest.mark.parametrize('identifierClass,valueExpected', [('ClassAlpha', True), ('ClassBeta', True), ('ClassGamma', False)])
def testMakeDictionaryClassDef(identifierClass: str, valueExpected: bool, moduleSampleClasses: ast.Module) -> None:
	"""Test makeDictionaryClassDef extracts class definitions correctly."""
	dictionaryResult = makeDictionaryClassDef(moduleSampleClasses)

	assert (identifierClass in dictionaryResult) is valueExpected, (
		f'makeDictionaryClassDef: {identifierClass} should {"be" if valueExpected else "not be"} in result'
	)

	if valueExpected:
		assert isinstance(dictionaryResult[identifierClass], ast.ClassDef), (
			f'makeDictionaryClassDef: value for {identifierClass} should be ast.ClassDef'
		)

@pytest.mark.parametrize(
	'identifierAsync,valueExpected', [('asyncFunctionNorth', True), ('asyncFunctionSouth', True), ('asyncFunctionEast', False)]
)
def testMakeDictionaryAsyncFunctionDef(identifierAsync: str, valueExpected: bool, moduleSampleAsyncFunctions: ast.Module) -> None:
	"""Test makeDictionaryAsyncFunctionDef extracts async function definitions correctly."""
	dictionaryResult = makeDictionaryAsyncFunctionDef(moduleSampleAsyncFunctions)

	assert (identifierAsync in dictionaryResult) is valueExpected, (
		f'makeDictionaryAsyncFunctionDef: {identifierAsync} should {"be" if valueExpected else "not be"} in result'
	)

	if valueExpected:
		assert isinstance(dictionaryResult[identifierAsync], ast.AsyncFunctionDef), (
			f'makeDictionaryAsyncFunctionDef: value for {identifierAsync} should be ast.AsyncFunctionDef'
		)

def testMakeDictionaryMosDef(moduleSampleMixed: ast.Module) -> None:
	"""Test makeDictionaryMosDef extracts all definition types correctly."""
	dictionaryResult = makeDictionaryMosDef(moduleSampleMixed)

	# Should contain async functions
	assert 'asyncFunctionPrimary' in dictionaryResult, 'makeDictionaryMosDef: should contain async function'
	assert isinstance(dictionaryResult['asyncFunctionPrimary'], ast.AsyncFunctionDef), (
		'makeDictionaryMosDef: async function should be ast.AsyncFunctionDef'
	)

	# Should contain classes
	assert 'ClassPrimary' in dictionaryResult, 'makeDictionaryMosDef: should contain class'
	assert isinstance(dictionaryResult['ClassPrimary'], ast.ClassDef), 'makeDictionaryMosDef: class should be ast.ClassDef'

	# Should contain functions
	assert 'functionPrimary' in dictionaryResult, 'makeDictionaryMosDef: should contain function'
	assert isinstance(dictionaryResult['functionPrimary'], ast.FunctionDef), 'makeDictionaryMosDef: function should be ast.FunctionDef'

def testInlineFunctionDefBasicInlining(moduleInliningBasic: ast.Module) -> None:
	"""Test inlineFunctionDef performs basic function inlining."""
	resultFunctionDef = inlineFunctionDef('functionTarget', moduleInliningBasic)

	assert isinstance(resultFunctionDef, ast.FunctionDef), 'inlineFunctionDef: should return ast.FunctionDef'
	assert resultFunctionDef.name == 'functionTarget', 'inlineFunctionDef: should preserve function name'

	# Check that function has been modified (body should contain inlined logic)
	assert len(resultFunctionDef.body) > 0, 'inlineFunctionDef: should have function body'

def testInlineFunctionDefMissingIdentifier(moduleSampleFunctions: ast.Module) -> None:
	"""Test inlineFunctionDef raises ValueError for missing identifier."""
	with pytest.raises(ValueError, match='unable to find'):
		inlineFunctionDef('functionNonexistent', moduleSampleFunctions)

def testInlineFunctionDefNoInliningNeeded(moduleInliningNone: ast.Module) -> None:
	"""Test inlineFunctionDef with function that needs no inlining."""
	resultFunctionDef = inlineFunctionDef('functionStandalone', moduleInliningNone)

	assert isinstance(resultFunctionDef, ast.FunctionDef), 'inlineFunctionDef: should return ast.FunctionDef'
	assert resultFunctionDef.name == 'functionStandalone', 'inlineFunctionDef: should preserve function name'

@pytest.mark.parametrize(
	'stringCode,expectedType',
	[
		('233', ast.Constant),  # Fibonacci number
		('variableNorth', ast.Name),
		('objectPrimary.methodSecondary', ast.Attribute),
		('listItems[13]', ast.Subscript),  # Fibonacci index
		('functionCall()', ast.Call),
	],
)
def testPythonCode2ASTExprVariousExpressions(stringCode: str, expectedType: type[ast.expr]) -> None:
	"""Test pythonCode2ast_expr converts various expressions correctly."""
	resultExpr = pythonCode2ast_expr(stringCode)

	assert isinstance(resultExpr, ast.expr), f"pythonCode2ast_expr: should return ast.expr for '{stringCode}'"
	assert isinstance(resultExpr, expectedType), f"pythonCode2ast_expr: '{stringCode}' should produce {expectedType.__name__}"

def testRemoveUnusedParametersBasicRemoval(functionDefUnusedParameters: ast.FunctionDef) -> None:
	"""Test removeUnusedParameters removes unused parameters correctly."""
	resultFunctionDef = removeUnusedParameters(functionDefUnusedParameters)

	assert isinstance(resultFunctionDef, ast.FunctionDef), 'removeUnusedParameters: should return ast.FunctionDef'

	# Check that unused parameters are removed
	listParameterNames = [argItem.arg for argItem in resultFunctionDef.args.args]
	assert 'parameterUnused' not in listParameterNames, 'removeUnusedParameters: should remove unused parameter'

def testRemoveUnusedParametersReturnUpdated(functionDefUnusedParameters: ast.FunctionDef) -> None:
	"""Test removeUnusedParameters updates return statements correctly."""
	resultFunctionDef = removeUnusedParameters(functionDefUnusedParameters)

	# Check that return statement is updated to tuple
	codeUnparsed = ast.unparse(resultFunctionDef)
	assert 'return' in codeUnparsed, 'removeUnusedParameters: should have return statement'

def testRemoveUnusedParametersAllUsed(functionDefAllParametersUsed: ast.FunctionDef) -> None:
	"""Test removeUnusedParameters with all parameters used."""
	resultFunctionDef = removeUnusedParameters(functionDefAllParametersUsed)

	assert isinstance(resultFunctionDef, ast.FunctionDef), 'removeUnusedParameters: should return ast.FunctionDef'

	# All parameters should still be present
	countParametersOriginal = len(functionDefAllParametersUsed.args.args)
	countParametersResult = len(resultFunctionDef.args.args)
	assert countParametersResult == countParametersOriginal, 'removeUnusedParameters: should preserve all used parameters'

@pytest.mark.parametrize('operatorType,countExpected', [(ast.Add, 3), (ast.operator, 3), (ast.Mult, 0)])
def testUnjoinBinOPBasicOperation(operatorType: type[ast.operator], countExpected: int, binOpChained: ast.BinOp) -> None:
	"""Test unjoinBinOP extracts expressions from binary operations."""
	listExpressions = unjoinBinOP(binOpChained) if operatorType is ast.operator else unjoinBinOP(binOpChained, operatorType)

	assert isinstance(listExpressions, list), f'unjoinBinOP: should return list for {operatorType.__name__}'
	assert len(listExpressions) == countExpected, (
		f'unjoinBinOP: should extract exactly {countExpected} expressions for {operatorType.__name__}'
	)
	expected: list[ast.expr] = [Make.Constant(233), Make.Constant(89), Make.Constant(144)] if countExpected else []
	assert all(map(ast.compare, listExpressions, expected, strict=True))

@pytest.mark.parametrize('astAST,operator,expected', [
	pytest.param(Make.Constant(89), ast.operator, [], id='constant'),
	pytest.param(Make.Name('north'), ast.Add, [], id='name'),
	pytest.param(Make.Module([]), ast.Add, [], id='empty-module'),
	pytest.param(Make.Add(), ast.Add, [], id='operator-node'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('east')]), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='two-operands'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='left-nested'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='right-nested'),
	pytest.param(Make.Add.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='both-branches'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('north'), Make.Name('east')]), ast.Add,
		[Make.Name('north'), Make.Name('north'), Make.Name('east')], id='repeated-operands'),
	pytest.param(Make.Add.join([
		Make.Mult.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]),
		Make.Name('west')]), ast.Add,
		[Make.Mult.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]),
			Make.Name('west')], id='different-left-operator'),
	pytest.param(Make.Add.join([
		Make.Name('north'),
		Make.Mult.join([Make.Add.join([Make.Name('east'), Make.Name('south')]), Make.Name('west')])]), ast.Add,
		[Make.Name('north'),
			Make.Mult.join([Make.Add.join([Make.Name('east'), Make.Name('south')]), Make.Name('west')])], id='different-right-operator'),
	pytest.param(Make.Add.join([
		Make.Mult.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')]), ast.operator,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='all-operators'),
	pytest.param(Make.Sub.join([Make.Name('north'), Make.Sub.join([Make.Name('east'), Make.Name('south')])]), ast.Sub,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='noncommutative-order'),
	pytest.param(Make.Mult.join([Make.Name('north'), Make.Name('east')]), ast.Add,
		[], id='no-matching-operator'),
	pytest.param(Make.Mult.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')]), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='search-inside-unmatched-root'),
	pytest.param(Make.Add.join([
		Make.Call(Make.Name('combine'), [Make.Add.join([Make.Name('north'), Make.Name('east')])]),
		Make.Name('south')]), ast.Add,
		[Make.Call(Make.Name('combine'), [Make.Add.join([Make.Name('north'), Make.Name('east')])]),
			Make.Name('south')], id='complete-call-operand'),
	pytest.param(Make.BitOr.join([
		Make.Subscript(Make.Name('list'), Make.BitOr.join([Make.Name('int'), Make.Name('str')])),
		Make.Constant(None)]), ast.BitOr,
		[Make.Subscript(Make.Name('list'), Make.BitOr.join([Make.Name('int'), Make.Name('str')])),
			Make.Constant(None)], id='nested-type-union'),
	pytest.param(Make.BitOr.join([
		Make.Attribute(Make.Name('ast'), 'expr'),
		Make.Subscript(Make.Name('list'), Make.Attribute(Make.Name('ast'), 'expr')),
		Make.Constant(None)]), ast.BitOr,
		[Make.Attribute(Make.Name('ast'), 'expr'), Make.Subscript(Make.Name('list'), Make.Attribute(Make.Name('ast'), 'expr')),
			Make.Constant(None)], id='factory-type-union'),
	pytest.param(Make.Module([
		Make.Expr(Make.Add.join([Make.Name('north'), Make.Name('east')])),
		Make.Expr(Make.Constant(89)),
		Make.Expr(Make.Add.join([Make.Name('south'), Make.Name('west')]))]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='separate-operations'),
	pytest.param(Make.Add.join([Make.Name('north')] * 3), ast.Add,
		[Make.Name('north'), Make.Name('north'), Make.Name('north')], id='shared-operand'),
	pytest.param(Make.Add.join([Make.Add.join([Make.Name('north'), Make.Name('east')])] * 2), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('north'), Make.Name('east')], id='shared-subtree'),
	pytest.param(Make.Add.join([
		Make.UnaryOp(Make.USub(), Make.Add.join([Make.Name('north'), Make.Name('east')])),
		Make.Name('south')]), ast.Add,
		[Make.UnaryOp(Make.USub(), Make.Add.join([Make.Name('north'), Make.Name('east')])),
			Make.Name('south')], id='complete-unary-operand'),
	pytest.param(Make.Add.join([
		Make.IfExp(Make.Name('ready'), Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')),
		Make.Name('west')]), ast.Add,
		[Make.IfExp(Make.Name('ready'), Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')),
			Make.Name('west')], id='complete-conditional-operand'),
	pytest.param(Make.Expression(Make.Add.join([Make.Name('north'), Make.Name('east')])), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='expression-root'),
	pytest.param(Make.Call(Make.Name('combine'), [
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='separate-call-arguments'),
	pytest.param(Make.Mult.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='search-both-unmatched-branches'),
	pytest.param(Make.Pow.join([Make.Name('north'), Make.Pow.join([Make.Name('east'), Make.Name('south')])]), ast.Pow,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='nested-power'),
	pytest.param(Make.FloorDiv.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.FloorDiv,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='floor-division'),
	pytest.param(Make.BitXor.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.BitXor,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='bitwise-xor'),
])
def testUnjoinBinOPSingleExpression(astAST: ast.AST, operator: type[ast.operator], expected: list[ast.expr]) -> None:
	"""Check operand structure, order, identity, and preservation of the input AST.

	(AI generated docstring)
	"""
	structure: ast.AST = deepcopy(astAST)
	identities: set[int] = set(map(id, ast.walk(astAST)))
	listExpressions = unjoinBinOP(astAST, operator)

	assert isinstance(listExpressions, list), 'unjoinBinOP: should return list for single expression'
	assert len(listExpressions) == len(expected)
	assert all(map(ast.compare, listExpressions, expected, strict=True))
	assert set(map(id, listExpressions)) <= identities
	assert set(map(id, ast.walk(astAST))) == identities
	assert ast.compare(astAST, structure, compare_attributes=True)

def testUnparseFindReplaceBasicReplacement() -> None:
	"""Test unparseFindReplace performs basic node replacement."""
	treeOriginal = Make.Module(
		[
			Make.Assign(
				targets=[Make.Name('variableAlpha', context=Make.Store())],
				value=Make.Constant(233),  # Fibonacci number
			)
		]
	)
	ast.fix_missing_locations(treeOriginal)

	mappingReplacements: dict[ast.AST, ast.AST] = {
		Make.Constant(233): Make.Constant(89)  # Different Fibonacci numbers
	}

	treeResult = unparseFindReplace(treeOriginal, mappingReplacements)

	assert isinstance(treeResult, ast.Module), 'unparseFindReplace: should return ast.Module'

	codeUnparsed = ast.unparse(treeResult)
	assert '89' in codeUnparsed, 'unparseFindReplace: should replace value with new value'
	assert '233' not in codeUnparsed, 'unparseFindReplace: should not contain old value'

def testUnparseFindReplaceNoReplacements() -> None:
	"""Test unparseFindReplace with no matching replacements."""
	treeOriginal = Make.Module(
		[
			Make.Assign(
				targets=[Make.Name('variableBeta', context=Make.Store())],
				value=Make.Constant(377),  # Fibonacci number
			)
		]
	)
	ast.fix_missing_locations(treeOriginal)

	mappingReplacements: dict[ast.AST, ast.AST] = {Make.Constant(233): Make.Constant(89)}

	treeResult = unparseFindReplace(treeOriginal, mappingReplacements)

	assert isinstance(treeResult, ast.Module), 'unparseFindReplace: should return ast.Module'

	codeUnparsed = ast.unparse(treeResult)
	assert '377' in codeUnparsed, 'unparseFindReplace: should preserve original value when no match'

def testWriteASTModuleToFile(moduleSampleSimple: ast.Module) -> None:
	"""Test write_astModule writes module to file correctly."""
	with TemporaryDirectory() as pathTemporary:
		pathFilename = Path(pathTemporary) / 'outputModule.py'

		write_astModule(moduleSampleSimple, pathFilename)

		assert pathFilename.exists(), 'write_astModule: should create output file'

		contentFile = pathFilename.read_text()
		assert len(contentFile) > 0, 'write_astModule: should write non-empty content'
		assert 'def ' in contentFile or 'class ' in contentFile, 'write_astModule: should contain Python code'

def testWriteASTModuleToStringIO(moduleSampleSimple: ast.Module) -> None:
	"""Test write_astModule writes module to StringIO correctly."""
	streamOutput = StringIO()

	write_astModule(moduleSampleSimple, streamOutput)

	contentStream = streamOutput.getvalue()
	assert len(contentStream) > 0, 'write_astModule: should write non-empty content to stream'
	assert 'def ' in contentStream or 'class ' in contentStream, 'write_astModule: should contain Python code in stream'

def testWriteASTModuleWithSettings(moduleSampleSimple: ast.Module) -> None:
	"""Test write_astModule with custom settings."""
	with TemporaryDirectory() as pathTemporary:
		pathFilename = Path(pathTemporary) / 'outputModuleWithSettings.py'

		settingsCustom: dict[str, dict[str, Any]] = {'autoflake': {'additional_imports': ['astToolkit']}}

		write_astModule(moduleSampleSimple, pathFilename, settingsCustom)

		assert pathFilename.exists(), 'write_astModule: should create output file with settings'

def testWriteASTModuleWithPackageIdentifier(moduleSampleSimple: ast.Module) -> None:
	"""Test write_astModule with package identifier."""
	with TemporaryDirectory() as pathTemporary:
		pathFilename = Path(pathTemporary) / 'outputModuleWithPackage.py'

		write_astModule(moduleSampleSimple, pathFilename, identifierPackage='astToolkit')

		assert pathFilename.exists(), 'write_astModule: should create output file with package identifier'
