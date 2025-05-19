"""
AST Node Transformation Actions for Python Code Manipulation

This module provides the Then class with static methods for generating callable action functions that specify what to do
with AST nodes that match predicates. These action functions are used primarily with NodeChanger and NodeTourist to
transform or extract information from AST nodes.

The module also contains the grab class that provides functions for modifying specific attributes of AST nodes while
preserving their structure, enabling fine-grained control when transforming AST structures.

Together, these classes provide a complete system for manipulating AST nodes once they have been identified using
predicate functions from ifThis.
"""

from astToolkit import 个
from collections.abc import Callable, Sequence
from typing import Any
import ast

class Then:
	"""
	Provide action functions that specify what to do with AST nodes that match predicates.

	The Then class contains static methods that generate action functions used with NodeChanger and NodeTourist to
	transform or extract information from AST nodes that match specific predicates. These actions include node
	replacement, insertion, extraction, and collection operations.

	When paired with predicates from the ifThis class, Then methods complete the pattern-matching-and-action workflow
	for AST manipulation.
	"""
	@staticmethod
	def appendTo(listOfAny: list[Any]) -> Callable[[ast.AST | str], ast.AST | str]:
		def workhorse(node: ast.AST | str) -> ast.AST | str:
			listOfAny.append(node)
			return node
		return workhorse

	@staticmethod
	def extractIt(node: 个) -> 个:
		return node

	@staticmethod
	def insertThisAbove(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		return lambda aboveMe: [*list_astAST, aboveMe]

	@staticmethod
	def insertThisBelow(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		return lambda belowMe: [belowMe, *list_astAST]

	@staticmethod
	def removeIt(_removeMe: ast.AST) -> None:
		return None

	@staticmethod
	def replaceWith(astAST: 个) -> Callable[[个], 个]:
		return lambda _replaceMe: astAST

	@staticmethod
	def updateKeyValueIn(key: Callable[..., Any], value: Callable[..., Any], dictionary: dict[Any, Any]) -> Callable[[ast.AST], dict[Any, Any]]:
		def workhorse(node: ast.AST) -> dict[Any, Any]:
			dictionary.setdefault(key(node), value(node))
			return dictionary
		return workhorse
