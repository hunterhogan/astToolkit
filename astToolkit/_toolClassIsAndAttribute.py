# pyright: reportArgumentType=false
# ruff: noqa: F403, F405
"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit._astTypes import *
from collections.abc import Callable, Sequence
from typing import overload, TypeGuard
import ast
import sys

class ClassIsAndAttribute:
    """
    Create functions that verify AST nodes by type and attribute conditions.

    The ClassIsAndAttribute class provides static methods that generate conditional functions for determining if an AST
    node is of a specific type AND its attribute meets a specified condition. These functions return TypeGuard-enabled
    callables that can be used in conditional statements to narrow node types during code traversal and transformation.

    Each generated function performs two checks:
    1. Verifies that the node is of the specified AST type
    2. Tests if the specified attribute of the node meets a custom condition

    This enables complex filtering and targeting of AST nodes based on both their type and attribute contents.
    """

    @staticmethod
    @overload
    def annotationIs(astClass: type[hasDOTannotation_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation_expr] | bool]:
        ...

    @staticmethod
    @overload
    def annotationIs(astClass: type[hasDOTannotation_exprOrNone], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation_exprOrNone] | bool]:
        ...

    @staticmethod
    def annotationIs(astClass: type[hasDOTannotation], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTannotation] | bool:
            return isinstance(node, astClass) and node.annotation is not None and attributeCondition(node.annotation)
        return workhorse

    @staticmethod
    @overload
    def argIs(astClass: type[hasDOTarg_str], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg_str] | bool]:
        ...

    @staticmethod
    @overload
    def argIs(astClass: type[hasDOTarg_strOrNone], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg_strOrNone] | bool]:
        ...

    @staticmethod
    def argIs(astClass: type[hasDOTarg], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTarg] | bool:
            return isinstance(node, astClass) and node.arg is not None and attributeCondition(node.arg)
        return workhorse

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_arguments], attributeCondition: Callable[[ast.arguments], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_arguments] | bool]:
        ...

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_list_arg], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_list_arg] | bool]:
        ...

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_list_expr], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_list_expr] | bool]:
        ...

    @staticmethod
    def argsIs(astClass: type[hasDOTargs], attributeCondition: Callable[[ast.arguments], bool] | Callable[[list[ast.arg]], bool] | Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTargs] | bool:
            return isinstance(node, astClass) and attributeCondition(node.args)
        return workhorse

    @staticmethod
    def argtypesIs(astClass: type[hasDOTargtypes], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargtypes] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTargtypes] | bool:
            return isinstance(node, astClass) and attributeCondition(node.argtypes)
        return workhorse

    @staticmethod
    def asnameIs(astClass: type[hasDOTasname], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTasname] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTasname] | bool:
            return isinstance(node, astClass) and node.asname is not None and attributeCondition(node.asname)
        return workhorse

    @staticmethod
    def attrIs(astClass: type[hasDOTattr], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTattr] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTattr] | bool:
            return isinstance(node, astClass) and attributeCondition(node.attr)
        return workhorse

    @staticmethod
    def basesIs(astClass: type[hasDOTbases], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbases] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbases] | bool:
            return isinstance(node, astClass) and attributeCondition(node.bases)
        return workhorse

    @staticmethod
    @overload
    def bodyIs(astClass: type[hasDOTbody_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody_expr] | bool]:
        ...

    @staticmethod
    @overload
    def bodyIs(astClass: type[hasDOTbody_list_stmt], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody_list_stmt] | bool]:
        ...

    @staticmethod
    def bodyIs(astClass: type[hasDOTbody], attributeCondition: Callable[[ast.expr], bool] | Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbody] | bool:
            return isinstance(node, astClass) and attributeCondition(node.body)
        return workhorse

    @staticmethod
    def boundIs(astClass: type[hasDOTbound], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbound] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbound] | bool:
            return isinstance(node, astClass) and node.bound is not None and attributeCondition(node.bound)
        return workhorse

    @staticmethod
    def casesIs(astClass: type[hasDOTcases], attributeCondition: Callable[[Sequence[ast.match_case]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcases] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcases] | bool:
            return isinstance(node, astClass) and attributeCondition(node.cases)
        return workhorse

    @staticmethod
    def causeIs(astClass: type[hasDOTcause], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcause] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcause] | bool:
            return isinstance(node, astClass) and node.cause is not None and attributeCondition(node.cause)
        return workhorse

    @staticmethod
    def clsIs(astClass: type[hasDOTcls], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcls] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcls] | bool:
            return isinstance(node, astClass) and attributeCondition(node.cls)
        return workhorse

    @staticmethod
    def comparatorsIs(astClass: type[hasDOTcomparators], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcomparators] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcomparators] | bool:
            return isinstance(node, astClass) and attributeCondition(node.comparators)
        return workhorse

    @staticmethod
    def context_exprIs(astClass: type[hasDOTcontext_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcontext_expr] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcontext_expr] | bool:
            return isinstance(node, astClass) and attributeCondition(node.context_expr)
        return workhorse

    @staticmethod
    def conversionIs(astClass: type[hasDOTconversion], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTconversion] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTconversion] | bool:
            return isinstance(node, astClass) and attributeCondition(node.conversion)
        return workhorse

    @staticmethod
    def ctxIs(astClass: type[hasDOTctx], attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTctx] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTctx] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ctx)
        return workhorse

    @staticmethod
    def decorator_listIs(astClass: type[hasDOTdecorator_list], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdecorator_list] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTdecorator_list] | bool:
            return isinstance(node, astClass) and attributeCondition(node.decorator_list)
        return workhorse
    if sys.version_info >= (3, 13):

        @staticmethod
        def default_valueIs(astClass: type[hasDOTdefault_value], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdefault_value] | bool]:

            def workhorse(node: ast.AST) -> TypeGuard[hasDOTdefault_value] | bool:
                return isinstance(node, astClass) and node.default_value is not None and attributeCondition(node.default_value)
            return workhorse

    @staticmethod
    def defaultsIs(astClass: type[hasDOTdefaults], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdefaults] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTdefaults] | bool:
            return isinstance(node, astClass) and attributeCondition(node.defaults)
        return workhorse

    @staticmethod
    def eltIs(astClass: type[hasDOTelt], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTelt] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTelt] | bool:
            return isinstance(node, astClass) and attributeCondition(node.elt)
        return workhorse

    @staticmethod
    def eltsIs(astClass: type[hasDOTelts], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTelts] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTelts] | bool:
            return isinstance(node, astClass) and attributeCondition(node.elts)
        return workhorse

    @staticmethod
    def excIs(astClass: type[hasDOTexc], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTexc] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTexc] | bool:
            return isinstance(node, astClass) and node.exc is not None and attributeCondition(node.exc)
        return workhorse

    @staticmethod
    def finalbodyIs(astClass: type[hasDOTfinalbody], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTfinalbody] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTfinalbody] | bool:
            return isinstance(node, astClass) and attributeCondition(node.finalbody)
        return workhorse

    @staticmethod
    def format_specIs(astClass: type[hasDOTformat_spec], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTformat_spec] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTformat_spec] | bool:
            return isinstance(node, astClass) and node.format_spec is not None and attributeCondition(node.format_spec)
        return workhorse

    @staticmethod
    def funcIs(astClass: type[hasDOTfunc], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTfunc] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTfunc] | bool:
            return isinstance(node, astClass) and attributeCondition(node.func)
        return workhorse

    @staticmethod
    def generatorsIs(astClass: type[hasDOTgenerators], attributeCondition: Callable[[Sequence[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTgenerators] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTgenerators] | bool:
            return isinstance(node, astClass) and attributeCondition(node.generators)
        return workhorse

    @staticmethod
    def guardIs(astClass: type[hasDOTguard], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTguard] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTguard] | bool:
            return isinstance(node, astClass) and node.guard is not None and attributeCondition(node.guard)
        return workhorse

    @staticmethod
    def handlersIs(astClass: type[hasDOThandlers], attributeCondition: Callable[[list[ast.ExceptHandler]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOThandlers] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOThandlers] | bool:
            return isinstance(node, astClass) and attributeCondition(node.handlers)
        return workhorse

    @staticmethod
    def idIs(astClass: type[hasDOTid], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTid] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTid] | bool:
            return isinstance(node, astClass) and attributeCondition(node.id)
        return workhorse

    @staticmethod
    def ifsIs(astClass: type[hasDOTifs], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTifs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTifs] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ifs)
        return workhorse

    @staticmethod
    def is_asyncIs(astClass: type[hasDOTis_async], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTis_async] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTis_async] | bool:
            return isinstance(node, astClass) and attributeCondition(node.is_async)
        return workhorse

    @staticmethod
    def itemsIs(astClass: type[hasDOTitems], attributeCondition: Callable[[Sequence[ast.withitem]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTitems] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTitems] | bool:
            return isinstance(node, astClass) and attributeCondition(node.items)
        return workhorse

    @staticmethod
    def iterIs(astClass: type[hasDOTiter], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTiter] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTiter] | bool:
            return isinstance(node, astClass) and attributeCondition(node.iter)
        return workhorse

    @staticmethod
    def keyIs(astClass: type[hasDOTkey], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkey] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkey] | bool:
            return isinstance(node, astClass) and attributeCondition(node.key)
        return workhorse

    @staticmethod
    @overload
    def keysIs(astClass: type[hasDOTkeys_list_expr], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys_list_expr] | bool]:
        ...

    @staticmethod
    @overload
    def keysIs(astClass: type[hasDOTkeys_list_exprOrNone], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys_list_exprOrNone] | bool]:
        ...

    @staticmethod
    def keysIs(astClass: type[hasDOTkeys], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkeys] | bool:
            return isinstance(node, astClass) and node.keys != [None] and attributeCondition(node.keys)
        return workhorse

    @staticmethod
    def keywordsIs(astClass: type[hasDOTkeywords], attributeCondition: Callable[[Sequence[ast.keyword]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeywords] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkeywords] | bool:
            return isinstance(node, astClass) and attributeCondition(node.keywords)
        return workhorse

    @staticmethod
    def kindIs(astClass: type[hasDOTkind], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkind] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkind] | bool:
            return isinstance(node, astClass) and node.kind is not None and attributeCondition(node.kind)
        return workhorse

    @staticmethod
    def kw_defaultsIs(astClass: type[hasDOTkw_defaults], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkw_defaults] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkw_defaults] | bool:
            return isinstance(node, astClass) and node.kw_defaults != [None] and attributeCondition(node.kw_defaults)
        return workhorse

    @staticmethod
    def kwargIs(astClass: type[hasDOTkwarg], attributeCondition: Callable[[ast.arg], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwarg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwarg] | bool:
            return isinstance(node, astClass) and node.kwarg is not None and attributeCondition(node.kwarg)
        return workhorse

    @staticmethod
    def kwd_attrsIs(astClass: type[hasDOTkwd_attrs], attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwd_attrs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwd_attrs] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwd_attrs)
        return workhorse

    @staticmethod
    def kwd_patternsIs(astClass: type[hasDOTkwd_patterns], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwd_patterns] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwd_patterns] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwd_patterns)
        return workhorse

    @staticmethod
    def kwonlyargsIs(astClass: type[hasDOTkwonlyargs], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwonlyargs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwonlyargs] | bool:
            return isinstance(node, astClass) and attributeCondition(node.kwonlyargs)
        return workhorse

    @staticmethod
    def leftIs(astClass: type[hasDOTleft], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTleft] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTleft] | bool:
            return isinstance(node, astClass) and attributeCondition(node.left)
        return workhorse

    @staticmethod
    def levelIs(astClass: type[hasDOTlevel], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlevel] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlevel] | bool:
            return isinstance(node, astClass) and attributeCondition(node.level)
        return workhorse

    @staticmethod
    def linenoIs(astClass: type[hasDOTlineno], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlineno] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlineno] | bool:
            return isinstance(node, astClass) and attributeCondition(node.lineno)
        return workhorse

    @staticmethod
    def lowerIs(astClass: type[hasDOTlower], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlower] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlower] | bool:
            return isinstance(node, astClass) and node.lower is not None and attributeCondition(node.lower)
        return workhorse

    @staticmethod
    def moduleIs(astClass: type[hasDOTmodule], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTmodule] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTmodule] | bool:
            return isinstance(node, astClass) and node.module is not None and attributeCondition(node.module)
        return workhorse

    @staticmethod
    def msgIs(astClass: type[hasDOTmsg], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTmsg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTmsg] | bool:
            return isinstance(node, astClass) and node.msg is not None and attributeCondition(node.msg)
        return workhorse

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_Name], attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_Name] | bool]:
        ...

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_str], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_str] | bool]:
        ...

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_strOrNone], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_strOrNone] | bool]:
        ...

    @staticmethod
    def nameIs(astClass: type[hasDOTname], attributeCondition: Callable[[ast.Name], bool] | Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTname] | bool:
            return isinstance(node, astClass) and node.name is not None and attributeCondition(node.name)
        return workhorse

    @staticmethod
    @overload
    def namesIs(astClass: type[hasDOTnames_list_alias], attributeCondition: Callable[[list[ast.alias]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames_list_alias] | bool]:
        ...

    @staticmethod
    @overload
    def namesIs(astClass: type[hasDOTnames_list_str], attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames_list_str] | bool]:
        ...

    @staticmethod
    def namesIs(astClass: type[hasDOTnames], attributeCondition: Callable[[list[ast.alias]], bool] | Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTnames] | bool:
            return isinstance(node, astClass) and attributeCondition(node.names)
        return workhorse

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_boolop], attributeCondition: Callable[[ast.boolop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_boolop] | bool]:
        ...

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_operator], attributeCondition: Callable[[ast.operator], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_operator] | bool]:
        ...

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_unaryop], attributeCondition: Callable[[ast.unaryop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_unaryop] | bool]:
        ...

    @staticmethod
    def opIs(astClass: type[hasDOTop], attributeCondition: Callable[[ast.boolop], bool] | Callable[[ast.operator], bool] | Callable[[ast.unaryop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTop] | bool:
            return isinstance(node, astClass) and attributeCondition(node.op)
        return workhorse

    @staticmethod
    def operandIs(astClass: type[hasDOToperand], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOToperand] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOToperand] | bool:
            return isinstance(node, astClass) and attributeCondition(node.operand)
        return workhorse

    @staticmethod
    def opsIs(astClass: type[hasDOTops], attributeCondition: Callable[[Sequence[ast.cmpop]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTops] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTops] | bool:
            return isinstance(node, astClass) and attributeCondition(node.ops)
        return workhorse

    @staticmethod
    def optional_varsIs(astClass: type[hasDOToptional_vars], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOToptional_vars] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOToptional_vars] | bool:
            return isinstance(node, astClass) and node.optional_vars is not None and attributeCondition(node.optional_vars)
        return workhorse

    @staticmethod
    @overload
    def orelseIs(astClass: type[hasDOTorelse_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse_expr] | bool]:
        ...

    @staticmethod
    @overload
    def orelseIs(astClass: type[hasDOTorelse_list_stmt], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse_list_stmt] | bool]:
        ...

    @staticmethod
    def orelseIs(astClass: type[hasDOTorelse], attributeCondition: Callable[[ast.expr], bool] | Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTorelse] | bool:
            return isinstance(node, astClass) and attributeCondition(node.orelse)
        return workhorse

    @staticmethod
    @overload
    def patternIs(astClass: type[hasDOTpattern_pattern], attributeCondition: Callable[[ast.pattern], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern_pattern] | bool]:
        ...

    @staticmethod
    @overload
    def patternIs(astClass: type[hasDOTpattern_patternOrNone], attributeCondition: Callable[[ast.pattern], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern_patternOrNone] | bool]:
        ...

    @staticmethod
    def patternIs(astClass: type[hasDOTpattern], attributeCondition: Callable[[ast.pattern], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTpattern] | bool:
            return isinstance(node, astClass) and node.pattern is not None and attributeCondition(node.pattern)
        return workhorse

    @staticmethod
    def patternsIs(astClass: type[hasDOTpatterns], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpatterns] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTpatterns] | bool:
            return isinstance(node, astClass) and attributeCondition(node.patterns)
        return workhorse

    @staticmethod
    def posonlyargsIs(astClass: type[hasDOTposonlyargs], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTposonlyargs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTposonlyargs] | bool:
            return isinstance(node, astClass) and attributeCondition(node.posonlyargs)
        return workhorse

    @staticmethod
    def restIs(astClass: type[hasDOTrest], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTrest] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTrest] | bool:
            return isinstance(node, astClass) and node.rest is not None and attributeCondition(node.rest)
        return workhorse

    @staticmethod
    @overload
    def returnsIs(astClass: type[hasDOTreturns_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns_expr] | bool]:
        ...

    @staticmethod
    @overload
    def returnsIs(astClass: type[hasDOTreturns_exprOrNone], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns_exprOrNone] | bool]:
        ...

    @staticmethod
    def returnsIs(astClass: type[hasDOTreturns], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTreturns] | bool:
            return isinstance(node, astClass) and node.returns is not None and attributeCondition(node.returns)
        return workhorse

    @staticmethod
    def rightIs(astClass: type[hasDOTright], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTright] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTright] | bool:
            return isinstance(node, astClass) and attributeCondition(node.right)
        return workhorse

    @staticmethod
    def simpleIs(astClass: type[hasDOTsimple], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTsimple] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTsimple] | bool:
            return isinstance(node, astClass) and attributeCondition(node.simple)
        return workhorse

    @staticmethod
    def sliceIs(astClass: type[hasDOTslice], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTslice] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTslice] | bool:
            return isinstance(node, astClass) and attributeCondition(node.slice)
        return workhorse

    @staticmethod
    def stepIs(astClass: type[hasDOTstep], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTstep] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTstep] | bool:
            return isinstance(node, astClass) and node.step is not None and attributeCondition(node.step)
        return workhorse

    @staticmethod
    def subjectIs(astClass: type[hasDOTsubject], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTsubject] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTsubject] | bool:
            return isinstance(node, astClass) and attributeCondition(node.subject)
        return workhorse

    @staticmethod
    def tagIs(astClass: type[hasDOTtag], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtag] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtag] | bool:
            return isinstance(node, astClass) and attributeCondition(node.tag)
        return workhorse

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_Name], attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_Name] | bool]:
        ...

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_NameOrAttributeOrSubscript], attributeCondition: Callable[[ast.Name | ast.Attribute | ast.Subscript], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_NameOrAttributeOrSubscript] | bool]:
        ...

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_expr] | bool]:
        ...

    @staticmethod
    def targetIs(astClass: type[hasDOTtarget], attributeCondition: Callable[[ast.expr], bool] | Callable[[ast.Name], bool] | Callable[[ast.Name | ast.Attribute | ast.Subscript], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtarget] | bool:
            return isinstance(node, astClass) and attributeCondition(node.target)
        return workhorse

    @staticmethod
    def targetsIs(astClass: type[hasDOTtargets], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtargets] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtargets] | bool:
            return isinstance(node, astClass) and attributeCondition(node.targets)
        return workhorse

    @staticmethod
    def testIs(astClass: type[hasDOTtest], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtest] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtest] | bool:
            return isinstance(node, astClass) and attributeCondition(node.test)
        return workhorse

    @staticmethod
    def typeIs(astClass: type[hasDOTtype], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype] | bool:
            return isinstance(node, astClass) and node.type is not None and attributeCondition(node.type)
        return workhorse

    @staticmethod
    def type_commentIs(astClass: type[hasDOTtype_comment], attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_comment] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_comment] | bool:
            return isinstance(node, astClass) and node.type_comment is not None and attributeCondition(node.type_comment)
        return workhorse

    @staticmethod
    def type_ignoresIs(astClass: type[hasDOTtype_ignores], attributeCondition: Callable[[list[ast.TypeIgnore]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_ignores] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_ignores] | bool:
            return isinstance(node, astClass) and attributeCondition(node.type_ignores)
        return workhorse

    @staticmethod
    def type_paramsIs(astClass: type[hasDOTtype_params], attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_params] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_params] | bool:
            return isinstance(node, astClass) and attributeCondition(node.type_params)
        return workhorse

    @staticmethod
    def upperIs(astClass: type[hasDOTupper], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTupper] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTupper] | bool:
            return isinstance(node, astClass) and node.upper is not None and attributeCondition(node.upper)
        return workhorse

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_ConstantValueType], attributeCondition: Callable[[ConstantValueType], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_ConstantValueType] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_boolOrNone], attributeCondition: Callable[[bool], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_boolOrNone] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_expr] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_exprOrNone], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_exprOrNone] | bool]:
        ...

    @staticmethod
    def valueIs(astClass: type[hasDOTvalue], attributeCondition: Callable[[ast.expr], bool] | Callable[[bool], bool] | Callable[[ConstantValueType], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvalue] | bool:
            return isinstance(node, astClass) and node.value is not None and attributeCondition(node.value)
        return workhorse

    @staticmethod
    def valuesIs(astClass: type[hasDOTvalues], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalues] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvalues] | bool:
            return isinstance(node, astClass) and attributeCondition(node.values)
        return workhorse

    @staticmethod
    def varargIs(astClass: type[hasDOTvararg], attributeCondition: Callable[[ast.arg], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvararg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvararg] | bool:
            return isinstance(node, astClass) and node.vararg is not None and attributeCondition(node.vararg)
        return workhorse