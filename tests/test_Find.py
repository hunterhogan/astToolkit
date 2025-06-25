from astToolkit import Find
from tests.conftest import generateBeTestData
import ast
import pytest

# @pytest.mark.parametrize("identifierClass, subtestName, dictionaryTests", list(generateBeTestData()))
# def test_Find_identifies_class(identifierClass, subtestName, dictionaryTests):
#     node = dictionaryTests["expression"]
#     findClass = Find.__getattribute__(Find(), identifierClass)
#     assert findClass(node)