"""AST Traversal and Transformation Classes.

(AI generated docstring)

This module provides the foundational visitor infrastructure for the astToolkit package, implementing
the antecedent-action pattern through specialized AST traversal classes. These classes enable precise,
type-safe AST operations by combining predicate functions (antecedents) with action functions
(consequents).

The antecedent-action pattern forms the conceptual core of astToolkit's design. Antecedents are
predicate functions that identify target nodes using tools like `Be` type guards, `IfThis` predicates.
Actions are consequent functions that specify operations to perform on matched nodes using tools like
`Then` actions, `Grab` transformations, or custom operations.

This module contains two complementary visitor classes that extend Python's built-in AST visitor
pattern:

`NodeTourist` extends `ast.NodeVisitor` for read-only AST traversal and information extraction. It
applies action functions to nodes that satisfy predicate conditions, capturing results without
modifying the original AST structure. This class enables analysis workflows, validation operations,
and data extraction tasks where the AST should remain unmodified.

`NodeChanger` extends `ast.NodeTransformer` for destructive AST modification and code transformation.
It selectively transforms nodes that satisfy predicate conditions, enabling targeted changes while
preserving overall tree structure and semantics. This class forms the foundation for code
optimization, refactoring, and generation workflows.

Both classes support generic type parameters for type-safe node matching and result handling,
integrating seamlessly with astToolkit's type system and atomic classes to create composable,
maintainable AST manipulation code.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import overload, TYPE_CHECKING
import ast

if TYPE_CHECKING:
	from collections.abc import Callable
	from typing import Final, TypeGuard, TypeIs

class NodeTourist[木: ast.AST, 归个](ast.NodeVisitor):
	"""Read and collect information from AST nodes that match a predicate.

	(AI generated docstring)

	`NodeTourist` implements the antecedent-action pattern for non-destructive AST analysis. It
	traverses an AST tree, applies predicate functions to identify target nodes, and executes action
	functions on matches to extract or analyze information. The visitor preserves the original AST
	structure while capturing results from matching nodes.

	This class is particularly useful for analysis workflows where you need to gather information
	about specific node types or patterns without modifying the source code structure. The generic
	type parameters ensure type safety when working with specific AST node types and return values.

	Attributes
	----------
	findThis : Callable[[ast.AST], bool]
		Predicate supplied at construction. A `TypeIs` or `TypeGuard` predicate identifies the
		matched node type for the action.
	doThat : Callable[[木], 归个]
		Action supplied at construction. The action receives the matched node and returns the
		information to capture. Use `DOT` getters to read attributes without changing the AST.
	nodeCaptured : 归个 | None = None
		Result from the most recent matching node. `captureLastMatch` resets this value before
		each search; `visit` leaves the previous value intact when no node matches.

	See Also
	--------
	`NodeChanger`
		Replace or remove nodes, or transform their attributes.
	`astToolkit.IfThis.isAllOf`
		Require several conditions on the same node.

	Nested Visitors
	---------------
	You can use an inner visitor's bound method as the outer visitor's `doThat`. The outer
	`findThis` selects a node, and the inner visitor searches that node and its descendants.
	Both predicates can match the starting node, but the inner predicate can also match nodes
	deeper in the selected subtree. This differs from `IfThis.isAllOf`, which gives every
	predicate the same node. Attribute predicates such as
	`Be.Assign.valueIs(IfThis.isCallIdentifier(identifier))` select an assignment by its value;
	the selected node is still the assignment.

	Use the inner `captureLastMatch` method when the outer visitor should capture a result from
	each selected subtree. The inner search resets its capture for each subtree. The outer
	`captureLastMatch` then returns the inner result for the last outer match, which can be
	`None` even when an earlier subtree contained a match. The inner `visit` method returns
	`None`; use that method when the inner action collects results in a supplied container.

	The outer visitor still searches descendants after its action finishes. If two outer matches
	contain the same descendant, the inner visitor searches that descendant more than once.
	Collection actions can therefore record duplicates. Choose the outer predicate according to
	the intended search scope; nesting does not restrict a search to direct children.

	Examples
	--------
	Combine the argument and annotation searches used to find a state dataclass identifier.
	The result is `'StateMapFolding'` for this annotated argument.

		```python
		from astToolkit import Be, DOT, Make, NodeTourist
		from typing import TYPE_CHECKING

		if TYPE_CHECKING:
			import ast

		ast_arg: ast.arg = Make.arg('state', Make.Name('StateMapFolding'))
		readIdentifier = NodeTourist(Be.Name, DOT.id)
		identifierDataclass: str | None = NodeTourist(
			Be.arg, readIdentifier.captureLastMatch).captureLastMatch(ast_arg)
		```
	"""

	@overload
	def __init__(self, findThis: Callable[[ast.AST], TypeIs[木]], doThat: Callable[[木], 归个]) -> None: ...
	@overload
	def __init__(self, findThis: Callable[[ast.AST], TypeGuard[木]], doThat: Callable[[木], 归个]) -> None: ...
	@overload
	def __init__(self, findThis: Callable[[ast.AST], bool], doThat: Callable[[ast.AST], 归个]) -> None: ...
	def __init__(self, findThis: Callable[[ast.AST], bool], doThat: Callable[[木], 归个]) -> None:
		self.findThis: Final[Callable[[ast.AST], bool]] = findThis
		self.doThat: Callable[[木], 归个] = doThat
		self.nodeCaptured: 归个 | None = None

	def _matches(self, node: ast.AST) -> TypeGuard[木]:
		return self.findThis(node)

	def visit(self, node: ast.AST) -> None:
		"""Apply predicate and action functions during AST traversal.

		(AI generated docstring)

		Overrides the base `ast.NodeVisitor.visit` method to implement the antecedent-action pattern.
		For each node visited during traversal, this method applies the predicate function
		(`findThis`) to test whether the node matches the desired criteria. If the predicate returns
		`True`, the action function (`doThat`) is applied to the node and the result is captured in
		`nodeCaptured`.

		The method continues standard AST traversal by calling `generic_visit` to ensure all child
		nodes are processed recursively. This preserves the complete tree traversal behavior while
		adding the predicate- action functionality.

		Parameters
		----------
		node : ast.AST
			AST node to test and potentially process during traversal.
		"""
		if self._matches(node):
			self.nodeCaptured = self.doThat(node)
		self.generic_visit(node)

	def captureLastMatch(self, node: ast.AST) -> 归个 | None:
		"""Visit an AST tree and return the result from the last matching node.

		(AI generated docstring)

		This method provides a convenient interface for single-result extraction workflows. It resets
		the internal capture state, traverses the provided AST tree, and returns the result from the
		most recently matched node. If no nodes match the predicate, returns `None`.

		The method is particularly useful when you expect exactly one match or when you only care
		about the final match in traversal order. For collecting multiple matches, modify the `doThat`
		action function to append results to a collection.

		Parameters
		----------
		node : ast.AST
			Root AST node to begin traversal from. Can be any AST node type including modules,
			functions, classes, or expressions.

		Returns
		-------
		lastResult : 归个 | None
			Result from the action function applied to the last matching node, or `None` if no matches
			were found during traversal.

		"""
		self.nodeCaptured = None
		self.visit(node)
		return self.nodeCaptured

class NodeChanger[木: ast.AST, 归木: ast.AST | Iterable[ast.AST] | None](ast.NodeTransformer):
	"""Transform AST nodes that match a predicate.

	(AI generated docstring)

	`NodeChanger` implements the antecedent-action pattern for targeted AST transformation. It extends
	Python's `ast.NodeTransformer` to provide precise control over which nodes are modified during
	tree traversal. The transformer applies predicate functions to identify target nodes and executes
	action functions to perform modifications, replacements, or deletions.

	This class forms the foundation for code optimization, refactoring, and generation workflows.
	Unlike `NodeTourist`, `NodeChanger` modifies the AST structure and returns a transformed tree. The
	visitor searches recursively until a node matches, then delegates that subtree to its action.

	The class is designed for scenarios where you need to make surgical changes to specific parts of
	an AST while preserving the overall structure and semantics of the code. Common use cases include
	function inlining, variable renaming, dead code elimination, and pattern-based code
	transformations.

	Attributes
	----------
	findThis : Callable[[ast.AST], bool]
		Predicate supplied at construction. A `TypeIs` or `TypeGuard` predicate identifies the
		matched node type for the action.
	doThat : Callable[[木], 归木]
		Action supplied at construction. Return the modified node, a replacement node, or `None`
		for removal. Statement-list positions also accept an iterable of replacement statements.

	See Also
	--------
	`NodeTourist`
		Read or collect nodes without replacing them.
	`astToolkit.IfThis.isAllOf`
		Require several conditions on the same node.

	Nested Visitors
	---------------
	You can use an inner `NodeChanger` object's bound `visit` method as the outer visitor's
	`doThat`. The outer predicate selects a node, and the inner visitor starts its search at
	that node. The inner visitor's return value becomes the outer action's result, so a
	replacement or removal propagates to the containing tree.

	A match ends the outer visitor's search within that subtree. The outer visitor does not
	automatically visit the matched node's children or the action's returned replacement.
	The inner visitor controls further traversal. If its starting node matches, the inner
	action runs without visiting children. Otherwise, the inner visitor searches descendants,
	even when its predicate rejects the starting node. Nesting therefore differs from
	`IfThis.isAllOf`, whose conditions must hold on the same node.

	Use nested visitors when a selected subtree needs a separate transformation. Searches inside
	a selected function also reach decorators, annotations, and nested definitions unless the
	inner visitor's predicates or actions limit that scope. Use attribute predicates to select a
	parent by an attribute, such as `Be.Assign.valueIs(IfThis.isCallIdentifier(identifier))`.
	The action still receives the assignment. To transform only that assignment's value, use
	`Grab.valueAttribute(innerVisitor.visit)` as the outer action. `Grab` retains the assignment
	and assigns the inner result to its `value` attribute.

	Examples
	--------
	Insert a state update after `tuple()` expressions in a selected counting function, following
	the module-generation transformation used for pruning. The outer visitor selects `count`;
	the inner visitor inserts `astAssign_shortcut` after the expression in that function.

		```python
		from astToolkit import Be, IfThis, Make, NodeChanger, Then
		from typing import TYPE_CHECKING

		if TYPE_CHECKING:
			import ast

		astAssign_shortcut: ast.Assign = Make.Assign(
			[Make.Name('state', Make.Store())]
			, Make.Call(Make.Name('prune'), [Make.Name('state')]))
		astModule: ast.Module = Make.Module([
			Make.FunctionDef('count', body=[Make.Expr(Make.Call(Make.Name('tuple'), []))])])
		insertShortcut = NodeChanger(
			Be.Expr.valueIs(IfThis.isCallIdentifier('tuple'))
			, Then.insertThisBelow([astAssign_shortcut]))
		NodeChanger(
			Be.FunctionDef.nameIs(IfThis.isIdentifier('count'))
			, insertShortcut.visit).visit(astModule)
		```
	"""

	@overload
	def __init__(self, findThis: Callable[[ast.AST], TypeIs[木]], doThat: Callable[[木], 归木]) -> None: ...
	@overload
	def __init__(self, findThis: Callable[[ast.AST], TypeGuard[木]], doThat: Callable[[木], 归木]) -> None: ...
	@overload
	def __init__(self, findThis: Callable[[ast.AST], bool], doThat: Callable[[ast.AST], 归木]) -> None: ...
	def __init__(self, findThis: Callable[[ast.AST], bool], doThat: Callable[[木], 归木]) -> None:
		self.findThis: Final[Callable[[ast.AST], bool]] = findThis
		self.doThat: Callable[[木], 归木] = doThat

	def _matches(self, node: ast.AST) -> TypeGuard[木]:
		return self.findThis(node)

	def visit(self, node: ast.AST) -> 归木 | ast.AST:
		"""Apply predicate and action functions during AST transformation.

		(AI generated docstring)

		Overrides the base `ast.NodeTransformer.visit` method to implement the antecedent-action
		pattern for destructive AST modification. For each node visited during traversal, this method
		applies the predicate function (`findThis`) to test whether the node should be transformed.

		If the predicate returns `True`, the action function (`doThat`) is applied to the node to
		perform the transformation. The action function may return a replacement node, a modified
		version of the original node, or `None` to delete the node from the tree. The matched node's
		children and the returned replacement are visited only if the action arranges that traversal.

		If the predicate returns `False`, the method delegates to the parent `visit` method to
		continue standard transformation traversal, ensuring all child nodes are processed
		recursively.

		Parameters
		----------
		node : ast.AST
			AST node to test and potentially transform during traversal.

		Returns
		-------
		transformedNode : 归木 | ast.AST
			The result of applying the action function if the predicate matches, otherwise the result
			of standard transformation traversal. Returns `None` if the node should be deleted.
		"""
		if self._matches(node):
			return self.doThat(node)
		return super().visit(node)
