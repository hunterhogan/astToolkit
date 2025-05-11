from toolFactory.docstrings import FunctionDefMake_AttributeDocstring
import ast

# `Grab` =====================================================================
FunctionDefGrab_andDoAllOf = ast.FunctionDef('andDoAllOf'
	, args=ast.arguments(args=[ast.arg('listOfActions', ast.Subscript(ast.Name('list'), ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Name('NodeORattribute')]), ast.Name('NodeORattribute')]))))])
	, body=[ast.FunctionDef('workhorse'
			, args=ast.arguments(args=[ast.arg('node', ast.Name('NodeORattribute'))])
			, body=[ast.For(ast.Name('action', ctx=ast.Store()), iter=ast.Name('listOfActions')
					, body=[ast.Assign([ast.Name('node', ctx=ast.Store())], value=ast.Call(ast.Name('action'), args=[ast.Name('node')]))]), ast.Return(ast.Name('node'))]
			, returns=ast.Name('NodeORattribute')), ast.Return(ast.Name('workhorse'))]
	, decorator_list=[ast.Name('staticmethod')]
	, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Name('NodeORattribute')]), ast.Name('NodeORattribute')])))

# `Make` =====================================================================
FunctionDefMake_Attribute: ast.FunctionDef = ast.FunctionDef('Attribute'
	, args=ast.arguments(args=[ast.arg(arg='value', annotation=ast.Attribute(ast.Name('ast'), 'expr'))]
						, vararg=ast.arg(arg='attribute', annotation=ast.Name('str'))
						, kwonlyargs=[ast.arg(arg='context', annotation=ast.Attribute(ast.Name('ast'), 'expr_context'))]
						, kw_defaults=[ast.Call(ast.Attribute(ast.Name('ast'), 'Load'))]
						, kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int')))
	, body=[FunctionDefMake_AttributeDocstring
		, ast.FunctionDef('addDOTattribute'
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

FunctionDefMake_Import: ast.FunctionDef = ast.FunctionDef('Import'
	, args=ast.arguments(args=[ast.arg(arg='moduleWithLogicalPath', annotation=ast.Name('str_nameDOTname'))
							, ast.arg(arg='asName', annotation=ast.BinOp(left=ast.Name('str'), op=ast.BitOr(), right=ast.Constant(None)))]
					, kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int'))
					, defaults=[ast.Constant(None)])
	, body=[ast.Return(ast.Call(ast.Attribute(ast.Name('ast'), 'Import')
							, keywords=[ast.keyword('names', ast.List([ast.Call(ast.Attribute(ast.Name('Make'), 'alias'), args=[ast.Name('moduleWithLogicalPath'), ast.Name('asName')])]))
										, ast.keyword(value=ast.Name('keywordArguments'))]))]
	, decorator_list=[ast.Name('staticmethod')]
	, returns=ast.Attribute(ast.Name('ast'), 'Import'))

# `TypeAlias` =====================================================================
listHandmadeTypeAlias_astTypes: list[ast.AnnAssign] = []

listStrRepresentationsOfTypeAlias: list[str] = [
	(astTypes_intORstr := "intORstr: typing_TypeAlias = Any"),
	(astTypes_intORstrORtype_params := "intORstrORtype_params: typing_TypeAlias = Any"),
	(astTypes_intORtype_params := "intORtype_params: typing_TypeAlias = Any"),
]

for string in listStrRepresentationsOfTypeAlias:
	# The string representation of the type alias is parsed into an AST module.
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.AnnAssign):
			listHandmadeTypeAlias_astTypes.append(node)

# ww='''
# if sys.version_info >= (3, 12):
# 	"ImaBody"
# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=4))
# from ast import *
