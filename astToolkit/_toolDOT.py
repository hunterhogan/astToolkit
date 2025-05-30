# pyright: reportReturnType=false
# ruff: noqa: F403, F405
"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit._astTypes import *
from collections.abc import Sequence
from typing import overload
import ast
import sys

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
    def annotation(node: hasDOTannotation_exprOrNone) -> ast.expr:
        ...

    @staticmethod
    def annotation(node: hasDOTannotation) -> ast.expr:
        return node.annotation

    @staticmethod
    @overload
    def arg(node: hasDOTarg_str) -> str:
        ...

    @staticmethod
    @overload
    def arg(node: hasDOTarg_strOrNone) -> str:
        ...

    @staticmethod
    def arg(node: hasDOTarg) -> str:
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
    def asname(node: hasDOTasname) -> str:
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
    def bound(node: hasDOTbound) -> ast.expr:
        return node.bound

    @staticmethod
    def cases(node: hasDOTcases) -> Sequence[ast.match_case]:
        return node.cases

    @staticmethod
    def cause(node: hasDOTcause) -> ast.expr:
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
        def default_value(node: hasDOTdefault_value) -> ast.expr:
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
    def exc(node: hasDOTexc) -> ast.expr:
        return node.exc

    @staticmethod
    def finalbody(node: hasDOTfinalbody) -> Sequence[ast.stmt]:
        return node.finalbody

    @staticmethod
    def format_spec(node: hasDOTformat_spec) -> ast.expr:
        return node.format_spec

    @staticmethod
    def func(node: hasDOTfunc) -> ast.expr:
        return node.func

    @staticmethod
    def generators(node: hasDOTgenerators) -> Sequence[ast.comprehension]:
        return node.generators

    @staticmethod
    def guard(node: hasDOTguard) -> ast.expr:
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
    def items(node: hasDOTitems) -> Sequence[ast.withitem]:
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
    def keys(node: hasDOTkeys_list_exprOrNone) -> Sequence[ast.expr]:
        ...

    @staticmethod
    def keys(node: hasDOTkeys) -> Sequence[ast.expr]:
        return node.keys

    @staticmethod
    def keywords(node: hasDOTkeywords) -> Sequence[ast.keyword]:
        return node.keywords

    @staticmethod
    def kind(node: hasDOTkind) -> str:
        return node.kind

    @staticmethod
    def kw_defaults(node: hasDOTkw_defaults) -> Sequence[ast.expr]:
        return node.kw_defaults

    @staticmethod
    def kwarg(node: hasDOTkwarg) -> ast.arg:
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
    def lower(node: hasDOTlower) -> ast.expr:
        return node.lower

    @staticmethod
    def module(node: hasDOTmodule) -> str:
        return node.module

    @staticmethod
    def msg(node: hasDOTmsg) -> ast.expr:
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
    def name(node: hasDOTname_strOrNone) -> str:
        ...

    @staticmethod
    def name(node: hasDOTname) -> ast.Name | str:
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
    def optional_vars(node: hasDOToptional_vars) -> ast.expr:
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
    def pattern(node: hasDOTpattern_patternOrNone) -> ast.pattern:
        ...

    @staticmethod
    def pattern(node: hasDOTpattern) -> ast.pattern:
        return node.pattern

    @staticmethod
    def patterns(node: hasDOTpatterns) -> Sequence[ast.pattern]:
        return node.patterns

    @staticmethod
    def posonlyargs(node: hasDOTposonlyargs) -> list[ast.arg]:
        return node.posonlyargs

    @staticmethod
    def rest(node: hasDOTrest) -> str:
        return node.rest

    @staticmethod
    @overload
    def returns(node: hasDOTreturns_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def returns(node: hasDOTreturns_exprOrNone) -> ast.expr:
        ...

    @staticmethod
    def returns(node: hasDOTreturns) -> ast.expr:
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
    def step(node: hasDOTstep) -> ast.expr:
        return node.step

    @staticmethod
    def subject(node: hasDOTsubject) -> ast.expr:
        return node.subject

    @staticmethod
    def tag(node: hasDOTtag) -> str:
        return node.tag

    @staticmethod
    @overload
    def target(node: hasDOTtarget_Name) -> ast.Name:
        ...

    @staticmethod
    @overload
    def target(node: hasDOTtarget_NameOrAttributeOrSubscript) -> ast.Name | ast.Attribute | ast.Subscript:
        ...

    @staticmethod
    @overload
    def target(node: hasDOTtarget_expr) -> ast.expr:
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
    def type(node: hasDOTtype) -> ast.expr:
        return node.type

    @staticmethod
    def type_comment(node: hasDOTtype_comment) -> str:
        return node.type_comment

    @staticmethod
    def type_ignores(node: hasDOTtype_ignores) -> list[ast.TypeIgnore]:
        return node.type_ignores

    @staticmethod
    def type_params(node: hasDOTtype_params) -> Sequence[ast.type_param]:
        return node.type_params

    @staticmethod
    def upper(node: hasDOTupper) -> ast.expr:
        return node.upper

    @staticmethod
    @overload
    def value(node: hasDOTvalue_ConstantValueType) -> ConstantValueType:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_boolOrNone) -> bool:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_expr) -> ast.expr:
        ...

    @staticmethod
    @overload
    def value(node: hasDOTvalue_exprOrNone) -> ast.expr:
        ...

    @staticmethod
    def value(node: hasDOTvalue) -> ast.expr | bool | ConstantValueType:
        return node.value

    @staticmethod
    def values(node: hasDOTvalues) -> Sequence[ast.expr]:
        return node.values

    @staticmethod
    def vararg(node: hasDOTvararg) -> ast.arg:
        return node.vararg