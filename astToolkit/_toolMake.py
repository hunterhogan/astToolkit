"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import astDOTTryStar, astDOTParamSpec, astDOTtype_param, astDOTTypeAlias, astDOTTypeVar, astDOTTypeVarTuple
from astToolkit import ast_Identifier, ast_expr_Slice, intORstr, intORstrORtype_params, intORtype_params, str_nameDOTname
from collections.abc import Sequence
from typing import Any, Literal
import ast

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
    def alias(name: ast_Identifier, asName: ast_Identifier | None=None, **keywordArguments: int) -> ast.alias:
        return ast.alias(name, asName, **keywordArguments)

    @staticmethod
    def AnnAssign(target: ast.Name | ast.Attribute | ast.Subscript, annotation: ast.expr, value: ast.expr | None, **keywordArguments: int) -> ast.AnnAssign:
        return ast.AnnAssign(target, annotation, value, **keywordArguments, simple=int(isinstance(target, ast.Name)))

    @staticmethod
    def arg(arg: ast_Identifier, annotation: ast.expr | None, **keywordArguments: intORstr) -> ast.arg:
        return ast.arg(arg, annotation, **keywordArguments)

    @staticmethod
    def arguments(posonlyargs: list[ast.arg]=[], args: list[ast.arg]=[], vararg: ast.arg | None=None, kwonlyargs: list[ast.arg]=[], kw_defaults: Sequence[ast.expr | None]=[None], kwarg: ast.arg | None=None, defaults: Sequence[ast.expr]=[], **keywordArguments: int) -> ast.arguments:
        return ast.arguments(posonlyargs, args, vararg, kwonlyargs, list(kw_defaults), kwarg, list(defaults), **keywordArguments)

    @staticmethod
    def Assert(test: ast.expr, msg: ast.expr | None, **keywordArguments: int) -> ast.Assert:
        return ast.Assert(test, msg, **keywordArguments)

    @staticmethod
    def Assign(targets: Sequence[ast.expr], value: ast.expr, **keywordArguments: intORstr) -> ast.Assign:
        return ast.Assign(list(targets), value, **keywordArguments)

    @staticmethod
    def AsyncFor(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: intORstr) -> ast.AsyncFor:
        return ast.AsyncFor(target, iter, list(body), list(orElse), **keywordArguments)

    @staticmethod
    def AsyncFunctionDef(name: ast_Identifier, args: ast.arguments, body: Sequence[ast.stmt], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, **keywordArguments: intORstrORtype_params) -> ast.AsyncFunctionDef:
        return ast.AsyncFunctionDef(name, args, list(body), list(decorator_list), returns, **keywordArguments)

    @staticmethod
    def AsyncWith(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: intORstr) -> ast.AsyncWith:
        return ast.AsyncWith(items, list(body), **keywordArguments)

    @staticmethod
    def Attribute(value: ast.expr, *attribute: ast_Identifier, context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.Attribute:
        """ If two `ast_Identifier` are joined by a dot `.`, they are _usually_ an `ast.Attribute`, but see `ast.ImportFrom`.
	Parameters:
		value: the part before the dot (e.g., `ast.Name`.)
		attribute: an `ast_Identifier` after a dot `.`; you can pass multiple `attribute` and they will be chained together.
	"""

        def addDOTattribute(chain: ast.expr, identifier: ast_Identifier, context: ast.expr_context, **keywordArguments: int) -> ast.Attribute:
            return ast.Attribute(value=chain, attr=identifier, ctx=context, **keywordArguments)
        buffaloBuffalo = addDOTattribute(value, attribute[0], context, **keywordArguments)
        for identifier in attribute[1:None]:
            buffaloBuffalo = addDOTattribute(buffaloBuffalo, identifier, context, **keywordArguments)
        return buffaloBuffalo

    @staticmethod
    def AugAssign(target: ast.Name | ast.Attribute | ast.Subscript, op: ast.operator, value: ast.expr, **keywordArguments: int) -> ast.AugAssign:
        return ast.AugAssign(target, op, value, **keywordArguments)

    @staticmethod
    def Await(value: ast.expr, **keywordArguments: int) -> ast.Await:
        return ast.Await(value, **keywordArguments)

    @staticmethod
    def BinOp(left: ast.expr, op: ast.operator, right: ast.expr, **keywordArguments: int) -> ast.BinOp:
        return ast.BinOp(left, op, right, **keywordArguments)

    @staticmethod
    def BoolOp(op: ast.boolop, values: Sequence[ast.expr], **keywordArguments: int) -> ast.BoolOp:
        return ast.BoolOp(op, list(values), **keywordArguments)

    @staticmethod
    def Call(callee: ast.expr, args: Sequence[ast.expr]=[], list_keyword: list[ast.keyword]=[], **keywordArguments: int) -> ast.Call:
        return ast.Call(callee, list(args), list_keyword, **keywordArguments)

    @staticmethod
    def ClassDef(name: ast_Identifier, bases: Sequence[ast.expr], list_keyword: list[ast.keyword]=[], body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], **keywordArguments: intORtype_params) -> ast.ClassDef:
        return ast.ClassDef(name, list(bases), list_keyword, list(body), list(decorator_list), **keywordArguments)

    @staticmethod
    def Compare(left: ast.expr, ops: Sequence[ast.cmpop], comparators: Sequence[ast.expr], **keywordArguments: int) -> ast.Compare:
        return ast.Compare(left, list(ops), list(comparators), **keywordArguments)

    @staticmethod
    def comprehension(target: ast.expr, iter: ast.expr, ifs: Sequence[ast.expr], is_async: int, **keywordArguments: int) -> ast.comprehension:
        return ast.comprehension(target, iter, list(ifs), is_async, **keywordArguments)

    @staticmethod
    def Constant(value: Any, **keywordArguments: intORstr) -> ast.Constant:
        return ast.Constant(value, **keywordArguments)

    @staticmethod
    def Delete(targets: Sequence[ast.expr], **keywordArguments: int) -> ast.Delete:
        return ast.Delete(list(targets), **keywordArguments)

    @staticmethod
    def Dict(keys: Sequence[ast.expr | None], values: Sequence[ast.expr], **keywordArguments: int) -> ast.Dict:
        return ast.Dict(list(keys), list(values), **keywordArguments)

    @staticmethod
    def DictComp(key: ast.expr, value: ast.expr, generators: list[ast.comprehension], **keywordArguments: int) -> ast.DictComp:
        return ast.DictComp(key, value, generators, **keywordArguments)

    @staticmethod
    def ExceptHandler(type: ast.expr | None, name: ast_Identifier | None, body: Sequence[ast.stmt], **keywordArguments: int) -> ast.ExceptHandler:
        return ast.ExceptHandler(type, name, list(body), **keywordArguments)

    @staticmethod
    def Expr(value: ast.expr, **keywordArguments: int) -> ast.Expr:
        return ast.Expr(value, **keywordArguments)

    @staticmethod
    def Expression(body: ast.expr) -> ast.Expression:
        return ast.Expression(body)

    @staticmethod
    def For(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: intORstr) -> ast.For:
        return ast.For(target, iter, list(body), list(orElse), **keywordArguments)

    @staticmethod
    def FormattedValue(value: ast.expr, conversion: int, format_spec: ast.expr | None, **keywordArguments: int) -> ast.FormattedValue:
        return ast.FormattedValue(value, conversion, format_spec, **keywordArguments)

    @staticmethod
    def FunctionDef(name: ast_Identifier, args: ast.arguments, body: Sequence[ast.stmt], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, **keywordArguments: intORstrORtype_params) -> ast.FunctionDef:
        return ast.FunctionDef(name, args, list(body), list(decorator_list), returns, **keywordArguments)

    @staticmethod
    def FunctionType(argtypes: Sequence[ast.expr], returns: ast.expr) -> ast.FunctionType:
        return ast.FunctionType(list(argtypes), returns)

    @staticmethod
    def GeneratorExp(elt: ast.expr, generators: list[ast.comprehension], **keywordArguments: int) -> ast.GeneratorExp:
        return ast.GeneratorExp(elt, generators, **keywordArguments)

    @staticmethod
    def Global(names: list[ast_Identifier], **keywordArguments: int) -> ast.Global:
        return ast.Global(names, **keywordArguments)

    @staticmethod
    def If(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: int) -> ast.If:
        return ast.If(test, list(body), list(orElse), **keywordArguments)

    @staticmethod
    def IfExp(test: ast.expr, body: ast.expr, orElse: ast.expr, **keywordArguments: int) -> ast.IfExp:
        return ast.IfExp(test, body, orElse, **keywordArguments)

    @staticmethod
    def Import(moduleWithLogicalPath: str_nameDOTname, asName: ast_Identifier | None=None, **keywordArguments: int) -> ast.Import:
        return ast.Import(names=[Make.alias(moduleWithLogicalPath, asName)], **keywordArguments)

    @staticmethod
    def ImportFrom(module: ast_Identifier | None, list_alias: list[ast.alias], **keywordArguments: int) -> ast.ImportFrom:
        return ast.ImportFrom(module, list_alias, **keywordArguments, level=0)

    @staticmethod
    def Interactive(body: Sequence[ast.stmt]) -> ast.Interactive:
        return ast.Interactive(list(body))

    @staticmethod
    def JoinedStr(values: Sequence[ast.expr], **keywordArguments: int) -> ast.JoinedStr:
        return ast.JoinedStr(list(values), **keywordArguments)

    @staticmethod
    def keyword(arg: ast_Identifier | None, value: ast.expr, **keywordArguments: int) -> ast.keyword:
        return ast.keyword(arg, value, **keywordArguments)

    @staticmethod
    def Lambda(args: ast.arguments, body: ast.expr, **keywordArguments: int) -> ast.Lambda:
        return ast.Lambda(args, body, **keywordArguments)

    @staticmethod
    def List(elts: Sequence[ast.expr], context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.List:
        return ast.List(list(elts), context, **keywordArguments)

    @staticmethod
    def ListComp(elt: ast.expr, generators: list[ast.comprehension], **keywordArguments: int) -> ast.ListComp:
        return ast.ListComp(elt, generators, **keywordArguments)

    @staticmethod
    def Match(subject: ast.expr, cases: list[ast.match_case], **keywordArguments: int) -> ast.Match:
        return ast.Match(subject, cases, **keywordArguments)

    @staticmethod
    def match_case(pattern: ast.pattern, guard: ast.expr | None, body: Sequence[ast.stmt], **keywordArguments: int) -> ast.match_case:
        return ast.match_case(pattern, guard, list(body), **keywordArguments)

    @staticmethod
    def MatchAs(pattern: ast.pattern | None, name: ast_Identifier | None, **keywordArguments: int) -> ast.MatchAs:
        return ast.MatchAs(pattern, name, **keywordArguments)

    @staticmethod
    def MatchClass(cls: ast.expr, patterns: Sequence[ast.pattern], kwd_attrs: list[ast_Identifier], kwd_patterns: Sequence[ast.pattern], **keywordArguments: int) -> ast.MatchClass:
        return ast.MatchClass(cls, list(patterns), kwd_attrs, list(kwd_patterns), **keywordArguments)

    @staticmethod
    def MatchMapping(keys: Sequence[ast.expr], patterns: Sequence[ast.pattern], rest: ast_Identifier | None, **keywordArguments: int) -> ast.MatchMapping:
        return ast.MatchMapping(list(keys), list(patterns), rest, **keywordArguments)

    @staticmethod
    def MatchOr(patterns: Sequence[ast.pattern], **keywordArguments: int) -> ast.MatchOr:
        return ast.MatchOr(list(patterns), **keywordArguments)

    @staticmethod
    def MatchSequence(patterns: Sequence[ast.pattern], **keywordArguments: int) -> ast.MatchSequence:
        return ast.MatchSequence(list(patterns), **keywordArguments)

    @staticmethod
    def MatchSingleton(value: Literal[True, False] | None, **keywordArguments: int) -> ast.MatchSingleton:
        return ast.MatchSingleton(value, **keywordArguments)

    @staticmethod
    def MatchStar(name: ast_Identifier | None, **keywordArguments: int) -> ast.MatchStar:
        return ast.MatchStar(name, **keywordArguments)

    @staticmethod
    def MatchValue(value: ast.expr, **keywordArguments: int) -> ast.MatchValue:
        return ast.MatchValue(value, **keywordArguments)

    @staticmethod
    def Module(body: Sequence[ast.stmt], type_ignores: list[ast.TypeIgnore]=[]) -> ast.Module:
        return ast.Module(list(body), type_ignores)

    @staticmethod
    def Name(id: ast_Identifier, context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.Name:
        return ast.Name(id, context, **keywordArguments)

    @staticmethod
    def NamedExpr(target: ast.Name, value: ast.expr, **keywordArguments: int) -> ast.NamedExpr:
        return ast.NamedExpr(target, value, **keywordArguments)

    @staticmethod
    def Nonlocal(names: list[ast_Identifier], **keywordArguments: int) -> ast.Nonlocal:
        return ast.Nonlocal(names, **keywordArguments)

    @staticmethod
    def ParamSpec(name: ast_Identifier, default_value: ast.expr | None, **keywordArguments: int) -> astDOTParamSpec:
        return astDOTParamSpec(name, default_value, **keywordArguments)

    @staticmethod
    def Raise(exc: ast.expr | None, cause: ast.expr | None, **keywordArguments: int) -> ast.Raise:
        return ast.Raise(exc, cause, **keywordArguments)

    @staticmethod
    def Return(value: ast.expr | None, **keywordArguments: int) -> ast.Return:
        return ast.Return(value, **keywordArguments)

    @staticmethod
    def Set(elts: Sequence[ast.expr], **keywordArguments: int) -> ast.Set:
        return ast.Set(list(elts), **keywordArguments)

    @staticmethod
    def SetComp(elt: ast.expr, generators: list[ast.comprehension], **keywordArguments: int) -> ast.SetComp:
        return ast.SetComp(elt, generators, **keywordArguments)

    @staticmethod
    def Slice(lower: ast.expr | None, upper: ast.expr | None, step: ast.expr | None, **keywordArguments: int) -> ast.Slice:
        return ast.Slice(lower, upper, step, **keywordArguments)

    @staticmethod
    def Starred(value: ast.expr, context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.Starred:
        return ast.Starred(value, context, **keywordArguments)

    @staticmethod
    def Subscript(value: ast.expr, slice: ast_expr_Slice, context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.Subscript:
        return ast.Subscript(value, slice, context, **keywordArguments)

    @staticmethod
    def Try(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt], finalbody: Sequence[ast.stmt]=[], **keywordArguments: int) -> ast.Try:
        return ast.Try(list(body), handlers, list(orElse), list(finalbody), **keywordArguments)

    @staticmethod
    def TryStar(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt], finalbody: Sequence[ast.stmt]=[], **keywordArguments: int) -> astDOTTryStar:
        return astDOTTryStar(list(body), handlers, list(orElse), list(finalbody), **keywordArguments)

    @staticmethod
    def Tuple(elts: Sequence[ast.expr], context: ast.expr_context=ast.Load(), **keywordArguments: int) -> ast.Tuple:
        return ast.Tuple(list(elts), context, **keywordArguments)

    @staticmethod
    def TypeAlias(name: ast.Name, type_params: Sequence[astDOTtype_param], value: ast.expr, **keywordArguments: int) -> astDOTTypeAlias:
        return astDOTTypeAlias(name, list(type_params), value, **keywordArguments)

    @staticmethod
    def TypeIgnore(lineno: int, tag: ast_Identifier, **keywordArguments: int) -> ast.TypeIgnore:
        return ast.TypeIgnore(lineno, tag, **keywordArguments)

    @staticmethod
    def TypeVar(name: ast_Identifier, bound: ast.expr | None, default_value: ast.expr | None, **keywordArguments: int) -> astDOTTypeVar:
        return astDOTTypeVar(name, bound, default_value, **keywordArguments)

    @staticmethod
    def TypeVarTuple(name: ast_Identifier, default_value: ast.expr | None, **keywordArguments: int) -> astDOTTypeVarTuple:
        return astDOTTypeVarTuple(name, default_value, **keywordArguments)

    @staticmethod
    def UnaryOp(op: ast.unaryop, operand: ast.expr, **keywordArguments: int) -> ast.UnaryOp:
        return ast.UnaryOp(op, operand, **keywordArguments)

    @staticmethod
    def While(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: int) -> ast.While:
        return ast.While(test, list(body), list(orElse), **keywordArguments)

    @staticmethod
    def With(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: intORstr) -> ast.With:
        return ast.With(items, list(body), **keywordArguments)

    @staticmethod
    def withitem(context_expr: ast.expr, optional_vars: ast.expr | None, **keywordArguments: int) -> ast.withitem:
        return ast.withitem(context_expr, optional_vars, **keywordArguments)

    @staticmethod
    def Yield(value: ast.expr | None, **keywordArguments: int) -> ast.Yield:
        return ast.Yield(value, **keywordArguments)

    @staticmethod
    def YieldFrom(value: ast.expr, **keywordArguments: int) -> ast.YieldFrom:
        return ast.YieldFrom(value, **keywordArguments)