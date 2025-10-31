"""SSOT for all tests."""
# pyright: standard
from astToolkit import Be, Make
from collections.abc import Callable, Iterator
from functools import cache
from tests.dataSamples.Make import allSubclasses
from typing import Any
import ast  # pyright: ignore[reportUnusedImport]
import datetime
import pytest

negativeTestsPerClass: int = 3
stepSize: int = (32 - datetime.date.today().weekday()) * (datetime.date.today().day + 1)

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

def generateBeNegativeTestData() -> Iterator[tuple[str, str, str, dict[str, Any]]]:
	for class2test, *list_vsClass in [(C, *list(set(allSubclasses)-{C}-{c.__name__ for c in eval('ast.'+C).__subclasses__()})) for C in allSubclasses]:  # noqa: S307
		testName = "class Make, maximally empty parameters"

		list_vsClass.sort()
		indexNormalizer: int = len(list_vsClass)
		setIndices: set[int] = set()
		step: int = stepSize
		while len(setIndices) < negativeTestsPerClass:
			setIndices.add(step % indexNormalizer)
			step = step + stepSize + 1

		listIndices: list[int] = sorted(setIndices)

		listTuplesTests: list[tuple[str, str, str, dict[str, Any]]] = [
			(class2test, list_vsClass[index], testName, getTestData(list_vsClass[index], testName))
			for index in listIndices
		]
		yield from listTuplesTests

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

def generateIfThisIdentifierTestCases() -> Iterator[tuple[str, str, Callable[[str], ast.AST], bool]]:
	"""Generate test data for IfThis identifier-based methods using non-contiguous test values."""

	# Using non-contiguous, semantic test values as per instructions
	listTestCases: list[tuple[str, str, Callable[[str], ast.AST], bool]] = [
		# methodNameIfThis, identifierToTest, factoryNodeAST, expectedPredicateResult
		("isNameIdentifier", "variableNorthward", lambda identifierParameter: Make.Name(identifierParameter), True),
		("isNameIdentifier", "variableSouthward", lambda _identifierIgnored: Make.Name("variableNorthward"), False),
		("isFunctionDefIdentifier", "functionEastward", lambda identifierParameter: Make.FunctionDef(name=identifierParameter), True),
		("isFunctionDefIdentifier", "functionWestward", lambda _identifierIgnored: Make.FunctionDef(name="functionEastward"), False),
		("isClassDefIdentifier", "ClassNorthEast", lambda identifierParameter: Make.ClassDef(name=identifierParameter), True),
		("isClassDefIdentifier", "ClassSouthWest", lambda _identifierIgnored: Make.ClassDef(name="ClassNorthEast"), False),
		("isCallIdentifier", "callablePrimary", lambda identifierParameter: Make.Call(Make.Name(identifierParameter)), True),
		("isCallIdentifier", "callableSecondary", lambda _identifierIgnored: Make.Call(Make.Name("callablePrimary")), False),
		("is_argIdentifier", "parameterFibonacci", lambda identifierParameter: Make.arg(identifierParameter), True),
		("is_argIdentifier", "parameterPrime", lambda _identifierIgnored: Make.arg("parameterFibonacci"), False),
		("is_keywordIdentifier", "keywordAlpha", lambda identifierParameter: Make.keyword(identifierParameter, Make.Constant("valueBeta")), True),
		("is_keywordIdentifier", "keywordGamma", lambda _identifierIgnored: Make.keyword("keywordAlpha", Make.Constant("valueBeta")), False),
	]

	yield from listTestCases

def generateIfThisSimplePredicateTestCases() -> Iterator[tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]]:
	"""Generate test data for simple predicate methods using unique test values."""

	listTestCases: list[tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]] = [
		# methodNameIfThis, tupleArgumentsTest, factoryNodeAST, expectedPredicateResult
		("isConstant_value", (233,), lambda: Make.Constant(233), True),  # Fibonacci number
		("isConstant_value", (89,), lambda: Make.Constant(233), False),  # Different Fibonacci number
	]

	yield from listTestCases

def generateIfThisDirectPredicateTestCases() -> Iterator[tuple[str, Callable[[], ast.AST], bool]]:
	"""Generate test data for direct predicate methods that take node directly."""

	listTestCases: list[tuple[str, Callable[[], ast.AST], bool]] = [
		# methodNameIfThis, factoryNodeAST, expectedPredicateResult
		("isAttributeName", lambda: Make.Attribute(Make.Name("objectPrime"), "attributeSecondary"), True),
		("isAttributeName", lambda: Make.Name("objectPrime"), False),
		("isCallToName", lambda: Make.Call(Make.Name("functionTertiary")), True),
		("isCallToName", lambda: Make.Call(Make.Attribute(Make.Name("objectPrime"), "methodQuinary")), False),
	]

	yield from listTestCases

def generateIfThisComplexPredicateTestCases() -> Iterator[tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]]:
	"""Generate test data for complex predicate methods using cardinal directions and primes."""

	listTestCases: list[tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]] = [
		# methodNameIfThis, tupleArgumentsTest, factoryNodeAST, expectedPredicateResult
		("isAttributeNamespaceIdentifier", ("namespacePrimary", "methodNorthward"), lambda: Make.Attribute(Make.Name("namespacePrimary"), "methodNorthward"), True),
		("isAttributeNamespaceIdentifier", ("namespaceSecondary", "methodNorthward"), lambda: Make.Attribute(Make.Name("namespacePrimary"), "methodNorthward"), False),
		("isCallAttributeNamespaceIdentifier", ("namespaceAlpha", "methodEastward"), lambda: Make.Call(Make.Attribute(Make.Name("namespaceAlpha"), "methodEastward")), True),
		("isCallAttributeNamespaceIdentifier", ("namespaceBeta", "methodEastward"), lambda: Make.Call(Make.Attribute(Make.Name("namespaceAlpha"), "methodEastward")), False),
		("isStarredIdentifier", ("argumentsCollection",), lambda: Make.Starred(Make.Name("argumentsCollection")), True),
		("isStarredIdentifier", ("keywordsMapping",), lambda: Make.Starred(Make.Name("argumentsCollection")), False),
		("isSubscriptIdentifier", ("arrayFibonacci",), lambda: Make.Subscript(Make.Name("arrayFibonacci"), Make.Constant(13)), True),
		("isSubscriptIdentifier", ("listPrime",), lambda: Make.Subscript(Make.Name("arrayFibonacci"), Make.Constant(13)), False),
		("isUnaryNotAttributeNamespaceIdentifier", ("objectTarget", "flagEnabled"), lambda: Make.UnaryOp(Make.Not(), Make.Attribute(Make.Name("objectTarget"), "flagEnabled")), True),
		("isUnaryNotAttributeNamespaceIdentifier", ("objectAlternate", "flagEnabled"), lambda: Make.UnaryOp(Make.Not(), Make.Attribute(Make.Name("objectTarget"), "flagEnabled")), False),
	]

	yield from listTestCases

@pytest.fixture(params=list(generateIfThisIdentifierTestCases()), ids=lambda parametersTest: f"{parametersTest[0]}_{parametersTest[1]}_{parametersTest[3]}")
def ifThisIdentifierTestData(request: pytest.FixtureRequest) -> tuple[str, str, Callable[[str], ast.AST], bool]:
	"""Fixture providing test data for identifier-based IfThis methods."""
	return request.param

@pytest.fixture(params=list(generateIfThisSimplePredicateTestCases()), ids=lambda parametersTest: f"{parametersTest[0]}_{parametersTest[3]}")
def ifThisSimplePredicateTestData(request: pytest.FixtureRequest) -> tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]:
	"""Fixture providing test data for simple IfThis predicate methods."""
	return request.param

@pytest.fixture(params=list(generateIfThisDirectPredicateTestCases()), ids=lambda parametersTest: f"{parametersTest[0]}_{parametersTest[2]}")
def ifThisDirectPredicateTestData(request: pytest.FixtureRequest) -> tuple[str, Callable[[], ast.AST], bool]:
	"""Fixture providing test data for direct IfThis predicate methods."""
	return request.param

@pytest.fixture(params=list(generateIfThisComplexPredicateTestCases()), ids=lambda parametersTest: f"{parametersTest[0]}_{parametersTest[3]}")
def ifThisComplexPredicateTestData(request: pytest.FixtureRequest) -> tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]:
	"""Fixture providing test data for complex IfThis predicate methods."""
	return request.param

# transformationTools test fixtures

@pytest.fixture
def moduleSampleFunctions() -> ast.Module:
	"""Fixture providing a module with sample function definitions."""
	return Make.Module([
		Make.FunctionDef(
			name="functionPrimary",
			argumentSpecification=Make.arguments(),
			body=[Make.Return(Make.Constant(233))]  # Fibonacci number
		),
		Make.FunctionDef(
			name="functionSecondary",
			argumentSpecification=Make.arguments(),
			body=[Make.Pass()]
		),
	])

@pytest.fixture
def moduleSampleClasses() -> ast.Module:
	"""Fixture providing a module with sample class definitions."""
	return Make.Module([
		Make.ClassDef(
			name="ClassAlpha",
			body=[Make.Pass()]
		),
		Make.ClassDef(
			name="ClassBeta",
			body=[Make.Pass()]
		),
	])

@pytest.fixture
def moduleSampleAsyncFunctions() -> ast.Module:
	"""Fixture providing a module with sample async function definitions."""
	return Make.Module([
		Make.AsyncFunctionDef(
			name="asyncFunctionNorth",
			argumentSpecification=Make.arguments(),
			body=[Make.Return(Make.Constant(89))]  # Fibonacci number
		),
		Make.AsyncFunctionDef(
			name="asyncFunctionSouth",
			argumentSpecification=Make.arguments(),
			body=[Make.Pass()]
		),
	])

@pytest.fixture
def moduleSampleMixed() -> ast.Module:
	"""Fixture providing a module with mixed definition types."""
	return Make.Module([
		Make.AsyncFunctionDef(
			name="asyncFunctionPrimary",
			argumentSpecification=Make.arguments(),
			body=[Make.Pass()]
		),
		Make.ClassDef(
			name="ClassPrimary",
			body=[Make.Pass()]
		),
		Make.FunctionDef(
			name="functionPrimary",
			argumentSpecification=Make.arguments(),
			body=[Make.Pass()]
		),
	])

@pytest.fixture
def moduleInliningBasic() -> ast.Module:
	"""Fixture providing a module for basic function inlining tests."""
	return Make.Module([
		Make.FunctionDef(
			name="functionHelper",
			argumentSpecification=Make.arguments(),
			body=[Make.Return(Make.Constant(233))]  # Fibonacci number
		),
		Make.FunctionDef(
			name="functionTarget",
			argumentSpecification=Make.arguments(),
			body=[
				Make.Assign(
					targets=[Make.Name("valueHelper", context=Make.Store())],
					value=Make.Call(Make.Name("functionHelper"))
				),
				Make.Return(Make.Name("valueHelper"))
			]
		),
	])

@pytest.fixture
def moduleInliningNone() -> ast.Module:
	"""Fixture providing a module with a function that needs no inlining."""
	return Make.Module([
		Make.FunctionDef(
			name="functionStandalone",
			argumentSpecification=Make.arguments(),
			body=[Make.Return(Make.Constant(377))]  # Fibonacci number
		),
	])

@pytest.fixture
def functionDefUnusedParameters() -> ast.FunctionDef:
	"""Fixture providing a function with unused parameters."""
	return Make.FunctionDef(
		name="functionWithUnused",
		argumentSpecification=Make.arguments(list_arg=[
			Make.arg("parameterUsed"),
			Make.arg("parameterUnused"),
		]),
		body=[
			Make.Assign(
				targets=[Make.Name("resultValue", context=Make.Store())],
				value=Make.Name("parameterUsed")
			),
			Make.Return(Make.Name("resultValue"))
		]
	)

@pytest.fixture
def functionDefAllParametersUsed() -> ast.FunctionDef:
	"""Fixture providing a function with all parameters used."""
	return Make.FunctionDef(
		name="functionAllUsed",
		argumentSpecification=Make.arguments(list_arg=[
			Make.arg("parameterAlpha"),
			Make.arg("parameterBeta"),
		]),
		body=[
			Make.Assign(
				targets=[Make.Name("resultSum", context=Make.Store())],
				value=Make.BinOp(
					left=Make.Name("parameterAlpha"),
					op=Make.Add(),
					right=Make.Name("parameterBeta")
				)
			),
			Make.Return(Make.Name("resultSum"))
		]
	)

@pytest.fixture
def binOpChained() -> ast.BinOp:
	"""Fixture providing a chained binary operation."""
	return Make.BinOp(
		left=Make.BinOp(
			left=Make.Constant(233),  # Fibonacci number
			op=Make.Add(),
			right=Make.Constant(89)  # Fibonacci number
		),
		op=Make.Add(),
		right=Make.Constant(144)  # Fibonacci number
	)

@pytest.fixture
def moduleSampleSimple() -> ast.Module:
	"""Fixture providing a simple module for write tests."""
	module = Make.Module([
		Make.FunctionDef(
			name="functionSimple",
			argumentSpecification=Make.arguments(),
			body=[Make.Return(Make.Constant(610))]  # Fibonacci number
		),
	])
	ast.fix_missing_locations(module)
	return module
