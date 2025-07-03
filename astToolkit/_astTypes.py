"""Automatically generated file, so changes may be overwritten."""
from types import EllipsisType
from typing import TypedDict, TypeVar as typing_TypeVar
import ast
import sys

type ConstantValueType = bool | bytes | complex | EllipsisType | float | int | None | range | str
type identifierDotAttribute = str
个 = typing_TypeVar('个', covariant=True)
归个 = typing_TypeVar('归个', covariant=True)
文件 = typing_TypeVar('文件', covariant=True)
文义 = typing_TypeVar('文义', covariant=True)
木 = typing_TypeVar('木', bound=ast.AST, covariant=True)
布尔符 = typing_TypeVar('布尔符', bound=ast.boolop, covariant=True)
比符 = typing_TypeVar('比符', bound=ast.cmpop, covariant=True)
常 = typing_TypeVar('常', bound=ast.Constant, covariant=True)
拦 = typing_TypeVar('拦', bound=ast.excepthandler, covariant=True)
工位 = typing_TypeVar('工位', bound=ast.expr_context, covariant=True)
工 = typing_TypeVar('工', bound=ast.expr, covariant=True)
本 = typing_TypeVar('本', bound=ast.mod, covariant=True)
二符 = typing_TypeVar('二符', bound=ast.operator, covariant=True)
俪 = typing_TypeVar('俪', bound=ast.pattern, covariant=True)
口 = typing_TypeVar('口', bound=ast.stmt, covariant=True)
忽 = typing_TypeVar('忽', bound=ast.type_ignore, covariant=True)
形 = typing_TypeVar('形', bound=ast.type_param, covariant=True)
一符 = typing_TypeVar('一符', bound=ast.unaryop, covariant=True)

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
type hasDOTannotation_expr = ast.AnnAssign
type hasDOTannotation_exprOrNone = ast.arg
type hasDOTannotation = hasDOTannotation_expr | hasDOTannotation_exprOrNone
type hasDOTarg_str = ast.arg
type hasDOTarg_strOrNone = ast.keyword
type hasDOTarg = hasDOTarg_str | hasDOTarg_strOrNone
type hasDOTargs_arguments = ast.AsyncFunctionDef | ast.FunctionDef | ast.Lambda
type hasDOTargs_list_arg = ast.arguments
type hasDOTargs_list_expr = ast.Call
type hasDOTargs = hasDOTargs_arguments | hasDOTargs_list_arg | hasDOTargs_list_expr
type hasDOTargtypes = ast.FunctionType
type hasDOTasname = ast.alias
type hasDOTattr = ast.Attribute
type hasDOTbases = ast.ClassDef
type hasDOTbody_expr = ast.Expression | ast.IfExp | ast.Lambda
type hasDOTbody_list_stmt = ast.AsyncFor | ast.AsyncFunctionDef | ast.AsyncWith | ast.ClassDef | ast.ExceptHandler | ast.For | ast.FunctionDef | ast.If | ast.Interactive | ast.match_case | ast.Module | ast.Try | ast.TryStar | ast.While | ast.With
type hasDOTbody = hasDOTbody_expr | hasDOTbody_list_stmt
type hasDOTbound = ast.TypeVar
type hasDOTcases = ast.Match
type hasDOTcause = ast.Raise
type hasDOTcls = ast.MatchClass
type hasDOTcomparators = ast.Compare
type hasDOTcontext_expr = ast.withitem
type hasDOTconversion = ast.FormattedValue
type hasDOTctx = ast.Attribute | ast.List | ast.Name | ast.Starred | ast.Subscript | ast.Tuple
type hasDOTdecorator_list = ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef
if sys.version_info >= (3, 13):
    type hasDOTdefault_value = ast.ParamSpec | ast.TypeVar | ast.TypeVarTuple
type hasDOTdefaults = ast.arguments
type hasDOTelt = ast.GeneratorExp | ast.ListComp | ast.SetComp
type hasDOTelts = ast.List | ast.Set | ast.Tuple
type hasDOTexc = ast.Raise
type hasDOTfinalbody = ast.Try | ast.TryStar
type hasDOTformat_spec = ast.FormattedValue
type hasDOTfunc = ast.Call
type hasDOTgenerators = ast.DictComp | ast.GeneratorExp | ast.ListComp | ast.SetComp
type hasDOTguard = ast.match_case
type hasDOThandlers = ast.Try | ast.TryStar
type hasDOTid = ast.Name
type hasDOTifs = ast.comprehension
type hasDOTis_async = ast.comprehension
type hasDOTitems = ast.AsyncWith | ast.With
type hasDOTiter = ast.AsyncFor | ast.comprehension | ast.For
type hasDOTkey = ast.DictComp
type hasDOTkeys_list_expr = ast.MatchMapping
type hasDOTkeys_list_exprOrNone = ast.Dict
type hasDOTkeys = hasDOTkeys_list_expr | hasDOTkeys_list_exprOrNone
type hasDOTkeywords = ast.Call | ast.ClassDef
type hasDOTkind = ast.Constant
type hasDOTkw_defaults = ast.arguments
type hasDOTkwarg = ast.arguments
type hasDOTkwd_attrs = ast.MatchClass
type hasDOTkwd_patterns = ast.MatchClass
type hasDOTkwonlyargs = ast.arguments
type hasDOTleft = ast.BinOp | ast.Compare
type hasDOTlevel = ast.ImportFrom
type hasDOTlineno = ast.TypeIgnore
type hasDOTlower = ast.Slice
type hasDOTmodule = ast.ImportFrom
type hasDOTmsg = ast.Assert
type hasDOTname_Name = ast.TypeAlias
type hasDOTname_str = ast.alias | ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef | ast.ParamSpec | ast.TypeVar | ast.TypeVarTuple
type hasDOTname_strOrNone = ast.ExceptHandler | ast.MatchAs | ast.MatchStar
type hasDOTname = hasDOTname_Name | hasDOTname_str | hasDOTname_strOrNone
type hasDOTnames_list_alias = ast.Import | ast.ImportFrom
type hasDOTnames_list_str = ast.Global | ast.Nonlocal
type hasDOTnames = hasDOTnames_list_alias | hasDOTnames_list_str
type hasDOTop_boolop = ast.BoolOp
type hasDOTop_operator = ast.AugAssign | ast.BinOp
type hasDOTop_unaryop = ast.UnaryOp
type hasDOTop = hasDOTop_boolop | hasDOTop_operator | hasDOTop_unaryop
type hasDOToperand = ast.UnaryOp
type hasDOTops = ast.Compare
type hasDOToptional_vars = ast.withitem
type hasDOTorelse_expr = ast.IfExp
type hasDOTorelse_list_stmt = ast.AsyncFor | ast.For | ast.If | ast.Try | ast.TryStar | ast.While
type hasDOTorelse = hasDOTorelse_expr | hasDOTorelse_list_stmt
type hasDOTpattern_pattern = ast.match_case
type hasDOTpattern_patternOrNone = ast.MatchAs
type hasDOTpattern = hasDOTpattern_pattern | hasDOTpattern_patternOrNone
type hasDOTpatterns = ast.MatchClass | ast.MatchMapping | ast.MatchOr | ast.MatchSequence
type hasDOTposonlyargs = ast.arguments
type hasDOTrest = ast.MatchMapping
type hasDOTreturns_expr = ast.FunctionType
type hasDOTreturns_exprOrNone = ast.AsyncFunctionDef | ast.FunctionDef
type hasDOTreturns = hasDOTreturns_expr | hasDOTreturns_exprOrNone
type hasDOTright = ast.BinOp
type hasDOTsimple = ast.AnnAssign
type hasDOTslice = ast.Subscript
type hasDOTstep = ast.Slice
type hasDOTsubject = ast.Match
type hasDOTtag = ast.TypeIgnore
type hasDOTtarget_expr = ast.AsyncFor | ast.comprehension | ast.For
type hasDOTtarget_Name = ast.NamedExpr
type hasDOTtarget_NameOrAttributeOrSubscript = ast.AnnAssign | ast.AugAssign
type hasDOTtarget = hasDOTtarget_expr | hasDOTtarget_Name | hasDOTtarget_NameOrAttributeOrSubscript
type hasDOTtargets = ast.Assign | ast.Delete
type hasDOTtest = ast.Assert | ast.If | ast.IfExp | ast.While
type hasDOTtype = ast.ExceptHandler
type hasDOTtype_comment = ast.arg | ast.Assign | ast.AsyncFor | ast.AsyncFunctionDef | ast.AsyncWith | ast.For | ast.FunctionDef | ast.With
type hasDOTtype_ignores = ast.Module
type hasDOTtype_params = ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef | ast.TypeAlias
type hasDOTupper = ast.Slice
type hasDOTvalue_boolOrNone = ast.MatchSingleton
type hasDOTvalue_ConstantValueType = ast.Constant
type hasDOTvalue_expr = ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
type hasDOTvalue_exprOrNone = ast.AnnAssign | ast.Return | ast.Yield
type hasDOTvalue = hasDOTvalue_boolOrNone | hasDOTvalue_ConstantValueType | hasDOTvalue_expr | hasDOTvalue_exprOrNone
type hasDOTvalues = ast.BoolOp | ast.Dict | ast.JoinedStr
type hasDOTvararg = ast.arguments