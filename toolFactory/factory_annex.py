from toolFactory.docstrings import FunctionDefMake_AttributeDocstring
import ast

# `Grab` =====================================================================
FunctionDefGrab_andDoAllOf = ast.FunctionDef('andDoAllOf'
	, args=ast.arguments(args=[ast.arg('listOfActions', ast.Subscript(ast.Name('list'), ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Name('个')]), ast.Name('个')]))))])
	, body=[ast.FunctionDef('workhorse'
			, args=ast.arguments(args=[ast.arg('node', ast.Name('个'))])
			, body=[ast.For(ast.Name('action', ctx=ast.Store()), iter=ast.Name('listOfActions')
					, body=[ast.Assign([ast.Name('node', ctx=ast.Store())], value=ast.Call(ast.Name('action'), args=[ast.Name('node')]))]), ast.Return(ast.Name('node'))]
			, returns=ast.Name('个')), ast.Return(ast.Name('workhorse'))]
	, decorator_list=[ast.Name('staticmethod')]
	, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Name('个')]), ast.Name('个')])))

# `Make` =====================================================================
astAssign_EndPositionT = ast.Assign([ast.Name('_EndPositionT', ast.Store())], value=ast.Call(ast.Name('typing_TypeVar'), args=[ast.Constant('_EndPositionT'), ast.Name('int'), ast.BinOp(ast.Name('int'), ast.BitOr(), ast.Constant(None))], keywords=[ast.keyword('default', value=ast.BinOp(ast.Name('int'), ast.BitOr(), ast.Constant(None)))]))

astClassDef_Attributes = ast.ClassDef('_Attributes', bases=[ast.Name('TypedDict'), ast.Subscript(ast.Name('Generic'), slice=ast.Name('_EndPositionT'))], keywords=[ast.keyword('total', value=ast.Constant(False))], body=[ast.AnnAssign(ast.Name('lineno', ast.Store()), annotation=ast.Name('int'), simple=1), ast.AnnAssign(ast.Name('col_offset', ast.Store()), annotation=ast.Name('int'), simple=1), ast.AnnAssign(ast.Name('end_lineno', ast.Store()), annotation=ast.Name('_EndPositionT'), simple=1), ast.AnnAssign(ast.Name('end_col_offset', ast.Store()), annotation=ast.Name('_EndPositionT'), simple=1)])

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
listHandmade_astTypes: list[ast.stmt] = [
	ast.AnnAssign(ast.Name('intORstr', ast.Store()), annotation=ast.Name('typing_TypeAlias'), value=ast.Name('Any'), simple=1),
	ast.AnnAssign(ast.Name('intORstrORtype_params', ast.Store()), annotation=ast.Name('typing_TypeAlias'), value=ast.Name('Any'), simple=1),
	ast.AnnAssign(ast.Name('intORtype_params', ast.Store()), annotation=ast.Name('typing_TypeAlias'), value=ast.Name('Any'), simple=1),
	ast.Assign([ast.Name('木', ast.Store())], value=ast.Call(ast.Name('typing_TypeVar'), args=[ast.Constant('木')], keywords=[ast.keyword('bound', value=ast.Attribute(ast.Name('ast'), attr='AST')), ast.keyword('covariant', value=ast.Constant(True))])),
	ast.Assign([ast.Name('个', ast.Store())], value=ast.Call(ast.Name('typing_TypeVar'), args=[ast.Constant('个')], keywords=[ast.keyword('covariant', value=ast.Constant(True))])),
	ast.Assign([ast.Name('个return', ast.Store())], value=ast.Call(ast.Name('typing_TypeVar'), args=[ast.Constant('个return')], keywords=[ast.keyword('covariant', value=ast.Constant(True))])),
]
