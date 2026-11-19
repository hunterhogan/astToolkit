"""Expected values come from the `Grab` docstring: each `Grab.<field>Attribute(action)` returns a function that sets the node's
`<field>` to `action` of its value and returns the node. `Grab.index` and `Grab.andDoAllOf` have no docstrings; their expected
values follow the antecedent-action convention of the `Then` docstrings: an action that returns `None` removes the matched node,
an action that returns a `list` replaces the matched node with the list's elements, and any other value replaces the matched node.
"""
from __future__ import annotations

from astToolkit import Grab, Make, Then
from operator import attrgetter
from tests import assertEqualTo, messageTestFailure
from tests.dataSamples.Make import lookupNodeField
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from collections.abc import Callable, Sequence
	from typing import Any
	import ast

# The builtin `id` as the action shows both that the action received the field's value and that its result replaced the value.
@pytest.mark.parametrize('identifierClass, node, field', lookupNodeField.values(), ids=lookupNodeField.keys(), indirect=['node'])
def test_GrabFieldAttribute(identifierClass: str, node: ast.AST, field: str) -> None:
	valueOriginal: Any = getattr(node, field)
	nodeReturned: ast.AST = getattr(Grab, f'{field}Attribute')(id)(node)
	assert nodeReturned is node, messageTestFailure(nodeReturned, node, f'Grab.{field}Attribute(id)', f'ast.{identifierClass}')
	assertEqualTo(getattr(node, field), id(valueOriginal), f'Grab.{field}Attribute(id)', f'ast.{identifierClass}')

namesAlphaBetaGamma: tuple[ast.Name, ...] = (Make.Name('alpha'), Make.Name('beta'), Make.Name('gamma'))

@pytest.mark.parametrize('node, at, action, expected', [
	pytest.param(namesAlphaBetaGamma, 0, Then.replaceWith(Make.Name('delta')), ['delta', 'beta', 'gamma'], id='at0-replaceWith')
	, pytest.param(namesAlphaBetaGamma, 1, Then.replaceWith(Make.Name('delta')), ['alpha', 'delta', 'gamma'], id='at1-replaceWith')
	, pytest.param(namesAlphaBetaGamma, 2, Then.replaceWith(Make.Name('delta')), ['alpha', 'beta', 'delta'], id='at2-replaceWith')
	, pytest.param(namesAlphaBetaGamma, -1, Then.replaceWith(Make.Name('delta')), ['alpha', 'beta', 'delta'], id='atLess1-replaceWith')
	, pytest.param(namesAlphaBetaGamma, 0, Then.removeIt, ['beta', 'gamma'], id='at0-removeIt')
	, pytest.param(namesAlphaBetaGamma, 1, Then.removeIt, ['alpha', 'gamma'], id='at1-removeIt')
	, pytest.param(namesAlphaBetaGamma, 2, Then.removeIt, ['alpha', 'beta'], id='at2-removeIt')
	, pytest.param(namesAlphaBetaGamma, -1, Then.removeIt, ['alpha', 'beta'], id='atLess1-removeIt')
	, pytest.param(namesAlphaBetaGamma, 0, Then.insertThisBelow([Make.Name('delta')]), ['alpha', 'delta', 'beta', 'gamma'], id='at0-insertThisBelow')
	, pytest.param(namesAlphaBetaGamma, 1, Then.insertThisBelow([Make.Name('delta')]), ['alpha', 'beta', 'delta', 'gamma'], id='at1-insertThisBelow')
	, pytest.param(namesAlphaBetaGamma, 2, Then.insertThisBelow([Make.Name('delta')]), ['alpha', 'beta', 'gamma', 'delta'], id='at2-insertThisBelow')
	, pytest.param(namesAlphaBetaGamma, -1, Then.insertThisBelow([Make.Name('delta')]), ['alpha', 'beta', 'gamma', 'delta'], id='atLess1-insertThisBelow'
		, marks=pytest.mark.xfail(strict=True, reason='`Grab.index` keeps `node[at + 1:None]` after the list, which for `at=-1` is the whole sequence.'))
])
def test_GrabIndex(node: Sequence[ast.Name], at: int, action: Callable[[ast.Name], Any], expected: list[str]) -> None:
	nodesReturned: list[ast.Name] = Grab.index(at, action)(node)
	assertEqualTo(([*map(attrgetter('id'), nodesReturned)], type(nodesReturned)), (expected, list), 'Grab.index', at, action, node)

@pytest.mark.parametrize('node, listOfActions, expected', [
	pytest.param(Make.Name('base'), [], 'base', id='actionsNone')
	, pytest.param(Make.Name('base'), [Grab.idAttribute('{}North'.format)], 'baseNorth', id='idAttributeNorth')
	, pytest.param(Make.Name('base'), [Grab.idAttribute('{}North'.format), Grab.idAttribute('{}East'.format)], 'baseNorthEast', id='idAttributeNorthThenEast')
	, pytest.param(Make.Name('base'), [Grab.idAttribute(str.upper), Grab.idAttribute('{}North'.format)], 'BASENorth', id='idAttributeUpperThenNorth')
	, pytest.param(Make.Name('base'), [Grab.idAttribute(str.upper), Then.replaceWith(Make.Name('delta'))], 'delta', id='idAttributeUpperThenReplaceWith')
], indirect=['node'])
def test_GrabAndDoAllOf(node: ast.Name, listOfActions: Sequence[Callable[[Any], Any]], expected: str) -> None:
	assertEqualTo(Grab.andDoAllOf(listOfActions)(node).id, expected, 'Grab.andDoAllOf', listOfActions, node)
