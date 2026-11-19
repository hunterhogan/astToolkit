from __future__ import annotations

from hunterMakesPy.tests import messageTestFailure
from typing import TYPE_CHECKING
import ast

if TYPE_CHECKING:
	from typing import Any

def assertComparable(actual: ast.AST, expected: ast.AST, function: str, *arguments: Any, **keywordArguments: Any) -> None:
	"""Assert that `ast.compare` finds `actual` and `expected` structurally equal, with a message that reads as the call."""
	# TODO Decide between compare_attributes on assertComparable and assertComparableAttributes when a test needs attributes.
	assert ast.compare(actual, expected), messageTestFailure(ast.dump(actual), ast.dump(expected), function, *arguments, **keywordArguments)
