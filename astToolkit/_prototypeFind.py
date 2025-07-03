from collections import deque
from collections.abc import Callable
from typing import Any
from typing_extensions import TypeIs
import ast

class Find:

    def __init__(self, queueOfTruth: list[Callable[[Any], tuple[bool, Any]]] | None=None, queueOfFind_attr: deque[str] | None=None) -> None:
        self.queueOfTruth = queueOfTruth or []
        self.queueOfFind_attr = queueOfFind_attr or deque()

    def __getattribute__(self, attr: str) -> Any:
        if object.__getattribute__(self, attr):
            if self.queueOfFind_attr:
                pass
            self.queueOfFind_attr.append(attr)
            return self

        def attribute_checker(attrCurrent: Any) -> tuple[bool, Any]:
            hasAttributeCheck = hasattr(attrCurrent, attr)
            if hasAttributeCheck:
                return (hasAttributeCheck, getattr(attrCurrent, attr))
            return (hasAttributeCheck, attrCurrent)
        Z0Z_ImaQueue = object.__getattribute__(self, 'queueOfTruth')
        dontMutateMyQueue: list[Callable[[Any], tuple[bool, Any]]] = [*Z0Z_ImaQueue, attribute_checker]
        return Find(dontMutateMyQueue)

    def __call__(self, node: ast.AST) -> bool:
        attrCurrent: Any = node
        for trueFalseCallable in self.queueOfTruth:
            Ima_bool, attrNext = trueFalseCallable(attrCurrent)
            if not Ima_bool:
                return False
            attrCurrent = attrNext
        return True
    'A comprehensive suite of functions for AST class identification and type narrowing.\n\n    `class` `Be` has a method for each `ast.AST` subclass, also called "node type", to perform type\n    checking while enabling compile-time type narrowing through `TypeIs` annotations. This tool\n    forms the foundation of type-safe AST analysis and transformation throughout astToolkit.\n\n    Each method takes an `ast.AST` node and returns a `TypeIs` that confirms both runtime type\n    safety and enables static type checkers to narrow the node type in conditional contexts. This\n    eliminates the need for unsafe casting while providing comprehensive coverage of Python\'s AST\n    node hierarchy.\n\n    Methods correspond directly to Python AST node types, following the naming convention of the AST\n    classes themselves. Coverage includes expression nodes (`Add`, `Call`, `Name`), statement nodes\n    (`Assign`, `FunctionDef`, `Return`), operator nodes (`And`, `Or`, `Not`), and structural nodes\n    (`Module`, `arguments`, `keyword`).\n\n    The `class` is the primary type-checker in the antecedent-action pattern, where predicates\n    identify target nodes and actions, uh... act on nodes and their attributes. Type guards from\n    this class are commonly used as building blocks in `IfThis` predicates and directly as\n    `findThis` parameters in visitor classes.\n\n    Parameters\n    ----------\n    node: ast.AST\n        AST node to test for specific type membership\n\n    Returns\n    -------\n    typeIs: TypeIs\n        `TypeIs` enabling both runtime validation and static type narrowing\n\n    Examples\n    --------\n    Type-safe node processing with automatic type narrowing:\n\n    ```python\n        if Be.FunctionDef(node):\n            functionName = node.name  # Type-safe access to name attribute parameterCount =\n            len(node.args.args)\n    ```\n\n    Using type guards in visitor patterns:\n\n    ```python\n        NodeTourist(Be.Return, Then.extractIt(DOT.value)).visit(functionNode)\n    ```\n\n    Type-safe access to attributes of specific node types:\n\n    ```python\n        if Be.Call(node) and Be.Name(node.func):\n            callableName = node.func.id  # Type-safe access to function name\n    ```\n\n    '

    @classmethod
    def Add(cls, node: ast.AST) -> TypeIs[ast.Add]:
        """`Be.Add` matches `class` `ast.Add`.

        This `class` is associated with Python delimiters '+=' and Python operators '+'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Add)

    @classmethod
    def alias(cls, node: ast.AST) -> TypeIs[ast.alias]:
        """`Be.alias` matches `class` `ast.alias`.

        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.alias)

    @classmethod
    def And(cls, node: ast.AST) -> TypeIs[ast.And]:
        """`Be.And` matches `class` `ast.And`.

        This `class` is associated with Python keywords `and`.
        It is a subclass of `ast.boolop`.
        """
        return isinstance(node, ast.And)

    @classmethod
    def AnnAssign(cls, node: ast.AST) -> TypeIs[ast.AnnAssign]:
        """`Be.AnnAssign`, ***Ann***otated ***Assign***ment, matches `class` `ast.AnnAssign`.

        This `class` is associated with Python delimiters ':, ='.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.AnnAssign)

    @classmethod
    def arg(cls, node: ast.AST) -> TypeIs[ast.arg]:
        """`Be.arg`, ***arg***ument, matches `class` `ast.arg`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.arg)

    @classmethod
    def arguments(cls, node: ast.AST) -> TypeIs[ast.arguments]:
        """`Be.arguments` matches `class` `ast.arguments`.

        This `class` is associated with Python delimiters ','.
        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.arguments)

    @classmethod
    def Assert(cls, node: ast.AST) -> TypeIs[ast.Assert]:
        """`Be.Assert` matches `class` `ast.Assert`.

        This `class` is associated with Python keywords `assert`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Assert)

    @classmethod
    def Assign(cls, node: ast.AST) -> TypeIs[ast.Assign]:
        """`Be.Assign` matches `class` `ast.Assign`.

        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Assign)

    @classmethod
    def AST(cls, node: ast.AST) -> TypeIs[ast.AST]:
        """`Be.AST`, Abstract Syntax Tree, matches any of `class` `ast.withitem` | `ast.expr_context` | `ast.cmpop` | `ast.Exec` | `ast.alias` | `ast.stmt` | `ast.match_case` | `ast.arg` | `ast.unaryop` | `ast.arguments` | `ast._NoParent` | `ast.keyword` | `ast.expr` | `ast.mod` | `ast.pattern` | `ast.type_param` | `ast.type_ignore` | `ast.operator` | `ast.comprehension` | `ast.NodeList` | `ast.excepthandler` | `ast.boolop` | `ast.slice` | `ast.AST`.

        It is a subclass of `ast.object`.
        """
        return isinstance(node, ast.AST)

    @classmethod
    def AsyncFor(cls, node: ast.AST) -> TypeIs[ast.AsyncFor]:
        """`Be.AsyncFor`, ***Async***hronous For loop, matches `class` `ast.AsyncFor`.

        This `class` is associated with Python keywords `async for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.AsyncFor)

    @classmethod
    def AsyncFunctionDef(cls, node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
        """`Be.AsyncFunctionDef`, ***Async***hronous Function ***Def***inition, matches `class` `ast.AsyncFunctionDef`.

        This `class` is associated with Python keywords `async def` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.AsyncFunctionDef)

    @classmethod
    def AsyncWith(cls, node: ast.AST) -> TypeIs[ast.AsyncWith]:
        """`Be.AsyncWith`, ***Async***hronous With statement, matches `class` `ast.AsyncWith`.

        This `class` is associated with Python keywords `async with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.AsyncWith)

    @classmethod
    def Attribute(cls, node: ast.AST) -> TypeIs[ast.Attribute]:
        """`Be.Attribute` matches `class` `ast.Attribute`.

        This `class` is associated with Python delimiters '.'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Attribute)

    @classmethod
    def AugAssign(cls, node: ast.AST) -> TypeIs[ast.AugAssign]:
        """`Be.AugAssign`, ***Aug***mented ***Assign***ment, matches `class` `ast.AugAssign`.

        This `class` is associated with Python delimiters '+=, -=, *=, /=, //=, %=, **=, |=, &=, ^=, <<=, >>='.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.AugAssign)

    @classmethod
    def Await(cls, node: ast.AST) -> TypeIs[ast.Await]:
        """`Be.Await`, ***Await*** the asynchronous operation, matches `class` `ast.Await`.

        This `class` is associated with Python keywords `await`.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Await)

    @classmethod
    def BinOp(cls, node: ast.AST) -> TypeIs[ast.BinOp]:
        """`Be.BinOp`, ***Bin***ary ***Op***eration, matches `class` `ast.BinOp`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.BinOp)

    @classmethod
    def BitAnd(cls, node: ast.AST) -> TypeIs[ast.BitAnd]:
        """`Be.BitAnd`, ***Bit***wise And, matches `class` `ast.BitAnd`.

        This `class` is associated with Python operators '&'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitAnd)

    @classmethod
    def BitOr(cls, node: ast.AST) -> TypeIs[ast.BitOr]:
        """`Be.BitOr`, ***Bit***wise Or, matches `class` `ast.BitOr`.

        This `class` is associated with Python operators '|'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitOr)

    @classmethod
    def BitXor(cls, node: ast.AST) -> TypeIs[ast.BitXor]:
        """`Be.BitXor`, ***Bit***wise e***X***clusive Or, matches `class` `ast.BitXor`.

        This `class` is associated with Python operators '^'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitXor)

    @classmethod
    def BoolOp(cls, node: ast.AST) -> TypeIs[ast.BoolOp]:
        """`Be.BoolOp`, ***Bool***ean ***Op***eration, matches `class` `ast.BoolOp`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.BoolOp)

    @classmethod
    def boolop(cls, node: ast.AST) -> TypeIs[ast.boolop]:
        """`Be.boolop`, ***bool***ean ***op***erator, matches any of `class` `ast.Or` | `ast.And` | `ast.boolop`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.boolop)

    @classmethod
    def Break(cls, node: ast.AST) -> TypeIs[ast.Break]:
        """`Be.Break` matches `class` `ast.Break`.

        This `class` is associated with Python keywords `break`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Break)

    @classmethod
    def Call(cls, node: ast.AST) -> TypeIs[ast.Call]:
        """`Be.Call` matches `class` `ast.Call`.

        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Call)

    @classmethod
    def ClassDef(cls, node: ast.AST) -> TypeIs[ast.ClassDef]:
        """`Be.ClassDef`, ***Class*** ***Def***inition, matches `class` `ast.ClassDef`.

        This `class` is associated with Python keywords `class` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.ClassDef)

    @classmethod
    def cmpop(cls, node: ast.AST) -> TypeIs[ast.cmpop]:
        """`Be.cmpop`, ***c***o***mp***arison ***op***erator, matches any of `class` `ast.NotEq` | `ast.In` | `ast.cmpop` | `ast.Lt` | `ast.GtE` | `ast.Gt` | `ast.IsNot` | `ast.Is` | `ast.Eq` | `ast.LtE` | `ast.NotIn`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.cmpop)

    @classmethod
    def Compare(cls, node: ast.AST) -> TypeIs[ast.Compare]:
        """`Be.Compare` matches `class` `ast.Compare`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Compare)

    @classmethod
    def comprehension(cls, node: ast.AST) -> TypeIs[ast.comprehension]:
        """`Be.comprehension` matches `class` `ast.comprehension`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.comprehension)

    @classmethod
    def Constant(cls, node: ast.AST) -> TypeIs[ast.Constant]:
        """`Be.Constant` matches any of `class` `ast.Str` | `ast.Num` | `ast.Ellipsis` | `ast.Bytes` | `ast.Constant` | `ast.NameConstant`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Constant)

    @classmethod
    def Continue(cls, node: ast.AST) -> TypeIs[ast.Continue]:
        """`Be.Continue` matches `class` `ast.Continue`.

        This `class` is associated with Python keywords `continue`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Continue)

    @classmethod
    def Del(cls, node: ast.AST) -> TypeIs[ast.Del]:
        """`Be.Del`, ***Del***ete, matches `class` `ast.Del`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Del)

    @classmethod
    def Delete(cls, node: ast.AST) -> TypeIs[ast.Delete]:
        """`Be.Delete` matches `class` `ast.Delete`.

        This `class` is associated with Python keywords `del`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Delete)

    @classmethod
    def Dict(cls, node: ast.AST) -> TypeIs[ast.Dict]:
        """`Be.Dict`, ***Dict***ionary, matches `class` `ast.Dict`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Dict)

    @classmethod
    def DictComp(cls, node: ast.AST) -> TypeIs[ast.DictComp]:
        """`Be.DictComp`, ***Dict***ionary ***c***o***mp***rehension, matches `class` `ast.DictComp`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.DictComp)

    @classmethod
    def Div(cls, node: ast.AST) -> TypeIs[ast.Div]:
        """`Be.Div`, ***Div***ision, matches `class` `ast.Div`.

        This `class` is associated with Python delimiters '/=' and Python operators '/'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Div)

    @classmethod
    def Eq(cls, node: ast.AST) -> TypeIs[ast.Eq]:
        """`Be.Eq`, is ***Eq***ual to, matches `class` `ast.Eq`.

        This `class` is associated with Python operators '=='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Eq)

    @classmethod
    def ExceptHandler(cls, node: ast.AST) -> TypeIs[ast.ExceptHandler]:
        """`Be.ExceptHandler`, ***Except***ion ***Handler***, matches `class` `ast.ExceptHandler`.

        This `class` is associated with Python keywords `except`.
        It is a subclass of `ast.excepthandler`.
        """
        return isinstance(node, ast.ExceptHandler)

    @classmethod
    def excepthandler(cls, node: ast.AST) -> TypeIs[ast.excepthandler]:
        """`Be.excepthandler`, ***except***ion ***handler***, matches any of `class` `ast.excepthandler` | `ast.ExceptHandler`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.excepthandler)

    @classmethod
    def expr(cls, node: ast.AST) -> TypeIs[ast.expr]:
        """`Be.expr`, ***expr***ession, matches any of `class` `ast.List` | `ast.SetComp` | `ast.Constant` | `ast.UnaryOp` | `ast.DictComp` | `ast.Dict` | `ast.Slice` | `ast.Await` | `ast.ListComp` | `ast.NamedExpr` | `ast.Tuple` | `ast.Attribute` | `ast.Starred` | `ast.Subscript` | `ast.BinOp` | `ast.expr` | `ast.FormattedValue` | `ast.GeneratorExp` | `ast.JoinedStr` | `ast.Name` | `ast.BoolOp` | `ast.IfExp` | `ast.Call` | `ast.YieldFrom` | `ast.Compare` | `ast.Lambda` | `ast.Set` | `ast.Yield`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.expr)

    @classmethod
    def Expr(cls, node: ast.AST) -> TypeIs[ast.Expr]:
        """`Be.Expr`, ***Expr***ession, matches `class` `ast.Expr`.

        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Expr)

    @classmethod
    def expr_context(cls, node: ast.AST) -> TypeIs[ast.expr_context]:
        """`Be.expr_context`, ***expr***ession ***context***, matches any of `class` `ast.expr_context` | `ast.AugLoad` | `ast.Load` | `ast.Store` | `ast.AugStore` | `ast.Param` | `ast.Del`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.expr_context)

    @classmethod
    def Expression(cls, node: ast.AST) -> TypeIs[ast.Expression]:
        """`Be.Expression` matches `class` `ast.Expression`.

        It is a subclass of `ast.mod`.
        """
        return isinstance(node, ast.Expression)

    @classmethod
    def FloorDiv(cls, node: ast.AST) -> TypeIs[ast.FloorDiv]:
        """`Be.FloorDiv`, Floor ***Div***ision, matches `class` `ast.FloorDiv`.

        This `class` is associated with Python delimiters '//=' and Python operators '//'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.FloorDiv)

    @classmethod
    def For(cls, node: ast.AST) -> TypeIs[ast.For]:
        """`Be.For` matches `class` `ast.For`.

        This `class` is associated with Python keywords `for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.For)

    @classmethod
    def FormattedValue(cls, node: ast.AST) -> TypeIs[ast.FormattedValue]:
        """`Be.FormattedValue` matches `class` `ast.FormattedValue`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.FormattedValue)

    @classmethod
    def FunctionDef(cls, node: ast.AST) -> TypeIs[ast.FunctionDef]:
        """`Be.FunctionDef`, Function ***Def***inition, matches `class` `ast.FunctionDef`.

        This `class` is associated with Python keywords `def` and Python delimiters '()'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.FunctionDef)

    @classmethod
    def FunctionType(cls, node: ast.AST) -> TypeIs[ast.FunctionType]:
        """`Be.FunctionType`, Function Type, matches `class` `ast.FunctionType`.

        It is a subclass of `ast.mod`.
        """
        return isinstance(node, ast.FunctionType)

    @classmethod
    def GeneratorExp(cls, node: ast.AST) -> TypeIs[ast.GeneratorExp]:
        """`Be.GeneratorExp`, Generator ***Exp***ression, matches `class` `ast.GeneratorExp`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.GeneratorExp)

    @classmethod
    def Global(cls, node: ast.AST) -> TypeIs[ast.Global]:
        """`Be.Global` matches `class` `ast.Global`.

        This `class` is associated with Python keywords `global`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Global)

    @classmethod
    def Gt(cls, node: ast.AST) -> TypeIs[ast.Gt]:
        """`Be.Gt`, is Greater than, matches `class` `ast.Gt`.

        This `class` is associated with Python operators '>'.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Gt)

    @classmethod
    def GtE(cls, node: ast.AST) -> TypeIs[ast.GtE]:
        """`Be.GtE`, is Greater than or Equal to, matches `class` `ast.GtE`.

        This `class` is associated with Python operators '>='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.GtE)

    @classmethod
    def If(cls, node: ast.AST) -> TypeIs[ast.If]:
        """`Be.If` matches `class` `ast.If`.

        This `class` is associated with Python keywords `if` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.If)

    @classmethod
    def IfExp(cls, node: ast.AST) -> TypeIs[ast.IfExp]:
        """`Be.IfExp`, If ***Exp***ression, matches `class` `ast.IfExp`.

        This `class` is associated with Python keywords `if`.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.IfExp)

    @classmethod
    def Import(cls, node: ast.AST) -> TypeIs[ast.Import]:
        """`Be.Import` matches `class` `ast.Import`.

        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Import)

    @classmethod
    def ImportFrom(cls, node: ast.AST) -> TypeIs[ast.ImportFrom]:
        """`Be.ImportFrom` matches `class` `ast.ImportFrom`.

        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.ImportFrom)

    @classmethod
    def In(cls, node: ast.AST) -> TypeIs[ast.In]:
        """`Be.In` matches `class` `ast.In`.

        This `class` is associated with Python keywords `in`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.In)

    @classmethod
    def Interactive(cls, node: ast.AST) -> TypeIs[ast.Interactive]:
        """`Be.Interactive`, Interactive mode, matches `class` `ast.Interactive`.

        It is a subclass of `ast.mod`.
        """
        return isinstance(node, ast.Interactive)

    @classmethod
    def Invert(cls, node: ast.AST) -> TypeIs[ast.Invert]:
        """`Be.Invert` matches `class` `ast.Invert`.

        This `class` is associated with Python operators '~'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.Invert)

    @classmethod
    def Is(cls, node: ast.AST) -> TypeIs[ast.Is]:
        """`Be.Is` matches `class` `ast.Is`.

        This `class` is associated with Python keywords `is`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Is)

    @classmethod
    def IsNot(cls, node: ast.AST) -> TypeIs[ast.IsNot]:
        """`Be.IsNot` matches `class` `ast.IsNot`.

        This `class` is associated with Python keywords `is not`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.IsNot)

    @classmethod
    def JoinedStr(cls, node: ast.AST) -> TypeIs[ast.JoinedStr]:
        """`Be.JoinedStr`, Joined ***Str***ing, matches `class` `ast.JoinedStr`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.JoinedStr)

    @classmethod
    def keyword(cls, node: ast.AST) -> TypeIs[ast.keyword]:
        """`Be.keyword` matches `class` `ast.keyword`.

        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.keyword)

    @classmethod
    def Lambda(cls, node: ast.AST) -> TypeIs[ast.Lambda]:
        """`Be.Lambda`, Lambda function, matches `class` `ast.Lambda`.

        This `class` is associated with Python keywords `lambda` and Python delimiters ':'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Lambda)

    @classmethod
    def List(cls, node: ast.AST) -> TypeIs[ast.List]:
        """`Be.List` matches `class` `ast.List`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.List)

    @classmethod
    def ListComp(cls, node: ast.AST) -> TypeIs[ast.ListComp]:
        """`Be.ListComp`, List ***c***o***mp***rehension, matches `class` `ast.ListComp`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.ListComp)

    @classmethod
    def Load(cls, node: ast.AST) -> TypeIs[ast.Load]:
        """`Be.Load` matches `class` `ast.Load`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Load)

    @classmethod
    def LShift(cls, node: ast.AST) -> TypeIs[ast.LShift]:
        """`Be.LShift`, Left Shift, matches `class` `ast.LShift`.

        This `class` is associated with Python delimiters '<<=' and Python operators '<<'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.LShift)

    @classmethod
    def Lt(cls, node: ast.AST) -> TypeIs[ast.Lt]:
        """`Be.Lt`, is Less than, matches `class` `ast.Lt`.

        This `class` is associated with Python operators '<'.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Lt)

    @classmethod
    def LtE(cls, node: ast.AST) -> TypeIs[ast.LtE]:
        """`Be.LtE`, is Less than or Equal to, matches `class` `ast.LtE`.

        This `class` is associated with Python operators '<='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.LtE)

    @classmethod
    def Match(cls, node: ast.AST) -> TypeIs[ast.Match]:
        """`Be.Match`, Match this, matches `class` `ast.Match`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Match)

    @classmethod
    def match_case(cls, node: ast.AST) -> TypeIs[ast.match_case]:
        """`Be.match_case`, match case, matches `class` `ast.match_case`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.match_case)

    @classmethod
    def MatchAs(cls, node: ast.AST) -> TypeIs[ast.MatchAs]:
        """`Be.MatchAs`, Match As, matches `class` `ast.MatchAs`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchAs)

    @classmethod
    def MatchClass(cls, node: ast.AST) -> TypeIs[ast.MatchClass]:
        """`Be.MatchClass`, Match Class, matches `class` `ast.MatchClass`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchClass)

    @classmethod
    def MatchMapping(cls, node: ast.AST) -> TypeIs[ast.MatchMapping]:
        """`Be.MatchMapping`, Match Mapping, matches `class` `ast.MatchMapping`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchMapping)

    @classmethod
    def MatchOr(cls, node: ast.AST) -> TypeIs[ast.MatchOr]:
        """`Be.MatchOr`, Match this Or that, matches `class` `ast.MatchOr`.

        This `class` is associated with Python delimiters ':' and Python operators '|'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchOr)

    @classmethod
    def MatchSequence(cls, node: ast.AST) -> TypeIs[ast.MatchSequence]:
        """`Be.MatchSequence`, Match this Sequence, matches `class` `ast.MatchSequence`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchSequence)

    @classmethod
    def MatchSingleton(cls, node: ast.AST) -> TypeIs[ast.MatchSingleton]:
        """`Be.MatchSingleton`, Match Singleton, matches `class` `ast.MatchSingleton`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchSingleton)

    @classmethod
    def MatchStar(cls, node: ast.AST) -> TypeIs[ast.MatchStar]:
        """`Be.MatchStar`, Match Star, matches `class` `ast.MatchStar`.

        This `class` is associated with Python delimiters ':' and Python operators '*'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchStar)

    @classmethod
    def MatchValue(cls, node: ast.AST) -> TypeIs[ast.MatchValue]:
        """`Be.MatchValue`, Match Value, matches `class` `ast.MatchValue`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`.
        """
        return isinstance(node, ast.MatchValue)

    @classmethod
    def MatMult(cls, node: ast.AST) -> TypeIs[ast.MatMult]:
        """`Be.MatMult`, ***Mat***rix ***Mult***iplication, matches `class` `ast.MatMult`.

        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.MatMult)

    @classmethod
    def mod(cls, node: ast.AST) -> TypeIs[ast.mod]:
        """`Be.mod`, ***mod***ule, matches any of `class` `ast.FunctionType` | `ast.mod` | `ast.Expression` | `ast.Interactive` | `ast.Suite` | `ast.Module`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.mod)

    @classmethod
    def Mod(cls, node: ast.AST) -> TypeIs[ast.Mod]:
        """`Be.Mod`, ***Mod***ulo, matches `class` `ast.Mod`.

        This `class` is associated with Python delimiters '%=' and Python operators '%'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Mod)

    @classmethod
    def Module(cls, node: ast.AST) -> TypeIs[ast.Module]:
        """`Be.Module` matches `class` `ast.Module`.

        It is a subclass of `ast.mod`.
        """
        return isinstance(node, ast.Module)

    @classmethod
    def Mult(cls, node: ast.AST) -> TypeIs[ast.Mult]:
        """`Be.Mult`, ***Mult***iplication, matches `class` `ast.Mult`.

        This `class` is associated with Python delimiters '*=' and Python operators '*'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Mult)

    @classmethod
    def Name(cls, node: ast.AST) -> TypeIs[ast.Name]:
        """`Be.Name` matches `class` `ast.Name`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Name)

    @classmethod
    def NamedExpr(cls, node: ast.AST) -> TypeIs[ast.NamedExpr]:
        """`Be.NamedExpr`, Named ***Expr***ession, matches `class` `ast.NamedExpr`.

        This `class` is associated with Python operators ':='.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.NamedExpr)

    @classmethod
    def Nonlocal(cls, node: ast.AST) -> TypeIs[ast.Nonlocal]:
        """`Be.Nonlocal` matches `class` `ast.Nonlocal`.

        This `class` is associated with Python keywords `nonlocal`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Nonlocal)

    @classmethod
    def Not(cls, node: ast.AST) -> TypeIs[ast.Not]:
        """`Be.Not` matches `class` `ast.Not`.

        This `class` is associated with Python keywords `not`.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.Not)

    @classmethod
    def NotEq(cls, node: ast.AST) -> TypeIs[ast.NotEq]:
        """`Be.NotEq`, is Not ***Eq***ual to, matches `class` `ast.NotEq`.

        This `class` is associated with Python operators '!='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.NotEq)

    @classmethod
    def NotIn(cls, node: ast.AST) -> TypeIs[ast.NotIn]:
        """`Be.NotIn`, is Not ***In***cluded in or does Not have membership In, matches `class` `ast.NotIn`.

        This `class` is associated with Python keywords `not in`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.NotIn)

    @classmethod
    def operator(cls, node: ast.AST) -> TypeIs[ast.operator]:
        """`Be.operator` matches any of `class` `ast.Div` | `ast.FloorDiv` | `ast.Mult` | `ast.operator` | `ast.RShift` | `ast.Pow` | `ast.BitAnd` | `ast.Sub` | `ast.MatMult` | `ast.BitXor` | `ast.Mod` | `ast.BitOr` | `ast.LShift` | `ast.Add`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.operator)

    @classmethod
    def Or(cls, node: ast.AST) -> TypeIs[ast.Or]:
        """`Be.Or` matches `class` `ast.Or`.

        This `class` is associated with Python keywords `or`.
        It is a subclass of `ast.boolop`.
        """
        return isinstance(node, ast.Or)

    @classmethod
    def ParamSpec(cls, node: ast.AST) -> TypeIs[ast.ParamSpec]:
        """`Be.ParamSpec`, ***Param***eter ***Spec***ification, matches `class` `ast.ParamSpec`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.type_param`.
        """
        return isinstance(node, ast.ParamSpec)

    @classmethod
    def Pass(cls, node: ast.AST) -> TypeIs[ast.Pass]:
        """`Be.Pass` matches `class` `ast.Pass`.

        This `class` is associated with Python keywords `pass`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Pass)

    @classmethod
    def pattern(cls, node: ast.AST) -> TypeIs[ast.pattern]:
        """`Be.pattern` matches any of `class` `ast.MatchAs` | `ast.MatchSequence` | `ast.MatchStar` | `ast.MatchValue` | `ast.pattern` | `ast.MatchSingleton` | `ast.MatchClass` | `ast.MatchOr` | `ast.MatchMapping`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.pattern)

    @classmethod
    def Pow(cls, node: ast.AST) -> TypeIs[ast.Pow]:
        """`Be.Pow`, ***Pow***er, matches `class` `ast.Pow`.

        This `class` is associated with Python delimiters '**=' and Python operators '**'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Pow)

    @classmethod
    def Raise(cls, node: ast.AST) -> TypeIs[ast.Raise]:
        """`Be.Raise` matches `class` `ast.Raise`.

        This `class` is associated with Python keywords `raise`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Raise)

    @classmethod
    def Return(cls, node: ast.AST) -> TypeIs[ast.Return]:
        """`Be.Return` matches `class` `ast.Return`.

        This `class` is associated with Python keywords `return`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Return)

    @classmethod
    def RShift(cls, node: ast.AST) -> TypeIs[ast.RShift]:
        """`Be.RShift`, Right Shift, matches `class` `ast.RShift`.

        This `class` is associated with Python delimiters '>>=' and Python operators '>>'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.RShift)

    @classmethod
    def Set(cls, node: ast.AST) -> TypeIs[ast.Set]:
        """`Be.Set` matches `class` `ast.Set`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Set)

    @classmethod
    def SetComp(cls, node: ast.AST) -> TypeIs[ast.SetComp]:
        """`Be.SetComp`, Set ***c***o***mp***rehension, matches `class` `ast.SetComp`.

        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.SetComp)

    @classmethod
    def Slice(cls, node: ast.AST) -> TypeIs[ast.Slice]:
        """`Be.Slice` matches `class` `ast.Slice`.

        This `class` is associated with Python delimiters '[], :'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Slice)

    @classmethod
    def Starred(cls, node: ast.AST) -> TypeIs[ast.Starred]:
        """`Be.Starred` matches `class` `ast.Starred`.

        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Starred)

    @classmethod
    def stmt(cls, node: ast.AST) -> TypeIs[ast.stmt]:
        """`Be.stmt`, ***st***ate***m***en***t***, matches any of `class` `ast.Return` | `ast.AsyncFor` | `ast.Assign` | `ast.AsyncWith` | `ast.Match` | `ast.stmt` | `ast.Try` | `ast.Import` | `ast.Pass` | `ast.Break` | `ast.With` | `ast.AnnAssign` | `ast.ImportFrom` | `ast.Raise` | `ast.FunctionDef` | `ast.AugAssign` | `ast.Assert` | `ast.While` | `ast.Continue` | `ast.If` | `ast.Delete` | `ast.TryStar` | `ast.AsyncFunctionDef` | `ast.For` | `ast.Expr` | `ast.ClassDef` | `ast.Nonlocal` | `ast.Global` | `ast.TypeAlias`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.stmt)

    @classmethod
    def Store(cls, node: ast.AST) -> TypeIs[ast.Store]:
        """`Be.Store` matches `class` `ast.Store`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Store)

    @classmethod
    def Sub(cls, node: ast.AST) -> TypeIs[ast.Sub]:
        """`Be.Sub`, ***Sub***traction, matches `class` `ast.Sub`.

        This `class` is associated with Python delimiters '-=' and Python operators '-'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Sub)

    @classmethod
    def Subscript(cls, node: ast.AST) -> TypeIs[ast.Subscript]:
        """`Be.Subscript` matches `class` `ast.Subscript`.

        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Subscript)

    @classmethod
    def Try(cls, node: ast.AST) -> TypeIs[ast.Try]:
        """`Be.Try` matches `class` `ast.Try`.

        This `class` is associated with Python keywords `try`, `except` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Try)

    @classmethod
    def TryStar(cls, node: ast.AST) -> TypeIs[ast.TryStar]:
        """`Be.TryStar`, Try executing this, protected by `except*` ("except star"), matches `class` `ast.TryStar`.

        This `class` is associated with Python keywords `try`, `except*` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.TryStar)

    @classmethod
    def Tuple(cls, node: ast.AST) -> TypeIs[ast.Tuple]:
        """`Be.Tuple` matches `class` `ast.Tuple`.

        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Tuple)

    @classmethod
    def type_ignore(cls, node: ast.AST) -> TypeIs[ast.type_ignore]:
        """`Be.type_ignore`, this `type` error, you ignore it, matches any of `class` `ast.TypeIgnore` | `ast.type_ignore`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.type_ignore)

    @classmethod
    def type_param(cls, node: ast.AST) -> TypeIs[ast.type_param]:
        """`Be.type_param`, type ***param***eter, matches any of `class` `ast.TypeVarTuple` | `ast.TypeVar` | `ast.type_param` | `ast.ParamSpec`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.type_param)

    @classmethod
    def TypeAlias(cls, node: ast.AST) -> TypeIs[ast.TypeAlias]:
        """`Be.TypeAlias`, Type Alias, matches `class` `ast.TypeAlias`.

        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.TypeAlias)

    @classmethod
    def TypeIgnore(cls, node: ast.AST) -> TypeIs[ast.TypeIgnore]:
        """`Be.TypeIgnore`, this Type (`type`) error, Ignore it, matches `class` `ast.TypeIgnore`.

        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.type_ignore`.
        """
        return isinstance(node, ast.TypeIgnore)

    @classmethod
    def TypeVar(cls, node: ast.AST) -> TypeIs[ast.TypeVar]:
        """`Be.TypeVar`, Type ***Var***iable, matches `class` `ast.TypeVar`.

        It is a subclass of `ast.type_param`.
        """
        return isinstance(node, ast.TypeVar)

    @classmethod
    def TypeVarTuple(cls, node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
        """`Be.TypeVarTuple`, Type ***Var***iable ***Tuple***, matches `class` `ast.TypeVarTuple`.

        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.type_param`.
        """
        return isinstance(node, ast.TypeVarTuple)

    @classmethod
    def UAdd(cls, node: ast.AST) -> TypeIs[ast.UAdd]:
        """`Be.UAdd`, ***U***nary ***Add***ition, matches `class` `ast.UAdd`.

        This `class` is associated with Python operators '+'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.UAdd)

    @classmethod
    def UnaryOp(cls, node: ast.AST) -> TypeIs[ast.UnaryOp]:
        """`Be.UnaryOp`, ***Un***ary ***Op***eration, matches `class` `ast.UnaryOp`.

        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.UnaryOp)

    @classmethod
    def unaryop(cls, node: ast.AST) -> TypeIs[ast.unaryop]:
        """`Be.unaryop`, ***un***ary ***op***erator, matches any of `class` `ast.unaryop` | `ast.UAdd` | `ast.USub` | `ast.Invert` | `ast.Not`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.unaryop)

    @classmethod
    def USub(cls, node: ast.AST) -> TypeIs[ast.USub]:
        """`Be.USub`, ***U***nary ***Sub***traction, matches `class` `ast.USub`.

        This `class` is associated with Python operators '-'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.USub)

    @classmethod
    def While(cls, node: ast.AST) -> TypeIs[ast.While]:
        """`Be.While` matches `class` `ast.While`.

        This `class` is associated with Python keywords `while`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.While)

    @classmethod
    def With(cls, node: ast.AST) -> TypeIs[ast.With]:
        """`Be.With` matches `class` `ast.With`.

        This `class` is associated with Python keywords `with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.With)

    @classmethod
    def withitem(cls, node: ast.AST) -> TypeIs[ast.withitem]:
        """`Be.withitem`, with item, matches `class` `ast.withitem`.

        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.withitem)

    @classmethod
    def Yield(cls, node: ast.AST) -> TypeIs[ast.Yield]:
        """`Be.Yield`, Yield an element, matches `class` `ast.Yield`.

        This `class` is associated with Python keywords `yield`.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.Yield)

    @classmethod
    def YieldFrom(cls, node: ast.AST) -> TypeIs[ast.YieldFrom]:
        """`Be.YieldFrom`, Yield an element From, matches `class` `ast.YieldFrom`.

        This `class` is associated with Python keywords `yield from`.
        It is a subclass of `ast.expr`.
        """
        return isinstance(node, ast.YieldFrom)