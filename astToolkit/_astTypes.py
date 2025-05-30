"""This file is generated automatically, so changes to this file will be lost."""
from types import EllipsisType
from typing import Any, TypeAlias as typing_TypeAlias, TypeVar as typing_TypeVar, TypedDict
import ast
import sys
intORstr: typing_TypeAlias = Any
intORstrORtype_params: typing_TypeAlias = Any
intORtype_params: typing_TypeAlias = Any
ConstantValueType: typing_TypeAlias = bool | bytes | complex | EllipsisType | float | int | None | range | str
木 = typing_TypeVar('木', bound=ast.AST, covariant=True)
个 = typing_TypeVar('个', covariant=True)
个return = typing_TypeVar('个return', covariant=True)

class _attributes(TypedDict, total=False):
    lineno: int
    col_offset: int

class ast_attributes(_attributes, total=False):
    end_lineno: int | None
    end_col_offset: int | None

class ast_attributes_int(_attributes, total=False):
    end_lineno: int
    end_col_offset: int

class ast_attributes_type_comment(ast_attributes, total=False):
    type_comment: str | None
hasDOTannotation_expr: typing_TypeAlias = ast.AnnAssign
hasDOTannotation_exprOrNone: typing_TypeAlias = ast.arg
hasDOTannotation: typing_TypeAlias = hasDOTannotation_expr | hasDOTannotation_exprOrNone
hasDOTarg_str: typing_TypeAlias = ast.arg
hasDOTarg_strOrNone: typing_TypeAlias = ast.keyword
hasDOTarg: typing_TypeAlias = hasDOTarg_str | hasDOTarg_strOrNone
hasDOTargs_arguments: typing_TypeAlias = ast.AsyncFunctionDef | ast.FunctionDef | ast.Lambda
hasDOTargs_list_arg: typing_TypeAlias = ast.arguments
hasDOTargs_list_expr: typing_TypeAlias = ast.Call
hasDOTargs: typing_TypeAlias = hasDOTargs_arguments | hasDOTargs_list_arg | hasDOTargs_list_expr
hasDOTargtypes: typing_TypeAlias = ast.FunctionType
hasDOTasname: typing_TypeAlias = ast.alias
hasDOTattr: typing_TypeAlias = ast.Attribute
hasDOTbases: typing_TypeAlias = ast.ClassDef
hasDOTbody_expr: typing_TypeAlias = ast.Expression | ast.IfExp | ast.Lambda
hasDOTbody_list_stmt: typing_TypeAlias = ast.AsyncFor | ast.AsyncFunctionDef | ast.AsyncWith | ast.ClassDef | ast.ExceptHandler | ast.For | ast.FunctionDef | ast.If | ast.Interactive | ast.match_case | ast.Module | ast.Try | ast.TryStar | ast.While | ast.With
hasDOTbody: typing_TypeAlias = hasDOTbody_expr | hasDOTbody_list_stmt
hasDOTbound: typing_TypeAlias = ast.TypeVar
hasDOTcases: typing_TypeAlias = ast.Match
hasDOTcause: typing_TypeAlias = ast.Raise
hasDOTcls: typing_TypeAlias = ast.MatchClass
hasDOTcomparators: typing_TypeAlias = ast.Compare
hasDOTcontext_expr: typing_TypeAlias = ast.withitem
hasDOTconversion: typing_TypeAlias = ast.FormattedValue
hasDOTctx: typing_TypeAlias = ast.Attribute | ast.List | ast.Name | ast.Starred | ast.Subscript | ast.Tuple
hasDOTdecorator_list: typing_TypeAlias = ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef
match sys.version_info:
    case version if version >= (3, 13):
        hasDOTdefault_value: typing_TypeAlias = ast.ParamSpec | ast.TypeVar | ast.TypeVarTuple
hasDOTdefaults: typing_TypeAlias = ast.arguments
hasDOTelt: typing_TypeAlias = ast.GeneratorExp | ast.ListComp | ast.SetComp
hasDOTelts: typing_TypeAlias = ast.List | ast.Set | ast.Tuple
hasDOTexc: typing_TypeAlias = ast.Raise
hasDOTfinalbody: typing_TypeAlias = ast.Try | ast.TryStar
hasDOTformat_spec: typing_TypeAlias = ast.FormattedValue
hasDOTfunc: typing_TypeAlias = ast.Call
hasDOTgenerators: typing_TypeAlias = ast.DictComp | ast.GeneratorExp | ast.ListComp | ast.SetComp
hasDOTguard: typing_TypeAlias = ast.match_case
hasDOThandlers: typing_TypeAlias = ast.Try | ast.TryStar
hasDOTid: typing_TypeAlias = ast.Name
hasDOTifs: typing_TypeAlias = ast.comprehension
hasDOTis_async: typing_TypeAlias = ast.comprehension
hasDOTitems: typing_TypeAlias = ast.AsyncWith | ast.With
hasDOTiter: typing_TypeAlias = ast.AsyncFor | ast.comprehension | ast.For
hasDOTkey: typing_TypeAlias = ast.DictComp
hasDOTkeys_list_expr: typing_TypeAlias = ast.MatchMapping
hasDOTkeys_list_exprOrNone: typing_TypeAlias = ast.Dict
hasDOTkeys: typing_TypeAlias = hasDOTkeys_list_expr | hasDOTkeys_list_exprOrNone
hasDOTkeywords: typing_TypeAlias = ast.Call | ast.ClassDef
hasDOTkind: typing_TypeAlias = ast.Constant
hasDOTkw_defaults: typing_TypeAlias = ast.arguments
hasDOTkwarg: typing_TypeAlias = ast.arguments
hasDOTkwd_attrs: typing_TypeAlias = ast.MatchClass
hasDOTkwd_patterns: typing_TypeAlias = ast.MatchClass
hasDOTkwonlyargs: typing_TypeAlias = ast.arguments
hasDOTleft: typing_TypeAlias = ast.BinOp | ast.Compare
hasDOTlevel: typing_TypeAlias = ast.ImportFrom
hasDOTlineno: typing_TypeAlias = ast.TypeIgnore
hasDOTlower: typing_TypeAlias = ast.Slice
hasDOTmodule: typing_TypeAlias = ast.ImportFrom
hasDOTmsg: typing_TypeAlias = ast.Assert
hasDOTname_Name: typing_TypeAlias = ast.TypeAlias
hasDOTname_str: typing_TypeAlias = ast.alias | ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef | ast.ParamSpec | ast.TypeVar | ast.TypeVarTuple
hasDOTname_strOrNone: typing_TypeAlias = ast.ExceptHandler | ast.MatchAs | ast.MatchStar
hasDOTname: typing_TypeAlias = hasDOTname_Name | hasDOTname_str | hasDOTname_strOrNone
hasDOTnames_list_alias: typing_TypeAlias = ast.Import | ast.ImportFrom
hasDOTnames_list_str: typing_TypeAlias = ast.Global | ast.Nonlocal
hasDOTnames: typing_TypeAlias = hasDOTnames_list_alias | hasDOTnames_list_str
hasDOTop_boolop: typing_TypeAlias = ast.BoolOp
hasDOTop_operator: typing_TypeAlias = ast.AugAssign | ast.BinOp
hasDOTop_unaryop: typing_TypeAlias = ast.UnaryOp
hasDOTop: typing_TypeAlias = hasDOTop_boolop | hasDOTop_operator | hasDOTop_unaryop
hasDOToperand: typing_TypeAlias = ast.UnaryOp
hasDOTops: typing_TypeAlias = ast.Compare
hasDOToptional_vars: typing_TypeAlias = ast.withitem
hasDOTorelse_expr: typing_TypeAlias = ast.IfExp
hasDOTorelse_list_stmt: typing_TypeAlias = ast.AsyncFor | ast.For | ast.If | ast.Try | ast.TryStar | ast.While
hasDOTorelse: typing_TypeAlias = hasDOTorelse_expr | hasDOTorelse_list_stmt
hasDOTpattern_pattern: typing_TypeAlias = ast.match_case
hasDOTpattern_patternOrNone: typing_TypeAlias = ast.MatchAs
hasDOTpattern: typing_TypeAlias = hasDOTpattern_pattern | hasDOTpattern_patternOrNone
hasDOTpatterns: typing_TypeAlias = ast.MatchClass | ast.MatchMapping | ast.MatchOr | ast.MatchSequence
hasDOTposonlyargs: typing_TypeAlias = ast.arguments
hasDOTrest: typing_TypeAlias = ast.MatchMapping
hasDOTreturns_expr: typing_TypeAlias = ast.FunctionType
hasDOTreturns_exprOrNone: typing_TypeAlias = ast.AsyncFunctionDef | ast.FunctionDef
hasDOTreturns: typing_TypeAlias = hasDOTreturns_expr | hasDOTreturns_exprOrNone
hasDOTright: typing_TypeAlias = ast.BinOp
hasDOTsimple: typing_TypeAlias = ast.AnnAssign
hasDOTslice: typing_TypeAlias = ast.Subscript
hasDOTstep: typing_TypeAlias = ast.Slice
hasDOTsubject: typing_TypeAlias = ast.Match
hasDOTtag: typing_TypeAlias = ast.TypeIgnore
hasDOTtarget_expr: typing_TypeAlias = ast.AsyncFor | ast.comprehension | ast.For
hasDOTtarget_Name: typing_TypeAlias = ast.NamedExpr
hasDOTtarget_NameOrAttributeOrSubscript: typing_TypeAlias = ast.AnnAssign | ast.AugAssign
hasDOTtarget: typing_TypeAlias = hasDOTtarget_expr | hasDOTtarget_Name | hasDOTtarget_NameOrAttributeOrSubscript
hasDOTtargets: typing_TypeAlias = ast.Assign | ast.Delete
hasDOTtest: typing_TypeAlias = ast.Assert | ast.If | ast.IfExp | ast.While
hasDOTtype: typing_TypeAlias = ast.ExceptHandler
hasDOTtype_comment: typing_TypeAlias = ast.arg | ast.Assign | ast.AsyncFor | ast.AsyncFunctionDef | ast.AsyncWith | ast.For | ast.FunctionDef | ast.With
hasDOTtype_ignores: typing_TypeAlias = ast.Module
hasDOTtype_params: typing_TypeAlias = ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef | ast.TypeAlias
hasDOTupper: typing_TypeAlias = ast.Slice
hasDOTvalue_boolOrNone: typing_TypeAlias = ast.MatchSingleton
hasDOTvalue_ConstantValueType: typing_TypeAlias = ast.Constant
hasDOTvalue_expr: typing_TypeAlias = ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
hasDOTvalue_exprOrNone: typing_TypeAlias = ast.AnnAssign | ast.Return | ast.Yield
hasDOTvalue: typing_TypeAlias = hasDOTvalue_boolOrNone | hasDOTvalue_ConstantValueType | hasDOTvalue_expr | hasDOTvalue_exprOrNone
hasDOTvalues: typing_TypeAlias = ast.BoolOp | ast.Dict | ast.JoinedStr
hasDOTvararg: typing_TypeAlias = ast.arguments