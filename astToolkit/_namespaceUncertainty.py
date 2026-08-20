"""IDK how I want to organize the namespace."""
from __future__ import annotations

from astToolkit import Be, DOT, Grab, IfThis, NodeChanger, NodeTourist, Then
from copy import deepcopy
from hunterMakesPy import raiseIfNone
from typing import TYPE_CHECKING
import ast

if TYPE_CHECKING:
	from collections.abc import Mapping

def pythonCode2ast_expr(string: str) -> ast.expr:
	"""Convert a single Python expression `str` (***str***ing) to an `ast.expr` (***expr***ession) node.

	(AI generated docstring)

	You can use `pythonCode2ast_expr` to parse a `str` containing exactly one Python expression into
	an `ast.expr` node. `pythonCode2ast_expr` parses `string` using `ast.parse` [1], then extracts
	the value of the first `ast.Expr` (***Expr***ession) statement node. See `Make.expr` [2] for an
	approximate list of applicable `ast.expr` subclasses.

	Parameters
	----------
	string : str
		(***str***ing) A `str` containing exactly one Python expression. `string` must be a valid
		Python expression that `ast.parse` [1] can parse into a single `ast.Expr` statement node.

	Returns
	-------
	astExpression : ast.expr
		The `ast.expr` (***expr***ession) node extracted from `string`.

	Limitations
	-----------
	This prototype shortcut has approximately 482 implied constraints and pitfalls. If `string` does
	not produce a single `ast.Expr` statement, `pythonCode2ast_expr` will raise a `ValueError` via
	`raiseIfNone` [3]. When the shortcut does not behave as expected, using `ast.parse` [1] directly
	will provide more control.

	References
	----------
	[1] ast.parse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.parse
	[2] astToolkit Make.expr - Context7
		https://context7.com/hunterhogan/asttoolkit
	[3] hunterMakesPy raiseIfNone - Context7
		https://context7.com/hunterhogan/huntermakespy
	"""
	return raiseIfNone(NodeTourist[ast.AST, ast.expr](Be.Expr, Then.extractIt(DOT.value)).captureLastMatch(ast.parse(string)))

def unparseFindReplace[木: ast.AST, 文件: ast.AST, 文义: ast.AST](astTree: 木, mappingFindReplaceNodes: Mapping[文件, 文义]) -> 木:
	"""Replace `ast.AST` (Abstract Syntax Tree) nodes in `astTree` using a find-replace `Mapping`.

	(AI generated docstring)

	You can use `unparseFindReplace` to substitute nodes throughout an `ast.AST` tree by comparing
	unparsed text representations. `unparseFindReplace` iterates the replacement pass until the
	unparsed form of `astTree` no longer changes, ensuring all matching nodes are replaced
	regardless of nesting depth. `unparseFindReplace` does not modify `astTree` in place; it
	returns a modified deep copy of the same type.

	Parameters
	----------
	astTree : ast.AST
		(abstract syntax tree) The root `ast.AST` `object` whose nodes `unparseFindReplace` will
		replace. `astTree` is not modified in place.
	mappingFindReplaceNodes : Mapping[ast.AST, ast.AST]
		A `Mapping` from source `ast.AST` nodes to replacement `ast.AST` nodes. Each entry
		specifies one find-replace substitution.

	Returns
	-------
	newTree : ast.AST
		A deep copy of `astTree`, of the same concrete type as `astTree`, with all nodes matching
		keys in `mappingFindReplaceNodes` replaced by their corresponding values.

	Algorithm Details
	-----------------
	`unparseFindReplace` compares nodes by their unparsed text representation using `ast.unparse`
	[1]. The outer loop repeats until `ast.unparse(newTree) == ast.unparse(astTree)`, guaranteeing
	convergence but potentially requiring multiple passes for deeply nested or chained substitutions.
	This text-based approach does not rely on node identity or structural equality.

	References
	----------
	[1] ast.unparse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.unparse
	[2] collections.abc.Mapping - Python documentation
		https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping
	[3] astToolkit IfThis.unparseIs - Context7
		https://context7.com/hunterhogan/asttoolkit
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
	"""Decompose a nested `ast.BinOp` (***Bin***ary ***Op***eration) tree into a flat `list` of `ast.expr` (***expr***ession) nodes.

	(AI generated docstring)

	You can use `unjoinBinOP` to flatten a binary operation tree rooted at `astAST` (abstract syntax
	tree) into a `list` of `ast.expr` leaf nodes. `unjoinBinOP` traverses the tree collecting the
	right-hand operands of every matching `ast.BinOp` and accumulating all non-`ast.BinOp` nodes
	into the result.

	Parameters
	----------
	astAST : ast.AST
		(abstract syntax tree) The root `ast.AST` `object` to decompose. `astAST` is typically an
		`ast.BinOp` node, but `unjoinBinOP` accepts any `ast.AST` `object`.
	operator : type[ast.operator] = ast.operator
		(***op***erator) The `ast.operator` subclass to match when deciding whether to descend into
		an `ast.BinOp.op` (***op***erator). Defaults to `ast.operator`, which matches all binary
		operators.

	Returns
	-------
	list_ast_expr : list[ast.expr]
		A flat `list` of `ast.expr` (***expr***ession) nodes that were the operands of the matched
		`ast.BinOp` nodes.

	Algorithm Details
	-----------------
	`unjoinBinOP` uses a `workbench` to hold `ast.BinOp` nodes encountered as left-hand operands
	of outer `ast.BinOp` nodes. The traversal continues until `workbench` is empty, at which point
	all nested `ast.BinOp` nodes have been decomposed and their non-`ast.BinOp` operands have been
	collected into the result `list`.

	References
	----------
	[1] ast.BinOp - Python documentation
		https://docs.python.org/3/library/ast.html#ast.BinOp
	[2] ast.operator - Python documentation
		https://docs.python.org/3/library/ast.html#ast.operator
	[3] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	list_ast_expr: list[ast.expr] = []
	workbench: list[ast.expr] = []

	findThis = Be.BinOp.opIs(lambda this_op: isinstance(this_op, operator))
	doThat = Grab.andDoAllOf([Grab.leftAttribute(Then.appendTo(workbench)), Grab.rightAttribute(Then.appendTo(list_ast_expr))])
	breakingBinOp = NodeTourist(findThis, doThat)

	breakingBinOp.visit(astAST)

	while workbench:
		ast_expr = workbench.pop()
		if isinstance(ast_expr, ast.BinOp):
			breakingBinOp.visit(ast_expr)
		else:
			list_ast_expr.append(ast_expr)

	return list_ast_expr
