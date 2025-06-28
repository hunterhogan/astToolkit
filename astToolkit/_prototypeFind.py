from collections.abc import Callable
from typing import Any
from typing_extensions import TypeIs
import ast

class Find:

    def __init__(self, queueOfGotten_attr: list[Callable[[Any], tuple[bool, Any]]] | None=None) -> None:
        self.queueOfGotten_attr = queueOfGotten_attr or []

    def __getattribute__(self, gotten_attrIdentifier: str) -> Any:
        try:
            return object.__getattribute__(self, gotten_attrIdentifier)
        except AttributeError:
            pass

        def attribute_checker(attrCurrent: Any) -> tuple[bool, Any]:
            hasAttributeCheck = hasattr(attrCurrent, gotten_attrIdentifier)
            if hasAttributeCheck:
                return (hasAttributeCheck, getattr(attrCurrent, gotten_attrIdentifier))
            return (hasAttributeCheck, attrCurrent)
        Z0Z_ImaQueue = object.__getattribute__(self, 'queueOfGotten_attr')
        dontMutateMyQueue: list[Callable[[Any], tuple[bool, Any]]] = [*Z0Z_ImaQueue, attribute_checker]
        return Find(dontMutateMyQueue)

    def equal(self, valueTarget: Any) -> 'Find':

        def workhorse(attrCurrent: Any) -> tuple[bool, Any]:
            comparisonValue = attrCurrent == valueTarget
            return (comparisonValue, attrCurrent)
        dontMutateMyQueue: list[Callable[[Any], tuple[bool, Any]]] = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def at(self, indexTarget: int) -> 'Find':

        def workhorse(attrCurrent: Any) -> tuple[bool, Any]:
            try:
                element: Any = attrCurrent[indexTarget]
            except (IndexError, TypeError, KeyError):
                indexAccessFailure = False
                return (indexAccessFailure, attrCurrent)
            else:
                indexAccessValue = True
                return (indexAccessValue, element)
        dontMutateMyQueue: list[Callable[[Any], tuple[bool, Any]]] = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def __call__(self, node: ast.AST) -> bool:
        attrCurrent: Any = node
        for trueFalseCallable in self.queueOfGotten_attr:
            Ima_bool, attrNext = trueFalseCallable(attrCurrent)
            if not Ima_bool:
                return False
            attrCurrent = attrNext
        return True

    def Add(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Add], ast.AST]:
            return (isinstance(node, ast.Add), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def alias(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.alias], ast.AST]:
            return (isinstance(node, ast.alias), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def And(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.And], ast.AST]:
            return (isinstance(node, ast.And), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AnnAssign(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AnnAssign], ast.AST]:
            return (isinstance(node, ast.AnnAssign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def arg(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.arg], ast.AST]:
            return (isinstance(node, ast.arg), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def arguments(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.arguments], ast.AST]:
            return (isinstance(node, ast.arguments), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Assert(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Assert], ast.AST]:
            return (isinstance(node, ast.Assert), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Assign(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Assign], ast.AST]:
            return (isinstance(node, ast.Assign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AST(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AST], ast.AST]:
            return (isinstance(node, ast.AST), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncFor(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncFor], ast.AST]:
            return (isinstance(node, ast.AsyncFor), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncFunctionDef(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncFunctionDef], ast.AST]:
            return (isinstance(node, ast.AsyncFunctionDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncWith(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncWith], ast.AST]:
            return (isinstance(node, ast.AsyncWith), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Attribute(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Attribute], ast.AST]:
            return (isinstance(node, ast.Attribute), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AugAssign(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AugAssign], ast.AST]:
            return (isinstance(node, ast.AugAssign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Await(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Await], ast.AST]:
            return (isinstance(node, ast.Await), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BinOp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BinOp], ast.AST]:
            return (isinstance(node, ast.BinOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitAnd(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitAnd], ast.AST]:
            return (isinstance(node, ast.BitAnd), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitOr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitOr], ast.AST]:
            return (isinstance(node, ast.BitOr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitXor(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitXor], ast.AST]:
            return (isinstance(node, ast.BitXor), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def boolop(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.boolop], ast.AST]:
            return (isinstance(node, ast.boolop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BoolOp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BoolOp], ast.AST]:
            return (isinstance(node, ast.BoolOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Break(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Break], ast.AST]:
            return (isinstance(node, ast.Break), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Call(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Call], ast.AST]:
            return (isinstance(node, ast.Call), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ClassDef(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ClassDef], ast.AST]:
            return (isinstance(node, ast.ClassDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def cmpop(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.cmpop], ast.AST]:
            return (isinstance(node, ast.cmpop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Compare(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Compare], ast.AST]:
            return (isinstance(node, ast.Compare), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def comprehension(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.comprehension], ast.AST]:
            return (isinstance(node, ast.comprehension), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Constant(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Constant], ast.AST]:
            return (isinstance(node, ast.Constant), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Continue(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Continue], ast.AST]:
            return (isinstance(node, ast.Continue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Del(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Del], ast.AST]:
            return (isinstance(node, ast.Del), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Delete(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Delete], ast.AST]:
            return (isinstance(node, ast.Delete), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Dict(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Dict], ast.AST]:
            return (isinstance(node, ast.Dict), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def DictComp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.DictComp], ast.AST]:
            return (isinstance(node, ast.DictComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Div(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Div], ast.AST]:
            return (isinstance(node, ast.Div), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Eq(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Eq], ast.AST]:
            return (isinstance(node, ast.Eq), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def excepthandler(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.excepthandler], ast.AST]:
            return (isinstance(node, ast.excepthandler), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ExceptHandler(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ExceptHandler], ast.AST]:
            return (isinstance(node, ast.ExceptHandler), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def expr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.expr], ast.AST]:
            return (isinstance(node, ast.expr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Expr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Expr], ast.AST]:
            return (isinstance(node, ast.Expr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def expr_context(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.expr_context], ast.AST]:
            return (isinstance(node, ast.expr_context), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Expression(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Expression], ast.AST]:
            return (isinstance(node, ast.Expression), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FloorDiv(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FloorDiv], ast.AST]:
            return (isinstance(node, ast.FloorDiv), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def For(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.For], ast.AST]:
            return (isinstance(node, ast.For), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FormattedValue(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FormattedValue], ast.AST]:
            return (isinstance(node, ast.FormattedValue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FunctionDef(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FunctionDef], ast.AST]:
            return (isinstance(node, ast.FunctionDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FunctionType(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FunctionType], ast.AST]:
            return (isinstance(node, ast.FunctionType), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def GeneratorExp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.GeneratorExp], ast.AST]:
            return (isinstance(node, ast.GeneratorExp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Global(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Global], ast.AST]:
            return (isinstance(node, ast.Global), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Gt(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Gt], ast.AST]:
            return (isinstance(node, ast.Gt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def GtE(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.GtE], ast.AST]:
            return (isinstance(node, ast.GtE), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def If(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.If], ast.AST]:
            return (isinstance(node, ast.If), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def IfExp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.IfExp], ast.AST]:
            return (isinstance(node, ast.IfExp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Import(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Import], ast.AST]:
            return (isinstance(node, ast.Import), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ImportFrom(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ImportFrom], ast.AST]:
            return (isinstance(node, ast.ImportFrom), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def In(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.In], ast.AST]:
            return (isinstance(node, ast.In), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Interactive(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Interactive], ast.AST]:
            return (isinstance(node, ast.Interactive), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Invert(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Invert], ast.AST]:
            return (isinstance(node, ast.Invert), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Is(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Is], ast.AST]:
            return (isinstance(node, ast.Is), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def IsNot(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.IsNot], ast.AST]:
            return (isinstance(node, ast.IsNot), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def JoinedStr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.JoinedStr], ast.AST]:
            return (isinstance(node, ast.JoinedStr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def keyword(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.keyword], ast.AST]:
            return (isinstance(node, ast.keyword), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Lambda(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Lambda], ast.AST]:
            return (isinstance(node, ast.Lambda), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def List(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.List], ast.AST]:
            return (isinstance(node, ast.List), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ListComp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ListComp], ast.AST]:
            return (isinstance(node, ast.ListComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Load(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Load], ast.AST]:
            return (isinstance(node, ast.Load), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def LShift(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.LShift], ast.AST]:
            return (isinstance(node, ast.LShift), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Lt(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Lt], ast.AST]:
            return (isinstance(node, ast.Lt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def LtE(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.LtE], ast.AST]:
            return (isinstance(node, ast.LtE), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Match(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Match], ast.AST]:
            return (isinstance(node, ast.Match), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def match_case(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.match_case], ast.AST]:
            return (isinstance(node, ast.match_case), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchAs(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchAs], ast.AST]:
            return (isinstance(node, ast.MatchAs), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchClass(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchClass], ast.AST]:
            return (isinstance(node, ast.MatchClass), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchMapping(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchMapping], ast.AST]:
            return (isinstance(node, ast.MatchMapping), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchOr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchOr], ast.AST]:
            return (isinstance(node, ast.MatchOr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchSequence(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchSequence], ast.AST]:
            return (isinstance(node, ast.MatchSequence), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchSingleton(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchSingleton], ast.AST]:
            return (isinstance(node, ast.MatchSingleton), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchStar(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchStar], ast.AST]:
            return (isinstance(node, ast.MatchStar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchValue(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchValue], ast.AST]:
            return (isinstance(node, ast.MatchValue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatMult(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatMult], ast.AST]:
            return (isinstance(node, ast.MatMult), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def mod(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.mod], ast.AST]:
            return (isinstance(node, ast.mod), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Mod(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Mod], ast.AST]:
            return (isinstance(node, ast.Mod), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Module(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Module], ast.AST]:
            return (isinstance(node, ast.Module), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Mult(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Mult], ast.AST]:
            return (isinstance(node, ast.Mult), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Name(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Name], ast.AST]:
            return (isinstance(node, ast.Name), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NamedExpr(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NamedExpr], ast.AST]:
            return (isinstance(node, ast.NamedExpr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Nonlocal(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Nonlocal], ast.AST]:
            return (isinstance(node, ast.Nonlocal), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Not(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Not], ast.AST]:
            return (isinstance(node, ast.Not), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NotEq(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NotEq], ast.AST]:
            return (isinstance(node, ast.NotEq), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NotIn(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NotIn], ast.AST]:
            return (isinstance(node, ast.NotIn), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def operator(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.operator], ast.AST]:
            return (isinstance(node, ast.operator), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Or(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Or], ast.AST]:
            return (isinstance(node, ast.Or), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ParamSpec(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ParamSpec], ast.AST]:
            return (isinstance(node, ast.ParamSpec), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Pass(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Pass], ast.AST]:
            return (isinstance(node, ast.Pass), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def pattern(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.pattern], ast.AST]:
            return (isinstance(node, ast.pattern), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Pow(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Pow], ast.AST]:
            return (isinstance(node, ast.Pow), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Raise(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Raise], ast.AST]:
            return (isinstance(node, ast.Raise), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Return(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Return], ast.AST]:
            return (isinstance(node, ast.Return), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def RShift(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.RShift], ast.AST]:
            return (isinstance(node, ast.RShift), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Set(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Set], ast.AST]:
            return (isinstance(node, ast.Set), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def SetComp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.SetComp], ast.AST]:
            return (isinstance(node, ast.SetComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Slice(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Slice], ast.AST]:
            return (isinstance(node, ast.Slice), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Starred(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Starred], ast.AST]:
            return (isinstance(node, ast.Starred), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def stmt(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.stmt], ast.AST]:
            return (isinstance(node, ast.stmt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Store(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Store], ast.AST]:
            return (isinstance(node, ast.Store), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Sub(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Sub], ast.AST]:
            return (isinstance(node, ast.Sub), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Subscript(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Subscript], ast.AST]:
            return (isinstance(node, ast.Subscript), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Try(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Try], ast.AST]:
            return (isinstance(node, ast.Try), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TryStar(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TryStar], ast.AST]:
            return (isinstance(node, ast.TryStar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Tuple(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Tuple], ast.AST]:
            return (isinstance(node, ast.Tuple), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def type_ignore(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.type_ignore], ast.AST]:
            return (isinstance(node, ast.type_ignore), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def type_param(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.type_param], ast.AST]:
            return (isinstance(node, ast.type_param), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeAlias(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeAlias], ast.AST]:
            return (isinstance(node, ast.TypeAlias), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeIgnore(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeIgnore], ast.AST]:
            return (isinstance(node, ast.TypeIgnore), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeVar(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeVar], ast.AST]:
            return (isinstance(node, ast.TypeVar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeVarTuple(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeVarTuple], ast.AST]:
            return (isinstance(node, ast.TypeVarTuple), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def UAdd(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.UAdd], ast.AST]:
            return (isinstance(node, ast.UAdd), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def unaryop(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.unaryop], ast.AST]:
            return (isinstance(node, ast.unaryop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def UnaryOp(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.UnaryOp], ast.AST]:
            return (isinstance(node, ast.UnaryOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def USub(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.USub], ast.AST]:
            return (isinstance(node, ast.USub), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def While(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.While], ast.AST]:
            return (isinstance(node, ast.While), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def With(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.With], ast.AST]:
            return (isinstance(node, ast.With), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def withitem(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.withitem], ast.AST]:
            return (isinstance(node, ast.withitem), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Yield(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Yield], ast.AST]:
            return (isinstance(node, ast.Yield), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def YieldFrom(self) -> 'Find':

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.YieldFrom], ast.AST]:
            return (isinstance(node, ast.YieldFrom), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)