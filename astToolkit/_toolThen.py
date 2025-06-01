from astToolkit import 个
from collections.abc import Callable, Sequence
from typing import Any
import ast

class Then:
	"""Action functions for AST node transformations in the antecedent-action pattern.
	(AI generated docstring)

	Provides action functions that serve as consequents in the antecedent-action pattern,
	working with visitor classes like `NodeTourist` and `NodeChanger` as the `doThat` parameter.
	Each method returns: a function that performs a specific operation on AST nodes identified
	by predicate functions from classes like `IfThis` or `Be`.

	The action functions fall into five categories: collection operations for gathering nodes,
	identity operations for extraction without modification, insertion operations for adding
	nodes relative to existing ones, removal operations for deletion, and replacement operations
	for substitution. These actions enable precise AST transformations while maintaining the
	composable nature of the toolkit's architecture.
	"""

	@staticmethod
	def appendTo(listOfAny: list[Any]) -> Callable[[ast.AST | str], ast.AST | str]:
		"""Append matched nodes to a collection while preserving them in the AST.
		(AI generated docstring)

		Creates an action function that adds encountered nodes to the specified list,
		enabling collection of multiple matching nodes during AST traversal. The node
		is returned unchanged, making this suitable for read-only analysis with
		`NodeTourist` where the original AST structure must be preserved.

		Parameters:

			listOfAny: Target collection for accumulating matched nodes

		Returns:

			actionFunction: Function that appends nodes to the list and returns: them unmodified
		"""
		def workhorse(node: ast.AST | str) -> ast.AST | str:
			listOfAny.append(node)
			return node
		return workhorse
	@staticmethod
	def extractIt(node: 个) -> 个:
		"""Extract and return nodes unchanged for identity operations.
		(AI generated docstring)

		Provides the identity action function for the antecedent-action pattern, returning
		nodes exactly as received without modification. Primarily used with `NodeTourist`
		for read-only analysis where the goal is to capture or examine specific nodes
		without altering the AST structure.

		Parameters:

			node: AST node to extract and return unchanged

		Returns:

			identicalNode: The same node passed as input
		"""
		return node
	@staticmethod
	def insertThisAbove(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		"""Insert specified nodes above the matched node in a sequence.
		(AI generated docstring)

		Creates an action function that places the provided AST nodes before the matched
		node, forming a new sequence. Designed for use with `NodeChanger` when adding
		statements or declarations that should precede the target node in the transformed AST.

		Parameters:

			list_astAST: AST nodes to insert above the matched node

		Returns:

			insertionFunction: Function that creates a sequence with new nodes above the target
		"""
		return lambda aboveMe: [*list_astAST, aboveMe]
	@staticmethod
	def insertThisBelow(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		"""Insert specified nodes below the matched node in a sequence.
		(AI generated docstring)

		Creates an action function that places the provided AST nodes after the matched
		node, forming a new sequence. Designed for use with `NodeChanger` when adding
		statements or declarations that should follow the target node in the transformed AST.

		Parameters:

			list_astAST: AST nodes to insert below the matched node

		Returns:

			insertionFunction: Function that creates a sequence with new nodes below the target
		"""
		return lambda belowMe: [belowMe, *list_astAST]
	@staticmethod
	def removeIt(_removeMe: ast.AST) -> None:
		"""Remove matched nodes from the AST through deletion.
		(AI generated docstring)

		Provides the deletion action for the antecedent-action pattern by returning `None`,
		which signals to `NodeChanger` that the matched node should be removed from the AST.
		The parameter name uses an underscore prefix to indicate it will be discarded.

		Parameters:

			_removeMe: AST node to be deleted (parameter ignored)

		Returns:

			None: Signals node deletion to the transformer
		"""
		return None
	@staticmethod
	def replaceWith(astAST: 个) -> Callable[[个], 个]:
		"""Replace matched nodes with a specified replacement node.
		(AI generated docstring)

		Creates an action function that substitutes the matched node with the provided
		replacement node. Essential for refactoring and code transformation workflows
		with `NodeChanger` where specific AST patterns need to be updated or modernized.

		Parameters:

			astAST: Replacement AST node to substitute for matched nodes

		Returns:

			replacementFunction: Function that returns: the replacement node, discarding the original
		"""
		return lambda _replaceMe: astAST
	@staticmethod
	def updateKeyValueIn(key: Callable[..., Any], value: Callable[..., Any], dictionary: dict[Any, Any]) -> Callable[[ast.AST], dict[Any, Any]]:
		"""Update a dictionary with key-value pairs derived from matched nodes.
		(AI generated docstring)

		Creates an action function that extracts information from AST nodes using the
		provided key and value functions, then stores the results in the specified dictionary.
		Uses `setdefault` to avoid overwriting existing entries, making it suitable for
		accumulating data across multiple node matches during traversal.

		Parameters:

			key: Function to extract dictionary keys from matched nodes
			value: Function to extract dictionary values from matched nodes
			dictionary: Target dictionary for storing extracted key-value pairs

		Returns:

			updateFunction: Function that processes nodes and returns: the updated dictionary
		"""
		def workhorse(node: ast.AST) -> dict[Any, Any]:
			dictionary.setdefault(key(node), value(node))
			return dictionary
		return workhorse
