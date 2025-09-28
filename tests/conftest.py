"""SSOT for all tests."""

from collections.abc import Iterator
from functools import cache
from tests.dataSamples.Make import allSubclasses
from typing import Any
import ast  # pyright: ignore[reportUnusedImport]
import pytest

def generateBeTestData() -> Iterator[tuple[str, str, dict[str, Any]]]:
	"""Yield test data for positive Be tests. (AI generated docstring).

	Yields
	------
	identifierClass : str
			Name of the class under test.
	subtestName : str
			Name of the subtest case.
	dictionaryTests : dict[str, Any]
			Dictionary containing test data for the subtest.

	"""
	for identifierClass, dictionaryClass in allSubclasses.items():
		for subtestName, dictionaryTests in dictionaryClass.items():
			yield (identifierClass, subtestName, dictionaryTests)

@cache
def getTestData(vsClass: str, testName: str) -> dict[str, Any]:
	return allSubclasses[vsClass][testName]

def generateBeNegativeTestData():  # noqa: ANN201
	for class2test, *list_vsClass in [(C, *list(set(allSubclasses)-{C}-{c.__name__ for c in eval('ast.'+C).__subclasses__()})) for C in allSubclasses]:  # noqa: S307
		testName = "class Make, maximally empty parameters"
		for vsClass in list_vsClass:
			testData = getTestData(vsClass, testName)
			yield (class2test, vsClass, testName, testData)

@pytest.fixture(params=list(generateBeTestData()), ids=lambda param: f"{param[0]}_{param[1]}")
def beTestData(request: pytest.FixtureRequest) -> tuple[str, str, dict[str, Any]]:
	"""Fixture providing positive Be test data. (AI generated docstring).

	Parameters
	----------
	request : pytest.FixtureRequest
			Pytest request object for the fixture.

	Returns
	-------
	tuple[str, str, dict[str, Any]]
			Tuple containing identifierClass, subtestName, and dictionaryTests.

	"""
	return request.param

@pytest.fixture(params=list(generateBeNegativeTestData()), ids=lambda param: f"{param[0]}_IsNot_{param[1]}_{param[2]}")  # pyright: ignore[reportArgumentType]
def beNegativeTestData(request: pytest.FixtureRequest) -> tuple[str, str, str, dict[str, Any]]:
	"""Fixture providing negative Be test data. (AI generated docstring).

	Parameters
	----------
	request : pytest.FixtureRequest
			Pytest request object for the fixture.

	Returns
	-------
	tuple[str, str, str, dict[str, Any]]
			Tuple containing identifierClass, vsClass, subtestName, and dictionaryTests.

	"""
	return request.param


# IfThis test data and fixtures

def generateIdentifierTestData():
	"""Generate test data for IfThis identifier-based methods."""
	from astToolkit import Make
	
	# Basic identifier patterns
	test_cases = [
		# (method_name, test_identifier, node_factory, expected_result)
		("isNameIdentifier", "test_var", lambda id: Make.Name(id), True),
		("isNameIdentifier", "different_var", lambda id: Make.Name("test_var"), False),
		("isFunctionDefIdentifier", "test_func", lambda id: Make.FunctionDef(name=id), True),
		("isFunctionDefIdentifier", "other_func", lambda id: Make.FunctionDef(name="test_func"), False),
		("isClassDefIdentifier", "TestClass", lambda id: Make.ClassDef(name=id), True),
		("isClassDefIdentifier", "OtherClass", lambda id: Make.ClassDef(name="TestClass"), False),
		("isCallIdentifier", "print", lambda id: Make.Call(callee=Make.Name(id)), True),
		("isCallIdentifier", "input", lambda id: Make.Call(callee=Make.Name("print")), False),
		("is_argIdentifier", "param", lambda id: Make.arg(id), True),
		("is_argIdentifier", "other_param", lambda id: Make.arg("param"), False),
		("is_keywordIdentifier", "key", lambda id: Make.keyword(id, Make.Constant("value")), True),
		("is_keywordIdentifier", "other_key", lambda id: Make.keyword("key", Make.Constant("value")), False),
	]
	
	for method_name, test_id, node_factory, expected in test_cases:
		yield (method_name, test_id, node_factory, expected)

def generateSimplePredicateTestData():
	"""Generate test data for simple predicate methods."""
	from astToolkit import Make, Be
	
	test_cases = [
		# (method_name, test_args, node_factory, expected_result)
		("isConstant_value", (42,), lambda: Make.Constant(42), True),
		("isConstant_value", (24,), lambda: Make.Constant(42), False),
	]
	
	for method_name, args, node_factory, expected in test_cases:
		yield (method_name, args, node_factory, expected)

def generateDirectPredicateTestData():
	"""Generate test data for direct predicate methods that take node directly."""
	from astToolkit import Make
	
	test_cases = [
		# (method_name, node_factory, expected_result)
		("isAttributeName", lambda: Make.Attribute(Make.Name("obj"), "attr"), True),
		("isAttributeName", lambda: Make.Name("obj"), False),
		("isCallToName", lambda: Make.Call(callee=Make.Name("func")), True),
		("isCallToName", lambda: Make.Call(callee=Make.Attribute(Make.Name("obj"), "method")), False),
	]
	
	for method_name, node_factory, expected in test_cases:
		yield (method_name, node_factory, expected)

def generateComplexPredicateTestData():
	"""Generate test data for complex predicate methods."""
	from astToolkit import Make
	
	test_cases = [
		# (method_name, test_args, node_factory, expected_result)
		("isAttributeNamespaceIdentifier", ("obj", "method"), lambda: Make.Attribute(Make.Name("obj"), "method"), True),
		("isAttributeNamespaceIdentifier", ("other_obj", "method"), lambda: Make.Attribute(Make.Name("obj"), "method"), False),
		("isCallAttributeNamespaceIdentifier", ("obj", "method"), lambda: Make.Call(callee=Make.Attribute(Make.Name("obj"), "method")), True),
		("isCallAttributeNamespaceIdentifier", ("other_obj", "method"), lambda: Make.Call(callee=Make.Attribute(Make.Name("obj"), "method")), False),
		("isStarredIdentifier", ("args",), lambda: Make.Starred(value=Make.Name("args")), True),
		("isStarredIdentifier", ("kwargs",), lambda: Make.Starred(value=Make.Name("args")), False),
		("isSubscriptIdentifier", ("arr",), lambda: Make.Subscript(value=Make.Name("arr"), slice=Make.Constant(0)), True),
		("isSubscriptIdentifier", ("list",), lambda: Make.Subscript(value=Make.Name("arr"), slice=Make.Constant(0)), False),
		("isUnaryNotAttributeNamespaceIdentifier", ("obj", "flag"), lambda: Make.UnaryOp(op=Make.Not(), operand=Make.Attribute(Make.Name("obj"), "flag")), True),
		("isUnaryNotAttributeNamespaceIdentifier", ("other_obj", "flag"), lambda: Make.UnaryOp(op=Make.Not(), operand=Make.Attribute(Make.Name("obj"), "flag")), False),
	]
	
	for method_name, args, node_factory, expected in test_cases:
		yield (method_name, args, node_factory, expected)

@pytest.fixture(params=list(generateIdentifierTestData()), ids=lambda param: f"{param[0]}_{param[1]}_{param[3]}")
def identifierTestData(request):
	"""Fixture providing test data for identifier-based IfThis methods."""
	return request.param

@pytest.fixture(params=list(generateSimplePredicateTestData()), ids=lambda param: f"{param[0]}_{param[3]}")
def simplePredicateTestData(request):
	"""Fixture providing test data for simple IfThis predicate methods."""
	return request.param

@pytest.fixture(params=list(generateDirectPredicateTestData()), ids=lambda param: f"{param[0]}_{param[2]}")
def directPredicateTestData(request):
	"""Fixture providing test data for direct IfThis predicate methods."""
	return request.param

@pytest.fixture(params=list(generateComplexPredicateTestData()), ids=lambda param: f"{param[0]}_{param[3]}")
def complexPredicateTestData(request):
	"""Fixture providing test data for complex IfThis predicate methods."""
	return request.param
