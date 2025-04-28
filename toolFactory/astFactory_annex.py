from typing import Any, cast, TypeAlias as typing_TypeAlias
import ast

astTypes_intORstr: str ="intORstr: typing_TypeAlias = Any"
astTypes_intORstrORtype_params: str ="intORstrORtype_params: typing_TypeAlias = Any"
astTypes_intORtype_params: str ="intORtype_params: typing_TypeAlias = Any"

handmadeTypeAlias_astTypes: list[ast.AnnAssign] = []
for string in [astTypes_intORstr, astTypes_intORstrORtype_params, astTypes_intORtype_params]:
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.AnnAssign):
			handmadeTypeAlias_astTypes.append(node)

Grab_andDoAllOf: str ="""@staticmethod
def andDoAllOf(listOfActions: list[Callable[[NodeORattribute], NodeORattribute]]) -> Callable[[NodeORattribute], NodeORattribute]:
	def workhorse(node: NodeORattribute) -> NodeORattribute:
		for action in listOfActions:
			node = action(node)
		return node
	return workhorse
"""

Grab_funcDOTidAttribute: str ="""@staticmethod
def funcDOTidAttribute(action: Callable[[ast_Identifier], Any]) -> Callable[[ImaCallToName], ImaCallToName]:
	def workhorse(node: ImaCallToName) -> ImaCallToName:
		node.func = Grab.idAttribute(action)(node.func)
		return node
	return workhorse
"""

handmadeMethodsGrab: list[ast.FunctionDef] = []
for string in [Grab_andDoAllOf, Grab_funcDOTidAttribute]:
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.FunctionDef):
			handmadeMethodsGrab.append(node)

MakeAttributeFunctionDef: ast.FunctionDef = ast.FunctionDef(
	name='Attribute',
	args=ast.arguments(args=[ast.arg(arg='value', annotation=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='expr', ctx=ast.Load()))], vararg=ast.arg(arg='attribute', annotation=ast.Name(id='ast_Identifier', ctx=ast.Load())), kwonlyargs=[ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='expr_context', ctx=ast.Load()))], kw_defaults=[ast.Call(func=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Load', ctx=ast.Load()))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name(id='int', ctx=ast.Load()))),
	body=[
		ast.Expr(value=ast.Constant(value=' If two `ast_Identifier` are joined by a dot `.`, they are _usually_ an `ast.Attribute`, but see `ast.ImportFrom`.\n\tParameters:\n\t\tvalue: the part before the dot (e.g., `ast.Name`.)\n\t\tattribute: an `ast_Identifier` after a dot `.`; you can pass multiple `attribute` and they will be chained together.\n\t')),
		ast.FunctionDef(
			name='addDOTattribute',
			args=ast.arguments(args=[ast.arg(arg='chain', annotation=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='expr', ctx=ast.Load())), ast.arg(arg='identifier', annotation=ast.Name(id='ast_Identifier', ctx=ast.Load())), ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='expr_context', ctx=ast.Load()))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name(id='int', ctx=ast.Load()))),
			body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()), keywords=[ast.keyword(arg='value', value=ast.Name(id='chain', ctx=ast.Load())), ast.keyword(arg='attr', value=ast.Name(id='identifier', ctx=ast.Load())), ast.keyword(arg='ctx', value=ast.Name(id='context', ctx=ast.Load())), ast.keyword(value=ast.Name(id='keywordArguments', ctx=ast.Load()))]))],
			returns=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load())),
		ast.Assign(targets=[ast.Name(id='buffaloBuffalo', ctx=ast.Store())], value=ast.Call(func=ast.Name(id='addDOTattribute', ctx=ast.Load()), args=[ast.Name(id='value', ctx=ast.Load()), ast.Subscript(value=ast.Name(id='attribute', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ast.Name(id='context', ctx=ast.Load())], keywords=[ast.keyword(value=ast.Name(id='keywordArguments', ctx=ast.Load()))])),
		ast.For(target=ast.Name(id='identifier', ctx=ast.Store()), iter=ast.Subscript(value=ast.Name(id='attribute', ctx=ast.Load()), slice=ast.Slice(lower=ast.Constant(value=1), upper=ast.Constant(value=None)), ctx=ast.Load()),
			body=[ast.Assign(targets=[ast.Name(id='buffaloBuffalo', ctx=ast.Store())], value=ast.Call(func=ast.Name(id='addDOTattribute', ctx=ast.Load()), args=[ast.Name(id='buffaloBuffalo', ctx=ast.Load()), ast.Name(id='identifier', ctx=ast.Load()), ast.Name(id='context', ctx=ast.Load())], keywords=[ast.keyword(value=ast.Name(id='keywordArguments', ctx=ast.Load()))]))]),
		ast.Return(value=ast.Name(id='buffaloBuffalo', ctx=ast.Load()))],
	decorator_list=[ast.Name(id='staticmethod', ctx=ast.Load())],
	returns=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))

MakeImportFunctionDef: ast.FunctionDef = ast.FunctionDef(name='Import', args=ast.arguments(args=[ast.arg(arg='moduleWithLogicalPath', annotation=ast.Name(id='str_nameDOTname', ctx=ast.Load())), ast.arg(arg='asName', annotation=ast.BinOp(left=ast.Name(id='ast_Identifier', ctx=ast.Load()), op=ast.BitOr(), right=ast.Constant(value=None)))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name(id='int', ctx=ast.Load())), defaults=[ast.Constant(value=None)]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Import', ctx=ast.Load()), keywords=[ast.keyword(arg='names', value=ast.List(elts=[ast.Call(func=ast.Attribute(value=ast.Name(id='Make', ctx=ast.Load()), attr='alias', ctx=ast.Load()), args=[ast.Name(id='moduleWithLogicalPath', ctx=ast.Load()), ast.Name(id='asName', ctx=ast.Load())])], ctx=ast.Load())), ast.keyword(value=ast.Name(id='keywordArguments', ctx=ast.Load()))]))], decorator_list=[ast.Name(id='staticmethod', ctx=ast.Load())], returns=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Import', ctx=ast.Load()))

# ww='''
# list(targets)
# '''

# print(ast.dump(ast.parse(ww), indent=4))
# from ast import *
