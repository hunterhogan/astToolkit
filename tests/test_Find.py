"""Not every module needs a docstring."""
from astToolkit import Find
from tests.conftest import generateBeTestData
from typing import Any, TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	import ast

# @pytest.mark.parametrize("identifierClass, subtestName, dictionaryTests", list(generateBeTestData()))  # noqa: PT006
# def test_Find_identifies_class(identifierClass: str, subtestName: str, dictionaryTests: dict[str, Any]) -> None:  # noqa: ARG001
# 	"""test_Find_identifies_class."""
# 	node: ast.AST = dictionaryTests["expression"]
# 	ww = eval(f"Find.{identifierClass}")
# 	assert ww(node)
