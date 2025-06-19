from astToolkit import Make
from typing import Any
import ast

allSubclasses: dict[str, dict[str, dict[str, Any]]] = {
"Add": {
"class Make, maximally empty parameters": {"expression": Make.Add(), "astToolkit.dump": "ast.Add()", "ast.dump": "Add()"},
"ast module, minimal parameters": {"expression": ast.Add(), "astToolkit.dump": "ast.Add()", "ast.dump": "Add()"}
},
"alias": {
"class Make, maximally empty parameters": {"expression": Make.alias(name='Make_alias'), "astToolkit.dump": "ast.alias(name='Make_alias', asname=None)", "ast.dump": "alias(name='Make_alias')"},
"class Make, minimal parameters": {"expression": Make.alias(name='Make_alias', asName=None), "astToolkit.dump": "ast.alias(name='Make_alias', asname=None)", "ast.dump": "alias(name='Make_alias')"},
"ast module, minimal parameters": {"expression": ast.alias(name='ast_alias'), "astToolkit.dump": "ast.alias(name='ast_alias', asname=None)", "ast.dump": "alias(name='ast_alias')"}
},
"And": {
"class Make, maximally empty parameters": {"expression": Make.And(), "astToolkit.dump": "ast.And()", "ast.dump": "And()"},
"ast module, minimal parameters": {"expression": ast.And(), "astToolkit.dump": "ast.And()", "ast.dump": "And()"}
},
"AnnAssign": {
"class Make, maximally empty parameters": {"expression": Make.AnnAssign(target=Make.Name(id='Make_AnnAssign_target', context=Make.Store()), annotation=Make.Name(id='Make_AnnAssign_annotation')), "astToolkit.dump": "ast.AnnAssign(target=ast.Name(id='Make_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='Make_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=1)", "ast.dump": "AnnAssign(target=Name(id='Make_AnnAssign_target', ctx=Store()), annotation=Name(id='Make_AnnAssign_annotation', ctx=Load()), simple=1)"},
"class Make, minimal parameters": {"expression": Make.AnnAssign(target=Make.Name(id='Make_AnnAssign_target', context=Make.Store()), annotation=Make.Name(id='Make_AnnAssign_annotation', context=Make.Load()), value=None), "astToolkit.dump": "ast.AnnAssign(target=ast.Name(id='Make_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='Make_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=1)", "ast.dump": "AnnAssign(target=Name(id='Make_AnnAssign_target', ctx=Store()), annotation=Name(id='Make_AnnAssign_annotation', ctx=Load()), simple=1)"},
"ast module, minimal parameters": {"expression": ast.AnnAssign(target=ast.Name(id='ast_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='ast_AnnAssign_annotation', ctx=ast.Load()), simple=0), "astToolkit.dump": "ast.AnnAssign(target=ast.Name(id='ast_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='ast_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=0)", "ast.dump": "AnnAssign(target=Name(id='ast_AnnAssign_target', ctx=Store()), annotation=Name(id='ast_AnnAssign_annotation', ctx=Load()), simple=0)"}
},
"arg": {
"class Make, maximally empty parameters": {"expression": Make.arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo='Make_arg'), "astToolkit.dump": "ast.arg(arg='Make_arg', annotation=None, type_comment=None)", "ast.dump": "arg(arg='Make_arg')"},
"class Make, minimal parameters": {"expression": Make.arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo='Make_arg', annotation=None), "astToolkit.dump": "ast.arg(arg='Make_arg', annotation=None, type_comment=None)", "ast.dump": "arg(arg='Make_arg')"},
"ast module, minimal parameters": {"expression": ast.arg(arg='ast_arg'), "astToolkit.dump": "ast.arg(arg='ast_arg', annotation=None, type_comment=None)", "ast.dump": "arg(arg='ast_arg')"}
},
"arguments": {
"class Make, maximally empty parameters": {"expression": Make.arguments(), "astToolkit.dump": "ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[])", "ast.dump": "arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[])"},
"class Make, minimal parameters": {"expression": Make.arguments(posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), "astToolkit.dump": "ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])", "ast.dump": "arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[])"},
"ast module, minimal parameters": {"expression": ast.arguments(), "astToolkit.dump": "ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])", "ast.dump": "arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[])"}
},
"Assert": {
"class Make, maximally empty parameters": {"expression": Make.Assert(test=Make.Name(id='Make_Assert_test')), "astToolkit.dump": "ast.Assert(test=ast.Name(id='Make_Assert_test', ctx=ast.Load()), msg=None)", "ast.dump": "Assert(test=Name(id='Make_Assert_test', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Assert(test=Make.Name(id='Make_Assert_test', context=Make.Load()), msg=None), "astToolkit.dump": "ast.Assert(test=ast.Name(id='Make_Assert_test', ctx=ast.Load()), msg=None)", "ast.dump": "Assert(test=Name(id='Make_Assert_test', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Assert(test=ast.Name(id='ast_Assert_test')), "astToolkit.dump": "ast.Assert(test=ast.Name(id='ast_Assert_test', ctx=ast.Load()), msg=None)", "ast.dump": "Assert(test=Name(id='ast_Assert_test', ctx=Load()))"}
},
"Assign": {
"class Make, maximally empty parameters": {"expression": Make.Assign(targets=[Make.Name(id='Make_Assign_targets', context=Make.Store())], value=Make.Name(id='Make_Assign_value')), "astToolkit.dump": "ast.Assign(targets=[ast.Name(id='Make_Assign_targets', ctx=ast.Store())], value=ast.Name(id='Make_Assign_value', ctx=ast.Load()), type_comment=None)", "ast.dump": "Assign(targets=[Name(id='Make_Assign_targets', ctx=Store())], value=Name(id='Make_Assign_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Assign(targets=[Make.Name(id='Make_Assign_targets', context=Make.Store())], value=Make.Name(id='Make_Assign_value', context=Make.Load())), "astToolkit.dump": "ast.Assign(targets=[ast.Name(id='Make_Assign_targets', ctx=ast.Store())], value=ast.Name(id='Make_Assign_value', ctx=ast.Load()), type_comment=None)", "ast.dump": "Assign(targets=[Name(id='Make_Assign_targets', ctx=Store())], value=Name(id='Make_Assign_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Assign(value=ast.Name(id='ast_Assign_value')), "astToolkit.dump": "ast.Assign(targets=[], value=ast.Name(id='ast_Assign_value', ctx=ast.Load()), type_comment=None)", "ast.dump": "Assign(targets=[], value=Name(id='ast_Assign_value', ctx=Load()))"}
},
"AsyncFor": {
"class Make, maximally empty parameters": {"expression": Make.AsyncFor(target=Make.Name(id='Make_AsyncFor_target', context=Make.Store()), iter=Make.Name(id='Make_AsyncFor_iter'), body=[Make.Pass()]), "astToolkit.dump": "ast.AsyncFor(target=ast.Name(id='Make_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='Make_AsyncFor_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)", "ast.dump": "AsyncFor(target=Name(id='Make_AsyncFor_target', ctx=Store()), iter=Name(id='Make_AsyncFor_iter', ctx=Load()), body=[Pass()], orelse=[])"},
"class Make, minimal parameters": {"expression": Make.AsyncFor(target=Make.Name(id='Make_AsyncFor_target', context=Make.Store()), iter=Make.Name(id='Make_AsyncFor_iter', context=Make.Load()), body=[Make.Pass()], orElse=[]), "astToolkit.dump": "ast.AsyncFor(target=ast.Name(id='Make_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='Make_AsyncFor_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)", "ast.dump": "AsyncFor(target=Name(id='Make_AsyncFor_target', ctx=Store()), iter=Name(id='Make_AsyncFor_iter', ctx=Load()), body=[Pass()], orelse=[])"},
"ast module, minimal parameters": {"expression": ast.AsyncFor(target=ast.Name(id='ast_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='ast_AsyncFor_iter', ctx=ast.Load())), "astToolkit.dump": "ast.AsyncFor(target=ast.Name(id='ast_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='ast_AsyncFor_iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)", "ast.dump": "AsyncFor(target=Name(id='ast_AsyncFor_target', ctx=Store()), iter=Name(id='ast_AsyncFor_iter', ctx=Load()), body=[], orelse=[])"}
},
"AsyncFunctionDef": {
"class Make, maximally empty parameters": {"expression": Make.AsyncFunctionDef(name='Make_AsyncFunctionDef'), "astToolkit.dump": "ast.AsyncFunctionDef(name='Make_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "AsyncFunctionDef(name='Make_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"},
"class Make, minimal parameters": {"expression": Make.AsyncFunctionDef(name='Make_AsyncFunctionDef', argumentSpecification=Make.arguments(posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Make.Pass()], decorator_list=[], returns=None, type_params=[]), "astToolkit.dump": "ast.AsyncFunctionDef(name='Make_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Pass()], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "AsyncFunctionDef(name='Make_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Pass()], decorator_list=[], type_params=[])"},
"ast module, minimal parameters": {"expression": ast.AsyncFunctionDef(name='ast_AsyncFunctionDef', args=ast.arguments()), "astToolkit.dump": "ast.AsyncFunctionDef(name='ast_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "AsyncFunctionDef(name='ast_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"}
},
"AsyncWith": {
"class Make, maximally empty parameters": {"expression": Make.AsyncWith(items=[Make.withitem(context_expr=Make.Name(id='Make_AsyncWith_context_expr'))], body=[Make.Pass()]), "astToolkit.dump": "ast.AsyncWith(items=[ast.withitem(context_expr=ast.Name(id='Make_AsyncWith_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)", "ast.dump": "AsyncWith(items=[withitem(context_expr=Name(id='Make_AsyncWith_context_expr', ctx=Load()))], body=[Pass()])"},
"class Make, minimal parameters": {"expression": Make.AsyncWith(items=[Make.withitem(context_expr=Make.Name(id='Make_AsyncWith_context_expr', context=Make.Load()), optional_vars=None)], body=[Make.Pass()]), "astToolkit.dump": "ast.AsyncWith(items=[ast.withitem(context_expr=ast.Name(id='Make_AsyncWith_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)", "ast.dump": "AsyncWith(items=[withitem(context_expr=Name(id='Make_AsyncWith_context_expr', ctx=Load()))], body=[Pass()])"},
"ast module, minimal parameters": {"expression": ast.AsyncWith(), "astToolkit.dump": "ast.AsyncWith(items=[], body=[], type_comment=None)", "ast.dump": "AsyncWith(items=[], body=[])"}
},
"Attribute": {
"class Make, maximally empty parameters": {"expression": Make.Attribute(Make.Name(id='Make_Attribute_value'), 'Make_Attribute_attr'), "astToolkit.dump": "ast.Attribute(value=ast.Name(id='Make_Attribute_value', ctx=ast.Load()), attr='Make_Attribute_attr', ctx=ast.Load())", "ast.dump": "Attribute(value=Name(id='Make_Attribute_value', ctx=Load()), attr='Make_Attribute_attr', ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.Attribute(Make.Name(id='Make_Attribute_value', context=Make.Load()), 'Make_Attribute_attr', context=Make.Load()), "astToolkit.dump": "ast.Attribute(value=ast.Name(id='Make_Attribute_value', ctx=ast.Load()), attr='Make_Attribute_attr', ctx=ast.Load())", "ast.dump": "Attribute(value=Name(id='Make_Attribute_value', ctx=Load()), attr='Make_Attribute_attr', ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.Attribute(value=ast.Name(id='ast_Attribute_value'), attr='ast_Attribute_attr'), "astToolkit.dump": "ast.Attribute(value=ast.Name(id='ast_Attribute_value', ctx=ast.Load()), attr='ast_Attribute_attr', ctx=ast.Load())", "ast.dump": "Attribute(value=Name(id='ast_Attribute_value', ctx=Load()), attr='ast_Attribute_attr', ctx=Load())"}
},
"AugAssign": {
"class Make, maximally empty parameters": {"expression": Make.AugAssign(target=Make.Name(id='Make_AugAssign_target', context=Make.Store()), op=Make.Add(), value=Make.Name(id='Make_AugAssign_value')), "astToolkit.dump": "ast.AugAssign(target=ast.Name(id='Make_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='Make_AugAssign_value', ctx=ast.Load()))", "ast.dump": "AugAssign(target=Name(id='Make_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='Make_AugAssign_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.AugAssign(target=Make.Name(id='Make_AugAssign_target', context=Make.Store()), op=Make.Add(), value=Make.Name(id='Make_AugAssign_value', context=Make.Load())), "astToolkit.dump": "ast.AugAssign(target=ast.Name(id='Make_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='Make_AugAssign_value', ctx=ast.Load()))", "ast.dump": "AugAssign(target=Name(id='Make_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='Make_AugAssign_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.AugAssign(target=ast.Name(id='ast_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='ast_AugAssign_value')), "astToolkit.dump": "ast.AugAssign(target=ast.Name(id='ast_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='ast_AugAssign_value', ctx=ast.Load()))", "ast.dump": "AugAssign(target=Name(id='ast_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='ast_AugAssign_value', ctx=Load()))"}
},
"Await": {
"class Make, maximally empty parameters": {"expression": Make.Await(value=Make.Name(id='Make_Await_value')), "astToolkit.dump": "ast.Await(value=ast.Name(id='Make_Await_value', ctx=ast.Load()))", "ast.dump": "Await(value=Name(id='Make_Await_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Await(value=Make.Name(id='Make_Await_value', context=Make.Load())), "astToolkit.dump": "ast.Await(value=ast.Name(id='Make_Await_value', ctx=ast.Load()))", "ast.dump": "Await(value=Name(id='Make_Await_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Await(value=ast.Name(id='ast_Await_value')), "astToolkit.dump": "ast.Await(value=ast.Name(id='ast_Await_value', ctx=ast.Load()))", "ast.dump": "Await(value=Name(id='ast_Await_value', ctx=Load()))"}
},
"BinOp": {
"class Make, maximally empty parameters": {"expression": Make.BinOp(right=Make.Name(id='Make_BinOp_right'), left=Make.Name(id='Make_BinOp_left'), op=Make.BitAnd()), "astToolkit.dump": "ast.BinOp(left=ast.Name(id='Make_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='Make_BinOp_right', ctx=ast.Load()))", "ast.dump": "BinOp(left=Name(id='Make_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='Make_BinOp_right', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.BinOp(left=Make.Name(id='Make_BinOp_left', context=Make.Load()), op=Make.BitAnd(), right=Make.Name(id='Make_BinOp_right', context=Make.Load())), "astToolkit.dump": "ast.BinOp(left=ast.Name(id='Make_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='Make_BinOp_right', ctx=ast.Load()))", "ast.dump": "BinOp(left=Name(id='Make_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='Make_BinOp_right', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.BinOp(right=ast.Name(id='ast_BinOp_right'), left=ast.Name(id='ast_BinOp_left'), op=ast.BitAnd()), "astToolkit.dump": "ast.BinOp(left=ast.Name(id='ast_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='ast_BinOp_right', ctx=ast.Load()))", "ast.dump": "BinOp(left=Name(id='ast_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='ast_BinOp_right', ctx=Load()))"}
},
"BitAnd": {
"class Make, maximally empty parameters": {"expression": Make.BitAnd(), "astToolkit.dump": "ast.BitAnd()", "ast.dump": "BitAnd()"},
"ast module, minimal parameters": {"expression": ast.BitAnd(), "astToolkit.dump": "ast.BitAnd()", "ast.dump": "BitAnd()"}
},
"BitOr": {
"class Make, maximally empty parameters": {"expression": Make.BitOr(), "astToolkit.dump": "ast.BitOr()", "ast.dump": "BitOr()"},
"ast module, minimal parameters": {"expression": ast.BitOr(), "astToolkit.dump": "ast.BitOr()", "ast.dump": "BitOr()"}
},
"BitXor": {
"class Make, maximally empty parameters": {"expression": Make.BitXor(), "astToolkit.dump": "ast.BitXor()", "ast.dump": "BitXor()"},
"ast module, minimal parameters": {"expression": ast.BitXor(), "astToolkit.dump": "ast.BitXor()", "ast.dump": "BitXor()"}
},
"boolop": {
"class Make, maximally empty parameters": {"expression": Make.boolop(), "astToolkit.dump": "ast.boolop()", "ast.dump": "boolop()"},
"ast module, minimal parameters": {"expression": ast.boolop(), "astToolkit.dump": "ast.boolop()", "ast.dump": "boolop()"}
},
"BoolOp": {
"class Make, maximally empty parameters": {"expression": Make.BoolOp(op=Make.And(), values=[Make.Name(id='Make_BoolOp_values')]), "astToolkit.dump": "ast.BoolOp(op=ast.And(), values=[ast.Name(id='Make_BoolOp_values', ctx=ast.Load())])", "ast.dump": "BoolOp(op=And(), values=[Name(id='Make_BoolOp_values', ctx=Load())])"},
"class Make, minimal parameters": {"expression": Make.BoolOp(op=Make.And(), values=[Make.Name(id='Make_BoolOp_values', context=Make.Load())]), "astToolkit.dump": "ast.BoolOp(op=ast.And(), values=[ast.Name(id='Make_BoolOp_values', ctx=ast.Load())])", "ast.dump": "BoolOp(op=And(), values=[Name(id='Make_BoolOp_values', ctx=Load())])"},
"ast module, minimal parameters": {"expression": ast.BoolOp(op=ast.And()), "astToolkit.dump": "ast.BoolOp(op=ast.And(), values=[])", "ast.dump": "BoolOp(op=And(), values=[])"}
},
"Break": {
"class Make, maximally empty parameters": {"expression": Make.Break(), "astToolkit.dump": "ast.Break()", "ast.dump": "Break()"},
"ast module, minimal parameters": {"expression": ast.Break(), "astToolkit.dump": "ast.Break()", "ast.dump": "Break()"}
},
"Call": {
"class Make, maximally empty parameters": {"expression": Make.Call(callee=Make.Name(id='Make_Call_callee')), "astToolkit.dump": "ast.Call(func=ast.Name(id='Make_Call_callee', ctx=ast.Load()), args=[], keywords=[])", "ast.dump": "Call(func=Name(id='Make_Call_callee', ctx=Load()), args=[], keywords=[])"},
"class Make, minimal parameters": {"expression": Make.Call(callee=Make.Name(id='Make_Call_callee', context=Make.Load()), listParameters=[], list_keyword=[]), "astToolkit.dump": "ast.Call(func=ast.Name(id='Make_Call_callee', ctx=ast.Load()), args=[], keywords=[])", "ast.dump": "Call(func=Name(id='Make_Call_callee', ctx=Load()), args=[], keywords=[])"},
"ast module, minimal parameters": {"expression": ast.Call(func=ast.Name(id='ast_Call_func')), "astToolkit.dump": "ast.Call(func=ast.Name(id='ast_Call_func', ctx=ast.Load()), args=[], keywords=[])", "ast.dump": "Call(func=Name(id='ast_Call_func', ctx=Load()), args=[], keywords=[])"}
},
"ClassDef": {
"class Make, maximally empty parameters": {"expression": Make.ClassDef(name='Make_ClassDef'), "astToolkit.dump": "ast.ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])", "ast.dump": "ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"},
"class Make, minimal parameters": {"expression": Make.ClassDef(name='Make_ClassDef', bases=[], list_keyword=[], body=[], decorator_list=[], type_params=[]), "astToolkit.dump": "ast.ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])", "ast.dump": "ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"},
"ast module, minimal parameters": {"expression": ast.ClassDef(name='ast_ClassDef'), "astToolkit.dump": "ast.ClassDef(name='ast_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])", "ast.dump": "ClassDef(name='ast_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"}
},
"cmpop": {
"class Make, maximally empty parameters": {"expression": Make.cmpop(), "astToolkit.dump": "ast.cmpop()", "ast.dump": "cmpop()"},
"ast module, minimal parameters": {"expression": ast.cmpop(), "astToolkit.dump": "ast.cmpop()", "ast.dump": "cmpop()"}
},
"Compare": {
"class Make, maximally empty parameters": {"expression": Make.Compare(left=Make.Name(id='Make_Compare_left'), ops=[Make.Eq()], comparators=[Make.Name(id='Make_Compare_comparators')]), "astToolkit.dump": "ast.Compare(left=ast.Name(id='Make_Compare_left', ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Name(id='Make_Compare_comparators', ctx=ast.Load())])", "ast.dump": "Compare(left=Name(id='Make_Compare_left', ctx=Load()), ops=[Eq()], comparators=[Name(id='Make_Compare_comparators', ctx=Load())])"},
"class Make, minimal parameters": {"expression": Make.Compare(left=Make.Name(id='Make_Compare_left', context=Make.Load()), ops=[Make.Eq()], comparators=[Make.Name(id='Make_Compare_comparators', context=Make.Load())]), "astToolkit.dump": "ast.Compare(left=ast.Name(id='Make_Compare_left', ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Name(id='Make_Compare_comparators', ctx=ast.Load())])", "ast.dump": "Compare(left=Name(id='Make_Compare_left', ctx=Load()), ops=[Eq()], comparators=[Name(id='Make_Compare_comparators', ctx=Load())])"},
"ast module, minimal parameters": {"expression": ast.Compare(left=ast.Name(id='ast_Compare_left')), "astToolkit.dump": "ast.Compare(left=ast.Name(id='ast_Compare_left', ctx=ast.Load()), ops=[], comparators=[])", "ast.dump": "Compare(left=Name(id='ast_Compare_left', ctx=Load()), ops=[], comparators=[])"}
},
"comprehension": {
"class Make, maximally empty parameters": {"expression": Make.comprehension(target=Make.Name(id='Make_comprehension_target', context=Make.Store()), iter=Make.Name(id='Make_comprehension_iter'), ifs=[Make.Name(id='Make_comprehension_ifs')]), "astToolkit.dump": "ast.comprehension(target=ast.Name(id='Make_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='Make_comprehension_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_comprehension_ifs', ctx=ast.Load())], is_async=0)", "ast.dump": "comprehension(target=Name(id='Make_comprehension_target', ctx=Store()), iter=Name(id='Make_comprehension_iter', ctx=Load()), ifs=[Name(id='Make_comprehension_ifs', ctx=Load())], is_async=0)"},
"class Make, minimal parameters": {"expression": Make.comprehension(target=Make.Name(id='Make_comprehension_target', context=Make.Store()), iter=Make.Name(id='Make_comprehension_iter', context=Make.Load()), ifs=[Make.Name(id='Make_comprehension_ifs', context=Make.Load())], is_async=0), "astToolkit.dump": "ast.comprehension(target=ast.Name(id='Make_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='Make_comprehension_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_comprehension_ifs', ctx=ast.Load())], is_async=0)", "ast.dump": "comprehension(target=Name(id='Make_comprehension_target', ctx=Store()), iter=Name(id='Make_comprehension_iter', ctx=Load()), ifs=[Name(id='Make_comprehension_ifs', ctx=Load())], is_async=0)"},
"ast module, minimal parameters": {"expression": ast.comprehension(target=ast.Name(id='ast_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='ast_comprehension_iter', ctx=ast.Load()), is_async=0), "astToolkit.dump": "ast.comprehension(target=ast.Name(id='ast_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='ast_comprehension_iter', ctx=ast.Load()), ifs=[], is_async=0)", "ast.dump": "comprehension(target=Name(id='ast_comprehension_target', ctx=Store()), iter=Name(id='ast_comprehension_iter', ctx=Load()), ifs=[], is_async=0)"}
},
"Constant": {
"class Make, maximally empty parameters": {"expression": Make.Constant(value='Make_Constant'), "astToolkit.dump": "ast.Constant(value='Make_Constant', kind=None)", "ast.dump": "Constant(value='Make_Constant')"},
"class Make, minimal parameters": {"expression": Make.Constant(value='Make_Constant', kind=None), "astToolkit.dump": "ast.Constant(value='Make_Constant', kind=None)", "ast.dump": "Constant(value='Make_Constant')"},
"ast module, minimal parameters": {"expression": ast.Constant(value='ast_Constant'), "astToolkit.dump": "ast.Constant(value='ast_Constant', kind=None)", "ast.dump": "Constant(value='ast_Constant')"}
},
"Continue": {
"class Make, maximally empty parameters": {"expression": Make.Continue(), "astToolkit.dump": "ast.Continue()", "ast.dump": "Continue()"},
"ast module, minimal parameters": {"expression": ast.Continue(), "astToolkit.dump": "ast.Continue()", "ast.dump": "Continue()"}
},
"Del": {
"class Make, maximally empty parameters": {"expression": Make.Del(), "astToolkit.dump": "ast.Del()", "ast.dump": "Del()"},
"ast module, minimal parameters": {"expression": ast.Del(), "astToolkit.dump": "ast.Del()", "ast.dump": "Del()"}
},
"Delete": {
"class Make, maximally empty parameters": {"expression": Make.Delete(targets=[Make.Name(id='Make_Delete_targets', context=Make.Del())]), "astToolkit.dump": "ast.Delete(targets=[ast.Name(id='Make_Delete_targets', ctx=ast.Del())])", "ast.dump": "Delete(targets=[Name(id='Make_Delete_targets', ctx=Del())])"},
"ast module, minimal parameters": {"expression": ast.Delete(), "astToolkit.dump": "ast.Delete(targets=[])", "ast.dump": "Delete(targets=[])"}
},
"Dict": {
"class Make, maximally empty parameters": {"expression": Make.Dict(), "astToolkit.dump": "ast.Dict(keys=[None], values=[])", "ast.dump": "Dict(keys=[None], values=[])"},
"class Make, minimal parameters": {"expression": Make.Dict(keys=[None], values=[]), "astToolkit.dump": "ast.Dict(keys=[None], values=[])", "ast.dump": "Dict(keys=[None], values=[])"},
"ast module, minimal parameters": {"expression": ast.Dict(), "astToolkit.dump": "ast.Dict(keys=[], values=[])", "ast.dump": "Dict(keys=[], values=[])"}
},
"DictComp": {
"class Make, maximally empty parameters": {"expression": Make.DictComp(key=Make.Name(id='Make_DictComp_key'), value=Make.Name(id='Make_DictComp_value'), generators=[Make.comprehension(target=Make.Name(id='Make_DictComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_DictComp_generators_iter'), ifs=[Make.Name(id='Make_DictComp_generators_ifs')])]), "astToolkit.dump": "ast.DictComp(key=ast.Name(id='Make_DictComp_key', ctx=ast.Load()), value=ast.Name(id='Make_DictComp_value', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_DictComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_DictComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_DictComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "DictComp(key=Name(id='Make_DictComp_key', ctx=Load()), value=Name(id='Make_DictComp_value', ctx=Load()), generators=[comprehension(target=Name(id='Make_DictComp_generators_target', ctx=Store()), iter=Name(id='Make_DictComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_DictComp_generators_ifs', ctx=Load())], is_async=0)])"},
"class Make, minimal parameters": {"expression": Make.DictComp(key=Make.Name(id='Make_DictComp_key', context=Make.Load()), value=Make.Name(id='Make_DictComp_value', context=Make.Load()), generators=[Make.comprehension(target=Make.Name(id='Make_DictComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_DictComp_generators_iter', context=Make.Load()), ifs=[Make.Name(id='Make_DictComp_generators_ifs', context=Make.Load())], is_async=0)]), "astToolkit.dump": "ast.DictComp(key=ast.Name(id='Make_DictComp_key', ctx=ast.Load()), value=ast.Name(id='Make_DictComp_value', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_DictComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_DictComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_DictComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "DictComp(key=Name(id='Make_DictComp_key', ctx=Load()), value=Name(id='Make_DictComp_value', ctx=Load()), generators=[comprehension(target=Name(id='Make_DictComp_generators_target', ctx=Store()), iter=Name(id='Make_DictComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_DictComp_generators_ifs', ctx=Load())], is_async=0)])"},
"ast module, minimal parameters": {"expression": ast.DictComp(key=ast.Name(id='ast_DictComp_key'), value=ast.Name(id='ast_DictComp_value')), "astToolkit.dump": "ast.DictComp(key=ast.Name(id='ast_DictComp_key', ctx=ast.Load()), value=ast.Name(id='ast_DictComp_value', ctx=ast.Load()), generators=[])", "ast.dump": "DictComp(key=Name(id='ast_DictComp_key', ctx=Load()), value=Name(id='ast_DictComp_value', ctx=Load()), generators=[])"}
},
"Div": {
"class Make, maximally empty parameters": {"expression": Make.Div(), "astToolkit.dump": "ast.Div()", "ast.dump": "Div()"},
"ast module, minimal parameters": {"expression": ast.Div(), "astToolkit.dump": "ast.Div()", "ast.dump": "Div()"}
},
"Eq": {
"class Make, maximally empty parameters": {"expression": Make.Eq(), "astToolkit.dump": "ast.Eq()", "ast.dump": "Eq()"},
"ast module, minimal parameters": {"expression": ast.Eq(), "astToolkit.dump": "ast.Eq()", "ast.dump": "Eq()"}
},
"excepthandler": {
"class Make, maximally empty parameters": {"expression": Make.excepthandler(), "astToolkit.dump": "ast.excepthandler()", "ast.dump": "excepthandler()"},
"ast module, minimal parameters": {"expression": ast.excepthandler(), "astToolkit.dump": "ast.excepthandler()", "ast.dump": "excepthandler()"}
},
"ExceptHandler": {
"class Make, maximally empty parameters": {"expression": Make.ExceptHandler(), "astToolkit.dump": "ast.ExceptHandler(type=None, name=None, body=[])", "ast.dump": "ExceptHandler(body=[])"},
"class Make, minimal parameters": {"expression": Make.ExceptHandler(type=None, name=None, body=[]), "astToolkit.dump": "ast.ExceptHandler(type=None, name=None, body=[])", "ast.dump": "ExceptHandler(body=[])"},
"ast module, minimal parameters": {"expression": ast.ExceptHandler(), "astToolkit.dump": "ast.ExceptHandler(type=None, name=None, body=[])", "ast.dump": "ExceptHandler(body=[])"}
},
"expr_context": {
"class Make, maximally empty parameters": {"expression": Make.expr_context(), "astToolkit.dump": "ast.expr_context()", "ast.dump": "expr_context()"},
"ast module, minimal parameters": {"expression": ast.expr_context(), "astToolkit.dump": "ast.expr_context()", "ast.dump": "expr_context()"}
},
"expr": {
"class Make, maximally empty parameters": {"expression": Make.expr(), "astToolkit.dump": "ast.expr()", "ast.dump": "expr()"},
"ast module, minimal parameters": {"expression": ast.expr(), "astToolkit.dump": "ast.expr()", "ast.dump": "expr()"}
},
"Expr": {
"class Make, maximally empty parameters": {"expression": Make.Expr(value=Make.Name(id='Make_Expr_value')), "astToolkit.dump": "ast.Expr(value=ast.Name(id='Make_Expr_value', ctx=ast.Load()))", "ast.dump": "Expr(value=Name(id='Make_Expr_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Expr(value=Make.Name(id='Make_Expr_value', context=Make.Load())), "astToolkit.dump": "ast.Expr(value=ast.Name(id='Make_Expr_value', ctx=ast.Load()))", "ast.dump": "Expr(value=Name(id='Make_Expr_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Expr(value=ast.Name(id='ast_Expr_value')), "astToolkit.dump": "ast.Expr(value=ast.Name(id='ast_Expr_value', ctx=ast.Load()))", "ast.dump": "Expr(value=Name(id='ast_Expr_value', ctx=Load()))"}
},
"Expression": {
"class Make, maximally empty parameters": {"expression": Make.Expression(body=Make.Name(id='Make_Expression_body')), "astToolkit.dump": "ast.Expression(body=ast.Name(id='Make_Expression_body', ctx=ast.Load()))", "ast.dump": "Expression(body=Name(id='Make_Expression_body', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Expression(body=Make.Name(id='Make_Expression_body', context=Make.Load())), "astToolkit.dump": "ast.Expression(body=ast.Name(id='Make_Expression_body', ctx=ast.Load()))", "ast.dump": "Expression(body=Name(id='Make_Expression_body', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Expression(body=ast.Name(id='ast_Expression_body')), "astToolkit.dump": "ast.Expression(body=ast.Name(id='ast_Expression_body', ctx=ast.Load()))", "ast.dump": "Expression(body=Name(id='ast_Expression_body', ctx=Load()))"}
},
"FloorDiv": {
"class Make, maximally empty parameters": {"expression": Make.FloorDiv(), "astToolkit.dump": "ast.FloorDiv()", "ast.dump": "FloorDiv()"},
"ast module, minimal parameters": {"expression": ast.FloorDiv(), "astToolkit.dump": "ast.FloorDiv()", "ast.dump": "FloorDiv()"}
},
"For": {
"class Make, maximally empty parameters": {"expression": Make.For(target=Make.Name(id='Make_For_target', context=Make.Store()), iter=Make.Name(id='Make_For_iter'), body=[Make.Pass()]), "astToolkit.dump": "ast.For(target=ast.Name(id='Make_For_target', ctx=ast.Store()), iter=ast.Name(id='Make_For_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)", "ast.dump": "For(target=Name(id='Make_For_target', ctx=Store()), iter=Name(id='Make_For_iter', ctx=Load()), body=[Pass()], orelse=[])"},
"class Make, minimal parameters": {"expression": Make.For(target=Make.Name(id='Make_For_target', context=Make.Store()), iter=Make.Name(id='Make_For_iter', context=Make.Load()), body=[Make.Pass()], orElse=[]), "astToolkit.dump": "ast.For(target=ast.Name(id='Make_For_target', ctx=ast.Store()), iter=ast.Name(id='Make_For_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)", "ast.dump": "For(target=Name(id='Make_For_target', ctx=Store()), iter=Name(id='Make_For_iter', ctx=Load()), body=[Pass()], orelse=[])"},
"ast module, minimal parameters": {"expression": ast.For(target=ast.Name(id='ast_For_target', ctx=ast.Store()), iter=ast.Name(id='ast_For_iter')), "astToolkit.dump": "ast.For(target=ast.Name(id='ast_For_target', ctx=ast.Store()), iter=ast.Name(id='ast_For_iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)", "ast.dump": "For(target=Name(id='ast_For_target', ctx=Store()), iter=Name(id='ast_For_iter', ctx=Load()), body=[], orelse=[])"}
},
"FormattedValue": {
"class Make, maximally empty parameters": {"expression": Make.FormattedValue(value=Make.Name(id='Make_FormattedValue_value'), conversion=-1), "astToolkit.dump": "ast.FormattedValue(value=ast.Name(id='Make_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)", "ast.dump": "FormattedValue(value=Name(id='Make_FormattedValue_value', ctx=Load()), conversion=-1)"},
"class Make, minimal parameters": {"expression": Make.FormattedValue(value=Make.Name(id='Make_FormattedValue_value', context=Make.Load()), conversion=-1, format_spec=None), "astToolkit.dump": "ast.FormattedValue(value=ast.Name(id='Make_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)", "ast.dump": "FormattedValue(value=Name(id='Make_FormattedValue_value', ctx=Load()), conversion=-1)"},
"ast module, minimal parameters": {"expression": ast.FormattedValue(value=ast.Name(id='ast_FormattedValue_value'), conversion=-1), "astToolkit.dump": "ast.FormattedValue(value=ast.Name(id='ast_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)", "ast.dump": "FormattedValue(value=Name(id='ast_FormattedValue_value', ctx=Load()), conversion=-1)"}
},
"FunctionDef": {
"class Make, maximally empty parameters": {"expression": Make.FunctionDef(name='Make_FunctionDef'), "astToolkit.dump": "ast.FunctionDef(name='Make_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "FunctionDef(name='Make_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"},
"class Make, minimal parameters": {"expression": Make.FunctionDef(name='Make_FunctionDef', argumentSpecification=Make.arguments(posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_params=[]), "astToolkit.dump": "ast.FunctionDef(name='Make_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "FunctionDef(name='Make_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"},
"ast module, minimal parameters": {"expression": ast.FunctionDef(name='ast_FunctionDef', args=ast.arguments()), "astToolkit.dump": "ast.FunctionDef(name='ast_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])", "ast.dump": "FunctionDef(name='ast_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"}
},
"FunctionType": {
"class Make, maximally empty parameters": {"expression": Make.FunctionType(argtypes=[Make.Name(id='Make_FunctionType_argtypes')], returns=Make.Name(id='Make_FunctionType_returns')), "astToolkit.dump": "ast.FunctionType(argtypes=[ast.Name(id='Make_FunctionType_argtypes', ctx=ast.Load())], returns=ast.Name(id='Make_FunctionType_returns', ctx=ast.Load()))", "ast.dump": "FunctionType(argtypes=[Name(id='Make_FunctionType_argtypes', ctx=Load())], returns=Name(id='Make_FunctionType_returns', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.FunctionType(argtypes=[Make.Name(id='Make_FunctionType_argtypes', context=Make.Load())], returns=Make.Name(id='Make_FunctionType_returns', context=Make.Load())), "astToolkit.dump": "ast.FunctionType(argtypes=[ast.Name(id='Make_FunctionType_argtypes', ctx=ast.Load())], returns=ast.Name(id='Make_FunctionType_returns', ctx=ast.Load()))", "ast.dump": "FunctionType(argtypes=[Name(id='Make_FunctionType_argtypes', ctx=Load())], returns=Name(id='Make_FunctionType_returns', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.FunctionType(returns=ast.Name(id='ast_FunctionType_returns')), "astToolkit.dump": "ast.FunctionType(argtypes=[], returns=ast.Name(id='ast_FunctionType_returns', ctx=ast.Load()))", "ast.dump": "FunctionType(argtypes=[], returns=Name(id='ast_FunctionType_returns', ctx=Load()))"}
},
"GeneratorExp": {
"class Make, maximally empty parameters": {"expression": Make.GeneratorExp(element=Make.Name(id='Make_GeneratorExp_element'), generators=[Make.comprehension(target=Make.Name(id='Make_GeneratorExp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_GeneratorExp_generators_iter'), ifs=[Make.Name(id='Make_GeneratorExp_generators_ifs')])]), "astToolkit.dump": "ast.GeneratorExp(elt=ast.Name(id='Make_GeneratorExp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_GeneratorExp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_GeneratorExp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_GeneratorExp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "GeneratorExp(elt=Name(id='Make_GeneratorExp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_GeneratorExp_generators_target', ctx=Store()), iter=Name(id='Make_GeneratorExp_generators_iter', ctx=Load()), ifs=[Name(id='Make_GeneratorExp_generators_ifs', ctx=Load())], is_async=0)])"},
"class Make, minimal parameters": {"expression": Make.GeneratorExp(element=Make.Name(id='Make_GeneratorExp_element', context=Make.Load()), generators=[Make.comprehension(target=Make.Name(id='Make_GeneratorExp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_GeneratorExp_generators_iter', context=Make.Load()), ifs=[Make.Name(id='Make_GeneratorExp_generators_ifs', context=Make.Load())], is_async=0)]), "astToolkit.dump": "ast.GeneratorExp(elt=ast.Name(id='Make_GeneratorExp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_GeneratorExp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_GeneratorExp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_GeneratorExp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "GeneratorExp(elt=Name(id='Make_GeneratorExp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_GeneratorExp_generators_target', ctx=Store()), iter=Name(id='Make_GeneratorExp_generators_iter', ctx=Load()), ifs=[Name(id='Make_GeneratorExp_generators_ifs', ctx=Load())], is_async=0)])"},
"ast module, minimal parameters": {"expression": ast.GeneratorExp(elt=ast.Name(id='ast_GeneratorExp_element')), "astToolkit.dump": "ast.GeneratorExp(elt=ast.Name(id='ast_GeneratorExp_element', ctx=ast.Load()), generators=[])", "ast.dump": "GeneratorExp(elt=Name(id='ast_GeneratorExp_element', ctx=Load()), generators=[])"}
},
"Global": {
"class Make, maximally empty parameters": {"expression": Make.Global(names=['Make_Global']), "astToolkit.dump": "ast.Global(names=['Make_Global'])", "ast.dump": "Global(names=['Make_Global'])"},
"ast module, minimal parameters": {"expression": ast.Global(), "astToolkit.dump": "ast.Global(names=[])", "ast.dump": "Global(names=[])"}
},
"Gt": {
"class Make, maximally empty parameters": {"expression": Make.Gt(), "astToolkit.dump": "ast.Gt()", "ast.dump": "Gt()"},
"ast module, minimal parameters": {"expression": ast.Gt(), "astToolkit.dump": "ast.Gt()", "ast.dump": "Gt()"}
},
"GtE": {
"class Make, maximally empty parameters": {"expression": Make.GtE(), "astToolkit.dump": "ast.GtE()", "ast.dump": "GtE()"},
"ast module, minimal parameters": {"expression": ast.GtE(), "astToolkit.dump": "ast.GtE()", "ast.dump": "GtE()"}
},
"If": {
"class Make, maximally empty parameters": {"expression": Make.If(test=Make.Name(id='Make_If_test'), body=[Make.Pass()]), "astToolkit.dump": "ast.If(test=ast.Name(id='Make_If_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])", "ast.dump": "If(test=Name(id='Make_If_test', ctx=Load()), body=[Pass()], orelse=[])"},
"class Make, minimal parameters": {"expression": Make.If(test=Make.Name(id='Make_If_test', context=Make.Load()), body=[Make.Pass()], orElse=[]), "astToolkit.dump": "ast.If(test=ast.Name(id='Make_If_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])", "ast.dump": "If(test=Name(id='Make_If_test', ctx=Load()), body=[Pass()], orelse=[])"},
"ast module, minimal parameters": {"expression": ast.If(test=ast.Name(id='ast_If_test')), "astToolkit.dump": "ast.If(test=ast.Name(id='ast_If_test', ctx=ast.Load()), body=[], orelse=[])", "ast.dump": "If(test=Name(id='ast_If_test', ctx=Load()), body=[], orelse=[])"}
},
"IfExp": {
"class Make, maximally empty parameters": {"expression": Make.IfExp(test=Make.Name(id='Make_IfExp_test'), body=Make.Name(id='Make_IfExp_body'), orElse=Make.Name(id='Make_IfExp_orelse')), "astToolkit.dump": "ast.IfExp(test=ast.Name(id='Make_IfExp_test', ctx=ast.Load()), body=ast.Name(id='Make_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='Make_IfExp_orelse', ctx=ast.Load()))", "ast.dump": "IfExp(test=Name(id='Make_IfExp_test', ctx=Load()), body=Name(id='Make_IfExp_body', ctx=Load()), orelse=Name(id='Make_IfExp_orelse', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.IfExp(test=Make.Name(id='Make_IfExp_test', context=Make.Load()), body=Make.Name(id='Make_IfExp_body', context=Make.Load()), orElse=Make.Name(id='Make_IfExp_orElse', context=Make.Load())), "astToolkit.dump": "ast.IfExp(test=ast.Name(id='Make_IfExp_test', ctx=ast.Load()), body=ast.Name(id='Make_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='Make_IfExp_orElse', ctx=ast.Load()))", "ast.dump": "IfExp(test=Name(id='Make_IfExp_test', ctx=Load()), body=Name(id='Make_IfExp_body', ctx=Load()), orelse=Name(id='Make_IfExp_orElse', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.IfExp(test=ast.Name(id='ast_IfExp_test'), body=ast.Name(id='ast_IfExp_body'), orelse=ast.Name(id='ast_IfExp_orelse')), "astToolkit.dump": "ast.IfExp(test=ast.Name(id='ast_IfExp_test', ctx=ast.Load()), body=ast.Name(id='ast_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='ast_IfExp_orelse', ctx=ast.Load()))", "ast.dump": "IfExp(test=Name(id='ast_IfExp_test', ctx=Load()), body=Name(id='ast_IfExp_body', ctx=Load()), orelse=Name(id='ast_IfExp_orelse', ctx=Load()))"}
},
"Import": {
"class Make, maximally empty parameters": {"expression": Make.Import(dotModule='Make.Import'), "astToolkit.dump": "ast.Import(names=[ast.alias(name='Make.Import', asname=None)])", "ast.dump": "Import(names=[alias(name='Make.Import')])"},
"ast module, minimal parameters": {"expression": ast.Import(), "astToolkit.dump": "ast.Import(names=[])", "ast.dump": "Import(names=[])"}
},
"ImportFrom": {
"class Make, maximally empty parameters": {"expression": Make.ImportFrom(dotModule='Make.ImportFrom', list_alias=[Make.alias(name='Make_ImportFrom_alias')]), "astToolkit.dump": "ast.ImportFrom(module='Make.ImportFrom', names=[ast.alias(name='Make_ImportFrom_alias', asname=None)], level=0)", "ast.dump": "ImportFrom(module='Make.ImportFrom', names=[alias(name='Make_ImportFrom_alias')], level=0)"},
"class Make, minimal parameters": {"expression": Make.ImportFrom(dotModule='Make.ImportFrom', list_alias=[Make.alias(name='Make_ImportFrom_alias', asName=None)], level=0), "astToolkit.dump": "ast.ImportFrom(module='Make.ImportFrom', names=[ast.alias(name='Make_ImportFrom_alias', asname=None)], level=0)", "ast.dump": "ImportFrom(module='Make.ImportFrom', names=[alias(name='Make_ImportFrom_alias')], level=0)"},
"ast module, minimal parameters": {"expression": ast.ImportFrom(), "astToolkit.dump": "ast.ImportFrom(module=None, names=[], level=None)", "ast.dump": "ImportFrom(names=[])"}
},
"In": {
"class Make, maximally empty parameters": {"expression": Make.In(), "astToolkit.dump": "ast.In()", "ast.dump": "In()"},
"ast module, minimal parameters": {"expression": ast.In(), "astToolkit.dump": "ast.In()", "ast.dump": "In()"}
},
"Interactive": {
"class Make, maximally empty parameters": {"expression": Make.Interactive(body=[Make.Pass()]), "astToolkit.dump": "ast.Interactive(body=[ast.Pass()])", "ast.dump": "Interactive(body=[Pass()])"},
"ast module, minimal parameters": {"expression": ast.Interactive(), "astToolkit.dump": "ast.Interactive(body=[])", "ast.dump": "Interactive(body=[])"}
},
"Invert": {
"class Make, maximally empty parameters": {"expression": Make.Invert(), "astToolkit.dump": "ast.Invert()", "ast.dump": "Invert()"},
"ast module, minimal parameters": {"expression": ast.Invert(), "astToolkit.dump": "ast.Invert()", "ast.dump": "Invert()"}
},
"Is": {
"class Make, maximally empty parameters": {"expression": Make.Is(), "astToolkit.dump": "ast.Is()", "ast.dump": "Is()"},
"ast module, minimal parameters": {"expression": ast.Is(), "astToolkit.dump": "ast.Is()", "ast.dump": "Is()"}
},
"IsNot": {
"class Make, maximally empty parameters": {"expression": Make.IsNot(), "astToolkit.dump": "ast.IsNot()", "ast.dump": "IsNot()"},
"ast module, minimal parameters": {"expression": ast.IsNot(), "astToolkit.dump": "ast.IsNot()", "ast.dump": "IsNot()"}
},
"JoinedStr": {
"class Make, maximally empty parameters": {"expression": Make.JoinedStr(values=[Make.Constant(value='Make_JoinedStr_values')]), "astToolkit.dump": "ast.JoinedStr(values=[ast.Constant(value='Make_JoinedStr_values', kind=None)])", "ast.dump": "JoinedStr(values=[Constant(value='Make_JoinedStr_values')])"},
"class Make, minimal parameters": {"expression": Make.JoinedStr(values=[Make.Constant(value='Make_JoinedStr_values', kind=None)]), "astToolkit.dump": "ast.JoinedStr(values=[ast.Constant(value='Make_JoinedStr_values', kind=None)])", "ast.dump": "JoinedStr(values=[Constant(value='Make_JoinedStr_values')])"},
"ast module, minimal parameters": {"expression": ast.JoinedStr(), "astToolkit.dump": "ast.JoinedStr(values=[])", "ast.dump": "JoinedStr(values=[])"}
},
"keyword": {
"class Make, maximally empty parameters": {"expression": Make.keyword(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo=None, value=Make.Name(id='Make_keyword_value')), "astToolkit.dump": "ast.keyword(arg=None, value=ast.Name(id='Make_keyword_value', ctx=ast.Load()))", "ast.dump": "keyword(value=Name(id='Make_keyword_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.keyword(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo=None, value=Make.Name(id='Make_keyword_value', context=Make.Load())), "astToolkit.dump": "ast.keyword(arg=None, value=ast.Name(id='Make_keyword_value', ctx=ast.Load()))", "ast.dump": "keyword(value=Name(id='Make_keyword_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.keyword(value=ast.Name(id='ast_keyword_value')), "astToolkit.dump": "ast.keyword(arg=None, value=ast.Name(id='ast_keyword_value', ctx=ast.Load()))", "ast.dump": "keyword(value=Name(id='ast_keyword_value', ctx=Load()))"}
},
"Lambda": {
"class Make, maximally empty parameters": {"expression": Make.Lambda(argumentSpecification=Make.arguments(), body=Make.Name(id='Make_Lambda_body')), "astToolkit.dump": "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]), body=ast.Name(id='Make_Lambda_body', ctx=ast.Load()))", "ast.dump": "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[]), body=Name(id='Make_Lambda_body', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.Lambda(argumentSpecification=Make.arguments(posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]), body=Make.Name(id='Make_Lambda_body', context=Make.Load())), "astToolkit.dump": "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]), body=ast.Name(id='Make_Lambda_body', ctx=ast.Load()))", "ast.dump": "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[]), body=Name(id='Make_Lambda_body', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.Lambda(args=ast.arguments(), body=ast.Name(id='ast_Lambda_body')), "astToolkit.dump": "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Name(id='ast_Lambda_body', ctx=ast.Load()))", "ast.dump": "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='ast_Lambda_body', ctx=Load()))"}
},
"List": {
"class Make, maximally empty parameters": {"expression": Make.List(), "astToolkit.dump": "ast.List(elts=[], ctx=ast.Load())", "ast.dump": "List(elts=[], ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.List(listElements=[], context=Make.Load()), "astToolkit.dump": "ast.List(elts=[], ctx=ast.Load())", "ast.dump": "List(elts=[], ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.List(), "astToolkit.dump": "ast.List(elts=[], ctx=ast.Load())", "ast.dump": "List(elts=[], ctx=Load())"}
},
"ListComp": {
"class Make, maximally empty parameters": {"expression": Make.ListComp(element=Make.Name(id='Make_ListComp_element'), generators=[Make.comprehension(target=Make.Name(id='Make_ListComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_ListComp_generators_iter'), ifs=[Make.Name(id='Make_ListComp_generators_ifs')])]), "astToolkit.dump": "ast.ListComp(elt=ast.Name(id='Make_ListComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_ListComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_ListComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_ListComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "ListComp(elt=Name(id='Make_ListComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_ListComp_generators_target', ctx=Store()), iter=Name(id='Make_ListComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_ListComp_generators_ifs', ctx=Load())], is_async=0)])"},
"class Make, minimal parameters": {"expression": Make.ListComp(element=Make.Name(id='Make_ListComp_element', context=Make.Load()), generators=[Make.comprehension(target=Make.Name(id='Make_ListComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_ListComp_generators_iter', context=Make.Load()), ifs=[Make.Name(id='Make_ListComp_generators_ifs', context=Make.Load())], is_async=0)]), "astToolkit.dump": "ast.ListComp(elt=ast.Name(id='Make_ListComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_ListComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_ListComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_ListComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "ListComp(elt=Name(id='Make_ListComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_ListComp_generators_target', ctx=Store()), iter=Name(id='Make_ListComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_ListComp_generators_ifs', ctx=Load())], is_async=0)])"},
"ast module, minimal parameters": {"expression": ast.ListComp(elt=ast.Name(id='ast_ListComp_element')), "astToolkit.dump": "ast.ListComp(elt=ast.Name(id='ast_ListComp_element', ctx=ast.Load()), generators=[])", "ast.dump": "ListComp(elt=Name(id='ast_ListComp_element', ctx=Load()), generators=[])"}
},
"Load": {
"class Make, maximally empty parameters": {"expression": Make.Load(), "astToolkit.dump": "ast.Load()", "ast.dump": "Load()"},
"ast module, minimal parameters": {"expression": ast.Load(), "astToolkit.dump": "ast.Load()", "ast.dump": "Load()"}
},
"LShift": {
"class Make, maximally empty parameters": {"expression": Make.LShift(), "astToolkit.dump": "ast.LShift()", "ast.dump": "LShift()"},
"ast module, minimal parameters": {"expression": ast.LShift(), "astToolkit.dump": "ast.LShift()", "ast.dump": "LShift()"}
},
"Lt": {
"class Make, maximally empty parameters": {"expression": Make.Lt(), "astToolkit.dump": "ast.Lt()", "ast.dump": "Lt()"},
"ast module, minimal parameters": {"expression": ast.Lt(), "astToolkit.dump": "ast.Lt()", "ast.dump": "Lt()"}
},
"LtE": {
"class Make, maximally empty parameters": {"expression": Make.LtE(), "astToolkit.dump": "ast.LtE()", "ast.dump": "LtE()"},
"ast module, minimal parameters": {"expression": ast.LtE(), "astToolkit.dump": "ast.LtE()", "ast.dump": "LtE()"}
},
"match_case": {
"class Make, maximally empty parameters": {"expression": Make.match_case(pattern=Make.MatchAs()), "astToolkit.dump": "ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])", "ast.dump": "match_case(pattern=MatchAs(), body=[])"},
"class Make, minimal parameters": {"expression": Make.match_case(pattern=Make.MatchAs(pattern=None, name=None), guard=None, body=[]), "astToolkit.dump": "ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])", "ast.dump": "match_case(pattern=MatchAs(), body=[])"},
"ast module, minimal parameters": {"expression": ast.match_case(pattern=ast.MatchAs()), "astToolkit.dump": "ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])", "ast.dump": "match_case(pattern=MatchAs(), body=[])"}
},
"Match": {
"class Make, maximally empty parameters": {"expression": Make.Match(subject=Make.Name(id='Make_Match_subject')), "astToolkit.dump": "ast.Match(subject=ast.Name(id='Make_Match_subject', ctx=ast.Load()), cases=[])", "ast.dump": "Match(subject=Name(id='Make_Match_subject', ctx=Load()), cases=[])"},
"class Make, minimal parameters": {"expression": Make.Match(subject=Make.Name(id='Make_Match_subject', context=Make.Load()), cases=[]), "astToolkit.dump": "ast.Match(subject=ast.Name(id='Make_Match_subject', ctx=ast.Load()), cases=[])", "ast.dump": "Match(subject=Name(id='Make_Match_subject', ctx=Load()), cases=[])"},
"ast module, minimal parameters": {"expression": ast.Match(subject=ast.Name(id='ast_Match_subject')), "astToolkit.dump": "ast.Match(subject=ast.Name(id='ast_Match_subject', ctx=ast.Load()), cases=[])", "ast.dump": "Match(subject=Name(id='ast_Match_subject', ctx=Load()), cases=[])"}
},
"MatchAs": {
"class Make, maximally empty parameters": {"expression": Make.MatchAs(), "astToolkit.dump": "ast.MatchAs(pattern=None, name=None)", "ast.dump": "MatchAs()"},
"class Make, minimal parameters": {"expression": Make.MatchAs(pattern=None, name=None), "astToolkit.dump": "ast.MatchAs(pattern=None, name=None)", "ast.dump": "MatchAs()"},
"ast module, minimal parameters": {"expression": ast.MatchAs(), "astToolkit.dump": "ast.MatchAs(pattern=None, name=None)", "ast.dump": "MatchAs()"}
},
"MatchClass": {
"class Make, maximally empty parameters": {"expression": Make.MatchClass(cls=Make.Name(id='Make_MatchClass_cls')), "astToolkit.dump": "ast.MatchClass(cls=ast.Name(id='Make_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])", "ast.dump": "MatchClass(cls=Name(id='Make_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"},
"class Make, minimal parameters": {"expression": Make.MatchClass(cls=Make.Name(id='Make_MatchClass_cls', context=Make.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[]), "astToolkit.dump": "ast.MatchClass(cls=ast.Name(id='Make_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])", "ast.dump": "MatchClass(cls=Name(id='Make_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"},
"ast module, minimal parameters": {"expression": ast.MatchClass(cls=ast.Name(id='ast_MatchClass_cls')), "astToolkit.dump": "ast.MatchClass(cls=ast.Name(id='ast_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])", "ast.dump": "MatchClass(cls=Name(id='ast_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"}
},
"MatchMapping": {
"class Make, maximally empty parameters": {"expression": Make.MatchMapping(), "astToolkit.dump": "ast.MatchMapping(keys=[], patterns=[], rest=None)", "ast.dump": "MatchMapping(keys=[], patterns=[])"},
"class Make, minimal parameters": {"expression": Make.MatchMapping(keys=[], patterns=[], rest=None), "astToolkit.dump": "ast.MatchMapping(keys=[], patterns=[], rest=None)", "ast.dump": "MatchMapping(keys=[], patterns=[])"},
"ast module, minimal parameters": {"expression": ast.MatchMapping(), "astToolkit.dump": "ast.MatchMapping(keys=[], patterns=[], rest=None)", "ast.dump": "MatchMapping(keys=[], patterns=[])"}
},
"MatchOr": {
"class Make, maximally empty parameters": {"expression": Make.MatchOr(), "astToolkit.dump": "ast.MatchOr(patterns=[])", "ast.dump": "MatchOr(patterns=[])"},
"class Make, minimal parameters": {"expression": Make.MatchOr(patterns=[]), "astToolkit.dump": "ast.MatchOr(patterns=[])", "ast.dump": "MatchOr(patterns=[])"},
"ast module, minimal parameters": {"expression": ast.MatchOr(), "astToolkit.dump": "ast.MatchOr(patterns=[])", "ast.dump": "MatchOr(patterns=[])"}
},
"MatchSequence": {
"class Make, maximally empty parameters": {"expression": Make.MatchSequence(), "astToolkit.dump": "ast.MatchSequence(patterns=[])", "ast.dump": "MatchSequence(patterns=[])"},
"class Make, minimal parameters": {"expression": Make.MatchSequence(patterns=[]), "astToolkit.dump": "ast.MatchSequence(patterns=[])", "ast.dump": "MatchSequence(patterns=[])"},
"ast module, minimal parameters": {"expression": ast.MatchSequence(), "astToolkit.dump": "ast.MatchSequence(patterns=[])", "ast.dump": "MatchSequence(patterns=[])"}
},
"MatchSingleton": {
"class Make, maximally empty parameters": {"expression": Make.MatchSingleton(value=True), "astToolkit.dump": "ast.MatchSingleton(value=True)", "ast.dump": "MatchSingleton(value=True)"},
"ast module, minimal parameters": {"expression": ast.MatchSingleton(value=True), "astToolkit.dump": "ast.MatchSingleton(value=True)", "ast.dump": "MatchSingleton(value=True)"}
},
"MatchStar": {
"class Make, maximally empty parameters": {"expression": Make.MatchStar(), "astToolkit.dump": "ast.MatchStar(name=None)", "ast.dump": "MatchStar()"},
"class Make, minimal parameters": {"expression": Make.MatchStar(name=None), "astToolkit.dump": "ast.MatchStar(name=None)", "ast.dump": "MatchStar()"},
"ast module, minimal parameters": {"expression": ast.MatchStar(), "astToolkit.dump": "ast.MatchStar(name=None)", "ast.dump": "MatchStar()"}
},
"MatchValue": {
"class Make, maximally empty parameters": {"expression": Make.MatchValue(value=Make.Name(id='Make_MatchValue_value')), "astToolkit.dump": "ast.MatchValue(value=ast.Name(id='Make_MatchValue_value', ctx=ast.Load()))", "ast.dump": "MatchValue(value=Name(id='Make_MatchValue_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.MatchValue(value=Make.Name(id='Make_MatchValue_value', context=Make.Load())), "astToolkit.dump": "ast.MatchValue(value=ast.Name(id='Make_MatchValue_value', ctx=ast.Load()))", "ast.dump": "MatchValue(value=Name(id='Make_MatchValue_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.MatchValue(value=ast.Name(id='ast_MatchValue_value')), "astToolkit.dump": "ast.MatchValue(value=ast.Name(id='ast_MatchValue_value', ctx=ast.Load()))", "ast.dump": "MatchValue(value=Name(id='ast_MatchValue_value', ctx=Load()))"}
},
"MatMult": {
"class Make, maximally empty parameters": {"expression": Make.MatMult(), "astToolkit.dump": "ast.MatMult()", "ast.dump": "MatMult()"},
"ast module, minimal parameters": {"expression": ast.MatMult(), "astToolkit.dump": "ast.MatMult()", "ast.dump": "MatMult()"}
},
"Mod": {
"class Make, maximally empty parameters": {"expression": Make.Mod(), "astToolkit.dump": "ast.Mod()", "ast.dump": "Mod()"},
"ast module, minimal parameters": {"expression": ast.Mod(), "astToolkit.dump": "ast.Mod()", "ast.dump": "Mod()"}
},
"mod": {
"class Make, maximally empty parameters": {"expression": Make.mod(), "astToolkit.dump": "ast.mod()", "ast.dump": "mod()"},
"ast module, minimal parameters": {"expression": ast.mod(), "astToolkit.dump": "ast.mod()", "ast.dump": "mod()"}
},
"Module": {
"class Make, maximally empty parameters": {"expression": Make.Module(body=[Make.Pass()]), "astToolkit.dump": "ast.Module(body=[ast.Pass()], type_ignores=[])", "ast.dump": "Module(body=[Pass()], type_ignores=[])"},
"class Make, minimal parameters": {"expression": Make.Module(body=[Make.Pass()], type_ignores=[]), "astToolkit.dump": "ast.Module(body=[ast.Pass()], type_ignores=[])", "ast.dump": "Module(body=[Pass()], type_ignores=[])"},
"ast module, minimal parameters": {"expression": ast.Module(), "astToolkit.dump": "ast.Module(body=[], type_ignores=[])", "ast.dump": "Module(body=[], type_ignores=[])"}
},
"Mult": {
"class Make, maximally empty parameters": {"expression": Make.Mult(), "astToolkit.dump": "ast.Mult()", "ast.dump": "Mult()"},
"ast module, minimal parameters": {"expression": ast.Mult(), "astToolkit.dump": "ast.Mult()", "ast.dump": "Mult()"}
},
"Name": {
"class Make, maximally empty parameters": {"expression": Make.Name(id='Make_Name'), "astToolkit.dump": "ast.Name(id='Make_Name', ctx=ast.Load())", "ast.dump": "Name(id='Make_Name', ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.Name(id='Make_Name', context=Make.Load()), "astToolkit.dump": "ast.Name(id='Make_Name', ctx=ast.Load())", "ast.dump": "Name(id='Make_Name', ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.Name(id='ast_Name'), "astToolkit.dump": "ast.Name(id='ast_Name', ctx=ast.Load())", "ast.dump": "Name(id='ast_Name', ctx=Load())"}
},
"NamedExpr": {
"class Make, maximally empty parameters": {"expression": Make.NamedExpr(target=Make.Name(id='Make_NamedExpr_target', context=Make.Store()), value=Make.Name(id='Make_NamedExpr_value')), "astToolkit.dump": "ast.NamedExpr(target=ast.Name(id='Make_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='Make_NamedExpr_value', ctx=ast.Load()))", "ast.dump": "NamedExpr(target=Name(id='Make_NamedExpr_target', ctx=Store()), value=Name(id='Make_NamedExpr_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.NamedExpr(target=Make.Name(id='Make_NamedExpr_target', context=Make.Store()), value=Make.Name(id='Make_NamedExpr_value', context=Make.Load())), "astToolkit.dump": "ast.NamedExpr(target=ast.Name(id='Make_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='Make_NamedExpr_value', ctx=ast.Load()))", "ast.dump": "NamedExpr(target=Name(id='Make_NamedExpr_target', ctx=Store()), value=Name(id='Make_NamedExpr_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.NamedExpr(target=ast.Name(id='ast_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='ast_NamedExpr_value')), "astToolkit.dump": "ast.NamedExpr(target=ast.Name(id='ast_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='ast_NamedExpr_value', ctx=ast.Load()))", "ast.dump": "NamedExpr(target=Name(id='ast_NamedExpr_target', ctx=Store()), value=Name(id='ast_NamedExpr_value', ctx=Load()))"}
},
"Nonlocal": {
"class Make, maximally empty parameters": {"expression": Make.Nonlocal(names=['Make_Nonlocal']), "astToolkit.dump": "ast.Nonlocal(names=['Make_Nonlocal'])", "ast.dump": "Nonlocal(names=['Make_Nonlocal'])"},
"ast module, minimal parameters": {"expression": ast.Nonlocal(), "astToolkit.dump": "ast.Nonlocal(names=[])", "ast.dump": "Nonlocal(names=[])"}
},
"Not": {
"class Make, maximally empty parameters": {"expression": Make.Not(), "astToolkit.dump": "ast.Not()", "ast.dump": "Not()"},
"ast module, minimal parameters": {"expression": ast.Not(), "astToolkit.dump": "ast.Not()", "ast.dump": "Not()"}
},
"NotEq": {
"class Make, maximally empty parameters": {"expression": Make.NotEq(), "astToolkit.dump": "ast.NotEq()", "ast.dump": "NotEq()"},
"ast module, minimal parameters": {"expression": ast.NotEq(), "astToolkit.dump": "ast.NotEq()", "ast.dump": "NotEq()"}
},
"NotIn": {
"class Make, maximally empty parameters": {"expression": Make.NotIn(), "astToolkit.dump": "ast.NotIn()", "ast.dump": "NotIn()"},
"ast module, minimal parameters": {"expression": ast.NotIn(), "astToolkit.dump": "ast.NotIn()", "ast.dump": "NotIn()"}
},
"operator": {
"class Make, maximally empty parameters": {"expression": Make.operator(), "astToolkit.dump": "ast.operator()", "ast.dump": "operator()"},
"ast module, minimal parameters": {"expression": ast.operator(), "astToolkit.dump": "ast.operator()", "ast.dump": "operator()"}
},
"Or": {
"class Make, maximally empty parameters": {"expression": Make.Or(), "astToolkit.dump": "ast.Or()", "ast.dump": "Or()"},
"ast module, minimal parameters": {"expression": ast.Or(), "astToolkit.dump": "ast.Or()", "ast.dump": "Or()"}
},
# "ParamSpec": {
# "class Make, maximally empty parameters": {"expression": Make.ParamSpec(name='Make_ParamSpec'), "astToolkit.dump": "ast.ParamSpec(name='Make_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='Make_ParamSpec')"},
# "class Make, minimal parameters": {"expression": Make.ParamSpec(name='Make_ParamSpec', default_value=None), "astToolkit.dump": "ast.ParamSpec(name='Make_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='Make_ParamSpec')"},
# "ast module, minimal parameters": {"expression": ast.ParamSpec(name='ast_ParamSpec'), "astToolkit.dump": "ast.ParamSpec(name='ast_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='ast_ParamSpec')"}
# },
"Pass": {
"class Make, maximally empty parameters": {"expression": Make.Pass(), "astToolkit.dump": "ast.Pass()", "ast.dump": "Pass()"},
"ast module, minimal parameters": {"expression": ast.Pass(), "astToolkit.dump": "ast.Pass()", "ast.dump": "Pass()"}
},
"pattern": {
"class Make, maximally empty parameters": {"expression": Make.pattern(), "astToolkit.dump": "ast.pattern()", "ast.dump": "pattern()"},
"ast module, minimal parameters": {"expression": ast.pattern(), "astToolkit.dump": "ast.pattern()", "ast.dump": "pattern()"}
},
"Pow": {
"class Make, maximally empty parameters": {"expression": Make.Pow(), "astToolkit.dump": "ast.Pow()", "ast.dump": "Pow()"},
"ast module, minimal parameters": {"expression": ast.Pow(), "astToolkit.dump": "ast.Pow()", "ast.dump": "Pow()"}
},
"Raise": {
"class Make, maximally empty parameters": {"expression": Make.Raise(), "astToolkit.dump": "ast.Raise(exc=None, cause=None)", "ast.dump": "Raise()"},
"class Make, minimal parameters": {"expression": Make.Raise(exc=None, cause=None), "astToolkit.dump": "ast.Raise(exc=None, cause=None)", "ast.dump": "Raise()"},
"ast module, minimal parameters": {"expression": ast.Raise(), "astToolkit.dump": "ast.Raise(exc=None, cause=None)", "ast.dump": "Raise()"}
},
"Return": {
"class Make, maximally empty parameters": {"expression": Make.Return(), "astToolkit.dump": "ast.Return(value=None)", "ast.dump": "Return()"},
"class Make, minimal parameters": {"expression": Make.Return(value=None), "astToolkit.dump": "ast.Return(value=None)", "ast.dump": "Return()"},
"ast module, minimal parameters": {"expression": ast.Return(), "astToolkit.dump": "ast.Return(value=None)", "ast.dump": "Return()"}
},
"RShift": {
"class Make, maximally empty parameters": {"expression": Make.RShift(), "astToolkit.dump": "ast.RShift()", "ast.dump": "RShift()"},
"ast module, minimal parameters": {"expression": ast.RShift(), "astToolkit.dump": "ast.RShift()", "ast.dump": "RShift()"}
},
"Set": {
"class Make, maximally empty parameters": {"expression": Make.Set(), "astToolkit.dump": "ast.Set(elts=[])", "ast.dump": "Set(elts=[])"},
"class Make, minimal parameters": {"expression": Make.Set(listElements=[]), "astToolkit.dump": "ast.Set(elts=[])", "ast.dump": "Set(elts=[])"},
"ast module, minimal parameters": {"expression": ast.Set(), "astToolkit.dump": "ast.Set(elts=[])", "ast.dump": "Set(elts=[])"}
},
"SetComp": {
"class Make, maximally empty parameters": {"expression": Make.SetComp(element=Make.Name(id='Make_SetComp_element'), generators=[Make.comprehension(target=Make.Name(id='Make_SetComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_SetComp_generators_iter'), ifs=[Make.Name(id='Make_SetComp_generators_ifs')])]), "astToolkit.dump": "ast.SetComp(elt=ast.Name(id='Make_SetComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_SetComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_SetComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_SetComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "SetComp(elt=Name(id='Make_SetComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_SetComp_generators_target', ctx=Store()), iter=Name(id='Make_SetComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_SetComp_generators_ifs', ctx=Load())], is_async=0)])"},
"class Make, minimal parameters": {"expression": Make.SetComp(element=Make.Name(id='Make_SetComp_element', context=Make.Load()), generators=[Make.comprehension(target=Make.Name(id='Make_SetComp_generators_target', context=Make.Store()), iter=Make.Name(id='Make_SetComp_generators_iter', context=Make.Load()), ifs=[Make.Name(id='Make_SetComp_generators_ifs', context=Make.Load())], is_async=0)]), "astToolkit.dump": "ast.SetComp(elt=ast.Name(id='Make_SetComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_SetComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_SetComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_SetComp_generators_ifs', ctx=ast.Load())], is_async=0)])", "ast.dump": "SetComp(elt=Name(id='Make_SetComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_SetComp_generators_target', ctx=Store()), iter=Name(id='Make_SetComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_SetComp_generators_ifs', ctx=Load())], is_async=0)])"},
"ast module, minimal parameters": {"expression": ast.SetComp(elt=ast.Name(id='ast_SetComp_element')), "astToolkit.dump": "ast.SetComp(elt=ast.Name(id='ast_SetComp_element', ctx=ast.Load()), generators=[])", "ast.dump": "SetComp(elt=Name(id='ast_SetComp_element', ctx=Load()), generators=[])"}
},
"Slice": {
"class Make, maximally empty parameters": {"expression": Make.Slice(), "astToolkit.dump": "ast.Slice(lower=None, upper=None, step=None)", "ast.dump": "Slice()"},
"class Make, minimal parameters": {"expression": Make.Slice(lower=None, upper=None, step=None), "astToolkit.dump": "ast.Slice(lower=None, upper=None, step=None)", "ast.dump": "Slice()"},
"ast module, minimal parameters": {"expression": ast.Slice(), "astToolkit.dump": "ast.Slice(lower=None, upper=None, step=None)", "ast.dump": "Slice()"}
},
"Starred": {
"class Make, maximally empty parameters": {"expression": Make.Starred(value=Make.Name(id='Make_Starred_value')), "astToolkit.dump": "ast.Starred(value=ast.Name(id='Make_Starred_value', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Starred(value=Name(id='Make_Starred_value', ctx=Load()), ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.Starred(value=Make.Name(id='Make_Starred_value', context=Make.Load()), context=Make.Load()), "astToolkit.dump": "ast.Starred(value=ast.Name(id='Make_Starred_value', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Starred(value=Name(id='Make_Starred_value', ctx=Load()), ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.Starred(value=ast.Name(id='ast_Starred_value')), "astToolkit.dump": "ast.Starred(value=ast.Name(id='ast_Starred_value', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Starred(value=Name(id='ast_Starred_value', ctx=Load()), ctx=Load())"}
},
"stmt": {
"class Make, maximally empty parameters": {"expression": Make.stmt(), "astToolkit.dump": "ast.stmt()", "ast.dump": "stmt()"},
"ast module, minimal parameters": {"expression": ast.stmt(), "astToolkit.dump": "ast.stmt()", "ast.dump": "stmt()"}
},
"Store": {
"class Make, maximally empty parameters": {"expression": Make.Store(), "astToolkit.dump": "ast.Store()", "ast.dump": "Store()"},
"ast module, minimal parameters": {"expression": ast.Store(), "astToolkit.dump": "ast.Store()", "ast.dump": "Store()"}
},
"Sub": {
"class Make, maximally empty parameters": {"expression": Make.Sub(), "astToolkit.dump": "ast.Sub()", "ast.dump": "Sub()"},
"ast module, minimal parameters": {"expression": ast.Sub(), "astToolkit.dump": "ast.Sub()", "ast.dump": "Sub()"}
},
"Subscript": {
"class Make, maximally empty parameters": {"expression": Make.Subscript(value=Make.Name(id='Make_Subscript_value'), slice=Make.Name(id='Make_Subscript_slice')), "astToolkit.dump": "ast.Subscript(value=ast.Name(id='Make_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='Make_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Subscript(value=Name(id='Make_Subscript_value', ctx=Load()), slice=Name(id='Make_Subscript_slice', ctx=Load()), ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.Subscript(value=Make.Name(id='Make_Subscript_value', context=Make.Load()), slice=Make.Name(id='Make_Subscript_slice', context=Make.Load()), context=Make.Load()), "astToolkit.dump": "ast.Subscript(value=ast.Name(id='Make_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='Make_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Subscript(value=Name(id='Make_Subscript_value', ctx=Load()), slice=Name(id='Make_Subscript_slice', ctx=Load()), ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.Subscript(value=ast.Name(id='ast_Subscript_value'), slice=ast.Name(id='ast_Subscript_slice')), "astToolkit.dump": "ast.Subscript(value=ast.Name(id='ast_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='ast_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())", "ast.dump": "Subscript(value=Name(id='ast_Subscript_value', ctx=Load()), slice=Name(id='ast_Subscript_slice', ctx=Load()), ctx=Load())"}
},
"Try": {
"class Make, maximally empty parameters": {"expression": Make.Try(body=[Make.Pass()], handlers=[Make.ExceptHandler()]), "astToolkit.dump": "ast.Try(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])", "ast.dump": "Try(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])"},
"class Make, minimal parameters": {"expression": Make.Try(body=[Make.Pass()], handlers=[Make.ExceptHandler(type=None, name=None, body=[])], orElse=[], finalbody=[]), "astToolkit.dump": "ast.Try(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])", "ast.dump": "Try(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])"},
"ast module, minimal parameters": {"expression": ast.Try(), "astToolkit.dump": "ast.Try(body=[], handlers=[], orelse=[], finalbody=[])", "ast.dump": "Try(body=[], handlers=[], orelse=[], finalbody=[])"}
},
"TryStar": {
"class Make, maximally empty parameters": {"expression": Make.TryStar(body=[Make.Pass()], handlers=[Make.ExceptHandler()]), "astToolkit.dump": "ast.TryStar(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])", "ast.dump": "TryStar(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])"},
"class Make, minimal parameters": {"expression": Make.TryStar(body=[Make.Pass()], handlers=[Make.ExceptHandler(type=None, name=None, body=[])], orElse=[], finalbody=[]), "astToolkit.dump": "ast.TryStar(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])", "ast.dump": "TryStar(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])"},
"ast module, minimal parameters": {"expression": ast.TryStar(), "astToolkit.dump": "ast.TryStar(body=[], handlers=[], orelse=[], finalbody=[])", "ast.dump": "TryStar(body=[], handlers=[], orelse=[], finalbody=[])"}
},
"Tuple": {
"class Make, maximally empty parameters": {"expression": Make.Tuple(), "astToolkit.dump": "ast.Tuple(elts=[], ctx=ast.Load())", "ast.dump": "Tuple(elts=[], ctx=Load())"},
"class Make, minimal parameters": {"expression": Make.Tuple(listElements=[], context=Make.Load()), "astToolkit.dump": "ast.Tuple(elts=[], ctx=ast.Load())", "ast.dump": "Tuple(elts=[], ctx=Load())"},
"ast module, minimal parameters": {"expression": ast.Tuple(), "astToolkit.dump": "ast.Tuple(elts=[], ctx=ast.Load())", "ast.dump": "Tuple(elts=[], ctx=Load())"}
},
"type_ignore": {
"class Make, maximally empty parameters": {"expression": Make.type_ignore(), "astToolkit.dump": "ast.type_ignore()", "ast.dump": "type_ignore()"},
"ast module, minimal parameters": {"expression": ast.type_ignore(), "astToolkit.dump": "ast.type_ignore()", "ast.dump": "type_ignore()"}
},
"type_param": {
"class Make, maximally empty parameters": {"expression": Make.type_param(), "astToolkit.dump": "ast.type_param()", "ast.dump": "type_param()"},
"ast module, minimal parameters": {"expression": ast.type_param(), "astToolkit.dump": "ast.type_param()", "ast.dump": "type_param()"}
},
# "TypeAlias": {
# "class Make, maximally empty parameters": {"expression": Make.TypeAlias(name=Make.Name(id='Make_TypeAlias'), type_params=[], value=Make.Name(id='Make_TypeAlias_value')), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='Make_TypeAlias', ctx=ast.Load()), type_params=[], value=ast.Name(id='Make_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='Make_TypeAlias', ctx=Load()), type_params=[], value=Name(id='Make_TypeAlias_value', ctx=Load()))"},
# "class Make, minimal parameters": {"expression": Make.TypeAlias(name=Make.Name(id='Make_TypeAlias', context=Make.Store()), type_params=[Make.TypeVar(name='Make_TypeAlias_type_params', bound=None, default_value=None)], value=Make.Name(id='Make_TypeAlias_value', context=Make.Load())), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='Make_TypeAlias', ctx=ast.Store()), type_params=[ast.TypeVar(name='Make_TypeAlias_type_params', bound=None, default_value=None)], value=ast.Name(id='Make_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='Make_TypeAlias', ctx=Store()), type_params=[TypeVar(name='Make_TypeAlias_type_params')], value=Name(id='Make_TypeAlias_value', ctx=Load()))"},
# "ast module, minimal parameters": {"expression": ast.TypeAlias(name=ast.Name(id='ast_TypeAlias'), value=ast.Name(id='ast_TypeAlias_value')), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='ast_TypeAlias', ctx=ast.Load()), type_params=[], value=ast.Name(id='ast_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='ast_TypeAlias', ctx=Load()), type_params=[], value=Name(id='ast_TypeAlias_value', ctx=Load()))"}
# },
"TypeIgnore": {
"class Make, maximally empty parameters": {"expression": Make.TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag'), "astToolkit.dump": "ast.TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag')", "ast.dump": "TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag')"},
"ast module, minimal parameters": {"expression": ast.TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag'), "astToolkit.dump": "ast.TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag')", "ast.dump": "TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag')"}
},
# "TypeVar": {
# "class Make, maximally empty parameters": {"expression": Make.TypeVar(name='Make_TypeVar'), "astToolkit.dump": "ast.TypeVar(name='Make_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='Make_TypeVar')"},
# "class Make, minimal parameters": {"expression": Make.TypeVar(name='Make_TypeVar', bound=None, default_value=None), "astToolkit.dump": "ast.TypeVar(name='Make_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='Make_TypeVar')"},
# "ast module, minimal parameters": {"expression": ast.TypeVar(name='ast_TypeVar'), "astToolkit.dump": "ast.TypeVar(name='ast_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='ast_TypeVar')"}
# },
# "TypeVarTuple": {
# "class Make, maximally empty parameters": {"expression": Make.TypeVarTuple(name='Make_TypeVarTuple'), "astToolkit.dump": "ast.TypeVarTuple(name='Make_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='Make_TypeVarTuple')"},
# "class Make, minimal parameters": {"expression": Make.TypeVarTuple(name='Make_TypeVarTuple', default_value=None), "astToolkit.dump": "ast.TypeVarTuple(name='Make_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='Make_TypeVarTuple')"},
# "ast module, minimal parameters": {"expression": ast.TypeVarTuple(name='ast_TypeVarTuple'), "astToolkit.dump": "ast.TypeVarTuple(name='ast_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='ast_TypeVarTuple')"}
# },
"UAdd": {
"class Make, maximally empty parameters": {"expression": Make.UAdd(), "astToolkit.dump": "ast.UAdd()", "ast.dump": "UAdd()"},
"ast module, minimal parameters": {"expression": ast.UAdd(), "astToolkit.dump": "ast.UAdd()", "ast.dump": "UAdd()"}
},
"unaryop": {
"class Make, maximally empty parameters": {"expression": Make.unaryop(), "astToolkit.dump": "ast.unaryop()", "ast.dump": "unaryop()"},
"ast module, minimal parameters": {"expression": ast.unaryop(), "astToolkit.dump": "ast.unaryop()", "ast.dump": "unaryop()"}
},
"UnaryOp": {
"class Make, maximally empty parameters": {"expression": Make.UnaryOp(op=Make.UAdd(), operand=Make.Name(id='Make_UnaryOp_operand')), "astToolkit.dump": "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='Make_UnaryOp_operand', ctx=ast.Load()))", "ast.dump": "UnaryOp(op=UAdd(), operand=Name(id='Make_UnaryOp_operand', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.UnaryOp(op=Make.UAdd(), operand=Make.Name(id='Make_UnaryOp_operand', context=Make.Load())), "astToolkit.dump": "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='Make_UnaryOp_operand', ctx=ast.Load()))", "ast.dump": "UnaryOp(op=UAdd(), operand=Name(id='Make_UnaryOp_operand', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='ast_UnaryOp_operand')), "astToolkit.dump": "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='ast_UnaryOp_operand', ctx=ast.Load()))", "ast.dump": "UnaryOp(op=UAdd(), operand=Name(id='ast_UnaryOp_operand', ctx=Load()))"}
},
"USub": {
"class Make, maximally empty parameters": {"expression": Make.USub(), "astToolkit.dump": "ast.USub()", "ast.dump": "USub()"},
"ast module, minimal parameters": {"expression": ast.USub(), "astToolkit.dump": "ast.USub()", "ast.dump": "USub()"}
},
"While": {
"class Make, maximally empty parameters": {"expression": Make.While(test=Make.Name(id='Make_While_test'), body=[Make.Pass()]), "astToolkit.dump": "ast.While(test=ast.Name(id='Make_While_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])", "ast.dump": "While(test=Name(id='Make_While_test', ctx=Load()), body=[Pass()], orelse=[])"},
"class Make, minimal parameters": {"expression": Make.While(test=Make.Name(id='Make_While_test', context=Make.Load()), body=[Make.Pass()], orElse=[]), "astToolkit.dump": "ast.While(test=ast.Name(id='Make_While_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])", "ast.dump": "While(test=Name(id='Make_While_test', ctx=Load()), body=[Pass()], orelse=[])"},
"ast module, minimal parameters": {"expression": ast.While(test=ast.Name(id='ast_While_test')), "astToolkit.dump": "ast.While(test=ast.Name(id='ast_While_test', ctx=ast.Load()), body=[], orelse=[])", "ast.dump": "While(test=Name(id='ast_While_test', ctx=Load()), body=[], orelse=[])"}
},
"With": {
"class Make, maximally empty parameters": {"expression": Make.With(items=[Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr'))], body=[Make.Pass()]), "astToolkit.dump": "ast.With(items=[ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)", "ast.dump": "With(items=[withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))], body=[Pass()])"},
"class Make, minimal parameters": {"expression": Make.With(items=[Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr', context=Make.Load()), optional_vars=None)], body=[Make.Pass()]), "astToolkit.dump": "ast.With(items=[ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)", "ast.dump": "With(items=[withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))], body=[Pass()])"},
"ast module, minimal parameters": {"expression": ast.With(), "astToolkit.dump": "ast.With(items=[], body=[], type_comment=None)", "ast.dump": "With(items=[], body=[])"}
},
"withitem": {
"class Make, maximally empty parameters": {"expression": Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr')), "astToolkit.dump": "ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)", "ast.dump": "withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr', context=Make.Load()), optional_vars=None), "astToolkit.dump": "ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)", "ast.dump": "withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.withitem(context_expr=ast.Name(id='ast_withitem_context_expr')), "astToolkit.dump": "ast.withitem(context_expr=ast.Name(id='ast_withitem_context_expr', ctx=ast.Load()), optional_vars=None)", "ast.dump": "withitem(context_expr=Name(id='ast_withitem_context_expr', ctx=Load()))"}
},
"Yield": {
"class Make, maximally empty parameters": {"expression": Make.Yield(), "astToolkit.dump": "ast.Yield(value=None)", "ast.dump": "Yield()"},
"class Make, minimal parameters": {"expression": Make.Yield(value=None), "astToolkit.dump": "ast.Yield(value=None)", "ast.dump": "Yield()"},
"ast module, minimal parameters": {"expression": ast.Yield(), "astToolkit.dump": "ast.Yield(value=None)", "ast.dump": "Yield()"}
},
"YieldFrom": {
"class Make, maximally empty parameters": {"expression": Make.YieldFrom(value=Make.Name(id='Make_YieldFrom_value')), "astToolkit.dump": "ast.YieldFrom(value=ast.Name(id='Make_YieldFrom_value', ctx=ast.Load()))", "ast.dump": "YieldFrom(value=Name(id='Make_YieldFrom_value', ctx=Load()))"},
"class Make, minimal parameters": {"expression": Make.YieldFrom(value=Make.Name(id='Make_YieldFrom_value', context=Make.Load())), "astToolkit.dump": "ast.YieldFrom(value=ast.Name(id='Make_YieldFrom_value', ctx=ast.Load()))", "ast.dump": "YieldFrom(value=Name(id='Make_YieldFrom_value', ctx=Load()))"},
"ast module, minimal parameters": {"expression": ast.YieldFrom(value=ast.Name(id='ast_YieldFrom_value')), "astToolkit.dump": "ast.YieldFrom(value=ast.Name(id='ast_YieldFrom_value', ctx=ast.Load()))", "ast.dump": "YieldFrom(value=Name(id='ast_YieldFrom_value', ctx=Load()))"}
},
}
