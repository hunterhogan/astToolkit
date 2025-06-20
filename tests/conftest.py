from collections.abc import Iterator
from random import sample
from tests.dataSamples.Make import allSubclasses
from typing import Any
import pytest

antiTests: int = 1

def generateBeTestData() -> Iterator[tuple[str, str, dict[str, Any]]]:
    for identifierClass, dictionaryClass in allSubclasses.items():
        for subtestName, dictionaryTests in dictionaryClass.items():
            yield (identifierClass, subtestName, dictionaryTests)

def generateBeNegativeTestData() -> Iterator[tuple[str, str, str, dict[str, Any]]]:
    for identifierClass in allSubclasses:
        for vsClass in sample(list(allSubclasses.keys()), antiTests):
            for subtestName, dictionaryTests in allSubclasses[vsClass].items():
                yield (identifierClass, vsClass, subtestName, dictionaryTests)

    # for class2test, *list_vsClass in [(subclass,) + random_combination(set(allSubclasses)-{subclass}, antiTests) for subclass in allSubclasses]:
    #     for vsClass, (testName, testData) in itertools.product(list_vsClass, allSubclasses[class2test].items()):
    #         yield (class2test, vsClass, testName, testData)

@pytest.fixture(params=list(generateBeTestData()), ids=lambda param: f"{param[0]}_{param[1]}")
def beTestData(request: pytest.FixtureRequest) -> tuple[str, str, dict[str, Any]]:
    return request.param

@pytest.fixture(params=list(generateBeNegativeTestData()), ids=lambda param: f"{param[0]}_IsNot_{param[1]}_{param[2]}")
def beNegativeTestData(request: pytest.FixtureRequest) -> tuple[str, str, str, dict[str, Any]]:
    return request.param