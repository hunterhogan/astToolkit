"""SSOT for all tests."""

from collections.abc import Iterator
from datetime import datetime, UTC
from functools import cache
from itertools import cycle, islice
from more_itertools import ncycles
from tests.dataSamples.Make import allSubclasses
from typing import Any
import ast
import pytest

antiTests: int = 3

shiftByHour: int = datetime.now(UTC).hour
shiftByDate: int = datetime.now(UTC).day
shiftTotal: int = shiftByHour * shiftByDate + 1


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

# def generateBeNegativeTestData():
# 	for class2test, *list_vsClass in [(C, *list(set(allSubclasses)-{C}-{c.__name__ for c in eval('ast.'+C).__subclasses__()})) for C in allSubclasses]:  # noqa: E501
# 		testName = "class Make, maximally empty parameters"
# 		# Select antiTests elements with shiftTotal spacing, wrapping around
# 		nn = (antiTests * shiftTotal) // len(list_vsClass) + 1
# 		selected_vsClasses = list(islice(ncycles(list_vsClass, nn), 0, len(list_vsClass)*nn, shiftTotal))

# 		for vsClass in selected_vsClasses:
# 			testData = allSubclasses[vsClass][testName]
# 			yield (class2test, vsClass, testName, testData)

@cache
def getTestData(vsClass: str, testName: str):
	return allSubclasses[vsClass][testName]

def generateBeNegativeTestData():  # noqa: ANN201, D103
	for class2test, *list_vsClass in [(C, *list(set(allSubclasses)-{C}-{c.__name__ for c in eval('ast.'+C).__subclasses__()})) for C in allSubclasses]:  # noqa: E501, S307
		testName = "class Make, maximally empty parameters"
		for vsClass in list_vsClass:
			# testData = allSubclasses[vsClass][testName]
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
