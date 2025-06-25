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
    'A comprehensive suite of functions for AST class identification and type narrowing.\n\n    `class` `Be` has a method for each `ast.AST` subclass, also called "node type", to perform type\n    checking while enabling compile-time type narrowing through `TypeIs` annotations. This tool\n    forms the foundation of type-safe AST analysis and transformation throughout astToolkit.\n\n    Each method takes an `ast.AST` node and returns a `TypeIs` that confirms both runtime type\n    safety and enables static type checkers to narrow the node type in conditional contexts. This\n    eliminates the need for unsafe casting while providing comprehensive coverage of Python\'s AST\n    node hierarchy.\n\n    Methods correspond directly to Python AST node types, following the naming convention of the AST\n    classes themselves. Coverage includes expression nodes (`Add`, `Call`, `Name`), statement nodes\n    (`Assign`, `FunctionDef`, `Return`), operator nodes (`And`, `Or`, `Not`), and structural nodes\n    (`Module`, `arguments`, `keyword`).\n\n    The `class` is the primary type-checker in the antecedent-action pattern, where predicates\n    identify target nodes and actions, uh... act on nodes and their attributes. Type guards from\n    this class are commonly used as building blocks in `IfThis` predicates and directly as\n    `findThis` parameters in visitor classes.\n\n    Parameters\n    ----------\n    node : ast.AST\n        The AST node to test for specific type membership.\n\n    Returns\n    -------\n    typeIs : `TypeIs`\n        A `TypeIs` instance that confirms the node\'s type and narrows its type in\n        static type checkers.\n\n    Examples\n    --------\n    Type-safe node processing with automatic type narrowing:\n\n    ```python\n        if Be.FunctionDef(node):\n            functionName = node.name  # Type-safe access to name attribute parameterCount =\n            len(node.args.args)\n    ```\n\n    Using type guards in visitor patterns:\n\n    ```python\n        NodeTourist(Be.Return, Then.extractIt(DOT.value)).visit(functionNode)\n    ```\n\n    Type-safe access to attributes of specific node types:\n\n    ```python\n        if Be.Call(node) and Be.Name(node.func):\n            callableName = node.func.id  # Type-safe access to function name\n    ```\n\n    '

    def Add(self) -> 'Find':
        """`Be.Add` matches any of `class` `ast.Add` | `ast.Add`.

        This `class` is associated with Python delimiters '+=' and Python operators '+'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Add], ast.AST]:
            return (isinstance(node, ast.Add), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def alias(self) -> 'Find':
        """`Be.alias` matches `class` `ast.alias`.

        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.alias], ast.AST]:
            return (isinstance(node, ast.alias), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def And(self) -> 'Find':
        """`Be.And` matches any of `ast.And` | `class` `ast.And`.

        This `class` is associated with Python keywords `and`.
        It is a subclass of `ast.boolop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.And], ast.AST]:
            return (isinstance(node, ast.And), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AnnAssign(self) -> 'Find':
        """`Be.AnnAssign`, ***Ann***otated ***Assign***ment, matches `class` `ast.AnnAssign`.

        This `class` is associated with Python delimiters ':, ='.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AnnAssign], ast.AST]:
            return (isinstance(node, ast.AnnAssign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def arg(self) -> 'Find':
        """`Be.arg`, ***arg***ument, matches `class` `ast.arg`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.arg], ast.AST]:
            return (isinstance(node, ast.arg), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def arguments(self) -> 'Find':
        """`Be.arguments` matches `class` `ast.arguments`.

        This `class` is associated with Python delimiters ','.
        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.arguments], ast.AST]:
            return (isinstance(node, ast.arguments), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Assert(self) -> 'Find':
        """`Be.Assert` matches `class` `ast.Assert`.

        This `class` is associated with Python keywords `assert`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Assert], ast.AST]:
            return (isinstance(node, ast.Assert), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Assign(self) -> 'Find':
        """`Be.Assign` matches `class` `ast.Assign`.

        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Assign], ast.AST]:
            return (isinstance(node, ast.Assign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AST(self) -> 'Find':
        """`Be.AST`, Abstract Syntax Tree, matches any of `ast.slice` | `ast.NodeList` | `ast.type_ignore` | `ast.mod` | `ast.keyword` | `ast.arg` | `ast.Exec` | `ast.match_case` | `ast.comprehension` | `ast.cmpop` | `ast.alias` | `ast.arguments` | `ast.stmt` | `ast.withitem` | `ast.expr_context` | `ast.unaryop` | `ast.pattern` | `ast._NoParent` | `ast.excepthandler` | `ast.type_param` | `ast.operator` | `class` `ast.AST` | `ast.boolop` | `ast.expr`.

        It is a subclass of `ast.object`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AST], ast.AST]:
            return (isinstance(node, ast.AST), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncFor(self) -> 'Find':
        """`Be.AsyncFor`, ***Async***hronous For loop, matches `class` `ast.AsyncFor`.

        This `class` is associated with Python keywords `async for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncFor], ast.AST]:
            return (isinstance(node, ast.AsyncFor), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncFunctionDef(self) -> 'Find':
        """`Be.AsyncFunctionDef`, ***Async***hronous Function ***Def***inition, matches `class` `ast.AsyncFunctionDef`.

        This `class` is associated with Python keywords `async def` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncFunctionDef], ast.AST]:
            return (isinstance(node, ast.AsyncFunctionDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AsyncWith(self) -> 'Find':
        """`Be.AsyncWith`, ***Async***hronous With statement, matches `class` `ast.AsyncWith`.

        This `class` is associated with Python keywords `async with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AsyncWith], ast.AST]:
            return (isinstance(node, ast.AsyncWith), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Attribute(self) -> 'Find':
        """`Be.Attribute` matches `class` `ast.Attribute`.

        This `class` is associated with Python delimiters '.'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Attribute], ast.AST]:
            return (isinstance(node, ast.Attribute), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def AugAssign(self) -> 'Find':
        """`Be.AugAssign`, ***Aug***mented ***Assign***ment, matches `class` `ast.AugAssign`.

        This `class` is associated with Python delimiters '+=, -=, *=, /=, //=, %=, **=, |=, &=, ^=, <<=, >>='.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.AugAssign], ast.AST]:
            return (isinstance(node, ast.AugAssign), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Await(self) -> 'Find':
        """`Be.Await`, ***Await*** the asynchronous operation, matches `class` `ast.Await`.

        This `class` is associated with Python keywords `await`.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Await], ast.AST]:
            return (isinstance(node, ast.Await), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BinOp(self) -> 'Find':
        """`Be.BinOp`, ***Bin***ary ***Op***eration, matches `class` `ast.BinOp`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BinOp], ast.AST]:
            return (isinstance(node, ast.BinOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitAnd(self) -> 'Find':
        """`Be.BitAnd`, ***Bit***wise And, matches any of `ast.BitAnd` | `class` `ast.BitAnd`.

        This `class` is associated with Python operators '&'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitAnd], ast.AST]:
            return (isinstance(node, ast.BitAnd), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitOr(self) -> 'Find':
        """`Be.BitOr`, ***Bit***wise Or, matches any of `class` `ast.BitOr` | `ast.BitOr`.

        This `class` is associated with Python operators '|'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitOr], ast.AST]:
            return (isinstance(node, ast.BitOr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BitXor(self) -> 'Find':
        """`Be.BitXor`, ***Bit***wise e***X***clusive Or, matches any of `class` `ast.BitXor` | `ast.BitXor`.

        This `class` is associated with Python operators '^'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BitXor], ast.AST]:
            return (isinstance(node, ast.BitXor), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def boolop(self) -> 'Find':
        """`Be.boolop`, ***bool***ean ***op***erator, matches any of `ast.And` | `ast.Or` | `class` `ast.boolop`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.boolop], ast.AST]:
            return (isinstance(node, ast.boolop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def BoolOp(self) -> 'Find':
        """`Be.BoolOp`, ***Bool***ean ***Op***eration, matches `class` `ast.BoolOp`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.BoolOp], ast.AST]:
            return (isinstance(node, ast.BoolOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Break(self) -> 'Find':
        """`Be.Break` matches `class` `ast.Break`.

        This `class` is associated with Python keywords `break`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Break], ast.AST]:
            return (isinstance(node, ast.Break), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Call(self) -> 'Find':
        """`Be.Call` matches `class` `ast.Call`.

        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Call], ast.AST]:
            return (isinstance(node, ast.Call), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ClassDef(self) -> 'Find':
        """`Be.ClassDef`, ***Class*** ***Def***inition, matches `class` `ast.ClassDef`.

        This `class` is associated with Python keywords `class` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ClassDef], ast.AST]:
            return (isinstance(node, ast.ClassDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def cmpop(self) -> 'Find':
        """`Be.cmpop`, ***c***o***mp***arison ***op***erator, matches any of `ast.NotEq` | `ast.NotIn` | `ast.GtE` | `ast.Gt` | `class` `ast.cmpop` | `ast.Lt` | `ast.LtE` | `ast.In` | `ast.Is` | `ast.Eq` | `ast.IsNot`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.cmpop], ast.AST]:
            return (isinstance(node, ast.cmpop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Compare(self) -> 'Find':
        """`Be.Compare` matches `class` `ast.Compare`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Compare], ast.AST]:
            return (isinstance(node, ast.Compare), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def comprehension(self) -> 'Find':
        """`Be.comprehension` matches `class` `ast.comprehension`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.comprehension], ast.AST]:
            return (isinstance(node, ast.comprehension), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Constant(self) -> 'Find':
        """`Be.Constant` matches any of `ast.NameConstant` | `ast.Ellipsis` | `ast.Str` | `ast.Bytes` | `ast.Num` | `class` `ast.Constant`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Constant], ast.AST]:
            return (isinstance(node, ast.Constant), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Continue(self) -> 'Find':
        """`Be.Continue` matches `class` `ast.Continue`.

        This `class` is associated with Python keywords `continue`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Continue], ast.AST]:
            return (isinstance(node, ast.Continue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Del(self) -> 'Find':
        """`Be.Del`, ***Del***ete, matches `class` `ast.Del`.

        It is a subclass of `ast.expr_context`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Del], ast.AST]:
            return (isinstance(node, ast.Del), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Delete(self) -> 'Find':
        """`Be.Delete` matches `class` `ast.Delete`.

        This `class` is associated with Python keywords `del`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Delete], ast.AST]:
            return (isinstance(node, ast.Delete), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Dict(self) -> 'Find':
        """`Be.Dict`, ***Dict***ionary, matches `class` `ast.Dict`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Dict], ast.AST]:
            return (isinstance(node, ast.Dict), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def DictComp(self) -> 'Find':
        """`Be.DictComp`, ***Dict***ionary ***c***o***mp***rehension, matches `class` `ast.DictComp`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.DictComp], ast.AST]:
            return (isinstance(node, ast.DictComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Div(self) -> 'Find':
        """`Be.Div`, ***Div***ision, matches any of `class` `ast.Div` | `ast.Div`.

        This `class` is associated with Python delimiters '/=' and Python operators '/'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Div], ast.AST]:
            return (isinstance(node, ast.Div), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Eq(self) -> 'Find':
        """`Be.Eq`, is ***Eq***ual to, matches `class` `ast.Eq`.

        This `class` is associated with Python operators '=='.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Eq], ast.AST]:
            return (isinstance(node, ast.Eq), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def excepthandler(self) -> 'Find':
        """`Be.excepthandler`, ***except***ion ***handler***, matches any of `ast.ExceptHandler` | `class` `ast.excepthandler`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.excepthandler], ast.AST]:
            return (isinstance(node, ast.excepthandler), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ExceptHandler(self) -> 'Find':
        """`Be.ExceptHandler`, ***Except***ion ***Handler***, matches `class` `ast.ExceptHandler`.

        This `class` is associated with Python keywords `except`.
        It is a subclass of `ast.excepthandler`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ExceptHandler], ast.AST]:
            return (isinstance(node, ast.ExceptHandler), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def expr(self) -> 'Find':
        """`Be.expr`, ***expr***ession, matches any of `ast.Subscript` | `ast.UnaryOp` | `ast.DictComp` | `ast.Name` | `ast.Tuple` | `ast.BoolOp` | `ast.IfExp` | `ast.JoinedStr` | `ast.NamedExpr` | `ast.YieldFrom` | `ast.Yield` | `ast.Starred` | `ast.List` | `ast.FormattedValue` | `ast.SetComp` | `ast.Dict` | `ast.BinOp` | `ast.Compare` | `ast.Set` | `ast.Attribute` | `ast.Call` | `ast.Await` | `ast.Lambda` | `ast.GeneratorExp` | `ast.Slice` | `ast.ListComp` | `class` `ast.expr` | `ast.Constant`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.expr], ast.AST]:
            return (isinstance(node, ast.expr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Expr(self) -> 'Find':
        """`Be.Expr`, ***Expr***ession, matches `class` `ast.Expr`.

        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Expr], ast.AST]:
            return (isinstance(node, ast.Expr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def expr_context(self) -> 'Find':
        """`Be.expr_context`, ***expr***ession ***context***, matches any of `ast.AugStore` | `ast.Del` | `ast.Load` | `class` `ast.expr_context` | `ast.Param` | `ast.AugLoad` | `ast.Store`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.expr_context], ast.AST]:
            return (isinstance(node, ast.expr_context), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Expression(self) -> 'Find':
        """`Be.Expression` matches `class` `ast.Expression`.

        It is a subclass of `ast.mod`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Expression], ast.AST]:
            return (isinstance(node, ast.Expression), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FloorDiv(self) -> 'Find':
        """`Be.FloorDiv`, Floor ***Div***ision, matches any of `ast.FloorDiv` | `class` `ast.FloorDiv`.

        This `class` is associated with Python delimiters '//=' and Python operators '//'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FloorDiv], ast.AST]:
            return (isinstance(node, ast.FloorDiv), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def For(self) -> 'Find':
        """`Be.For` matches `class` `ast.For`.

        This `class` is associated with Python keywords `for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.For], ast.AST]:
            return (isinstance(node, ast.For), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FormattedValue(self) -> 'Find':
        """`Be.FormattedValue` matches `class` `ast.FormattedValue`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FormattedValue], ast.AST]:
            return (isinstance(node, ast.FormattedValue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FunctionDef(self) -> 'Find':
        """`Be.FunctionDef`, Function ***Def***inition, matches `class` `ast.FunctionDef`.

        This `class` is associated with Python keywords `def` and Python delimiters '()'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FunctionDef], ast.AST]:
            return (isinstance(node, ast.FunctionDef), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def FunctionType(self) -> 'Find':
        """`Be.FunctionType`, Function Type, matches `class` `ast.FunctionType`.

        It is a subclass of `ast.mod`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.FunctionType], ast.AST]:
            return (isinstance(node, ast.FunctionType), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def GeneratorExp(self) -> 'Find':
        """`Be.GeneratorExp`, Generator ***Exp***ression, matches `class` `ast.GeneratorExp`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.GeneratorExp], ast.AST]:
            return (isinstance(node, ast.GeneratorExp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Global(self) -> 'Find':
        """`Be.Global` matches `class` `ast.Global`.

        This `class` is associated with Python keywords `global`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Global], ast.AST]:
            return (isinstance(node, ast.Global), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Gt(self) -> 'Find':
        """`Be.Gt`, is Greater than, matches `class` `ast.Gt`.

        This `class` is associated with Python operators '>'.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Gt], ast.AST]:
            return (isinstance(node, ast.Gt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def GtE(self) -> 'Find':
        """`Be.GtE`, is Greater than or Equal to, matches `class` `ast.GtE`.

        This `class` is associated with Python operators '>='.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.GtE], ast.AST]:
            return (isinstance(node, ast.GtE), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def If(self) -> 'Find':
        """`Be.If` matches `class` `ast.If`.

        This `class` is associated with Python keywords `if` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.If], ast.AST]:
            return (isinstance(node, ast.If), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def IfExp(self) -> 'Find':
        """`Be.IfExp`, If ***Exp***ression, matches `class` `ast.IfExp`.

        This `class` is associated with Python keywords `if`.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.IfExp], ast.AST]:
            return (isinstance(node, ast.IfExp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Import(self) -> 'Find':
        """`Be.Import` matches `class` `ast.Import`.

        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Import], ast.AST]:
            return (isinstance(node, ast.Import), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ImportFrom(self) -> 'Find':
        """`Be.ImportFrom` matches `class` `ast.ImportFrom`.

        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ImportFrom], ast.AST]:
            return (isinstance(node, ast.ImportFrom), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def In(self) -> 'Find':
        """`Be.In` matches `class` `ast.In`.

        This `class` is associated with Python keywords `in`.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.In], ast.AST]:
            return (isinstance(node, ast.In), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Interactive(self) -> 'Find':
        """`Be.Interactive`, Interactive mode, matches `class` `ast.Interactive`.

        It is a subclass of `ast.mod`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Interactive], ast.AST]:
            return (isinstance(node, ast.Interactive), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Invert(self) -> 'Find':
        """`Be.Invert` matches `class` `ast.Invert`.

        This `class` is associated with Python operators '~'.
        It is a subclass of `ast.unaryop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Invert], ast.AST]:
            return (isinstance(node, ast.Invert), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Is(self) -> 'Find':
        """`Be.Is` matches `class` `ast.Is`.

        This `class` is associated with Python keywords `is`.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Is], ast.AST]:
            return (isinstance(node, ast.Is), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def IsNot(self) -> 'Find':
        """`Be.IsNot` matches `class` `ast.IsNot`.

        This `class` is associated with Python keywords `is not`.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.IsNot], ast.AST]:
            return (isinstance(node, ast.IsNot), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def JoinedStr(self) -> 'Find':
        """`Be.JoinedStr`, Joined ***Str***ing, matches `class` `ast.JoinedStr`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.JoinedStr], ast.AST]:
            return (isinstance(node, ast.JoinedStr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def keyword(self) -> 'Find':
        """`Be.keyword` matches `class` `ast.keyword`.

        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.keyword], ast.AST]:
            return (isinstance(node, ast.keyword), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Lambda(self) -> 'Find':
        """`Be.Lambda`, Lambda function, matches `class` `ast.Lambda`.

        This `class` is associated with Python keywords `lambda` and Python delimiters ':'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Lambda], ast.AST]:
            return (isinstance(node, ast.Lambda), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def List(self) -> 'Find':
        """`Be.List` matches `class` `ast.List`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.List], ast.AST]:
            return (isinstance(node, ast.List), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ListComp(self) -> 'Find':
        """`Be.ListComp`, List ***c***o***mp***rehension, matches `class` `ast.ListComp`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ListComp], ast.AST]:
            return (isinstance(node, ast.ListComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Load(self) -> 'Find':
        """`Be.Load` matches `class` `ast.Load`.

        It is a subclass of `ast.expr_context`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Load], ast.AST]:
            return (isinstance(node, ast.Load), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def LShift(self) -> 'Find':
        """`Be.LShift`, Left Shift, matches any of `ast.LShift` | `class` `ast.LShift`.

        This `class` is associated with Python delimiters '<<=' and Python operators '<<'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.LShift], ast.AST]:
            return (isinstance(node, ast.LShift), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Lt(self) -> 'Find':
        """`Be.Lt`, is Less than, matches `class` `ast.Lt`.

        This `class` is associated with Python operators '<'.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Lt], ast.AST]:
            return (isinstance(node, ast.Lt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def LtE(self) -> 'Find':
        """`Be.LtE`, is Less than or Equal to, matches `class` `ast.LtE`.

        This `class` is associated with Python operators '<='.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.LtE], ast.AST]:
            return (isinstance(node, ast.LtE), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Match(self) -> 'Find':
        """`Be.Match`, Match this, matches `class` `ast.Match`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Match], ast.AST]:
            return (isinstance(node, ast.Match), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def match_case(self) -> 'Find':
        """`Be.match_case`, match case, matches `class` `ast.match_case`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.match_case], ast.AST]:
            return (isinstance(node, ast.match_case), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchAs(self) -> 'Find':
        """`Be.MatchAs`, Match As, matches `class` `ast.MatchAs`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchAs], ast.AST]:
            return (isinstance(node, ast.MatchAs), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchClass(self) -> 'Find':
        """`Be.MatchClass`, Match Class, matches `class` `ast.MatchClass`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchClass], ast.AST]:
            return (isinstance(node, ast.MatchClass), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchMapping(self) -> 'Find':
        """`Be.MatchMapping`, Match Mapping, matches `class` `ast.MatchMapping`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchMapping], ast.AST]:
            return (isinstance(node, ast.MatchMapping), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchOr(self) -> 'Find':
        """`Be.MatchOr`, Match this Or that, matches `class` `ast.MatchOr`.

        This `class` is associated with Python delimiters ':' and Python operators '|'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchOr], ast.AST]:
            return (isinstance(node, ast.MatchOr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchSequence(self) -> 'Find':
        """`Be.MatchSequence`, Match this Sequence, matches `class` `ast.MatchSequence`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchSequence], ast.AST]:
            return (isinstance(node, ast.MatchSequence), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchSingleton(self) -> 'Find':
        """`Be.MatchSingleton`, Match Singleton, matches `class` `ast.MatchSingleton`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchSingleton], ast.AST]:
            return (isinstance(node, ast.MatchSingleton), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchStar(self) -> 'Find':
        """`Be.MatchStar`, Match Star, matches `class` `ast.MatchStar`.

        This `class` is associated with Python delimiters ':' and Python operators '*'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchStar], ast.AST]:
            return (isinstance(node, ast.MatchStar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatchValue(self) -> 'Find':
        """`Be.MatchValue`, Match Value, matches `class` `ast.MatchValue`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatchValue], ast.AST]:
            return (isinstance(node, ast.MatchValue), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def MatMult(self) -> 'Find':
        """`Be.MatMult`, ***Mat***rix ***Mult***iplication, matches any of `class` `ast.MatMult` | `ast.MatMult`.

        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.MatMult], ast.AST]:
            return (isinstance(node, ast.MatMult), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def mod(self) -> 'Find':
        """`Be.mod`, ***mod***ule, matches any of `ast.FunctionType` | `class` `ast.mod` | `ast.Suite` | `ast.Module` | `ast.Expression` | `ast.Interactive`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.mod], ast.AST]:
            return (isinstance(node, ast.mod), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Mod(self) -> 'Find':
        """`Be.Mod`, ***Mod***ulo, matches any of `class` `ast.Mod` | `ast.Mod`.

        This `class` is associated with Python delimiters '%=' and Python operators '%'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Mod], ast.AST]:
            return (isinstance(node, ast.Mod), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Module(self) -> 'Find':
        """`Be.Module` matches `class` `ast.Module`.

        It is a subclass of `ast.mod`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Module], ast.AST]:
            return (isinstance(node, ast.Module), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Mult(self) -> 'Find':
        """`Be.Mult`, ***Mult***iplication, matches any of `class` `ast.Mult` | `ast.Mult`.

        This `class` is associated with Python delimiters '*=' and Python operators '*'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Mult], ast.AST]:
            return (isinstance(node, ast.Mult), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Name(self) -> 'Find':
        """`Be.Name` matches `class` `ast.Name`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Name], ast.AST]:
            return (isinstance(node, ast.Name), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NamedExpr(self) -> 'Find':
        """`Be.NamedExpr`, Named ***Expr***ession, matches `class` `ast.NamedExpr`.

        This `class` is associated with Python operators ':='.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NamedExpr], ast.AST]:
            return (isinstance(node, ast.NamedExpr), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Nonlocal(self) -> 'Find':
        """`Be.Nonlocal` matches `class` `ast.Nonlocal`.

        This `class` is associated with Python keywords `nonlocal`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Nonlocal], ast.AST]:
            return (isinstance(node, ast.Nonlocal), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Not(self) -> 'Find':
        """`Be.Not` matches `class` `ast.Not`.

        This `class` is associated with Python keywords `not`.
        It is a subclass of `ast.unaryop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Not], ast.AST]:
            return (isinstance(node, ast.Not), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NotEq(self) -> 'Find':
        """`Be.NotEq`, is Not ***Eq***ual to, matches `class` `ast.NotEq`.

        This `class` is associated with Python operators '!='.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NotEq], ast.AST]:
            return (isinstance(node, ast.NotEq), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def NotIn(self) -> 'Find':
        """`Be.NotIn`, is Not ***In***cluded in or does Not have membership In, matches `class` `ast.NotIn`.

        This `class` is associated with Python keywords `not in`.
        It is a subclass of `ast.cmpop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.NotIn], ast.AST]:
            return (isinstance(node, ast.NotIn), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def operator(self) -> 'Find':
        """`Be.operator` matches any of `ast.MatMult` | `ast.Pow` | `ast.FloorDiv` | `ast.LShift` | `ast.RShift` | `ast.BitAnd` | `ast.Sub` | `ast.BitOr` | `class` `ast.operator` | `ast.BitXor` | `ast.Add` | `ast.Mod` | `ast.Div` | `ast.Mult`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.operator], ast.AST]:
            return (isinstance(node, ast.operator), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Or(self) -> 'Find':
        """`Be.Or` matches any of `ast.Or` | `class` `ast.Or`.

        This `class` is associated with Python keywords `or`.
        It is a subclass of `ast.boolop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Or], ast.AST]:
            return (isinstance(node, ast.Or), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def ParamSpec(self) -> 'Find':
        """`Be.ParamSpec`, ***Param***eter ***Spec***ification, matches `class` `ast.ParamSpec`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.type_param`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.ParamSpec], ast.AST]:
            return (isinstance(node, ast.ParamSpec), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Pass(self) -> 'Find':
        """`Be.Pass` matches `class` `ast.Pass`.

        This `class` is associated with Python keywords `pass`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Pass], ast.AST]:
            return (isinstance(node, ast.Pass), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def pattern(self) -> 'Find':
        """`Be.pattern` matches any of `ast.MatchOr` | `ast.MatchAs` | `ast.MatchMapping` | `ast.MatchClass` | `class` `ast.pattern` | `ast.MatchSequence` | `ast.MatchSingleton` | `ast.MatchStar` | `ast.MatchValue`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.pattern], ast.AST]:
            return (isinstance(node, ast.pattern), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Pow(self) -> 'Find':
        """`Be.Pow`, ***Pow***er, matches any of `class` `ast.Pow` | `ast.Pow`.

        This `class` is associated with Python delimiters '**=' and Python operators '**'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Pow], ast.AST]:
            return (isinstance(node, ast.Pow), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Raise(self) -> 'Find':
        """`Be.Raise` matches `class` `ast.Raise`.

        This `class` is associated with Python keywords `raise`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Raise], ast.AST]:
            return (isinstance(node, ast.Raise), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Return(self) -> 'Find':
        """`Be.Return` matches `class` `ast.Return`.

        This `class` is associated with Python keywords `return`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Return], ast.AST]:
            return (isinstance(node, ast.Return), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def RShift(self) -> 'Find':
        """`Be.RShift`, Right Shift, matches any of `ast.RShift` | `class` `ast.RShift`.

        This `class` is associated with Python delimiters '>>=' and Python operators '>>'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.RShift], ast.AST]:
            return (isinstance(node, ast.RShift), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Set(self) -> 'Find':
        """`Be.Set` matches `class` `ast.Set`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Set], ast.AST]:
            return (isinstance(node, ast.Set), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def SetComp(self) -> 'Find':
        """`Be.SetComp`, Set ***c***o***mp***rehension, matches `class` `ast.SetComp`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.SetComp], ast.AST]:
            return (isinstance(node, ast.SetComp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Slice(self) -> 'Find':
        """`Be.Slice` matches `class` `ast.Slice`.

        This `class` is associated with Python delimiters '[], :'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Slice], ast.AST]:
            return (isinstance(node, ast.Slice), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Starred(self) -> 'Find':
        """`Be.Starred` matches `class` `ast.Starred`.

        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Starred], ast.AST]:
            return (isinstance(node, ast.Starred), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def stmt(self) -> 'Find':
        """`Be.stmt`, ***st***ate***m***en***t***, matches any of `ast.Delete` | `ast.Import` | `ast.Assert` | `ast.Try` | `ast.Raise` | `ast.Expr` | `class` `ast.stmt` | `ast.Break` | `ast.Match` | `ast.Nonlocal` | `ast.AsyncFor` | `ast.Assign` | `ast.Pass` | `ast.Continue` | `ast.ClassDef` | `ast.TryStar` | `ast.TypeAlias` | `ast.If` | `ast.AnnAssign` | `ast.With` | `ast.FunctionDef` | `ast.Return` | `ast.AugAssign` | `ast.While` | `ast.AsyncFunctionDef` | `ast.For` | `ast.AsyncWith` | `ast.Global` | `ast.ImportFrom`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.stmt], ast.AST]:
            return (isinstance(node, ast.stmt), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Store(self) -> 'Find':
        """`Be.Store` matches `class` `ast.Store`.

        It is a subclass of `ast.expr_context`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Store], ast.AST]:
            return (isinstance(node, ast.Store), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Sub(self) -> 'Find':
        """`Be.Sub`, ***Sub***traction, matches any of `class` `ast.Sub` | `ast.Sub`.

        This `class` is associated with Python delimiters '-=' and Python operators '-'.
        It is a subclass of `ast.operator`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Sub], ast.AST]:
            return (isinstance(node, ast.Sub), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Subscript(self) -> 'Find':
        """`Be.Subscript` matches `class` `ast.Subscript`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Subscript], ast.AST]:
            return (isinstance(node, ast.Subscript), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Try(self) -> 'Find':
        """`Be.Try` matches `class` `ast.Try`.

        This `class` is associated with Python keywords `try`, `except` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Try], ast.AST]:
            return (isinstance(node, ast.Try), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TryStar(self) -> 'Find':
        """`Be.TryStar`, Try executing this, protected by `except*` ("except star"), matches `class` `ast.TryStar`.

        This `class` is associated with Python keywords `try`, `except*` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TryStar], ast.AST]:
            return (isinstance(node, ast.TryStar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Tuple(self) -> 'Find':
        """`Be.Tuple` matches `class` `ast.Tuple`.

        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Tuple], ast.AST]:
            return (isinstance(node, ast.Tuple), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def type_ignore(self) -> 'Find':
        """`Be.type_ignore`, this `type` error, you ignore it, matches any of `ast.TypeIgnore` | `class` `ast.type_ignore`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.type_ignore], ast.AST]:
            return (isinstance(node, ast.type_ignore), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def type_param(self) -> 'Find':
        """`Be.type_param`, type ***param***eter, matches any of `ast.ParamSpec` | `ast.TypeVar` | `ast.TypeVarTuple` | `class` `ast.type_param`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.type_param], ast.AST]:
            return (isinstance(node, ast.type_param), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeAlias(self) -> 'Find':
        """`Be.TypeAlias`, Type Alias, matches `class` `ast.TypeAlias`.

        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeAlias], ast.AST]:
            return (isinstance(node, ast.TypeAlias), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeIgnore(self) -> 'Find':
        """`Be.TypeIgnore`, this Type (`type`) error, Ignore it, matches `class` `ast.TypeIgnore`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.type_ignore`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeIgnore], ast.AST]:
            return (isinstance(node, ast.TypeIgnore), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeVar(self) -> 'Find':
        """`Be.TypeVar`, Type ***Var***iable, matches `class` `ast.TypeVar`.

        It is a subclass of `ast.type_param`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeVar], ast.AST]:
            return (isinstance(node, ast.TypeVar), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def TypeVarTuple(self) -> 'Find':
        """`Be.TypeVarTuple`, Type ***Var***iable ***Tuple***, matches `class` `ast.TypeVarTuple`.

        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.type_param`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.TypeVarTuple], ast.AST]:
            return (isinstance(node, ast.TypeVarTuple), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def UAdd(self) -> 'Find':
        """`Be.UAdd`, ***U***nary ***Add***ition, matches `class` `ast.UAdd`.

        This `class` is associated with Python operators '+'.
        It is a subclass of `ast.unaryop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.UAdd], ast.AST]:
            return (isinstance(node, ast.UAdd), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def unaryop(self) -> 'Find':
        """`Be.unaryop`, ***un***ary ***op***erator, matches any of `ast.UAdd` | `ast.Not` | `class` `ast.unaryop` | `ast.Invert` | `ast.USub`.

        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.unaryop], ast.AST]:
            return (isinstance(node, ast.unaryop), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def UnaryOp(self) -> 'Find':
        """`Be.UnaryOp`, ***Un***ary ***Op***eration, matches `class` `ast.UnaryOp`.

        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.UnaryOp], ast.AST]:
            return (isinstance(node, ast.UnaryOp), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def USub(self) -> 'Find':
        """`Be.USub`, ***U***nary ***Sub***traction, matches `class` `ast.USub`.

        This `class` is associated with Python operators '-'.
        It is a subclass of `ast.unaryop`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.USub], ast.AST]:
            return (isinstance(node, ast.USub), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def While(self) -> 'Find':
        """`Be.While` matches `class` `ast.While`.

        This `class` is associated with Python keywords `while`.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.While], ast.AST]:
            return (isinstance(node, ast.While), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def With(self) -> 'Find':
        """`Be.With` matches `class` `ast.With`.

        This `class` is associated with Python keywords `with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.With], ast.AST]:
            return (isinstance(node, ast.With), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def withitem(self) -> 'Find':
        """`Be.withitem`, with item, matches `class` `ast.withitem`.

        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.withitem], ast.AST]:
            return (isinstance(node, ast.withitem), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def Yield(self) -> 'Find':
        """`Be.Yield`, Yield an element, matches `class` `ast.Yield`.

        This `class` is associated with Python keywords `yield`.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.Yield], ast.AST]:
            return (isinstance(node, ast.Yield), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)

    def YieldFrom(self) -> 'Find':
        """`Be.YieldFrom`, Yield an element From, matches `class` `ast.YieldFrom`.

        This `class` is associated with Python keywords `yield from`.
        It is a subclass of `ast.expr`.
        """

        def workhorse(node: ast.AST) -> tuple[TypeIs[ast.YieldFrom], ast.AST]:
            return (isinstance(node, ast.YieldFrom), node)
        dontMutateMyQueue = [*self.queueOfGotten_attr, workhorse]
        return Find(dontMutateMyQueue)