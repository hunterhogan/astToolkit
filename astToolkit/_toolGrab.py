# ruff: noqa: B009, B010
"""Automatically generated file, so changes may be overwritten."""
from __future__ import annotations

from typing import TYPE_CHECKING
import sys

if TYPE_CHECKING:
    from astToolkit.theTypes import (
        ast_ConstantValue, hasDOTannotation, hasDOTarg, hasDOTargs, hasDOTargtypes, hasDOTasname, hasDOTattr, hasDOTbases, hasDOTbody,
        hasDOTbound, hasDOTcases, hasDOTcause, hasDOTcls, hasDOTcomparators, hasDOTcontext_expr, hasDOTconversion, hasDOTctx,
        hasDOTdecorator_list, hasDOTdefault_value, hasDOTdefaults, hasDOTelt, hasDOTelts, hasDOTexc, hasDOTfinalbody, hasDOTformat_spec,
        hasDOTfunc, hasDOTgenerators, hasDOTguard, hasDOThandlers, hasDOTid, hasDOTifs, hasDOTis_async, hasDOTitems, hasDOTiter, hasDOTkey,
        hasDOTkeys, hasDOTkeywords, hasDOTkind, hasDOTkw_defaults, hasDOTkwarg, hasDOTkwd_attrs, hasDOTkwd_patterns, hasDOTkwonlyargs,
        hasDOTleft, hasDOTlevel, hasDOTlineno, hasDOTlower, hasDOTmodule, hasDOTmsg, hasDOTname, hasDOTnames, hasDOTop, hasDOToperand,
        hasDOTops, hasDOToptional_vars, hasDOTorelse, hasDOTpattern, hasDOTpatterns, hasDOTposonlyargs, hasDOTrest, hasDOTreturns,
        hasDOTright, hasDOTsimple, hasDOTslice, hasDOTstep, hasDOTstr, hasDOTsubject, hasDOTtag, hasDOTtarget, hasDOTtargets, hasDOTtest,
        hasDOTtype, hasDOTtype_comment, hasDOTtype_ignores, hasDOTtype_params, hasDOTupper, hasDOTvalue, hasDOTvalues, hasDOTvararg, 一符, 个,
        二符, 俪, 口, 工, 工位, 布尔符, 形, 比符)
    from collections.abc import Callable, Sequence
    from typing import Any
    import ast
    if sys.version_info >= (3, 15):
        from astToolkit.theTypes import hasDOTis_lazy

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
        """Apply `action` to the `annotation` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.AnnAssign`. The `action` annotation uses `工` for this
        type.

        The field has type `ast.expr | None` on `ast.arg`. The `action` annotation uses `工 | None` for
        this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTannotation], hasDOTannotation]
            A function that updates the node's `annotation` field in place and returns the same node.
        """

        def workhorse(node: hasDOTannotation) -> hasDOTannotation:
            setattr(node, 'annotation', action(getattr(node, 'annotation')))
            return node
        return workhorse

    @staticmethod
    def argAttribute(action: Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTarg], hasDOTarg]:
        """Apply `action` to the `arg` field of an AST node.

        (AI generated docstring)

        The field has type `str` on `ast.arg`.

        The field has type `str | None` on `ast.keyword`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTarg], hasDOTarg]
            A function that updates the node's `arg` field in place and returns the same node.
        """

        def workhorse(node: hasDOTarg) -> hasDOTarg:
            setattr(node, 'arg', action(getattr(node, 'arg')))
            return node
        return workhorse

    @staticmethod
    def argsAttribute(action: Callable[[ast.arguments], ast.arguments] | Callable[[list[ast.arg]], list[ast.arg]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTargs], hasDOTargs]:
        """Apply `action` to the `args` field of an AST node.

        (AI generated docstring)

        The field has type `ast.arguments` on `ast.AsyncFunctionDef`, `ast.FunctionDef`, `ast.Lambda`.

        The field has type `list[ast.arg]` on `ast.arguments`.

        The field has type `list[ast.expr]` on `ast.Call`. The `action` annotation uses `list[工]` for
        this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTargs], hasDOTargs]
            A function that updates the node's `args` field in place and returns the same node.
        """

        def workhorse(node: hasDOTargs) -> hasDOTargs:
            setattr(node, 'args', action(getattr(node, 'args')))
            return node
        return workhorse

    @staticmethod
    def argtypesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTargtypes], hasDOTargtypes]:
        """Apply `action` to the `argtypes` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.FunctionType`. The `action` annotation uses
        `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTargtypes], hasDOTargtypes]
            A function that updates the node's `argtypes` field in place and returns the same node.
        """

        def workhorse(node: hasDOTargtypes) -> hasDOTargtypes:
            setattr(node, 'argtypes', action(getattr(node, 'argtypes')))
            return node
        return workhorse

    @staticmethod
    def asnameAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTasname], hasDOTasname]:
        """Apply `action` to the `asname` field of an AST node.

        (AI generated docstring)

        The field has type `str | None` on `ast.alias`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTasname], hasDOTasname]
            A function that updates the node's `asname` field in place and returns the same node.
        """

        def workhorse(node: hasDOTasname) -> hasDOTasname:
            setattr(node, 'asname', action(getattr(node, 'asname')))
            return node
        return workhorse

    @staticmethod
    def attrAttribute(action: Callable[[str], str]) -> Callable[[hasDOTattr], hasDOTattr]:
        """Apply `action` to the `attr` field of an AST node.

        (AI generated docstring)

        The field has type `str` on `ast.Attribute`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTattr], hasDOTattr]
            A function that updates the node's `attr` field in place and returns the same node.
        """

        def workhorse(node: hasDOTattr) -> hasDOTattr:
            setattr(node, 'attr', action(getattr(node, 'attr')))
            return node
        return workhorse

    @staticmethod
    def basesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTbases], hasDOTbases]:
        """Apply `action` to the `bases` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.ClassDef`. The `action` annotation uses `list[工]`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTbases], hasDOTbases]
            A function that updates the node's `bases` field in place and returns the same node.
        """

        def workhorse(node: hasDOTbases) -> hasDOTbases:
            setattr(node, 'bases', action(getattr(node, 'bases')))
            return node
        return workhorse

    @staticmethod
    def bodyAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTbody], hasDOTbody]:
        """Apply `action` to the `body` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Expression`, `ast.IfExp`, `ast.Lambda`. The `action`
        annotation uses `工` for this type.

        The field has type `list[ast.stmt]` on `ast.AsyncFor`, `ast.AsyncFunctionDef`,
        `ast.AsyncWith`, `ast.ClassDef`, `ast.ExceptHandler`, `ast.For`, `ast.FunctionDef`, `ast.If`,
        `ast.Interactive`, `ast.Module`, `ast.Try`, `ast.TryStar`, `ast.While`, `ast.With`,
        `ast.match_case`. The `action` annotation uses `list[口]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTbody], hasDOTbody]
            A function that updates the node's `body` field in place and returns the same node.
        """

        def workhorse(node: hasDOTbody) -> hasDOTbody:
            setattr(node, 'body', action(getattr(node, 'body')))
            return node
        return workhorse

    @staticmethod
    def boundAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTbound], hasDOTbound]:
        """Apply `action` to the `bound` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.TypeVar`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTbound], hasDOTbound]
            A function that updates the node's `bound` field in place and returns the same node.
        """

        def workhorse(node: hasDOTbound) -> hasDOTbound:
            setattr(node, 'bound', action(getattr(node, 'bound')))
            return node
        return workhorse

    @staticmethod
    def casesAttribute(action: Callable[[list[ast.match_case]], list[ast.match_case]]) -> Callable[[hasDOTcases], hasDOTcases]:
        """Apply `action` to the `cases` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.match_case]` on `ast.Match`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTcases], hasDOTcases]
            A function that updates the node's `cases` field in place and returns the same node.
        """

        def workhorse(node: hasDOTcases) -> hasDOTcases:
            setattr(node, 'cases', action(getattr(node, 'cases')))
            return node
        return workhorse

    @staticmethod
    def causeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTcause], hasDOTcause]:
        """Apply `action` to the `cause` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Raise`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTcause], hasDOTcause]
            A function that updates the node's `cause` field in place and returns the same node.
        """

        def workhorse(node: hasDOTcause) -> hasDOTcause:
            setattr(node, 'cause', action(getattr(node, 'cause')))
            return node
        return workhorse

    @staticmethod
    def clsAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcls], hasDOTcls]:
        """Apply `action` to the `cls` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.MatchClass`. The `action` annotation uses `工` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTcls], hasDOTcls]
            A function that updates the node's `cls` field in place and returns the same node.
        """

        def workhorse(node: hasDOTcls) -> hasDOTcls:
            setattr(node, 'cls', action(getattr(node, 'cls')))
            return node
        return workhorse

    @staticmethod
    def comparatorsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTcomparators], hasDOTcomparators]:
        """Apply `action` to the `comparators` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.Compare`. The `action` annotation uses `list[工]`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTcomparators], hasDOTcomparators]
            A function that updates the node's `comparators` field in place and returns the same node.
        """

        def workhorse(node: hasDOTcomparators) -> hasDOTcomparators:
            setattr(node, 'comparators', action(getattr(node, 'comparators')))
            return node
        return workhorse

    @staticmethod
    def context_exprAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcontext_expr], hasDOTcontext_expr]:
        """Apply `action` to the `context_expr` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.withitem`. The `action` annotation uses `工` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTcontext_expr], hasDOTcontext_expr]
            A function that updates the node's `context_expr` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTcontext_expr) -> hasDOTcontext_expr:
            setattr(node, 'context_expr', action(getattr(node, 'context_expr')))
            return node
        return workhorse

    @staticmethod
    def conversionAttribute(action: Callable[[int], int]) -> Callable[[hasDOTconversion], hasDOTconversion]:
        """Apply `action` to the `conversion` field of an AST node.

        (AI generated docstring)

        The field has type `int` on `ast.FormattedValue`, `ast.Interpolation`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTconversion], hasDOTconversion]
            A function that updates the node's `conversion` field in place and returns the same node.
        """

        def workhorse(node: hasDOTconversion) -> hasDOTconversion:
            setattr(node, 'conversion', action(getattr(node, 'conversion')))
            return node
        return workhorse

    @staticmethod
    def ctxAttribute(action: Callable[[工位], 工位]) -> Callable[[hasDOTctx], hasDOTctx]:
        """Apply `action` to the `ctx` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr_context` on `ast.Attribute`, `ast.List`, `ast.Name`,
        `ast.Starred`, `ast.Subscript`, `ast.Tuple`. The `action` annotation uses `工位` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTctx], hasDOTctx]
            A function that updates the node's `ctx` field in place and returns the same node.
        """

        def workhorse(node: hasDOTctx) -> hasDOTctx:
            setattr(node, 'ctx', action(getattr(node, 'ctx')))
            return node
        return workhorse

    @staticmethod
    def decorator_listAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdecorator_list], hasDOTdecorator_list]:
        """Apply `action` to the `decorator_list` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.AsyncFunctionDef`, `ast.ClassDef`,
        `ast.FunctionDef`. The `action` annotation uses `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTdecorator_list], hasDOTdecorator_list]
            A function that updates the node's `decorator_list` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTdecorator_list) -> hasDOTdecorator_list:
            setattr(node, 'decorator_list', action(getattr(node, 'decorator_list')))
            return node
        return workhorse

    @staticmethod
    def default_valueAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTdefault_value], hasDOTdefault_value]:
        """Apply `action` to the `default_value` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.ParamSpec`, `ast.TypeVar`, `ast.TypeVarTuple`.
        The `action` annotation uses `工 | None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTdefault_value], hasDOTdefault_value]
            A function that updates the node's `default_value` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTdefault_value) -> hasDOTdefault_value:
            setattr(node, 'default_value', action(getattr(node, 'default_value')))
            return node
        return workhorse

    @staticmethod
    def defaultsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdefaults], hasDOTdefaults]:
        """Apply `action` to the `defaults` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.arguments`. The `action` annotation uses `list[工]`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTdefaults], hasDOTdefaults]
            A function that updates the node's `defaults` field in place and returns the same node.
        """

        def workhorse(node: hasDOTdefaults) -> hasDOTdefaults:
            setattr(node, 'defaults', action(getattr(node, 'defaults')))
            return node
        return workhorse

    @staticmethod
    def eltAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTelt], hasDOTelt]:
        """Apply `action` to the `elt` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.GeneratorExp`, `ast.ListComp`, `ast.SetComp`. The
        `action` annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTelt], hasDOTelt]
            A function that updates the node's `elt` field in place and returns the same node.
        """

        def workhorse(node: hasDOTelt) -> hasDOTelt:
            setattr(node, 'elt', action(getattr(node, 'elt')))
            return node
        return workhorse

    @staticmethod
    def eltsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTelts], hasDOTelts]:
        """Apply `action` to the `elts` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.List`, `ast.Set`, `ast.Tuple`. The `action`
        annotation uses `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTelts], hasDOTelts]
            A function that updates the node's `elts` field in place and returns the same node.
        """

        def workhorse(node: hasDOTelts) -> hasDOTelts:
            setattr(node, 'elts', action(getattr(node, 'elts')))
            return node
        return workhorse

    @staticmethod
    def excAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTexc], hasDOTexc]:
        """Apply `action` to the `exc` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Raise`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTexc], hasDOTexc]
            A function that updates the node's `exc` field in place and returns the same node.
        """

        def workhorse(node: hasDOTexc) -> hasDOTexc:
            setattr(node, 'exc', action(getattr(node, 'exc')))
            return node
        return workhorse

    @staticmethod
    def finalbodyAttribute(action: Callable[[list[口]], list[口]]) -> Callable[[hasDOTfinalbody], hasDOTfinalbody]:
        """Apply `action` to the `finalbody` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.stmt]` on `ast.Try`, `ast.TryStar`. The `action` annotation uses
        `list[口]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTfinalbody], hasDOTfinalbody]
            A function that updates the node's `finalbody` field in place and returns the same node.
        """

        def workhorse(node: hasDOTfinalbody) -> hasDOTfinalbody:
            setattr(node, 'finalbody', action(getattr(node, 'finalbody')))
            return node
        return workhorse

    @staticmethod
    def format_specAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTformat_spec], hasDOTformat_spec]:
        """Apply `action` to the `format_spec` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.FormattedValue`, `ast.Interpolation`. The
        `action` annotation uses `工 | None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTformat_spec], hasDOTformat_spec]
            A function that updates the node's `format_spec` field in place and returns the same node.
        """

        def workhorse(node: hasDOTformat_spec) -> hasDOTformat_spec:
            setattr(node, 'format_spec', action(getattr(node, 'format_spec')))
            return node
        return workhorse

    @staticmethod
    def funcAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTfunc], hasDOTfunc]:
        """Apply `action` to the `func` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Call`. The `action` annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTfunc], hasDOTfunc]
            A function that updates the node's `func` field in place and returns the same node.
        """

        def workhorse(node: hasDOTfunc) -> hasDOTfunc:
            setattr(node, 'func', action(getattr(node, 'func')))
            return node
        return workhorse

    @staticmethod
    def generatorsAttribute(action: Callable[[list[ast.comprehension]], list[ast.comprehension]]) -> Callable[[hasDOTgenerators], hasDOTgenerators]:
        """Apply `action` to the `generators` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.comprehension]` on `ast.DictComp`, `ast.GeneratorExp`,
        `ast.ListComp`, `ast.SetComp`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTgenerators], hasDOTgenerators]
            A function that updates the node's `generators` field in place and returns the same node.
        """

        def workhorse(node: hasDOTgenerators) -> hasDOTgenerators:
            setattr(node, 'generators', action(getattr(node, 'generators')))
            return node
        return workhorse

    @staticmethod
    def guardAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTguard], hasDOTguard]:
        """Apply `action` to the `guard` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.match_case`. The `action` annotation uses `工 |
        None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTguard], hasDOTguard]
            A function that updates the node's `guard` field in place and returns the same node.
        """

        def workhorse(node: hasDOTguard) -> hasDOTguard:
            setattr(node, 'guard', action(getattr(node, 'guard')))
            return node
        return workhorse

    @staticmethod
    def handlersAttribute(action: Callable[[list[ast.ExceptHandler]], list[ast.ExceptHandler]]) -> Callable[[hasDOThandlers], hasDOThandlers]:
        """Apply `action` to the `handlers` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.ExceptHandler]` on `ast.Try`, `ast.TryStar`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOThandlers], hasDOThandlers]
            A function that updates the node's `handlers` field in place and returns the same node.
        """

        def workhorse(node: hasDOThandlers) -> hasDOThandlers:
            setattr(node, 'handlers', action(getattr(node, 'handlers')))
            return node
        return workhorse

    @staticmethod
    def idAttribute(action: Callable[[str], str]) -> Callable[[hasDOTid], hasDOTid]:
        """Apply `action` to the `id` field of an AST node.

        (AI generated docstring)

        The field has type `str` on `ast.Name`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTid], hasDOTid]
            A function that updates the node's `id` field in place and returns the same node.
        """

        def workhorse(node: hasDOTid) -> hasDOTid:
            setattr(node, 'id', action(getattr(node, 'id')))
            return node
        return workhorse

    @staticmethod
    def ifsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTifs], hasDOTifs]:
        """Apply `action` to the `ifs` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.comprehension`. The `action` annotation uses
        `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTifs], hasDOTifs]
            A function that updates the node's `ifs` field in place and returns the same node.
        """

        def workhorse(node: hasDOTifs) -> hasDOTifs:
            setattr(node, 'ifs', action(getattr(node, 'ifs')))
            return node
        return workhorse

    @staticmethod
    def is_asyncAttribute(action: Callable[[int], int]) -> Callable[[hasDOTis_async], hasDOTis_async]:
        """Apply `action` to the `is_async` field of an AST node.

        (AI generated docstring)

        The field has type `int` on `ast.comprehension`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTis_async], hasDOTis_async]
            A function that updates the node's `is_async` field in place and returns the same node.
        """

        def workhorse(node: hasDOTis_async) -> hasDOTis_async:
            setattr(node, 'is_async', action(getattr(node, 'is_async')))
            return node
        return workhorse
    if sys.version_info >= (3, 15):

        @staticmethod
        def is_lazyAttribute(action: Callable[[bool | None], bool | None]) -> Callable[[hasDOTis_lazy], hasDOTis_lazy]:
            """Apply `action` to the `is_lazy` field of an AST node.

            (AI generated docstring)

            The field has type `bool | None` on `ast.Import`, `ast.ImportFrom`.

            Parameters
            ----------
            action : Callable
                A function that takes the field's current value and returns a replacement of the same
                type.

            Returns
            -------
            workhorse : Callable[[hasDOTis_lazy], hasDOTis_lazy]
                A function that updates the node's `is_lazy` field in place and returns the same node.
            """

            def workhorse(node: hasDOTis_lazy) -> hasDOTis_lazy:
                setattr(node, 'is_lazy', action(getattr(node, 'is_lazy')))
                return node
            return workhorse

    @staticmethod
    def itemsAttribute(action: Callable[[list[ast.withitem]], list[ast.withitem]]) -> Callable[[hasDOTitems], hasDOTitems]:
        """Apply `action` to the `items` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.withitem]` on `ast.AsyncWith`, `ast.With`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTitems], hasDOTitems]
            A function that updates the node's `items` field in place and returns the same node.
        """

        def workhorse(node: hasDOTitems) -> hasDOTitems:
            setattr(node, 'items', action(getattr(node, 'items')))
            return node
        return workhorse

    @staticmethod
    def iterAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTiter], hasDOTiter]:
        """Apply `action` to the `iter` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.AsyncFor`, `ast.For`, `ast.comprehension`. The `action`
        annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTiter], hasDOTiter]
            A function that updates the node's `iter` field in place and returns the same node.
        """

        def workhorse(node: hasDOTiter) -> hasDOTiter:
            setattr(node, 'iter', action(getattr(node, 'iter')))
            return node
        return workhorse

    @staticmethod
    def keyAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTkey], hasDOTkey]:
        """Apply `action` to the `key` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.DictComp`. The `action` annotation uses `工` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkey], hasDOTkey]
            A function that updates the node's `key` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkey) -> hasDOTkey:
            setattr(node, 'key', action(getattr(node, 'key')))
            return node
        return workhorse

    @staticmethod
    def keysAttribute(action: Callable[[list[工 | None]], list[工 | None]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTkeys], hasDOTkeys]:
        """Apply `action` to the `keys` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr | None]` on `ast.Dict`. The `action` annotation uses `list[工
        | None]` for this type.

        The field has type `list[ast.expr]` on `ast.MatchMapping`. The `action` annotation uses
        `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkeys], hasDOTkeys]
            A function that updates the node's `keys` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkeys) -> hasDOTkeys:
            setattr(node, 'keys', action(getattr(node, 'keys')))
            return node
        return workhorse

    @staticmethod
    def keywordsAttribute(action: Callable[[list[ast.keyword]], list[ast.keyword]]) -> Callable[[hasDOTkeywords], hasDOTkeywords]:
        """Apply `action` to the `keywords` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.keyword]` on `ast.Call`, `ast.ClassDef`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkeywords], hasDOTkeywords]
            A function that updates the node's `keywords` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkeywords) -> hasDOTkeywords:
            setattr(node, 'keywords', action(getattr(node, 'keywords')))
            return node
        return workhorse

    @staticmethod
    def kindAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTkind], hasDOTkind]:
        """Apply `action` to the `kind` field of an AST node.

        (AI generated docstring)

        The field has type `str | None` on `ast.Constant`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkind], hasDOTkind]
            A function that updates the node's `kind` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkind) -> hasDOTkind:
            setattr(node, 'kind', action(getattr(node, 'kind')))
            return node
        return workhorse

    @staticmethod
    def kw_defaultsAttribute(action: Callable[[list[工 | None]], list[工 | None]]) -> Callable[[hasDOTkw_defaults], hasDOTkw_defaults]:
        """Apply `action` to the `kw_defaults` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr | None]` on `ast.arguments`. The `action` annotation uses
        `list[工 | None]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkw_defaults], hasDOTkw_defaults]
            A function that updates the node's `kw_defaults` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkw_defaults) -> hasDOTkw_defaults:
            setattr(node, 'kw_defaults', action(getattr(node, 'kw_defaults')))
            return node
        return workhorse

    @staticmethod
    def kwargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTkwarg], hasDOTkwarg]:
        """Apply `action` to the `kwarg` field of an AST node.

        (AI generated docstring)

        The field has type `ast.arg | None` on `ast.arguments`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkwarg], hasDOTkwarg]
            A function that updates the node's `kwarg` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkwarg) -> hasDOTkwarg:
            setattr(node, 'kwarg', action(getattr(node, 'kwarg')))
            return node
        return workhorse

    @staticmethod
    def kwd_attrsAttribute(action: Callable[[list[str]], list[str]]) -> Callable[[hasDOTkwd_attrs], hasDOTkwd_attrs]:
        """Apply `action` to the `kwd_attrs` field of an AST node.

        (AI generated docstring)

        The field has type `list[str]` on `ast.MatchClass`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkwd_attrs], hasDOTkwd_attrs]
            A function that updates the node's `kwd_attrs` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkwd_attrs) -> hasDOTkwd_attrs:
            setattr(node, 'kwd_attrs', action(getattr(node, 'kwd_attrs')))
            return node
        return workhorse

    @staticmethod
    def kwd_patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTkwd_patterns], hasDOTkwd_patterns]:
        """Apply `action` to the `kwd_patterns` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.pattern]` on `ast.MatchClass`. The `action` annotation uses
        `list[俪]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkwd_patterns], hasDOTkwd_patterns]
            A function that updates the node's `kwd_patterns` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTkwd_patterns) -> hasDOTkwd_patterns:
            setattr(node, 'kwd_patterns', action(getattr(node, 'kwd_patterns')))
            return node
        return workhorse

    @staticmethod
    def kwonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTkwonlyargs], hasDOTkwonlyargs]:
        """Apply `action` to the `kwonlyargs` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.arg]` on `ast.arguments`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTkwonlyargs], hasDOTkwonlyargs]
            A function that updates the node's `kwonlyargs` field in place and returns the same node.
        """

        def workhorse(node: hasDOTkwonlyargs) -> hasDOTkwonlyargs:
            setattr(node, 'kwonlyargs', action(getattr(node, 'kwonlyargs')))
            return node
        return workhorse

    @staticmethod
    def leftAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTleft], hasDOTleft]:
        """Apply `action` to the `left` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.BinOp`, `ast.Compare`. The `action` annotation uses `工`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTleft], hasDOTleft]
            A function that updates the node's `left` field in place and returns the same node.
        """

        def workhorse(node: hasDOTleft) -> hasDOTleft:
            setattr(node, 'left', action(getattr(node, 'left')))
            return node
        return workhorse

    @staticmethod
    def levelAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlevel], hasDOTlevel]:
        """Apply `action` to the `level` field of an AST node.

        (AI generated docstring)

        The field has type `int` on `ast.ImportFrom`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTlevel], hasDOTlevel]
            A function that updates the node's `level` field in place and returns the same node.
        """

        def workhorse(node: hasDOTlevel) -> hasDOTlevel:
            setattr(node, 'level', action(getattr(node, 'level')))
            return node
        return workhorse

    @staticmethod
    def linenoAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlineno], hasDOTlineno]:
        """Apply `action` to the `lineno` field of an AST node.

        (AI generated docstring)

        The field has type `int` on `ast.TypeIgnore`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTlineno], hasDOTlineno]
            A function that updates the node's `lineno` field in place and returns the same node.
        """

        def workhorse(node: hasDOTlineno) -> hasDOTlineno:
            setattr(node, 'lineno', action(getattr(node, 'lineno')))
            return node
        return workhorse

    @staticmethod
    def lowerAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTlower], hasDOTlower]:
        """Apply `action` to the `lower` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Slice`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTlower], hasDOTlower]
            A function that updates the node's `lower` field in place and returns the same node.
        """

        def workhorse(node: hasDOTlower) -> hasDOTlower:
            setattr(node, 'lower', action(getattr(node, 'lower')))
            return node
        return workhorse

    @staticmethod
    def moduleAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTmodule], hasDOTmodule]:
        """Apply `action` to the `module` field of an AST node.

        (AI generated docstring)

        The field has type `str | None` on `ast.ImportFrom`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTmodule], hasDOTmodule]
            A function that updates the node's `module` field in place and returns the same node.
        """

        def workhorse(node: hasDOTmodule) -> hasDOTmodule:
            setattr(node, 'module', action(getattr(node, 'module')))
            return node
        return workhorse

    @staticmethod
    def msgAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTmsg], hasDOTmsg]:
        """Apply `action` to the `msg` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Assert`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTmsg], hasDOTmsg]
            A function that updates the node's `msg` field in place and returns the same node.
        """

        def workhorse(node: hasDOTmsg) -> hasDOTmsg:
            setattr(node, 'msg', action(getattr(node, 'msg')))
            return node
        return workhorse

    @staticmethod
    def nameAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTname], hasDOTname]:
        """Apply `action` to the `name` field of an AST node.

        (AI generated docstring)

        The field has type `ast.Name` on `ast.TypeAlias`.

        The field has type `str` on `ast.AsyncFunctionDef`, `ast.ClassDef`, `ast.FunctionDef`,
        `ast.ParamSpec`, `ast.TypeVar`, `ast.TypeVarTuple`, `ast.alias`.

        The field has type `str | None` on `ast.ExceptHandler`, `ast.MatchAs`, `ast.MatchStar`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTname], hasDOTname]
            A function that updates the node's `name` field in place and returns the same node.
        """

        def workhorse(node: hasDOTname) -> hasDOTname:
            setattr(node, 'name', action(getattr(node, 'name')))
            return node
        return workhorse

    @staticmethod
    def namesAttribute(action: Callable[[list[ast.alias]], list[ast.alias]] | Callable[[list[str]], list[str]]) -> Callable[[hasDOTnames], hasDOTnames]:
        """Apply `action` to the `names` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.alias]` on `ast.Import`, `ast.ImportFrom`.

        The field has type `list[str]` on `ast.Global`, `ast.Nonlocal`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTnames], hasDOTnames]
            A function that updates the node's `names` field in place and returns the same node.
        """

        def workhorse(node: hasDOTnames) -> hasDOTnames:
            setattr(node, 'names', action(getattr(node, 'names')))
            return node
        return workhorse

    @staticmethod
    def opAttribute(action: Callable[[一符], 一符] | Callable[[二符], 二符] | Callable[[布尔符], 布尔符]) -> Callable[[hasDOTop], hasDOTop]:
        """Apply `action` to the `op` field of an AST node.

        (AI generated docstring)

        The field has type `ast.boolop` on `ast.BoolOp`. The `action` annotation uses `布尔符` for this
        type.

        The field has type `ast.operator` on `ast.AugAssign`, `ast.BinOp`. The `action` annotation
        uses `二符` for this type.

        The field has type `ast.unaryop` on `ast.UnaryOp`. The `action` annotation uses `一符` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTop], hasDOTop]
            A function that updates the node's `op` field in place and returns the same node.
        """

        def workhorse(node: hasDOTop) -> hasDOTop:
            setattr(node, 'op', action(getattr(node, 'op')))
            return node
        return workhorse

    @staticmethod
    def operandAttribute(action: Callable[[工], 工]) -> Callable[[hasDOToperand], hasDOToperand]:
        """Apply `action` to the `operand` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.UnaryOp`. The `action` annotation uses `工` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOToperand], hasDOToperand]
            A function that updates the node's `operand` field in place and returns the same node.
        """

        def workhorse(node: hasDOToperand) -> hasDOToperand:
            setattr(node, 'operand', action(getattr(node, 'operand')))
            return node
        return workhorse

    @staticmethod
    def opsAttribute(action: Callable[[list[比符]], list[比符]]) -> Callable[[hasDOTops], hasDOTops]:
        """Apply `action` to the `ops` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.cmpop]` on `ast.Compare`. The `action` annotation uses `list[比符]`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTops], hasDOTops]
            A function that updates the node's `ops` field in place and returns the same node.
        """

        def workhorse(node: hasDOTops) -> hasDOTops:
            setattr(node, 'ops', action(getattr(node, 'ops')))
            return node
        return workhorse

    @staticmethod
    def optional_varsAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOToptional_vars], hasDOToptional_vars]:
        """Apply `action` to the `optional_vars` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.withitem`. The `action` annotation uses `工 |
        None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOToptional_vars], hasDOToptional_vars]
            A function that updates the node's `optional_vars` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOToptional_vars) -> hasDOToptional_vars:
            setattr(node, 'optional_vars', action(getattr(node, 'optional_vars')))
            return node
        return workhorse

    @staticmethod
    def orelseAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTorelse], hasDOTorelse]:
        """Apply `action` to the `orelse` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.IfExp`. The `action` annotation uses `工` for this type.

        The field has type `list[ast.stmt]` on `ast.AsyncFor`, `ast.For`, `ast.If`, `ast.Try`,
        `ast.TryStar`, `ast.While`. The `action` annotation uses `list[口]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTorelse], hasDOTorelse]
            A function that updates the node's `orelse` field in place and returns the same node.
        """

        def workhorse(node: hasDOTorelse) -> hasDOTorelse:
            setattr(node, 'orelse', action(getattr(node, 'orelse')))
            return node
        return workhorse

    @staticmethod
    def patternAttribute(action: Callable[[俪], 俪] | Callable[[俪 | None], 俪 | None]) -> Callable[[hasDOTpattern], hasDOTpattern]:
        """Apply `action` to the `pattern` field of an AST node.

        (AI generated docstring)

        The field has type `ast.pattern` on `ast.match_case`. The `action` annotation uses `俪` for
        this type.

        The field has type `ast.pattern | None` on `ast.MatchAs`. The `action` annotation uses `俪 |
        None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTpattern], hasDOTpattern]
            A function that updates the node's `pattern` field in place and returns the same node.
        """

        def workhorse(node: hasDOTpattern) -> hasDOTpattern:
            setattr(node, 'pattern', action(getattr(node, 'pattern')))
            return node
        return workhorse

    @staticmethod
    def patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTpatterns], hasDOTpatterns]:
        """Apply `action` to the `patterns` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.pattern]` on `ast.MatchClass`, `ast.MatchMapping`, `ast.MatchOr`,
        `ast.MatchSequence`. The `action` annotation uses `list[俪]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTpatterns], hasDOTpatterns]
            A function that updates the node's `patterns` field in place and returns the same node.
        """

        def workhorse(node: hasDOTpatterns) -> hasDOTpatterns:
            setattr(node, 'patterns', action(getattr(node, 'patterns')))
            return node
        return workhorse

    @staticmethod
    def posonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTposonlyargs], hasDOTposonlyargs]:
        """Apply `action` to the `posonlyargs` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.arg]` on `ast.arguments`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTposonlyargs], hasDOTposonlyargs]
            A function that updates the node's `posonlyargs` field in place and returns the same node.
        """

        def workhorse(node: hasDOTposonlyargs) -> hasDOTposonlyargs:
            setattr(node, 'posonlyargs', action(getattr(node, 'posonlyargs')))
            return node
        return workhorse

    @staticmethod
    def restAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTrest], hasDOTrest]:
        """Apply `action` to the `rest` field of an AST node.

        (AI generated docstring)

        The field has type `str | None` on `ast.MatchMapping`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTrest], hasDOTrest]
            A function that updates the node's `rest` field in place and returns the same node.
        """

        def workhorse(node: hasDOTrest) -> hasDOTrest:
            setattr(node, 'rest', action(getattr(node, 'rest')))
            return node
        return workhorse

    @staticmethod
    def returnsAttribute(action: Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTreturns], hasDOTreturns]:
        """Apply `action` to the `returns` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.FunctionType`. The `action` annotation uses `工` for this
        type.

        The field has type `ast.expr | None` on `ast.AsyncFunctionDef`, `ast.FunctionDef`. The
        `action` annotation uses `工 | None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTreturns], hasDOTreturns]
            A function that updates the node's `returns` field in place and returns the same node.
        """

        def workhorse(node: hasDOTreturns) -> hasDOTreturns:
            setattr(node, 'returns', action(getattr(node, 'returns')))
            return node
        return workhorse

    @staticmethod
    def rightAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTright], hasDOTright]:
        """Apply `action` to the `right` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.BinOp`. The `action` annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTright], hasDOTright]
            A function that updates the node's `right` field in place and returns the same node.
        """

        def workhorse(node: hasDOTright) -> hasDOTright:
            setattr(node, 'right', action(getattr(node, 'right')))
            return node
        return workhorse

    @staticmethod
    def simpleAttribute(action: Callable[[int], int]) -> Callable[[hasDOTsimple], hasDOTsimple]:
        """Apply `action` to the `simple` field of an AST node.

        (AI generated docstring)

        The field has type `int` on `ast.AnnAssign`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTsimple], hasDOTsimple]
            A function that updates the node's `simple` field in place and returns the same node.
        """

        def workhorse(node: hasDOTsimple) -> hasDOTsimple:
            setattr(node, 'simple', action(getattr(node, 'simple')))
            return node
        return workhorse

    @staticmethod
    def sliceAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTslice], hasDOTslice]:
        """Apply `action` to the `slice` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Subscript`. The `action` annotation uses `工` for this
        type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTslice], hasDOTslice]
            A function that updates the node's `slice` field in place and returns the same node.
        """

        def workhorse(node: hasDOTslice) -> hasDOTslice:
            setattr(node, 'slice', action(getattr(node, 'slice')))
            return node
        return workhorse

    @staticmethod
    def stepAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTstep], hasDOTstep]:
        """Apply `action` to the `step` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Slice`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTstep], hasDOTstep]
            A function that updates the node's `step` field in place and returns the same node.
        """

        def workhorse(node: hasDOTstep) -> hasDOTstep:
            setattr(node, 'step', action(getattr(node, 'step')))
            return node
        return workhorse

    @staticmethod
    def strAttribute(action: Callable[[str], str]) -> Callable[[hasDOTstr], hasDOTstr]:
        """Apply `action` to the `str` field of an AST node.

        (AI generated docstring)

        The field has type `str` on `ast.Interpolation`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTstr], hasDOTstr]
            A function that updates the node's `str` field in place and returns the same node.
        """

        def workhorse(node: hasDOTstr) -> hasDOTstr:
            setattr(node, 'str', action(getattr(node, 'str')))
            return node
        return workhorse

    @staticmethod
    def subjectAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTsubject], hasDOTsubject]:
        """Apply `action` to the `subject` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Match`. The `action` annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTsubject], hasDOTsubject]
            A function that updates the node's `subject` field in place and returns the same node.
        """

        def workhorse(node: hasDOTsubject) -> hasDOTsubject:
            setattr(node, 'subject', action(getattr(node, 'subject')))
            return node
        return workhorse

    @staticmethod
    def tagAttribute(action: Callable[[str], str]) -> Callable[[hasDOTtag], hasDOTtag]:
        """Apply `action` to the `tag` field of an AST node.

        (AI generated docstring)

        The field has type `str` on `ast.TypeIgnore`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtag], hasDOTtag]
            A function that updates the node's `tag` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtag) -> hasDOTtag:
            setattr(node, 'tag', action(getattr(node, 'tag')))
            return node
        return workhorse

    @staticmethod
    def targetAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[ast.Name | ast.Attribute | ast.Subscript], ast.Name | ast.Attribute | ast.Subscript] | Callable[[工], 工]) -> Callable[[hasDOTtarget], hasDOTtarget]:
        """Apply `action` to the `target` field of an AST node.

        (AI generated docstring)

        The field has type `ast.Name` on `ast.NamedExpr`.

        The field has type `ast.Name | ast.Attribute | ast.Subscript` on `ast.AnnAssign`,
        `ast.AugAssign`.

        The field has type `ast.expr` on `ast.AsyncFor`, `ast.For`, `ast.comprehension`. The `action`
        annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtarget], hasDOTtarget]
            A function that updates the node's `target` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtarget) -> hasDOTtarget:
            setattr(node, 'target', action(getattr(node, 'target')))
            return node
        return workhorse

    @staticmethod
    def targetsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTtargets], hasDOTtargets]:
        """Apply `action` to the `targets` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.Assign`, `ast.Delete`. The `action` annotation
        uses `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtargets], hasDOTtargets]
            A function that updates the node's `targets` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtargets) -> hasDOTtargets:
            setattr(node, 'targets', action(getattr(node, 'targets')))
            return node
        return workhorse

    @staticmethod
    def testAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTtest], hasDOTtest]:
        """Apply `action` to the `test` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Assert`, `ast.If`, `ast.IfExp`, `ast.While`. The
        `action` annotation uses `工` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtest], hasDOTtest]
            A function that updates the node's `test` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtest) -> hasDOTtest:
            setattr(node, 'test', action(getattr(node, 'test')))
            return node
        return workhorse

    @staticmethod
    def typeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTtype], hasDOTtype]:
        """Apply `action` to the `type` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.ExceptHandler`. The `action` annotation uses `工 |
        None` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtype], hasDOTtype]
            A function that updates the node's `type` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtype) -> hasDOTtype:
            setattr(node, 'type', action(getattr(node, 'type')))
            return node
        return workhorse

    @staticmethod
    def type_commentAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTtype_comment], hasDOTtype_comment]:
        """Apply `action` to the `type_comment` field of an AST node.

        (AI generated docstring)

        The field has type `str | None` on `ast.Assign`, `ast.AsyncFor`, `ast.AsyncFunctionDef`,
        `ast.AsyncWith`, `ast.For`, `ast.FunctionDef`, `ast.With`, `ast.arg`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_comment], hasDOTtype_comment]
            A function that updates the node's `type_comment` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTtype_comment) -> hasDOTtype_comment:
            setattr(node, 'type_comment', action(getattr(node, 'type_comment')))
            return node
        return workhorse

    @staticmethod
    def type_ignoresAttribute(action: Callable[[list[ast.TypeIgnore]], list[ast.TypeIgnore]]) -> Callable[[hasDOTtype_ignores], hasDOTtype_ignores]:
        """Apply `action` to the `type_ignores` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.TypeIgnore]` on `ast.Module`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_ignores], hasDOTtype_ignores]
            A function that updates the node's `type_ignores` field in place and returns the same
            node.
        """

        def workhorse(node: hasDOTtype_ignores) -> hasDOTtype_ignores:
            setattr(node, 'type_ignores', action(getattr(node, 'type_ignores')))
            return node
        return workhorse

    @staticmethod
    def type_paramsAttribute(action: Callable[[list[形]], list[形]]) -> Callable[[hasDOTtype_params], hasDOTtype_params]:
        """Apply `action` to the `type_params` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.type_param]` on `ast.AsyncFunctionDef`, `ast.ClassDef`,
        `ast.FunctionDef`, `ast.TypeAlias`. The `action` annotation uses `list[形]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTtype_params], hasDOTtype_params]
            A function that updates the node's `type_params` field in place and returns the same node.
        """

        def workhorse(node: hasDOTtype_params) -> hasDOTtype_params:
            setattr(node, 'type_params', action(getattr(node, 'type_params')))
            return node
        return workhorse

    @staticmethod
    def upperAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTupper], hasDOTupper]:
        """Apply `action` to the `upper` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr | None` on `ast.Slice`. The `action` annotation uses `工 | None`
        for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTupper], hasDOTupper]
            A function that updates the node's `upper` field in place and returns the same node.
        """

        def workhorse(node: hasDOTupper) -> hasDOTupper:
            setattr(node, 'upper', action(getattr(node, 'upper')))
            return node
        return workhorse

    @staticmethod
    def valueAttribute(action: Callable[[ast_ConstantValue], ast_ConstantValue] | Callable[[bool | None], bool | None] | Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTvalue], hasDOTvalue]:
        """Apply `action` to the `value` field of an AST node.

        (AI generated docstring)

        The field has type `ast.expr` on `ast.Assign`, `ast.Attribute`, `ast.AugAssign`, `ast.Await`,
        `ast.DictComp`, `ast.Expr`, `ast.FormattedValue`, `ast.Interpolation`, `ast.MatchValue`,
        `ast.NamedExpr`, `ast.Starred`, `ast.Subscript`, `ast.TypeAlias`, `ast.YieldFrom`,
        `ast.keyword`. The `action` annotation uses `工` for this type.

        The field has type `ast.expr | None` on `ast.AnnAssign`, `ast.Return`, `ast.Yield`. The
        `action` annotation uses `工 | None` for this type.

        The field has type `ast_ConstantValue` on `ast.Constant`.

        The field has type `bool | None` on `ast.MatchSingleton`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTvalue], hasDOTvalue]
            A function that updates the node's `value` field in place and returns the same node.
        """

        def workhorse(node: hasDOTvalue) -> hasDOTvalue:
            setattr(node, 'value', action(getattr(node, 'value')))
            return node
        return workhorse

    @staticmethod
    def valuesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTvalues], hasDOTvalues]:
        """Apply `action` to the `values` field of an AST node.

        (AI generated docstring)

        The field has type `list[ast.expr]` on `ast.BoolOp`, `ast.Dict`, `ast.JoinedStr`,
        `ast.TemplateStr`. The `action` annotation uses `list[工]` for this type.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTvalues], hasDOTvalues]
            A function that updates the node's `values` field in place and returns the same node.
        """

        def workhorse(node: hasDOTvalues) -> hasDOTvalues:
            setattr(node, 'values', action(getattr(node, 'values')))
            return node
        return workhorse

    @staticmethod
    def varargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTvararg], hasDOTvararg]:
        """Apply `action` to the `vararg` field of an AST node.

        (AI generated docstring)

        The field has type `ast.arg | None` on `ast.arguments`.

        Parameters
        ----------
        action : Callable
            A function that takes the field's current value and returns a replacement of the same
            type.

        Returns
        -------
        workhorse : Callable[[hasDOTvararg], hasDOTvararg]
            A function that updates the node's `vararg` field in place and returns the same node.
        """

        def workhorse(node: hasDOTvararg) -> hasDOTvararg:
            setattr(node, 'vararg', action(getattr(node, 'vararg')))
            return node
        return workhorse
