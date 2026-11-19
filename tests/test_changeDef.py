"""Expected values and exceptions are hand-derived from the `changeDef` docstrings."""
from __future__ import annotations

from astToolkit import Make
from astToolkit.changeDef import (
	inlineFunctionDef, makeDictionaryAsyncFunctionDef, makeDictionaryClassDef, makeDictionaryFunctionDef, makeDictionaryMosDef,
	removeUnusedParameters)
from tests import assertComparable, assertEqualTo, messageTestFailure
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from hunterMakesPy import CallableFunction
	import ast

markDefectFirstDefinitionWins: pytest.MarkDecorator = pytest.mark.xfail(
	strict=True, reason='`Then.updateKeyValueIn` stores with `setdefault`, so the first definition of a repeated name wins.')

FunctionDefNorth: ast.FunctionDef = Make.FunctionDef(name='north', body=[Make.Return(Make.Constant(2))])
FunctionDefNorthRepeated: ast.FunctionDef = Make.FunctionDef(name='north', body=[Make.Return(Make.Constant(3))])
FunctionDefMethod: ast.FunctionDef = Make.FunctionDef(name='method', body=[Make.Pass()])
ClassDefEastWithMethod: ast.ClassDef = Make.ClassDef(name='east', body=[FunctionDefMethod])
ClassDefNorth: ast.ClassDef = Make.ClassDef(name='north', body=[Make.Pass()])
ClassDefNorthRepeated: ast.ClassDef = Make.ClassDef(name='north', body=[Make.Pass(), Make.Pass()])
AsyncFunctionDefSouth: ast.AsyncFunctionDef = Make.AsyncFunctionDef(name='south', body=[Make.Pass()])
AsyncFunctionDefSouthRepeated: ast.AsyncFunctionDef = Make.AsyncFunctionDef(name='south', body=[Make.Pass(), Make.Pass()])
AsyncFunctionDefEast: ast.AsyncFunctionDef = Make.AsyncFunctionDef(name='east', body=[Make.Pass()])

moduleDefinitionsNamesShared: ast.Module = Make.Module(
	[FunctionDefNorth, ClassDefEastWithMethod, AsyncFunctionDefSouth, ClassDefNorth, AsyncFunctionDefEast])
moduleDefinitionsNamesRepeated: ast.Module = Make.Module([
	FunctionDefNorth, ClassDefNorth, AsyncFunctionDefSouth, FunctionDefNorthRepeated, ClassDefNorthRepeated, AsyncFunctionDefSouthRepeated])

@pytest.mark.parametrize('makeDictionary, astAST, expected', [
	pytest.param(makeDictionaryFunctionDef, moduleDefinitionsNamesShared, {'north': FunctionDefNorth, 'method': FunctionDefMethod}
		, id='makeDictionaryFunctionDef-moduleDefinitionsNamesShared')
	, pytest.param(makeDictionaryClassDef, moduleDefinitionsNamesShared, {'east': ClassDefEastWithMethod, 'north': ClassDefNorth}
		, id='makeDictionaryClassDef-moduleDefinitionsNamesShared')
	, pytest.param(makeDictionaryAsyncFunctionDef, moduleDefinitionsNamesShared, {'south': AsyncFunctionDefSouth, 'east': AsyncFunctionDefEast}
		, id='makeDictionaryAsyncFunctionDef-moduleDefinitionsNamesShared')
	, pytest.param(makeDictionaryMosDef, moduleDefinitionsNamesShared
		, {'north': FunctionDefNorth, 'method': FunctionDefMethod, 'east': ClassDefEastWithMethod, 'south': AsyncFunctionDefSouth}
		, id='makeDictionaryMosDef-moduleDefinitionsNamesShared')
	, pytest.param(makeDictionaryFunctionDef, moduleDefinitionsNamesRepeated, {'north': FunctionDefNorthRepeated}
		, id='makeDictionaryFunctionDef-moduleDefinitionsNamesRepeated', marks=markDefectFirstDefinitionWins)
	, pytest.param(makeDictionaryClassDef, moduleDefinitionsNamesRepeated, {'north': ClassDefNorthRepeated}
		, id='makeDictionaryClassDef-moduleDefinitionsNamesRepeated', marks=markDefectFirstDefinitionWins)
	, pytest.param(makeDictionaryAsyncFunctionDef, moduleDefinitionsNamesRepeated, {'south': AsyncFunctionDefSouthRepeated}
		, id='makeDictionaryAsyncFunctionDef-moduleDefinitionsNamesRepeated', marks=markDefectFirstDefinitionWins)
	, pytest.param(makeDictionaryMosDef, moduleDefinitionsNamesRepeated, {'north': FunctionDefNorthRepeated, 'south': AsyncFunctionDefSouthRepeated}
		, id='makeDictionaryMosDef-moduleDefinitionsNamesRepeated', marks=markDefectFirstDefinitionWins)
])
def test_makeDictionary(makeDictionary: CallableFunction[[ast.AST], dict[str, ast.AST]], astAST: ast.AST, expected: dict[str, ast.AST]) -> None:
	assertEqualTo(makeDictionary(astAST), expected, makeDictionary.__name__, astAST)

@pytest.mark.parametrize('identifierToInline, astModule, expected', [
	pytest.param('target', Make.Module([
		Make.FunctionDef(name='helper', body=[Make.Return(Make.Constant(233))])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('value', context=Make.Store())], Make.Call(Make.Name('helper'))), Make.Return(Make.Name('value'))])])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('value', context=Make.Store())], Make.Constant(233)), Make.Return(Make.Name('value'))])
		, id='helperBodyReturn')
	, pytest.param('target', Make.Module([
		Make.FunctionDef(name='helper', body=[
			Make.Assign([Make.Name('total', context=Make.Store())], Make.Constant(89)), Make.Return(Make.Name('total'))])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('total', context=Make.Store())], Make.Call(Make.Name('helper'))), Make.Return(Make.Name('total'))])])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('total', context=Make.Store())], Make.Constant(89)), Make.Return(Make.Name('total'))])
		, id='helperBodyAssignReturn')
	, pytest.param('target', Make.Module([
		Make.FunctionDef(name='helper', body=[Make.Return(Make.Constant(233))])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('value', context=Make.Store())], Make.Call(Make.Attribute(Make.Name('pathlib'), 'helper')))
			, Make.Return(Make.Name('value'))])])
		, Make.FunctionDef(name='target', body=[
			Make.Assign([Make.Name('value', context=Make.Store())], Make.Call(Make.Attribute(Make.Name('pathlib'), 'helper')))
			, Make.Return(Make.Name('value'))])
		, id='callAttributeExcluded')
	, pytest.param('target', Make.Module([Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(377))])])
		, Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(377))])
		, id='callsNone')
	, pytest.param('target', Make.Module([
		Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(2))])
		, Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(3))])])
		, Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(3))])
		, id='targetRepeated', marks=pytest.mark.xfail(
			strict=True, reason='`inlineFunctionDef` selects through `makeDictionaryFunctionDef`, which keeps the first definition of a repeated name.'))
], indirect=['astModule'])
def test_inlineFunctionDef(identifierToInline: str, astModule: ast.Module, expected: ast.FunctionDef) -> None:
	assertComparable(inlineFunctionDef(identifierToInline, astModule), expected, inlineFunctionDef.__name__, identifierToInline)

@pytest.mark.parametrize('identifierToInline, astModule, expected', [
	pytest.param('absent', Make.Module([Make.FunctionDef(name='target', body=[Make.Return(Make.Constant(377))])]), ValueError, id='absent')
], indirect=['astModule'])
def test_inlineFunctionDefError(identifierToInline: str, astModule: ast.Module, expected: type[Exception]) -> None:
	with pytest.raises(expected, match=r"unable to find an `ast\.FunctionDef` with name identifierToInline = 'absent'"):
		inlineFunctionDef(identifierToInline, astModule)

@pytest.mark.parametrize('FunctionDef, expected', [
	pytest.param(
		Make.FunctionDef(name='north', argumentSpecification=Make.arguments(list_arg=[Make.arg('used'), Make.arg('unused')]), body=[
			Make.Assign([Make.Name('result', context=Make.Store())], Make.Name('used')), Make.Return(Make.Name('result'))])
		, Make.FunctionDef(name='north', argumentSpecification=Make.arguments(list_arg=[Make.arg('used')]), body=[
			Make.Assign([Make.Name('result', context=Make.Store())], Make.Name('used')), Make.Return(Make.Tuple([Make.Name('used')]))]
			, returns=Make.Subscript(Make.Name('tuple'), Make.Tuple([])))
		, id='parameterUnused')
	, pytest.param(
		Make.FunctionDef(name='north'
			, argumentSpecification=Make.arguments(list_arg=[Make.arg('alpha', Make.Name('int')), Make.arg('beta', Make.Name('str'))])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('alpha'), Make.Name('beta')])), Make.Return()])
		, Make.FunctionDef(name='north'
			, argumentSpecification=Make.arguments(list_arg=[Make.arg('alpha', Make.Name('int')), Make.arg('beta', Make.Name('str'))])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('alpha'), Make.Name('beta')]))
				, Make.Return(Make.Tuple([Make.Name('alpha'), Make.Name('beta')]))]
			, returns=Make.Subscript(Make.Name('tuple'), Make.Tuple([Make.Name('int'), Make.Name('str')])))
		, id='parametersUsedAnnotated')
	, pytest.param(
		Make.FunctionDef(name='north'
			, argumentSpecification=Make.arguments(posonlyargs=[Make.arg('east')], list_arg=[Make.arg('west')], kwonlyargs=[Make.arg('south')])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('east'), Make.Name('west'), Make.Name('south')])), Make.Return()])
		, Make.FunctionDef(name='north'
			, argumentSpecification=Make.arguments(posonlyargs=[Make.arg('east')], list_arg=[Make.arg('west')], kwonlyargs=[Make.arg('south')])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('east'), Make.Name('west'), Make.Name('south')]))
				, Make.Return(Make.Tuple([Make.Name('west'), Make.Name('east'), Make.Name('south')]))]
			, returns=Make.Subscript(Make.Name('tuple'), Make.Tuple([])))
		, id='parameterKindsArgsPosonlyargsKwonlyargs')
	, pytest.param(
		Make.FunctionDef(name='north', argumentSpecification=Make.arguments(list_arg=[Make.arg('alpha')]), body=[Make.Return(Make.Name('alpha'))])
		, Make.FunctionDef(name='north', argumentSpecification=Make.arguments(), body=[Make.Return(Make.Tuple([]))]
			, returns=Make.Subscript(Make.Name('tuple'), Make.Tuple([])))
		, id='parameterUsedOnlyInReturn')
	, pytest.param(
		Make.FunctionDef(name='north', argumentSpecification=Make.arguments(list_arg=[Make.arg('alpha')])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('alpha')]))])
		, Make.FunctionDef(name='north', argumentSpecification=Make.arguments(list_arg=[Make.arg('alpha')])
			, body=[Make.Expr(Make.Call(Make.Name('combine'), [Make.Name('alpha')]))]
			, returns=Make.Subscript(Make.Name('tuple'), Make.Tuple([])))
		, id='returnNone')
], indirect=['FunctionDef'])
def test_removeUnusedParameters(FunctionDef: ast.FunctionDef, expected: ast.FunctionDef) -> None:
	FunctionDefReturned: ast.FunctionDef = removeUnusedParameters(FunctionDef)
	assert FunctionDefReturned is FunctionDef, messageTestFailure(FunctionDefReturned, FunctionDef, removeUnusedParameters.__name__, FunctionDef)
	assertComparable(FunctionDefReturned, expected, removeUnusedParameters.__name__)
