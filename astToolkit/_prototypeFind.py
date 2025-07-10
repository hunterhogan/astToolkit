# ruff: noqa: A001
from astToolkit import ConstantValueType
from collections.abc import Sequence
from typing import Any
from typing_extensions import TypeIs
import ast

class Find:

    @classmethod
    def at(cls, getable: Any, index: int, /) -> object:
        return getable.__getitem__(index)

    @staticmethod
    def Add(node: ast.AST) -> TypeIs[ast.Add]:
        return isinstance(node, ast.Add)

    @staticmethod
    def alias(node: ast.AST) -> TypeIs[ast.alias]:
        return isinstance(node, ast.alias)

    @staticmethod
    def alias_name(node: ast.alias) -> str:
        return node.name

    @staticmethod
    def alias_asname(node: ast.alias) -> str | None:
        return node.asname

    @staticmethod
    def And(node: ast.AST) -> TypeIs[ast.And]:
        return isinstance(node, ast.And)

    @staticmethod
    def AnnAssign(node: ast.AST) -> TypeIs[ast.AnnAssign]:
        return isinstance(node, ast.AnnAssign)

    @staticmethod
    def AnnAssign_target(node: ast.AnnAssign) -> ast.Name | ast.Attribute | ast.Subscript:
        return node.target

    @staticmethod
    def AnnAssign_annotation(node: ast.AnnAssign) -> ast.expr:
        return node.annotation

    @staticmethod
    def AnnAssign_value(node: ast.AnnAssign) -> ast.expr | None:
        return node.value

    @staticmethod
    def AnnAssign_simple(node: ast.AnnAssign) -> int:
        return node.simple

    @staticmethod
    def arg(node: ast.AST) -> TypeIs[ast.arg]:
        return isinstance(node, ast.arg)

    @staticmethod
    def arg_arg(node: ast.arg) -> str:
        return node.arg

    @staticmethod
    def arg_annotation(node: ast.arg) -> ast.expr | None:
        return node.annotation

    @staticmethod
    def arg_type_comment(node: ast.arg) -> str | None:
        return node.type_comment

    @staticmethod
    def arguments(node: ast.AST) -> TypeIs[ast.arguments]:
        return isinstance(node, ast.arguments)

    @staticmethod
    def arguments_posonlyargs(node: ast.arguments) -> list[ast.arg]:
        return node.posonlyargs

    @staticmethod
    def arguments_args(node: ast.arguments) -> list[ast.arg]:
        return node.args

    @staticmethod
    def arguments_vararg(node: ast.arguments) -> ast.arg | None:
        return node.vararg

    @staticmethod
    def arguments_kwonlyargs(node: ast.arguments) -> list[ast.arg]:
        return node.kwonlyargs

    @staticmethod
    def arguments_kw_defaults(node: ast.arguments) -> Sequence[ast.expr | None]:
        return node.kw_defaults

    @staticmethod
    def arguments_kwarg(node: ast.arguments) -> ast.arg | None:
        return node.kwarg

    @staticmethod
    def arguments_defaults(node: ast.arguments) -> Sequence[ast.expr]:
        return node.defaults

    @staticmethod
    def Assert(node: ast.AST) -> TypeIs[ast.Assert]:
        return isinstance(node, ast.Assert)

    @staticmethod
    def Assert_test(node: ast.Assert) -> ast.expr:
        return node.test

    @staticmethod
    def Assert_msg(node: ast.Assert) -> ast.expr | None:
        return node.msg

    @staticmethod
    def Assign(node: ast.AST) -> TypeIs[ast.Assign]:
        return isinstance(node, ast.Assign)

    @staticmethod
    def Assign_targets(node: ast.Assign) -> Sequence[ast.expr]:
        return node.targets

    @staticmethod
    def Assign_value(node: ast.Assign) -> ast.expr:
        return node.value

    @staticmethod
    def Assign_type_comment(node: ast.Assign) -> str | None:
        return node.type_comment

    @staticmethod
    def AST(node: ast.AST) -> TypeIs[ast.AST]:
        return isinstance(node, ast.AST)

    @staticmethod
    def AsyncFor(node: ast.AST) -> TypeIs[ast.AsyncFor]:
        return isinstance(node, ast.AsyncFor)

    @staticmethod
    def AsyncFor_target(node: ast.AsyncFor) -> ast.expr:
        return node.target

    @staticmethod
    def AsyncFor_iter(node: ast.AsyncFor) -> ast.expr:
        return node.iter

    @staticmethod
    def AsyncFor_body(node: ast.AsyncFor) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def AsyncFor_orelse(node: ast.AsyncFor) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def AsyncFor_type_comment(node: ast.AsyncFor) -> str | None:
        return node.type_comment

    @staticmethod
    def AsyncFunctionDef(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
        return isinstance(node, ast.AsyncFunctionDef)

    @staticmethod
    def AsyncFunctionDef_name(node: ast.AsyncFunctionDef) -> str:
        return node.name

    @staticmethod
    def AsyncFunctionDef_args(node: ast.AsyncFunctionDef) -> ast.arguments:
        return node.args

    @staticmethod
    def AsyncFunctionDef_body(node: ast.AsyncFunctionDef) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def AsyncFunctionDef_decorator_list(node: ast.AsyncFunctionDef) -> Sequence[ast.expr]:
        return node.decorator_list

    @staticmethod
    def AsyncFunctionDef_returns(node: ast.AsyncFunctionDef) -> ast.expr | None:
        return node.returns

    @staticmethod
    def AsyncFunctionDef_type_comment(node: ast.AsyncFunctionDef) -> str | None:
        return node.type_comment

    @staticmethod
    def AsyncFunctionDef_type_params(node: ast.AsyncFunctionDef) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def AsyncWith(node: ast.AST) -> TypeIs[ast.AsyncWith]:
        return isinstance(node, ast.AsyncWith)

    @staticmethod
    def AsyncWith_items(node: ast.AsyncWith) -> list[ast.withitem]:
        return node.items

    @staticmethod
    def AsyncWith_body(node: ast.AsyncWith) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def AsyncWith_type_comment(node: ast.AsyncWith) -> str | None:
        return node.type_comment

    @staticmethod
    def Attribute(node: ast.AST) -> TypeIs[ast.Attribute]:
        return isinstance(node, ast.Attribute)

    @staticmethod
    def Attribute_value(node: ast.Attribute) -> ast.expr:
        return node.value

    @staticmethod
    def Attribute_attr(node: ast.Attribute) -> str:
        return node.attr

    @staticmethod
    def Attribute_ctx(node: ast.Attribute) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def AugAssign(node: ast.AST) -> TypeIs[ast.AugAssign]:
        return isinstance(node, ast.AugAssign)

    @staticmethod
    def AugAssign_target(node: ast.AugAssign) -> ast.Name | ast.Attribute | ast.Subscript:
        return node.target

    @staticmethod
    def AugAssign_op(node: ast.AugAssign) -> ast.operator:
        return node.op

    @staticmethod
    def AugAssign_value(node: ast.AugAssign) -> ast.expr:
        return node.value

    @staticmethod
    def Await(node: ast.AST) -> TypeIs[ast.Await]:
        return isinstance(node, ast.Await)

    @staticmethod
    def Await_value(node: ast.Await) -> ast.expr:
        return node.value

    @staticmethod
    def BinOp(node: ast.AST) -> TypeIs[ast.BinOp]:
        return isinstance(node, ast.BinOp)

    @staticmethod
    def BinOp_left(node: ast.BinOp) -> ast.expr:
        return node.left

    @staticmethod
    def BinOp_op(node: ast.BinOp) -> ast.operator:
        return node.op

    @staticmethod
    def BinOp_right(node: ast.BinOp) -> ast.expr:
        return node.right

    @staticmethod
    def BitAnd(node: ast.AST) -> TypeIs[ast.BitAnd]:
        return isinstance(node, ast.BitAnd)

    @staticmethod
    def BitOr(node: ast.AST) -> TypeIs[ast.BitOr]:
        return isinstance(node, ast.BitOr)

    @staticmethod
    def BitXor(node: ast.AST) -> TypeIs[ast.BitXor]:
        return isinstance(node, ast.BitXor)

    @staticmethod
    def boolop(node: ast.AST) -> TypeIs[ast.boolop]:
        return isinstance(node, ast.boolop)

    @staticmethod
    def BoolOp(node: ast.AST) -> TypeIs[ast.BoolOp]:
        return isinstance(node, ast.BoolOp)

    @staticmethod
    def BoolOp_op(node: ast.BoolOp) -> ast.boolop:
        return node.op

    @staticmethod
    def BoolOp_values(node: ast.BoolOp) -> Sequence[ast.expr]:
        return node.values

    @staticmethod
    def Break(node: ast.AST) -> TypeIs[ast.Break]:
        return isinstance(node, ast.Break)

    @staticmethod
    def Call(node: ast.AST) -> TypeIs[ast.Call]:
        return isinstance(node, ast.Call)

    @staticmethod
    def Call_func(node: ast.Call) -> ast.expr:
        return node.func

    @staticmethod
    def Call_args(node: ast.Call) -> Sequence[ast.expr]:
        return node.args

    @staticmethod
    def Call_keywords(node: ast.Call) -> list[ast.keyword]:
        return node.keywords

    @staticmethod
    def ClassDef(node: ast.AST) -> TypeIs[ast.ClassDef]:
        return isinstance(node, ast.ClassDef)

    @staticmethod
    def ClassDef_name(node: ast.ClassDef) -> str:
        return node.name

    @staticmethod
    def ClassDef_bases(node: ast.ClassDef) -> Sequence[ast.expr]:
        return node.bases

    @staticmethod
    def ClassDef_keywords(node: ast.ClassDef) -> list[ast.keyword]:
        return node.keywords

    @staticmethod
    def ClassDef_body(node: ast.ClassDef) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def ClassDef_decorator_list(node: ast.ClassDef) -> Sequence[ast.expr]:
        return node.decorator_list

    @staticmethod
    def ClassDef_type_params(node: ast.ClassDef) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def cmpop(node: ast.AST) -> TypeIs[ast.cmpop]:
        return isinstance(node, ast.cmpop)

    @staticmethod
    def Compare(node: ast.AST) -> TypeIs[ast.Compare]:
        return isinstance(node, ast.Compare)

    @staticmethod
    def Compare_left(node: ast.Compare) -> ast.expr:
        return node.left

    @staticmethod
    def Compare_ops(node: ast.Compare) -> Sequence[ast.cmpop]:
        return node.ops

    @staticmethod
    def Compare_comparators(node: ast.Compare) -> Sequence[ast.expr]:
        return node.comparators

    @staticmethod
    def comprehension(node: ast.AST) -> TypeIs[ast.comprehension]:
        return isinstance(node, ast.comprehension)

    @staticmethod
    def comprehension_target(node: ast.comprehension) -> ast.expr:
        return node.target

    @staticmethod
    def comprehension_iter(node: ast.comprehension) -> ast.expr:
        return node.iter

    @staticmethod
    def comprehension_ifs(node: ast.comprehension) -> Sequence[ast.expr]:
        return node.ifs

    @staticmethod
    def comprehension_is_async(node: ast.comprehension) -> int:
        return node.is_async

    @staticmethod
    def Constant(node: ast.AST) -> TypeIs[ast.Constant]:
        return isinstance(node, ast.Constant)

    @staticmethod
    def Constant_value(node: ast.Constant) -> ConstantValueType:
        return node.value

    @staticmethod
    def Constant_kind(node: ast.Constant) -> str | None:
        return node.kind

    @staticmethod
    def Continue(node: ast.AST) -> TypeIs[ast.Continue]:
        return isinstance(node, ast.Continue)

    @staticmethod
    def Del(node: ast.AST) -> TypeIs[ast.Del]:
        return isinstance(node, ast.Del)

    @staticmethod
    def Delete(node: ast.AST) -> TypeIs[ast.Delete]:
        return isinstance(node, ast.Delete)

    @staticmethod
    def Delete_targets(node: ast.Delete) -> Sequence[ast.expr]:
        return node.targets

    @staticmethod
    def Dict(node: ast.AST) -> TypeIs[ast.Dict]:
        return isinstance(node, ast.Dict)

    @staticmethod
    def Dict_keys(node: ast.Dict) -> Sequence[ast.expr | None]:
        return node.keys

    @staticmethod
    def Dict_values(node: ast.Dict) -> Sequence[ast.expr]:
        return node.values

    @staticmethod
    def DictComp(node: ast.AST) -> TypeIs[ast.DictComp]:
        return isinstance(node, ast.DictComp)

    @staticmethod
    def DictComp_key(node: ast.DictComp) -> ast.expr:
        return node.key

    @staticmethod
    def DictComp_value(node: ast.DictComp) -> ast.expr:
        return node.value

    @staticmethod
    def DictComp_generators(node: ast.DictComp) -> list[ast.comprehension]:
        return node.generators

    @staticmethod
    def Div(node: ast.AST) -> TypeIs[ast.Div]:
        return isinstance(node, ast.Div)

    @staticmethod
    def Eq(node: ast.AST) -> TypeIs[ast.Eq]:
        return isinstance(node, ast.Eq)

    @staticmethod
    def ExceptHandler(node: ast.AST) -> TypeIs[ast.ExceptHandler]:
        return isinstance(node, ast.ExceptHandler)

    @staticmethod
    def ExceptHandler_type(node: ast.ExceptHandler) -> ast.expr | None:
        return node.type

    @staticmethod
    def ExceptHandler_name(node: ast.ExceptHandler) -> str | None:
        return node.name

    @staticmethod
    def ExceptHandler_body(node: ast.ExceptHandler) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def excepthandler(node: ast.AST) -> TypeIs[ast.excepthandler]:
        return isinstance(node, ast.excepthandler)

    @staticmethod
    def expr(node: ast.AST) -> TypeIs[ast.expr]:
        return isinstance(node, ast.expr)

    @staticmethod
    def Expr(node: ast.AST) -> TypeIs[ast.Expr]:
        return isinstance(node, ast.Expr)

    @staticmethod
    def Expr_value(node: ast.Expr) -> ast.expr:
        return node.value

    @staticmethod
    def expr_context(node: ast.AST) -> TypeIs[ast.expr_context]:
        return isinstance(node, ast.expr_context)

    @staticmethod
    def Expression(node: ast.AST) -> TypeIs[ast.Expression]:
        return isinstance(node, ast.Expression)

    @staticmethod
    def Expression_body(node: ast.Expression) -> ast.expr:
        return node.body

    @staticmethod
    def FloorDiv(node: ast.AST) -> TypeIs[ast.FloorDiv]:
        return isinstance(node, ast.FloorDiv)

    @staticmethod
    def For(node: ast.AST) -> TypeIs[ast.For]:
        return isinstance(node, ast.For)

    @staticmethod
    def For_target(node: ast.For) -> ast.expr:
        return node.target

    @staticmethod
    def For_iter(node: ast.For) -> ast.expr:
        return node.iter

    @staticmethod
    def For_body(node: ast.For) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def For_orelse(node: ast.For) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def For_type_comment(node: ast.For) -> str | None:
        return node.type_comment

    @staticmethod
    def FormattedValue(node: ast.AST) -> TypeIs[ast.FormattedValue]:
        return isinstance(node, ast.FormattedValue)

    @staticmethod
    def FormattedValue_value(node: ast.FormattedValue) -> ast.expr:
        return node.value

    @staticmethod
    def FormattedValue_conversion(node: ast.FormattedValue) -> int:
        return node.conversion

    @staticmethod
    def FormattedValue_format_spec(node: ast.FormattedValue) -> ast.expr | None:
        return node.format_spec

    @staticmethod
    def FunctionDef(node: ast.AST) -> TypeIs[ast.FunctionDef]:
        return isinstance(node, ast.FunctionDef)

    @staticmethod
    def FunctionDef_name(node: ast.FunctionDef) -> str:
        return node.name

    @staticmethod
    def FunctionDef_args(node: ast.FunctionDef) -> ast.arguments:
        return node.args

    @staticmethod
    def FunctionDef_body(node: ast.FunctionDef) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def FunctionDef_decorator_list(node: ast.FunctionDef) -> Sequence[ast.expr]:
        return node.decorator_list

    @staticmethod
    def FunctionDef_returns(node: ast.FunctionDef) -> ast.expr | None:
        return node.returns

    @staticmethod
    def FunctionDef_type_comment(node: ast.FunctionDef) -> str | None:
        return node.type_comment

    @staticmethod
    def FunctionDef_type_params(node: ast.FunctionDef) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def FunctionType(node: ast.AST) -> TypeIs[ast.FunctionType]:
        return isinstance(node, ast.FunctionType)

    @staticmethod
    def FunctionType_argtypes(node: ast.FunctionType) -> Sequence[ast.expr]:
        return node.argtypes

    @staticmethod
    def FunctionType_returns(node: ast.FunctionType) -> ast.expr:
        return node.returns

    @staticmethod
    def GeneratorExp(node: ast.AST) -> TypeIs[ast.GeneratorExp]:
        return isinstance(node, ast.GeneratorExp)

    @staticmethod
    def GeneratorExp_elt(node: ast.GeneratorExp) -> ast.expr:
        return node.elt

    @staticmethod
    def GeneratorExp_generators(node: ast.GeneratorExp) -> list[ast.comprehension]:
        return node.generators

    @staticmethod
    def Global(node: ast.AST) -> TypeIs[ast.Global]:
        return isinstance(node, ast.Global)

    @staticmethod
    def Global_names(node: ast.Global) -> list[str]:
        return node.names

    @staticmethod
    def Gt(node: ast.AST) -> TypeIs[ast.Gt]:
        return isinstance(node, ast.Gt)

    @staticmethod
    def GtE(node: ast.AST) -> TypeIs[ast.GtE]:
        return isinstance(node, ast.GtE)

    @staticmethod
    def If(node: ast.AST) -> TypeIs[ast.If]:
        return isinstance(node, ast.If)

    @staticmethod
    def If_test(node: ast.If) -> ast.expr:
        return node.test

    @staticmethod
    def If_body(node: ast.If) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def If_orelse(node: ast.If) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def IfExp(node: ast.AST) -> TypeIs[ast.IfExp]:
        return isinstance(node, ast.IfExp)

    @staticmethod
    def IfExp_test(node: ast.IfExp) -> ast.expr:
        return node.test

    @staticmethod
    def IfExp_body(node: ast.IfExp) -> ast.expr:
        return node.body

    @staticmethod
    def IfExp_orelse(node: ast.IfExp) -> ast.expr:
        return node.orelse

    @staticmethod
    def Import(node: ast.AST) -> TypeIs[ast.Import]:
        return isinstance(node, ast.Import)

    @staticmethod
    def Import_names(node: ast.Import) -> list[ast.alias]:
        return node.names

    @staticmethod
    def ImportFrom(node: ast.AST) -> TypeIs[ast.ImportFrom]:
        return isinstance(node, ast.ImportFrom)

    @staticmethod
    def ImportFrom_module(node: ast.ImportFrom) -> str | None:
        return node.module

    @staticmethod
    def ImportFrom_names(node: ast.ImportFrom) -> list[ast.alias]:
        return node.names

    @staticmethod
    def ImportFrom_level(node: ast.ImportFrom) -> int:
        return node.level

    @staticmethod
    def In(node: ast.AST) -> TypeIs[ast.In]:
        return isinstance(node, ast.In)

    @staticmethod
    def Interactive(node: ast.AST) -> TypeIs[ast.Interactive]:
        return isinstance(node, ast.Interactive)

    @staticmethod
    def Interactive_body(node: ast.Interactive) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def Invert(node: ast.AST) -> TypeIs[ast.Invert]:
        return isinstance(node, ast.Invert)

    @staticmethod
    def Is(node: ast.AST) -> TypeIs[ast.Is]:
        return isinstance(node, ast.Is)

    @staticmethod
    def IsNot(node: ast.AST) -> TypeIs[ast.IsNot]:
        return isinstance(node, ast.IsNot)

    @staticmethod
    def JoinedStr(node: ast.AST) -> TypeIs[ast.JoinedStr]:
        return isinstance(node, ast.JoinedStr)

    @staticmethod
    def JoinedStr_values(node: ast.JoinedStr) -> Sequence[ast.expr]:
        return node.values

    @staticmethod
    def keyword(node: ast.AST) -> TypeIs[ast.keyword]:
        return isinstance(node, ast.keyword)

    @staticmethod
    def keyword_arg(node: ast.keyword) -> str | None:
        return node.arg

    @staticmethod
    def keyword_value(node: ast.keyword) -> ast.expr:
        return node.value

    @staticmethod
    def Lambda(node: ast.AST) -> TypeIs[ast.Lambda]:
        return isinstance(node, ast.Lambda)

    @staticmethod
    def Lambda_args(node: ast.Lambda) -> ast.arguments:
        return node.args

    @staticmethod
    def Lambda_body(node: ast.Lambda) -> ast.expr:
        return node.body

    @staticmethod
    def List(node: ast.AST) -> TypeIs[ast.List]:
        return isinstance(node, ast.List)

    @staticmethod
    def List_elts(node: ast.List) -> Sequence[ast.expr]:
        return node.elts

    @staticmethod
    def List_ctx(node: ast.List) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def ListComp(node: ast.AST) -> TypeIs[ast.ListComp]:
        return isinstance(node, ast.ListComp)

    @staticmethod
    def ListComp_elt(node: ast.ListComp) -> ast.expr:
        return node.elt

    @staticmethod
    def ListComp_generators(node: ast.ListComp) -> list[ast.comprehension]:
        return node.generators

    @staticmethod
    def Load(node: ast.AST) -> TypeIs[ast.Load]:
        return isinstance(node, ast.Load)

    @staticmethod
    def LShift(node: ast.AST) -> TypeIs[ast.LShift]:
        return isinstance(node, ast.LShift)

    @staticmethod
    def Lt(node: ast.AST) -> TypeIs[ast.Lt]:
        return isinstance(node, ast.Lt)

    @staticmethod
    def LtE(node: ast.AST) -> TypeIs[ast.LtE]:
        return isinstance(node, ast.LtE)

    @staticmethod
    def Match(node: ast.AST) -> TypeIs[ast.Match]:
        return isinstance(node, ast.Match)

    @staticmethod
    def Match_subject(node: ast.Match) -> ast.expr:
        return node.subject

    @staticmethod
    def Match_cases(node: ast.Match) -> list[ast.match_case]:
        return node.cases

    @staticmethod
    def match_case(node: ast.AST) -> TypeIs[ast.match_case]:
        return isinstance(node, ast.match_case)

    @staticmethod
    def match_case_pattern(node: ast.match_case) -> ast.pattern:
        return node.pattern

    @staticmethod
    def match_case_guard(node: ast.match_case) -> ast.expr | None:
        return node.guard

    @staticmethod
    def match_case_body(node: ast.match_case) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def MatchAs(node: ast.AST) -> TypeIs[ast.MatchAs]:
        return isinstance(node, ast.MatchAs)

    @staticmethod
    def MatchAs_pattern(node: ast.MatchAs) -> ast.pattern | None:
        return node.pattern

    @staticmethod
    def MatchAs_name(node: ast.MatchAs) -> str | None:
        return node.name

    @staticmethod
    def MatchClass(node: ast.AST) -> TypeIs[ast.MatchClass]:
        return isinstance(node, ast.MatchClass)

    @staticmethod
    def MatchClass_cls(node: ast.MatchClass) -> ast.expr:
        return node.cls

    @staticmethod
    def MatchClass_patterns(node: ast.MatchClass) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def MatchClass_kwd_attrs(node: ast.MatchClass) -> list[str]:
        return node.kwd_attrs

    @staticmethod
    def MatchClass_kwd_patterns(node: ast.MatchClass) -> Sequence[ast.pattern]:
        return node.kwd_patterns

    @staticmethod
    def MatchMapping(node: ast.AST) -> TypeIs[ast.MatchMapping]:
        return isinstance(node, ast.MatchMapping)

    @staticmethod
    def MatchMapping_keys(node: ast.MatchMapping) -> Sequence[ast.expr]:
        return node.keys

    @staticmethod
    def MatchMapping_patterns(node: ast.MatchMapping) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def MatchMapping_rest(node: ast.MatchMapping) -> str | None:
        return node.rest

    @staticmethod
    def MatchOr(node: ast.AST) -> TypeIs[ast.MatchOr]:
        return isinstance(node, ast.MatchOr)

    @staticmethod
    def MatchOr_patterns(node: ast.MatchOr) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def MatchSequence(node: ast.AST) -> TypeIs[ast.MatchSequence]:
        return isinstance(node, ast.MatchSequence)

    @staticmethod
    def MatchSequence_patterns(node: ast.MatchSequence) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def MatchSingleton(node: ast.AST) -> TypeIs[ast.MatchSingleton]:
        return isinstance(node, ast.MatchSingleton)

    @staticmethod
    def MatchSingleton_value(node: ast.MatchSingleton) -> bool | None:
        return node.value

    @staticmethod
    def MatchStar(node: ast.AST) -> TypeIs[ast.MatchStar]:
        return isinstance(node, ast.MatchStar)

    @staticmethod
    def MatchStar_name(node: ast.MatchStar) -> str | None:
        return node.name

    @staticmethod
    def MatchValue(node: ast.AST) -> TypeIs[ast.MatchValue]:
        return isinstance(node, ast.MatchValue)

    @staticmethod
    def MatchValue_value(node: ast.MatchValue) -> ast.expr:
        return node.value

    @staticmethod
    def MatMult(node: ast.AST) -> TypeIs[ast.MatMult]:
        return isinstance(node, ast.MatMult)

    @staticmethod
    def mod(node: ast.AST) -> TypeIs[ast.mod]:
        return isinstance(node, ast.mod)

    @staticmethod
    def Mod(node: ast.AST) -> TypeIs[ast.Mod]:
        return isinstance(node, ast.Mod)

    @staticmethod
    def Module(node: ast.AST) -> TypeIs[ast.Module]:
        return isinstance(node, ast.Module)

    @staticmethod
    def Module_body(node: ast.Module) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def Module_type_ignores(node: ast.Module) -> list[ast.TypeIgnore]:
        return node.type_ignores

    @staticmethod
    def Mult(node: ast.AST) -> TypeIs[ast.Mult]:
        return isinstance(node, ast.Mult)

    @staticmethod
    def Name(node: ast.AST) -> TypeIs[ast.Name]:
        return isinstance(node, ast.Name)

    @staticmethod
    def Name_id(node: ast.Name) -> str:
        return node.id

    @staticmethod
    def Name_ctx(node: ast.Name) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def NamedExpr(node: ast.AST) -> TypeIs[ast.NamedExpr]:
        return isinstance(node, ast.NamedExpr)

    @staticmethod
    def NamedExpr_target(node: ast.NamedExpr) -> ast.Name:
        return node.target

    @staticmethod
    def NamedExpr_value(node: ast.NamedExpr) -> ast.expr:
        return node.value

    @staticmethod
    def Nonlocal(node: ast.AST) -> TypeIs[ast.Nonlocal]:
        return isinstance(node, ast.Nonlocal)

    @staticmethod
    def Nonlocal_names(node: ast.Nonlocal) -> list[str]:
        return node.names

    @staticmethod
    def Not(node: ast.AST) -> TypeIs[ast.Not]:
        return isinstance(node, ast.Not)

    @staticmethod
    def NotEq(node: ast.AST) -> TypeIs[ast.NotEq]:
        return isinstance(node, ast.NotEq)

    @staticmethod
    def NotIn(node: ast.AST) -> TypeIs[ast.NotIn]:
        return isinstance(node, ast.NotIn)

    @staticmethod
    def operator(node: ast.AST) -> TypeIs[ast.operator]:
        return isinstance(node, ast.operator)

    @staticmethod
    def Or(node: ast.AST) -> TypeIs[ast.Or]:
        return isinstance(node, ast.Or)

    @staticmethod
    def ParamSpec(node: ast.AST) -> TypeIs[ast.ParamSpec]:
        return isinstance(node, ast.ParamSpec)

    @staticmethod
    def ParamSpec_name(node: ast.ParamSpec) -> str:
        return node.name

    @staticmethod
    def ParamSpec_default_value(node: ast.ParamSpec) -> ast.expr | None:
        return node.default_value

    @staticmethod
    def Pass(node: ast.AST) -> TypeIs[ast.Pass]:
        return isinstance(node, ast.Pass)

    @staticmethod
    def pattern(node: ast.AST) -> TypeIs[ast.pattern]:
        return isinstance(node, ast.pattern)

    @staticmethod
    def Pow(node: ast.AST) -> TypeIs[ast.Pow]:
        return isinstance(node, ast.Pow)

    @staticmethod
    def Raise(node: ast.AST) -> TypeIs[ast.Raise]:
        return isinstance(node, ast.Raise)

    @staticmethod
    def Raise_exc(node: ast.Raise) -> ast.expr | None:
        return node.exc

    @staticmethod
    def Raise_cause(node: ast.Raise) -> ast.expr | None:
        return node.cause

    @staticmethod
    def Return(node: ast.AST) -> TypeIs[ast.Return]:
        return isinstance(node, ast.Return)

    @staticmethod
    def Return_value(node: ast.Return) -> ast.expr | None:
        return node.value

    @staticmethod
    def RShift(node: ast.AST) -> TypeIs[ast.RShift]:
        return isinstance(node, ast.RShift)

    @staticmethod
    def Set(node: ast.AST) -> TypeIs[ast.Set]:
        return isinstance(node, ast.Set)

    @staticmethod
    def Set_elts(node: ast.Set) -> Sequence[ast.expr]:
        return node.elts

    @staticmethod
    def SetComp(node: ast.AST) -> TypeIs[ast.SetComp]:
        return isinstance(node, ast.SetComp)

    @staticmethod
    def SetComp_elt(node: ast.SetComp) -> ast.expr:
        return node.elt

    @staticmethod
    def SetComp_generators(node: ast.SetComp) -> list[ast.comprehension]:
        return node.generators

    @staticmethod
    def Slice(node: ast.AST) -> TypeIs[ast.Slice]:
        return isinstance(node, ast.Slice)

    @staticmethod
    def Slice_lower(node: ast.Slice) -> ast.expr | None:
        return node.lower

    @staticmethod
    def Slice_upper(node: ast.Slice) -> ast.expr | None:
        return node.upper

    @staticmethod
    def Slice_step(node: ast.Slice) -> ast.expr | None:
        return node.step

    @staticmethod
    def Starred(node: ast.AST) -> TypeIs[ast.Starred]:
        return isinstance(node, ast.Starred)

    @staticmethod
    def Starred_value(node: ast.Starred) -> ast.expr:
        return node.value

    @staticmethod
    def Starred_ctx(node: ast.Starred) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def stmt(node: ast.AST) -> TypeIs[ast.stmt]:
        return isinstance(node, ast.stmt)

    @staticmethod
    def Store(node: ast.AST) -> TypeIs[ast.Store]:
        return isinstance(node, ast.Store)

    @staticmethod
    def Sub(node: ast.AST) -> TypeIs[ast.Sub]:
        return isinstance(node, ast.Sub)

    @staticmethod
    def Subscript(node: ast.AST) -> TypeIs[ast.Subscript]:
        return isinstance(node, ast.Subscript)

    @staticmethod
    def Subscript_value(node: ast.Subscript) -> ast.expr:
        return node.value

    @staticmethod
    def Subscript_slice(node: ast.Subscript) -> ast.expr:
        return node.slice

    @staticmethod
    def Subscript_ctx(node: ast.Subscript) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def Try(node: ast.AST) -> TypeIs[ast.Try]:
        return isinstance(node, ast.Try)

    @staticmethod
    def Try_body(node: ast.Try) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def Try_handlers(node: ast.Try) -> list[ast.ExceptHandler]:
        return node.handlers

    @staticmethod
    def Try_orelse(node: ast.Try) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def Try_finalbody(node: ast.Try) -> Sequence[ast.stmt]:
        return node.finalbody

    @staticmethod
    def TryStar(node: ast.AST) -> TypeIs[ast.TryStar]:
        return isinstance(node, ast.TryStar)

    @staticmethod
    def TryStar_body(node: ast.TryStar) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def TryStar_handlers(node: ast.TryStar) -> list[ast.ExceptHandler]:
        return node.handlers

    @staticmethod
    def TryStar_orelse(node: ast.TryStar) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def TryStar_finalbody(node: ast.TryStar) -> Sequence[ast.stmt]:
        return node.finalbody

    @staticmethod
    def Tuple(node: ast.AST) -> TypeIs[ast.Tuple]:
        return isinstance(node, ast.Tuple)

    @staticmethod
    def Tuple_elts(node: ast.Tuple) -> Sequence[ast.expr]:
        return node.elts

    @staticmethod
    def Tuple_ctx(node: ast.Tuple) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def type_ignore(node: ast.AST) -> TypeIs[ast.type_ignore]:
        return isinstance(node, ast.type_ignore)

    @staticmethod
    def type_param(node: ast.AST) -> TypeIs[ast.type_param]:
        return isinstance(node, ast.type_param)

    @staticmethod
    def TypeAlias(node: ast.AST) -> TypeIs[ast.TypeAlias]:
        return isinstance(node, ast.TypeAlias)

    @staticmethod
    def TypeAlias_name(node: ast.TypeAlias) -> ast.Name:
        return node.name

    @staticmethod
    def TypeAlias_type_params(node: ast.TypeAlias) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def TypeAlias_value(node: ast.TypeAlias) -> ast.expr:
        return node.value

    @staticmethod
    def TypeIgnore(node: ast.AST) -> TypeIs[ast.TypeIgnore]:
        return isinstance(node, ast.TypeIgnore)

    @staticmethod
    def TypeIgnore_lineno(node: ast.TypeIgnore) -> int:
        return node.lineno

    @staticmethod
    def TypeIgnore_tag(node: ast.TypeIgnore) -> str:
        return node.tag

    @staticmethod
    def TypeVar(node: ast.AST) -> TypeIs[ast.TypeVar]:
        return isinstance(node, ast.TypeVar)

    @staticmethod
    def TypeVar_name(node: ast.TypeVar) -> str:
        return node.name

    @staticmethod
    def TypeVar_bound(node: ast.TypeVar) -> ast.expr | None:
        return node.bound

    @staticmethod
    def TypeVar_default_value(node: ast.TypeVar) -> ast.expr | None:
        return node.default_value

    @staticmethod
    def TypeVarTuple(node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
        return isinstance(node, ast.TypeVarTuple)

    @staticmethod
    def TypeVarTuple_name(node: ast.TypeVarTuple) -> str:
        return node.name

    @staticmethod
    def TypeVarTuple_default_value(node: ast.TypeVarTuple) -> ast.expr | None:
        return node.default_value

    @staticmethod
    def UAdd(node: ast.AST) -> TypeIs[ast.UAdd]:
        return isinstance(node, ast.UAdd)

    @staticmethod
    def unaryop(node: ast.AST) -> TypeIs[ast.unaryop]:
        return isinstance(node, ast.unaryop)

    @staticmethod
    def UnaryOp(node: ast.AST) -> TypeIs[ast.UnaryOp]:
        return isinstance(node, ast.UnaryOp)

    @staticmethod
    def UnaryOp_op(node: ast.UnaryOp) -> ast.unaryop:
        return node.op

    @staticmethod
    def UnaryOp_operand(node: ast.UnaryOp) -> ast.expr:
        return node.operand

    @staticmethod
    def USub(node: ast.AST) -> TypeIs[ast.USub]:
        return isinstance(node, ast.USub)

    @staticmethod
    def While(node: ast.AST) -> TypeIs[ast.While]:
        return isinstance(node, ast.While)

    @staticmethod
    def While_test(node: ast.While) -> ast.expr:
        return node.test

    @staticmethod
    def While_body(node: ast.While) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def While_orelse(node: ast.While) -> Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    def With(node: ast.AST) -> TypeIs[ast.With]:
        return isinstance(node, ast.With)

    @staticmethod
    def With_items(node: ast.With) -> list[ast.withitem]:
        return node.items

    @staticmethod
    def With_body(node: ast.With) -> Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def With_type_comment(node: ast.With) -> str | None:
        return node.type_comment

    @staticmethod
    def withitem(node: ast.AST) -> TypeIs[ast.withitem]:
        return isinstance(node, ast.withitem)

    @staticmethod
    def withitem_context_expr(node: ast.withitem) -> ast.expr:
        return node.context_expr

    @staticmethod
    def withitem_optional_vars(node: ast.withitem) -> ast.expr | None:
        return node.optional_vars

    @staticmethod
    def Yield(node: ast.AST) -> TypeIs[ast.Yield]:
        return isinstance(node, ast.Yield)

    @staticmethod
    def Yield_value(node: ast.Yield) -> ast.expr | None:
        return node.value

    @staticmethod
    def YieldFrom(node: ast.AST) -> TypeIs[ast.YieldFrom]:
        return isinstance(node, ast.YieldFrom)

    @staticmethod
    def YieldFrom_value(node: ast.YieldFrom) -> ast.expr:
        return node.value
