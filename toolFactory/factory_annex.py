from typing import cast
import ast
from toolFactory.docstrings import FunctionDefMake_AttributeDocstring

format_asNameAttribute: str = "astDOT{nameAttribute}"
listHandmadeTypeAlias_astTypes: list[ast.AnnAssign | ast.If] = []

listStrRepresentationsOfTypeAlias: list[str] = [
	(astTypes_intORstr := "intORstr: typing_TypeAlias = Any"),
	(astTypes_intORstrORtype_params := "intORstrORtype_params: typing_TypeAlias = Any"),
	(astTypes_intORtype_params := "intORtype_params: typing_TypeAlias = Any"),
	(astTypes_yourPythonIsOld := "yourPythonIsOld: typing_TypeAlias = Any"),
]

for string in listStrRepresentationsOfTypeAlias:
	# The string representation of the type alias is parsed into an AST module.
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.AnnAssign):
			listHandmadeTypeAlias_astTypes.append(node)

# astImportFromClassNewInPythonVersion: ast.ImportFrom = ast.ImportFrom('astToolkit', [], 0)
# listPythonVersionNewClass = [(11, ['TryStar']),
# 	(12, ['ParamSpec', 'type_param', 'TypeAlias', 'TypeVar', 'TypeVarTuple'])
# ]

# for tupleOfClassData in listPythonVersionNewClass:
# 	pythonVersionMinor: int = tupleOfClassData[0]

# 	conditionalTypeAlias = ast.If(
# 		test=ast.Compare(left=ast.Attribute(value=ast.Name('sys'), attr='version_info'),
# 						ops=[ast.GtE()],
# 						comparators=[ast.Tuple([ast.Constant(3), ast.Constant(pythonVersionMinor)])]),
# 		body=[ast.ImportFrom(module='ast', names=[
# 			], level=0)],
# 		orelse=[
# 				])

# 	for nameAttribute in tupleOfClassData[1]:
# 		asNameAttribute = format_asNameAttribute.format(nameAttribute=nameAttribute)
# 		cast(ast.ImportFrom, conditionalTypeAlias.body[0]).names.append(ast.alias(name=nameAttribute, asname=asNameAttribute))
# 		conditionalTypeAlias.orelse.append(ast.AnnAssign(target=ast.Name(asNameAttribute, ast.Store()), annotation=ast.Name('typing_TypeAlias'), value=ast.Name('yourPythonIsOld'), simple=1))
# 		astImportFromClassNewInPythonVersion.names.append(ast.alias(name=asNameAttribute))

# 	listHandmadeTypeAlias_astTypes.append(conditionalTypeAlias)

Grab_andDoAllOf: str = """@staticmethod
def andDoAllOf(listOfActions: list[Callable[[NodeORattribute], NodeORattribute]]) -> Callable[[NodeORattribute], NodeORattribute]:
	def workhorse(node: NodeORattribute) -> NodeORattribute:
		for action in listOfActions:
			node = action(node)
		return node
	return workhorse
"""

listHandmadeMethodsGrab: list[ast.FunctionDef] = []
for string in [Grab_andDoAllOf]:
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.FunctionDef):
			listHandmadeMethodsGrab.append(node)

FunctionDefMake_Attribute: ast.FunctionDef = ast.FunctionDef(
	name='Attribute'
	, args=ast.arguments(args=[ast.arg(arg='value', annotation=ast.Attribute(ast.Name('ast'), 'expr'))]
						, vararg=ast.arg(arg='attribute', annotation=ast.Name('str'))
						, kwonlyargs=[ast.arg(arg='context', annotation=ast.Attribute(ast.Name('ast'), 'expr_context'))]
						, kw_defaults=[ast.Call(ast.Attribute(ast.Name('ast'), 'Load'))]
						, kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int')))
	, body=[FunctionDefMake_AttributeDocstring
		, ast.FunctionDef(
			name='addDOTattribute'
			, args=ast.arguments(args=[ast.arg(arg='chain', annotation=ast.Attribute(ast.Name('ast'), 'expr'))
										, ast.arg(arg='identifier', annotation=ast.Name('str'))
										, ast.arg(arg='context', annotation=ast.Attribute(ast.Name('ast'), 'expr_context'))]
								, kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int')))
			, body=[ast.Return(ast.Call(ast.Attribute(ast.Name('ast'), 'Attribute')
										, keywords=[ast.keyword('value', ast.Name('chain')), ast.keyword('attr', ast.Name('identifier'))
													, ast.keyword('ctx', ast.Name('context')), ast.keyword(value=ast.Name('keywordArguments'))]))]
			, returns=ast.Attribute(ast.Name('ast'), 'Attribute'))
		, ast.Assign([ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute')
																				, args=[ast.Name('value'), ast.Subscript(ast.Name('attribute'), slice=ast.Constant(0)), ast.Name('context')]
																				, keywords=[ast.keyword(value=ast.Name('keywordArguments'))]))
		, ast.For(target=ast.Name('identifier', ast.Store()), iter=ast.Subscript(ast.Name('attribute'), slice=ast.Slice(lower=ast.Constant(1), upper=ast.Constant(None)))
			, body=[ast.Assign([ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute')
																				, args=[ast.Name('buffaloBuffalo'), ast.Name('identifier'), ast.Name('context')]
																				, keywords=[ast.keyword(value=ast.Name('keywordArguments'))]))])
		, ast.Return(ast.Name('buffaloBuffalo'))]
	, decorator_list=[ast.Name('staticmethod')]
	, returns=ast.Attribute(ast.Name('ast'), 'Attribute'))

FunctionDefMake_Import: ast.FunctionDef = ast.FunctionDef(
	name='Import'
	, args=ast.arguments(args=[ast.arg(arg='moduleWithLogicalPath', annotation=ast.Name('str_nameDOTname'))
							, ast.arg(arg='asName', annotation=ast.BinOp(left=ast.Name('str'), op=ast.BitOr(), right=ast.Constant(None)))]
					, kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int'))
					, defaults=[ast.Constant(None)])
	, body=[ast.Return(ast.Call(ast.Attribute(ast.Name('ast'), 'Import')
							, keywords=[ast.keyword('names', ast.List(elts=[ast.Call(ast.Attribute(ast.Name('Make'), 'alias'), args=[ast.Name('moduleWithLogicalPath'), ast.Name('asName')])]))
										, ast.keyword(value=ast.Name('keywordArguments'))]))]
	, decorator_list=[ast.Name('staticmethod')]
	, returns=ast.Attribute(ast.Name('ast'), 'Import'))

listPylanceErrors: list[str] = ['annotation', 'arg', 'args', 'body', 'keys', 'name', 'names', 'op', 'orelse', 'pattern', 'returns', 'target', 'value',]

# ww='''
# if sys.version_info >= (3, 12):
# 	"ImaBody"
# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=4))
# from ast import *
