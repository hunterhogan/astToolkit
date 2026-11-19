"""Expected values and exceptions are hand-derived from the `transformationTools` docstrings."""
from __future__ import annotations

from astToolkit import Make
from astToolkit.transformationTools import pythonCode2ast_expr, unjoinBinOP, unparseFindReplace
from copy import deepcopy
from tests import assertComparable, assertEqualTo, messageTestFailure
from typing import TYPE_CHECKING
import ast
import pytest

if TYPE_CHECKING:
	from collections.abc import Mapping

@pytest.mark.parametrize('string, expected', [
	pytest.param('233', Make.Constant(233), id='constant233')
	, pytest.param('north', Make.Name('north'), id='nameNorth')
	, pytest.param('north.east', Make.Attribute(Make.Name('north'), 'east'), id='attributeNorthEast')
	, pytest.param('north[13]', Make.Subscript(Make.Name('north'), Make.Constant(13)), id='subscriptNorth13')
	, pytest.param('north()', Make.Call(Make.Name('north')), id='callNorth')
	, pytest.param('value = 13\nnorth', Make.Name('north'), id='assignThenNameNorth')
	, pytest.param('north\ndef south():\n    east', Make.Name('east'), id='nameNorthThenNestedEast')
	, pytest.param('def south():\n    east\nnorth', Make.Name('north'), id='nestedEastThenNameNorth')
])
def test_pythonCode2ast_expr(string: str, expected: ast.expr) -> None:
	assertComparable(pythonCode2ast_expr(string), expected, pythonCode2ast_expr.__name__, string)

@pytest.mark.parametrize('string, expected, match', [
	pytest.param('value = 13', ValueError, 'unexpectedly returned `None`', id='exprNone')
	, pytest.param('north(', SyntaxError, r"'\(' was never closed", id='syntaxInvalid')
])
def test_pythonCode2ast_exprError(string: str, expected: type[Exception], match: str) -> None:
	with pytest.raises(expected, match=match):
		pythonCode2ast_expr(string)

@pytest.mark.parametrize('astAST, operator, expected', [
	pytest.param(Make.Constant(89), ast.operator, [], id='constant89'),
	pytest.param(Make.Name('north'), ast.Add, [], id='nameNorth'),
	pytest.param(Make.Module([]), ast.Add, [], id='emptyModule'),
	pytest.param(Make.Add(), ast.Add, [], id='operatorNode'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('east')]), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='twoOperands'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='leftNested'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='rightNested'),
	pytest.param(Make.Add.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='bothBranches'),
	pytest.param(Make.Add.join([Make.Name('north'), Make.Name('north'), Make.Name('east')]), ast.Add,
		[Make.Name('north'), Make.Name('north'), Make.Name('east')], id='repeatedOperands'),
	pytest.param(Make.Add.join([
		Make.Mult.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]),
		Make.Name('west')]), ast.Add,
		[Make.Mult.join([Make.Name('north'), Make.Add.join([Make.Name('east'), Make.Name('south')])]),
			Make.Name('west')], id='differentLeftOperator'),
	pytest.param(Make.Add.join([
		Make.Name('north'),
		Make.Mult.join([Make.Add.join([Make.Name('east'), Make.Name('south')]), Make.Name('west')])]), ast.Add,
		[Make.Name('north'),
			Make.Mult.join([Make.Add.join([Make.Name('east'), Make.Name('south')]), Make.Name('west')])], id='differentRightOperator'),
	pytest.param(Make.Add.join([
		Make.Mult.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')]), ast.operator,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='allOperators'),
	pytest.param(Make.Sub.join([Make.Name('north'), Make.Sub.join([Make.Name('east'), Make.Name('south')])]), ast.Sub,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='noncommutativeOrder'),
	pytest.param(Make.Mult.join([Make.Name('north'), Make.Name('east')]), ast.Add,
		[], id='noMatchingOperator'),
	pytest.param(Make.Mult.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')]), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='searchInsideUnmatchedRoot'),
	pytest.param(Make.Add.join([
		Make.Call(Make.Name('combine'), [Make.Add.join([Make.Name('north'), Make.Name('east')])]),
		Make.Name('south')]), ast.Add,
		[Make.Call(Make.Name('combine'), [Make.Add.join([Make.Name('north'), Make.Name('east')])]),
			Make.Name('south')], id='completeCallOperand'),
	pytest.param(Make.BitOr.join([
		Make.Subscript(Make.Name('list'), Make.BitOr.join([Make.Name('int'), Make.Name('str')])),
		Make.Constant(None)]), ast.BitOr,
		[Make.Subscript(Make.Name('list'), Make.BitOr.join([Make.Name('int'), Make.Name('str')])),
			Make.Constant(None)], id='nestedTypeUnion'),
	pytest.param(Make.BitOr.join([
		Make.Attribute(Make.Name('ast'), 'expr'),
		Make.Subscript(Make.Name('list'), Make.Attribute(Make.Name('ast'), 'expr')),
		Make.Constant(None)]), ast.BitOr,
		[Make.Attribute(Make.Name('ast'), 'expr'), Make.Subscript(Make.Name('list'), Make.Attribute(Make.Name('ast'), 'expr')),
			Make.Constant(None)], id='factoryTypeUnion'),
	pytest.param(Make.Module([
		Make.Expr(Make.Add.join([Make.Name('north'), Make.Name('east')])),
		Make.Expr(Make.Constant(89)),
		Make.Expr(Make.Add.join([Make.Name('south'), Make.Name('west')]))]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='separateOperations'),
	pytest.param(Make.Add.join([Make.Name('north')] * 3), ast.Add,
		[Make.Name('north'), Make.Name('north'), Make.Name('north')], id='sharedOperand'),
	pytest.param(Make.Add.join([Make.Add.join([Make.Name('north'), Make.Name('east')])] * 2), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('north'), Make.Name('east')], id='sharedSubtree'),
	pytest.param(Make.Add.join([
		Make.UnaryOp(Make.USub(), Make.Add.join([Make.Name('north'), Make.Name('east')])),
		Make.Name('south')]), ast.Add,
		[Make.UnaryOp(Make.USub(), Make.Add.join([Make.Name('north'), Make.Name('east')])),
			Make.Name('south')], id='completeUnaryOperand'),
	pytest.param(Make.Add.join([
		Make.IfExp(Make.Name('ready'), Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')),
		Make.Name('west')]), ast.Add,
		[Make.IfExp(Make.Name('ready'), Make.Add.join([Make.Name('north'), Make.Name('east')]), Make.Name('south')),
			Make.Name('west')], id='completeConditionalOperand'),
	pytest.param(Make.Expression(Make.Add.join([Make.Name('north'), Make.Name('east')])), ast.Add,
		[Make.Name('north'), Make.Name('east')], id='expressionRoot'),
	pytest.param(Make.Call(Make.Name('combine'), [
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='separateCallArguments'),
	pytest.param(Make.Mult.join([
		Make.Add.join([Make.Name('north'), Make.Name('east')]),
		Make.Add.join([Make.Name('south'), Make.Name('west')])]), ast.Add,
		[Make.Name('north'), Make.Name('east'), Make.Name('south'), Make.Name('west')], id='searchBothUnmatchedBranches'),
	pytest.param(Make.Pow.join([Make.Name('north'), Make.Pow.join([Make.Name('east'), Make.Name('south')])]), ast.Pow,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='nestedPower'),
	pytest.param(Make.FloorDiv.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.FloorDiv,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='floorDivision'),
	pytest.param(Make.BitXor.join([Make.Name('north'), Make.Name('east'), Make.Name('south')]), ast.BitXor,
		[Make.Name('north'), Make.Name('east'), Make.Name('south')], id='bitwiseXor'),
])
def test_unjoinBinOP(astAST: ast.AST, operator: type[ast.operator], expected: list[ast.expr]) -> None:
	astASTBefore: ast.AST = deepcopy(astAST)
	identities: set[int] = set(map(id, ast.walk(astAST)))
	list_ast_expr: list[ast.expr] = unjoinBinOP(astAST, operator)
	assertEqualTo(type(list_ast_expr), list, unjoinBinOP.__name__, astAST, operator)
	assertComparable(Make.Tuple(list_ast_expr), Make.Tuple(expected), unjoinBinOP.__name__, astAST, operator)
	assert set(map(id, list_ast_expr)) <= identities, messageTestFailure(
		list_ast_expr, 'the operand nodes of astAST', unjoinBinOP.__name__, astAST, operator)
	assert ast.compare(astAST, astASTBefore, compare_attributes=True), messageTestFailure(
		ast.dump(astAST), ast.dump(astASTBefore), unjoinBinOP.__name__, astAST, operator)

# `ast.unparse` reads the `lineno` of an `ast.Assign`, so the sample comes from `ast.parse`.
assignNorth233: ast.Module = ast.parse('north = 233')

@pytest.mark.parametrize('astTree, mappingFindReplaceNodes, expected', [
	pytest.param(assignNorth233, {Make.Constant(233): Make.Constant(89)}
		, Make.Module([Make.Assign([Make.Name('north', context=Make.Store())], Make.Constant(89))]), id='constant233To89')
	, pytest.param(assignNorth233, {Make.Constant(377): Make.Constant(89)}, assignNorth233, id='matchNone')
	, pytest.param(assignNorth233, {Make.Name('north'): Make.Name('south')}
		, Make.Module([Make.Assign([Make.Name('south')], Make.Constant(233))]), id='nameLoadMatchesNameStore')
	, pytest.param(assignNorth233, {Make.Constant(233): Make.Constant(89), Make.Constant(89): Make.Constant(13)}
		, Make.Module([Make.Assign([Make.Name('north', context=Make.Store())], Make.Constant(13))]), id='replacementMatchesLaterEntry')
	, pytest.param(Make.Constant(233), {Make.Constant(233): Make.Constant(89)}, Make.Constant(233), id='rootNotReplaced')
])
def test_unparseFindReplace(astTree: ast.AST, mappingFindReplaceNodes: Mapping[ast.AST, ast.AST], expected: ast.AST) -> None:
	astTreeBefore: ast.AST = deepcopy(astTree)
	newTree: ast.AST = unparseFindReplace(astTree, mappingFindReplaceNodes)
	assert newTree is not astTree, messageTestFailure(newTree, 'a copy of astTree', unparseFindReplace.__name__, astTree, mappingFindReplaceNodes)
	assertComparable(newTree, expected, unparseFindReplace.__name__, astTree, mappingFindReplaceNodes)
	assertComparable(astTree, astTreeBefore, unparseFindReplace.__name__, astTree, mappingFindReplaceNodes)
