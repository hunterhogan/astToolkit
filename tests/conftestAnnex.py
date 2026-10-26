from __future__ import annotations

from itertools import starmap
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from typing import Any

#================== Assert scalar and built-in containers ========================================================================

def assertEqualTo[个](actual: 个, expected: 个, function: str, *arguments: Any, **keywordArguments: Any) -> None:
	"""Assert that two objects are equal, and if not, raise an AssertionError with a detailed message."""
	assert actual == expected, messageTestFailure(actual, expected, function, *arguments, **keywordArguments)

def assert_approx[个](actual: 个, expected: 个, pytest_rel: float, pytest_abs: float, function: str, *arguments: Any, **keywordArguments: Any) -> None:
	assert actual == pytest.approx(expected, pytest_rel, pytest_abs, nan_ok=True), messageTestFailure(actual, expected, function, *arguments, **keywordArguments)

def messageTestFailure(actual: Any, expected: Any, function: str, *arguments: Any, **keywordArguments: Any) -> str:
	"""Format assertion message for any test comparison."""
	parameters: list[str] = [*map(repr, arguments), *starmap('{}={!r}'.format, keywordArguments.items())]
	return f'{function}({", ".join(parameters)}) = {actual!r}, but {expected = }.'
