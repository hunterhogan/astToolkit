# ruff: noqa: F403, F405
"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit._astTypes import *
from collections.abc import Callable, Sequence
from astToolkit import ast_Identifier, ast_expr_Slice, astDOTtype_param, DOT
from typing import Any, Literal, overload
import ast

class ClassIsAndAttribute:

    @staticmethod
    def annotationIs(astClass: type[hasDOTannotation], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.annotation(node))
        return workhorse

    @staticmethod
    def argIs(astClass: type[hasDOTarg], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.arg(node))
        return workhorse

    @staticmethod
    def argsIs(astClass: type[hasDOTargs], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.args(node))
        return workhorse

    @staticmethod
    def argtypesIs(astClass: type[hasDOTargtypes], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.argtypes(node))
        return workhorse

    @staticmethod
    def asnameIs(astClass: type[hasDOTasname], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.asname(node))
        return workhorse

    @staticmethod
    def attrIs(astClass: type[hasDOTattr], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.attr(node))
        return workhorse

    @staticmethod
    def basesIs(astClass: type[hasDOTbases], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.bases(node))
        return workhorse

    @staticmethod
    def bodyIs(astClass: type[hasDOTbody], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.body(node))
        return workhorse

    @staticmethod
    def boundIs(astClass: type[hasDOTbound], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.bound(node))
        return workhorse

    @staticmethod
    def casesIs(astClass: type[hasDOTcases], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.cases(node))
        return workhorse

    @staticmethod
    def causeIs(astClass: type[hasDOTcause], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.cause(node))
        return workhorse

    @staticmethod
    def clsIs(astClass: type[hasDOTcls], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.cls(node))
        return workhorse

    @staticmethod
    def comparatorsIs(astClass: type[hasDOTcomparators], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.comparators(node))
        return workhorse

    @staticmethod
    def context_exprIs(astClass: type[hasDOTcontext_expr], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.context_expr(node))
        return workhorse

    @staticmethod
    def conversionIs(astClass: type[hasDOTconversion], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.conversion(node))
        return workhorse

    @staticmethod
    def ctxIs(astClass: type[hasDOTctx], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.ctx(node))
        return workhorse

    @staticmethod
    def decorator_listIs(astClass: type[hasDOTdecorator_list], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.decorator_list(node))
        return workhorse

    @staticmethod
    def default_valueIs(astClass: type[hasDOTdefault_value], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.default_value(node))
        return workhorse

    @staticmethod
    def defaultsIs(astClass: type[hasDOTdefaults], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.defaults(node))
        return workhorse

    @staticmethod
    def eltIs(astClass: type[hasDOTelt], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.elt(node))
        return workhorse

    @staticmethod
    def eltsIs(astClass: type[hasDOTelts], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.elts(node))
        return workhorse

    @staticmethod
    def excIs(astClass: type[hasDOTexc], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.exc(node))
        return workhorse

    @staticmethod
    def finalbodyIs(astClass: type[hasDOTfinalbody], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.finalbody(node))
        return workhorse

    @staticmethod
    def format_specIs(astClass: type[hasDOTformat_spec], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.format_spec(node))
        return workhorse

    @staticmethod
    def funcIs(astClass: type[hasDOTfunc], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.func(node))
        return workhorse

    @staticmethod
    def generatorsIs(astClass: type[hasDOTgenerators], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.generators(node))
        return workhorse

    @staticmethod
    def guardIs(astClass: type[hasDOTguard], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.guard(node))
        return workhorse

    @staticmethod
    def handlersIs(astClass: type[hasDOThandlers], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.handlers(node))
        return workhorse

    @staticmethod
    def idIs(astClass: type[hasDOTid], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.id(node))
        return workhorse

    @staticmethod
    def ifsIs(astClass: type[hasDOTifs], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.ifs(node))
        return workhorse

    @staticmethod
    def is_asyncIs(astClass: type[hasDOTis_async], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.is_async(node))
        return workhorse

    @staticmethod
    def itemsIs(astClass: type[hasDOTitems], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.items(node))
        return workhorse

    @staticmethod
    def iterIs(astClass: type[hasDOTiter], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.iter(node))
        return workhorse

    @staticmethod
    def keyIs(astClass: type[hasDOTkey], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.key(node))
        return workhorse

    @staticmethod
    def keysIs(astClass: type[hasDOTkeys], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.keys(node))
        return workhorse

    @staticmethod
    def keywordsIs(astClass: type[hasDOTkeywords], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.keywords(node))
        return workhorse

    @staticmethod
    def kindIs(astClass: type[hasDOTkind], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kind(node))
        return workhorse

    @staticmethod
    def kw_defaultsIs(astClass: type[hasDOTkw_defaults], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kw_defaults(node))
        return workhorse

    @staticmethod
    def kwargIs(astClass: type[hasDOTkwarg], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kwarg(node))
        return workhorse

    @staticmethod
    def kwd_attrsIs(astClass: type[hasDOTkwd_attrs], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kwd_attrs(node))
        return workhorse

    @staticmethod
    def kwd_patternsIs(astClass: type[hasDOTkwd_patterns], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kwd_patterns(node))
        return workhorse

    @staticmethod
    def kwonlyargsIs(astClass: type[hasDOTkwonlyargs], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.kwonlyargs(node))
        return workhorse

    @staticmethod
    def leftIs(astClass: type[hasDOTleft], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.left(node))
        return workhorse

    @staticmethod
    def levelIs(astClass: type[hasDOTlevel], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.level(node))
        return workhorse

    @staticmethod
    def linenoIs(astClass: type[hasDOTlineno], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.lineno(node))
        return workhorse

    @staticmethod
    def lowerIs(astClass: type[hasDOTlower], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.lower(node))
        return workhorse

    @staticmethod
    def moduleIs(astClass: type[hasDOTmodule], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.module(node))
        return workhorse

    @staticmethod
    def msgIs(astClass: type[hasDOTmsg], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.msg(node))
        return workhorse

    @staticmethod
    def nameIs(astClass: type[hasDOTname], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.name(node))
        return workhorse

    @staticmethod
    def namesIs(astClass: type[hasDOTnames], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.names(node))
        return workhorse

    @staticmethod
    def opIs(astClass: type[hasDOTop], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.op(node))
        return workhorse

    @staticmethod
    def operandIs(astClass: type[hasDOToperand], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.operand(node))
        return workhorse

    @staticmethod
    def opsIs(astClass: type[hasDOTops], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.ops(node))
        return workhorse

    @staticmethod
    def optional_varsIs(astClass: type[hasDOToptional_vars], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.optional_vars(node))
        return workhorse

    @staticmethod
    def orelseIs(astClass: type[hasDOTorelse], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.orelse(node))
        return workhorse

    @staticmethod
    def patternIs(astClass: type[hasDOTpattern], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.pattern(node))
        return workhorse

    @staticmethod
    def patternsIs(astClass: type[hasDOTpatterns], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.patterns(node))
        return workhorse

    @staticmethod
    def posonlyargsIs(astClass: type[hasDOTposonlyargs], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.posonlyargs(node))
        return workhorse

    @staticmethod
    def restIs(astClass: type[hasDOTrest], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.rest(node))
        return workhorse

    @staticmethod
    def returnsIs(astClass: type[hasDOTreturns], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.returns(node))
        return workhorse

    @staticmethod
    def rightIs(astClass: type[hasDOTright], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.right(node))
        return workhorse

    @staticmethod
    def simpleIs(astClass: type[hasDOTsimple], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.simple(node))
        return workhorse

    @staticmethod
    def sliceIs(astClass: type[hasDOTslice], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.slice(node))
        return workhorse

    @staticmethod
    def stepIs(astClass: type[hasDOTstep], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.step(node))
        return workhorse

    @staticmethod
    def subjectIs(astClass: type[hasDOTsubject], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.subject(node))
        return workhorse

    @staticmethod
    def tagIs(astClass: type[hasDOTtag], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.tag(node))
        return workhorse

    @staticmethod
    def targetIs(astClass: type[hasDOTtarget], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.target(node))
        return workhorse

    @staticmethod
    def targetsIs(astClass: type[hasDOTtargets], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.targets(node))
        return workhorse

    @staticmethod
    def testIs(astClass: type[hasDOTtest], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.test(node))
        return workhorse

    @staticmethod
    def typeIs(astClass: type[hasDOTtype], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.type(node))
        return workhorse

    @staticmethod
    def type_commentIs(astClass: type[hasDOTtype_comment], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.type_comment(node))
        return workhorse

    @staticmethod
    def type_ignoresIs(astClass: type[hasDOTtype_ignores], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.type_ignores(node))
        return workhorse

    @staticmethod
    def type_paramsIs(astClass: type[hasDOTtype_params], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.type_params(node))
        return workhorse

    @staticmethod
    def upperIs(astClass: type[hasDOTupper], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.upper(node))
        return workhorse

    @staticmethod
    def valueIs(astClass: type[hasDOTvalue], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.value(node))
        return workhorse

    @staticmethod
    def valuesIs(astClass: type[hasDOTvalues], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.values(node))
        return workhorse

    @staticmethod
    def varargIs(astClass: type[hasDOTvararg], attributeCondition: Callable[[Any], Any]) -> Callable[[ast.AST], Any]:

        def workhorse(node: ast.AST) -> Any:
            return isinstance(node, astClass) and attributeCondition(DOT.vararg(node))
        return workhorse