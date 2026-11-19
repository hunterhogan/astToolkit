"""Expected values come from the `Be` docstrings: `Be.<class>` matches `ast.<class>`, which is a subclass of the class each docstring
names, and `Be.<class>.<field>Is(attributeCondition)` also requires `attributeCondition` of that field.

The generated contracts compare with the node's method resolution order, which records the `ast` class hierarchy."""
from __future__ import annotations

from astToolkit import Be
from functools import partial
from hypothesis import given, strategies
from operator import is_, is_not
from tests import messageTestFailure
from tests.dataSamples.Make import allSubclasses, lookupNodeClassMatching, lookupNodeField, nodesSample
from typing import TYPE_CHECKING
import ast
import pytest

if TYPE_CHECKING:
	from hunterMakesPy import CallableFunction

@pytest.mark.parametrize('identifierClass, node', lookupNodeClassMatching.values(), ids=lookupNodeClassMatching.keys())
def test_Be(identifierClass: str, node: ast.AST) -> None:
	actual: bool = getattr(Be, identifierClass)(node)
	assert actual is True, messageTestFailure(actual, True, f'Be.{identifierClass}', node)

# Every class with every sample is 123 × 315 = 38,745 pairs, 47 seconds when enumerated. `test_Be` enumerates each sample with every
# class that matches it; each run of this test draws other pairs, and Hypothesis replays any failure first on the next run.
@given(identifierClass=strategies.sampled_from(tuple(allSubclasses)), node=strategies.sampled_from(nodesSample))
def test_BeGenerated(identifierClass: str, node: ast.AST) -> None:
	expected: bool = getattr(ast, identifierClass) in type(node).__mro__
	actual: bool = getattr(Be, identifierClass)(node)
	assert actual is expected, messageTestFailure(actual, expected, f'Be.{identifierClass}', node)

@pytest.mark.parametrize('comparison, expected', [(is_, True), (is_not, False)])
@pytest.mark.parametrize('identifierClass, node, field', lookupNodeField.values(), ids=lookupNodeField.keys())
def test_BeFieldIs(identifierClass: str, node: ast.AST, field: str, comparison: CallableFunction[[object, object], bool], expected: bool) -> None:
	attributeCondition: partial[bool] = partial(comparison, getattr(node, field))
	actual: bool = getattr(getattr(Be, identifierClass), f'{field}Is')(attributeCondition)(node)
	assert actual is expected, messageTestFailure(actual, expected, f'Be.{identifierClass}.{field}Is({comparison.__name__}, {getattr(node, field)!r})', node)

# A new `object()` is no attribute of any node, so `is_not` with it is a condition that every attribute satisfies, and `is_` with it
# is a condition that no attribute satisfies.
@given(
	method=strategies.sampled_from(tuple(lookupNodeField.values()))
	, node=strategies.sampled_from(nodesSample)
	, conditionAndResult=strategies.sampled_from(((partial(is_not, object()), True), (partial(is_, object()), False)))
)
def test_BeFieldIsGenerated(method: tuple[str, ast.AST, str], node: ast.AST, conditionAndResult: tuple[partial[bool], bool]) -> None:
	identifierClass, _nodeOfMethod, field = method
	attributeCondition, conditionResult = conditionAndResult
	expected: bool = getattr(ast, identifierClass) in type(node).__mro__ and conditionResult
	actual: bool = getattr(getattr(Be, identifierClass), f'{field}Is')(attributeCondition)(node)
	assert actual is expected, messageTestFailure(actual, expected, f'Be.{identifierClass}.{field}Is(<condition returning {conditionResult}>)', node)
