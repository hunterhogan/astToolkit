from collections.abc import Iterable
from pathlib import Path
import ast

pythonVersionMinorMinimum: int = 12

class FREAKOUT(Exception):
	pass

listPylanceErrors: list[str] = ['annotation', 'arg', 'args', 'body', 'keys', 'name', 'names', 'op', 'orelse', 'pattern', 'returns', 'target', 'value',]

# filesystem and namespace ===============================================
packageName: str = 'astToolkit'
keywordArgumentsIdentifier: str = 'keywordArguments'

pathRoot = Path('/apps') / packageName
pathPackage = pathRoot / packageName
pathToolFactory = pathRoot / 'toolFactory'

pathFilenameDataframeAST = pathToolFactory / 'dataframeAST.parquet'

fileExtension: str = '.py'

# classmethod .join() =================================================
def joinOperatorExpressions(operatorClass: type[ast.operator], expressions: Iterable[ast.expr]) -> ast.expr:
	"""
	Join AST expressions with a specified operator into a nested BinOp structure.

	This function creates a chain of binary operations by nesting BinOp nodes.
	Each BinOp node uses the specified operator to join two expressions.

	Parameters:
		operatorClass: The ast.operator subclass to use for joining (e.g., ast.Add, ast.BitOr).
		expressions: Iterable of ast.expr objects to join together.

	Returns:
		ast.expr: A single expression representing the joined operations, or the single expression if only one was provided.

	Raises:
		ValueError: If the expressions iterable is empty.
	"""
	expressionsList = list(expressions)

	if not expressionsList:
		raise ValueError("Cannot join an empty iterable of expressions")

	if len(expressionsList) == 1:
		return expressionsList[0]

	result: ast.expr = expressionsList[0]
	for expression in expressionsList[1:]:
		result = ast.BinOp(left=result, op=operatorClass(), right=expression)

	return result

# Add join method to all ast.operator subclasses
def operatorJoinMethod(cls: type[ast.operator], expressions: Iterable[ast.expr]) -> ast.expr:
    """Class method that joins AST expressions using this operator."""
    return joinOperatorExpressions(cls, expressions)

for operatorSubclass in ast.operator.__subclasses__():
    setattr(operatorSubclass, 'join', classmethod(operatorJoinMethod))


# ast.BinOp.join = classmethod(operatorJoinMethod)
# ast.BitOr.join = classmethod(operatorJoinMethod)  # Add join method specifically for ast.BitOr
# class BitOr(ast.BitOr):
# 	"""Custom BitOr class with a join method."""
# 	@classmethod
# 	def join(cls, expressions: Iterable[ast.expr]) -> ast.expr:
# 		return operatorJoinMethod(cls, expressions)

# super(ast.BitOr, ('join', classmethod(operatorJoinMethod)))
# class BitOr():
# 	@classmethod
# 	def join(cls, expressions: Iterable[ast.expr]) -> ast.expr:
# 		return operatorJoinMethod(cls, expressions)

# class ast.Add
# class ast.Sub
# class ast.Mult
# class ast.MatMult
# class ast.Div
# class ast.Mod
# class ast.Pow
# class ast.LShift
# class ast.RShift
# class ast.BitXor
# class ast.BitAnd
# class ast.FloorDiv

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

# ww='''
# ast.arguments()
# ast.Load()
# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=None))
# from ast import *
