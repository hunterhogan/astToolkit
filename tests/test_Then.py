"""Expected values come from the `Then` docstrings unless a comment names another basis."""
from __future__ import annotations

from ast import unparse
from astToolkit import DOT, Make, Then
from operator import attrgetter
from tests import assertEqualTo, messageTestFailure
from tests.dataSamples.Make import lookupNode
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from collections.abc import Callable, Sequence
	from typing import Any
	import ast

@pytest.mark.parametrize('identifierClass, node', lookupNode.values(), ids=lookupNode.keys())
def test_ThenAppendTo(identifierClass: str, node: ast.AST) -> None:
	listOfAny: list[Any] = [Make.Name('north')]
	nodeReturned: ast.AST = Then.appendTo(listOfAny)(node)
	assert nodeReturned is node, messageTestFailure(nodeReturned, node, Then.appendTo.__name__, f'ast.{identifierClass}')
	assertEqualTo([*map(id, listOfAny)], [id(listOfAny[0]), id(node)], Then.appendTo.__name__, f'ast.{identifierClass}')

@pytest.mark.parametrize('identifierClass, node', lookupNode.values(), ids=lookupNode.keys())
def test_ThenExtractIt(identifierClass: str, node: ast.AST) -> None:
	nodeReturned: ast.AST = Then.extractIt(node)
	assert nodeReturned is node, messageTestFailure(nodeReturned, node, Then.extractIt.__name__, f'ast.{identifierClass}')

@pytest.mark.parametrize('identifierClass, node', lookupNode.values(), ids=lookupNode.keys())
def test_ThenRemoveIt(identifierClass: str, node: ast.AST) -> None:
	assertEqualTo(Then.removeIt(node), None, Then.removeIt.__name__, f'ast.{identifierClass}')

@pytest.mark.parametrize('identifierClass, node', lookupNode.values(), ids=lookupNode.keys())
def test_ThenReplaceWith(identifierClass: str, node: ast.AST) -> None:
	this: ast.Name = Make.Name('north')
	nodeReturned: ast.AST = Then.replaceWith(this)(node)
	assert nodeReturned is this, messageTestFailure(nodeReturned, this, Then.replaceWith.__name__, f'ast.{identifierClass}')

nodePass: ast.Pass = Make.Pass()
nodeReturn233: ast.Return = Make.Return(Make.Constant(233))
nodeAssignNorth: ast.Assign = Make.Assign([Make.Name('north', context=Make.Store())], Make.Constant(89))

@pytest.mark.parametrize('list_astAST, node, expected', [
	pytest.param([], nodeReturn233, [nodeReturn233], id='astASTNone')
	, pytest.param([nodePass], nodeReturn233, [nodePass, nodeReturn233], id='pass')
	, pytest.param([nodeAssignNorth, nodePass], nodeReturn233, [nodeAssignNorth, nodePass, nodeReturn233], id='assignNorthThenPass')
])
def test_ThenInsertThisAbove(list_astAST: Sequence[ast.AST], node: ast.AST, expected: list[ast.AST]) -> None:
	assertEqualTo([*map(id, Then.insertThisAbove(list_astAST)(node))], [*map(id, expected)], Then.insertThisAbove.__name__, list_astAST, node)

@pytest.mark.parametrize('list_astAST, node, expected', [
	pytest.param([], nodeReturn233, [nodeReturn233], id='astASTNone')
	, pytest.param([nodePass], nodeReturn233, [nodeReturn233, nodePass], id='pass')
	, pytest.param([nodeAssignNorth, nodePass], nodeReturn233, [nodeReturn233, nodeAssignNorth, nodePass], id='assignNorthThenPass')
])
def test_ThenInsertThisBelow(list_astAST: Sequence[ast.AST], node: ast.AST, expected: list[ast.AST]) -> None:
	assertEqualTo([*map(id, Then.insertThisBelow(list_astAST)(node))], [*map(id, expected)], Then.insertThisBelow.__name__, list_astAST, node)

@pytest.mark.parametrize('key, value, nodes, expected', [
	pytest.param(DOT.id, attrgetter('ctx.__class__.__name__'), [Make.Name('north'), Make.Name('south', context=Make.Store())]
		, {'north': 'Load', 'south': 'Store'}, id='keysDistinct')
	, pytest.param(attrgetter('__class__.__name__'), DOT.id, [Make.Name('north'), Make.Name('south'), Make.Name('east')]
		, {'Name': 'north'}, id='keyRepeatedKeepsFirst')
	, pytest.param(attrgetter('__class__.__name__'), unparse, [Make.Constant(233), Make.Name('north'), Make.Constant(89)]
		, {'Constant': '233', 'Name': 'north'}, id='keyRepeatedAfterOtherKey')
])
def test_ThenUpdateKeyValueIn(key: Callable[[Any], Any], value: Callable[[Any], Any], nodes: Sequence[ast.AST], expected: dict[Any, Any]) -> None:
	dictionary: dict[Any, Any] = {}
	updateFunction: Callable[[ast.AST], Any] = Then.updateKeyValueIn(key, value, dictionary)
	mappingsReturned: list[Any] = [*map(updateFunction, nodes)]
	assertEqualTo([*map(id, mappingsReturned)], [id(dictionary)] * len(nodes), Then.updateKeyValueIn.__name__, key, value, dictionary)
	assertEqualTo(dictionary, expected, Then.updateKeyValueIn.__name__, key, value, nodes)
