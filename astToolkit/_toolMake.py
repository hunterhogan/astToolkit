"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import (
	ast_attributes, ast_attributes_int, ast_attributes_type_comment, ConstantValueType,
	identifierDotAttribute,
)
from collections.abc import Sequence
from typing import overload
from typing_extensions import Unpack
import ast
import sys

class Make:
    """
    Almost all parameters described here are only accessible through a method's `**keywordArguments` parameter.

    Parameters:
        context (ast.Load()): Are you loading from, storing to, or deleting the identifier? The `context` (also, `ctx`) value is `ast.Load()`, `ast.Store()`, or `ast.Del()`.
        col_offset (0): int Position information specifying the column where an AST node begins.
        end_col_offset (None): int|None Position information specifying the column where an AST node ends.
        end_lineno (None): int|None Position information specifying the line number where an AST node ends.
        level (0): int Module import depth level that controls relative vs absolute imports. Default 0 indicates absolute import.
        lineno: int Position information manually specifying the line number where an AST node begins.
        kind (None): str|None Used for type annotations in limited cases.
        type_comment (None): str|None "type_comment is an optional string with the type annotation as a comment." or `# type: ignore`.
        type_params: list[ast.type_param] Type parameters for generic type definitions.

    The `ast._Attributes`, lineno, col_offset, end_lineno, and end_col_offset, hold position information; however, they are, importantly, _not_ `ast._fields`.
    """

    @staticmethod
    def alias(name: str, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.alias:
        return ast.alias(name=name, asname=asName, **keywordArguments)

    @staticmethod
    def AnnAssign(target: ast.Name | ast.Attribute | ast.Subscript, annotation: ast.expr, value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.AnnAssign:
        return ast.AnnAssign(target=target, annotation=annotation, value=value, simple=int(isinstance(target, ast.Name)), **keywordArguments)

    @staticmethod
    def arg(arg: str, annotation: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.arg:
        return ast.arg(arg=arg, annotation=annotation, **keywordArguments)

    @staticmethod
    def arguments(posonlyargs: list[ast.arg]=[], args: list[ast.arg]=[], vararg: ast.arg | None=None, kwonlyargs: list[ast.arg]=[], kw_defaults: Sequence[ast.expr | None]=[None], kwarg: ast.arg | None=None, defaults: Sequence[ast.expr]=[]) -> ast.arguments:
        return ast.arguments(posonlyargs=posonlyargs, args=args, vararg=vararg, kwonlyargs=kwonlyargs, kw_defaults=list(kw_defaults), kwarg=kwarg, defaults=list(defaults))

    @staticmethod
    def Assert(test: ast.expr, msg: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Assert:
        return ast.Assert(test=test, msg=msg, **keywordArguments)

    @staticmethod
    def Assign(targets: Sequence[ast.expr], value: ast.expr, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.Assign:
        return ast.Assign(targets=list(targets), value=value, **keywordArguments)

    @staticmethod
    def AsyncFor(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFor:
        return ast.AsyncFor(target=target, iter=iter, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def AsyncFunctionDef(name: str, args: ast.arguments=ast.arguments(), body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFunctionDef:
        return ast.AsyncFunctionDef(name=name, args=args, body=list(body), decorator_list=list(decorator_list), returns=returns, type_params=list(type_params), **keywordArguments)

    @staticmethod
    def AsyncWith(items: Sequence[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncWith:
        return ast.AsyncWith(items=list(items), body=list(body), **keywordArguments)

    @staticmethod
    def Attribute(value: ast.expr, *attribute: str, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
        """
        If two identifiers are joined by a dot '`.`', they are _usually_ an `ast.Attribute`, but see, for example, `ast.ImportFrom`.

        Parameters:
            value: the part before the dot (e.g., `ast.Name`.)
            attribute: an identifier after a dot '`.`'; you can pass multiple `attribute` and they will be chained together.
        """

        def addDOTattribute(chain: ast.expr, identifier: str, context: ast.expr_context, **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
            return ast.Attribute(value=chain, attr=identifier, ctx=context, **keywordArguments)
        buffaloBuffalo = addDOTattribute(value, attribute[0], context, **keywordArguments)
        for identifier in attribute[1:None]:
            buffaloBuffalo = addDOTattribute(buffaloBuffalo, identifier, context, **keywordArguments)
        return buffaloBuffalo

    @staticmethod
    def AugAssign(target: ast.Name | ast.Attribute | ast.Subscript, op: ast.operator, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.AugAssign:
        return ast.AugAssign(target=target, op=op, value=value, **keywordArguments)

    @staticmethod
    def Await(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Await:
        return ast.Await(value=value, **keywordArguments)

    @staticmethod
    def BinOp(left: ast.expr, op: ast.operator, right: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.BinOp:
        return ast.BinOp(left=left, op=op, right=right, **keywordArguments)

    @staticmethod
    def BoolOp(op: ast.boolop, values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.BoolOp:
        return ast.BoolOp(op=op, values=list(values), **keywordArguments)

    @staticmethod
    def Break(**keywordArguments: Unpack[ast_attributes]) -> ast.Break:
        return ast.Break(**keywordArguments)

    @staticmethod
    def Call(callee: ast.expr, args: Sequence[ast.expr]=[], list_keyword: Sequence[ast.keyword]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Call:
        return ast.Call(func=callee, args=list(args), keywords=list(list_keyword), **keywordArguments)

    @staticmethod
    def ClassDef(name: str, bases: Sequence[ast.expr]=[], list_keyword: Sequence[ast.keyword]=[], body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.ClassDef:
        return ast.ClassDef(name=name, bases=list(bases), keywords=list(list_keyword), body=list(body), decorator_list=list(decorator_list), type_params=list(type_params), **keywordArguments)

    @staticmethod
    def Compare(left: ast.expr, ops: Sequence[ast.cmpop], comparators: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Compare:
        return ast.Compare(left=left, ops=list(ops), comparators=list(comparators), **keywordArguments)

    @staticmethod
    def comprehension(target: ast.expr, iter: ast.expr, ifs: Sequence[ast.expr], is_async: int) -> ast.comprehension:
        return ast.comprehension(target=target, iter=iter, ifs=list(ifs), is_async=is_async)

    @staticmethod
    def Constant(value: ConstantValueType, kind: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Constant:
        return ast.Constant(value=value, kind=kind, **keywordArguments) # pyright: ignore[reportArgumentType]

    @staticmethod
    def Continue(**keywordArguments: Unpack[ast_attributes]) -> ast.Continue:
        return ast.Continue(**keywordArguments)

    @staticmethod
    def Delete(targets: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Delete:
        return ast.Delete(targets=list(targets), **keywordArguments)

    @staticmethod
    def Dict(keys: Sequence[ast.expr | None]=[None], values: Sequence[ast.expr]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Dict:
        return ast.Dict(keys=list(keys), values=list(values), **keywordArguments)

    @staticmethod
    def DictComp(key: ast.expr, value: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.DictComp:
        return ast.DictComp(key=key, value=value, generators=list(generators), **keywordArguments)

    @staticmethod
    def excepthandler(**keywordArguments: Unpack[ast_attributes]) -> ast.excepthandler:
        return ast.excepthandler(**keywordArguments)

    @staticmethod
    def ExceptHandler(type: ast.expr | None=None, name: str | None=None, body: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.ExceptHandler:
        return ast.ExceptHandler(type=type, name=name, body=list(body), **keywordArguments)

    @staticmethod
    def expr(**keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        return ast.expr(**keywordArguments)

    @staticmethod
    def Expr(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Expr:
        return ast.Expr(value=value, **keywordArguments)

    @staticmethod
    def Expression(body: ast.expr) -> ast.Expression:
        return ast.Expression(body=body)

    @staticmethod
    def For(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.For:
        return ast.For(target=target, iter=iter, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def FormattedValue(value: ast.expr, conversion: int, format_spec: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.FormattedValue:
        return ast.FormattedValue(value=value, conversion=conversion, format_spec=format_spec, **keywordArguments)

    @staticmethod
    def FunctionDef(name: str, args: ast.arguments=ast.arguments(), body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.FunctionDef:
        return ast.FunctionDef(name=name, args=args, body=list(body), decorator_list=list(decorator_list), returns=returns, type_params=list(type_params), **keywordArguments)

    @staticmethod
    def FunctionType(argtypes: Sequence[ast.expr], returns: ast.expr) -> ast.FunctionType:
        return ast.FunctionType(argtypes=list(argtypes), returns=returns)

    @staticmethod
    def GeneratorExp(elt: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.GeneratorExp:
        return ast.GeneratorExp(elt=elt, generators=list(generators), **keywordArguments)

    @staticmethod
    def Global(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Global:
        return ast.Global(names=names, **keywordArguments)

    @staticmethod
    def If(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.If:
        return ast.If(test=test, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def IfExp(test: ast.expr, body: ast.expr, orElse: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.IfExp:
        return ast.IfExp(test=test, body=body, orelse=orElse, **keywordArguments)

    @staticmethod
    def Import(dotModule: identifierDotAttribute, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Import:
        return ast.Import(names=[Make.alias(dotModule, asName)], **keywordArguments)

    @staticmethod
    def ImportFrom(module: str | None, list_alias: list[ast.alias], level: int=0, **keywordArguments: Unpack[ast_attributes]) -> ast.ImportFrom:
        return ast.ImportFrom(module=module, names=list_alias, level=level, **keywordArguments)

    @staticmethod
    def Interactive(body: Sequence[ast.stmt]) -> ast.Interactive:
        return ast.Interactive(body=list(body))

    @staticmethod
    def JoinedStr(values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.JoinedStr:
        return ast.JoinedStr(values=list(values), **keywordArguments)

    @staticmethod
    @overload
    def keyword(arg: str | None, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword:...
    @staticmethod
    @overload
    def keyword(arg: str | None = None, *, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword:...
    @staticmethod
    def keyword(arg: str | None, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword: # pyright: ignore[reportInconsistentOverload]
        return ast.keyword(arg=arg, value=value, **keywordArguments)

    @staticmethod
    def Lambda(args: ast.arguments, body: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Lambda:
        return ast.Lambda(args=args, body=body, **keywordArguments)

    @staticmethod
    def List(elts: Sequence[ast.expr]=[], context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.List:
        return ast.List(elts=list(elts), ctx=context, **keywordArguments)

    @staticmethod
    def ListComp(elt: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.ListComp:
        return ast.ListComp(elt=elt, generators=list(generators), **keywordArguments)

    @staticmethod
    def Match(subject: ast.expr, cases: Sequence[ast.match_case]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Match:
        return ast.Match(subject=subject, cases=list(cases), **keywordArguments)

    @staticmethod
    def match_case(pattern: ast.pattern, guard: ast.expr | None=None, body: Sequence[ast.stmt]=[]) -> ast.match_case:
        return ast.match_case(pattern=pattern, guard=guard, body=list(body))

    @staticmethod
    def MatchAs(pattern: ast.pattern | None=None, name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchAs:
        return ast.MatchAs(pattern=pattern, name=name, **keywordArguments)

    @staticmethod
    def MatchClass(cls: ast.expr, patterns: Sequence[ast.pattern]=[], kwd_attrs: list[str]=[], kwd_patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchClass: # pyright: ignore[reportSelfClsParameterName]
        return ast.MatchClass(cls=cls, patterns=list(patterns), kwd_attrs=kwd_attrs, kwd_patterns=list(kwd_patterns), **keywordArguments)

    @staticmethod
    def MatchMapping(keys: Sequence[ast.expr]=[], patterns: Sequence[ast.pattern]=[], rest: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchMapping:
        return ast.MatchMapping(keys=list(keys), patterns=list(patterns), rest=rest, **keywordArguments)

    @staticmethod
    def MatchOr(patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchOr:
        return ast.MatchOr(patterns=list(patterns), **keywordArguments)

    @staticmethod
    def MatchSequence(patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSequence:
        return ast.MatchSequence(patterns=list(patterns), **keywordArguments)

    @staticmethod
    def MatchSingleton(value: bool | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSingleton:
        return ast.MatchSingleton(value=value, **keywordArguments)

    @staticmethod
    def MatchStar(name: str | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchStar:
        return ast.MatchStar(name=name, **keywordArguments)

    @staticmethod
    def MatchValue(value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchValue:
        return ast.MatchValue(value=value, **keywordArguments)

    @staticmethod
    def Module(body: Sequence[ast.stmt], type_ignores: list[ast.TypeIgnore]=[]) -> ast.Module:
        return ast.Module(body=list(body), type_ignores=type_ignores)

    @staticmethod
    def Name(id: str, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Name:
        return ast.Name(id=id, ctx=context, **keywordArguments)

    @staticmethod
    def NamedExpr(target: ast.Name, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.NamedExpr:
        return ast.NamedExpr(target=target, value=value, **keywordArguments)

    @staticmethod
    def Nonlocal(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Nonlocal:
        return ast.Nonlocal(names=names, **keywordArguments)
    if sys.version_info >= (3, 13):

        @staticmethod
        def ParamSpec(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
            return ast.ParamSpec(name=name, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def ParamSpec(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
            return ast.ParamSpec(name=name, **keywordArguments)

    @staticmethod
    def Pass(**keywordArguments: Unpack[ast_attributes]) -> ast.Pass:
        return ast.Pass(**keywordArguments)

    @staticmethod
    def pattern(**keywordArguments: Unpack[ast_attributes_int]) -> ast.pattern:
        return ast.pattern(**keywordArguments)

    @staticmethod
    def Raise(exc: ast.expr | None=None, cause: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Raise:
        return ast.Raise(exc=exc, cause=cause, **keywordArguments)

    @staticmethod
    def Return(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Return:
        return ast.Return(value=value, **keywordArguments)

    @staticmethod
    def Set(elts: Sequence[ast.expr]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Set:
        return ast.Set(elts=list(elts), **keywordArguments)

    @staticmethod
    def SetComp(elt: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.SetComp:
        return ast.SetComp(elt=elt, generators=list(generators), **keywordArguments)

    @staticmethod
    def Slice(lower: ast.expr | None=None, upper: ast.expr | None=None, step: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Slice:
        return ast.Slice(lower=lower, upper=upper, step=step, **keywordArguments)

    @staticmethod
    def Starred(value: ast.expr, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Starred:
        return ast.Starred(value=value, ctx=context, **keywordArguments)

    @staticmethod
    def stmt(**keywordArguments: Unpack[ast_attributes]) -> ast.stmt:
        return ast.stmt(**keywordArguments)

    @staticmethod
    def Subscript(value: ast.expr, slice: ast.expr, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Subscript:
        return ast.Subscript(value=value, slice=slice, ctx=context, **keywordArguments)

    @staticmethod
    def Try(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt]=[], finalbody: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Try:
        return ast.Try(body=list(body), handlers=handlers, orelse=list(orElse), finalbody=list(finalbody), **keywordArguments)

    @staticmethod
    def TryStar(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt]=[], finalbody: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.TryStar:
        return ast.TryStar(body=list(body), handlers=handlers, orelse=list(orElse), finalbody=list(finalbody), **keywordArguments)

    @staticmethod
    def Tuple(elts: Sequence[ast.expr]=[], context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Tuple:
        return ast.Tuple(elts=list(elts), ctx=context, **keywordArguments)

    @staticmethod
    def type_param(**keywordArguments: Unpack[ast_attributes_int]) -> ast.type_param:
        return ast.type_param(**keywordArguments)

    @staticmethod
    @overload
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param] = [], *, value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias:...
    @staticmethod
    @overload
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias:...
    @staticmethod
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias: # pyright: ignore[reportInconsistentOverload]
        return ast.TypeAlias(name=name, type_params=list(type_params), value=value, **keywordArguments)

    @staticmethod
    def TypeIgnore(lineno: int, tag: str) -> ast.TypeIgnore:
        return ast.TypeIgnore(lineno=lineno, tag=tag)
    if sys.version_info >= (3, 13):

        @staticmethod
        def TypeVar(name: str, bound: ast.expr | None=None, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
            return ast.TypeVar(name=name, bound=bound, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def TypeVar(name: str, bound: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
            return ast.TypeVar(name=name, bound=bound, **keywordArguments)
    if sys.version_info >= (3, 13):

        @staticmethod
        def TypeVarTuple(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
            return ast.TypeVarTuple(name=name, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def TypeVarTuple(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
            return ast.TypeVarTuple(name=name, **keywordArguments)

    @staticmethod
    def UnaryOp(op: ast.unaryop, operand: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.UnaryOp:
        return ast.UnaryOp(op=op, operand=operand, **keywordArguments)

    @staticmethod
    def While(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.While:
        return ast.While(test=test, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def With(items: Sequence[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.With:
        return ast.With(items=list(items), body=list(body), **keywordArguments)

    @staticmethod
    def withitem(context_expr: ast.expr, optional_vars: ast.expr | None=None) -> ast.withitem:
        return ast.withitem(context_expr=context_expr, optional_vars=optional_vars)

    @staticmethod
    def Yield(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Yield:
        return ast.Yield(value=value, **keywordArguments)

    @staticmethod
    def YieldFrom(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.YieldFrom:
        return ast.YieldFrom(value=value, **keywordArguments)