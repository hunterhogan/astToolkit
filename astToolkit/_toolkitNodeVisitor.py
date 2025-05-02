"""
Core AST Traversal and Transformation Utilities for Python Code Manipulation

This module provides the foundation for traversing and modifying Python Abstract Syntax Trees (ASTs). It contains two
primary classes:

1. NodeTourist: Implements the visitor pattern to traverse an AST and extract information from nodes that match specific
	predicates without modifying the AST.

2. NodeChanger: Extends ast.NodeTransformer to selectively transform AST nodes that match specific predicates, enabling
	targeted code modifications.

The module also provides utilities for importing modules, loading callables from files, and parsing Python code into AST
structures, creating a complete workflow for code analysis and transformation.
"""

from collections.abc import Callable
from typing import Any, cast, Generic, TypeGuard, TypeVar
import ast
from astToolkit import NodeORattribute, 个, 个return

# TODO Identify the logic that narrows the type and can help the user during static type checking.

class NodeTourist(ast.NodeVisitor, Generic[个, 个return]):
	"""
	Visit and extract information from AST nodes that match a predicate.

	NodeTourist implements the visitor pattern to traverse an AST, applying a predicate function to each node and
	capturing nodes or their attributes when they match. Unlike NodeChanger, it doesn't modify the AST but collects
	information during traversal.

	This class is particularly useful for analyzing AST structures, extracting specific nodes or node properties, and
	gathering information about code patterns.
	"""
	def __init__(self, findThis: Callable[[ast.AST], TypeGuard[个] | bool], doThat: Callable[[个], 个return]) -> None:
		self.findThis = findThis
		self.doThat = doThat
		self.nodeCaptured: 个return | None = None

	def visit(self, node: ast.AST) -> None:
		if self.findThis(node):
			node = cast(个, node)
			self.nodeCaptured = self.doThat(node)
		self.generic_visit(node)

	def captureLastMatch(self, node: ast.AST) -> 个return | None:
		self.nodeCaptured = None
		self.visit(node)
		return self.nodeCaptured

class NodeChanger(ast.NodeTransformer):
	"""
	Transform AST nodes that match a predicate by applying a transformation function.

	NodeChanger is an AST node transformer that applies a targeted transformation to nodes matching a specific
	predicate. It traverses the AST and only modifies nodes that satisfy the predicate condition, leaving other nodes
	unchanged.

	This class extends ast.NodeTransformer and implements the visitor pattern to systematically process and transform an
	AST tree.
	"""
	def __init__(self, findThis: Callable[..., Any], doThat: Callable[..., Any]) -> None:
		self.findThis = findThis
		self.doThat = doThat

	def visit(self, node: ast.AST) -> ast.AST:
		if self.findThis(node):
			return self.doThat(node)
		return super().visit(node)
