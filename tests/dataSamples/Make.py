"""Samples of each `ast` class, built with `Make` and with the `ast` constructors, and their recorded dumps.

`allSubclasses` maps each class identifier to its samples, keyed by how each sample was constructed. Consumers do not mutate
the samples; a target that mutates a node receives a copy from the `node` fixture.
"""
from __future__ import annotations

from astToolkit import Make
from functools import partial
from itertools import chain, repeat
from operator import attrgetter, itemgetter
from typing import Any
import ast

allSubclasses: dict[str, dict[str, dict[str, Any]]] = {
	'Add': {
		'MakeMaximallyEmpty': {'expression': Make.Add(), 'astToolkit.dump': 'ast.Add()', 'ast.dump': 'Add()'}
		, 'astMinimal': {'expression': ast.Add(), 'astToolkit.dump': 'ast.Add()', 'ast.dump': 'Add()'}
	}
	, 'alias': {
		'MakeMaximallyEmpty': {
			'expression': Make.alias(dotModule='Make_alias')
			, 'astToolkit.dump': "ast.alias(name='Make_alias', asname=None)"
			, 'ast.dump': "alias(name='Make_alias')"
		}
		, 'MakeMinimal': {
			'expression': Make.alias(dotModule='Make_alias', asName=None)
			, 'astToolkit.dump': "ast.alias(name='Make_alias', asname=None)"
			, 'ast.dump': "alias(name='Make_alias')"
		}
		, 'astMinimal': {
			'expression': ast.alias(name='ast_alias')
			, 'astToolkit.dump': "ast.alias(name='ast_alias', asname=None)"
			, 'ast.dump': "alias(name='ast_alias')"
		}
	}
	, 'And': {
		'MakeMaximallyEmpty': {'expression': Make.And(), 'astToolkit.dump': 'ast.And()', 'ast.dump': 'And()'}
		, 'astMinimal': {'expression': ast.And(), 'astToolkit.dump': 'ast.And()', 'ast.dump': 'And()'}
	}
	, 'AnnAssign': {
		'MakeMaximallyEmpty': {
			'expression': Make.AnnAssign(
				target=Make.Name(id='Make_AnnAssign_target', context=Make.Store()), annotation=Make.Name(id='Make_AnnAssign_annotation')
			)
			, 'astToolkit.dump': "ast.AnnAssign(target=ast.Name(id='Make_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='Make_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=1)"
			, 'ast.dump': "AnnAssign(target=Name(id='Make_AnnAssign_target', ctx=Store()), annotation=Name(id='Make_AnnAssign_annotation', ctx=Load()), simple=1)"
		}
		, 'MakeMinimal': {
			'expression': Make.AnnAssign(
				target=Make.Name(id='Make_AnnAssign_target', context=Make.Store())
				, annotation=Make.Name(id='Make_AnnAssign_annotation', context=Make.Load())
				, value=None
			)
			, 'astToolkit.dump': "ast.AnnAssign(target=ast.Name(id='Make_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='Make_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=1)"
			, 'ast.dump': "AnnAssign(target=Name(id='Make_AnnAssign_target', ctx=Store()), annotation=Name(id='Make_AnnAssign_annotation', ctx=Load()), simple=1)"
		}
		, 'astMinimal': {
			'expression': ast.AnnAssign(
				target=ast.Name(id='ast_AnnAssign_target', ctx=ast.Store())
				, annotation=ast.Name(id='ast_AnnAssign_annotation', ctx=ast.Load())
				, simple=0
			)
			, 'astToolkit.dump': "ast.AnnAssign(target=ast.Name(id='ast_AnnAssign_target', ctx=ast.Store()), annotation=ast.Name(id='ast_AnnAssign_annotation', ctx=ast.Load()), value=None, simple=0)"
			, 'ast.dump': "AnnAssign(target=Name(id='ast_AnnAssign_target', ctx=Store()), annotation=Name(id='ast_AnnAssign_annotation', ctx=Load()), simple=0)"
		}
	}
	, 'arg': {
		'MakeMaximallyEmpty': {
			'expression': Make.arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo='Make_arg')
			, 'astToolkit.dump': "ast.arg(arg='Make_arg', annotation=None, type_comment=None)"
			, 'ast.dump': "arg(arg='Make_arg')"
		}
		, 'MakeMinimal': {
			'expression': Make.arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo='Make_arg', annotation=None)
			, 'astToolkit.dump': "ast.arg(arg='Make_arg', annotation=None, type_comment=None)"
			, 'ast.dump': "arg(arg='Make_arg')"
		}
		, 'astMinimal': {
			'expression': ast.arg(arg='ast_arg')
			, 'astToolkit.dump': "ast.arg(arg='ast_arg', annotation=None, type_comment=None)"
			, 'ast.dump': "arg(arg='ast_arg')"
		}
	}
	, 'arguments': {
		'MakeMaximallyEmpty': {
			'expression': Make.arguments()
			, 'astToolkit.dump': 'ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[])'
			, 'ast.dump': 'arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.arguments(posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, 'astToolkit.dump': 'ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])'
			, 'ast.dump': 'arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[])'
		}
		, 'astMinimal': {
			'expression': ast.arguments()
			, 'astToolkit.dump': 'ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])'
			, 'ast.dump': 'arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[])'
		}
	}
	, 'Assert': {
		'MakeMaximallyEmpty': {
			'expression': Make.Assert(test=Make.Name(id='Make_Assert_test'))
			, 'astToolkit.dump': "ast.Assert(test=ast.Name(id='Make_Assert_test', ctx=ast.Load()), msg=None)"
			, 'ast.dump': "Assert(test=Name(id='Make_Assert_test', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Assert(test=Make.Name(id='Make_Assert_test', context=Make.Load()), msg=None)
			, 'astToolkit.dump': "ast.Assert(test=ast.Name(id='Make_Assert_test', ctx=ast.Load()), msg=None)"
			, 'ast.dump': "Assert(test=Name(id='Make_Assert_test', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Assert(test=ast.Name(id='ast_Assert_test'))
			, 'astToolkit.dump': "ast.Assert(test=ast.Name(id='ast_Assert_test', ctx=ast.Load()), msg=None)"
			, 'ast.dump': "Assert(test=Name(id='ast_Assert_test', ctx=Load()))"
		}
	}
	, 'Assign': {
		'MakeMaximallyEmpty': {
			'expression': Make.Assign(
				targets=[Make.Name(id='Make_Assign_targets', context=Make.Store())], value=Make.Name(id='Make_Assign_value')
			)
			, 'astToolkit.dump': "ast.Assign(targets=[ast.Name(id='Make_Assign_targets', ctx=ast.Store())], value=ast.Name(id='Make_Assign_value', ctx=ast.Load()), type_comment=None)"
			, 'ast.dump': "Assign(targets=[Name(id='Make_Assign_targets', ctx=Store())], value=Name(id='Make_Assign_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Assign(
				targets=[Make.Name(id='Make_Assign_targets', context=Make.Store())]
				, value=Make.Name(id='Make_Assign_value', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.Assign(targets=[ast.Name(id='Make_Assign_targets', ctx=ast.Store())], value=ast.Name(id='Make_Assign_value', ctx=ast.Load()), type_comment=None)"
			, 'ast.dump': "Assign(targets=[Name(id='Make_Assign_targets', ctx=Store())], value=Name(id='Make_Assign_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Assign(value=ast.Name(id='ast_Assign_value'))
			, 'astToolkit.dump': "ast.Assign(targets=[], value=ast.Name(id='ast_Assign_value', ctx=ast.Load()), type_comment=None)"
			, 'ast.dump': "Assign(targets=[], value=Name(id='ast_Assign_value', ctx=Load()))"
		}
	}
	, 'AsyncFor': {
		'MakeMaximallyEmpty': {
			'expression': Make.AsyncFor(
				target=Make.Name(id='Make_AsyncFor_target', context=Make.Store())
				, iter=Make.Name(id='Make_AsyncFor_iter')
				, body=[Make.Pass()]
			)
			, 'astToolkit.dump': "ast.AsyncFor(target=ast.Name(id='Make_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='Make_AsyncFor_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)"
			, 'ast.dump': "AsyncFor(target=Name(id='Make_AsyncFor_target', ctx=Store()), iter=Name(id='Make_AsyncFor_iter', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.AsyncFor(
				target=Make.Name(id='Make_AsyncFor_target', context=Make.Store())
				, iter=Make.Name(id='Make_AsyncFor_iter', context=Make.Load())
				, body=[Make.Pass()]
				, orElse=[]
			)
			, 'astToolkit.dump': "ast.AsyncFor(target=ast.Name(id='Make_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='Make_AsyncFor_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)"
			, 'ast.dump': "AsyncFor(target=Name(id='Make_AsyncFor_target', ctx=Store()), iter=Name(id='Make_AsyncFor_iter', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'astMinimal': {
			'expression': ast.AsyncFor(
				target=ast.Name(id='ast_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='ast_AsyncFor_iter', ctx=ast.Load())
			)
			, 'astToolkit.dump': "ast.AsyncFor(target=ast.Name(id='ast_AsyncFor_target', ctx=ast.Store()), iter=ast.Name(id='ast_AsyncFor_iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)"
			, 'ast.dump': "AsyncFor(target=Name(id='ast_AsyncFor_target', ctx=Store()), iter=Name(id='ast_AsyncFor_iter', ctx=Load()), body=[], orelse=[])"
		}
	}
	, 'AsyncFunctionDef': {
		'MakeMaximallyEmpty': {
			'expression': Make.AsyncFunctionDef(name='Make_AsyncFunctionDef')
			, 'astToolkit.dump': "ast.AsyncFunctionDef(name='Make_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "AsyncFunctionDef(name='Make_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.AsyncFunctionDef(
				name='Make_AsyncFunctionDef'
				, argumentSpecification=Make.arguments(
					posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]
				)
				, body=[Make.Pass()]
				, decorator_list=[]
				, returns=None
				, type_params=[]
			)
			, 'astToolkit.dump': "ast.AsyncFunctionDef(name='Make_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Pass()], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "AsyncFunctionDef(name='Make_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Pass()], decorator_list=[], type_params=[])"
		}
		, 'astMinimal': {
			'expression': ast.AsyncFunctionDef(name='ast_AsyncFunctionDef', args=ast.arguments())
			, 'astToolkit.dump': "ast.AsyncFunctionDef(name='ast_AsyncFunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "AsyncFunctionDef(name='ast_AsyncFunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"
		}
	}
	, 'AsyncWith': {
		'MakeMaximallyEmpty': {
			'expression': Make.AsyncWith(
				items=[Make.withitem(context_expr=Make.Name(id='Make_AsyncWith_context_expr'))], body=[Make.Pass()]
			)
			, 'astToolkit.dump': "ast.AsyncWith(items=[ast.withitem(context_expr=ast.Name(id='Make_AsyncWith_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)"
			, 'ast.dump': "AsyncWith(items=[withitem(context_expr=Name(id='Make_AsyncWith_context_expr', ctx=Load()))], body=[Pass()])"
		}
		, 'MakeMinimal': {
			'expression': Make.AsyncWith(
				items=[Make.withitem(context_expr=Make.Name(id='Make_AsyncWith_context_expr', context=Make.Load()), optional_vars=None)]
				, body=[Make.Pass()]
			)
			, 'astToolkit.dump': "ast.AsyncWith(items=[ast.withitem(context_expr=ast.Name(id='Make_AsyncWith_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)"
			, 'ast.dump': "AsyncWith(items=[withitem(context_expr=Name(id='Make_AsyncWith_context_expr', ctx=Load()))], body=[Pass()])"
		}
		, 'astMinimal': {
			'expression': ast.AsyncWith()
			, 'astToolkit.dump': 'ast.AsyncWith(items=[], body=[], type_comment=None)'
			, 'ast.dump': 'AsyncWith(items=[], body=[])'
		}
	}
	, 'Attribute': {
		'MakeMaximallyEmpty': {
			'expression': Make.Attribute(Make.Name(id='Make_Attribute_value'), 'Make_Attribute_attr')
			, 'astToolkit.dump': "ast.Attribute(value=ast.Name(id='Make_Attribute_value', ctx=ast.Load()), attr='Make_Attribute_attr', ctx=ast.Load())"
			, 'ast.dump': "Attribute(value=Name(id='Make_Attribute_value', ctx=Load()), attr='Make_Attribute_attr', ctx=Load())"
		}
		, 'MakeMinimal': {
			'expression': Make.Attribute(
				Make.Name(id='Make_Attribute_value', context=Make.Load()), 'Make_Attribute_attr', context=Make.Load()
			)
			, 'astToolkit.dump': "ast.Attribute(value=ast.Name(id='Make_Attribute_value', ctx=ast.Load()), attr='Make_Attribute_attr', ctx=ast.Load())"
			, 'ast.dump': "Attribute(value=Name(id='Make_Attribute_value', ctx=Load()), attr='Make_Attribute_attr', ctx=Load())"
		}
		, 'astMinimal': {
			'expression': ast.Attribute(value=ast.Name(id='ast_Attribute_value'), attr='ast_Attribute_attr')
			, 'astToolkit.dump': "ast.Attribute(value=ast.Name(id='ast_Attribute_value', ctx=ast.Load()), attr='ast_Attribute_attr', ctx=ast.Load())"
			, 'ast.dump': "Attribute(value=Name(id='ast_Attribute_value', ctx=Load()), attr='ast_Attribute_attr', ctx=Load())"
		}
	}
	, 'AugAssign': {
		'MakeMaximallyEmpty': {
			'expression': Make.AugAssign(
				target=Make.Name(id='Make_AugAssign_target', context=Make.Store())
				, op=Make.Add()
				, value=Make.Name(id='Make_AugAssign_value')
			)
			, 'astToolkit.dump': "ast.AugAssign(target=ast.Name(id='Make_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='Make_AugAssign_value', ctx=ast.Load()))"
			, 'ast.dump': "AugAssign(target=Name(id='Make_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='Make_AugAssign_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.AugAssign(
				target=Make.Name(id='Make_AugAssign_target', context=Make.Store())
				, op=Make.Add()
				, value=Make.Name(id='Make_AugAssign_value', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.AugAssign(target=ast.Name(id='Make_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='Make_AugAssign_value', ctx=ast.Load()))"
			, 'ast.dump': "AugAssign(target=Name(id='Make_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='Make_AugAssign_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.AugAssign(
				target=ast.Name(id='ast_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='ast_AugAssign_value')
			)
			, 'astToolkit.dump': "ast.AugAssign(target=ast.Name(id='ast_AugAssign_target', ctx=ast.Store()), op=ast.Add(), value=ast.Name(id='ast_AugAssign_value', ctx=ast.Load()))"
			, 'ast.dump': "AugAssign(target=Name(id='ast_AugAssign_target', ctx=Store()), op=Add(), value=Name(id='ast_AugAssign_value', ctx=Load()))"
		}
	}
	, 'Await': {
		'MakeMaximallyEmpty': {
			'expression': Make.Await(value=Make.Name(id='Make_Await_value'))
			, 'astToolkit.dump': "ast.Await(value=ast.Name(id='Make_Await_value', ctx=ast.Load()))"
			, 'ast.dump': "Await(value=Name(id='Make_Await_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Await(value=Make.Name(id='Make_Await_value', context=Make.Load()))
			, 'astToolkit.dump': "ast.Await(value=ast.Name(id='Make_Await_value', ctx=ast.Load()))"
			, 'ast.dump': "Await(value=Name(id='Make_Await_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Await(value=ast.Name(id='ast_Await_value'))
			, 'astToolkit.dump': "ast.Await(value=ast.Name(id='ast_Await_value', ctx=ast.Load()))"
			, 'ast.dump': "Await(value=Name(id='ast_Await_value', ctx=Load()))"
		}
	}
	, 'BinOp': {
		'MakeMaximallyEmpty': {
			'expression': Make.BinOp(right=Make.Name(id='Make_BinOp_right'), left=Make.Name(id='Make_BinOp_left'), op=Make.BitAnd())
			, 'astToolkit.dump': "ast.BinOp(left=ast.Name(id='Make_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='Make_BinOp_right', ctx=ast.Load()))"
			, 'ast.dump': "BinOp(left=Name(id='Make_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='Make_BinOp_right', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.BinOp(
				left=Make.Name(id='Make_BinOp_left', context=Make.Load())
				, op=Make.BitAnd()
				, right=Make.Name(id='Make_BinOp_right', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.BinOp(left=ast.Name(id='Make_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='Make_BinOp_right', ctx=ast.Load()))"
			, 'ast.dump': "BinOp(left=Name(id='Make_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='Make_BinOp_right', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.BinOp(right=ast.Name(id='ast_BinOp_right'), left=ast.Name(id='ast_BinOp_left'), op=ast.BitAnd())
			, 'astToolkit.dump': "ast.BinOp(left=ast.Name(id='ast_BinOp_left', ctx=ast.Load()), op=ast.BitAnd(), right=ast.Name(id='ast_BinOp_right', ctx=ast.Load()))"
			, 'ast.dump': "BinOp(left=Name(id='ast_BinOp_left', ctx=Load()), op=BitAnd(), right=Name(id='ast_BinOp_right', ctx=Load()))"
		}
	}
	, 'BitAnd': {
		'MakeMaximallyEmpty': {'expression': Make.BitAnd(), 'astToolkit.dump': 'ast.BitAnd()', 'ast.dump': 'BitAnd()'}
		, 'astMinimal': {'expression': ast.BitAnd(), 'astToolkit.dump': 'ast.BitAnd()', 'ast.dump': 'BitAnd()'}
	}
	, 'BitOr': {
		'MakeMaximallyEmpty': {'expression': Make.BitOr(), 'astToolkit.dump': 'ast.BitOr()', 'ast.dump': 'BitOr()'}
		, 'astMinimal': {'expression': ast.BitOr(), 'astToolkit.dump': 'ast.BitOr()', 'ast.dump': 'BitOr()'}
	}
	, 'BitXor': {
		'MakeMaximallyEmpty': {'expression': Make.BitXor(), 'astToolkit.dump': 'ast.BitXor()', 'ast.dump': 'BitXor()'}
		, 'astMinimal': {'expression': ast.BitXor(), 'astToolkit.dump': 'ast.BitXor()', 'ast.dump': 'BitXor()'}
	}
	, 'boolop': {
		'MakeMaximallyEmpty': {'expression': Make.boolop(), 'astToolkit.dump': 'ast.boolop()', 'ast.dump': 'boolop()'}
		, 'astMinimal': {'expression': ast.boolop(), 'astToolkit.dump': 'ast.boolop()', 'ast.dump': 'boolop()'}
	}
	, 'BoolOp': {
		'MakeMaximallyEmpty': {
			'expression': Make.BoolOp(op=Make.And(), values=[Make.Name(id='Make_BoolOp_values')])
			, 'astToolkit.dump': "ast.BoolOp(op=ast.And(), values=[ast.Name(id='Make_BoolOp_values', ctx=ast.Load())])"
			, 'ast.dump': "BoolOp(op=And(), values=[Name(id='Make_BoolOp_values', ctx=Load())])"
		}
		, 'MakeMinimal': {
			'expression': Make.BoolOp(op=Make.And(), values=[Make.Name(id='Make_BoolOp_values', context=Make.Load())])
			, 'astToolkit.dump': "ast.BoolOp(op=ast.And(), values=[ast.Name(id='Make_BoolOp_values', ctx=ast.Load())])"
			, 'ast.dump': "BoolOp(op=And(), values=[Name(id='Make_BoolOp_values', ctx=Load())])"
		}
		, 'astMinimal': {
			'expression': ast.BoolOp(op=ast.And())
			, 'astToolkit.dump': 'ast.BoolOp(op=ast.And(), values=[])'
			, 'ast.dump': 'BoolOp(op=And(), values=[])'
		}
	}
	, 'Break': {
		'MakeMaximallyEmpty': {'expression': Make.Break(), 'astToolkit.dump': 'ast.Break()', 'ast.dump': 'Break()'}
		, 'astMinimal': {'expression': ast.Break(), 'astToolkit.dump': 'ast.Break()', 'ast.dump': 'Break()'}
	}
	, 'Call': {
		'MakeMaximallyEmpty': {
			'expression': Make.Call(callee=Make.Name(id='Make_Call_callee'))
			, 'astToolkit.dump': "ast.Call(func=ast.Name(id='Make_Call_callee', ctx=ast.Load()), args=[], keywords=[])"
			, 'ast.dump': "Call(func=Name(id='Make_Call_callee', ctx=Load()), args=[], keywords=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.Call(callee=Make.Name(id='Make_Call_callee', context=Make.Load()), listParameters=[], list_keyword=[])
			, 'astToolkit.dump': "ast.Call(func=ast.Name(id='Make_Call_callee', ctx=ast.Load()), args=[], keywords=[])"
			, 'ast.dump': "Call(func=Name(id='Make_Call_callee', ctx=Load()), args=[], keywords=[])"
		}
		, 'astMinimal': {
			'expression': ast.Call(func=ast.Name(id='ast_Call_func'))
			, 'astToolkit.dump': "ast.Call(func=ast.Name(id='ast_Call_func', ctx=ast.Load()), args=[], keywords=[])"
			, 'ast.dump': "Call(func=Name(id='ast_Call_func', ctx=Load()), args=[], keywords=[])"
		}
	}
	, 'ClassDef': {
		'MakeMaximallyEmpty': {
			'expression': Make.ClassDef(name='Make_ClassDef')
			, 'astToolkit.dump': "ast.ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
			, 'ast.dump': "ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.ClassDef(name='Make_ClassDef', bases=[], list_keyword=[], body=[], decorator_list=[], type_params=[])
			, 'astToolkit.dump': "ast.ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
			, 'ast.dump': "ClassDef(name='Make_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
		}
		, 'astMinimal': {
			'expression': ast.ClassDef(name='ast_ClassDef')
			, 'astToolkit.dump': "ast.ClassDef(name='ast_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
			, 'ast.dump': "ClassDef(name='ast_ClassDef', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
		}
	}
	, 'cmpop': {
		'MakeMaximallyEmpty': {'expression': Make.cmpop(), 'astToolkit.dump': 'ast.cmpop()', 'ast.dump': 'cmpop()'}
		, 'astMinimal': {'expression': ast.cmpop(), 'astToolkit.dump': 'ast.cmpop()', 'ast.dump': 'cmpop()'}
	}
	, 'Compare': {
		'MakeMaximallyEmpty': {
			'expression': Make.Compare(
				left=Make.Name(id='Make_Compare_left'), ops=[Make.Eq()], comparators=[Make.Name(id='Make_Compare_comparators')]
			)
			, 'astToolkit.dump': "ast.Compare(left=ast.Name(id='Make_Compare_left', ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Name(id='Make_Compare_comparators', ctx=ast.Load())])"
			, 'ast.dump': "Compare(left=Name(id='Make_Compare_left', ctx=Load()), ops=[Eq()], comparators=[Name(id='Make_Compare_comparators', ctx=Load())])"
		}
		, 'MakeMinimal': {
			'expression': Make.Compare(
				left=Make.Name(id='Make_Compare_left', context=Make.Load())
				, ops=[Make.Eq()]
				, comparators=[Make.Name(id='Make_Compare_comparators', context=Make.Load())]
			)
			, 'astToolkit.dump': "ast.Compare(left=ast.Name(id='Make_Compare_left', ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Name(id='Make_Compare_comparators', ctx=ast.Load())])"
			, 'ast.dump': "Compare(left=Name(id='Make_Compare_left', ctx=Load()), ops=[Eq()], comparators=[Name(id='Make_Compare_comparators', ctx=Load())])"
		}
		, 'astMinimal': {
			'expression': ast.Compare(left=ast.Name(id='ast_Compare_left'))
			, 'astToolkit.dump': "ast.Compare(left=ast.Name(id='ast_Compare_left', ctx=ast.Load()), ops=[], comparators=[])"
			, 'ast.dump': "Compare(left=Name(id='ast_Compare_left', ctx=Load()), ops=[], comparators=[])"
		}
	}
	, 'comprehension': {
		'MakeMaximallyEmpty': {
			'expression': Make.comprehension(
				target=Make.Name(id='Make_comprehension_target', context=Make.Store())
				, iter=Make.Name(id='Make_comprehension_iter')
				, ifs=[Make.Name(id='Make_comprehension_ifs')]
			)
			, 'astToolkit.dump': "ast.comprehension(target=ast.Name(id='Make_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='Make_comprehension_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_comprehension_ifs', ctx=ast.Load())], is_async=0)"
			, 'ast.dump': "comprehension(target=Name(id='Make_comprehension_target', ctx=Store()), iter=Name(id='Make_comprehension_iter', ctx=Load()), ifs=[Name(id='Make_comprehension_ifs', ctx=Load())], is_async=0)"
		}
		, 'MakeMinimal': {
			'expression': Make.comprehension(
				target=Make.Name(id='Make_comprehension_target', context=Make.Store())
				, iter=Make.Name(id='Make_comprehension_iter', context=Make.Load())
				, ifs=[Make.Name(id='Make_comprehension_ifs', context=Make.Load())]
				, is_async=0
			)
			, 'astToolkit.dump': "ast.comprehension(target=ast.Name(id='Make_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='Make_comprehension_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_comprehension_ifs', ctx=ast.Load())], is_async=0)"
			, 'ast.dump': "comprehension(target=Name(id='Make_comprehension_target', ctx=Store()), iter=Name(id='Make_comprehension_iter', ctx=Load()), ifs=[Name(id='Make_comprehension_ifs', ctx=Load())], is_async=0)"
		}
		, 'astMinimal': {
			'expression': ast.comprehension(
				target=ast.Name(id='ast_comprehension_target', ctx=ast.Store())
				, iter=ast.Name(id='ast_comprehension_iter', ctx=ast.Load())
				, is_async=0
			)
			, 'astToolkit.dump': "ast.comprehension(target=ast.Name(id='ast_comprehension_target', ctx=ast.Store()), iter=ast.Name(id='ast_comprehension_iter', ctx=ast.Load()), ifs=[], is_async=0)"
			, 'ast.dump': "comprehension(target=Name(id='ast_comprehension_target', ctx=Store()), iter=Name(id='ast_comprehension_iter', ctx=Load()), ifs=[], is_async=0)"
		}
	}
	, 'Constant': {
		'MakeMaximallyEmpty': {
			'expression': Make.Constant(value='Make_Constant')
			, 'astToolkit.dump': "ast.Constant(value='Make_Constant', kind=None)"
			, 'ast.dump': "Constant(value='Make_Constant')"
		}
		, 'MakeMinimal': {
			'expression': Make.Constant(value='Make_Constant', kind=None)
			, 'astToolkit.dump': "ast.Constant(value='Make_Constant', kind=None)"
			, 'ast.dump': "Constant(value='Make_Constant')"
		}
		, 'astMinimal': {
			'expression': ast.Constant(value='ast_Constant')
			, 'astToolkit.dump': "ast.Constant(value='ast_Constant', kind=None)"
			, 'ast.dump': "Constant(value='ast_Constant')"
		}
	}
	, 'Continue': {
		'MakeMaximallyEmpty': {
			'expression': Make.Continue()
			, 'astToolkit.dump': 'ast.Continue()'
			, 'ast.dump': 'Continue()'
		}
		, 'astMinimal': {'expression': ast.Continue(), 'astToolkit.dump': 'ast.Continue()', 'ast.dump': 'Continue()'}
	}
	, 'Del': {
		'MakeMaximallyEmpty': {'expression': Make.Del(), 'astToolkit.dump': 'ast.Del()', 'ast.dump': 'Del()'}
		, 'astMinimal': {'expression': ast.Del(), 'astToolkit.dump': 'ast.Del()', 'ast.dump': 'Del()'}
	}
	, 'Delete': {
		'MakeMaximallyEmpty': {
			'expression': Make.Delete(targets=[Make.Name(id='Make_Delete_targets', context=Make.Del())])
			, 'astToolkit.dump': "ast.Delete(targets=[ast.Name(id='Make_Delete_targets', ctx=ast.Del())])"
			, 'ast.dump': "Delete(targets=[Name(id='Make_Delete_targets', ctx=Del())])"
		}
		, 'astMinimal': {
			'expression': ast.Delete()
			, 'astToolkit.dump': 'ast.Delete(targets=[])'
			, 'ast.dump': 'Delete(targets=[])'
		}
	}
	, 'Dict': {
		'MakeMaximallyEmpty': {
			'expression': Make.Dict()
			, 'astToolkit.dump': 'ast.Dict(keys=[None], values=[])'
			, 'ast.dump': 'Dict(keys=[None], values=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.Dict(keys=[None], values=[])
			, 'astToolkit.dump': 'ast.Dict(keys=[None], values=[])'
			, 'ast.dump': 'Dict(keys=[None], values=[])'
		}
		, 'astMinimal': {
			'expression': ast.Dict()
			, 'astToolkit.dump': 'ast.Dict(keys=[], values=[])'
			, 'ast.dump': 'Dict(keys=[], values=[])'
		}
	}
	, 'DictComp': {
		'MakeMaximallyEmpty': {
			'expression': Make.DictComp(
				key=Make.Name(id='Make_DictComp_key')
				, value=Make.Name(id='Make_DictComp_value')
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_DictComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_DictComp_generators_iter')
						, ifs=[Make.Name(id='Make_DictComp_generators_ifs')]
					)
				]
			)
			, 'astToolkit.dump': "ast.DictComp(key=ast.Name(id='Make_DictComp_key', ctx=ast.Load()), value=ast.Name(id='Make_DictComp_value', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_DictComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_DictComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_DictComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "DictComp(key=Name(id='Make_DictComp_key', ctx=Load()), value=Name(id='Make_DictComp_value', ctx=Load()), generators=[comprehension(target=Name(id='Make_DictComp_generators_target', ctx=Store()), iter=Name(id='Make_DictComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_DictComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'MakeMinimal': {
			'expression': Make.DictComp(
				key=Make.Name(id='Make_DictComp_key', context=Make.Load())
				, value=Make.Name(id='Make_DictComp_value', context=Make.Load())
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_DictComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_DictComp_generators_iter', context=Make.Load())
						, ifs=[Make.Name(id='Make_DictComp_generators_ifs', context=Make.Load())]
						, is_async=0
					)
				]
			)
			, 'astToolkit.dump': "ast.DictComp(key=ast.Name(id='Make_DictComp_key', ctx=ast.Load()), value=ast.Name(id='Make_DictComp_value', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_DictComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_DictComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_DictComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "DictComp(key=Name(id='Make_DictComp_key', ctx=Load()), value=Name(id='Make_DictComp_value', ctx=Load()), generators=[comprehension(target=Name(id='Make_DictComp_generators_target', ctx=Store()), iter=Name(id='Make_DictComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_DictComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'astMinimal': {
			'expression': ast.DictComp(key=ast.Name(id='ast_DictComp_key'), value=ast.Name(id='ast_DictComp_value'))
			, 'astToolkit.dump': "ast.DictComp(key=ast.Name(id='ast_DictComp_key', ctx=ast.Load()), value=ast.Name(id='ast_DictComp_value', ctx=ast.Load()), generators=[])"
			, 'ast.dump': "DictComp(key=Name(id='ast_DictComp_key', ctx=Load()), value=Name(id='ast_DictComp_value', ctx=Load()), generators=[])"
		}
	}
	, 'Div': {
		'MakeMaximallyEmpty': {'expression': Make.Div(), 'astToolkit.dump': 'ast.Div()', 'ast.dump': 'Div()'}
		, 'astMinimal': {'expression': ast.Div(), 'astToolkit.dump': 'ast.Div()', 'ast.dump': 'Div()'}
	}
	, 'Eq': {
		'MakeMaximallyEmpty': {'expression': Make.Eq(), 'astToolkit.dump': 'ast.Eq()', 'ast.dump': 'Eq()'}
		, 'astMinimal': {'expression': ast.Eq(), 'astToolkit.dump': 'ast.Eq()', 'ast.dump': 'Eq()'}
	}
	, 'excepthandler': {
		'MakeMaximallyEmpty': {
			'expression': Make.excepthandler()
			, 'astToolkit.dump': 'ast.excepthandler()'
			, 'ast.dump': 'excepthandler()'
		}
		, 'astMinimal': {
			'expression': ast.excepthandler()
			, 'astToolkit.dump': 'ast.excepthandler()'
			, 'ast.dump': 'excepthandler()'
		}
	}
	, 'ExceptHandler': {
		'MakeMaximallyEmpty': {
			'expression': Make.ExceptHandler()
			, 'astToolkit.dump': 'ast.ExceptHandler(type=None, name=None, body=[])'
			, 'ast.dump': 'ExceptHandler(body=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.ExceptHandler(type=None, name=None, body=[])
			, 'astToolkit.dump': 'ast.ExceptHandler(type=None, name=None, body=[])'
			, 'ast.dump': 'ExceptHandler(body=[])'
		}
		, 'astMinimal': {
			'expression': ast.ExceptHandler()
			, 'astToolkit.dump': 'ast.ExceptHandler(type=None, name=None, body=[])'
			, 'ast.dump': 'ExceptHandler(body=[])'
		}
	}
	, 'expr_context': {
		'MakeMaximallyEmpty': {
			'expression': Make.expr_context()
			, 'astToolkit.dump': 'ast.expr_context()'
			, 'ast.dump': 'expr_context()'
		}
		, 'astMinimal': {
			'expression': ast.expr_context()
			, 'astToolkit.dump': 'ast.expr_context()'
			, 'ast.dump': 'expr_context()'
		}
	}
	, 'expr': {
		'MakeMaximallyEmpty': {'expression': Make.expr(), 'astToolkit.dump': 'ast.expr()', 'ast.dump': 'expr()'}
		, 'astMinimal': {'expression': ast.expr(), 'astToolkit.dump': 'ast.expr()', 'ast.dump': 'expr()'}
	}
	, 'Expr': {
		'MakeMaximallyEmpty': {
			'expression': Make.Expr(value=Make.Name(id='Make_Expr_value'))
			, 'astToolkit.dump': "ast.Expr(value=ast.Name(id='Make_Expr_value', ctx=ast.Load()))"
			, 'ast.dump': "Expr(value=Name(id='Make_Expr_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Expr(value=Make.Name(id='Make_Expr_value', context=Make.Load()))
			, 'astToolkit.dump': "ast.Expr(value=ast.Name(id='Make_Expr_value', ctx=ast.Load()))"
			, 'ast.dump': "Expr(value=Name(id='Make_Expr_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Expr(value=ast.Name(id='ast_Expr_value'))
			, 'astToolkit.dump': "ast.Expr(value=ast.Name(id='ast_Expr_value', ctx=ast.Load()))"
			, 'ast.dump': "Expr(value=Name(id='ast_Expr_value', ctx=Load()))"
		}
	}
	, 'Expression': {
		'MakeMaximallyEmpty': {
			'expression': Make.Expression(body=Make.Name(id='Make_Expression_body'))
			, 'astToolkit.dump': "ast.Expression(body=ast.Name(id='Make_Expression_body', ctx=ast.Load()))"
			, 'ast.dump': "Expression(body=Name(id='Make_Expression_body', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Expression(body=Make.Name(id='Make_Expression_body', context=Make.Load()))
			, 'astToolkit.dump': "ast.Expression(body=ast.Name(id='Make_Expression_body', ctx=ast.Load()))"
			, 'ast.dump': "Expression(body=Name(id='Make_Expression_body', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Expression(body=ast.Name(id='ast_Expression_body'))
			, 'astToolkit.dump': "ast.Expression(body=ast.Name(id='ast_Expression_body', ctx=ast.Load()))"
			, 'ast.dump': "Expression(body=Name(id='ast_Expression_body', ctx=Load()))"
		}
	}
	, 'FloorDiv': {
		'MakeMaximallyEmpty': {
			'expression': Make.FloorDiv()
			, 'astToolkit.dump': 'ast.FloorDiv()'
			, 'ast.dump': 'FloorDiv()'
		}
		, 'astMinimal': {'expression': ast.FloorDiv(), 'astToolkit.dump': 'ast.FloorDiv()', 'ast.dump': 'FloorDiv()'}
	}
	, 'For': {
		'MakeMaximallyEmpty': {
			'expression': Make.For(
				target=Make.Name(id='Make_For_target', context=Make.Store()), iter=Make.Name(id='Make_For_iter'), body=[Make.Pass()]
			)
			, 'astToolkit.dump': "ast.For(target=ast.Name(id='Make_For_target', ctx=ast.Store()), iter=ast.Name(id='Make_For_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)"
			, 'ast.dump': "For(target=Name(id='Make_For_target', ctx=Store()), iter=Name(id='Make_For_iter', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.For(
				target=Make.Name(id='Make_For_target', context=Make.Store())
				, iter=Make.Name(id='Make_For_iter', context=Make.Load())
				, body=[Make.Pass()]
				, orElse=[]
			)
			, 'astToolkit.dump': "ast.For(target=ast.Name(id='Make_For_target', ctx=ast.Store()), iter=ast.Name(id='Make_For_iter', ctx=ast.Load()), body=[ast.Pass()], orelse=[], type_comment=None)"
			, 'ast.dump': "For(target=Name(id='Make_For_target', ctx=Store()), iter=Name(id='Make_For_iter', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'astMinimal': {
			'expression': ast.For(target=ast.Name(id='ast_For_target', ctx=ast.Store()), iter=ast.Name(id='ast_For_iter'))
			, 'astToolkit.dump': "ast.For(target=ast.Name(id='ast_For_target', ctx=ast.Store()), iter=ast.Name(id='ast_For_iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)"
			, 'ast.dump': "For(target=Name(id='ast_For_target', ctx=Store()), iter=Name(id='ast_For_iter', ctx=Load()), body=[], orelse=[])"
		}
	}
	, 'FormattedValue': {
		'MakeMaximallyEmpty': {
			'expression': Make.FormattedValue(value=Make.Name(id='Make_FormattedValue_value'), conversion=-1)
			, 'astToolkit.dump': "ast.FormattedValue(value=ast.Name(id='Make_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)"
			, 'ast.dump': "FormattedValue(value=Name(id='Make_FormattedValue_value', ctx=Load()), conversion=-1)"
		}
		, 'MakeMinimal': {
			'expression': Make.FormattedValue(
				value=Make.Name(id='Make_FormattedValue_value', context=Make.Load()), conversion=-1, format_spec=None
			)
			, 'astToolkit.dump': "ast.FormattedValue(value=ast.Name(id='Make_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)"
			, 'ast.dump': "FormattedValue(value=Name(id='Make_FormattedValue_value', ctx=Load()), conversion=-1)"
		}
		, 'astMinimal': {
			'expression': ast.FormattedValue(value=ast.Name(id='ast_FormattedValue_value'), conversion=-1)
			, 'astToolkit.dump': "ast.FormattedValue(value=ast.Name(id='ast_FormattedValue_value', ctx=ast.Load()), conversion=-1, format_spec=None)"
			, 'ast.dump': "FormattedValue(value=Name(id='ast_FormattedValue_value', ctx=Load()), conversion=-1)"
		}
	}
	, 'FunctionDef': {
		'MakeMaximallyEmpty': {
			'expression': Make.FunctionDef(name='Make_FunctionDef')
			, 'astToolkit.dump': "ast.FunctionDef(name='Make_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "FunctionDef(name='Make_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.FunctionDef(
				name='Make_FunctionDef'
				, argumentSpecification=Make.arguments(
					posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]
				)
				, body=[]
				, decorator_list=[]
				, returns=None
				, type_params=[]
			)
			, 'astToolkit.dump': "ast.FunctionDef(name='Make_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "FunctionDef(name='Make_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"
		}
		, 'astMinimal': {
			'expression': ast.FunctionDef(name='ast_FunctionDef', args=ast.arguments())
			, 'astToolkit.dump': "ast.FunctionDef(name='ast_FunctionDef', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
			, 'ast.dump': "FunctionDef(name='ast_FunctionDef', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[], decorator_list=[], type_params=[])"
		}
	}
	, 'FunctionType': {
		'MakeMaximallyEmpty': {
			'expression': Make.FunctionType(
				argtypes=[Make.Name(id='Make_FunctionType_argtypes')], returns=Make.Name(id='Make_FunctionType_returns')
			)
			, 'astToolkit.dump': "ast.FunctionType(argtypes=[ast.Name(id='Make_FunctionType_argtypes', ctx=ast.Load())], returns=ast.Name(id='Make_FunctionType_returns', ctx=ast.Load()))"
			, 'ast.dump': "FunctionType(argtypes=[Name(id='Make_FunctionType_argtypes', ctx=Load())], returns=Name(id='Make_FunctionType_returns', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.FunctionType(
				argtypes=[Make.Name(id='Make_FunctionType_argtypes', context=Make.Load())]
				, returns=Make.Name(id='Make_FunctionType_returns', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.FunctionType(argtypes=[ast.Name(id='Make_FunctionType_argtypes', ctx=ast.Load())], returns=ast.Name(id='Make_FunctionType_returns', ctx=ast.Load()))"
			, 'ast.dump': "FunctionType(argtypes=[Name(id='Make_FunctionType_argtypes', ctx=Load())], returns=Name(id='Make_FunctionType_returns', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.FunctionType(returns=ast.Name(id='ast_FunctionType_returns'))
			, 'astToolkit.dump': "ast.FunctionType(argtypes=[], returns=ast.Name(id='ast_FunctionType_returns', ctx=ast.Load()))"
			, 'ast.dump': "FunctionType(argtypes=[], returns=Name(id='ast_FunctionType_returns', ctx=Load()))"
		}
	}
	, 'GeneratorExp': {
		'MakeMaximallyEmpty': {
			'expression': Make.GeneratorExp(
				element=Make.Name(id='Make_GeneratorExp_element')
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_GeneratorExp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_GeneratorExp_generators_iter')
						, ifs=[Make.Name(id='Make_GeneratorExp_generators_ifs')]
					)
				]
			)
			, 'astToolkit.dump': "ast.GeneratorExp(elt=ast.Name(id='Make_GeneratorExp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_GeneratorExp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_GeneratorExp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_GeneratorExp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "GeneratorExp(elt=Name(id='Make_GeneratorExp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_GeneratorExp_generators_target', ctx=Store()), iter=Name(id='Make_GeneratorExp_generators_iter', ctx=Load()), ifs=[Name(id='Make_GeneratorExp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'MakeMinimal': {
			'expression': Make.GeneratorExp(
				element=Make.Name(id='Make_GeneratorExp_element', context=Make.Load())
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_GeneratorExp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_GeneratorExp_generators_iter', context=Make.Load())
						, ifs=[Make.Name(id='Make_GeneratorExp_generators_ifs', context=Make.Load())]
						, is_async=0
					)
				]
			)
			, 'astToolkit.dump': "ast.GeneratorExp(elt=ast.Name(id='Make_GeneratorExp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_GeneratorExp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_GeneratorExp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_GeneratorExp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "GeneratorExp(elt=Name(id='Make_GeneratorExp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_GeneratorExp_generators_target', ctx=Store()), iter=Name(id='Make_GeneratorExp_generators_iter', ctx=Load()), ifs=[Name(id='Make_GeneratorExp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'astMinimal': {
			'expression': ast.GeneratorExp(elt=ast.Name(id='ast_GeneratorExp_element'))
			, 'astToolkit.dump': "ast.GeneratorExp(elt=ast.Name(id='ast_GeneratorExp_element', ctx=ast.Load()), generators=[])"
			, 'ast.dump': "GeneratorExp(elt=Name(id='ast_GeneratorExp_element', ctx=Load()), generators=[])"
		}
	}
	, 'Global': {
		'MakeMaximallyEmpty': {
			'expression': Make.Global(names=['Make_Global'])
			, 'astToolkit.dump': "ast.Global(names=['Make_Global'])"
			, 'ast.dump': "Global(names=['Make_Global'])"
		}
		, 'astMinimal': {
			'expression': ast.Global()
			, 'astToolkit.dump': 'ast.Global(names=[])'
			, 'ast.dump': 'Global(names=[])'
		}
	}
	, 'Gt': {
		'MakeMaximallyEmpty': {'expression': Make.Gt(), 'astToolkit.dump': 'ast.Gt()', 'ast.dump': 'Gt()'}
		, 'astMinimal': {'expression': ast.Gt(), 'astToolkit.dump': 'ast.Gt()', 'ast.dump': 'Gt()'}
	}
	, 'GtE': {
		'MakeMaximallyEmpty': {'expression': Make.GtE(), 'astToolkit.dump': 'ast.GtE()', 'ast.dump': 'GtE()'}
		, 'astMinimal': {'expression': ast.GtE(), 'astToolkit.dump': 'ast.GtE()', 'ast.dump': 'GtE()'}
	}
	, 'If': {
		'MakeMaximallyEmpty': {
			'expression': Make.If(test=Make.Name(id='Make_If_test'), body=[Make.Pass()])
			, 'astToolkit.dump': "ast.If(test=ast.Name(id='Make_If_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])"
			, 'ast.dump': "If(test=Name(id='Make_If_test', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.If(test=Make.Name(id='Make_If_test', context=Make.Load()), body=[Make.Pass()], orElse=[])
			, 'astToolkit.dump': "ast.If(test=ast.Name(id='Make_If_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])"
			, 'ast.dump': "If(test=Name(id='Make_If_test', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'astMinimal': {
			'expression': ast.If(test=ast.Name(id='ast_If_test'))
			, 'astToolkit.dump': "ast.If(test=ast.Name(id='ast_If_test', ctx=ast.Load()), body=[], orelse=[])"
			, 'ast.dump': "If(test=Name(id='ast_If_test', ctx=Load()), body=[], orelse=[])"
		}
	}
	, 'IfExp': {
		'MakeMaximallyEmpty': {
			'expression': Make.IfExp(
				test=Make.Name(id='Make_IfExp_test'), body=Make.Name(id='Make_IfExp_body'), orElse=Make.Name(id='Make_IfExp_orelse')
			)
			, 'astToolkit.dump': "ast.IfExp(test=ast.Name(id='Make_IfExp_test', ctx=ast.Load()), body=ast.Name(id='Make_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='Make_IfExp_orelse', ctx=ast.Load()))"
			, 'ast.dump': "IfExp(test=Name(id='Make_IfExp_test', ctx=Load()), body=Name(id='Make_IfExp_body', ctx=Load()), orelse=Name(id='Make_IfExp_orelse', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.IfExp(
				test=Make.Name(id='Make_IfExp_test', context=Make.Load())
				, body=Make.Name(id='Make_IfExp_body', context=Make.Load())
				, orElse=Make.Name(id='Make_IfExp_orElse', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.IfExp(test=ast.Name(id='Make_IfExp_test', ctx=ast.Load()), body=ast.Name(id='Make_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='Make_IfExp_orElse', ctx=ast.Load()))"
			, 'ast.dump': "IfExp(test=Name(id='Make_IfExp_test', ctx=Load()), body=Name(id='Make_IfExp_body', ctx=Load()), orelse=Name(id='Make_IfExp_orElse', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.IfExp(
				test=ast.Name(id='ast_IfExp_test'), body=ast.Name(id='ast_IfExp_body'), orelse=ast.Name(id='ast_IfExp_orelse')
			)
			, 'astToolkit.dump': "ast.IfExp(test=ast.Name(id='ast_IfExp_test', ctx=ast.Load()), body=ast.Name(id='ast_IfExp_body', ctx=ast.Load()), orelse=ast.Name(id='ast_IfExp_orelse', ctx=ast.Load()))"
			, 'ast.dump': "IfExp(test=Name(id='ast_IfExp_test', ctx=Load()), body=Name(id='ast_IfExp_body', ctx=Load()), orelse=Name(id='ast_IfExp_orelse', ctx=Load()))"
		}
	}
	, 'Import': {
		'MakeMaximallyEmpty': {
			'expression': Make.Import(dotModule='Make.Import')
			, 'astToolkit.dump': "ast.Import(names=[ast.alias(name='Make.Import', asname=None)])"
			, 'ast.dump': "Import(names=[alias(name='Make.Import')])"
		}
		, 'astMinimal': {
			'expression': ast.Import()
			, 'astToolkit.dump': 'ast.Import(names=[])'
			, 'ast.dump': 'Import(names=[])'
		}
	}
	, 'ImportFrom': {
		'MakeMaximallyEmpty': {
			'expression': Make.ImportFrom(dotModule='Make.ImportFrom', list_alias=[Make.alias(dotModule='Make_ImportFrom_alias')])
			, 'astToolkit.dump': "ast.ImportFrom(module='Make.ImportFrom', names=[ast.alias(name='Make_ImportFrom_alias', asname=None)], level=0)"
			, 'ast.dump': "ImportFrom(module='Make.ImportFrom', names=[alias(name='Make_ImportFrom_alias')], level=0)"
		}
		, 'MakeMinimal': {
			'expression': Make.ImportFrom(
				dotModule='Make.ImportFrom', list_alias=[Make.alias(dotModule='Make_ImportFrom_alias', asName=None)], level=0
			)
			, 'astToolkit.dump': "ast.ImportFrom(module='Make.ImportFrom', names=[ast.alias(name='Make_ImportFrom_alias', asname=None)], level=0)"
			, 'ast.dump': "ImportFrom(module='Make.ImportFrom', names=[alias(name='Make_ImportFrom_alias')], level=0)"
		}
		, 'astMinimal': {
			'expression': ast.ImportFrom()
			, 'astToolkit.dump': 'ast.ImportFrom(module=None, names=[], level=None)'
			, 'ast.dump': 'ImportFrom(names=[])'
		},
	}
	, 'In': {
		'MakeMaximallyEmpty': {'expression': Make.In(), 'astToolkit.dump': 'ast.In()', 'ast.dump': 'In()'}
		, 'astMinimal': {'expression': ast.In(), 'astToolkit.dump': 'ast.In()', 'ast.dump': 'In()'}
	}
	, 'Interactive': {
		'MakeMaximallyEmpty': {
			'expression': Make.Interactive(body=[Make.Pass()])
			, 'astToolkit.dump': 'ast.Interactive(body=[ast.Pass()])'
			, 'ast.dump': 'Interactive(body=[Pass()])'
		}
		, 'astMinimal': {
			'expression': ast.Interactive()
			, 'astToolkit.dump': 'ast.Interactive(body=[])'
			, 'ast.dump': 'Interactive(body=[])'
		}
	}
	, 'Invert': {
		'MakeMaximallyEmpty': {'expression': Make.Invert(), 'astToolkit.dump': 'ast.Invert()', 'ast.dump': 'Invert()'}
		, 'astMinimal': {'expression': ast.Invert(), 'astToolkit.dump': 'ast.Invert()', 'ast.dump': 'Invert()'}
	}
	, 'Is': {
		'MakeMaximallyEmpty': {'expression': Make.Is(), 'astToolkit.dump': 'ast.Is()', 'ast.dump': 'Is()'}
		, 'astMinimal': {'expression': ast.Is(), 'astToolkit.dump': 'ast.Is()', 'ast.dump': 'Is()'}
	}
	, 'IsNot': {
		'MakeMaximallyEmpty': {'expression': Make.IsNot(), 'astToolkit.dump': 'ast.IsNot()', 'ast.dump': 'IsNot()'}
		, 'astMinimal': {'expression': ast.IsNot(), 'astToolkit.dump': 'ast.IsNot()', 'ast.dump': 'IsNot()'}
	}
	, 'JoinedStr': {
		'MakeMaximallyEmpty': {
			'expression': Make.JoinedStr(values=[Make.Constant(value='Make_JoinedStr_values')])
			, 'astToolkit.dump': "ast.JoinedStr(values=[ast.Constant(value='Make_JoinedStr_values', kind=None)])"
			, 'ast.dump': "JoinedStr(values=[Constant(value='Make_JoinedStr_values')])"
		}
		, 'MakeMinimal': {
			'expression': Make.JoinedStr(values=[Make.Constant(value='Make_JoinedStr_values', kind=None)])
			, 'astToolkit.dump': "ast.JoinedStr(values=[ast.Constant(value='Make_JoinedStr_values', kind=None)])"
			, 'ast.dump': "JoinedStr(values=[Constant(value='Make_JoinedStr_values')])"
		}
		, 'astMinimal': {
			'expression': ast.JoinedStr()
			, 'astToolkit.dump': 'ast.JoinedStr(values=[])'
			, 'ast.dump': 'JoinedStr(values=[])'
		}
	}
	, 'keyword': {
		'MakeMaximallyEmpty': {
			'expression': Make.keyword(
				Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo=None, value=Make.Name(id='Make_keyword_value')
			)
			, 'astToolkit.dump': "ast.keyword(arg=None, value=ast.Name(id='Make_keyword_value', ctx=ast.Load()))"
			, 'ast.dump': "keyword(value=Name(id='Make_keyword_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.keyword(
				Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo=None
				, value=Make.Name(id='Make_keyword_value', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.keyword(arg=None, value=ast.Name(id='Make_keyword_value', ctx=ast.Load()))"
			, 'ast.dump': "keyword(value=Name(id='Make_keyword_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.keyword(value=ast.Name(id='ast_keyword_value'))
			, 'astToolkit.dump': "ast.keyword(arg=None, value=ast.Name(id='ast_keyword_value', ctx=ast.Load()))"
			, 'ast.dump': "keyword(value=Name(id='ast_keyword_value', ctx=Load()))"
		}
	}
	, 'Lambda': {
		'MakeMaximallyEmpty': {
			'expression': Make.Lambda(argumentSpecification=Make.arguments(), body=Make.Name(id='Make_Lambda_body'))
			, 'astToolkit.dump': "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]), body=ast.Name(id='Make_Lambda_body', ctx=ast.Load()))"
			, 'ast.dump': "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[]), body=Name(id='Make_Lambda_body', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.Lambda(
				argumentSpecification=Make.arguments(
					posonlyargs=[], list_arg=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]
				)
				, body=Make.Name(id='Make_Lambda_body', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[None], kwarg=None, defaults=[]), body=ast.Name(id='Make_Lambda_body', ctx=ast.Load()))"
			, 'ast.dump': "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[None], defaults=[]), body=Name(id='Make_Lambda_body', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.Lambda(args=ast.arguments(), body=ast.Name(id='ast_Lambda_body'))
			, 'astToolkit.dump': "ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Name(id='ast_Lambda_body', ctx=ast.Load()))"
			, 'ast.dump': "Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='ast_Lambda_body', ctx=Load()))"
		}
	}
	, 'List': {
		'MakeMaximallyEmpty': {
			'expression': Make.List()
			, 'astToolkit.dump': 'ast.List(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'List(elts=[], ctx=Load())'
		}
		, 'MakeMinimal': {
			'expression': Make.List(listElements=[], context=Make.Load())
			, 'astToolkit.dump': 'ast.List(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'List(elts=[], ctx=Load())'
		}
		, 'astMinimal': {
			'expression': ast.List()
			, 'astToolkit.dump': 'ast.List(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'List(elts=[], ctx=Load())'
		}
	}
	, 'ListComp': {
		'MakeMaximallyEmpty': {
			'expression': Make.ListComp(
				element=Make.Name(id='Make_ListComp_element')
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_ListComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_ListComp_generators_iter')
						, ifs=[Make.Name(id='Make_ListComp_generators_ifs')]
					)
				]
			)
			, 'astToolkit.dump': "ast.ListComp(elt=ast.Name(id='Make_ListComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_ListComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_ListComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_ListComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "ListComp(elt=Name(id='Make_ListComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_ListComp_generators_target', ctx=Store()), iter=Name(id='Make_ListComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_ListComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'MakeMinimal': {
			'expression': Make.ListComp(
				element=Make.Name(id='Make_ListComp_element', context=Make.Load())
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_ListComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_ListComp_generators_iter', context=Make.Load())
						, ifs=[Make.Name(id='Make_ListComp_generators_ifs', context=Make.Load())]
						, is_async=0
					)
				]
			)
			, 'astToolkit.dump': "ast.ListComp(elt=ast.Name(id='Make_ListComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_ListComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_ListComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_ListComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "ListComp(elt=Name(id='Make_ListComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_ListComp_generators_target', ctx=Store()), iter=Name(id='Make_ListComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_ListComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'astMinimal': {
			'expression': ast.ListComp(elt=ast.Name(id='ast_ListComp_element'))
			, 'astToolkit.dump': "ast.ListComp(elt=ast.Name(id='ast_ListComp_element', ctx=ast.Load()), generators=[])"
			, 'ast.dump': "ListComp(elt=Name(id='ast_ListComp_element', ctx=Load()), generators=[])"
		}
	}
	, 'Load': {
		'MakeMaximallyEmpty': {'expression': Make.Load(), 'astToolkit.dump': 'ast.Load()', 'ast.dump': 'Load()'}
		, 'astMinimal': {'expression': ast.Load(), 'astToolkit.dump': 'ast.Load()', 'ast.dump': 'Load()'}
	}
	, 'LShift': {
		'MakeMaximallyEmpty': {'expression': Make.LShift(), 'astToolkit.dump': 'ast.LShift()', 'ast.dump': 'LShift()'}
		, 'astMinimal': {'expression': ast.LShift(), 'astToolkit.dump': 'ast.LShift()', 'ast.dump': 'LShift()'}
	}
	, 'Lt': {
		'MakeMaximallyEmpty': {'expression': Make.Lt(), 'astToolkit.dump': 'ast.Lt()', 'ast.dump': 'Lt()'}
		, 'astMinimal': {'expression': ast.Lt(), 'astToolkit.dump': 'ast.Lt()', 'ast.dump': 'Lt()'}
	}
	, 'LtE': {
		'MakeMaximallyEmpty': {'expression': Make.LtE(), 'astToolkit.dump': 'ast.LtE()', 'ast.dump': 'LtE()'}
		, 'astMinimal': {'expression': ast.LtE(), 'astToolkit.dump': 'ast.LtE()', 'ast.dump': 'LtE()'}
	}
	, 'match_case': {
		'MakeMaximallyEmpty': {
			'expression': Make.match_case(pattern=Make.MatchAs())
			, 'astToolkit.dump': 'ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])'
			, 'ast.dump': 'match_case(pattern=MatchAs(), body=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.match_case(pattern=Make.MatchAs(pattern=None, name=None), guard=None, body=[])
			, 'astToolkit.dump': 'ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])'
			, 'ast.dump': 'match_case(pattern=MatchAs(), body=[])'
		}
		, 'astMinimal': {
			'expression': ast.match_case(pattern=ast.MatchAs())
			, 'astToolkit.dump': 'ast.match_case(pattern=ast.MatchAs(pattern=None, name=None), guard=None, body=[])'
			, 'ast.dump': 'match_case(pattern=MatchAs(), body=[])'
		}
	}
	, 'Match': {
		'MakeMaximallyEmpty': {
			'expression': Make.Match(subject=Make.Name(id='Make_Match_subject'))
			, 'astToolkit.dump': "ast.Match(subject=ast.Name(id='Make_Match_subject', ctx=ast.Load()), cases=[])"
			, 'ast.dump': "Match(subject=Name(id='Make_Match_subject', ctx=Load()), cases=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.Match(subject=Make.Name(id='Make_Match_subject', context=Make.Load()), cases=[])
			, 'astToolkit.dump': "ast.Match(subject=ast.Name(id='Make_Match_subject', ctx=ast.Load()), cases=[])"
			, 'ast.dump': "Match(subject=Name(id='Make_Match_subject', ctx=Load()), cases=[])"
		}
		, 'astMinimal': {
			'expression': ast.Match(subject=ast.Name(id='ast_Match_subject'))
			, 'astToolkit.dump': "ast.Match(subject=ast.Name(id='ast_Match_subject', ctx=ast.Load()), cases=[])"
			, 'ast.dump': "Match(subject=Name(id='ast_Match_subject', ctx=Load()), cases=[])"
		}
	}
	, 'MatchAs': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchAs()
			, 'astToolkit.dump': 'ast.MatchAs(pattern=None, name=None)'
			, 'ast.dump': 'MatchAs()'
		}
		, 'MakeMinimal': {
			'expression': Make.MatchAs(pattern=None, name=None)
			, 'astToolkit.dump': 'ast.MatchAs(pattern=None, name=None)'
			, 'ast.dump': 'MatchAs()'
		}
		, 'astMinimal': {
			'expression': ast.MatchAs()
			, 'astToolkit.dump': 'ast.MatchAs(pattern=None, name=None)'
			, 'ast.dump': 'MatchAs()'
		}
	}
	, 'MatchClass': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchClass(cls=Make.Name(id='Make_MatchClass_cls'))
			, 'astToolkit.dump': "ast.MatchClass(cls=ast.Name(id='Make_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
			, 'ast.dump': "MatchClass(cls=Name(id='Make_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.MatchClass(
				cls=Make.Name(id='Make_MatchClass_cls', context=Make.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[]
			)
			, 'astToolkit.dump': "ast.MatchClass(cls=ast.Name(id='Make_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
			, 'ast.dump': "MatchClass(cls=Name(id='Make_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
		}
		, 'astMinimal': {
			'expression': ast.MatchClass(cls=ast.Name(id='ast_MatchClass_cls'))
			, 'astToolkit.dump': "ast.MatchClass(cls=ast.Name(id='ast_MatchClass_cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
			, 'ast.dump': "MatchClass(cls=Name(id='ast_MatchClass_cls', ctx=Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
		}
	}
	, 'MatchMapping': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchMapping()
			, 'astToolkit.dump': 'ast.MatchMapping(keys=[], patterns=[], rest=None)'
			, 'ast.dump': 'MatchMapping(keys=[], patterns=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.MatchMapping(keys=[], patterns=[], rest=None)
			, 'astToolkit.dump': 'ast.MatchMapping(keys=[], patterns=[], rest=None)'
			, 'ast.dump': 'MatchMapping(keys=[], patterns=[])'
		}
		, 'astMinimal': {
			'expression': ast.MatchMapping()
			, 'astToolkit.dump': 'ast.MatchMapping(keys=[], patterns=[], rest=None)'
			, 'ast.dump': 'MatchMapping(keys=[], patterns=[])'
		}
	}
	, 'MatchOr': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchOr()
			, 'astToolkit.dump': 'ast.MatchOr(patterns=[])'
			, 'ast.dump': 'MatchOr(patterns=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.MatchOr(patterns=[])
			, 'astToolkit.dump': 'ast.MatchOr(patterns=[])'
			, 'ast.dump': 'MatchOr(patterns=[])'
		}
		, 'astMinimal': {
			'expression': ast.MatchOr()
			, 'astToolkit.dump': 'ast.MatchOr(patterns=[])'
			, 'ast.dump': 'MatchOr(patterns=[])'
		}
	}
	, 'MatchSequence': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchSequence()
			, 'astToolkit.dump': 'ast.MatchSequence(patterns=[])'
			, 'ast.dump': 'MatchSequence(patterns=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.MatchSequence(patterns=[])
			, 'astToolkit.dump': 'ast.MatchSequence(patterns=[])'
			, 'ast.dump': 'MatchSequence(patterns=[])'
		}
		, 'astMinimal': {
			'expression': ast.MatchSequence()
			, 'astToolkit.dump': 'ast.MatchSequence(patterns=[])'
			, 'ast.dump': 'MatchSequence(patterns=[])'
		}
	}
	, 'MatchSingleton': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchSingleton(value=True)
			, 'astToolkit.dump': 'ast.MatchSingleton(value=True)'
			, 'ast.dump': 'MatchSingleton(value=True)'
		}
		, 'astMinimal': {
			'expression': ast.MatchSingleton(value=True)
			, 'astToolkit.dump': 'ast.MatchSingleton(value=True)'
			, 'ast.dump': 'MatchSingleton(value=True)'
		}
	}
	, 'MatchStar': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchStar()
			, 'astToolkit.dump': 'ast.MatchStar(name=None)'
			, 'ast.dump': 'MatchStar()'
		}
		, 'MakeMinimal': {
			'expression': Make.MatchStar(name=None)
			, 'astToolkit.dump': 'ast.MatchStar(name=None)'
			, 'ast.dump': 'MatchStar()'
		}
		, 'astMinimal': {
			'expression': ast.MatchStar()
			, 'astToolkit.dump': 'ast.MatchStar(name=None)'
			, 'ast.dump': 'MatchStar()'
		}
	}
	, 'MatchValue': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatchValue(value=Make.Name(id='Make_MatchValue_value'))
			, 'astToolkit.dump': "ast.MatchValue(value=ast.Name(id='Make_MatchValue_value', ctx=ast.Load()))"
			, 'ast.dump': "MatchValue(value=Name(id='Make_MatchValue_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.MatchValue(value=Make.Name(id='Make_MatchValue_value', context=Make.Load()))
			, 'astToolkit.dump': "ast.MatchValue(value=ast.Name(id='Make_MatchValue_value', ctx=ast.Load()))"
			, 'ast.dump': "MatchValue(value=Name(id='Make_MatchValue_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.MatchValue(value=ast.Name(id='ast_MatchValue_value'))
			, 'astToolkit.dump': "ast.MatchValue(value=ast.Name(id='ast_MatchValue_value', ctx=ast.Load()))"
			, 'ast.dump': "MatchValue(value=Name(id='ast_MatchValue_value', ctx=Load()))"
		}
	}
	, 'MatMult': {
		'MakeMaximallyEmpty': {
			'expression': Make.MatMult()
			, 'astToolkit.dump': 'ast.MatMult()'
			, 'ast.dump': 'MatMult()'
		}
		, 'astMinimal': {'expression': ast.MatMult(), 'astToolkit.dump': 'ast.MatMult()', 'ast.dump': 'MatMult()'}
	}
	, 'Mod': {
		'MakeMaximallyEmpty': {'expression': Make.Mod(), 'astToolkit.dump': 'ast.Mod()', 'ast.dump': 'Mod()'}
		, 'astMinimal': {'expression': ast.Mod(), 'astToolkit.dump': 'ast.Mod()', 'ast.dump': 'Mod()'}
	}
	, 'mod': {
		'MakeMaximallyEmpty': {'expression': Make.mod(), 'astToolkit.dump': 'ast.mod()', 'ast.dump': 'mod()'}
		, 'astMinimal': {'expression': ast.mod(), 'astToolkit.dump': 'ast.mod()', 'ast.dump': 'mod()'}
	}
	, 'Module': {
		'MakeMaximallyEmpty': {
			'expression': Make.Module(body=[Make.Pass()])
			, 'astToolkit.dump': 'ast.Module(body=[ast.Pass()], type_ignores=[])'
			, 'ast.dump': 'Module(body=[Pass()], type_ignores=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.Module(body=[Make.Pass()], type_ignores=[])
			, 'astToolkit.dump': 'ast.Module(body=[ast.Pass()], type_ignores=[])'
			, 'ast.dump': 'Module(body=[Pass()], type_ignores=[])'
		}
		, 'astMinimal': {
			'expression': ast.Module()
			, 'astToolkit.dump': 'ast.Module(body=[], type_ignores=[])'
			, 'ast.dump': 'Module(body=[], type_ignores=[])'
		}
	}
	, 'Mult': {
		'MakeMaximallyEmpty': {'expression': Make.Mult(), 'astToolkit.dump': 'ast.Mult()', 'ast.dump': 'Mult()'}
		, 'astMinimal': {'expression': ast.Mult(), 'astToolkit.dump': 'ast.Mult()', 'ast.dump': 'Mult()'}
	}
	, 'Name': {
		'MakeMaximallyEmpty': {
			'expression': Make.Name(id='Make_Name')
			, 'astToolkit.dump': "ast.Name(id='Make_Name', ctx=ast.Load())"
			, 'ast.dump': "Name(id='Make_Name', ctx=Load())"
		}
		, 'MakeMinimal': {
			'expression': Make.Name(id='Make_Name', context=Make.Load())
			, 'astToolkit.dump': "ast.Name(id='Make_Name', ctx=ast.Load())"
			, 'ast.dump': "Name(id='Make_Name', ctx=Load())"
		}
		, 'astMinimal': {
			'expression': ast.Name(id='ast_Name')
			, 'astToolkit.dump': "ast.Name(id='ast_Name', ctx=ast.Load())"
			, 'ast.dump': "Name(id='ast_Name', ctx=Load())"
		}
	}
	, 'NamedExpr': {
		'MakeMaximallyEmpty': {
			'expression': Make.NamedExpr(
				target=Make.Name(id='Make_NamedExpr_target', context=Make.Store()), value=Make.Name(id='Make_NamedExpr_value')
			)
			, 'astToolkit.dump': "ast.NamedExpr(target=ast.Name(id='Make_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='Make_NamedExpr_value', ctx=ast.Load()))"
			, 'ast.dump': "NamedExpr(target=Name(id='Make_NamedExpr_target', ctx=Store()), value=Name(id='Make_NamedExpr_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.NamedExpr(
				target=Make.Name(id='Make_NamedExpr_target', context=Make.Store())
				, value=Make.Name(id='Make_NamedExpr_value', context=Make.Load())
			)
			, 'astToolkit.dump': "ast.NamedExpr(target=ast.Name(id='Make_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='Make_NamedExpr_value', ctx=ast.Load()))"
			, 'ast.dump': "NamedExpr(target=Name(id='Make_NamedExpr_target', ctx=Store()), value=Name(id='Make_NamedExpr_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.NamedExpr(
				target=ast.Name(id='ast_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='ast_NamedExpr_value')
			)
			, 'astToolkit.dump': "ast.NamedExpr(target=ast.Name(id='ast_NamedExpr_target', ctx=ast.Store()), value=ast.Name(id='ast_NamedExpr_value', ctx=ast.Load()))"
			, 'ast.dump': "NamedExpr(target=Name(id='ast_NamedExpr_target', ctx=Store()), value=Name(id='ast_NamedExpr_value', ctx=Load()))"
		}
	}
	, 'Nonlocal': {
		'MakeMaximallyEmpty': {
			'expression': Make.Nonlocal(names=['Make_Nonlocal'])
			, 'astToolkit.dump': "ast.Nonlocal(names=['Make_Nonlocal'])"
			, 'ast.dump': "Nonlocal(names=['Make_Nonlocal'])"
		}
		, 'astMinimal': {
			'expression': ast.Nonlocal()
			, 'astToolkit.dump': 'ast.Nonlocal(names=[])'
			, 'ast.dump': 'Nonlocal(names=[])'
		}
	}
	, 'Not': {
		'MakeMaximallyEmpty': {'expression': Make.Not(), 'astToolkit.dump': 'ast.Not()', 'ast.dump': 'Not()'}
		, 'astMinimal': {'expression': ast.Not(), 'astToolkit.dump': 'ast.Not()', 'ast.dump': 'Not()'}
	}
	, 'NotEq': {
		'MakeMaximallyEmpty': {'expression': Make.NotEq(), 'astToolkit.dump': 'ast.NotEq()', 'ast.dump': 'NotEq()'}
		, 'astMinimal': {'expression': ast.NotEq(), 'astToolkit.dump': 'ast.NotEq()', 'ast.dump': 'NotEq()'}
	}
	, 'NotIn': {
		'MakeMaximallyEmpty': {'expression': Make.NotIn(), 'astToolkit.dump': 'ast.NotIn()', 'ast.dump': 'NotIn()'}
		, 'astMinimal': {'expression': ast.NotIn(), 'astToolkit.dump': 'ast.NotIn()', 'ast.dump': 'NotIn()'}
	}
	, 'operator': {
		'MakeMaximallyEmpty': {
			'expression': Make.operator()
			, 'astToolkit.dump': 'ast.operator()'
			, 'ast.dump': 'operator()'
		}
		, 'astMinimal': {'expression': ast.operator(), 'astToolkit.dump': 'ast.operator()', 'ast.dump': 'operator()'}
	}
	, 'Or': {
		'MakeMaximallyEmpty': {'expression': Make.Or(), 'astToolkit.dump': 'ast.Or()', 'ast.dump': 'Or()'}
		, 'astMinimal': {'expression': ast.Or(), 'astToolkit.dump': 'ast.Or()', 'ast.dump': 'Or()'}
	}
	, "ParamSpec": {
		"class Make, maximally empty parameters": {"expression": Make.ParamSpec(name='Make_ParamSpec'), "astToolkit.dump": "ast.ParamSpec(name='Make_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='Make_ParamSpec')"}
		, "class Make, minimal parameters": {"expression": Make.ParamSpec(name='Make_ParamSpec', default_value=None), "astToolkit.dump": "ast.ParamSpec(name='Make_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='Make_ParamSpec')"}
		, "ast module, minimal parameters": {"expression": ast.ParamSpec(name='ast_ParamSpec'), "astToolkit.dump": "ast.ParamSpec(name='ast_ParamSpec', default_value=None)", "ast.dump": "ParamSpec(name='ast_ParamSpec')"}
	}
	, 'Pass': {
		'MakeMaximallyEmpty': {'expression': Make.Pass(), 'astToolkit.dump': 'ast.Pass()', 'ast.dump': 'Pass()'}
		, 'astMinimal': {'expression': ast.Pass(), 'astToolkit.dump': 'ast.Pass()', 'ast.dump': 'Pass()'}
	}
	, 'pattern': {
		'MakeMaximallyEmpty': {
			'expression': Make.pattern()
			, 'astToolkit.dump': 'ast.pattern()'
			, 'ast.dump': 'pattern()'
		}
		, 'astMinimal': {'expression': ast.pattern(), 'astToolkit.dump': 'ast.pattern()', 'ast.dump': 'pattern()'}
	}
	, 'Pow': {
		'MakeMaximallyEmpty': {'expression': Make.Pow(), 'astToolkit.dump': 'ast.Pow()', 'ast.dump': 'Pow()'}
		, 'astMinimal': {'expression': ast.Pow(), 'astToolkit.dump': 'ast.Pow()', 'ast.dump': 'Pow()'}
	}
	, 'Raise': {
		'MakeMaximallyEmpty': {
			'expression': Make.Raise()
			, 'astToolkit.dump': 'ast.Raise(exc=None, cause=None)'
			, 'ast.dump': 'Raise()'
		}
		, 'MakeMinimal': {
			'expression': Make.Raise(exc=None, cause=None)
			, 'astToolkit.dump': 'ast.Raise(exc=None, cause=None)'
			, 'ast.dump': 'Raise()'
		}
		, 'astMinimal': {
			'expression': ast.Raise()
			, 'astToolkit.dump': 'ast.Raise(exc=None, cause=None)'
			, 'ast.dump': 'Raise()'
		}
	}
	, 'Return': {
		'MakeMaximallyEmpty': {
			'expression': Make.Return()
			, 'astToolkit.dump': 'ast.Return(value=None)'
			, 'ast.dump': 'Return()'
		}
		, 'MakeMinimal': {
			'expression': Make.Return(value=None)
			, 'astToolkit.dump': 'ast.Return(value=None)'
			, 'ast.dump': 'Return()'
		}
		, 'astMinimal': {'expression': ast.Return(), 'astToolkit.dump': 'ast.Return(value=None)', 'ast.dump': 'Return()'}
	}
	, 'RShift': {
		'MakeMaximallyEmpty': {'expression': Make.RShift(), 'astToolkit.dump': 'ast.RShift()', 'ast.dump': 'RShift()'}
		, 'astMinimal': {'expression': ast.RShift(), 'astToolkit.dump': 'ast.RShift()', 'ast.dump': 'RShift()'}
	}
	, 'Set': {
		'MakeMaximallyEmpty': {
			'expression': Make.Set()
			, 'astToolkit.dump': 'ast.Set(elts=[])'
			, 'ast.dump': 'Set(elts=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.Set(listElements=[])
			, 'astToolkit.dump': 'ast.Set(elts=[])'
			, 'ast.dump': 'Set(elts=[])'
		}
		, 'astMinimal': {'expression': ast.Set(), 'astToolkit.dump': 'ast.Set(elts=[])', 'ast.dump': 'Set(elts=[])'}
	}
	, 'SetComp': {
		'MakeMaximallyEmpty': {
			'expression': Make.SetComp(
				element=Make.Name(id='Make_SetComp_element')
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_SetComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_SetComp_generators_iter')
						, ifs=[Make.Name(id='Make_SetComp_generators_ifs')]
					)
				]
			)
			, 'astToolkit.dump': "ast.SetComp(elt=ast.Name(id='Make_SetComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_SetComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_SetComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_SetComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "SetComp(elt=Name(id='Make_SetComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_SetComp_generators_target', ctx=Store()), iter=Name(id='Make_SetComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_SetComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'MakeMinimal': {
			'expression': Make.SetComp(
				element=Make.Name(id='Make_SetComp_element', context=Make.Load())
				, generators=[
					Make.comprehension(
						target=Make.Name(id='Make_SetComp_generators_target', context=Make.Store())
						, iter=Make.Name(id='Make_SetComp_generators_iter', context=Make.Load())
						, ifs=[Make.Name(id='Make_SetComp_generators_ifs', context=Make.Load())]
						, is_async=0
					)
				]
			)
			, 'astToolkit.dump': "ast.SetComp(elt=ast.Name(id='Make_SetComp_element', ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id='Make_SetComp_generators_target', ctx=ast.Store()), iter=ast.Name(id='Make_SetComp_generators_iter', ctx=ast.Load()), ifs=[ast.Name(id='Make_SetComp_generators_ifs', ctx=ast.Load())], is_async=0)])"
			, 'ast.dump': "SetComp(elt=Name(id='Make_SetComp_element', ctx=Load()), generators=[comprehension(target=Name(id='Make_SetComp_generators_target', ctx=Store()), iter=Name(id='Make_SetComp_generators_iter', ctx=Load()), ifs=[Name(id='Make_SetComp_generators_ifs', ctx=Load())], is_async=0)])"
		}
		, 'astMinimal': {
			'expression': ast.SetComp(elt=ast.Name(id='ast_SetComp_element'))
			, 'astToolkit.dump': "ast.SetComp(elt=ast.Name(id='ast_SetComp_element', ctx=ast.Load()), generators=[])"
			, 'ast.dump': "SetComp(elt=Name(id='ast_SetComp_element', ctx=Load()), generators=[])"
		}
	}
	, 'Slice': {
		'MakeMaximallyEmpty': {
			'expression': Make.Slice()
			, 'astToolkit.dump': 'ast.Slice(lower=None, upper=None, step=None)'
			, 'ast.dump': 'Slice()'
		}
		, 'MakeMinimal': {
			'expression': Make.Slice(lower=None, upper=None, step=None)
			, 'astToolkit.dump': 'ast.Slice(lower=None, upper=None, step=None)'
			, 'ast.dump': 'Slice()'
		}
		, 'astMinimal': {
			'expression': ast.Slice()
			, 'astToolkit.dump': 'ast.Slice(lower=None, upper=None, step=None)'
			, 'ast.dump': 'Slice()'
		}
	}
	, 'Starred': {
		'MakeMaximallyEmpty': {
			'expression': Make.Starred(value=Make.Name(id='Make_Starred_value'))
			, 'astToolkit.dump': "ast.Starred(value=ast.Name(id='Make_Starred_value', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Starred(value=Name(id='Make_Starred_value', ctx=Load()), ctx=Load())"
		}
		, 'MakeMinimal': {
			'expression': Make.Starred(value=Make.Name(id='Make_Starred_value', context=Make.Load()), context=Make.Load())
			, 'astToolkit.dump': "ast.Starred(value=ast.Name(id='Make_Starred_value', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Starred(value=Name(id='Make_Starred_value', ctx=Load()), ctx=Load())"
		}
		, 'astMinimal': {
			'expression': ast.Starred(value=ast.Name(id='ast_Starred_value'))
			, 'astToolkit.dump': "ast.Starred(value=ast.Name(id='ast_Starred_value', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Starred(value=Name(id='ast_Starred_value', ctx=Load()), ctx=Load())"
		}
	}
	, 'stmt': {
		'MakeMaximallyEmpty': {'expression': Make.stmt(), 'astToolkit.dump': 'ast.stmt()', 'ast.dump': 'stmt()'}
		, 'astMinimal': {'expression': ast.stmt(), 'astToolkit.dump': 'ast.stmt()', 'ast.dump': 'stmt()'}
	}
	, 'Store': {
		'MakeMaximallyEmpty': {'expression': Make.Store(), 'astToolkit.dump': 'ast.Store()', 'ast.dump': 'Store()'}
		, 'astMinimal': {'expression': ast.Store(), 'astToolkit.dump': 'ast.Store()', 'ast.dump': 'Store()'}
	}
	, 'Sub': {
		'MakeMaximallyEmpty': {'expression': Make.Sub(), 'astToolkit.dump': 'ast.Sub()', 'ast.dump': 'Sub()'}
		, 'astMinimal': {'expression': ast.Sub(), 'astToolkit.dump': 'ast.Sub()', 'ast.dump': 'Sub()'}
	}
	, 'Subscript': {
		'MakeMaximallyEmpty': {
			'expression': Make.Subscript(value=Make.Name(id='Make_Subscript_value'), slice=Make.Name(id='Make_Subscript_slice'))
			, 'astToolkit.dump': "ast.Subscript(value=ast.Name(id='Make_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='Make_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Subscript(value=Name(id='Make_Subscript_value', ctx=Load()), slice=Name(id='Make_Subscript_slice', ctx=Load()), ctx=Load())"
		}
		, 'MakeMinimal': {
			'expression': Make.Subscript(
				value=Make.Name(id='Make_Subscript_value', context=Make.Load())
				, slice=Make.Name(id='Make_Subscript_slice', context=Make.Load())
				, context=Make.Load()
			)
			, 'astToolkit.dump': "ast.Subscript(value=ast.Name(id='Make_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='Make_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Subscript(value=Name(id='Make_Subscript_value', ctx=Load()), slice=Name(id='Make_Subscript_slice', ctx=Load()), ctx=Load())"
		}
		, 'astMinimal': {
			'expression': ast.Subscript(value=ast.Name(id='ast_Subscript_value'), slice=ast.Name(id='ast_Subscript_slice'))
			, 'astToolkit.dump': "ast.Subscript(value=ast.Name(id='ast_Subscript_value', ctx=ast.Load()), slice=ast.Name(id='ast_Subscript_slice', ctx=ast.Load()), ctx=ast.Load())"
			, 'ast.dump': "Subscript(value=Name(id='ast_Subscript_value', ctx=Load()), slice=Name(id='ast_Subscript_slice', ctx=Load()), ctx=Load())"
		}
	}
	, 'Try': {
		'MakeMaximallyEmpty': {
			'expression': Make.Try(body=[Make.Pass()], handlers=[Make.ExceptHandler()])
			, 'astToolkit.dump': 'ast.Try(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])'
			, 'ast.dump': 'Try(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.Try(
				body=[Make.Pass()], handlers=[Make.ExceptHandler(type=None, name=None, body=[])], orElse=[], finalbody=[]
			)
			, 'astToolkit.dump': 'ast.Try(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])'
			, 'ast.dump': 'Try(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])'
		}
		, 'astMinimal': {
			'expression': ast.Try()
			, 'astToolkit.dump': 'ast.Try(body=[], handlers=[], orelse=[], finalbody=[])'
			, 'ast.dump': 'Try(body=[], handlers=[], orelse=[], finalbody=[])'
		}
	}
	, 'TryStar': {
		'MakeMaximallyEmpty': {
			'expression': Make.TryStar(body=[Make.Pass()], handlers=[Make.ExceptHandler()])
			, 'astToolkit.dump': 'ast.TryStar(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])'
			, 'ast.dump': 'TryStar(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])'
		}
		, 'MakeMinimal': {
			'expression': Make.TryStar(
				body=[Make.Pass()], handlers=[Make.ExceptHandler(type=None, name=None, body=[])], orElse=[], finalbody=[]
			)
			, 'astToolkit.dump': 'ast.TryStar(body=[ast.Pass()], handlers=[ast.ExceptHandler(type=None, name=None, body=[])], orelse=[], finalbody=[])'
			, 'ast.dump': 'TryStar(body=[Pass()], handlers=[ExceptHandler(body=[])], orelse=[], finalbody=[])'
		}
		, 'astMinimal': {
			'expression': ast.TryStar()
			, 'astToolkit.dump': 'ast.TryStar(body=[], handlers=[], orelse=[], finalbody=[])'
			, 'ast.dump': 'TryStar(body=[], handlers=[], orelse=[], finalbody=[])'
		}
	}
	, 'Tuple': {
		'MakeMaximallyEmpty': {
			'expression': Make.Tuple()
			, 'astToolkit.dump': 'ast.Tuple(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'Tuple(elts=[], ctx=Load())'
		}
		, 'MakeMinimal': {
			'expression': Make.Tuple(listElements=[], context=Make.Load())
			, 'astToolkit.dump': 'ast.Tuple(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'Tuple(elts=[], ctx=Load())'
		}
		, 'astMinimal': {
			'expression': ast.Tuple()
			, 'astToolkit.dump': 'ast.Tuple(elts=[], ctx=ast.Load())'
			, 'ast.dump': 'Tuple(elts=[], ctx=Load())'
		}
	}
	, 'type_ignore': {
		'MakeMaximallyEmpty': {
			'expression': Make.type_ignore()
			, 'astToolkit.dump': 'ast.type_ignore()'
			, 'ast.dump': 'type_ignore()'
		}
		, 'astMinimal': {
			'expression': ast.type_ignore()
			, 'astToolkit.dump': 'ast.type_ignore()'
			, 'ast.dump': 'type_ignore()'
		}
	}
	, 'type_param': {
		'MakeMaximallyEmpty': {
			'expression': Make.type_param()
			, 'astToolkit.dump': 'ast.type_param()'
			, 'ast.dump': 'type_param()'
		}
		, 'astMinimal': {
			'expression': ast.type_param()
			, 'astToolkit.dump': 'ast.type_param()'
			, 'ast.dump': 'type_param()'
		}
	}
	, "TypeAlias": {
		"class Make, maximally empty parameters": {"expression": Make.TypeAlias(name=Make.Name(id='Make_TypeAlias'), type_params=[], value=Make.Name(id='Make_TypeAlias_value')), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='Make_TypeAlias', ctx=ast.Load()), type_params=[], value=ast.Name(id='Make_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='Make_TypeAlias', ctx=Load()), type_params=[], value=Name(id='Make_TypeAlias_value', ctx=Load()))"}
		, "class Make, minimal parameters": {"expression": Make.TypeAlias(name=Make.Name(id='Make_TypeAlias', context=Make.Store()), type_params=[Make.TypeVar(name='Make_TypeAlias_type_params', bound=None, default_value=None)], value=Make.Name(id='Make_TypeAlias_value', context=Make.Load())), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='Make_TypeAlias', ctx=ast.Store()), type_params=[ast.TypeVar(name='Make_TypeAlias_type_params', bound=None, default_value=None)], value=ast.Name(id='Make_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='Make_TypeAlias', ctx=Store()), type_params=[TypeVar(name='Make_TypeAlias_type_params')], value=Name(id='Make_TypeAlias_value', ctx=Load()))"}
		, "ast module, minimal parameters": {"expression": ast.TypeAlias(name=ast.Name(id='ast_TypeAlias'), value=ast.Name(id='ast_TypeAlias_value')), "astToolkit.dump": "ast.TypeAlias(name=ast.Name(id='ast_TypeAlias', ctx=ast.Load()), type_params=[], value=ast.Name(id='ast_TypeAlias_value', ctx=ast.Load()))", "ast.dump": "TypeAlias(name=Name(id='ast_TypeAlias', ctx=Load()), type_params=[], value=Name(id='ast_TypeAlias_value', ctx=Load()))"}
	}
	, 'TypeIgnore': {
		'MakeMaximallyEmpty': {
			'expression': Make.TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag')
			, 'astToolkit.dump': "ast.TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag')"
			, 'ast.dump': "TypeIgnore(lineno=1, tag='Make_TypeIgnore_tag')"
		}
		, 'astMinimal': {
			'expression': ast.TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag')
			, 'astToolkit.dump': "ast.TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag')"
			, 'ast.dump': "TypeIgnore(lineno=1, tag='ast_TypeIgnore_tag')"
		}
	}
	, "TypeVar": {
		"class Make, maximally empty parameters": {"expression": Make.TypeVar(name='Make_TypeVar'), "astToolkit.dump": "ast.TypeVar(name='Make_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='Make_TypeVar')"}
		, "class Make, minimal parameters": {"expression": Make.TypeVar(name='Make_TypeVar', bound=None, default_value=None), "astToolkit.dump": "ast.TypeVar(name='Make_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='Make_TypeVar')"}
		, "ast module, minimal parameters": {"expression": ast.TypeVar(name='ast_TypeVar'), "astToolkit.dump": "ast.TypeVar(name='ast_TypeVar', bound=None, default_value=None)", "ast.dump": "TypeVar(name='ast_TypeVar')"}
	}
	, "TypeVarTuple": {
		"class Make, maximally empty parameters": {"expression": Make.TypeVarTuple(name='Make_TypeVarTuple'), "astToolkit.dump": "ast.TypeVarTuple(name='Make_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='Make_TypeVarTuple')"}
		, "class Make, minimal parameters": {"expression": Make.TypeVarTuple(name='Make_TypeVarTuple', default_value=None), "astToolkit.dump": "ast.TypeVarTuple(name='Make_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='Make_TypeVarTuple')"}
		, "ast module, minimal parameters": {"expression": ast.TypeVarTuple(name='ast_TypeVarTuple'), "astToolkit.dump": "ast.TypeVarTuple(name='ast_TypeVarTuple', default_value=None)", "ast.dump": "TypeVarTuple(name='ast_TypeVarTuple')"}
	}
	, 'UAdd': {
		'MakeMaximallyEmpty': {'expression': Make.UAdd(), 'astToolkit.dump': 'ast.UAdd()', 'ast.dump': 'UAdd()'}
		, 'astMinimal': {'expression': ast.UAdd(), 'astToolkit.dump': 'ast.UAdd()', 'ast.dump': 'UAdd()'}
	}
	, 'unaryop': {
		'MakeMaximallyEmpty': {
			'expression': Make.unaryop()
			, 'astToolkit.dump': 'ast.unaryop()'
			, 'ast.dump': 'unaryop()'
		}
		, 'astMinimal': {'expression': ast.unaryop(), 'astToolkit.dump': 'ast.unaryop()', 'ast.dump': 'unaryop()'}
	}
	, 'UnaryOp': {
		'MakeMaximallyEmpty': {
			'expression': Make.UnaryOp(op=Make.UAdd(), operand=Make.Name(id='Make_UnaryOp_operand'))
			, 'astToolkit.dump': "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='Make_UnaryOp_operand', ctx=ast.Load()))"
			, 'ast.dump': "UnaryOp(op=UAdd(), operand=Name(id='Make_UnaryOp_operand', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.UnaryOp(op=Make.UAdd(), operand=Make.Name(id='Make_UnaryOp_operand', context=Make.Load()))
			, 'astToolkit.dump': "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='Make_UnaryOp_operand', ctx=ast.Load()))"
			, 'ast.dump': "UnaryOp(op=UAdd(), operand=Name(id='Make_UnaryOp_operand', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='ast_UnaryOp_operand'))
			, 'astToolkit.dump': "ast.UnaryOp(op=ast.UAdd(), operand=ast.Name(id='ast_UnaryOp_operand', ctx=ast.Load()))"
			, 'ast.dump': "UnaryOp(op=UAdd(), operand=Name(id='ast_UnaryOp_operand', ctx=Load()))"
		}
	}
	, 'USub': {
		'MakeMaximallyEmpty': {'expression': Make.USub(), 'astToolkit.dump': 'ast.USub()', 'ast.dump': 'USub()'}
		, 'astMinimal': {'expression': ast.USub(), 'astToolkit.dump': 'ast.USub()', 'ast.dump': 'USub()'}
	}
	, 'While': {
		'MakeMaximallyEmpty': {
			'expression': Make.While(test=Make.Name(id='Make_While_test'), body=[Make.Pass()])
			, 'astToolkit.dump': "ast.While(test=ast.Name(id='Make_While_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])"
			, 'ast.dump': "While(test=Name(id='Make_While_test', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'MakeMinimal': {
			'expression': Make.While(test=Make.Name(id='Make_While_test', context=Make.Load()), body=[Make.Pass()], orElse=[])
			, 'astToolkit.dump': "ast.While(test=ast.Name(id='Make_While_test', ctx=ast.Load()), body=[ast.Pass()], orelse=[])"
			, 'ast.dump': "While(test=Name(id='Make_While_test', ctx=Load()), body=[Pass()], orelse=[])"
		}
		, 'astMinimal': {
			'expression': ast.While(test=ast.Name(id='ast_While_test'))
			, 'astToolkit.dump': "ast.While(test=ast.Name(id='ast_While_test', ctx=ast.Load()), body=[], orelse=[])"
			, 'ast.dump': "While(test=Name(id='ast_While_test', ctx=Load()), body=[], orelse=[])"
		}
	}
	, 'With': {
		'MakeMaximallyEmpty': {
			'expression': Make.With(items=[Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr'))], body=[Make.Pass()])
			, 'astToolkit.dump': "ast.With(items=[ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)"
			, 'ast.dump': "With(items=[withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))], body=[Pass()])"
		}
		, 'MakeMinimal': {
			'expression': Make.With(
				items=[Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr', context=Make.Load()), optional_vars=None)]
				, body=[Make.Pass()]
			)
			, 'astToolkit.dump': "ast.With(items=[ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)], body=[ast.Pass()], type_comment=None)"
			, 'ast.dump': "With(items=[withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))], body=[Pass()])"
		}
		, 'astMinimal': {
			'expression': ast.With()
			, 'astToolkit.dump': 'ast.With(items=[], body=[], type_comment=None)'
			, 'ast.dump': 'With(items=[], body=[])'
		}
	}
	, 'withitem': {
		'MakeMaximallyEmpty': {
			'expression': Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr'))
			, 'astToolkit.dump': "ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)"
			, 'ast.dump': "withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.withitem(context_expr=Make.Name(id='Make_withitem_context_expr', context=Make.Load()), optional_vars=None)
			, 'astToolkit.dump': "ast.withitem(context_expr=ast.Name(id='Make_withitem_context_expr', ctx=ast.Load()), optional_vars=None)"
			, 'ast.dump': "withitem(context_expr=Name(id='Make_withitem_context_expr', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.withitem(context_expr=ast.Name(id='ast_withitem_context_expr'))
			, 'astToolkit.dump': "ast.withitem(context_expr=ast.Name(id='ast_withitem_context_expr', ctx=ast.Load()), optional_vars=None)"
			, 'ast.dump': "withitem(context_expr=Name(id='ast_withitem_context_expr', ctx=Load()))"
		}
	}
	, 'Yield': {
		'MakeMaximallyEmpty': {
			'expression': Make.Yield()
			, 'astToolkit.dump': 'ast.Yield(value=None)'
			, 'ast.dump': 'Yield()'
		}
		, 'MakeMinimal': {
			'expression': Make.Yield(value=None)
			, 'astToolkit.dump': 'ast.Yield(value=None)'
			, 'ast.dump': 'Yield()'
		}
		, 'astMinimal': {'expression': ast.Yield(), 'astToolkit.dump': 'ast.Yield(value=None)', 'ast.dump': 'Yield()'}
	}
	, 'YieldFrom': {
		'MakeMaximallyEmpty': {
			'expression': Make.YieldFrom(value=Make.Name(id='Make_YieldFrom_value'))
			, 'astToolkit.dump': "ast.YieldFrom(value=ast.Name(id='Make_YieldFrom_value', ctx=ast.Load()))"
			, 'ast.dump': "YieldFrom(value=Name(id='Make_YieldFrom_value', ctx=Load()))"
		}
		, 'MakeMinimal': {
			'expression': Make.YieldFrom(value=Make.Name(id='Make_YieldFrom_value', context=Make.Load()))
			, 'astToolkit.dump': "ast.YieldFrom(value=ast.Name(id='Make_YieldFrom_value', ctx=ast.Load()))"
			, 'ast.dump': "YieldFrom(value=Name(id='Make_YieldFrom_value', ctx=Load()))"
		}
		, 'astMinimal': {
			'expression': ast.YieldFrom(value=ast.Name(id='ast_YieldFrom_value'))
			, 'astToolkit.dump': "ast.YieldFrom(value=ast.Name(id='ast_YieldFrom_value', ctx=ast.Load()))"
			, 'ast.dump': "YieldFrom(value=Name(id='ast_YieldFrom_value', ctx=Load()))"
		}
	}
}

identifiersClassOfEachSample: tuple[str, ...] = tuple(chain.from_iterable(map(repeat, allSubclasses, map(len, allSubclasses.values()), strict=True)))
identifiersSample: tuple[str, ...] = tuple(map('{}_{}'.format, identifiersClassOfEachSample, chain.from_iterable(allSubclasses.values()), strict=True))
nodesSample: tuple[ast.AST, ...] = tuple(map(itemgetter('expression'), chain.from_iterable(map(dict[str, dict[str, Any]].values, allSubclasses.values()))))
fieldsOfEachSample: tuple[tuple[str, ...], ...] = tuple(map(attrgetter('_fields'), map(getattr, repeat(ast), identifiersClassOfEachSample)))

lookupNode: dict[str, tuple[str, ast.AST]] = dict(zip(identifiersSample, zip(identifiersClassOfEachSample, nodesSample, strict=True), strict=True))
"""Each sample, keyed by `'<class>_<construction>'`, as `(identifierClass, node)`."""

identifiersClassMatchingEachSample: tuple[tuple[str, ...], ...] = tuple(map(tuple[str, ...], map(partial(filter, allSubclasses.__contains__)
	, map(partial(map, attrgetter('__name__')), map(attrgetter('__mro__'), map(type, nodesSample))))))  # pyright: ignore[reportUnknownArgumentType]

lookupNodeClassMatching: dict[str, tuple[str, ast.AST]] = dict(zip(
	map('{}-{}'.format, chain.from_iterable(map(repeat, identifiersSample, map(len, identifiersClassMatchingEachSample), strict=True))
		, chain.from_iterable(identifiersClassMatchingEachSample), strict=True)
	, zip(
		chain.from_iterable(identifiersClassMatchingEachSample)
		, chain.from_iterable(map(repeat, nodesSample, map(len, identifiersClassMatchingEachSample), strict=True))
		, strict=True)
	, strict=True))
"""Each sample with its own class and each superclass of it in `allSubclasses`, keyed by `'<class>_<construction>-<matchingClass>'`,
as `(identifierClassMatching, node)`."""

lookupNodeField: dict[str, tuple[str, ast.AST, str]] = dict(zip(
	map('{}-{}'.format, chain.from_iterable(map(repeat, identifiersSample, map(len, fieldsOfEachSample), strict=True)), chain.from_iterable(fieldsOfEachSample)
		, strict=True)
	, zip(
		chain.from_iterable(map(repeat, identifiersClassOfEachSample, map(len, fieldsOfEachSample), strict=True))
		, chain.from_iterable(map(repeat, nodesSample, map(len, fieldsOfEachSample), strict=True))
		, chain.from_iterable(fieldsOfEachSample)
		, strict=True)
	, strict=True))
"""Each sample with each field that its class declares in `_fields`, keyed by `'<class>_<construction>-<field>'`, as
`(identifierClass, node, field)`."""
