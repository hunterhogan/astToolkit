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
