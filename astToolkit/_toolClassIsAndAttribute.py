# ruff: noqa: F403, F405
"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import ast_Identifier, ast_expr_Slice, astDOTtype_param, DOT
from astToolkit._astTypes import *
from collections.abc import Callable, Sequence
from typing import Any, Literal, overload, TypeGuard
import ast

class ClassIsAndAttribute:

    @staticmethod
    @overload
    def annotationIs(astClass: type[hasDOTannotation_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation_expr] | bool]:
        ...

    @staticmethod
    @overload
    def annotationIs(astClass: type[hasDOTannotation_exprOrNone], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation_exprOrNone] | bool]:
        ...

    @staticmethod
    def annotationIs(astClass: type[hasDOTannotation], attributeCondition: Callable[[ast.expr | (ast.expr | None)], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTannotation] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTannotation] | bool:
            return isinstance(node, astClass) and DOT.annotation(node) is not None and attributeCondition(DOT.annotation(node))
        return workhorse

    @staticmethod
    @overload
    def argIs(astClass: type[hasDOTarg_Identifier], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg_Identifier] | bool]:
        ...

    @staticmethod
    @overload
    def argIs(astClass: type[hasDOTarg_IdentifierOrNone], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg_IdentifierOrNone] | bool]:
        ...

    @staticmethod
    def argIs(astClass: type[hasDOTarg], attributeCondition: Callable[[ast_Identifier | (ast_Identifier | None)], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTarg] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTarg] | bool:
            return isinstance(node, astClass) and DOT.arg(node) is not None and attributeCondition(DOT.arg(node))
        return workhorse

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_arguments], attributeCondition: Callable[[ast.arguments], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_arguments] | bool]:
        ...

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_list_expr], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_list_expr] | bool]:
        ...

    @staticmethod
    @overload
    def argsIs(astClass: type[hasDOTargs_list_arg], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs_list_arg] | bool]:
        ...

    @staticmethod
    def argsIs(astClass: type[hasDOTargs], attributeCondition: Callable[[ast.arguments | Sequence[ast.expr] | list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargs] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTargs] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.args(node))
        return workhorse

    @staticmethod
    def argtypesIs(astClass: type[hasDOTargtypes], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTargtypes] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTargtypes] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.argtypes(node))
        return workhorse

    @staticmethod
    def asnameIs(astClass: type[hasDOTasname], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTasname] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTasname] | bool:
            return isinstance(node, astClass) and DOT.asname(node) is not None and attributeCondition(DOT.asname(node))
        return workhorse

    @staticmethod
    def attrIs(astClass: type[hasDOTattr], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTattr] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTattr] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.attr(node))
        return workhorse

    @staticmethod
    def basesIs(astClass: type[hasDOTbases], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbases] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbases] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.bases(node))
        return workhorse

    @staticmethod
    @overload
    def bodyIs(astClass: type[hasDOTbody_list_stmt], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody_list_stmt] | bool]:
        ...

    @staticmethod
    @overload
    def bodyIs(astClass: type[hasDOTbody_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody_expr] | bool]:
        ...

    @staticmethod
    def bodyIs(astClass: type[hasDOTbody], attributeCondition: Callable[[Sequence[ast.stmt] | ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbody] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbody] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.body(node))
        return workhorse

    @staticmethod
    def boundIs(astClass: type[hasDOTbound], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTbound] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTbound] | bool:
            return isinstance(node, astClass) and DOT.bound(node) is not None and attributeCondition(DOT.bound(node))
        return workhorse

    @staticmethod
    def casesIs(astClass: type[hasDOTcases], attributeCondition: Callable[[list[ast.match_case]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcases] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcases] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.cases(node))
        return workhorse

    @staticmethod
    def causeIs(astClass: type[hasDOTcause], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcause] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcause] | bool:
            return isinstance(node, astClass) and DOT.cause(node) is not None and attributeCondition(DOT.cause(node))
        return workhorse

    @staticmethod
    def clsIs(astClass: type[hasDOTcls], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcls] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcls] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.cls(node))
        return workhorse

    @staticmethod
    def comparatorsIs(astClass: type[hasDOTcomparators], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcomparators] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcomparators] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.comparators(node))
        return workhorse

    @staticmethod
    def context_exprIs(astClass: type[hasDOTcontext_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTcontext_expr] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTcontext_expr] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.context_expr(node))
        return workhorse

    @staticmethod
    def conversionIs(astClass: type[hasDOTconversion], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTconversion] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTconversion] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.conversion(node))
        return workhorse

    @staticmethod
    def ctxIs(astClass: type[hasDOTctx], attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTctx] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTctx] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.ctx(node))
        return workhorse

    @staticmethod
    def decorator_listIs(astClass: type[hasDOTdecorator_list], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdecorator_list] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTdecorator_list] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.decorator_list(node))
        return workhorse

    @staticmethod
    def default_valueIs(astClass: type[hasDOTdefault_value], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdefault_value] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTdefault_value] | bool:
            return isinstance(node, astClass) and DOT.default_value(node) is not None and attributeCondition(DOT.default_value(node))
        return workhorse

    @staticmethod
    def defaultsIs(astClass: type[hasDOTdefaults], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTdefaults] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTdefaults] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.defaults(node))
        return workhorse

    @staticmethod
    def eltIs(astClass: type[hasDOTelt], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTelt] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTelt] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.elt(node))
        return workhorse

    @staticmethod
    def eltsIs(astClass: type[hasDOTelts], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTelts] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTelts] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.elts(node))
        return workhorse

    @staticmethod
    def excIs(astClass: type[hasDOTexc], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTexc] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTexc] | bool:
            return isinstance(node, astClass) and DOT.exc(node) is not None and attributeCondition(DOT.exc(node))
        return workhorse

    @staticmethod
    def finalbodyIs(astClass: type[hasDOTfinalbody], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTfinalbody] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTfinalbody] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.finalbody(node))
        return workhorse

    @staticmethod
    def format_specIs(astClass: type[hasDOTformat_spec], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTformat_spec] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTformat_spec] | bool:
            return isinstance(node, astClass) and DOT.format_spec(node) is not None and attributeCondition(DOT.format_spec(node))
        return workhorse

    @staticmethod
    def funcIs(astClass: type[hasDOTfunc], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTfunc] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTfunc] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.func(node))
        return workhorse

    @staticmethod
    def generatorsIs(astClass: type[hasDOTgenerators], attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTgenerators] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTgenerators] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.generators(node))
        return workhorse

    @staticmethod
    def guardIs(astClass: type[hasDOTguard], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTguard] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTguard] | bool:
            return isinstance(node, astClass) and DOT.guard(node) is not None and attributeCondition(DOT.guard(node))
        return workhorse

    @staticmethod
    def handlersIs(astClass: type[hasDOThandlers], attributeCondition: Callable[[list[ast.ExceptHandler]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOThandlers] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOThandlers] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.handlers(node))
        return workhorse

    @staticmethod
    def idIs(astClass: type[hasDOTid], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTid] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTid] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.id(node))
        return workhorse

    @staticmethod
    def ifsIs(astClass: type[hasDOTifs], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTifs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTifs] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.ifs(node))
        return workhorse

    @staticmethod
    def is_asyncIs(astClass: type[hasDOTis_async], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTis_async] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTis_async] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.is_async(node))
        return workhorse

    @staticmethod
    def itemsIs(astClass: type[hasDOTitems], attributeCondition: Callable[[list[ast.withitem]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTitems] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTitems] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.items(node))
        return workhorse

    @staticmethod
    def iterIs(astClass: type[hasDOTiter], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTiter] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTiter] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.iter(node))
        return workhorse

    @staticmethod
    def keyIs(astClass: type[hasDOTkey], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkey] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkey] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.key(node))
        return workhorse

    @staticmethod
    @overload
    def keysIs(astClass: type[hasDOTkeys_list_exprOrNone], attributeCondition: Callable[[Sequence[ast.expr | None]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys_list_exprOrNone] | bool]:
        ...

    @staticmethod
    @overload
    def keysIs(astClass: type[hasDOTkeys_list_expr], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys_list_expr] | bool]:
        ...

    @staticmethod
    def keysIs(astClass: type[hasDOTkeys], attributeCondition: Callable[[Sequence[ast.expr | None] | Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeys] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkeys] | bool:
            return isinstance(node, astClass) and DOT.keys(node) != [None] and attributeCondition(DOT.keys(node))
        return workhorse

    @staticmethod
    def keywordsIs(astClass: type[hasDOTkeywords], attributeCondition: Callable[[list[ast.keyword]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkeywords] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkeywords] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.keywords(node))
        return workhorse

    @staticmethod
    def kindIs(astClass: type[hasDOTkind], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkind] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkind] | bool:
            return isinstance(node, astClass) and DOT.kind(node) is not None and attributeCondition(DOT.kind(node))
        return workhorse

    @staticmethod
    def kw_defaultsIs(astClass: type[hasDOTkw_defaults], attributeCondition: Callable[[Sequence[ast.expr | None]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkw_defaults] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkw_defaults] | bool:
            return isinstance(node, astClass) and DOT.kw_defaults(node) != [None] and attributeCondition(DOT.kw_defaults(node))
        return workhorse

    @staticmethod
    def kwargIs(astClass: type[hasDOTkwarg], attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwarg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwarg] | bool:
            return isinstance(node, astClass) and DOT.kwarg(node) is not None and attributeCondition(DOT.kwarg(node))
        return workhorse

    @staticmethod
    def kwd_attrsIs(astClass: type[hasDOTkwd_attrs], attributeCondition: Callable[[list[ast_Identifier]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwd_attrs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwd_attrs] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.kwd_attrs(node))
        return workhorse

    @staticmethod
    def kwd_patternsIs(astClass: type[hasDOTkwd_patterns], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwd_patterns] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwd_patterns] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.kwd_patterns(node))
        return workhorse

    @staticmethod
    def kwonlyargsIs(astClass: type[hasDOTkwonlyargs], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTkwonlyargs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTkwonlyargs] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.kwonlyargs(node))
        return workhorse

    @staticmethod
    def leftIs(astClass: type[hasDOTleft], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTleft] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTleft] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.left(node))
        return workhorse

    @staticmethod
    def levelIs(astClass: type[hasDOTlevel], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlevel] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlevel] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.level(node))
        return workhorse

    @staticmethod
    def linenoIs(astClass: type[hasDOTlineno], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlineno] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlineno] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.lineno(node))
        return workhorse

    @staticmethod
    def lowerIs(astClass: type[hasDOTlower], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTlower] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTlower] | bool:
            return isinstance(node, astClass) and DOT.lower(node) is not None and attributeCondition(DOT.lower(node))
        return workhorse

    @staticmethod
    def moduleIs(astClass: type[hasDOTmodule], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTmodule] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTmodule] | bool:
            return isinstance(node, astClass) and DOT.module(node) is not None and attributeCondition(DOT.module(node))
        return workhorse

    @staticmethod
    def msgIs(astClass: type[hasDOTmsg], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTmsg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTmsg] | bool:
            return isinstance(node, astClass) and DOT.msg(node) is not None and attributeCondition(DOT.msg(node))
        return workhorse

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_Identifier], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_Identifier] | bool]:
        ...

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_IdentifierOrNone], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_IdentifierOrNone] | bool]:
        ...

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_str], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_str] | bool]:
        ...

    @staticmethod
    @overload
    def nameIs(astClass: type[hasDOTname_Name], attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname_Name] | bool]:
        ...

    @staticmethod
    def nameIs(astClass: type[hasDOTname], attributeCondition: Callable[[ast_Identifier | (ast_Identifier | None) | ast_Identifier | ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTname] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTname] | bool:
            return isinstance(node, astClass) and DOT.name(node) is not None and attributeCondition(DOT.name(node))
        return workhorse

    @staticmethod
    @overload
    def namesIs(astClass: type[hasDOTnames_list_alias], attributeCondition: Callable[[list[ast.alias]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames_list_alias] | bool]:
        ...

    @staticmethod
    @overload
    def namesIs(astClass: type[hasDOTnames_list_Identifier], attributeCondition: Callable[[list[ast_Identifier]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames_list_Identifier] | bool]:
        ...

    @staticmethod
    def namesIs(astClass: type[hasDOTnames], attributeCondition: Callable[[list[ast.alias] | list[ast_Identifier]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTnames] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTnames] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.names(node))
        return workhorse

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_operator], attributeCondition: Callable[[ast.operator], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_operator] | bool]:
        ...

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_boolop], attributeCondition: Callable[[ast.boolop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_boolop] | bool]:
        ...

    @staticmethod
    @overload
    def opIs(astClass: type[hasDOTop_unaryop], attributeCondition: Callable[[ast.unaryop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop_unaryop] | bool]:
        ...

    @staticmethod
    def opIs(astClass: type[hasDOTop], attributeCondition: Callable[[ast.operator | ast.boolop | ast.unaryop], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTop] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTop] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.op(node))
        return workhorse

    @staticmethod
    def operandIs(astClass: type[hasDOToperand], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOToperand] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOToperand] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.operand(node))
        return workhorse

    @staticmethod
    def opsIs(astClass: type[hasDOTops], attributeCondition: Callable[[Sequence[ast.cmpop]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTops] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTops] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.ops(node))
        return workhorse

    @staticmethod
    def optional_varsIs(astClass: type[hasDOToptional_vars], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOToptional_vars] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOToptional_vars] | bool:
            return isinstance(node, astClass) and DOT.optional_vars(node) is not None and attributeCondition(DOT.optional_vars(node))
        return workhorse

    @staticmethod
    @overload
    def orelseIs(astClass: type[hasDOTorelse_list_stmt], attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse_list_stmt] | bool]:
        ...

    @staticmethod
    @overload
    def orelseIs(astClass: type[hasDOTorelse_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse_expr] | bool]:
        ...

    @staticmethod
    def orelseIs(astClass: type[hasDOTorelse], attributeCondition: Callable[[Sequence[ast.stmt] | ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTorelse] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTorelse] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.orelse(node))
        return workhorse

    @staticmethod
    @overload
    def patternIs(astClass: type[hasDOTpattern_Pattern], attributeCondition: Callable[[ast.pattern], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern_Pattern] | bool]:
        ...

    @staticmethod
    @overload
    def patternIs(astClass: type[hasDOTpattern_patternOrNone], attributeCondition: Callable[[ast.pattern | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern_patternOrNone] | bool]:
        ...

    @staticmethod
    def patternIs(astClass: type[hasDOTpattern], attributeCondition: Callable[[ast.pattern | (ast.pattern | None)], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpattern] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTpattern] | bool:
            return isinstance(node, astClass) and DOT.pattern(node) is not None and attributeCondition(DOT.pattern(node))
        return workhorse

    @staticmethod
    def patternsIs(astClass: type[hasDOTpatterns], attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTpatterns] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTpatterns] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.patterns(node))
        return workhorse

    @staticmethod
    def posonlyargsIs(astClass: type[hasDOTposonlyargs], attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTposonlyargs] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTposonlyargs] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.posonlyargs(node))
        return workhorse

    @staticmethod
    def restIs(astClass: type[hasDOTrest], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTrest] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTrest] | bool:
            return isinstance(node, astClass) and DOT.rest(node) is not None and attributeCondition(DOT.rest(node))
        return workhorse

    @staticmethod
    @overload
    def returnsIs(astClass: type[hasDOTreturns_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns_expr] | bool]:
        ...

    @staticmethod
    @overload
    def returnsIs(astClass: type[hasDOTreturns_exprOrNone], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns_exprOrNone] | bool]:
        ...

    @staticmethod
    def returnsIs(astClass: type[hasDOTreturns], attributeCondition: Callable[[ast.expr | (ast.expr | None)], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTreturns] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTreturns] | bool:
            return isinstance(node, astClass) and DOT.returns(node) is not None and attributeCondition(DOT.returns(node))
        return workhorse

    @staticmethod
    def rightIs(astClass: type[hasDOTright], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTright] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTright] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.right(node))
        return workhorse

    @staticmethod
    def simpleIs(astClass: type[hasDOTsimple], attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTsimple] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTsimple] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.simple(node))
        return workhorse

    @staticmethod
    def sliceIs(astClass: type[hasDOTslice], attributeCondition: Callable[[ast_expr_Slice], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTslice] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTslice] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.slice(node))
        return workhorse

    @staticmethod
    def stepIs(astClass: type[hasDOTstep], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTstep] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTstep] | bool:
            return isinstance(node, astClass) and DOT.step(node) is not None and attributeCondition(DOT.step(node))
        return workhorse

    @staticmethod
    def subjectIs(astClass: type[hasDOTsubject], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTsubject] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTsubject] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.subject(node))
        return workhorse

    @staticmethod
    def tagIs(astClass: type[hasDOTtag], attributeCondition: Callable[[ast_Identifier], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtag] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtag] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.tag(node))
        return workhorse

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_NameOrAttributeOrSubscript], attributeCondition: Callable[[ast.Name | ast.Attribute | ast.Subscript], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_NameOrAttributeOrSubscript] | bool]:
        ...

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_expr] | bool]:
        ...

    @staticmethod
    @overload
    def targetIs(astClass: type[hasDOTtarget_Name], attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget_Name] | bool]:
        ...

    @staticmethod
    def targetIs(astClass: type[hasDOTtarget], attributeCondition: Callable[[ast.Name | ast.Attribute | ast.Subscript | ast.expr | ast.Name], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtarget] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtarget] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.target(node))
        return workhorse

    @staticmethod
    def targetsIs(astClass: type[hasDOTtargets], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtargets] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtargets] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.targets(node))
        return workhorse

    @staticmethod
    def testIs(astClass: type[hasDOTtest], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtest] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtest] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.test(node))
        return workhorse

    @staticmethod
    def typeIs(astClass: type[hasDOTtype], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype] | bool:
            return isinstance(node, astClass) and DOT.type(node) is not None and attributeCondition(DOT.type(node))
        return workhorse

    @staticmethod
    def type_commentIs(astClass: type[hasDOTtype_comment], attributeCondition: Callable[[ast_Identifier | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_comment] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_comment] | bool:
            return isinstance(node, astClass) and DOT.type_comment(node) is not None and attributeCondition(DOT.type_comment(node))
        return workhorse

    @staticmethod
    def type_ignoresIs(astClass: type[hasDOTtype_ignores], attributeCondition: Callable[[list[ast.TypeIgnore]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_ignores] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_ignores] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.type_ignores(node))
        return workhorse

    @staticmethod
    def type_paramsIs(astClass: type[hasDOTtype_params], attributeCondition: Callable[[Sequence[astDOTtype_param]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTtype_params] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTtype_params] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.type_params(node))
        return workhorse

    @staticmethod
    def upperIs(astClass: type[hasDOTupper], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTupper] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTupper] | bool:
            return isinstance(node, astClass) and DOT.upper(node) is not None and attributeCondition(DOT.upper(node))
        return workhorse

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_exprOrNone], attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_exprOrNone] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_expr], attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_expr] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_Any], attributeCondition: Callable[[Any], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_Any] | bool]:
        ...

    @staticmethod
    @overload
    def valueIs(astClass: type[hasDOTvalue_LiteralTrueFalseOrNone], attributeCondition: Callable[[Literal[True, False] | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue_LiteralTrueFalseOrNone] | bool]:
        ...

    @staticmethod
    def valueIs(astClass: type[hasDOTvalue], attributeCondition: Callable[[ast.expr | None | ast.expr | Any | (Literal[True, False] | None)], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalue] | bool]: # type: ignore[reportInconsistentOverload]

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvalue] | bool:
            return isinstance(node, astClass) and DOT.value(node) is not None and attributeCondition(DOT.value(node))
        return workhorse

    @staticmethod
    def valuesIs(astClass: type[hasDOTvalues], attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvalues] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvalues] | bool:
            return isinstance(node, astClass) and attributeCondition(DOT.values(node))
        return workhorse

    @staticmethod
    def varargIs(astClass: type[hasDOTvararg], attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeGuard[hasDOTvararg] | bool]:

        def workhorse(node: ast.AST) -> TypeGuard[hasDOTvararg] | bool:
            return isinstance(node, astClass) and DOT.vararg(node) is not None and attributeCondition(DOT.vararg(node))
        return workhorse