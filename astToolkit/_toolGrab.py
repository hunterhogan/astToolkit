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
	hasDOTtype_params, hasDOTupper, hasDOTvalue, hasDOTvalues, hasDOTvararg, 一符, 个, 二符, 俪, 口, 工, 工位, 布尔符, 形, 比符,
)
from collections.abc import Callable, Sequence
from typing import Any
import ast
import sys

if sys.version_info >= (3, 13):
    from astToolkit import hasDOTdefault_value as hasDOTdefault_value

class Grab:
    """
    Modify specific attributes of AST nodes while preserving the node structure.

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
    def annotationAttribute(action: Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTannotation], hasDOTannotation]:

        def workhorse(node: hasDOTannotation) -> hasDOTannotation:
            setattr(node, 'annotation', action(getattr(node, 'annotation')))
            return node
        return workhorse

    @staticmethod
    def argAttribute(action: Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTarg], hasDOTarg]:

        def workhorse(node: hasDOTarg) -> hasDOTarg:
            setattr(node, 'arg', action(getattr(node, 'arg')))
            return node
        return workhorse

    @staticmethod
    def argsAttribute(action: Callable[[ast.arguments], ast.arguments] | Callable[[list[ast.arg]], list[ast.arg]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTargs], hasDOTargs]:

        def workhorse(node: hasDOTargs) -> hasDOTargs:
            setattr(node, 'args', action(getattr(node, 'args')))
            return node
        return workhorse

    @staticmethod
    def argtypesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTargtypes], hasDOTargtypes]:

        def workhorse(node: hasDOTargtypes) -> hasDOTargtypes:
            setattr(node, 'argtypes', action(getattr(node, 'argtypes')))
            return node
        return workhorse

    @staticmethod
    def asnameAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTasname], hasDOTasname]:

        def workhorse(node: hasDOTasname) -> hasDOTasname:
            setattr(node, 'asname', action(getattr(node, 'asname')))
            return node
        return workhorse

    @staticmethod
    def attrAttribute(action: Callable[[str], str]) -> Callable[[hasDOTattr], hasDOTattr]:

        def workhorse(node: hasDOTattr) -> hasDOTattr:
            setattr(node, 'attr', action(getattr(node, 'attr')))
            return node
        return workhorse

    @staticmethod
    def basesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTbases], hasDOTbases]:

        def workhorse(node: hasDOTbases) -> hasDOTbases:
            setattr(node, 'bases', action(getattr(node, 'bases')))
            return node
        return workhorse

    @staticmethod
    def bodyAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTbody], hasDOTbody]:

        def workhorse(node: hasDOTbody) -> hasDOTbody:
            setattr(node, 'body', action(getattr(node, 'body')))
            return node
        return workhorse

    @staticmethod
    def boundAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTbound], hasDOTbound]:

        def workhorse(node: hasDOTbound) -> hasDOTbound:
            setattr(node, 'bound', action(getattr(node, 'bound')))
            return node
        return workhorse

    @staticmethod
    def casesAttribute(action: Callable[[list[ast.match_case]], list[ast.match_case]]) -> Callable[[hasDOTcases], hasDOTcases]:

        def workhorse(node: hasDOTcases) -> hasDOTcases:
            setattr(node, 'cases', action(getattr(node, 'cases')))
            return node
        return workhorse

    @staticmethod
    def causeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTcause], hasDOTcause]:

        def workhorse(node: hasDOTcause) -> hasDOTcause:
            setattr(node, 'cause', action(getattr(node, 'cause')))
            return node
        return workhorse

    @staticmethod
    def clsAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcls], hasDOTcls]:

        def workhorse(node: hasDOTcls) -> hasDOTcls:
            setattr(node, 'cls', action(getattr(node, 'cls')))
            return node
        return workhorse

    @staticmethod
    def comparatorsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTcomparators], hasDOTcomparators]:

        def workhorse(node: hasDOTcomparators) -> hasDOTcomparators:
            setattr(node, 'comparators', action(getattr(node, 'comparators')))
            return node
        return workhorse

    @staticmethod
    def context_exprAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTcontext_expr], hasDOTcontext_expr]:

        def workhorse(node: hasDOTcontext_expr) -> hasDOTcontext_expr:
            setattr(node, 'context_expr', action(getattr(node, 'context_expr')))
            return node
        return workhorse

    @staticmethod
    def conversionAttribute(action: Callable[[int], int]) -> Callable[[hasDOTconversion], hasDOTconversion]:

        def workhorse(node: hasDOTconversion) -> hasDOTconversion:
            setattr(node, 'conversion', action(getattr(node, 'conversion')))
            return node
        return workhorse

    @staticmethod
    def ctxAttribute(action: Callable[[工位], 工位]) -> Callable[[hasDOTctx], hasDOTctx]:

        def workhorse(node: hasDOTctx) -> hasDOTctx:
            setattr(node, 'ctx', action(getattr(node, 'ctx')))
            return node
        return workhorse

    @staticmethod
    def decorator_listAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdecorator_list], hasDOTdecorator_list]:

        def workhorse(node: hasDOTdecorator_list) -> hasDOTdecorator_list:
            setattr(node, 'decorator_list', action(getattr(node, 'decorator_list')))
            return node
        return workhorse
    if sys.version_info >= (3, 13):

        @staticmethod
        def default_valueAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTdefault_value], hasDOTdefault_value]:

            def workhorse(node: hasDOTdefault_value) -> hasDOTdefault_value:
                setattr(node, 'default_value', action(getattr(node, 'default_value')))
                return node
            return workhorse

    @staticmethod
    def defaultsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTdefaults], hasDOTdefaults]:

        def workhorse(node: hasDOTdefaults) -> hasDOTdefaults:
            setattr(node, 'defaults', action(getattr(node, 'defaults')))
            return node
        return workhorse

    @staticmethod
    def eltAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTelt], hasDOTelt]:

        def workhorse(node: hasDOTelt) -> hasDOTelt:
            setattr(node, 'elt', action(getattr(node, 'elt')))
            return node
        return workhorse

    @staticmethod
    def eltsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTelts], hasDOTelts]:

        def workhorse(node: hasDOTelts) -> hasDOTelts:
            setattr(node, 'elts', action(getattr(node, 'elts')))
            return node
        return workhorse

    @staticmethod
    def excAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTexc], hasDOTexc]:

        def workhorse(node: hasDOTexc) -> hasDOTexc:
            setattr(node, 'exc', action(getattr(node, 'exc')))
            return node
        return workhorse

    @staticmethod
    def finalbodyAttribute(action: Callable[[list[口]], list[口]]) -> Callable[[hasDOTfinalbody], hasDOTfinalbody]:

        def workhorse(node: hasDOTfinalbody) -> hasDOTfinalbody:
            setattr(node, 'finalbody', action(getattr(node, 'finalbody')))
            return node
        return workhorse

    @staticmethod
    def format_specAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTformat_spec], hasDOTformat_spec]:

        def workhorse(node: hasDOTformat_spec) -> hasDOTformat_spec:
            setattr(node, 'format_spec', action(getattr(node, 'format_spec')))
            return node
        return workhorse

    @staticmethod
    def funcAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTfunc], hasDOTfunc]:

        def workhorse(node: hasDOTfunc) -> hasDOTfunc:
            setattr(node, 'func', action(getattr(node, 'func')))
            return node
        return workhorse

    @staticmethod
    def generatorsAttribute(action: Callable[[list[ast.comprehension]], list[ast.comprehension]]) -> Callable[[hasDOTgenerators], hasDOTgenerators]:

        def workhorse(node: hasDOTgenerators) -> hasDOTgenerators:
            setattr(node, 'generators', action(getattr(node, 'generators')))
            return node
        return workhorse

    @staticmethod
    def guardAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTguard], hasDOTguard]:

        def workhorse(node: hasDOTguard) -> hasDOTguard:
            setattr(node, 'guard', action(getattr(node, 'guard')))
            return node
        return workhorse

    @staticmethod
    def handlersAttribute(action: Callable[[list[ast.ExceptHandler]], list[ast.ExceptHandler]]) -> Callable[[hasDOThandlers], hasDOThandlers]:

        def workhorse(node: hasDOThandlers) -> hasDOThandlers:
            setattr(node, 'handlers', action(getattr(node, 'handlers')))
            return node
        return workhorse

    @staticmethod
    def idAttribute(action: Callable[[str], str]) -> Callable[[hasDOTid], hasDOTid]:

        def workhorse(node: hasDOTid) -> hasDOTid:
            setattr(node, 'id', action(getattr(node, 'id')))
            return node
        return workhorse

    @staticmethod
    def ifsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTifs], hasDOTifs]:

        def workhorse(node: hasDOTifs) -> hasDOTifs:
            setattr(node, 'ifs', action(getattr(node, 'ifs')))
            return node
        return workhorse

    @staticmethod
    def is_asyncAttribute(action: Callable[[int], int]) -> Callable[[hasDOTis_async], hasDOTis_async]:

        def workhorse(node: hasDOTis_async) -> hasDOTis_async:
            setattr(node, 'is_async', action(getattr(node, 'is_async')))
            return node
        return workhorse

    @staticmethod
    def itemsAttribute(action: Callable[[list[ast.withitem]], list[ast.withitem]]) -> Callable[[hasDOTitems], hasDOTitems]:

        def workhorse(node: hasDOTitems) -> hasDOTitems:
            setattr(node, 'items', action(getattr(node, 'items')))
            return node
        return workhorse

    @staticmethod
    def iterAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTiter], hasDOTiter]:

        def workhorse(node: hasDOTiter) -> hasDOTiter:
            setattr(node, 'iter', action(getattr(node, 'iter')))
            return node
        return workhorse

    @staticmethod
    def keyAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTkey], hasDOTkey]:

        def workhorse(node: hasDOTkey) -> hasDOTkey:
            setattr(node, 'key', action(getattr(node, 'key')))
            return node
        return workhorse

    @staticmethod
    def keysAttribute(action: Callable[[list[工 | None]], list[工 | None]] | Callable[[list[工]], list[工]]) -> Callable[[hasDOTkeys], hasDOTkeys]:

        def workhorse(node: hasDOTkeys) -> hasDOTkeys:
            setattr(node, 'keys', action(getattr(node, 'keys')))
            return node
        return workhorse

    @staticmethod
    def keywordsAttribute(action: Callable[[list[ast.keyword]], list[ast.keyword]]) -> Callable[[hasDOTkeywords], hasDOTkeywords]:

        def workhorse(node: hasDOTkeywords) -> hasDOTkeywords:
            setattr(node, 'keywords', action(getattr(node, 'keywords')))
            return node
        return workhorse

    @staticmethod
    def kindAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTkind], hasDOTkind]:

        def workhorse(node: hasDOTkind) -> hasDOTkind:
            setattr(node, 'kind', action(getattr(node, 'kind')))
            return node
        return workhorse

    @staticmethod
    def kw_defaultsAttribute(action: Callable[[list[工 | None]], list[工 | None]]) -> Callable[[hasDOTkw_defaults], hasDOTkw_defaults]:

        def workhorse(node: hasDOTkw_defaults) -> hasDOTkw_defaults:
            setattr(node, 'kw_defaults', action(getattr(node, 'kw_defaults')))
            return node
        return workhorse

    @staticmethod
    def kwargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTkwarg], hasDOTkwarg]:

        def workhorse(node: hasDOTkwarg) -> hasDOTkwarg:
            setattr(node, 'kwarg', action(getattr(node, 'kwarg')))
            return node
        return workhorse

    @staticmethod
    def kwd_attrsAttribute(action: Callable[[list[str]], list[str]]) -> Callable[[hasDOTkwd_attrs], hasDOTkwd_attrs]:

        def workhorse(node: hasDOTkwd_attrs) -> hasDOTkwd_attrs:
            setattr(node, 'kwd_attrs', action(getattr(node, 'kwd_attrs')))
            return node
        return workhorse

    @staticmethod
    def kwd_patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTkwd_patterns], hasDOTkwd_patterns]:

        def workhorse(node: hasDOTkwd_patterns) -> hasDOTkwd_patterns:
            setattr(node, 'kwd_patterns', action(getattr(node, 'kwd_patterns')))
            return node
        return workhorse

    @staticmethod
    def kwonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTkwonlyargs], hasDOTkwonlyargs]:

        def workhorse(node: hasDOTkwonlyargs) -> hasDOTkwonlyargs:
            setattr(node, 'kwonlyargs', action(getattr(node, 'kwonlyargs')))
            return node
        return workhorse

    @staticmethod
    def leftAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTleft], hasDOTleft]:

        def workhorse(node: hasDOTleft) -> hasDOTleft:
            setattr(node, 'left', action(getattr(node, 'left')))
            return node
        return workhorse

    @staticmethod
    def levelAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlevel], hasDOTlevel]:

        def workhorse(node: hasDOTlevel) -> hasDOTlevel:
            setattr(node, 'level', action(getattr(node, 'level')))
            return node
        return workhorse

    @staticmethod
    def linenoAttribute(action: Callable[[int], int]) -> Callable[[hasDOTlineno], hasDOTlineno]:

        def workhorse(node: hasDOTlineno) -> hasDOTlineno:
            setattr(node, 'lineno', action(getattr(node, 'lineno')))
            return node
        return workhorse

    @staticmethod
    def lowerAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTlower], hasDOTlower]:

        def workhorse(node: hasDOTlower) -> hasDOTlower:
            setattr(node, 'lower', action(getattr(node, 'lower')))
            return node
        return workhorse

    @staticmethod
    def moduleAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTmodule], hasDOTmodule]:

        def workhorse(node: hasDOTmodule) -> hasDOTmodule:
            setattr(node, 'module', action(getattr(node, 'module')))
            return node
        return workhorse

    @staticmethod
    def msgAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTmsg], hasDOTmsg]:

        def workhorse(node: hasDOTmsg) -> hasDOTmsg:
            setattr(node, 'msg', action(getattr(node, 'msg')))
            return node
        return workhorse

    @staticmethod
    def nameAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[str], str] | Callable[[str | None], str | None]) -> Callable[[hasDOTname], hasDOTname]:

        def workhorse(node: hasDOTname) -> hasDOTname:
            setattr(node, 'name', action(getattr(node, 'name')))
            return node
        return workhorse

    @staticmethod
    def namesAttribute(action: Callable[[list[ast.alias]], list[ast.alias]] | Callable[[list[str]], list[str]]) -> Callable[[hasDOTnames], hasDOTnames]:

        def workhorse(node: hasDOTnames) -> hasDOTnames:
            setattr(node, 'names', action(getattr(node, 'names')))
            return node
        return workhorse

    @staticmethod
    def opAttribute(action: Callable[[一符], 一符] | Callable[[二符], 二符] | Callable[[布尔符], 布尔符]) -> Callable[[hasDOTop], hasDOTop]:

        def workhorse(node: hasDOTop) -> hasDOTop:
            setattr(node, 'op', action(getattr(node, 'op')))
            return node
        return workhorse

    @staticmethod
    def operandAttribute(action: Callable[[工], 工]) -> Callable[[hasDOToperand], hasDOToperand]:

        def workhorse(node: hasDOToperand) -> hasDOToperand:
            setattr(node, 'operand', action(getattr(node, 'operand')))
            return node
        return workhorse

    @staticmethod
    def opsAttribute(action: Callable[[list[比符]], list[比符]]) -> Callable[[hasDOTops], hasDOTops]:

        def workhorse(node: hasDOTops) -> hasDOTops:
            setattr(node, 'ops', action(getattr(node, 'ops')))
            return node
        return workhorse

    @staticmethod
    def optional_varsAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOToptional_vars], hasDOToptional_vars]:

        def workhorse(node: hasDOToptional_vars) -> hasDOToptional_vars:
            setattr(node, 'optional_vars', action(getattr(node, 'optional_vars')))
            return node
        return workhorse

    @staticmethod
    def orelseAttribute(action: Callable[[list[口]], list[口]] | Callable[[工], 工]) -> Callable[[hasDOTorelse], hasDOTorelse]:

        def workhorse(node: hasDOTorelse) -> hasDOTorelse:
            setattr(node, 'orelse', action(getattr(node, 'orelse')))
            return node
        return workhorse

    @staticmethod
    def patternAttribute(action: Callable[[俪], 俪] | Callable[[俪 | None], 俪 | None]) -> Callable[[hasDOTpattern], hasDOTpattern]:

        def workhorse(node: hasDOTpattern) -> hasDOTpattern:
            setattr(node, 'pattern', action(getattr(node, 'pattern')))
            return node
        return workhorse

    @staticmethod
    def patternsAttribute(action: Callable[[list[俪]], list[俪]]) -> Callable[[hasDOTpatterns], hasDOTpatterns]:

        def workhorse(node: hasDOTpatterns) -> hasDOTpatterns:
            setattr(node, 'patterns', action(getattr(node, 'patterns')))
            return node
        return workhorse

    @staticmethod
    def posonlyargsAttribute(action: Callable[[list[ast.arg]], list[ast.arg]]) -> Callable[[hasDOTposonlyargs], hasDOTposonlyargs]:

        def workhorse(node: hasDOTposonlyargs) -> hasDOTposonlyargs:
            setattr(node, 'posonlyargs', action(getattr(node, 'posonlyargs')))
            return node
        return workhorse

    @staticmethod
    def restAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTrest], hasDOTrest]:

        def workhorse(node: hasDOTrest) -> hasDOTrest:
            setattr(node, 'rest', action(getattr(node, 'rest')))
            return node
        return workhorse

    @staticmethod
    def returnsAttribute(action: Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTreturns], hasDOTreturns]:

        def workhorse(node: hasDOTreturns) -> hasDOTreturns:
            setattr(node, 'returns', action(getattr(node, 'returns')))
            return node
        return workhorse

    @staticmethod
    def rightAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTright], hasDOTright]:

        def workhorse(node: hasDOTright) -> hasDOTright:
            setattr(node, 'right', action(getattr(node, 'right')))
            return node
        return workhorse

    @staticmethod
    def simpleAttribute(action: Callable[[int], int]) -> Callable[[hasDOTsimple], hasDOTsimple]:

        def workhorse(node: hasDOTsimple) -> hasDOTsimple:
            setattr(node, 'simple', action(getattr(node, 'simple')))
            return node
        return workhorse

    @staticmethod
    def sliceAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTslice], hasDOTslice]:

        def workhorse(node: hasDOTslice) -> hasDOTslice:
            setattr(node, 'slice', action(getattr(node, 'slice')))
            return node
        return workhorse

    @staticmethod
    def stepAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTstep], hasDOTstep]:

        def workhorse(node: hasDOTstep) -> hasDOTstep:
            setattr(node, 'step', action(getattr(node, 'step')))
            return node
        return workhorse

    @staticmethod
    def subjectAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTsubject], hasDOTsubject]:

        def workhorse(node: hasDOTsubject) -> hasDOTsubject:
            setattr(node, 'subject', action(getattr(node, 'subject')))
            return node
        return workhorse

    @staticmethod
    def tagAttribute(action: Callable[[str], str]) -> Callable[[hasDOTtag], hasDOTtag]:

        def workhorse(node: hasDOTtag) -> hasDOTtag:
            setattr(node, 'tag', action(getattr(node, 'tag')))
            return node
        return workhorse

    @staticmethod
    def targetAttribute(action: Callable[[ast.Name], ast.Name] | Callable[[ast.Name | ast.Attribute | ast.Subscript], ast.Name | ast.Attribute | ast.Subscript] | Callable[[工], 工]) -> Callable[[hasDOTtarget], hasDOTtarget]:

        def workhorse(node: hasDOTtarget) -> hasDOTtarget:
            setattr(node, 'target', action(getattr(node, 'target')))
            return node
        return workhorse

    @staticmethod
    def targetsAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTtargets], hasDOTtargets]:

        def workhorse(node: hasDOTtargets) -> hasDOTtargets:
            setattr(node, 'targets', action(getattr(node, 'targets')))
            return node
        return workhorse

    @staticmethod
    def testAttribute(action: Callable[[工], 工]) -> Callable[[hasDOTtest], hasDOTtest]:

        def workhorse(node: hasDOTtest) -> hasDOTtest:
            setattr(node, 'test', action(getattr(node, 'test')))
            return node
        return workhorse

    @staticmethod
    def typeAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTtype], hasDOTtype]:

        def workhorse(node: hasDOTtype) -> hasDOTtype:
            setattr(node, 'type', action(getattr(node, 'type')))
            return node
        return workhorse

    @staticmethod
    def type_commentAttribute(action: Callable[[str | None], str | None]) -> Callable[[hasDOTtype_comment], hasDOTtype_comment]:

        def workhorse(node: hasDOTtype_comment) -> hasDOTtype_comment:
            setattr(node, 'type_comment', action(getattr(node, 'type_comment')))
            return node
        return workhorse

    @staticmethod
    def type_ignoresAttribute(action: Callable[[list[ast.TypeIgnore]], list[ast.TypeIgnore]]) -> Callable[[hasDOTtype_ignores], hasDOTtype_ignores]:

        def workhorse(node: hasDOTtype_ignores) -> hasDOTtype_ignores:
            setattr(node, 'type_ignores', action(getattr(node, 'type_ignores')))
            return node
        return workhorse

    @staticmethod
    def type_paramsAttribute(action: Callable[[list[形]], list[形]]) -> Callable[[hasDOTtype_params], hasDOTtype_params]:

        def workhorse(node: hasDOTtype_params) -> hasDOTtype_params:
            setattr(node, 'type_params', action(getattr(node, 'type_params')))
            return node
        return workhorse

    @staticmethod
    def upperAttribute(action: Callable[[工 | None], 工 | None]) -> Callable[[hasDOTupper], hasDOTupper]:

        def workhorse(node: hasDOTupper) -> hasDOTupper:
            setattr(node, 'upper', action(getattr(node, 'upper')))
            return node
        return workhorse

    @staticmethod
    def valueAttribute(action: Callable[[bool | None], bool | None] | Callable[[ConstantValueType], ConstantValueType] | Callable[[工], 工] | Callable[[工 | None], 工 | None]) -> Callable[[hasDOTvalue], hasDOTvalue]:

        def workhorse(node: hasDOTvalue) -> hasDOTvalue:
            setattr(node, 'value', action(getattr(node, 'value')))
            return node
        return workhorse

    @staticmethod
    def valuesAttribute(action: Callable[[list[工]], list[工]]) -> Callable[[hasDOTvalues], hasDOTvalues]:

        def workhorse(node: hasDOTvalues) -> hasDOTvalues:
            setattr(node, 'values', action(getattr(node, 'values')))
            return node
        return workhorse

    @staticmethod
    def varargAttribute(action: Callable[[ast.arg | None], ast.arg | None]) -> Callable[[hasDOTvararg], hasDOTvararg]:

        def workhorse(node: hasDOTvararg) -> hasDOTvararg:
            setattr(node, 'vararg', action(getattr(node, 'vararg')))
            return node
        return workhorse