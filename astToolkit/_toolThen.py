from collections.abc import Callable, Mapping, Sequence
from typing import Any
import ast

class Then:
	"""Apply an action to a `node`, especially in the antecedent-action pattern of `NodeTourist` and `NodeChanger`.

	Keep the `node`:
	- `appendTo()` a list your provide.
	- `extractIt()` as a return value.
	- `updateKeyValueIn()` a dictionary you provide.

	Change the `node`:
	- `insertThisAbove()` the `node`.
	- `insertThisBelow()` the `node`.
	- `removeIt()`.
	- `replaceWith()` an `ast.AST` or appropriate `object`.

	"""

	@staticmethod
	def appendTo[个](listOfAny: list[Any]) -> Callable[[个],  个]:
		"""Append matched nodes to a collection while preserving them in the AST.

		(AI generated docstring)

		Creates an action function that adds encountered nodes to the specified list, enabling collection of multiple matching
		nodes during AST traversal. The node is returned unchanged, making this suitable for read-only analysis with `NodeTourist`
		where the original AST structure must be preserved.

		Parameters
		----------
		listOfAny : list[Any]
			Target collection for accumulating matched nodes.

		Returns
		-------
		actionFunction : Callable[[个], 个]
			Function that appends nodes to the list and returns them unmodified.

		"""
		def workhorse(node: 个) -> 个:
			listOfAny.append(node)
			return node
		return workhorse

	@staticmethod
	def extractIt[个](node: 个) -> 个:
		"""Extract and return nodes unchanged for identity operations.

		(AI generated docstring)

		Provides the identity action function for the antecedent-action pattern, returning nodes exactly as received without
		modification. Primarily used with `NodeTourist` for read-only analysis where the goal is to capture or examine specific
		nodes without altering the AST structure.

		Parameters
		----------
		node : 个
			AST node to extract and return unchanged.

		Returns
		-------
		identicalNode : 个
			The same node passed as input.

		"""
		return node

	@staticmethod
	def insertThisAbove(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		"""Create a list of `ast.AST` with `list_astAST` above the matched node.

		By physically inserting the list of `ast.AST` subclasses before the matched node, the list will logical precede the
		matched node.

		Parameters
		----------
		list_astAST : Sequence[ast.AST]
			A list of one or more `ast.AST` subclasses to effectively insert above the matched node.

		Returns
		-------
		insertionFunction : Callable[[ast.AST], Sequence[ast.AST]]
			Function that creates a sequence with new nodes above the target.

		"""
		return lambda aboveMe: [*list_astAST, aboveMe]

	@staticmethod
	def insertThisBelow(list_astAST: Sequence[ast.AST]) -> Callable[[ast.AST], Sequence[ast.AST]]:
		"""Insert specified nodes below the matched node in a sequence.

		(AI generated docstring)

		Creates an action function that places the provided AST nodes after the matched node, forming a new sequence. Designed for
		use with `NodeChanger` when adding statements or declarations that should follow the target node in the transformed AST.

		Parameters
		----------
		list_astAST : Sequence[ast.AST]
			AST nodes to insert below the matched node.

		Returns
		-------
		insertionFunction : Callable[[ast.AST], Sequence[ast.AST]]
			Function that creates a sequence with new nodes below the target.

		"""
		return lambda belowMe: [belowMe, *list_astAST]

	@staticmethod
	def removeIt(_removeMe: ast.AST) -> None:
		"""Remove matched nodes from the AST through deletion.

		(AI generated docstring)

		Provides the deletion action for the antecedent-action pattern by returning `None`, which signals to `NodeChanger` that
		the matched node should be removed from the AST. The parameter name uses an underscore prefix to indicate it will be
		discarded.

		Parameters
		----------
		_removeMe : ast.AST
			AST node to be deleted (parameter ignored).

		Returns
		-------
		None
			Signals node deletion to the transformer.

		"""
		return

	@staticmethod
	def replaceWith[归个](this: 归个) -> Callable[[Any], 归个]:
		"""Replace matched nodes with a specified replacement node.

		(AI generated docstring)

		Creates an action function that substitutes the matched node with the provided replacement node. Essential for refactoring
		and code transformation workflows with `NodeChanger` where specific AST patterns need to be updated or modernized.

		Parameters
		----------
		this : 归个
			Replacement AST node to substitute for matched nodes.

		Returns
		-------
		replacementFunction : Callable[[Any], 归个]
			Function that returns the replacement node, discarding the original.

		"""
		return lambda _replaceMe: this

	@staticmethod
	def updateKeyValueIn[个, 文件, 文义](key: Callable[[个], 文件], value: Callable[[个], 文义], dictionary: dict[文件, 文义]) -> Callable[[个], Mapping[文件, 文义]]:
		"""Update a dictionary with key-value pairs derived from matched nodes.

		(AI generated docstring)

		Creates an action function that extracts information from AST nodes using the provided key and value functions, then
		stores the results in the specified dictionary. Uses `setdefault` to avoid overwriting existing entries, making it
		suitable for accumulating data across multiple node matches during traversal.

		Parameters
		----------
		key : Callable[[个], 文件]
			Function to extract dictionary keys from matched nodes.
		value : Callable[[个], 文义]
			Function to extract dictionary values from matched nodes.
		dictionary : dict[文件, 文义]
			Target dictionary for storing extracted key-value pairs.

		Returns
		-------
		updateFunction : Callable[[个], Mapping[文件, 文义]]
			Function that processes nodes and returns the updated dictionary.

		"""
		def workhorse(node: 个) -> dict[文件, 文义]:
			dictionary.setdefault(key(node), value(node))
			return dictionary
		return workhorse
