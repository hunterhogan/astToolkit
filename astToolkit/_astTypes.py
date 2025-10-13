"""Automatically generated file, so changes may be overwritten."""
from types import EllipsisType
from typing import TypedDict, TypeVar as typing_TypeVar
import ast
import sys

type ConstantValueType = bool | bytes | complex | EllipsisType | float | int | None | range | str
type astASTattributes = ast.AST | ConstantValueType | list[ast.AST] | list[ast.AST | None] | list[str]
type identifierDotAttribute = str
个 = typing_TypeVar('个', covariant=True)
"Generic `TypeVar` (Type ***Var***iable).\n\n(AI generated docstring.)\n\nThe ideograph '个' (gè) is a generic measure word. Its decimal unicode is 20010.\n"
归个 = typing_TypeVar('归个', covariant=True)
"Generic `return` `TypeVar` (Type ***Var***iable).\n\n(AI generated docstring.)\n\nThe ideograph '归' (guī) means 'return'. Its decimal unicode is 24402. The ideograph '个' (gè) is a generic measure word.\nIts decimal unicode is 20010. `归个` is often paired with `个` when the `return` type may differ from the parameter type.\n"
文件 = typing_TypeVar('文件', covariant=True)
"Dictionary key `TypeVar` (Type ***Var***iable).\n\n(AI generated docstring.)\n\nThe ideograph '文件' (wénjiàn) means 'dictionary key'. Its decimal unicode is 25991 and 20214.\n"
文义 = typing_TypeVar('文义', covariant=True)
"Dictionary value `TypeVar` (Type ***Var***iable).\n\n(AI generated docstring.)\n\nThe ideograph '文义' (wényì) means 'dictionary value'. Its decimal unicode is 25991 and 20041. `文义` is often paired with\n`文件` for dictionary type parameters.\n"
木 = typing_TypeVar('木', bound=ast.AST, covariant=True)
"`AST` `TypeVar` (Type ***Var***iable) bound to `ast.AST`.\n\n(AI generated docstring.)\n\nThe ideograph '木' (mù) means 'tree', short for abstract syntax tree. Its decimal unicode is 26408. This `covariant`\n`TypeVar` is bound to `ast.AST`, the base class for all AST nodes, and its subclasses, `ast.alias`, `ast.arg`,\n`ast.arguments`, `ast.boolop`, `ast.cmpop`, `ast.comprehension`, `ast.excepthandler`, `ast.expr`, `ast.expr_context`,\n`ast.keyword`, `ast.match_case`, `ast.mod`, `ast.operator`, `ast.pattern`, `ast.slice`, `ast.stmt`, `ast.type_ignore`,\n`ast.type_param`, `ast.unaryop`, and `ast.withitem`.\n"
本 = typing_TypeVar('本', bound=ast.mod, covariant=True)
"`mod` `TypeVar` (Type ***Var***iable) bound to `ast.mod`.\n\n(AI generated docstring.)\n\nThe ideograph '本' (běn) means 'module'. Its decimal unicode is 26412. This `covariant` `TypeVar` is bound to `ast.mod`,\nthe base class for module-level AST nodes, and its subclasses, `ast.Expression`, `ast.FunctionType`, `ast.Interactive`,\n`ast.Module`, and `ast.Suite`.\n"
口 = typing_TypeVar('口', bound=ast.stmt, covariant=True)
"`stmt` `TypeVar` (Type ***Var***iable) bound to `ast.stmt`.\n\n(AI generated docstring.)\n\nThe ideograph '口' (kǒu) means 'statement'. Its decimal unicode is 21475. This `covariant` `TypeVar` is bound to\n`ast.stmt` and its subclasses, `ast.AnnAssign`, `ast.Assert`, `ast.Assign`, `ast.AsyncFor`, `ast.AsyncFunctionDef`,\n`ast.AsyncWith`, `ast.AugAssign`, `ast.Break`, `ast.ClassDef`, `ast.Continue`, `ast.Delete`, `ast.Expr`, `ast.For`,\n`ast.FunctionDef`, `ast.Global`, `ast.If`, `ast.Import`, `ast.ImportFrom`, `ast.Match`, `ast.Nonlocal`, `ast.Pass`,\n`ast.Raise`, `ast.Return`, `ast.Try`, `ast.TryStar`, `ast.TypeAlias`, `ast.While`, and `ast.With`.\n"
工 = typing_TypeVar('工', bound=ast.expr, covariant=True)
"`expr` `TypeVar` (Type ***Var***iable) bound to `ast.expr`.\n\n(AI generated docstring.)\n\nThe ideograph '工' (gōng) means 'expression'. Its decimal unicode is 24037. This `covariant` `TypeVar` is bound to\n`ast.expr`, the base class for all expression nodes, and its subclasses, `ast.Attribute`, `ast.Await`, `ast.BinOp`,\n`ast.BoolOp`, `ast.Call`, `ast.Compare`, `ast.Constant`, `ast.Dict`, `ast.DictComp`, `ast.FormattedValue`,\n`ast.GeneratorExp`, `ast.IfExp`, `ast.JoinedStr`, `ast.Lambda`, `ast.List`, `ast.ListComp`, `ast.Name`, `ast.NamedExpr`,\n`ast.Set`, `ast.SetComp`, `ast.Slice`, `ast.Starred`, `ast.Subscript`, `ast.Tuple`, `ast.UnaryOp`, `ast.Yield`, and\n`ast.YieldFrom`.\n"
工位 = typing_TypeVar('工位', bound=ast.expr_context, covariant=True)
"`expr_context` `TypeVar` (Type ***Var***iable) bound to `ast.expr_context`.\n\n(AI generated docstring.)\n\nThe ideograph '工位' (gōngwèi) means 'expression context'. Its decimal unicode is 24037 and 20301. This `covariant`\n`TypeVar` is bound to `ast.expr_context`, representing whether an expression appears in loading, storing, or deleting\ncontext, and its subclasses, `ast.AugLoad`, `ast.AugStore`, `ast.Del`, `ast.Load`, `ast.Param`, and `ast.Store`.\n"
一符 = typing_TypeVar('一符', bound=ast.unaryop, covariant=True)
"`unaryop` `TypeVar` (Type ***Var***iable) bound to `ast.unaryop`.\n\n(AI generated docstring.)\n\nThe ideograph '一符' (yīfú) means 'unary operator'. Its decimal unicode is 19968 and 31526. This `covariant` `TypeVar` is\nbound to `ast.unaryop`, representing unary operators like negation and bitwise NOT, and its subclasses, `ast.Invert`,\n`ast.Not`, `ast.UAdd`, and `ast.USub`.\n"
二符 = typing_TypeVar('二符', bound=ast.operator, covariant=True)
"`operator` `TypeVar` (Type ***Var***iable) bound to `ast.operator`.\n\n(AI generated docstring.)\n\nThe ideograph '二符' (èrfú) means 'binary operator'. Its decimal unicode is 20108 and 31526. This `covariant` `TypeVar` is\nbound to `ast.operator`, representing binary operators like addition and multiplication, and its subclasses, `ast.Add`,\n`ast.BitAnd`, `ast.BitOr`, `ast.BitXor`, `ast.Div`, `ast.FloorDiv`, `ast.LShift`, `ast.MatMult`, `ast.Mod`, `ast.Mult`,\n`ast.Pow`, `ast.RShift`, and `ast.Sub`.\n"
比符 = typing_TypeVar('比符', bound=ast.cmpop, covariant=True)
"`cmpop` `TypeVar` (Type ***Var***iable) bound to `ast.cmpop`.\n\n(AI generated docstring.)\n\nThe ideograph '比符' (bǐfú) means 'comparison operator'. Its decimal unicode is 27604 and 31526. This `covariant`\n`TypeVar` is bound to `ast.cmpop`, representing comparison operators like less than and equality, and its subclasses,\n`ast.Eq`, `ast.Gt`, `ast.GtE`, `ast.In`, `ast.Is`, `ast.IsNot`, `ast.Lt`, `ast.LtE`, `ast.NotEq`, and `ast.NotIn`.\nTogether with '一符' (unary), '二符' (binary), and '布尔符' (boolean), these form a semiotic system for operator types.\n"
布尔符 = typing_TypeVar('布尔符', bound=ast.boolop, covariant=True)
"`boolop` `TypeVar` (Type ***Var***iable) bound to `ast.boolop`.\n\n(AI generated docstring.)\n\nThe ideograph '布尔符' (bùěrfú) means 'boolean operator'. Its decimal unicode is 24067, 23572, and 31526. This `covariant`\n`TypeVar` is bound to `ast.boolop`, representing boolean operators `and` and `or`, and its subclasses, `ast.And` and\n`ast.Or`. Together with '一符' (unary), '二符' (binary), and '比符' (comparison), these form a semiotic system for operator\ntypes.\n"
常 = typing_TypeVar('常', bound=ast.Constant, covariant=True)
"`Constant` `TypeVar` (Type ***Var***iable) bound to `ast.Constant`.\n\n(AI generated docstring.)\n\nThe ideograph '常' (cháng) means 'constant'. Its decimal unicode is 24120. This `covariant` `TypeVar` is bound to\n`ast.Constant`, representing literal constant values in Python code, and its subclasses, `ast.Bytes`, `ast.Ellipsis`,\n`ast.NameConstant`, `ast.Num`, and `ast.Str`.\n"
拦 = typing_TypeVar('拦', bound=ast.excepthandler, covariant=True)
"`excepthandler` `TypeVar` (Type ***Var***iable) bound to `ast.excepthandler`.\n\n(AI generated docstring.)\n\nThe ideograph '拦' (lán) means 'exception handler'. Its decimal unicode is 25318. This `covariant` `TypeVar` is bound to\n`ast.excepthandler`, representing `except` clauses in try statements, and its subclasses, `ast.ExceptHandler`.\n"
俪 = typing_TypeVar('俪', bound=ast.pattern, covariant=True)
"`pattern` `TypeVar` (Type ***Var***iable) bound to `ast.pattern`.\n\n(AI generated docstring.)\n\nThe ideograph '俪' (lì) means 'pattern'. Its decimal unicode is 20458. This `covariant` `TypeVar` is bound to\n`ast.pattern`, representing patterns used in structural pattern matching, and its subclasses, `ast.MatchAs`,\n`ast.MatchClass`, `ast.MatchMapping`, `ast.MatchOr`, `ast.MatchSequence`, `ast.MatchSingleton`, `ast.MatchStar`, and\n`ast.MatchValue`.\n"
忽 = typing_TypeVar('忽', bound=ast.type_ignore, covariant=True)
"`type_ignore` `TypeVar` (Type ***Var***iable) bound to `ast.type_ignore`.\n\n(AI generated docstring.)\n\nThe ideograph '忽' (hū) means 'ignore'. Its decimal unicode is 24573. This `covariant` `TypeVar` is bound to\n`ast.type_ignore`, representing type checker ignore comments, and its subclasses, `ast.TypeIgnore`.\n"
形 = typing_TypeVar('形', bound=ast.type_param, covariant=True)
"`type_param` `TypeVar` (Type ***Var***iable) bound to `ast.type_param`.\n\n(AI generated docstring.)\n\nThe ideograph '形' (xíng) means 'type parameter'. Its decimal unicode is 24418. This `covariant` `TypeVar` is bound to\n`ast.type_param`, representing type parameters in generic classes and functions, and its subclasses, `ast.ParamSpec`,\n`ast.TypeVar`, and `ast.TypeVarTuple`.\n"

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
