from collections.abc import Iterable
from pathlib import Path
import ast
from typing import Generic, TypeVar as typing_TypeVar, TypedDict, Unpack
pythonVersionMinorMinimum: int = 12

listPylanceErrors: list[str] = ['annotation', 'arg', 'args', 'body', 'keys', 'name', 'names', 'op', 'orelse', 'pattern', 'returns', 'target', 'value',]
listPylanceErrors.extend(['argtypes', 'bases', 'cases', 'comparators', 'decorator_list', 'defaults', 'elts', 'finalbody', 'generators', 'ifs', 'items',])
listPylanceErrors.extend(['keywords', 'kw_defaults', 'kwd_patterns', 'ops', 'patterns', 'targets', 'type_params', 'values',])

# filesystem and namespace ===============================================
packageName: str = 'astToolkit'
keywordArgumentsIdentifier: str = 'keywordArguments'

pathRoot = Path('/apps') / packageName
pathPackage = pathRoot / packageName
pathToolFactory = pathRoot / 'toolFactory'

pathFilenameDataframeAST = pathToolFactory / 'dataframeAST.parquet'

fileExtension: str = '.py'

# classmethod .join() =================================================
# TODO this is cool, but I need to learn how to properly add it to the classes so the type checker knows what to do with it. Note the use of setattr! grr!

# Used for node end positions in constructor keyword arguments
_EndPositionT = typing_TypeVar("_EndPositionT", int, int | None, default=int | None)

# Corresponds to the names in the `_attributes` class variable which is non-empty in certain AST nodes
class _Attributes(TypedDict, Generic[_EndPositionT], total=False):
	lineno: int
	col_offset: int
	end_lineno: _EndPositionT
	end_col_offset: _EndPositionT

def operatorJoinMethod(ast_operator: type[ast.operator], expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
	listExpressions: list[ast.expr] = list(expressions)

	if not listExpressions:
		listExpressions.append(ast.Constant('', **keywordArguments))

	expressionsJoined: ast.expr = listExpressions[0]
	for expression in listExpressions[1:]:
		expressionsJoined = ast.BinOp(left=expressionsJoined, op=ast_operator(), right=expression, **keywordArguments)

	return expressionsJoined

"""
Usage examples:
ImaIterable: Iterable[ast.expr] = [ast.Name('a'), ast.Name('b'), ast.Name('c')]

# Manual approach
joinedBinOp: ast.expr | ast.BinOp = ImaIterable[0]
for element in ImaIterable[1:]:
	joinedBinOp = ast.BinOp(left=joinedBinOp, op=ast.BitOr(), right=element)
# Result is equivalent to: a | b | c

# Using the new join method
joinedBinOp = ast.BitOr.join(ImaIterable)  # Creates the nested structure for a | b | c
joinedAdd = ast.Add.join(ImaIterable)      # Creates the nested structure for a + b + c
"""

class Add(ast.Add):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class BitAnd(ast.BitAnd):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class BitOr(ast.BitOr):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class BitXor(ast.BitXor):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class Div(ast.Div):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class FloorDiv(ast.FloorDiv):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class LShift(ast.LShift):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class MatMult(ast.MatMult):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class Mod(ast.Mod):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class Mult(ast.Mult):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class Pow(ast.Pow):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class RShift(ast.RShift):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)
class Sub(ast.Sub):
	@classmethod
	def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
		return operatorJoinMethod(cls, expressions, **keywordArguments)

# ww='''
# 木 = typing_TypeVar('木', bound = ast.AST, covariant = True)
# 个 = typing_TypeVar('个', covariant = True)
# 个return = typing_TypeVar('个return', covariant = True)

# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=None))
# from ast import *  # noqa: E402, F403
# ruff: noqa: F405

# rr='''
# Assign(lineno=0,col_offset=0, [ast.Name('key', ast.Store())], value=Lambda(args=arguments(args=[arg('x', annotation=ast.Attribute(ast.Name('pandas'), 'Series'))]), body=Call(ast.Attribute(Attribute(ast.Name('x'), attr='str'), attr='lower'))))
# '''

# print(ast.unparse(ast.Module([eval(rr)])))
