"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import (
	ConstantValueType, hasDOTannotation, hasDOTarg, hasDOTargs, hasDOTargtypes, hasDOTasname, hasDOTattr, hasDOTbases,
	hasDOTbody, hasDOTbound, hasDOTcases, hasDOTcause, hasDOTcls, hasDOTcomparators, hasDOTcontext_expr, hasDOTconversion,
	hasDOTctx, hasDOTdecorator_list, hasDOTdefaults, hasDOTelt, hasDOTelts, hasDOTexc, hasDOTfinalbody, hasDOTformat_spec,
	hasDOTfunc, hasDOTgenerators, hasDOTguard, hasDOThandlers, hasDOTid, hasDOTifs, hasDOTis_async, hasDOTitems,
	hasDOTiter, hasDOTkey, hasDOTkeys, hasDOTkeywords, hasDOTkind, hasDOTkw_defaults, hasDOTkwarg, hasDOTkwd_attrs,
	hasDOTkwd_patterns, hasDOTkwonlyargs, hasDOTleft, hasDOTlevel, hasDOTlineno, hasDOTlower, hasDOTmodule, hasDOTmsg,
	hasDOTname, hasDOTnames, hasDOTop, hasDOToperand, hasDOTops, hasDOToptional_vars, hasDOTorelse, hasDOTpattern,
	hasDOTpatterns, hasDOTposonlyargs, hasDOTrest, hasDOTreturns, hasDOTright, hasDOTsimple, hasDOTslice, hasDOTstep,
	hasDOTsubject, hasDOTtag, hasDOTtarget, hasDOTtargets, hasDOTtest, hasDOTtype, hasDOTtype_comment, hasDOTtype_ignores,
	hasDOTtype_params, hasDOTupper, hasDOTvalue, hasDOTvalues, hasDOTvararg,
)
from collections.abc import Callable, Sequence
from typing_extensions import TypeIs
import ast
import sys

if sys.version_info >= (3, 13):
    from astToolkit import hasDOTdefault_value as hasDOTdefault_value

class ClassIsAndAttribute:
    """
    Create functions that verify AST nodes by type and attribute conditions.

    The ClassIsAndAttribute class provides static methods that generate conditional functions for determining if an AST
    node is of a specific type AND its attribute meets a specified condition. These functions return TypeIs-enabled
    callables that can be used in conditional statements to narrow node types during code traversal and transformation.

    Each generated function performs two checks:
    1. Verifies that the node is of the specified AST type
    2. Tests if the specified attribute of the node meets a custom condition

    This enables complex filtering and targeting of AST nodes based on both their type and attribute contents.
    """

    @staticmethod
    def annotationIs[是: hasDOTannotation](astClass: type[是], attributeCondition: Callable[[ast.expr | (ast.expr | None)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.annotation is not None and attributeCondition(node.annotation)
        return workhorse

    @staticmethod
    def argIs[是: hasDOTarg](astClass: type[是], attributeCondition: Callable[[str | (str | None)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.arg is not None and attributeCondition(node.arg)
        return workhorse

    @staticmethod
    def argsIs[是: hasDOTargs](astClass: type[是], attributeCondition: Callable[[ast.arguments | list[ast.arg] | Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.args)
        return workhorse

    @staticmethod
    def argtypesIs[是: hasDOTargtypes](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.argtypes)
        return workhorse

    @staticmethod
    def asnameIs[是: hasDOTasname](astClass: type[是], attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.asname is not None and attributeCondition(node.asname)
        return workhorse

    @staticmethod
    def attrIs[是: hasDOTattr](astClass: type[是], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.attr)
        return workhorse

    @staticmethod
    def basesIs[是: hasDOTbases](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.bases)
        return workhorse

    @staticmethod
    def bodyIs[是: hasDOTbody](astClass: type[是], attributeCondition: Callable[[ast.expr | Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.body)
        return workhorse

    @staticmethod
    def boundIs[是: hasDOTbound](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.bound is not None and attributeCondition(node.bound)
        return workhorse

    @staticmethod
    def casesIs[是: hasDOTcases](astClass: type[是], attributeCondition: Callable[[list[ast.match_case]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.cases)
        return workhorse

    @staticmethod
    def causeIs[是: hasDOTcause](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.cause is not None and attributeCondition(node.cause)
        return workhorse

    @staticmethod
    def clsIs[是: hasDOTcls](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.cls)
        return workhorse

    @staticmethod
    def comparatorsIs[是: hasDOTcomparators](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.comparators)
        return workhorse

    @staticmethod
    def context_exprIs[是: hasDOTcontext_expr](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.context_expr)
        return workhorse

    @staticmethod
    def conversionIs[是: hasDOTconversion](astClass: type[是], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.conversion)
        return workhorse

    @staticmethod
    def ctxIs[是: hasDOTctx](astClass: type[是], attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ctx)
        return workhorse

    @staticmethod
    def decorator_listIs[是: hasDOTdecorator_list](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.decorator_list)
        return workhorse
    if sys.version_info >= (3, 13):

        @staticmethod
        def default_valueIs[是: hasDOTdefault_value](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[是] | bool:
                return isinstance(node, astClass) and node.default_value is not None and attributeCondition(node.default_value)
            return workhorse

    @staticmethod
    def defaultsIs[是: hasDOTdefaults](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.defaults)
        return workhorse

    @staticmethod
    def eltIs[是: hasDOTelt](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.elt)
        return workhorse

    @staticmethod
    def eltsIs[是: hasDOTelts](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.elts)
        return workhorse

    @staticmethod
    def excIs[是: hasDOTexc](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.exc is not None and attributeCondition(node.exc)
        return workhorse

    @staticmethod
    def finalbodyIs[是: hasDOTfinalbody](astClass: type[是], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.finalbody)
        return workhorse

    @staticmethod
    def format_specIs[是: hasDOTformat_spec](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.format_spec is not None and attributeCondition(node.format_spec)
        return workhorse

    @staticmethod
    def funcIs[是: hasDOTfunc](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.func)
        return workhorse

    @staticmethod
    def generatorsIs[是: hasDOTgenerators](astClass: type[是], attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.generators)
        return workhorse

    @staticmethod
    def guardIs[是: hasDOTguard](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.guard is not None and attributeCondition(node.guard)
        return workhorse

    @staticmethod
    def handlersIs[是: hasDOThandlers](astClass: type[是], attributeCondition: Callable[[list[ast.ExceptHandler]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.handlers)
        return workhorse

    @staticmethod
    def idIs[是: hasDOTid](astClass: type[是], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.id)
        return workhorse

    @staticmethod
    def ifsIs[是: hasDOTifs](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ifs)
        return workhorse

    @staticmethod
    def is_asyncIs[是: hasDOTis_async](astClass: type[是], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.is_async)
        return workhorse

    @staticmethod
    def itemsIs[是: hasDOTitems](astClass: type[是], attributeCondition: Callable[[list[ast.withitem]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.items)
        return workhorse

    @staticmethod
    def iterIs[是: hasDOTiter](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.iter)
        return workhorse

    @staticmethod
    def keyIs[是: hasDOTkey](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.key)
        return workhorse

    @staticmethod
    def keysIs[是: hasDOTkeys](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr | None] | Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.keys != [None] and attributeCondition(node.keys)
        return workhorse

    @staticmethod
    def keywordsIs[是: hasDOTkeywords](astClass: type[是], attributeCondition: Callable[[list[ast.keyword]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.keywords)
        return workhorse

    @staticmethod
    def kindIs[是: hasDOTkind](astClass: type[是], attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.kind is not None and attributeCondition(node.kind)
        return workhorse

    @staticmethod
    def kw_defaultsIs[是: hasDOTkw_defaults](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr | None]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.kw_defaults != [None] and attributeCondition(node.kw_defaults)
        return workhorse

    @staticmethod
    def kwargIs[是: hasDOTkwarg](astClass: type[是], attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.kwarg is not None and attributeCondition(node.kwarg)
        return workhorse

    @staticmethod
    def kwd_attrsIs[是: hasDOTkwd_attrs](astClass: type[是], attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwd_attrs)
        return workhorse

    @staticmethod
    def kwd_patternsIs[是: hasDOTkwd_patterns](astClass: type[是], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwd_patterns)
        return workhorse

    @staticmethod
    def kwonlyargsIs[是: hasDOTkwonlyargs](astClass: type[是], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwonlyargs)
        return workhorse

    @staticmethod
    def leftIs[是: hasDOTleft](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.left)
        return workhorse

    @staticmethod
    def levelIs[是: hasDOTlevel](astClass: type[是], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.level)
        return workhorse

    @staticmethod
    def linenoIs[是: hasDOTlineno](astClass: type[是], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.lineno)
        return workhorse

    @staticmethod
    def lowerIs[是: hasDOTlower](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.lower is not None and attributeCondition(node.lower)
        return workhorse

    @staticmethod
    def moduleIs[是: hasDOTmodule](astClass: type[是], attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.module is not None and attributeCondition(node.module)
        return workhorse

    @staticmethod
    def msgIs[是: hasDOTmsg](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.msg is not None and attributeCondition(node.msg)
        return workhorse

    @staticmethod
    def nameIs[是: hasDOTname](astClass: type[是], attributeCondition: Callable[[ast.Name | str | (str | None)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.name is not None and attributeCondition(node.name)
        return workhorse

    @staticmethod
    def namesIs[是: hasDOTnames](astClass: type[是], attributeCondition: Callable[[list[ast.alias] | list[str]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.names)
        return workhorse

    @staticmethod
    def opIs[是: hasDOTop](astClass: type[是], attributeCondition: Callable[[ast.boolop | ast.operator | ast.unaryop], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.op)
        return workhorse

    @staticmethod
    def operandIs[是: hasDOToperand](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.operand)
        return workhorse

    @staticmethod
    def opsIs[是: hasDOTops](astClass: type[是], attributeCondition: Callable[[Sequence[ast.cmpop]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ops)
        return workhorse

    @staticmethod
    def optional_varsIs[是: hasDOToptional_vars](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.optional_vars is not None and attributeCondition(node.optional_vars)
        return workhorse

    @staticmethod
    def orelseIs[是: hasDOTorelse](astClass: type[是], attributeCondition: Callable[[ast.expr | Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.orelse)
        return workhorse

    @staticmethod
    def patternIs[是: hasDOTpattern](astClass: type[是], attributeCondition: Callable[[ast.pattern | (ast.pattern | None)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.pattern is not None and attributeCondition(node.pattern)
        return workhorse

    @staticmethod
    def patternsIs[是: hasDOTpatterns](astClass: type[是], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.patterns)
        return workhorse

    @staticmethod
    def posonlyargsIs[是: hasDOTposonlyargs](astClass: type[是], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.posonlyargs)
        return workhorse

    @staticmethod
    def restIs[是: hasDOTrest](astClass: type[是], attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.rest is not None and attributeCondition(node.rest)
        return workhorse

    @staticmethod
    def returnsIs[是: hasDOTreturns](astClass: type[是], attributeCondition: Callable[[ast.expr | (ast.expr | None)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.returns is not None and attributeCondition(node.returns)
        return workhorse

    @staticmethod
    def rightIs[是: hasDOTright](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.right)
        return workhorse

    @staticmethod
    def simpleIs[是: hasDOTsimple](astClass: type[是], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.simple)
        return workhorse

    @staticmethod
    def sliceIs[是: hasDOTslice](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.slice)
        return workhorse

    @staticmethod
    def stepIs[是: hasDOTstep](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.step is not None and attributeCondition(node.step)
        return workhorse

    @staticmethod
    def subjectIs[是: hasDOTsubject](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.subject)
        return workhorse

    @staticmethod
    def tagIs[是: hasDOTtag](astClass: type[是], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.tag)
        return workhorse

    @staticmethod
    def targetIs[是: hasDOTtarget](astClass: type[是], attributeCondition: Callable[[ast.expr | ast.Name | (ast.Name | ast.Attribute | ast.Subscript)], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.target)
        return workhorse

    @staticmethod
    def targetsIs[是: hasDOTtargets](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.targets)
        return workhorse

    @staticmethod
    def testIs[是: hasDOTtest](astClass: type[是], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.test)
        return workhorse

    @staticmethod
    def typeIs[是: hasDOTtype](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.type is not None and attributeCondition(node.type)
        return workhorse

    @staticmethod
    def type_commentIs[是: hasDOTtype_comment](astClass: type[是], attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.type_comment is not None and attributeCondition(node.type_comment)
        return workhorse

    @staticmethod
    def type_ignoresIs[是: hasDOTtype_ignores](astClass: type[是], attributeCondition: Callable[[list[ast.TypeIgnore]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.type_ignores)
        return workhorse

    @staticmethod
    def type_paramsIs[是: hasDOTtype_params](astClass: type[是], attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.type_params)
        return workhorse

    @staticmethod
    def upperIs[是: hasDOTupper](astClass: type[是], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.upper is not None and attributeCondition(node.upper)
        return workhorse

    @staticmethod
    def valueIs[是: hasDOTvalue](astClass: type[是], attributeCondition: Callable[[ast.expr | (ast.expr | None) | (bool | None) | ConstantValueType], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.value is not None and attributeCondition(node.value)
        return workhorse

    @staticmethod
    def valuesIs[是: hasDOTvalues](astClass: type[是], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and attributeCondition(node.values)
        return workhorse

    @staticmethod
    def varargIs[是: hasDOTvararg](astClass: type[是], attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeIs[是] | bool]:

        def workhorse(node: ast.AST) -> TypeIs[是] | bool:
            return isinstance(node, astClass) and node.vararg is not None and attributeCondition(node.vararg)
        return workhorse