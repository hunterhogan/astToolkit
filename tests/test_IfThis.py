"""Expected values are hand-derived from the `IfThis` docstrings unless a comment names another basis."""
from __future__ import annotations

from astToolkit import Be, IfThis, Make
from tests import messageTestFailure
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from collections.abc import Callable, Sequence
	from hunterMakesPy import CallableFunction
	from typing import Any
	import ast

nodesIdentifierNorth: dict[str, ast.AST] = {
	'nameNorth': Make.Name('north'),
	'nameSouth': Make.Name('south'),
	'FunctionDefNorth': Make.FunctionDef(name='north'),
	'ClassDefNorth': Make.ClassDef(name='north'),
	'callNorth': Make.Call(Make.Name('north')),
	'callSouth': Make.Call(Make.Name('south')),
	'callAttributeNorthEast': Make.Call(Make.Attribute(Make.Name('north'), 'east')),
	'argNorth': Make.arg('north'),
	'keywordNorth': Make.keyword('north', Make.Constant(13)),
	'starredNorth': Make.Starred(Make.Name('north')),
	'starredSubscriptNorth': Make.Starred(Make.Subscript(Make.Name('north'), Make.Constant(13))),
	'subscriptNorth': Make.Subscript(Make.Name('north'), Make.Constant(13)),
	'attributeNorthEast': Make.Attribute(Make.Name('north'), 'east'),
	'attributeNorthEastWest': Make.Attribute(Make.Attribute(Make.Name('north'), 'east'), 'west'),
	'attributeSouthNorth': Make.Attribute(Make.Name('south'), 'north'),
	'constantNorth': Make.Constant('north'),
}

lookupMatchesIdentifierNorth: dict[CallableFunction[[str], Callable[[ast.AST], bool]], frozenset[str]] = {
	IfThis.isNameIdentifier: frozenset({'nameNorth'}),
	IfThis.isFunctionDefIdentifier: frozenset({'FunctionDefNorth'}),
	IfThis.isClassDefIdentifier: frozenset({'ClassDefNorth'}),
	IfThis.isCallIdentifier: frozenset({'callNorth'}),
	IfThis.is_argIdentifier: frozenset({'argNorth'}),
	IfThis.is_keywordIdentifier: frozenset({'keywordNorth'}),
	IfThis.isAttributeIdentifier: frozenset({'attributeNorthEast', 'attributeNorthEastWest'}),
	IfThis.isStarredIdentifier: frozenset({'starredNorth', 'starredSubscriptNorth'}),
	IfThis.isSubscriptIdentifier: frozenset({'subscriptNorth'}),
	IfThis.isNestedNameIdentifier: frozenset({
		'nameNorth', 'starredNorth', 'starredSubscriptNorth', 'subscriptNorth', 'attributeNorthEast', 'attributeNorthEastWest'}),
}

@pytest.mark.parametrize('identifierNode', nodesIdentifierNorth)
@pytest.mark.parametrize('methodIfThis', lookupMatchesIdentifierNorth)
def test_IfThisIdentifier(methodIfThis: CallableFunction[[str], Callable[[ast.AST], bool]], identifierNode: str) -> None:
	actual: bool = methodIfThis('north')(nodesIdentifierNorth[identifierNode])
	expected: bool = identifierNode in lookupMatchesIdentifierNorth[methodIfThis]
	assert actual is expected, messageTestFailure(actual, expected, f'IfThis.{methodIfThis.__name__}', 'north', nodesIdentifierNorth[identifierNode])

lookupMatchesNode: dict[CallableFunction[[ast.AST], bool], frozenset[str]] = {
	IfThis.isAttributeName: frozenset({'attributeNorthEast', 'attributeSouthNorth'}),
	IfThis.isCallToName: frozenset({'callNorth', 'callSouth'}),
}

@pytest.mark.parametrize('identifierNode', nodesIdentifierNorth)
@pytest.mark.parametrize('methodIfThis', lookupMatchesNode)
def test_IfThisNode(methodIfThis: CallableFunction[[ast.AST], bool], identifierNode: str) -> None:
	actual: bool = methodIfThis(nodesIdentifierNorth[identifierNode])
	expected: bool = identifierNode in lookupMatchesNode[methodIfThis]
	assert actual is expected, messageTestFailure(actual, expected, f'IfThis.{methodIfThis.__name__}', nodesIdentifierNorth[identifierNode])

nodesNamespaceNorthIdentifierEast: dict[str, ast.AST] = {
	'attributeNorthEast': Make.Attribute(Make.Name('north'), 'east'),
	'attributeNorthWest': Make.Attribute(Make.Name('north'), 'west'),
	'attributeSouthEast': Make.Attribute(Make.Name('south'), 'east'),
	'attributeNorthSouthEast': Make.Attribute(Make.Attribute(Make.Name('north'), 'south'), 'east'),
	'callAttributeNorthEast': Make.Call(Make.Attribute(Make.Name('north'), 'east')),
	'unaryNotAttributeNorthEast': Make.UnaryOp(Make.Not(), Make.Attribute(Make.Name('north'), 'east')),
	'unaryInvertAttributeNorthEast': Make.UnaryOp(Make.Invert(), Make.Attribute(Make.Name('north'), 'east')),
	'ifUnaryNotAttributeNorthEast': Make.If(Make.UnaryOp(Make.Not(), Make.Attribute(Make.Name('north'), 'east')), [Make.Pass()]),
	'ifAttributeNorthEast': Make.If(Make.Attribute(Make.Name('north'), 'east'), [Make.Pass()]),
}

lookupMatchesNamespaceNorthIdentifierEast: dict[CallableFunction[[str, str], Callable[[ast.AST], bool]], frozenset[str]] = {
	IfThis.isAttributeNamespaceIdentifier: frozenset({'attributeNorthEast'}),
	IfThis.isCallAttributeNamespaceIdentifier: frozenset({'callAttributeNorthEast'}),
	IfThis.isUnaryNotAttributeNamespaceIdentifier: frozenset({'unaryNotAttributeNorthEast'}),
	IfThis.isIfUnaryNotAttributeNamespaceIdentifier: frozenset({'ifUnaryNotAttributeNorthEast'}),
}

@pytest.mark.parametrize('identifierNode', nodesNamespaceNorthIdentifierEast)
@pytest.mark.parametrize('methodIfThis', lookupMatchesNamespaceNorthIdentifierEast)
def test_IfThisNamespaceIdentifier(methodIfThis: CallableFunction[[str, str], Callable[[ast.AST], bool]], identifierNode: str) -> None:
	actual: bool = methodIfThis('north', 'east')(nodesNamespaceNorthIdentifierEast[identifierNode])
	expected: bool = identifierNode in lookupMatchesNamespaceNorthIdentifierEast[methodIfThis]
	assert actual is expected, messageTestFailure(
		actual, expected, f'IfThis.{methodIfThis.__name__}', 'north', 'east', nodesNamespaceNorthIdentifierEast[identifierNode])

@pytest.mark.parametrize('identifier, node, expected', [
	pytest.param('north', 'north', True, id='north-north')
	, pytest.param('north', 'south', False, id='north-south')
	, pytest.param('north', None, False, id='north-None')
	, pytest.param(None, None, True, id='None-None')
	, pytest.param(None, 'north', False, id='None-north')
])
def test_IfThisIsIdentifier(identifier: str | None, node: str | None, expected: bool) -> None:
	actual: bool = IfThis.isIdentifier(identifier)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.isIdentifier.__name__, identifier, node)

@pytest.mark.parametrize('value, node, expected', [
	pytest.param(233, Make.Constant(233), True, id='233-constant233')
	, pytest.param(233, Make.Constant(89), False, id='233-constant89')
	, pytest.param('north', Make.Constant('north'), True, id='north-constantNorth')
	, pytest.param('north', Make.Name('north'), False, id='north-nameNorth')
	, pytest.param(None, Make.Constant(None), True, id='None-constantNone')
	, pytest.param(None, Make.Constant(233), False, id='None-constant233')
])
def test_IfThisIsConstant_value(value: Any, node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.isConstant_value(value)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.isConstant_value.__name__, value, node)

@pytest.mark.parametrize('predicate, node, expected', [
	pytest.param((Be.Name, IfThis.isNameIdentifier('north')), Make.Name('north'), True, id='everyPredicateMatches')
	, pytest.param((Be.Name, IfThis.isNameIdentifier('south')), Make.Name('north'), False, id='onePredicateFails')
	, pytest.param((IfThis.isNameIdentifier('south'), Be.Name), Make.Name('north'), False, id='firstPredicateFails')
	, pytest.param((), Make.Name('north'), True, id='predicatesNone')
])
def test_IfThisIsAllOf(predicate: Sequence[Callable[[ast.AST], bool]], node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.isAllOf(*predicate)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.isAllOf.__name__, *predicate)

@pytest.mark.parametrize('predicate, node, expected', [
	pytest.param((Be.Constant, Be.Name), Make.Name('north'), True, id='onePredicateMatches')
	, pytest.param((Be.Name, Be.Constant), Make.Name('north'), True, id='firstPredicateMatches')
	, pytest.param((Be.Constant, Be.FunctionDef), Make.Name('north'), False, id='noPredicateMatches')
	, pytest.param((), Make.Name('north'), False, id='predicatesNone')
])
def test_IfThisIsAnyOf(predicate: Sequence[Callable[[ast.AST], bool]], node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.isAnyOf(*predicate)(node)  # pyright: ignore[reportUnknownVariableType]
	assert actual is expected, messageTestFailure(actual, expected, IfThis.isAnyOf.__name__, *predicate)

assignNorth233: ast.Assign = Make.Assign([Make.Name('north', context=Make.Store())], Make.Constant(233))

@pytest.mark.parametrize('targets0Predicate, node, expected', [
	pytest.param(IfThis.isNameIdentifier('north'), assignNorth233, True, id='nameNorth-assignNorth233')
	, pytest.param(IfThis.isNameIdentifier('south'), assignNorth233, False, id='nameSouth-assignNorth233')
	, pytest.param(IfThis.isNameIdentifier('north')
		, Make.Assign([Make.Name('south', context=Make.Store()), Make.Name('north', context=Make.Store())], Make.Constant(233))
		, False, id='nameNorth-assignSouthNorth233')
	, pytest.param(IfThis.isNameIdentifier('north'), Make.Name('north'), False, id='nameNorth-nameNorth')
])
def test_IfThisIsAssignAndTargets0Is(targets0Predicate: Callable[[ast.AST], bool], node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.isAssignAndTargets0Is(targets0Predicate)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.isAssignAndTargets0Is.__name__, targets0Predicate, node)

FunctionDefNestingAssign: ast.FunctionDef = Make.FunctionDef(name='north', body=[assignNorth233])
FunctionDefNestingFunctionDef: ast.FunctionDef = Make.FunctionDef(name='north', body=[Make.FunctionDef(name='south', body=[Make.Pass()])])

@pytest.mark.parametrize('predicate, node, expected', [
	pytest.param(IfThis.isNameIdentifier('south'), assignNorth233, True, id='nameSouth-assignNorth233')
	, pytest.param(IfThis.isNameIdentifier('north'), assignNorth233, False, id='nameNorth-assignNorth233')
	, pytest.param(Be.Assign, assignNorth233, True, id='Assign-assignNorth233')
	, pytest.param(Be.Assign, FunctionDefNestingAssign, False, id='Assign-FunctionDefNestingAssign')
])
def test_IfThisMatchesNoDescendant(predicate: Callable[[ast.AST], bool], node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.matchesNoDescendant(predicate)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.matchesNoDescendant.__name__, predicate, node)

@pytest.mark.parametrize('predicate, node, expected', [
	pytest.param(Be.Assign, assignNorth233, True, id='Assign-assignNorth233')
	, pytest.param(Be.Assign, Make.Name('north'), False, id='Assign-nameNorth')
	, pytest.param(Be.FunctionDef, FunctionDefNestingAssign, True, id='FunctionDef-FunctionDefNestingAssign')
	, pytest.param(Be.FunctionDef, FunctionDefNestingFunctionDef, False, id='FunctionDef-FunctionDefNestingFunctionDef')
])
def test_IfThisMatchesMeButNotAnyDescendant(predicate: Callable[[ast.AST], bool], node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.matchesMeButNotAnyDescendant(predicate)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.matchesMeButNotAnyDescendant.__name__, predicate, node)

@pytest.mark.parametrize('astAST, node, expected', [
	pytest.param(Make.Name('north'), Make.Name('north'), True, id='nameNorth-nameNorth')
	, pytest.param(Make.Name('north'), Make.Name('south'), False, id='nameNorth-nameSouth')
	, pytest.param(Make.Name('north'), Make.Name('north', context=Make.Store()), True, id='nameNorth-nameNorthStore')
	, pytest.param(Make.Constant(233), Make.Constant(233), True, id='constant233-constant233')
	, pytest.param(Make.Constant(233), Make.Constant(89), False, id='constant233-constant89')
])
def test_IfThisUnparseIs(astAST: ast.AST, node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.unparseIs(astAST)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.unparseIs.__name__, astAST, node)

# Reference: `unparseFindReplace`'s docstring: `IfThis.astIs` matches AST structure rather than unparsed text.
@pytest.mark.parametrize('astAST, node, expected', [
	pytest.param(Make.Name('north'), Make.Name('north'), True, id='nameNorth-nameNorth')
	, pytest.param(Make.Name('north'), Make.Name('south'), False, id='nameNorth-nameSouth')
	, pytest.param(Make.Name('north'), Make.Name('north', context=Make.Store()), False, id='nameNorth-nameNorthStore')
	, pytest.param(Make.Constant(233), Make.Constant(233), True, id='constant233-constant233')
])
def test_IfThisAstIs(astAST: ast.AST, node: ast.AST, expected: bool) -> None:
	actual: bool = IfThis.astIs(astAST)(node)
	assert actual is expected, messageTestFailure(actual, expected, IfThis.astIs.__name__, astAST, node)
