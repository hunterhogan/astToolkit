"""Parse expression text, replace nodes by unparsed text, and inspect binary operands.

(AI generated docstring)

You can convert Python expression text to an `ast.expr` (***expr***ession), substitute
nodes by matching their unparsed Python text, or collect operands from binary operations.
The expression and text-replacement shortcuts have input and replacement restrictions
described in their docstrings.

Contents
--------
Functions
	pythonCode2ast_expr
		Extract an expression node from Python source text.
	unjoinBinOP
		Collect operands of matching binary operations without changing the tree.
	unparseFindReplace
		Replace matching descendants in a copied AST using their unparsed text.
"""

from __future__ import annotations

from astToolkit import Be, DOT, IfThis, NodeChanger, NodeTourist, Then
from copy import deepcopy
from humpy_cytoolz.functoolz import complement
from hunterMakesPy import raiseIfNone
from typing import TYPE_CHECKING
import ast

if TYPE_CHECKING:
	from collections.abc import Mapping

def pythonCode2ast_expr(string: str) -> ast.expr:
	"""Convert Python expression text to an `ast.expr` (***expr***ession) node.

	(AI generated docstring)

	You can use `pythonCode2ast_expr` as a shortcut for a `str` (***str***ing) containing one
	Python expression. The result is the value of the last `ast.Expr` (***Expr***ession)
	statement in traversal order, including statements inside nested definitions.

	Parameters
	----------
	string : str
		(***str***ing) Python source text. Supply a single expression to obtain that expression
		as the result. A source tree without an `ast.Expr` statement causes a `ValueError`;
		invalid Python syntax causes a `SyntaxError`.

	Returns
	-------
	astExpression : ast.expr
		The `ast.expr` (***expr***ession) value from the last expression statement.

	See Also
	--------
	`astToolkit.Make`
		Construct expression nodes directly with the node factories.
	`astToolkit.filesystem.parsePathFilename2astModule`
		Obtain a complete module tree from a source file.

	Limitations
	-----------
	This prototype shortcut has approximately 482 implied constraints and pitfalls.
	`pythonCode2ast_expr` does not enforce the single-expression input contract. Additional
	statements can be present, and an expression used only as part of an assignment does not
	count as an `ast.Expr` statement. Using `ast.parse` directly provides more control.
	"""
	return raiseIfNone(NodeTourist[ast.AST, ast.expr](Be.Expr, Then.extractIt(DOT.value)).captureLastMatch(ast.parse(string)))

def unparseFindReplace[木: ast.AST, 文件: ast.AST, 文义: ast.AST](astTree: 木, mappingFindReplaceNodes: Mapping[文件, 文义]) -> 木:
	"""Replace AST nodes whose unparsed Python text matches a supplied node.

	(AI generated docstring)

	You can substitute nodes throughout an `ast.AST` (Abstract Syntax Tree) by matching the
	Python source text produced by `ast.unparse`. Matching ignores node identity and can
	equate structurally different nodes that produce the same text.

	Parameters
	----------
	astTree : ast.AST
		(Abstract Syntax Tree) The root of the tree to copy before applying substitutions.
	mappingFindReplaceNodes : Mapping[ast.AST, ast.AST]
		Nodes to find and their replacements. Entries apply in mapping iteration order, and
		a replacement can match a later entry. Substitutions must reach a state where a
		complete pass leaves the tree's unparsed text unchanged.

	Returns
	-------
	newTree : ast.AST
		A deep copy of `astTree` with matching descendants replaced. Replacement nodes are
		inserted directly and can be shared with the supplied mapping. The root retains its
		original concrete type.

	See Also
	--------
	`astToolkit.NodeChanger`
		Express a replacement directly with a predicate and an action.
	`astToolkit.IfThis.astIs`
		Match AST structure rather than unparsed text.

	Replacement Scope
	-----------------
	A matched subtree is replaced as a whole; its descendants are skipped for that substitution.
	Further substitutions can transform inserted nodes. Replacements that continually change
	the unparsed text prevent termination.

	The root itself is not replaced because the returned value from the visitor is discarded.
	Only replacements within the copied root are retained.

	Later substitutions can modify shared replacement nodes, including replacement nodes taken
	from the original tree.
	"""
	keepGoing = True
	newTree: 木 = deepcopy(astTree)

	while keepGoing:
		for nodeFind, nodeReplace in mappingFindReplaceNodes.items():
			NodeChanger(IfThis.unparseIs(nodeFind), Then.replaceWith(nodeReplace)).visit(newTree)

		if ast.unparse(newTree) == ast.unparse(astTree):
			keepGoing = False
		else:
			astTree = deepcopy(newTree)
	return newTree

def unjoinBinOP(astAST: ast.AST, operator: type[ast.operator] = ast.operator) -> list[ast.expr]:
	"""Extract the operands of matching binary operations in traversal order.

	(AI generated docstring)

	You can use `unjoinBinOP` to collect the operands of `ast.BinOp` (***Bin***ary ***Op***eration)
	nodes whose `op` (***op***erator) matches `operator`. Each matching chain is flattened in
	left-to-right order, preserving repeated operands. The search can find separate matching
	operations anywhere in `astAST`.

	Within a matching operation, only operands that are themselves matching `ast.BinOp` nodes
	are split further. Other operands remain complete expressions, including calls, subscripts,
	and binary operations with a different operator. Matching operations inside those complete
	operands are not collected separately. The input tree is unchanged.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The root to search. `astAST` is typically an `ast.BinOp` node,
		but any AST node is accepted.
	operator : type[ast.operator] = ast.operator
		(***op***erator) The class matched against each `ast.BinOp.op` (***op***erator) instance.
		The default `ast.operator` matches all binary operators.

	Returns
	-------
	list_ast_expr : list[ast.expr]
		The original `ast.expr` (***expr***ession) operand nodes in traversal order. An empty
		`list` is returned when no binary operation matches. The nodes are shared with `astAST`.

	See Also
	--------
	`astToolkit.Make.BinOp`
		Construct a binary operation from two operands and an operator.
	"""
	list_ast_expr: list[ast.expr] = []

	findThis = Be.BinOp.opIs(operator.__instancecheck__)
	doThat = NodeChanger[ast.expr, ast.expr](
		IfThis.isAllOf(Be.expr, complement(findThis)), Then.appendTo(list_ast_expr)).visit
	breakingBinOp = NodeChanger(findThis, doThat)

	breakingBinOp.visit(astAST)

	return list_ast_expr
