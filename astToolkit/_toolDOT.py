"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import (
	ConstantValueType, hasDOTannotation, hasDOTannotation_expr, hasDOTannotation_exprOrNone, hasDOTarg, hasDOTarg_str,
	hasDOTarg_strOrNone, hasDOTargs, hasDOTargs_arguments, hasDOTargs_list_arg, hasDOTargs_list_expr, hasDOTargtypes,
	hasDOTasname, hasDOTattr, hasDOTbases, hasDOTbody, hasDOTbody_expr, hasDOTbody_list_stmt, hasDOTbound, hasDOTcases,
	hasDOTcause, hasDOTcls, hasDOTcomparators, hasDOTcontext_expr, hasDOTconversion, hasDOTctx, hasDOTdecorator_list,
	hasDOTdefaults, hasDOTelt, hasDOTelts, hasDOTexc, hasDOTfinalbody, hasDOTformat_spec, hasDOTfunc, hasDOTgenerators,
	hasDOTguard, hasDOThandlers, hasDOTid, hasDOTifs, hasDOTis_async, hasDOTitems, hasDOTiter, hasDOTkey, hasDOTkeys,
	hasDOTkeys_list_expr, hasDOTkeys_list_exprOrNone, hasDOTkeywords, hasDOTkind, hasDOTkw_defaults, hasDOTkwarg,
	hasDOTkwd_attrs, hasDOTkwd_patterns, hasDOTkwonlyargs, hasDOTleft, hasDOTlevel, hasDOTlineno, hasDOTlower,
	hasDOTmodule, hasDOTmsg, hasDOTname, hasDOTname_Name, hasDOTname_str, hasDOTname_strOrNone, hasDOTnames,
	hasDOTnames_list_alias, hasDOTnames_list_str, hasDOTop, hasDOTop_boolop, hasDOTop_operator, hasDOTop_unaryop,
	hasDOToperand, hasDOTops, hasDOToptional_vars, hasDOTorelse, hasDOTorelse_expr, hasDOTorelse_list_stmt, hasDOTpattern,
	hasDOTpattern_pattern, hasDOTpattern_patternOrNone, hasDOTpatterns, hasDOTposonlyargs, hasDOTrest, hasDOTreturns,
	hasDOTreturns_expr, hasDOTreturns_exprOrNone, hasDOTright, hasDOTsimple, hasDOTslice, hasDOTstep, hasDOTsubject,
	hasDOTtag, hasDOTtarget, hasDOTtarget_expr, hasDOTtarget_Name, hasDOTtarget_NameOrAttributeOrSubscript, hasDOTtargets,
	hasDOTtest, hasDOTtype, hasDOTtype_comment, hasDOTtype_ignores, hasDOTtype_params, hasDOTupper, hasDOTvalue,
	hasDOTvalue_boolOrNone, hasDOTvalue_ConstantValueType, hasDOTvalue_expr, hasDOTvalue_exprOrNone, hasDOTvalues,
	hasDOTvararg,
)
from collections.abc import Sequence
from typing import overload
import ast
import sys

if sys.version_info >= (3, 13):
    from astToolkit import hasDOTdefault_value as hasDOTdefault_value

class DOT:
    """
    Access attributes and sub-nodes of AST elements via consistent accessor methods.

    The DOT class provides static methods to access specific attributes of different types of AST nodes in a consistent
    way. This simplifies attribute access across various node types and improves code readability by abstracting the
    underlying AST structure details.

    DOT is designed for safe, read-only access to node properties, unlike the grab class which is designed for modifying
    node attributes.
    """

    @staticmethod
    @overload
    def annotation(node: hasDOTannotation_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def annotation(node: hasDOTannotation_exprOrNone) -> ast.expr | None:
        ...

    @staticmethod
    def annotation(node: hasDOTannotation) -> ast.expr | (ast.expr | None):
        return node.annotation

    @staticmethod
    @overload
    def arg(node: hasDOTarg_str) -> str:
        ...

    @staticmethod
    @overload
    def arg(node: hasDOTarg_strOrNone) -> str | None:
        ...

    @staticmethod
    def arg(node: hasDOTarg) -> str | (str | None):
        return node.arg

    @staticmethod
    @overload
    def args(node: hasDOTargs_arguments) -> ast.arguments:
        ...

    @staticmethod
    @overload
    def args(node: hasDOTargs_list_arg) -> list[ast.arg]:
        ...

    @staticmethod
    @overload
    def args(node: hasDOTargs_list_expr) -> Sequence[ast.expr]:
        ...

    @staticmethod
    def args(node: hasDOTargs) -> ast.arguments | list[ast.arg] | Sequence[ast.expr]:
        return node.args

    @staticmethod
    def argtypes(node: hasDOTargtypes) -> Sequence[ast.expr]:
        return node.argtypes

    @staticmethod
    def asname(node: hasDOTasname) -> str | None:
        return node.asname

    @staticmethod
    def attr(node: hasDOTattr) -> str:
        return node.attr

    @staticmethod
    def bases(node: hasDOTbases) -> Sequence[ast.expr]:
        return node.bases

    @staticmethod
    @overload
    def body(node: hasDOTbody_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def body(node: hasDOTbody_list_stmt) -> Sequence[ast.stmt]:
        ...

    @staticmethod
    def body(node: hasDOTbody) -> ast.expr | Sequence[ast.stmt]:
        return node.body

    @staticmethod
    def bound(node: hasDOTbound) -> ast.expr | None:
        return node.bound

    @staticmethod
    def cases(node: hasDOTcases) -> list[ast.match_case]:
        return node.cases

    @staticmethod
    def cause(node: hasDOTcause) -> ast.expr | None:
        return node.cause

    @staticmethod
    def cls(node: hasDOTcls) -> ast.expr:
        return node.cls

    @staticmethod
    def comparators(node: hasDOTcomparators) -> Sequence[ast.expr]:
        return node.comparators

    @staticmethod
    def context_expr(node: hasDOTcontext_expr) -> ast.expr:
        return node.context_expr

    @staticmethod
    def conversion(node: hasDOTconversion) -> int:
        return node.conversion

    @staticmethod
    def ctx(node: hasDOTctx) -> ast.expr_context:
        return node.ctx

    @staticmethod
    def decorator_list(node: hasDOTdecorator_list) -> Sequence[ast.expr]:
        return node.decorator_list
    if sys.version_info >= (3, 13):

        @staticmethod
        def default_value(node: hasDOTdefault_value) -> ast.expr | None:
            return node.default_value

    @staticmethod
    def defaults(node: hasDOTdefaults) -> Sequence[ast.expr]:
        return node.defaults

    @staticmethod
    def elt(node: hasDOTelt) -> ast.expr:
        return node.elt

    @staticmethod
    def elts(node: hasDOTelts) -> Sequence[ast.expr]:
        return node.elts

    @staticmethod
    def exc(node: hasDOTexc) -> ast.expr | None:
        return node.exc

    @staticmethod
    def finalbody(node: hasDOTfinalbody) -> Sequence[ast.stmt]:
        return node.finalbody

    @staticmethod
    def format_spec(node: hasDOTformat_spec) -> ast.expr | None:
        return node.format_spec

    @staticmethod
    def func(node: hasDOTfunc) -> ast.expr:
        return node.func

    @staticmethod
    def generators(node: hasDOTgenerators) -> list[ast.comprehension]:
        return node.generators

    @staticmethod
    def guard(node: hasDOTguard) -> ast.expr | None:
        return node.guard

    @staticmethod
    def handlers(node: hasDOThandlers) -> list[ast.ExceptHandler]:
        return node.handlers

    @staticmethod
    def id(node: hasDOTid) -> str:
        return node.id

    @staticmethod
    def ifs(node: hasDOTifs) -> Sequence[ast.expr]:
        return node.ifs

    @staticmethod
    def is_async(node: hasDOTis_async) -> int:
        return node.is_async

    @staticmethod
    def items(node: hasDOTitems) -> list[ast.withitem]:
        return node.items

    @staticmethod
    def iter(node: hasDOTiter) -> ast.expr:
        return node.iter

    @staticmethod
    def key(node: hasDOTkey) -> ast.expr:
        return node.key

    @staticmethod
    @overload
    def keys(node: hasDOTkeys_list_expr) -> Sequence[ast.expr]:
        ...

    @staticmethod
    @overload
    def keys(node: hasDOTkeys_list_exprOrNone) -> Sequence[ast.expr | None]:
        ...

    @staticmethod
    def keys(node: hasDOTkeys) -> Sequence[ast.expr | None] | Sequence[ast.expr]:
        return node.keys

    @staticmethod
    def keywords(node: hasDOTkeywords) -> list[ast.keyword]:
        return node.keywords

    @staticmethod
    def kind(node: hasDOTkind) -> str | None:
        return node.kind

    @staticmethod
    def kw_defaults(node: hasDOTkw_defaults) -> Sequence[ast.expr | None]:
        return node.kw_defaults

    @staticmethod
    def kwarg(node: hasDOTkwarg) -> ast.arg | None:
        return node.kwarg

    @staticmethod
    def kwd_attrs(node: hasDOTkwd_attrs) -> list[str]:
        return node.kwd_attrs

    @staticmethod
    def kwd_patterns(node: hasDOTkwd_patterns) -> Sequence[ast.pattern]:
        return node.kwd_patterns

    @staticmethod
    def kwonlyargs(node: hasDOTkwonlyargs) -> list[ast.arg]:
        return node.kwonlyargs

    @staticmethod
    def left(node: hasDOTleft) -> ast.expr:
        return node.left

    @staticmethod
    def level(node: hasDOTlevel) -> int:
        return node.level

    @staticmethod
    def lineno(node: hasDOTlineno) -> int:
        return node.lineno

    @staticmethod
    def lower(node: hasDOTlower) -> ast.expr | None:
        return node.lower

    @staticmethod
    def module(node: hasDOTmodule) -> str | None:
        return node.module

    @staticmethod
    def msg(node: hasDOTmsg) -> ast.expr | None:
        return node.msg

    @staticmethod
    @overload
    def name(node: hasDOTname_Name) -> ast.Name:
        ...

    @staticmethod
    @overload
    def name(node: hasDOTname_str) -> str:
        ...

    @staticmethod
    @overload
    def name(node: hasDOTname_strOrNone) -> str | None:
        ...

    @staticmethod
    def name(node: hasDOTname) -> ast.Name | str | (str | None):
        return node.name

    @staticmethod
    @overload
    def names(node: hasDOTnames_list_alias) -> list[ast.alias]:
        ...

    @staticmethod
    @overload
    def names(node: hasDOTnames_list_str) -> list[str]:
        ...

    @staticmethod
    def names(node: hasDOTnames) -> list[ast.alias] | list[str]:
        return node.names

    @staticmethod
    @overload
    def op(node: hasDOTop_boolop) -> ast.boolop:
        ...

    @staticmethod
    @overload
    def op(node: hasDOTop_operator) -> ast.operator:
        ...

    @staticmethod
    @overload
    def op(node: hasDOTop_unaryop) -> ast.unaryop:
        ...

    @staticmethod
    def op(node: hasDOTop) -> ast.boolop | ast.operator | ast.unaryop:
        return node.op

    @staticmethod
    def operand(node: hasDOToperand) -> ast.expr:
        return node.operand

    @staticmethod
    def ops(node: hasDOTops) -> Sequence[ast.cmpop]:
        return node.ops

    @staticmethod
    def optional_vars(node: hasDOToptional_vars) -> ast.expr | None:
        return node.optional_vars

    @staticmethod
    @overload
    def orelse(node: hasDOTorelse_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def orelse(node: hasDOTorelse_list_stmt) -> Sequence[ast.stmt]:
        ...

    @staticmethod
    def orelse(node: hasDOTorelse) -> ast.expr | Sequence[ast.stmt]:
        return node.orelse

    @staticmethod
    @overload
    def pattern(node: hasDOTpattern_pattern) -> ast.pattern:
        ...

    @staticmethod
    @overload
    def pattern(node: hasDOTpattern_patternOrNone) -> ast.pattern | None:
        ...

    @staticmethod
    def pattern(node: hasDOTpattern) -> ast.pattern | (ast.pattern | None):
        return node.pattern

    @staticmethod
    def patterns(node: hasDOTpatterns) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def posonlyargs(node: hasDOTposonlyargs) -> list[ast.arg]:
        return node.posonlyargs

    @staticmethod
    def rest(node: hasDOTrest) -> str | None:
        return node.rest

    @staticmethod
    @overload
    def returns(node: hasDOTreturns_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def returns(node: hasDOTreturns_exprOrNone) -> ast.expr | None:
        ...

    @staticmethod
    def returns(node: hasDOTreturns) -> ast.expr | (ast.expr | None):
        return node.returns

    @staticmethod
    def right(node: hasDOTright) -> ast.expr:
        return node.right

    @staticmethod
    def simple(node: hasDOTsimple) -> int:
        return node.simple

    @staticmethod
    def slice(node: hasDOTslice) -> ast.expr:
        return node.slice

    @staticmethod
    def step(node: hasDOTstep) -> ast.expr | None:
        return node.step

    @staticmethod
    def subject(node: hasDOTsubject) -> ast.expr:
        return node.subject

    @staticmethod
    def tag(node: hasDOTtag) -> str:
        return node.tag

    @staticmethod
    @overload
    def target(node: hasDOTtarget_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def target(node: hasDOTtarget_Name) -> ast.Name:
        ...

    @staticmethod
    @overload
    def target(node: hasDOTtarget_NameOrAttributeOrSubscript) -> ast.Name | ast.Attribute | ast.Subscript:
        ...

    @staticmethod
    def target(node: hasDOTtarget) -> ast.expr | ast.Name | (ast.Name | ast.Attribute | ast.Subscript):
        return node.target

    @staticmethod
    def targets(node: hasDOTtargets) -> Sequence[ast.expr]:
        return node.targets

    @staticmethod
    def test(node: hasDOTtest) -> ast.expr:
        return node.test

    @staticmethod
    def type(node: hasDOTtype) -> ast.expr | None:
        return node.type

    @staticmethod
    def type_comment(node: hasDOTtype_comment) -> str | None:
        return node.type_comment

    @staticmethod
    def type_ignores(node: hasDOTtype_ignores) -> list[ast.TypeIgnore]:
        return node.type_ignores

    @staticmethod
    def type_params(node: hasDOTtype_params) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def upper(node: hasDOTupper) -> ast.expr | None:
        return node.upper

    @staticmethod
    @overload
    def value(node: hasDOTvalue_boolOrNone) -> bool | None:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_ConstantValueType) -> ConstantValueType:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_exprOrNone) -> ast.expr | None:
        ...

    @staticmethod
    def value(node: hasDOTvalue) -> ast.expr | (ast.expr | None) | (bool | None) | ConstantValueType:
        return node.value

    @staticmethod
    def values(node: hasDOTvalues) -> Sequence[ast.expr]:
        return node.values

    @staticmethod
    def vararg(node: hasDOTvararg) -> ast.arg | None:
        return node.vararg