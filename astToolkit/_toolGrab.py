# ruff: noqa: B009, B010
"""Automatically generated file, so changes may be overwritten."""
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
	hasDOTtype_params, hasDOTupper, hasDOTvalue, hasDOTvalues, hasDOTvararg, 一符, 个, 二符, 俪, 口, 工, 工位, 布尔符, 形, 比符)
from collections.abc import Callable, Sequence
from typing import Any
import ast
import sys

if sys.version_info >= (3, 13):
    from astToolkit import hasDOTdefault_value
if sys.version_info >= (3, 14):
    from astToolkit import hasDOTstr

class Grab:
    """Modify specific attributes of AST nodes while preserving the node structure.

    The Grab class provides static methods that create transformation functions to modify specific attributes of AST
    nodes. Unlike DOT which provides read-only access, Grab allows for targeted modifications of node attributes without
    replacing the entire node.

    Each method returns a function that takes a node, applies a transformation to a specific attribute of that node, and
    returns the modified node. This enables fine-grained control when transforming AST structures.
    """

    @staticmethod
    def andDoAllOf(listOfActions: Sequence[Callable[[Any], Any]]) -> Callable[[个], 个]:

        def workhorse(node: 个) -> 个:
            for action in listOfActions:
                node = action(node)
            return node
        return workhorse

    @staticmethod
    def index(at: int, /, action: Callable[[Any], Any]) -> Callable[[Sequence[个]], list[个]]:

        def workhorse(node: Sequence[个]) -> list[个]:
            node = list(node)
            consequences = action(node[at])
            if consequences is None:
                node.pop(at)
            elif isinstance(consequences, list):
                node = node[0:at] + consequences + node[at + 1:None]
            else:
                node[at] = consequences
            return node
        return workhorse

    @staticmethod
    def annotationAttribute(action: Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTannotation], hasDOTannotation]:
        """Apply a function to the `annotation` attribute of a 'node' of `type` `hasDOTannotation`.

        The `type` of the `annotation` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `annotation` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工] | Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTannotation], hasDOTannotation]
            A function with one parameter for a 'node' of `type` `hasDOTannotation` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTannotation) -> hasDOTannotation:
            setattr(node, 'annotation', action(getattr(node, 'annotation')))
            return node
        return workhorse

    @staticmethod
    def argAttribute(action: Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTarg], hasDOTarg]:
        """Apply a function to the `arg` attribute of a 'node' of `type` `hasDOTarg`.

        The `type` of the `arg` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `arg` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str], str] | Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTarg], hasDOTarg]
            A function with one parameter for a 'node' of `type` `hasDOTarg` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTarg) -> hasDOTarg:
            setattr(node, 'arg', action(getattr(node, 'arg')))
            return node
        return workhorse

    @staticmethod
    def argsAttribute(action: Callable[[ast.arguments], ast.arguments] | Callable[[list[ast.arg]], list[ast.arg]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTargs], hasDOTargs]:
        """Apply a function to the `args` attribute of a 'node' of `type` `hasDOTargs`.

        The `type` of the `args` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `args` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[ast.arguments], ast.arguments] | Callable[[list[ast.arg]], list[ast.arg]] |
        Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTargs], hasDOTargs]
            A function with one parameter for a 'node' of `type` `hasDOTargs` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTargs) -> hasDOTargs:
            setattr(node, 'args', action(getattr(node, 'args')))
            return node
        return workhorse

    @staticmethod
    def argtypesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTargtypes], hasDOTargtypes]:
        """Apply a function to the `argtypes` attribute of a 'node' of `type` `hasDOTargtypes`.

        The `type` of the `argtypes` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `argtypes` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTargtypes], hasDOTargtypes]
            A function with one parameter for a 'node' of `type` `hasDOTargtypes` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTargtypes) -> hasDOTargtypes:
            setattr(node, 'argtypes', action(getattr(node, 'argtypes')))
            return node
        return workhorse

    @staticmethod
    def asnameAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTasname], hasDOTasname]:
        """Apply a function to the `asname` attribute of a 'node' of `type` `hasDOTasname`.

        The `type` of the `asname` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `asname` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTasname], hasDOTasname]
            A function with one parameter for a 'node' of `type` `hasDOTasname` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTasname) -> hasDOTasname:
            setattr(node, 'asname', action(getattr(node, 'asname')))
            return node
        return workhorse

    @staticmethod
    def attrAttribute(action: Callable[[str], str]) -> Callable[[hasDOTattr], hasDOTattr]:
        """Apply a function to the `attr` attribute of a 'node' of `type` `hasDOTattr`.

        The `type` of the `attr` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `attr` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str], str]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTattr], hasDOTattr]
            A function with one parameter for a 'node' of `type` `hasDOTattr` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTattr) -> hasDOTattr:
            setattr(node, 'attr', action(getattr(node, 'attr')))
            return node
        return workhorse

    @staticmethod
    def basesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTbases], hasDOTbases]:
        """Apply a function to the `bases` attribute of a 'node' of `type` `hasDOTbases`.

        The `type` of the `bases` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `bases` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTbases], hasDOTbases]
            A function with one parameter for a 'node' of `type` `hasDOTbases` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTbases) -> hasDOTbases:
            setattr(node, 'bases', action(getattr(node, 'bases')))
            return node
        return workhorse

    @staticmethod
    def bodyAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTbody], hasDOTbody]:
        """Apply a function to the `body` attribute of a 'node' of `type` `hasDOTbody`.

        The `type` of the `body` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `body` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[口]], list[口]] | Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTbody], hasDOTbody]
            A function with one parameter for a 'node' of `type` `hasDOTbody` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTbody) -> hasDOTbody:
            setattr(node, 'body', action(getattr(node, 'body')))
            return node
        return workhorse

    @staticmethod
    def boundAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTbound], hasDOTbound]:
        """Apply a function to the `bound` attribute of a 'node' of `type` `hasDOTbound`.

        The `type` of the `bound` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `bound` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTbound], hasDOTbound]
            A function with one parameter for a 'node' of `type` `hasDOTbound` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTbound) -> hasDOTbound:
            setattr(node, 'bound', action(getattr(node, 'bound')))
            return node
        return workhorse

    @staticmethod
    def casesAttribute(action: Callable[[list[ast.match_case]], list[ast.match_case]]) -> Callable[[hasDOTcases], hasDOTcases]:
        """Apply a function to the `cases` attribute of a 'node' of `type` `hasDOTcases`.

        The `type` of the `cases` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `cases` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.match_case]], list[ast.match_case]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTcases], hasDOTcases]
            A function with one parameter for a 'node' of `type` `hasDOTcases` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTcases) -> hasDOTcases:
            setattr(node, 'cases', action(getattr(node, 'cases')))
            return node
        return workhorse

    @staticmethod
    def causeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTcause], hasDOTcause]:
        """Apply a function to the `cause` attribute of a 'node' of `type` `hasDOTcause`.

        The `type` of the `cause` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `cause` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTcause], hasDOTcause]
            A function with one parameter for a 'node' of `type` `hasDOTcause` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTcause) -> hasDOTcause:
            setattr(node, 'cause', action(getattr(node, 'cause')))
            return node
        return workhorse

    @staticmethod
    def clsAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcls], hasDOTcls]:
        """Apply a function to the `cls` attribute of a 'node' of `type` `hasDOTcls`.

        The `type` of the `cls` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `cls` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTcls], hasDOTcls]
            A function with one parameter for a 'node' of `type` `hasDOTcls` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTcls) -> hasDOTcls:
            setattr(node, 'cls', action(getattr(node, 'cls')))
            return node
        return workhorse

    @staticmethod
    def comparatorsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTcomparators], hasDOTcomparators]:
        """Apply a function to the `comparators` attribute of a 'node' of `type` `hasDOTcomparators`.

        The `type` of the `comparators` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `comparators` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTcomparators], hasDOTcomparators]
            A function with one parameter for a 'node' of `type` `hasDOTcomparators` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTcomparators) -> hasDOTcomparators:
            setattr(node, 'comparators', action(getattr(node, 'comparators')))
            return node
        return workhorse

    @staticmethod
    def context_exprAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcontext_expr], hasDOTcontext_expr]:
        """Apply a function to the `context_expr` attribute of a 'node' of `type` `hasDOTcontext_expr`.

        The `type` of the `context_expr` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `context_expr` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTcontext_expr], hasDOTcontext_expr]
            A function with one parameter for a 'node' of `type` `hasDOTcontext_expr` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTcontext_expr) -> hasDOTcontext_expr:
            setattr(node, 'context_expr', action(getattr(node, 'context_expr')))
            return node
        return workhorse

    @staticmethod
    def conversionAttribute(action: Callable[[int], int]) -> Callable[[hasDOTconversion], hasDOTconversion]:
        """Apply a function to the `conversion` attribute of a 'node' of `type` `hasDOTconversion`.

        The `type` of the `conversion` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `conversion` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[int], int]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTconversion], hasDOTconversion]
            A function with one parameter for a 'node' of `type` `hasDOTconversion` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTconversion) -> hasDOTconversion:
            setattr(node, 'conversion', action(getattr(node, 'conversion')))
            return node
        return workhorse

    @staticmethod
    def ctxAttribute(action: Callable[[工位], 工位]) -> Callable[[hasDOTctx], hasDOTctx]:
        """Apply a function to the `ctx` attribute of a 'node' of `type` `hasDOTctx`.

        The `type` of the `ctx` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `ctx` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工位], 工位]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTctx], hasDOTctx]
            A function with one parameter for a 'node' of `type` `hasDOTctx` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTctx) -> hasDOTctx:
            setattr(node, 'ctx', action(getattr(node, 'ctx')))
            return node
        return workhorse

    @staticmethod
    def decorator_listAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdecorator_list], hasDOTdecorator_list]:
        """Apply a function to the `decorator_list` attribute of a 'node' of `type` `hasDOTdecorator_list`.

        The `type` of the `decorator_list` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `decorator_list` could be a second type,
        I would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTdecorator_list], hasDOTdecorator_list]
            A function with one parameter for a 'node' of `type` `hasDOTdecorator_list` and a `return` of the same
            `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTdecorator_list) -> hasDOTdecorator_list:
            setattr(node, 'decorator_list', action(getattr(node, 'decorator_list')))
            return node
        return workhorse
    if sys.version_info >= (3, 13):

        @staticmethod
        def default_valueAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTdefault_value], hasDOTdefault_value]:
            """Apply a function to the `default_value` attribute of a 'node' of `type` `hasDOTdefault_value`.

            The `type` of the `default_value` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
            represented by a `TypeVar`, I would tell you what the ideogram is.  If `default_value` could be a second type, I
            would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

            Parameters
            ----------
            action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

            Returns
            -------
            workhorse : Callable[[hasDOTdefault_value], hasDOTdefault_value]
            A function with one parameter for a 'node' of `type` `hasDOTdefault_value` and a `return` of the same
            `type`.

            Type Checker Error?
            -------------------
            If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
            in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
            """

            def workhorse(node: hasDOTdefault_value) -> hasDOTdefault_value:
                setattr(node, 'default_value', action(getattr(node, 'default_value')))
                return node
            return workhorse

    @staticmethod
    def defaultsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdefaults], hasDOTdefaults]:
        """Apply a function to the `defaults` attribute of a 'node' of `type` `hasDOTdefaults`.

        The `type` of the `defaults` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `defaults` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTdefaults], hasDOTdefaults]
            A function with one parameter for a 'node' of `type` `hasDOTdefaults` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTdefaults) -> hasDOTdefaults:
            setattr(node, 'defaults', action(getattr(node, 'defaults')))
            return node
        return workhorse

    @staticmethod
    def eltAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTelt], hasDOTelt]:
        """Apply a function to the `elt` attribute of a 'node' of `type` `hasDOTelt`.

        The `type` of the `elt` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `elt` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTelt], hasDOTelt]
            A function with one parameter for a 'node' of `type` `hasDOTelt` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTelt) -> hasDOTelt:
            setattr(node, 'elt', action(getattr(node, 'elt')))
            return node
        return workhorse

    @staticmethod
    def eltsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTelts], hasDOTelts]:
        """Apply a function to the `elts` attribute of a 'node' of `type` `hasDOTelts`.

        The `type` of the `elts` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `elts` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTelts], hasDOTelts]
            A function with one parameter for a 'node' of `type` `hasDOTelts` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTelts) -> hasDOTelts:
            setattr(node, 'elts', action(getattr(node, 'elts')))
            return node
        return workhorse

    @staticmethod
    def excAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTexc], hasDOTexc]:
        """Apply a function to the `exc` attribute of a 'node' of `type` `hasDOTexc`.

        The `type` of the `exc` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `exc` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTexc], hasDOTexc]
            A function with one parameter for a 'node' of `type` `hasDOTexc` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTexc) -> hasDOTexc:
            setattr(node, 'exc', action(getattr(node, 'exc')))
            return node
        return workhorse

    @staticmethod
    def finalbodyAttribute(action: Callable[[list[口]], list[口]]) -> Callable[[hasDOTfinalbody], hasDOTfinalbody]:
        """Apply a function to the `finalbody` attribute of a 'node' of `type` `hasDOTfinalbody`.

        The `type` of the `finalbody` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `finalbody` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[口]], list[口]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTfinalbody], hasDOTfinalbody]
            A function with one parameter for a 'node' of `type` `hasDOTfinalbody` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTfinalbody) -> hasDOTfinalbody:
            setattr(node, 'finalbody', action(getattr(node, 'finalbody')))
            return node
        return workhorse

    @staticmethod
    def format_specAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTformat_spec], hasDOTformat_spec]:
        """Apply a function to the `format_spec` attribute of a 'node' of `type` `hasDOTformat_spec`.

        The `type` of the `format_spec` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `format_spec` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTformat_spec], hasDOTformat_spec]
            A function with one parameter for a 'node' of `type` `hasDOTformat_spec` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTformat_spec) -> hasDOTformat_spec:
            setattr(node, 'format_spec', action(getattr(node, 'format_spec')))
            return node
        return workhorse

    @staticmethod
    def funcAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTfunc], hasDOTfunc]:
        """Apply a function to the `func` attribute of a 'node' of `type` `hasDOTfunc`.

        The `type` of the `func` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `func` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTfunc], hasDOTfunc]
            A function with one parameter for a 'node' of `type` `hasDOTfunc` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTfunc) -> hasDOTfunc:
            setattr(node, 'func', action(getattr(node, 'func')))
            return node
        return workhorse

    @staticmethod
    def generatorsAttribute(action: Callable[[list[ast.comprehension]], list[ast.comprehension]]) -> Callable[[hasDOTgenerators], hasDOTgenerators]:
        """Apply a function to the `generators` attribute of a 'node' of `type` `hasDOTgenerators`.

        The `type` of the `generators` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `generators` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.comprehension]], list[ast.comprehension]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTgenerators], hasDOTgenerators]
            A function with one parameter for a 'node' of `type` `hasDOTgenerators` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTgenerators) -> hasDOTgenerators:
            setattr(node, 'generators', action(getattr(node, 'generators')))
            return node
        return workhorse

    @staticmethod
    def guardAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTguard], hasDOTguard]:
        """Apply a function to the `guard` attribute of a 'node' of `type` `hasDOTguard`.

        The `type` of the `guard` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `guard` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTguard], hasDOTguard]
            A function with one parameter for a 'node' of `type` `hasDOTguard` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTguard) -> hasDOTguard:
            setattr(node, 'guard', action(getattr(node, 'guard')))
            return node
        return workhorse

    @staticmethod
    def handlersAttribute(action: Callable[[list[ast.ExceptHandler]], list[ast.ExceptHandler]]) -> Callable[[hasDOThandlers], hasDOThandlers]:
        """Apply a function to the `handlers` attribute of a 'node' of `type` `hasDOThandlers`.

        The `type` of the `handlers` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `handlers` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.ExceptHandler]], list[ast.ExceptHandler]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOThandlers], hasDOThandlers]
            A function with one parameter for a 'node' of `type` `hasDOThandlers` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOThandlers) -> hasDOThandlers:
            setattr(node, 'handlers', action(getattr(node, 'handlers')))
            return node
        return workhorse

    @staticmethod
    def idAttribute(action: Callable[[str], str]) -> Callable[[hasDOTid], hasDOTid]:
        """Apply a function to the `id` attribute of a 'node' of `type` `hasDOTid`.

        The `type` of the `id` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by a
        `TypeVar`, I would tell you what the ideogram is.  If `id` could be a second type, I would tell you it is `type`
        `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str], str]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTid], hasDOTid]
            A function with one parameter for a 'node' of `type` `hasDOTid` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTid) -> hasDOTid:
            setattr(node, 'id', action(getattr(node, 'id')))
            return node
        return workhorse

    @staticmethod
    def ifsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTifs], hasDOTifs]:
        """Apply a function to the `ifs` attribute of a 'node' of `type` `hasDOTifs`.

        The `type` of the `ifs` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `ifs` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTifs], hasDOTifs]
            A function with one parameter for a 'node' of `type` `hasDOTifs` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTifs) -> hasDOTifs:
            setattr(node, 'ifs', action(getattr(node, 'ifs')))
            return node
        return workhorse

    @staticmethod
    def is_asyncAttribute(action: Callable[[int], int]) -> Callable[[hasDOTis_async], hasDOTis_async]:
        """Apply a function to the `is_async` attribute of a 'node' of `type` `hasDOTis_async`.

        The `type` of the `is_async` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `is_async` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[int], int]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTis_async], hasDOTis_async]
            A function with one parameter for a 'node' of `type` `hasDOTis_async` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTis_async) -> hasDOTis_async:
            setattr(node, 'is_async', action(getattr(node, 'is_async')))
            return node
        return workhorse

    @staticmethod
    def itemsAttribute(action: Callable[[list[ast.withitem]], list[ast.withitem]]) -> Callable[[hasDOTitems], hasDOTitems]:
        """Apply a function to the `items` attribute of a 'node' of `type` `hasDOTitems`.

        The `type` of the `items` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `items` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.withitem]], list[ast.withitem]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTitems], hasDOTitems]
            A function with one parameter for a 'node' of `type` `hasDOTitems` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTitems) -> hasDOTitems:
            setattr(node, 'items', action(getattr(node, 'items')))
            return node
        return workhorse

    @staticmethod
    def iterAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTiter], hasDOTiter]:
        """Apply a function to the `iter` attribute of a 'node' of `type` `hasDOTiter`.

        The `type` of the `iter` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `iter` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTiter], hasDOTiter]
            A function with one parameter for a 'node' of `type` `hasDOTiter` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTiter) -> hasDOTiter:
            setattr(node, 'iter', action(getattr(node, 'iter')))
            return node
        return workhorse

    @staticmethod
    def keyAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTkey], hasDOTkey]:
        """Apply a function to the `key` attribute of a 'node' of `type` `hasDOTkey`.

        The `type` of the `key` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `key` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkey], hasDOTkey]
            A function with one parameter for a 'node' of `type` `hasDOTkey` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkey) -> hasDOTkey:
            setattr(node, 'key', action(getattr(node, 'key')))
            return node
        return workhorse

    @staticmethod
    def keysAttribute(action: Callable[[list[工 | None]], list[工 | None]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTkeys], hasDOTkeys]:
        """Apply a function to the `keys` attribute of a 'node' of `type` `hasDOTkeys`.

        The `type` of the `keys` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `keys` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工 | None]], list[工 | None]] | Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkeys], hasDOTkeys]
            A function with one parameter for a 'node' of `type` `hasDOTkeys` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkeys) -> hasDOTkeys:
            setattr(node, 'keys', action(getattr(node, 'keys')))
            return node
        return workhorse

    @staticmethod
    def keywordsAttribute(action: Callable[[list[ast.keyword]], list[ast.keyword]]) -> Callable[[hasDOTkeywords], hasDOTkeywords]:
        """Apply a function to the `keywords` attribute of a 'node' of `type` `hasDOTkeywords`.

        The `type` of the `keywords` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `keywords` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.keyword]], list[ast.keyword]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkeywords], hasDOTkeywords]
            A function with one parameter for a 'node' of `type` `hasDOTkeywords` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkeywords) -> hasDOTkeywords:
            setattr(node, 'keywords', action(getattr(node, 'keywords')))
            return node
        return workhorse

    @staticmethod
    def kindAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTkind], hasDOTkind]:
        """Apply a function to the `kind` attribute of a 'node' of `type` `hasDOTkind`.

        The `type` of the `kind` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `kind` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkind], hasDOTkind]
            A function with one parameter for a 'node' of `type` `hasDOTkind` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkind) -> hasDOTkind:
            setattr(node, 'kind', action(getattr(node, 'kind')))
            return node
        return workhorse

    @staticmethod
    def kw_defaultsAttribute(action: Callable[[list[工 | None]], list[工 | None]]) -> Callable[[hasDOTkw_defaults], hasDOTkw_defaults]:
        """Apply a function to the `kw_defaults` attribute of a 'node' of `type` `hasDOTkw_defaults`.

        The `type` of the `kw_defaults` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `kw_defaults` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工 | None]], list[工 | None]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkw_defaults], hasDOTkw_defaults]
            A function with one parameter for a 'node' of `type` `hasDOTkw_defaults` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkw_defaults) -> hasDOTkw_defaults:
            setattr(node, 'kw_defaults', action(getattr(node, 'kw_defaults')))
            return node
        return workhorse

    @staticmethod
    def kwargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTkwarg], hasDOTkwarg]:
        """Apply a function to the `kwarg` attribute of a 'node' of `type` `hasDOTkwarg`.

        The `type` of the `kwarg` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `kwarg` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[ast.arg | None], ast.arg | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkwarg], hasDOTkwarg]
            A function with one parameter for a 'node' of `type` `hasDOTkwarg` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkwarg) -> hasDOTkwarg:
            setattr(node, 'kwarg', action(getattr(node, 'kwarg')))
            return node
        return workhorse

    @staticmethod
    def kwd_attrsAttribute(action: Callable[[list[str]], list[str]]) -> Callable[[hasDOTkwd_attrs], hasDOTkwd_attrs]:
        """Apply a function to the `kwd_attrs` attribute of a 'node' of `type` `hasDOTkwd_attrs`.

        The `type` of the `kwd_attrs` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `kwd_attrs` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[str]], list[str]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkwd_attrs], hasDOTkwd_attrs]
            A function with one parameter for a 'node' of `type` `hasDOTkwd_attrs` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkwd_attrs) -> hasDOTkwd_attrs:
            setattr(node, 'kwd_attrs', action(getattr(node, 'kwd_attrs')))
            return node
        return workhorse

    @staticmethod
    def kwd_patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTkwd_patterns], hasDOTkwd_patterns]:
        """Apply a function to the `kwd_patterns` attribute of a 'node' of `type` `hasDOTkwd_patterns`.

        The `type` of the `kwd_patterns` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `kwd_patterns` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[俪]], list[俪]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkwd_patterns], hasDOTkwd_patterns]
            A function with one parameter for a 'node' of `type` `hasDOTkwd_patterns` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkwd_patterns) -> hasDOTkwd_patterns:
            setattr(node, 'kwd_patterns', action(getattr(node, 'kwd_patterns')))
            return node
        return workhorse

    @staticmethod
    def kwonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTkwonlyargs], hasDOTkwonlyargs]:
        """Apply a function to the `kwonlyargs` attribute of a 'node' of `type` `hasDOTkwonlyargs`.

        The `type` of the `kwonlyargs` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `kwonlyargs` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.arg]], list[ast.arg]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTkwonlyargs], hasDOTkwonlyargs]
            A function with one parameter for a 'node' of `type` `hasDOTkwonlyargs` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTkwonlyargs) -> hasDOTkwonlyargs:
            setattr(node, 'kwonlyargs', action(getattr(node, 'kwonlyargs')))
            return node
        return workhorse

    @staticmethod
    def leftAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTleft], hasDOTleft]:
        """Apply a function to the `left` attribute of a 'node' of `type` `hasDOTleft`.

        The `type` of the `left` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `left` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTleft], hasDOTleft]
            A function with one parameter for a 'node' of `type` `hasDOTleft` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTleft) -> hasDOTleft:
            setattr(node, 'left', action(getattr(node, 'left')))
            return node
        return workhorse

    @staticmethod
    def levelAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlevel], hasDOTlevel]:
        """Apply a function to the `level` attribute of a 'node' of `type` `hasDOTlevel`.

        The `type` of the `level` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `level` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[int], int]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTlevel], hasDOTlevel]
            A function with one parameter for a 'node' of `type` `hasDOTlevel` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTlevel) -> hasDOTlevel:
            setattr(node, 'level', action(getattr(node, 'level')))
            return node
        return workhorse

    @staticmethod
    def linenoAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlineno], hasDOTlineno]:
        """Apply a function to the `lineno` attribute of a 'node' of `type` `hasDOTlineno`.

        The `type` of the `lineno` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `lineno` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[int], int]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTlineno], hasDOTlineno]
            A function with one parameter for a 'node' of `type` `hasDOTlineno` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTlineno) -> hasDOTlineno:
            setattr(node, 'lineno', action(getattr(node, 'lineno')))
            return node
        return workhorse

    @staticmethod
    def lowerAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTlower], hasDOTlower]:
        """Apply a function to the `lower` attribute of a 'node' of `type` `hasDOTlower`.

        The `type` of the `lower` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `lower` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTlower], hasDOTlower]
            A function with one parameter for a 'node' of `type` `hasDOTlower` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTlower) -> hasDOTlower:
            setattr(node, 'lower', action(getattr(node, 'lower')))
            return node
        return workhorse

    @staticmethod
    def moduleAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTmodule], hasDOTmodule]:
        """Apply a function to the `module` attribute of a 'node' of `type` `hasDOTmodule`.

        The `type` of the `module` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `module` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTmodule], hasDOTmodule]
            A function with one parameter for a 'node' of `type` `hasDOTmodule` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTmodule) -> hasDOTmodule:
            setattr(node, 'module', action(getattr(node, 'module')))
            return node
        return workhorse

    @staticmethod
    def msgAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTmsg], hasDOTmsg]:
        """Apply a function to the `msg` attribute of a 'node' of `type` `hasDOTmsg`.

        The `type` of the `msg` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `msg` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTmsg], hasDOTmsg]
            A function with one parameter for a 'node' of `type` `hasDOTmsg` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTmsg) -> hasDOTmsg:
            setattr(node, 'msg', action(getattr(node, 'msg')))
            return node
        return workhorse

    @staticmethod
    def nameAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTname], hasDOTname]:
        """Apply a function to the `name` attribute of a 'node' of `type` `hasDOTname`.

        The `type` of the `name` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `name` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[ast.Name], ast.Name] | Callable[[str], str] | Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTname], hasDOTname]
            A function with one parameter for a 'node' of `type` `hasDOTname` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTname) -> hasDOTname:
            setattr(node, 'name', action(getattr(node, 'name')))
            return node
        return workhorse

    @staticmethod
    def namesAttribute(action: Callable[[list[ast.alias]], list[ast.alias]] | Callable[[list[str]], list[str]]) -> Callable[[hasDOTnames], hasDOTnames]:
        """Apply a function to the `names` attribute of a 'node' of `type` `hasDOTnames`.

        The `type` of the `names` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `names` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.alias]], list[ast.alias]] | Callable[[list[str]], list[str]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTnames], hasDOTnames]
            A function with one parameter for a 'node' of `type` `hasDOTnames` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTnames) -> hasDOTnames:
            setattr(node, 'names', action(getattr(node, 'names')))
            return node
        return workhorse

    @staticmethod
    def opAttribute(action: Callable[[一符], 一符] | Callable[[二符], 二符] | Callable[[布尔符], 布尔符]) -> Callable[[hasDOTop], hasDOTop]:
        """Apply a function to the `op` attribute of a 'node' of `type` `hasDOTop`.

        The `type` of the `op` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by a
        `TypeVar`, I would tell you what the ideogram is.  If `op` could be a second type, I would tell you it is `type`
        `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[一符], 一符] | Callable[[二符], 二符] | Callable[[布尔符], 布尔符]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTop], hasDOTop]
            A function with one parameter for a 'node' of `type` `hasDOTop` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTop) -> hasDOTop:
            setattr(node, 'op', action(getattr(node, 'op')))
            return node
        return workhorse

    @staticmethod
    def operandAttribute(action: Callable[[工], 工]) -> Callable[[hasDOToperand], hasDOToperand]:
        """Apply a function to the `operand` attribute of a 'node' of `type` `hasDOToperand`.

        The `type` of the `operand` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `operand` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOToperand], hasDOToperand]
            A function with one parameter for a 'node' of `type` `hasDOToperand` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOToperand) -> hasDOToperand:
            setattr(node, 'operand', action(getattr(node, 'operand')))
            return node
        return workhorse

    @staticmethod
    def opsAttribute(action: Callable[[list[比符]], list[比符]]) -> Callable[[hasDOTops], hasDOTops]:
        """Apply a function to the `ops` attribute of a 'node' of `type` `hasDOTops`.

        The `type` of the `ops` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `ops` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[比符]], list[比符]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTops], hasDOTops]
            A function with one parameter for a 'node' of `type` `hasDOTops` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTops) -> hasDOTops:
            setattr(node, 'ops', action(getattr(node, 'ops')))
            return node
        return workhorse

    @staticmethod
    def optional_varsAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOToptional_vars], hasDOToptional_vars]:
        """Apply a function to the `optional_vars` attribute of a 'node' of `type` `hasDOToptional_vars`.

        The `type` of the `optional_vars` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `optional_vars` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOToptional_vars], hasDOToptional_vars]
            A function with one parameter for a 'node' of `type` `hasDOToptional_vars` and a `return` of the same
            `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOToptional_vars) -> hasDOToptional_vars:
            setattr(node, 'optional_vars', action(getattr(node, 'optional_vars')))
            return node
        return workhorse

    @staticmethod
    def orelseAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTorelse], hasDOTorelse]:
        """Apply a function to the `orelse` attribute of a 'node' of `type` `hasDOTorelse`.

        The `type` of the `orelse` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `orelse` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[口]], list[口]] | Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTorelse], hasDOTorelse]
            A function with one parameter for a 'node' of `type` `hasDOTorelse` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTorelse) -> hasDOTorelse:
            setattr(node, 'orelse', action(getattr(node, 'orelse')))
            return node
        return workhorse

    @staticmethod
    def patternAttribute(action: Callable[[俪], 俪] | Callable[[俪 | None], 俪 | None]) -> Callable[[hasDOTpattern], hasDOTpattern]:
        """Apply a function to the `pattern` attribute of a 'node' of `type` `hasDOTpattern`.

        The `type` of the `pattern` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `pattern` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[俪], 俪] | Callable[[俪 | None], 俪 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTpattern], hasDOTpattern]
            A function with one parameter for a 'node' of `type` `hasDOTpattern` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTpattern) -> hasDOTpattern:
            setattr(node, 'pattern', action(getattr(node, 'pattern')))
            return node
        return workhorse

    @staticmethod
    def patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTpatterns], hasDOTpatterns]:
        """Apply a function to the `patterns` attribute of a 'node' of `type` `hasDOTpatterns`.

        The `type` of the `patterns` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `patterns` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[俪]], list[俪]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTpatterns], hasDOTpatterns]
            A function with one parameter for a 'node' of `type` `hasDOTpatterns` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTpatterns) -> hasDOTpatterns:
            setattr(node, 'patterns', action(getattr(node, 'patterns')))
            return node
        return workhorse

    @staticmethod
    def posonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTposonlyargs], hasDOTposonlyargs]:
        """Apply a function to the `posonlyargs` attribute of a 'node' of `type` `hasDOTposonlyargs`.

        The `type` of the `posonlyargs` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `posonlyargs` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.arg]], list[ast.arg]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTposonlyargs], hasDOTposonlyargs]
            A function with one parameter for a 'node' of `type` `hasDOTposonlyargs` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTposonlyargs) -> hasDOTposonlyargs:
            setattr(node, 'posonlyargs', action(getattr(node, 'posonlyargs')))
            return node
        return workhorse

    @staticmethod
    def restAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTrest], hasDOTrest]:
        """Apply a function to the `rest` attribute of a 'node' of `type` `hasDOTrest`.

        The `type` of the `rest` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `rest` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTrest], hasDOTrest]
            A function with one parameter for a 'node' of `type` `hasDOTrest` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTrest) -> hasDOTrest:
            setattr(node, 'rest', action(getattr(node, 'rest')))
            return node
        return workhorse

    @staticmethod
    def returnsAttribute(action: Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTreturns], hasDOTreturns]:
        """Apply a function to the `returns` attribute of a 'node' of `type` `hasDOTreturns`.

        The `type` of the `returns` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `returns` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工] | Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTreturns], hasDOTreturns]
            A function with one parameter for a 'node' of `type` `hasDOTreturns` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTreturns) -> hasDOTreturns:
            setattr(node, 'returns', action(getattr(node, 'returns')))
            return node
        return workhorse

    @staticmethod
    def rightAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTright], hasDOTright]:
        """Apply a function to the `right` attribute of a 'node' of `type` `hasDOTright`.

        The `type` of the `right` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `right` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTright], hasDOTright]
            A function with one parameter for a 'node' of `type` `hasDOTright` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTright) -> hasDOTright:
            setattr(node, 'right', action(getattr(node, 'right')))
            return node
        return workhorse

    @staticmethod
    def simpleAttribute(action: Callable[[int], int]) -> Callable[[hasDOTsimple], hasDOTsimple]:
        """Apply a function to the `simple` attribute of a 'node' of `type` `hasDOTsimple`.

        The `type` of the `simple` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `simple` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[int], int]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTsimple], hasDOTsimple]
            A function with one parameter for a 'node' of `type` `hasDOTsimple` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTsimple) -> hasDOTsimple:
            setattr(node, 'simple', action(getattr(node, 'simple')))
            return node
        return workhorse

    @staticmethod
    def sliceAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTslice], hasDOTslice]:
        """Apply a function to the `slice` attribute of a 'node' of `type` `hasDOTslice`.

        The `type` of the `slice` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `slice` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTslice], hasDOTslice]
            A function with one parameter for a 'node' of `type` `hasDOTslice` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTslice) -> hasDOTslice:
            setattr(node, 'slice', action(getattr(node, 'slice')))
            return node
        return workhorse

    @staticmethod
    def stepAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTstep], hasDOTstep]:
        """Apply a function to the `step` attribute of a 'node' of `type` `hasDOTstep`.

        The `type` of the `step` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `step` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTstep], hasDOTstep]
            A function with one parameter for a 'node' of `type` `hasDOTstep` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTstep) -> hasDOTstep:
            setattr(node, 'step', action(getattr(node, 'step')))
            return node
        return workhorse
    if sys.version_info >= (3, 14):

        @staticmethod
        def strAttribute(action: Callable[[str], str]) -> Callable[[hasDOTstr], hasDOTstr]:
            """Apply a function to the `str` attribute of a 'node' of `type` `hasDOTstr`.

            The `type` of the `str` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
            a `TypeVar`, I would tell you what the ideogram is.  If `str` could be a second type, I would tell you it is
            `type` `somethingElse` for [any of] `class` `ast.FML`.

            Parameters
            ----------
            action : Callable[[str], str]
            A function with one parameter and a `return` of the same `type`.

            Returns
            -------
            workhorse : Callable[[hasDOTstr], hasDOTstr]
            A function with one parameter for a 'node' of `type` `hasDOTstr` and a `return` of the same `type`.

            Type Checker Error?
            -------------------
            If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
            in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
            """

            def workhorse(node: hasDOTstr) -> hasDOTstr:
                setattr(node, 'str', action(getattr(node, 'str')))
                return node
            return workhorse

    @staticmethod
    def subjectAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTsubject], hasDOTsubject]:
        """Apply a function to the `subject` attribute of a 'node' of `type` `hasDOTsubject`.

        The `type` of the `subject` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `subject` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTsubject], hasDOTsubject]
            A function with one parameter for a 'node' of `type` `hasDOTsubject` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTsubject) -> hasDOTsubject:
            setattr(node, 'subject', action(getattr(node, 'subject')))
            return node
        return workhorse

    @staticmethod
    def tagAttribute(action: Callable[[str], str]) -> Callable[[hasDOTtag], hasDOTtag]:
        """Apply a function to the `tag` attribute of a 'node' of `type` `hasDOTtag`.

        The `type` of the `tag` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `tag` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str], str]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtag], hasDOTtag]
            A function with one parameter for a 'node' of `type` `hasDOTtag` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtag) -> hasDOTtag:
            setattr(node, 'tag', action(getattr(node, 'tag')))
            return node
        return workhorse

    @staticmethod
    def targetAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[ast.Name | ast.Attribute | ast.Subscript], ast.Name | ast.Attribute | ast.Subscript] | Callable[[工], 工]) -> Callable[[hasDOTtarget], hasDOTtarget]:
        """Apply a function to the `target` attribute of a 'node' of `type` `hasDOTtarget`.

        The `type` of the `target` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `target` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[ast.Name], ast.Name] | Callable[[ast.Name | ast.Attribute | ast.Subscript], ast.Name |
        ast.Attribute | ast.Subscript] | Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtarget], hasDOTtarget]
            A function with one parameter for a 'node' of `type` `hasDOTtarget` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtarget) -> hasDOTtarget:
            setattr(node, 'target', action(getattr(node, 'target')))
            return node
        return workhorse

    @staticmethod
    def targetsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTtargets], hasDOTtargets]:
        """Apply a function to the `targets` attribute of a 'node' of `type` `hasDOTtargets`.

        The `type` of the `targets` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `targets` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtargets], hasDOTtargets]
            A function with one parameter for a 'node' of `type` `hasDOTtargets` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtargets) -> hasDOTtargets:
            setattr(node, 'targets', action(getattr(node, 'targets')))
            return node
        return workhorse

    @staticmethod
    def testAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTtest], hasDOTtest]:
        """Apply a function to the `test` attribute of a 'node' of `type` `hasDOTtest`.

        The `type` of the `test` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `test` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工], 工]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtest], hasDOTtest]
            A function with one parameter for a 'node' of `type` `hasDOTtest` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtest) -> hasDOTtest:
            setattr(node, 'test', action(getattr(node, 'test')))
            return node
        return workhorse

    @staticmethod
    def typeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTtype], hasDOTtype]:
        """Apply a function to the `type` attribute of a 'node' of `type` `hasDOTtype`.

        The `type` of the `type` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented by
        a `TypeVar`, I would tell you what the ideogram is.  If `type` could be a second type, I would tell you it is
        `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtype], hasDOTtype]
            A function with one parameter for a 'node' of `type` `hasDOTtype` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtype) -> hasDOTtype:
            setattr(node, 'type', action(getattr(node, 'type')))
            return node
        return workhorse

    @staticmethod
    def type_commentAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTtype_comment], hasDOTtype_comment]:
        """Apply a function to the `type_comment` attribute of a 'node' of `type` `hasDOTtype_comment`.

        The `type` of the `type_comment` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `type_comment` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[str | None], str | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_comment], hasDOTtype_comment]
            A function with one parameter for a 'node' of `type` `hasDOTtype_comment` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtype_comment) -> hasDOTtype_comment:
            setattr(node, 'type_comment', action(getattr(node, 'type_comment')))
            return node
        return workhorse

    @staticmethod
    def type_ignoresAttribute(action: Callable[[list[ast.TypeIgnore]], list[ast.TypeIgnore]]) -> Callable[[hasDOTtype_ignores], hasDOTtype_ignores]:
        """Apply a function to the `type_ignores` attribute of a 'node' of `type` `hasDOTtype_ignores`.

        The `type` of the `type_ignores` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `type_ignores` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[ast.TypeIgnore]], list[ast.TypeIgnore]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_ignores], hasDOTtype_ignores]
            A function with one parameter for a 'node' of `type` `hasDOTtype_ignores` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtype_ignores) -> hasDOTtype_ignores:
            setattr(node, 'type_ignores', action(getattr(node, 'type_ignores')))
            return node
        return workhorse

    @staticmethod
    def type_paramsAttribute(action: Callable[[list[形]], list[形]]) -> Callable[[hasDOTtype_params], hasDOTtype_params]:
        """Apply a function to the `type_params` attribute of a 'node' of `type` `hasDOTtype_params`.

        The `type` of the `type_params` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were
        represented by a `TypeVar`, I would tell you what the ideogram is.  If `type_params` could be a second type, I
        would tell you it is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[形]], list[形]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_params], hasDOTtype_params]
            A function with one parameter for a 'node' of `type` `hasDOTtype_params` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTtype_params) -> hasDOTtype_params:
            setattr(node, 'type_params', action(getattr(node, 'type_params')))
            return node
        return workhorse

    @staticmethod
    def upperAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTupper], hasDOTupper]:
        """Apply a function to the `upper` attribute of a 'node' of `type` `hasDOTupper`.

        The `type` of the `upper` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `upper` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTupper], hasDOTupper]
            A function with one parameter for a 'node' of `type` `hasDOTupper` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTupper) -> hasDOTupper:
            setattr(node, 'upper', action(getattr(node, 'upper')))
            return node
        return workhorse

    @staticmethod
    def valueAttribute(action: Callable[[bool | None], bool | None] | Callable[[ConstantValueType], ConstantValueType] | Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTvalue], hasDOTvalue]:
        """Apply a function to the `value` attribute of a 'node' of `type` `hasDOTvalue`.

        The `type` of the `value` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `value` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[bool | None], bool | None] | Callable[[ConstantValueType], ConstantValueType] | Callable[[工],
        工] | Callable[[工 | None], 工 | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTvalue], hasDOTvalue]
            A function with one parameter for a 'node' of `type` `hasDOTvalue` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTvalue) -> hasDOTvalue:
            setattr(node, 'value', action(getattr(node, 'value')))
            return node
        return workhorse

    @staticmethod
    def valuesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTvalues], hasDOTvalues]:
        """Apply a function to the `values` attribute of a 'node' of `type` `hasDOTvalues`.

        The `type` of the `values` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `values` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[list[工]], list[工]]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTvalues], hasDOTvalues]
            A function with one parameter for a 'node' of `type` `hasDOTvalues` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTvalues) -> hasDOTvalues:
            setattr(node, 'values', action(getattr(node, 'values')))
            return node
        return workhorse

    @staticmethod
    def varargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTvararg], hasDOTvararg]:
        """Apply a function to the `vararg` attribute of a 'node' of `type` `hasDOTvararg`.

        The `type` of the `vararg` attribute is `something` for [any of] `class` `ast.IDK`.  If `type` were represented
        by a `TypeVar`, I would tell you what the ideogram is.  If `vararg` could be a second type, I would tell you it
        is `type` `somethingElse` for [any of] `class` `ast.FML`.

        Parameters
        ----------
        action : Callable[[ast.arg | None], ast.arg | None]
            A function with one parameter and a `return` of the same `type`.

        Returns
        -------
        workhorse : Callable[[hasDOTvararg], hasDOTvararg]
            A function with one parameter for a 'node' of `type` `hasDOTvararg` and a `return` of the same `type`.

        Type Checker Error?
        -------------------
        If you use `Grab` with one level of complexity, your type checker will give you accurate guidance. With two levels of complexity, such as nesting `Grab`
        in another `Grab`, your type checker will be angry. I recommend `typing.cast()`. The fault is mine: the 'type safety' of `Grab` is inherently limited.
        """

        def workhorse(node: hasDOTvararg) -> hasDOTvararg:
            setattr(node, 'vararg', action(getattr(node, 'vararg')))
            return node
        return workhorse
