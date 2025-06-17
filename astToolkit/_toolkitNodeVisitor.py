"""
AST Traversal and Transformation Classes
(AI generated docstring)

This module provides the foundational visitor infrastructure for the astToolkit package, implementing the
antecedent-action pattern through specialized AST traversal classes. These classes enable precise, type-safe AST
operations by combining predicate functions (antecedents) with action functions (consequents).

The antecedent-action pattern forms the conceptual core of astToolkit's design. Antecedents are predicate functions
that identify target nodes using tools like `Be` type guards, `IfThis` predicates, or `ClassIsAndAttribute`
conditions. Actions are consequent functions that specify operations to perform on matched nodes using tools like
`Then` actions, `Grab` transformations, or custom operations.

This module contains two complementary visitor classes that extend Python's built-in AST visitor pattern:

`NodeTourist` extends `ast.NodeVisitor` for read-only AST traversal and information extraction. It applies action
functions to nodes that satisfy predicate conditions, capturing results without modifying the original AST
structure. This class enables analysis workflows, validation operations, and data extraction tasks where the AST
should remain unmodified.

`NodeChanger` extends `ast.NodeTransformer` for destructive AST modification and code transformation. It
selectively transforms nodes that satisfy predicate conditions, enabling targeted changes while preserving overall
tree structure and semantics. This class forms the foundation for code optimization, refactoring, and generation
workflows.

Both classes support generic type parameters for type-safe node matching and result handling, integrating
seamlessly with astToolkit's type system and atomic classes to create composable, maintainable AST manipulation
code.
"""

from astToolkit import 归个, 木
from collections.abc import Callable
from typing import cast, Generic
from typing_extensions import TypeIs
import ast

class NodeTourist(ast.NodeVisitor, Generic[木, 归个]):
    """
    Read-only AST visitor that extracts information from nodes matching predicate conditions.
    (AI generated docstring)

    `NodeTourist` implements the antecedent-action pattern for non-destructive AST analysis. It traverses an AST
    tree, applies predicate functions to identify target nodes, and executes action functions on matches to extract
    or analyze information. The visitor preserves the original AST structure while capturing results from matching
    nodes.

    This class is particularly useful for analysis workflows where you need to gather information about specific
    node types or patterns without modifying the source code structure. The generic type parameters ensure type
    safety when working with specific AST node types and return values.

    Parameters:
            findThis: Predicate function that tests AST nodes. Can return either a `TypeIs` for type narrowing or a
            simple boolean. When using `TypeIs`, the type checker can safely narrow the node type for the action
            function.
            doThat: Action function that operates on nodes matching the predicate. Receives the matched node with
            properly narrowed typing and returns the extracted information.

    Examples:
            Extract all function names from a module:
            ```python
            functionNameCollector = NodeTourist(Be.FunctionDef, lambda functionDef: DOT.name(functionDef))
            functionNames = []
            functionNameCollector.doThat = Then.appendTo(functionNames)
            functionNameCollector.visit(astModule)
            ```

            Find specific function definition:
            ```python
            specificFunction = NodeTourist(IfThis.isFunctionDefIdentifier("targetFunction"), Then.extractIt)
            foundFunction = specificFunction.captureLastMatch(astModule)
            ```
    """

    def __init__(self, findThis: Callable[[ast.AST], TypeIs[木] | bool], doThat: Callable[[木], 归个]) -> None:
        self.findThis = findThis
        self.doThat = doThat
        self.nodeCaptured: 归个 | None = None

    def visit(self, node: ast.AST):
        if self.findThis(node):
            self.nodeCaptured = self.doThat(cast(木, node))
        self.generic_visit(node)

    def captureLastMatch(self, node: ast.AST) -> 归个 | None:
        """
        Visit an AST tree and return the result from the last matching node.
        (AI generated docstring)

        This method provides a convenient interface for single-result extraction workflows. It resets the internal
        capture state, traverses the provided AST tree, and returns the result from the most recently matched node.
        If no nodes match the predicate, returns `None`.

        The method is particularly useful when you expect exactly one match or when you only care about the final
        match in traversal order. For collecting multiple matches, modify the `doThat` action function to append
        results to a collection.

        Parameters:
                node: Root AST node to begin traversal from. Can be any AST node type including modules, functions,
                classes, or expressions.

        Returns:
                lastResult: Result from the action function applied to the last matching node, or `None` if no matches
                were found during traversal.
        """
        self.nodeCaptured = None
        self.visit(node)
        return self.nodeCaptured

class NodeChanger(ast.NodeTransformer, Generic[木, 归个]):
    """
    Destructive AST transformer that selectively modifies nodes matching predicate conditions.
    (AI generated docstring)

    `NodeChanger` implements the antecedent-action pattern for targeted AST transformation. It extends Python's
    `ast.NodeTransformer` to provide precise control over which nodes are modified during tree traversal. The
    transformer applies predicate functions to identify target nodes and executes action functions to perform
    modifications, replacements, or deletions.

    This class forms the foundation for code optimization, refactoring, and generation workflows. Unlike
    `NodeTourist`, `NodeChanger` modifies the AST structure and returns a transformed tree. The transformation
    is applied recursively, ensuring that nested structures are properly processed.

    The class is designed for scenarios where you need to make surgical changes to specific parts of an AST while
    preserving the overall structure and semantics of the code. Common use cases include function inlining,
    variable renaming, dead code elimination, and pattern-based code transformations.

    Parameters:
            findThis: Predicate function that identifies nodes to transform. Should return `True` for nodes that require
            modification and `False` for nodes that should remain unchanged. The function receives an `ast.AST` node
            and determines whether transformation is needed.
            doThat: Action function that performs the actual transformation. Receives nodes that matched the predicate
            and returns the replacement node, modified node, or `None` for deletion. The return value becomes the new
            node in the transformed tree.

    Examples:
            Replace all function calls to a specific function:
            ```python
            callReplacer = NodeChanger(
                    IfThis.isCallIdentifier("oldFunction"),
                    Then.replaceWith(Make.Call(Make.Name("newFunction"), [], []))
            )
            transformedAST = callReplacer.visit(originalAST)
            ```

            Remove all pass statements:
            ```python
            passRemover = NodeChanger(Be.Pass, Then.removeIt)
            cleanedAST = passRemover.visit(originalAST)
            ```
    """

    def __init__(self, findThis: Callable[[ast.AST], TypeIs[木] | bool], doThat: Callable[[木], 归个]) -> None:
        self.findThis = findThis
        self.doThat = doThat

    def visit(self, node: ast.AST):
        if self.findThis(node):
            return self.doThat(cast(木, node))
        return super().visit(node)
