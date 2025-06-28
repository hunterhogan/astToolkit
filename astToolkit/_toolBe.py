"""Automatically generated file, so changes may be overwritten."""
from astToolkit import ConstantValueType
from collections.abc import Callable, Sequence
from typing_extensions import TypeIs
import ast

class Be:
    """A comprehensive suite of functions for AST class identification and type narrowing.

    `class` `Be` has a method for each `ast.AST` subclass, also called "node type", to perform type
    checking while enabling compile-time type narrowing through `TypeIs` annotations. This tool
    forms the foundation of type-safe AST analysis and transformation throughout astToolkit.

    Each method takes an `ast.AST` node and returns a `TypeIs` that confirms both runtime type
    safety and enables static type checkers to narrow the node type in conditional contexts. This
    eliminates the need for unsafe casting while providing comprehensive coverage of Python's AST
    node hierarchy.

    Methods correspond directly to Python AST node types, following the naming convention of the AST
    classes themselves. Coverage includes expression nodes (`Add`, `Call`, `Name`), statement nodes
    (`Assign`, `FunctionDef`, `Return`), operator nodes (`And`, `Or`, `Not`), and structural nodes
    (`Module`, `arguments`, `keyword`).

    The `class` is the primary type-checker in the antecedent-action pattern, where predicates
    identify target nodes and actions, uh... act on nodes and their attributes. Type guards from
    this class are commonly used as building blocks in `IfThis` predicates and directly as
    `findThis` parameters in visitor classes.

    Parameters
    ----------
    node: ast.AST
        AST node to test for specific type membership

    Returns
    -------
    typeIs: TypeIs
        `TypeIs` enabling both runtime validation and static type narrowing

    Examples
    --------
    Type-safe node processing with automatic type narrowing:

    ```python
        if Be.FunctionDef(node):
            functionName = node.name  # Type-safe access to name attribute parameterCount =
            len(node.args.args)
    ```

    Using type guards in visitor patterns:

    ```python
        NodeTourist(Be.Return, Then.extractIt(DOT.value)).visit(functionNode)
    ```

    Type-safe access to attributes of specific node types:

    ```python
        if Be.Call(node) and Be.Name(node.func):
            callableName = node.func.id  # Type-safe access to function name
    ```

    """

    @staticmethod
    def Add(node: ast.AST) -> TypeIs[ast.Add]:
        """`Be.Add` matches any of `ast.Add` | `class` `ast.Add`.

        This `class` is associated with Python delimiters '+=' and Python operators '+'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Add)

    class _alias:

        def __call__(self, node: ast.AST) -> TypeIs[ast.alias]:
            return isinstance(node, ast.alias)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.alias] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.alias] | bool:
                return isinstance(node, ast.alias) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def asnameIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.alias] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.alias] | bool:
                return isinstance(node, ast.alias) and attributeCondition(node.asname)
            return workhorse
    alias = _alias()
    '`Be.alias` matches `class` `ast.alias`.\n\n        This `class` is associated with Python keywords `as`.\n        It is a subclass of `ast.AST`.\n        '

    @staticmethod
    def And(node: ast.AST) -> TypeIs[ast.And]:
        """`Be.And` matches any of `class` `ast.And` | `ast.And`.

        This `class` is associated with Python keywords `and`.
        It is a subclass of `ast.boolop`.
        """
        return isinstance(node, ast.And)

    class _AnnAssign:

        def __call__(self, node: ast.AST) -> TypeIs[ast.AnnAssign]:
            return isinstance(node, ast.AnnAssign)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.Name | ast.Attribute | ast.Subscript], bool]) -> Callable[[ast.AST], TypeIs[ast.AnnAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AnnAssign] | bool:
                return isinstance(node, ast.AnnAssign) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def annotationIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.AnnAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AnnAssign] | bool:
                return isinstance(node, ast.AnnAssign) and attributeCondition(node.annotation)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.AnnAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AnnAssign] | bool:
                return isinstance(node, ast.AnnAssign) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def simpleIs(attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[ast.AnnAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AnnAssign] | bool:
                return isinstance(node, ast.AnnAssign) and attributeCondition(node.simple)
            return workhorse
    AnnAssign = _AnnAssign()
    "`Be.AnnAssign`, ***Ann***otated ***Assign***ment, matches `class` `ast.AnnAssign`.\n\n        This `class` is associated with Python delimiters ':, ='.\n        It is a subclass of `ast.stmt`.\n        "

    class _arg:

        def __call__(self, node: ast.AST) -> TypeIs[ast.arg]:
            return isinstance(node, ast.arg)

        @staticmethod
        def argIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.arg] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arg] | bool:
                return isinstance(node, ast.arg) and attributeCondition(node.arg)
            return workhorse

        @staticmethod
        def annotationIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.arg] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arg] | bool:
                return isinstance(node, ast.arg) and attributeCondition(node.annotation)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.arg] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arg] | bool:
                return isinstance(node, ast.arg) and attributeCondition(node.type_comment)
            return workhorse
    arg = _arg()
    '`Be.arg`, ***arg***ument, matches `class` `ast.arg`.\n\n        It is a subclass of `ast.AST`.\n        '

    class _arguments:

        def __call__(self, node: ast.AST) -> TypeIs[ast.arguments]:
            return isinstance(node, ast.arguments)

        @staticmethod
        def posonlyargsIs(attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.posonlyargs)
            return workhorse

        @staticmethod
        def argsIs(attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.args)
            return workhorse

        @staticmethod
        def varargIs(attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.vararg)
            return workhorse

        @staticmethod
        def kwonlyargsIs(attributeCondition: Callable[[list[ast.arg]], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.kwonlyargs)
            return workhorse

        @staticmethod
        def kw_defaultsIs(attributeCondition: Callable[[Sequence[ast.expr | None]], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.kw_defaults)
            return workhorse

        @staticmethod
        def kwargIs(attributeCondition: Callable[[ast.arg | None], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.kwarg)
            return workhorse

        @staticmethod
        def defaultsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.arguments] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.arguments] | bool:
                return isinstance(node, ast.arguments) and attributeCondition(node.defaults)
            return workhorse
    arguments = _arguments()
    "`Be.arguments` matches `class` `ast.arguments`.\n\n        This `class` is associated with Python delimiters ','.\n        It is a subclass of `ast.AST`.\n        "

    class _Assert:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Assert]:
            return isinstance(node, ast.Assert)

        @staticmethod
        def testIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Assert] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Assert] | bool:
                return isinstance(node, ast.Assert) and attributeCondition(node.test)
            return workhorse

        @staticmethod
        def msgIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Assert] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Assert] | bool:
                return isinstance(node, ast.Assert) and attributeCondition(node.msg)
            return workhorse
    Assert = _Assert()
    '`Be.Assert` matches `class` `ast.Assert`.\n\n        This `class` is associated with Python keywords `assert`.\n        It is a subclass of `ast.stmt`.\n        '

    class _Assign:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Assign]:
            return isinstance(node, ast.Assign)

        @staticmethod
        def targetsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Assign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Assign] | bool:
                return isinstance(node, ast.Assign) and attributeCondition(node.targets)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Assign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Assign] | bool:
                return isinstance(node, ast.Assign) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Assign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Assign] | bool:
                return isinstance(node, ast.Assign) and attributeCondition(node.type_comment)
            return workhorse
    Assign = _Assign()
    "`Be.Assign` matches `class` `ast.Assign`.\n\n        This `class` is associated with Python delimiters '='.\n        It is a subclass of `ast.stmt`.\n        "

    @staticmethod
    def AST(node: ast.AST) -> TypeIs[ast.AST]:
        """`Be.AST`, Abstract Syntax Tree, matches any of `ast._NoParent` | `ast.withitem` | `ast.excepthandler` | `ast.keyword` | `ast.comprehension` | `ast.NodeList` | `ast.type_ignore` | `ast.slice` | `ast.type_param` | `ast.expr_context` | `ast.boolop` | `ast.operator` | `ast.Exec` | `ast.stmt` | `ast.arg` | `class` `ast.AST` | `ast.match_case` | `ast.alias` | `ast.unaryop` | `ast.expr` | `ast.mod` | `ast.pattern` | `ast.cmpop` | `ast.arguments`.

        It is a subclass of `ast.object`.
        """
        return isinstance(node, ast.AST)

    class _AsyncFor:

        def __call__(self, node: ast.AST) -> TypeIs[ast.AsyncFor]:
            return isinstance(node, ast.AsyncFor)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFor] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFor] | bool:
                return isinstance(node, ast.AsyncFor) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def iterIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFor] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFor] | bool:
                return isinstance(node, ast.AsyncFor) and attributeCondition(node.iter)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFor] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFor] | bool:
                return isinstance(node, ast.AsyncFor) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFor] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFor] | bool:
                return isinstance(node, ast.AsyncFor) and attributeCondition(node.orelse)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFor] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFor] | bool:
                return isinstance(node, ast.AsyncFor) and attributeCondition(node.type_comment)
            return workhorse
    AsyncFor = _AsyncFor()
    "`Be.AsyncFor`, ***Async***hronous For loop, matches `class` `ast.AsyncFor`.\n\n        This `class` is associated with Python keywords `async for` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _AsyncFunctionDef:

        def __call__(self, node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
            return isinstance(node, ast.AsyncFunctionDef)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def argsIs(attributeCondition: Callable[[ast.arguments], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.args)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def decorator_listIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.decorator_list)
            return workhorse

        @staticmethod
        def returnsIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.returns)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.type_comment)
            return workhorse

        @staticmethod
        def type_paramsIs(attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncFunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef] | bool:
                return isinstance(node, ast.AsyncFunctionDef) and attributeCondition(node.type_params)
            return workhorse
    AsyncFunctionDef = _AsyncFunctionDef()
    "`Be.AsyncFunctionDef`, ***Async***hronous Function ***Def***inition, matches `class` `ast.AsyncFunctionDef`.\n\n        This `class` is associated with Python keywords `async def` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _AsyncWith:

        def __call__(self, node: ast.AST) -> TypeIs[ast.AsyncWith]:
            return isinstance(node, ast.AsyncWith)

        @staticmethod
        def itemsIs(attributeCondition: Callable[[list[ast.withitem]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncWith] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncWith] | bool:
                return isinstance(node, ast.AsyncWith) and attributeCondition(node.items)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncWith] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncWith] | bool:
                return isinstance(node, ast.AsyncWith) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.AsyncWith] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AsyncWith] | bool:
                return isinstance(node, ast.AsyncWith) and attributeCondition(node.type_comment)
            return workhorse
    AsyncWith = _AsyncWith()
    "`Be.AsyncWith`, ***Async***hronous With statement, matches `class` `ast.AsyncWith`.\n\n        This `class` is associated with Python keywords `async with` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _Attribute:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Attribute]:
            return isinstance(node, ast.Attribute)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Attribute] | bool:
                return isinstance(node, ast.Attribute) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def attrIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Attribute] | bool:
                return isinstance(node, ast.Attribute) and attributeCondition(node.attr)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Attribute] | bool:
                return isinstance(node, ast.Attribute) and attributeCondition(node.ctx)
            return workhorse
    Attribute = _Attribute()
    "`Be.Attribute` matches `class` `ast.Attribute`.\n\n        This `class` is associated with Python delimiters '.'.\n        It is a subclass of `ast.expr`.\n        "

    class _AugAssign:

        def __call__(self, node: ast.AST) -> TypeIs[ast.AugAssign]:
            return isinstance(node, ast.AugAssign)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.Name | ast.Attribute | ast.Subscript], bool]) -> Callable[[ast.AST], TypeIs[ast.AugAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AugAssign] | bool:
                return isinstance(node, ast.AugAssign) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def opIs(attributeCondition: Callable[[ast.operator], bool]) -> Callable[[ast.AST], TypeIs[ast.AugAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AugAssign] | bool:
                return isinstance(node, ast.AugAssign) and attributeCondition(node.op)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.AugAssign] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.AugAssign] | bool:
                return isinstance(node, ast.AugAssign) and attributeCondition(node.value)
            return workhorse
    AugAssign = _AugAssign()
    "`Be.AugAssign`, ***Aug***mented ***Assign***ment, matches `class` `ast.AugAssign`.\n\n        This `class` is associated with Python delimiters '+=, -=, *=, /=, //=, %=, **=, |=, &=, ^=, <<=, >>='.\n        It is a subclass of `ast.stmt`.\n        "

    class _Await:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Await]:
            return isinstance(node, ast.Await)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Await] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Await] | bool:
                return isinstance(node, ast.Await) and attributeCondition(node.value)
            return workhorse
    Await = _Await()
    '`Be.Await`, ***Await*** the asynchronous operation, matches `class` `ast.Await`.\n\n        This `class` is associated with Python keywords `await`.\n        It is a subclass of `ast.expr`.\n        '

    class _BinOp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.BinOp]:
            return isinstance(node, ast.BinOp)

        @staticmethod
        def leftIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.BinOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.BinOp] | bool:
                return isinstance(node, ast.BinOp) and attributeCondition(node.left)
            return workhorse

        @staticmethod
        def opIs(attributeCondition: Callable[[ast.operator], bool]) -> Callable[[ast.AST], TypeIs[ast.BinOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.BinOp] | bool:
                return isinstance(node, ast.BinOp) and attributeCondition(node.op)
            return workhorse

        @staticmethod
        def rightIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.BinOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.BinOp] | bool:
                return isinstance(node, ast.BinOp) and attributeCondition(node.right)
            return workhorse
    BinOp = _BinOp()
    '`Be.BinOp`, ***Bin***ary ***Op***eration, matches `class` `ast.BinOp`.\n\n        It is a subclass of `ast.expr`.\n        '

    @staticmethod
    def BitAnd(node: ast.AST) -> TypeIs[ast.BitAnd]:
        """`Be.BitAnd`, ***Bit***wise And, matches any of `class` `ast.BitAnd` | `ast.BitAnd`.

        This `class` is associated with Python operators '&'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitAnd)

    @staticmethod
    def BitOr(node: ast.AST) -> TypeIs[ast.BitOr]:
        """`Be.BitOr`, ***Bit***wise Or, matches any of `class` `ast.BitOr` | `ast.BitOr`.

        This `class` is associated with Python operators '|'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitOr)

    @staticmethod
    def BitXor(node: ast.AST) -> TypeIs[ast.BitXor]:
        """`Be.BitXor`, ***Bit***wise e***X***clusive Or, matches any of `class` `ast.BitXor` | `ast.BitXor`.

        This `class` is associated with Python operators '^'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.BitXor)

    @staticmethod
    def boolop(node: ast.AST) -> TypeIs[ast.boolop]:
        """`Be.boolop`, ***bool***ean ***op***erator, matches any of `class` `ast.boolop` | `ast.Or` | `ast.And`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.boolop)

    class _BoolOp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.BoolOp]:
            return isinstance(node, ast.BoolOp)

        @staticmethod
        def opIs(attributeCondition: Callable[[ast.boolop], bool]) -> Callable[[ast.AST], TypeIs[ast.BoolOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.BoolOp] | bool:
                return isinstance(node, ast.BoolOp) and attributeCondition(node.op)
            return workhorse

        @staticmethod
        def valuesIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.BoolOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.BoolOp] | bool:
                return isinstance(node, ast.BoolOp) and attributeCondition(node.values)
            return workhorse
    BoolOp = _BoolOp()
    '`Be.BoolOp`, ***Bool***ean ***Op***eration, matches `class` `ast.BoolOp`.\n\n        It is a subclass of `ast.expr`.\n        '

    @staticmethod
    def Break(node: ast.AST) -> TypeIs[ast.Break]:
        """`Be.Break` matches `class` `ast.Break`.

        This `class` is associated with Python keywords `break`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Break)

    class _Call:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Call]:
            return isinstance(node, ast.Call)

        @staticmethod
        def funcIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
                return isinstance(node, ast.Call) and attributeCondition(node.func)
            return workhorse

        @staticmethod
        def argsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
                return isinstance(node, ast.Call) and attributeCondition(node.args)
            return workhorse

        @staticmethod
        def keywordsIs(attributeCondition: Callable[[list[ast.keyword]], bool]) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
                return isinstance(node, ast.Call) and attributeCondition(node.keywords)
            return workhorse
    Call = _Call()
    "`Be.Call` matches `class` `ast.Call`.\n\n        This `class` is associated with Python delimiters '()'.\n        It is a subclass of `ast.expr`.\n        "

    class _ClassDef:

        def __call__(self, node: ast.AST) -> TypeIs[ast.ClassDef]:
            return isinstance(node, ast.ClassDef)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def basesIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.bases)
            return workhorse

        @staticmethod
        def keywordsIs(attributeCondition: Callable[[list[ast.keyword]], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.keywords)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def decorator_listIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.decorator_list)
            return workhorse

        @staticmethod
        def type_paramsIs(attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
                return isinstance(node, ast.ClassDef) and attributeCondition(node.type_params)
            return workhorse
    ClassDef = _ClassDef()
    "`Be.ClassDef`, ***Class*** ***Def***inition, matches `class` `ast.ClassDef`.\n\n        This `class` is associated with Python keywords `class` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    @staticmethod
    def cmpop(node: ast.AST) -> TypeIs[ast.cmpop]:
        """`Be.cmpop`, ***c***o***mp***arison ***op***erator, matches any of `ast.Is` | `ast.Lt` | `ast.NotIn` | `ast.Gt` | `ast.Eq` | `ast.NotEq` | `ast.IsNot` | `ast.In` | `ast.GtE` | `class` `ast.cmpop` | `ast.LtE`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.cmpop)

    class _Compare:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Compare]:
            return isinstance(node, ast.Compare)

        @staticmethod
        def leftIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Compare] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Compare] | bool:
                return isinstance(node, ast.Compare) and attributeCondition(node.left)
            return workhorse

        @staticmethod
        def opsIs(attributeCondition: Callable[[Sequence[ast.cmpop]], bool]) -> Callable[[ast.AST], TypeIs[ast.Compare] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Compare] | bool:
                return isinstance(node, ast.Compare) and attributeCondition(node.ops)
            return workhorse

        @staticmethod
        def comparatorsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Compare] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Compare] | bool:
                return isinstance(node, ast.Compare) and attributeCondition(node.comparators)
            return workhorse
    Compare = _Compare()
    '`Be.Compare` matches `class` `ast.Compare`.\n\n        It is a subclass of `ast.expr`.\n        '

    class _comprehension:

        def __call__(self, node: ast.AST) -> TypeIs[ast.comprehension]:
            return isinstance(node, ast.comprehension)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.comprehension] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.comprehension] | bool:
                return isinstance(node, ast.comprehension) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def iterIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.comprehension] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.comprehension] | bool:
                return isinstance(node, ast.comprehension) and attributeCondition(node.iter)
            return workhorse

        @staticmethod
        def ifsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.comprehension] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.comprehension] | bool:
                return isinstance(node, ast.comprehension) and attributeCondition(node.ifs)
            return workhorse

        @staticmethod
        def is_asyncIs(attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[ast.comprehension] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.comprehension] | bool:
                return isinstance(node, ast.comprehension) and attributeCondition(node.is_async)
            return workhorse
    comprehension = _comprehension()
    '`Be.comprehension` matches `class` `ast.comprehension`.\n\n        It is a subclass of `ast.AST`.\n        '

    class _Constant:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Constant]:
            return isinstance(node, ast.Constant)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ConstantValueType], bool]) -> Callable[[ast.AST], TypeIs[ast.Constant] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Constant] | bool:
                return isinstance(node, ast.Constant) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def kindIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Constant] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Constant] | bool:
                return isinstance(node, ast.Constant) and attributeCondition(node.kind)
            return workhorse
    Constant = _Constant()
    '`Be.Constant` matches any of `ast.Ellipsis` | `ast.Str` | `ast.Num` | `ast.NameConstant` | `ast.Bytes` | `class` `ast.Constant`.\n\n        It is a subclass of `ast.expr`.\n        '

    @staticmethod
    def Continue(node: ast.AST) -> TypeIs[ast.Continue]:
        """`Be.Continue` matches `class` `ast.Continue`.

        This `class` is associated with Python keywords `continue`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Continue)

    @staticmethod
    def Del(node: ast.AST) -> TypeIs[ast.Del]:
        """`Be.Del`, ***Del***ete, matches `class` `ast.Del`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Del)

    class _Delete:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Delete]:
            return isinstance(node, ast.Delete)

        @staticmethod
        def targetsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Delete] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Delete] | bool:
                return isinstance(node, ast.Delete) and attributeCondition(node.targets)
            return workhorse
    Delete = _Delete()
    '`Be.Delete` matches `class` `ast.Delete`.\n\n        This `class` is associated with Python keywords `del`.\n        It is a subclass of `ast.stmt`.\n        '

    class _Dict:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Dict]:
            return isinstance(node, ast.Dict)

        @staticmethod
        def keysIs(attributeCondition: Callable[[Sequence[ast.expr | None]], bool]) -> Callable[[ast.AST], TypeIs[ast.Dict] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Dict] | bool:
                return isinstance(node, ast.Dict) and attributeCondition(node.keys)
            return workhorse

        @staticmethod
        def valuesIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Dict] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Dict] | bool:
                return isinstance(node, ast.Dict) and attributeCondition(node.values)
            return workhorse
    Dict = _Dict()
    "`Be.Dict`, ***Dict***ionary, matches `class` `ast.Dict`.\n\n        This `class` is associated with Python delimiters '{}'.\n        It is a subclass of `ast.expr`.\n        "

    class _DictComp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.DictComp]:
            return isinstance(node, ast.DictComp)

        @staticmethod
        def keyIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.DictComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.DictComp] | bool:
                return isinstance(node, ast.DictComp) and attributeCondition(node.key)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.DictComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.DictComp] | bool:
                return isinstance(node, ast.DictComp) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def generatorsIs(attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeIs[ast.DictComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.DictComp] | bool:
                return isinstance(node, ast.DictComp) and attributeCondition(node.generators)
            return workhorse
    DictComp = _DictComp()
    "`Be.DictComp`, ***Dict***ionary ***c***o***mp***rehension, matches `class` `ast.DictComp`.\n\n        This `class` is associated with Python delimiters '{}'.\n        It is a subclass of `ast.expr`.\n        "

    @staticmethod
    def Div(node: ast.AST) -> TypeIs[ast.Div]:
        """`Be.Div`, ***Div***ision, matches any of `ast.Div` | `class` `ast.Div`.

        This `class` is associated with Python delimiters '/=' and Python operators '/'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Div)

    @staticmethod
    def Eq(node: ast.AST) -> TypeIs[ast.Eq]:
        """`Be.Eq`, is ***Eq***ual to, matches `class` `ast.Eq`.

        This `class` is associated with Python operators '=='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Eq)

    @staticmethod
    def excepthandler(node: ast.AST) -> TypeIs[ast.excepthandler]:
        """`Be.excepthandler`, ***except***ion ***handler***, matches any of `ast.ExceptHandler` | `class` `ast.excepthandler`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.excepthandler)

    class _ExceptHandler:

        def __call__(self, node: ast.AST) -> TypeIs[ast.ExceptHandler]:
            return isinstance(node, ast.ExceptHandler)

        @staticmethod
        def typeIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.ExceptHandler] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ExceptHandler] | bool:
                return isinstance(node, ast.ExceptHandler) and attributeCondition(node.type)
            return workhorse

        @staticmethod
        def nameIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.ExceptHandler] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ExceptHandler] | bool:
                return isinstance(node, ast.ExceptHandler) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.ExceptHandler] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ExceptHandler] | bool:
                return isinstance(node, ast.ExceptHandler) and attributeCondition(node.body)
            return workhorse
    ExceptHandler = _ExceptHandler()
    '`Be.ExceptHandler`, ***Except***ion ***Handler***, matches `class` `ast.ExceptHandler`.\n\n        This `class` is associated with Python keywords `except`.\n        It is a subclass of `ast.excepthandler`.\n        '

    @staticmethod
    def expr(node: ast.AST) -> TypeIs[ast.expr]:
        """`Be.expr`, ***expr***ession, matches any of `ast.Call` | `class` `ast.expr` | `ast.Tuple` | `ast.List` | `ast.ListComp` | `ast.Name` | `ast.BoolOp` | `ast.BinOp` | `ast.Yield` | `ast.Attribute` | `ast.IfExp` | `ast.Set` | `ast.DictComp` | `ast.NamedExpr` | `ast.Subscript` | `ast.Dict` | `ast.FormattedValue` | `ast.Await` | `ast.Constant` | `ast.Lambda` | `ast.YieldFrom` | `ast.JoinedStr` | `ast.SetComp` | `ast.GeneratorExp` | `ast.Compare` | `ast.Slice` | `ast.Starred` | `ast.UnaryOp`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.expr)

    class _Expr:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Expr]:
            return isinstance(node, ast.Expr)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Expr] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Expr] | bool:
                return isinstance(node, ast.Expr) and attributeCondition(node.value)
            return workhorse
    Expr = _Expr()
    '`Be.Expr`, ***Expr***ession, matches `class` `ast.Expr`.\n\n        It is a subclass of `ast.stmt`.\n        '

    @staticmethod
    def expr_context(node: ast.AST) -> TypeIs[ast.expr_context]:
        """`Be.expr_context`, ***expr***ession ***context***, matches any of `ast.Param` | `ast.Store` | `ast.AugStore` | `ast.AugLoad` | `class` `ast.expr_context` | `ast.Del` | `ast.Load`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.expr_context)

    class _Expression:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Expression]:
            return isinstance(node, ast.Expression)

        @staticmethod
        def bodyIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Expression] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Expression] | bool:
                return isinstance(node, ast.Expression) and attributeCondition(node.body)
            return workhorse
    Expression = _Expression()
    '`Be.Expression` matches `class` `ast.Expression`.\n\n        It is a subclass of `ast.mod`.\n        '

    @staticmethod
    def FloorDiv(node: ast.AST) -> TypeIs[ast.FloorDiv]:
        """`Be.FloorDiv`, Floor ***Div***ision, matches any of `ast.FloorDiv` | `class` `ast.FloorDiv`.

        This `class` is associated with Python delimiters '//=' and Python operators '//'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.FloorDiv)

    class _For:

        def __call__(self, node: ast.AST) -> TypeIs[ast.For]:
            return isinstance(node, ast.For)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.For] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.For] | bool:
                return isinstance(node, ast.For) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def iterIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.For] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.For] | bool:
                return isinstance(node, ast.For) and attributeCondition(node.iter)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.For] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.For] | bool:
                return isinstance(node, ast.For) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.For] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.For] | bool:
                return isinstance(node, ast.For) and attributeCondition(node.orelse)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.For] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.For] | bool:
                return isinstance(node, ast.For) and attributeCondition(node.type_comment)
            return workhorse
    For = _For()
    "`Be.For` matches `class` `ast.For`.\n\n        This `class` is associated with Python keywords `for` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _FormattedValue:

        def __call__(self, node: ast.AST) -> TypeIs[ast.FormattedValue]:
            return isinstance(node, ast.FormattedValue)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.FormattedValue] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FormattedValue] | bool:
                return isinstance(node, ast.FormattedValue) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def conversionIs(attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[ast.FormattedValue] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FormattedValue] | bool:
                return isinstance(node, ast.FormattedValue) and attributeCondition(node.conversion)
            return workhorse

        @staticmethod
        def format_specIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.FormattedValue] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FormattedValue] | bool:
                return isinstance(node, ast.FormattedValue) and attributeCondition(node.format_spec)
            return workhorse
    FormattedValue = _FormattedValue()
    "`Be.FormattedValue` matches `class` `ast.FormattedValue`.\n\n        This `class` is associated with Python delimiters '{}'.\n        It is a subclass of `ast.expr`.\n        "

    class _FunctionDef:

        def __call__(self, node: ast.AST) -> TypeIs[ast.FunctionDef]:
            return isinstance(node, ast.FunctionDef)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def argsIs(attributeCondition: Callable[[ast.arguments], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.args)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def decorator_listIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.decorator_list)
            return workhorse

        @staticmethod
        def returnsIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.returns)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.type_comment)
            return workhorse

        @staticmethod
        def type_paramsIs(attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
                return isinstance(node, ast.FunctionDef) and attributeCondition(node.type_params)
            return workhorse
    FunctionDef = _FunctionDef()
    "`Be.FunctionDef`, Function ***Def***inition, matches `class` `ast.FunctionDef`.\n\n        This `class` is associated with Python keywords `def` and Python delimiters '()'.\n        It is a subclass of `ast.stmt`.\n        "

    class _FunctionType:

        def __call__(self, node: ast.AST) -> TypeIs[ast.FunctionType]:
            return isinstance(node, ast.FunctionType)

        @staticmethod
        def argtypesIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionType] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionType] | bool:
                return isinstance(node, ast.FunctionType) and attributeCondition(node.argtypes)
            return workhorse

        @staticmethod
        def returnsIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.FunctionType] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.FunctionType] | bool:
                return isinstance(node, ast.FunctionType) and attributeCondition(node.returns)
            return workhorse
    FunctionType = _FunctionType()
    '`Be.FunctionType`, Function Type, matches `class` `ast.FunctionType`.\n\n        It is a subclass of `ast.mod`.\n        '

    class _GeneratorExp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.GeneratorExp]:
            return isinstance(node, ast.GeneratorExp)

        @staticmethod
        def eltIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.GeneratorExp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.GeneratorExp] | bool:
                return isinstance(node, ast.GeneratorExp) and attributeCondition(node.elt)
            return workhorse

        @staticmethod
        def generatorsIs(attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeIs[ast.GeneratorExp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.GeneratorExp] | bool:
                return isinstance(node, ast.GeneratorExp) and attributeCondition(node.generators)
            return workhorse
    GeneratorExp = _GeneratorExp()
    '`Be.GeneratorExp`, Generator ***Exp***ression, matches `class` `ast.GeneratorExp`.\n\n        It is a subclass of `ast.expr`.\n        '

    class _Global:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Global]:
            return isinstance(node, ast.Global)

        @staticmethod
        def namesIs(attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeIs[ast.Global] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Global] | bool:
                return isinstance(node, ast.Global) and attributeCondition(node.names)
            return workhorse
    Global = _Global()
    '`Be.Global` matches `class` `ast.Global`.\n\n        This `class` is associated with Python keywords `global`.\n        It is a subclass of `ast.stmt`.\n        '

    @staticmethod
    def Gt(node: ast.AST) -> TypeIs[ast.Gt]:
        """`Be.Gt`, is Greater than, matches `class` `ast.Gt`.

        This `class` is associated with Python operators '>'.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Gt)

    @staticmethod
    def GtE(node: ast.AST) -> TypeIs[ast.GtE]:
        """`Be.GtE`, is Greater than or Equal to, matches `class` `ast.GtE`.

        This `class` is associated with Python operators '>='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.GtE)

    class _If:

        def __call__(self, node: ast.AST) -> TypeIs[ast.If]:
            return isinstance(node, ast.If)

        @staticmethod
        def testIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.If] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.If] | bool:
                return isinstance(node, ast.If) and attributeCondition(node.test)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.If] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.If] | bool:
                return isinstance(node, ast.If) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.If] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.If] | bool:
                return isinstance(node, ast.If) and attributeCondition(node.orelse)
            return workhorse
    If = _If()
    "`Be.If` matches `class` `ast.If`.\n\n        This `class` is associated with Python keywords `if` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _IfExp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.IfExp]:
            return isinstance(node, ast.IfExp)

        @staticmethod
        def testIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.IfExp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.IfExp] | bool:
                return isinstance(node, ast.IfExp) and attributeCondition(node.test)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.IfExp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.IfExp] | bool:
                return isinstance(node, ast.IfExp) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.IfExp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.IfExp] | bool:
                return isinstance(node, ast.IfExp) and attributeCondition(node.orelse)
            return workhorse
    IfExp = _IfExp()
    '`Be.IfExp`, If ***Exp***ression, matches `class` `ast.IfExp`.\n\n        This `class` is associated with Python keywords `if`.\n        It is a subclass of `ast.expr`.\n        '

    class _Import:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Import]:
            return isinstance(node, ast.Import)

        @staticmethod
        def namesIs(attributeCondition: Callable[[list[ast.alias]], bool]) -> Callable[[ast.AST], TypeIs[ast.Import] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Import] | bool:
                return isinstance(node, ast.Import) and attributeCondition(node.names)
            return workhorse
    Import = _Import()
    '`Be.Import` matches `class` `ast.Import`.\n\n        This `class` is associated with Python keywords `import`.\n        It is a subclass of `ast.stmt`.\n        '

    class _ImportFrom:

        def __call__(self, node: ast.AST) -> TypeIs[ast.ImportFrom]:
            return isinstance(node, ast.ImportFrom)

        @staticmethod
        def moduleIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.ImportFrom] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ImportFrom] | bool:
                return isinstance(node, ast.ImportFrom) and attributeCondition(node.module)
            return workhorse

        @staticmethod
        def namesIs(attributeCondition: Callable[[list[ast.alias]], bool]) -> Callable[[ast.AST], TypeIs[ast.ImportFrom] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ImportFrom] | bool:
                return isinstance(node, ast.ImportFrom) and attributeCondition(node.names)
            return workhorse

        @staticmethod
        def levelIs(attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[ast.ImportFrom] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ImportFrom] | bool:
                return isinstance(node, ast.ImportFrom) and attributeCondition(node.level)
            return workhorse
    ImportFrom = _ImportFrom()
    '`Be.ImportFrom` matches `class` `ast.ImportFrom`.\n\n        This `class` is associated with Python keywords `import`.\n        It is a subclass of `ast.stmt`.\n        '

    @staticmethod
    def In(node: ast.AST) -> TypeIs[ast.In]:
        """`Be.In` matches `class` `ast.In`.

        This `class` is associated with Python keywords `in`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.In)

    class _Interactive:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Interactive]:
            return isinstance(node, ast.Interactive)

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.Interactive] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Interactive] | bool:
                return isinstance(node, ast.Interactive) and attributeCondition(node.body)
            return workhorse
    Interactive = _Interactive()
    '`Be.Interactive`, Interactive mode, matches `class` `ast.Interactive`.\n\n        It is a subclass of `ast.mod`.\n        '

    @staticmethod
    def Invert(node: ast.AST) -> TypeIs[ast.Invert]:
        """`Be.Invert` matches `class` `ast.Invert`.

        This `class` is associated with Python operators '~'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.Invert)

    @staticmethod
    def Is(node: ast.AST) -> TypeIs[ast.Is]:
        """`Be.Is` matches `class` `ast.Is`.

        This `class` is associated with Python keywords `is`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Is)

    @staticmethod
    def IsNot(node: ast.AST) -> TypeIs[ast.IsNot]:
        """`Be.IsNot` matches `class` `ast.IsNot`.

        This `class` is associated with Python keywords `is not`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.IsNot)

    class _JoinedStr:

        def __call__(self, node: ast.AST) -> TypeIs[ast.JoinedStr]:
            return isinstance(node, ast.JoinedStr)

        @staticmethod
        def valuesIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.JoinedStr] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.JoinedStr] | bool:
                return isinstance(node, ast.JoinedStr) and attributeCondition(node.values)
            return workhorse
    JoinedStr = _JoinedStr()
    '`Be.JoinedStr`, Joined ***Str***ing, matches `class` `ast.JoinedStr`.\n\n        It is a subclass of `ast.expr`.\n        '

    class _keyword:

        def __call__(self, node: ast.AST) -> TypeIs[ast.keyword]:
            return isinstance(node, ast.keyword)

        @staticmethod
        def argIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.keyword] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.keyword] | bool:
                return isinstance(node, ast.keyword) and attributeCondition(node.arg)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.keyword] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.keyword] | bool:
                return isinstance(node, ast.keyword) and attributeCondition(node.value)
            return workhorse
    keyword = _keyword()
    "`Be.keyword` matches `class` `ast.keyword`.\n\n        This `class` is associated with Python delimiters '='.\n        It is a subclass of `ast.AST`.\n        "

    class _Lambda:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Lambda]:
            return isinstance(node, ast.Lambda)

        @staticmethod
        def argsIs(attributeCondition: Callable[[ast.arguments], bool]) -> Callable[[ast.AST], TypeIs[ast.Lambda] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Lambda] | bool:
                return isinstance(node, ast.Lambda) and attributeCondition(node.args)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Lambda] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Lambda] | bool:
                return isinstance(node, ast.Lambda) and attributeCondition(node.body)
            return workhorse
    Lambda = _Lambda()
    "`Be.Lambda`, Lambda function, matches `class` `ast.Lambda`.\n\n        This `class` is associated with Python keywords `lambda` and Python delimiters ':'.\n        It is a subclass of `ast.expr`.\n        "

    class _List:

        def __call__(self, node: ast.AST) -> TypeIs[ast.List]:
            return isinstance(node, ast.List)

        @staticmethod
        def eltsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.List] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.List] | bool:
                return isinstance(node, ast.List) and attributeCondition(node.elts)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.List] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.List] | bool:
                return isinstance(node, ast.List) and attributeCondition(node.ctx)
            return workhorse
    List = _List()
    "`Be.List` matches `class` `ast.List`.\n\n        This `class` is associated with Python delimiters '[]'.\n        It is a subclass of `ast.expr`.\n        "

    class _ListComp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.ListComp]:
            return isinstance(node, ast.ListComp)

        @staticmethod
        def eltIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.ListComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ListComp] | bool:
                return isinstance(node, ast.ListComp) and attributeCondition(node.elt)
            return workhorse

        @staticmethod
        def generatorsIs(attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeIs[ast.ListComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ListComp] | bool:
                return isinstance(node, ast.ListComp) and attributeCondition(node.generators)
            return workhorse
    ListComp = _ListComp()
    "`Be.ListComp`, List ***c***o***mp***rehension, matches `class` `ast.ListComp`.\n\n        This `class` is associated with Python delimiters '[]'.\n        It is a subclass of `ast.expr`.\n        "

    @staticmethod
    def Load(node: ast.AST) -> TypeIs[ast.Load]:
        """`Be.Load` matches `class` `ast.Load`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Load)

    @staticmethod
    def LShift(node: ast.AST) -> TypeIs[ast.LShift]:
        """`Be.LShift`, Left Shift, matches any of `class` `ast.LShift` | `ast.LShift`.

        This `class` is associated with Python delimiters '<<=' and Python operators '<<'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.LShift)

    @staticmethod
    def Lt(node: ast.AST) -> TypeIs[ast.Lt]:
        """`Be.Lt`, is Less than, matches `class` `ast.Lt`.

        This `class` is associated with Python operators '<'.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.Lt)

    @staticmethod
    def LtE(node: ast.AST) -> TypeIs[ast.LtE]:
        """`Be.LtE`, is Less than or Equal to, matches `class` `ast.LtE`.

        This `class` is associated with Python operators '<='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.LtE)

    class _Match:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Match]:
            return isinstance(node, ast.Match)

        @staticmethod
        def subjectIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Match] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Match] | bool:
                return isinstance(node, ast.Match) and attributeCondition(node.subject)
            return workhorse

        @staticmethod
        def casesIs(attributeCondition: Callable[[list[ast.match_case]], bool]) -> Callable[[ast.AST], TypeIs[ast.Match] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Match] | bool:
                return isinstance(node, ast.Match) and attributeCondition(node.cases)
            return workhorse
    Match = _Match()
    "`Be.Match`, Match this, matches `class` `ast.Match`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _match_case:

        def __call__(self, node: ast.AST) -> TypeIs[ast.match_case]:
            return isinstance(node, ast.match_case)

        @staticmethod
        def patternIs(attributeCondition: Callable[[ast.pattern], bool]) -> Callable[[ast.AST], TypeIs[ast.match_case] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.match_case] | bool:
                return isinstance(node, ast.match_case) and attributeCondition(node.pattern)
            return workhorse

        @staticmethod
        def guardIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.match_case] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.match_case] | bool:
                return isinstance(node, ast.match_case) and attributeCondition(node.guard)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.match_case] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.match_case] | bool:
                return isinstance(node, ast.match_case) and attributeCondition(node.body)
            return workhorse
    match_case = _match_case()
    "`Be.match_case`, match case, matches `class` `ast.match_case`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.AST`.\n        "

    class _MatchAs:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchAs]:
            return isinstance(node, ast.MatchAs)

        @staticmethod
        def patternIs(attributeCondition: Callable[[ast.pattern | None], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchAs] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchAs] | bool:
                return isinstance(node, ast.MatchAs) and attributeCondition(node.pattern)
            return workhorse

        @staticmethod
        def nameIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchAs] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchAs] | bool:
                return isinstance(node, ast.MatchAs) and attributeCondition(node.name)
            return workhorse
    MatchAs = _MatchAs()
    "`Be.MatchAs`, Match As, matches `class` `ast.MatchAs`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchClass:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchClass]:
            return isinstance(node, ast.MatchClass)

        @staticmethod
        def clsIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchClass] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchClass] | bool:
                return isinstance(node, ast.MatchClass) and attributeCondition(node.cls)
            return workhorse

        @staticmethod
        def patternsIs(attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchClass] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchClass] | bool:
                return isinstance(node, ast.MatchClass) and attributeCondition(node.patterns)
            return workhorse

        @staticmethod
        def kwd_attrsIs(attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchClass] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchClass] | bool:
                return isinstance(node, ast.MatchClass) and attributeCondition(node.kwd_attrs)
            return workhorse

        @staticmethod
        def kwd_patternsIs(attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchClass] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchClass] | bool:
                return isinstance(node, ast.MatchClass) and attributeCondition(node.kwd_patterns)
            return workhorse
    MatchClass = _MatchClass()
    "`Be.MatchClass`, Match Class, matches `class` `ast.MatchClass`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchMapping:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchMapping]:
            return isinstance(node, ast.MatchMapping)

        @staticmethod
        def keysIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchMapping] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchMapping] | bool:
                return isinstance(node, ast.MatchMapping) and attributeCondition(node.keys)
            return workhorse

        @staticmethod
        def patternsIs(attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchMapping] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchMapping] | bool:
                return isinstance(node, ast.MatchMapping) and attributeCondition(node.patterns)
            return workhorse

        @staticmethod
        def restIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchMapping] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchMapping] | bool:
                return isinstance(node, ast.MatchMapping) and attributeCondition(node.rest)
            return workhorse
    MatchMapping = _MatchMapping()
    "`Be.MatchMapping`, Match Mapping, matches `class` `ast.MatchMapping`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchOr:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchOr]:
            return isinstance(node, ast.MatchOr)

        @staticmethod
        def patternsIs(attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchOr] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchOr] | bool:
                return isinstance(node, ast.MatchOr) and attributeCondition(node.patterns)
            return workhorse
    MatchOr = _MatchOr()
    "`Be.MatchOr`, Match this Or that, matches `class` `ast.MatchOr`.\n\n        This `class` is associated with Python delimiters ':' and Python operators '|'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchSequence:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchSequence]:
            return isinstance(node, ast.MatchSequence)

        @staticmethod
        def patternsIs(attributeCondition: Callable[[Sequence[ast.pattern]], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchSequence] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchSequence] | bool:
                return isinstance(node, ast.MatchSequence) and attributeCondition(node.patterns)
            return workhorse
    MatchSequence = _MatchSequence()
    "`Be.MatchSequence`, Match this Sequence, matches `class` `ast.MatchSequence`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchSingleton:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchSingleton]:
            return isinstance(node, ast.MatchSingleton)

        @staticmethod
        def valueIs(attributeCondition: Callable[[bool | None], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchSingleton] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchSingleton] | bool:
                return isinstance(node, ast.MatchSingleton) and attributeCondition(node.value)
            return workhorse
    MatchSingleton = _MatchSingleton()
    "`Be.MatchSingleton`, Match Singleton, matches `class` `ast.MatchSingleton`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchStar:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchStar]:
            return isinstance(node, ast.MatchStar)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchStar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchStar] | bool:
                return isinstance(node, ast.MatchStar) and attributeCondition(node.name)
            return workhorse
    MatchStar = _MatchStar()
    "`Be.MatchStar`, Match Star, matches `class` `ast.MatchStar`.\n\n        This `class` is associated with Python delimiters ':' and Python operators '*'.\n        It is a subclass of `ast.pattern`.\n        "

    class _MatchValue:

        def __call__(self, node: ast.AST) -> TypeIs[ast.MatchValue]:
            return isinstance(node, ast.MatchValue)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.MatchValue] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.MatchValue] | bool:
                return isinstance(node, ast.MatchValue) and attributeCondition(node.value)
            return workhorse
    MatchValue = _MatchValue()
    "`Be.MatchValue`, Match Value, matches `class` `ast.MatchValue`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.pattern`.\n        "

    @staticmethod
    def MatMult(node: ast.AST) -> TypeIs[ast.MatMult]:
        """`Be.MatMult`, ***Mat***rix ***Mult***iplication, matches any of `class` `ast.MatMult` | `ast.MatMult`.

        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.MatMult)

    @staticmethod
    def mod(node: ast.AST) -> TypeIs[ast.mod]:
        """`Be.mod`, ***mod***ule, matches any of `ast.Interactive` | `ast.Expression` | `class` `ast.mod` | `ast.Module` | `ast.FunctionType` | `ast.Suite`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.mod)

    @staticmethod
    def Mod(node: ast.AST) -> TypeIs[ast.Mod]:
        """`Be.Mod`, ***Mod***ulo, matches any of `ast.Mod` | `class` `ast.Mod`.

        This `class` is associated with Python delimiters '%=' and Python operators '%'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Mod)

    class _Module:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Module]:
            return isinstance(node, ast.Module)

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.Module] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Module] | bool:
                return isinstance(node, ast.Module) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def type_ignoresIs(attributeCondition: Callable[[list[ast.TypeIgnore]], bool]) -> Callable[[ast.AST], TypeIs[ast.Module] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Module] | bool:
                return isinstance(node, ast.Module) and attributeCondition(node.type_ignores)
            return workhorse
    Module = _Module()
    '`Be.Module` matches `class` `ast.Module`.\n\n        It is a subclass of `ast.mod`.\n        '

    @staticmethod
    def Mult(node: ast.AST) -> TypeIs[ast.Mult]:
        """`Be.Mult`, ***Mult***iplication, matches any of `ast.Mult` | `class` `ast.Mult`.

        This `class` is associated with Python delimiters '*=' and Python operators '*'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Mult)

    class _Name:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Name]:
            return isinstance(node, ast.Name)

        @staticmethod
        def idIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.Name] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Name] | bool:
                return isinstance(node, ast.Name) and attributeCondition(node.id)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.Name] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Name] | bool:
                return isinstance(node, ast.Name) and attributeCondition(node.ctx)
            return workhorse
    Name = _Name()
    '`Be.Name` matches `class` `ast.Name`.\n\n        It is a subclass of `ast.expr`.\n        '

    class _NamedExpr:

        def __call__(self, node: ast.AST) -> TypeIs[ast.NamedExpr]:
            return isinstance(node, ast.NamedExpr)

        @staticmethod
        def targetIs(attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeIs[ast.NamedExpr] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.NamedExpr] | bool:
                return isinstance(node, ast.NamedExpr) and attributeCondition(node.target)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.NamedExpr] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.NamedExpr] | bool:
                return isinstance(node, ast.NamedExpr) and attributeCondition(node.value)
            return workhorse
    NamedExpr = _NamedExpr()
    "`Be.NamedExpr`, Named ***Expr***ession, matches `class` `ast.NamedExpr`.\n\n        This `class` is associated with Python operators ':='.\n        It is a subclass of `ast.expr`.\n        "

    class _Nonlocal:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Nonlocal]:
            return isinstance(node, ast.Nonlocal)

        @staticmethod
        def namesIs(attributeCondition: Callable[[list[str]], bool]) -> Callable[[ast.AST], TypeIs[ast.Nonlocal] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Nonlocal] | bool:
                return isinstance(node, ast.Nonlocal) and attributeCondition(node.names)
            return workhorse
    Nonlocal = _Nonlocal()
    '`Be.Nonlocal` matches `class` `ast.Nonlocal`.\n\n        This `class` is associated with Python keywords `nonlocal`.\n        It is a subclass of `ast.stmt`.\n        '

    @staticmethod
    def Not(node: ast.AST) -> TypeIs[ast.Not]:
        """`Be.Not` matches `class` `ast.Not`.

        This `class` is associated with Python keywords `not`.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.Not)

    @staticmethod
    def NotEq(node: ast.AST) -> TypeIs[ast.NotEq]:
        """`Be.NotEq`, is Not ***Eq***ual to, matches `class` `ast.NotEq`.

        This `class` is associated with Python operators '!='.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.NotEq)

    @staticmethod
    def NotIn(node: ast.AST) -> TypeIs[ast.NotIn]:
        """`Be.NotIn`, is Not ***In***cluded in or does Not have membership In, matches `class` `ast.NotIn`.

        This `class` is associated with Python keywords `not in`.
        It is a subclass of `ast.cmpop`.
        """
        return isinstance(node, ast.NotIn)

    @staticmethod
    def operator(node: ast.AST) -> TypeIs[ast.operator]:
        """`Be.operator` matches any of `ast.FloorDiv` | `ast.Mod` | `ast.Div` | `ast.Sub` | `ast.LShift` | `ast.BitOr` | `ast.RShift` | `ast.MatMult` | `ast.Pow` | `ast.BitAnd` | `ast.Mult` | `class` `ast.operator` | `ast.Add` | `ast.BitXor`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.operator)

    @staticmethod
    def Or(node: ast.AST) -> TypeIs[ast.Or]:
        """`Be.Or` matches any of `ast.Or` | `class` `ast.Or`.

        This `class` is associated with Python keywords `or`.
        It is a subclass of `ast.boolop`.
        """
        return isinstance(node, ast.Or)

    class _ParamSpec:

        def __call__(self, node: ast.AST) -> TypeIs[ast.ParamSpec]:
            return isinstance(node, ast.ParamSpec)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.ParamSpec] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.ParamSpec] | bool:
                return isinstance(node, ast.ParamSpec) and attributeCondition(node.name)
            return workhorse
    ParamSpec = _ParamSpec()
    "`Be.ParamSpec`, ***Param***eter ***Spec***ification, matches `class` `ast.ParamSpec`.\n\n        This `class` is associated with Python delimiters '[]'.\n        It is a subclass of `ast.type_param`.\n        "

    @staticmethod
    def Pass(node: ast.AST) -> TypeIs[ast.Pass]:
        """`Be.Pass` matches `class` `ast.Pass`.

        This `class` is associated with Python keywords `pass`.
        It is a subclass of `ast.stmt`.
        """
        return isinstance(node, ast.Pass)

    @staticmethod
    def pattern(node: ast.AST) -> TypeIs[ast.pattern]:
        """`Be.pattern` matches any of `ast.MatchClass` | `ast.MatchMapping` | `ast.MatchSingleton` | `ast.MatchOr` | `ast.MatchAs` | `ast.MatchSequence` | `ast.MatchValue` | `class` `ast.pattern` | `ast.MatchStar`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.pattern)

    @staticmethod
    def Pow(node: ast.AST) -> TypeIs[ast.Pow]:
        """`Be.Pow`, ***Pow***er, matches any of `class` `ast.Pow` | `ast.Pow`.

        This `class` is associated with Python delimiters '**=' and Python operators '**'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Pow)

    class _Raise:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Raise]:
            return isinstance(node, ast.Raise)

        @staticmethod
        def excIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Raise] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Raise] | bool:
                return isinstance(node, ast.Raise) and attributeCondition(node.exc)
            return workhorse

        @staticmethod
        def causeIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Raise] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Raise] | bool:
                return isinstance(node, ast.Raise) and attributeCondition(node.cause)
            return workhorse
    Raise = _Raise()
    '`Be.Raise` matches `class` `ast.Raise`.\n\n        This `class` is associated with Python keywords `raise`.\n        It is a subclass of `ast.stmt`.\n        '

    class _Return:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Return]:
            return isinstance(node, ast.Return)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Return] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Return] | bool:
                return isinstance(node, ast.Return) and attributeCondition(node.value)
            return workhorse
    Return = _Return()
    '`Be.Return` matches `class` `ast.Return`.\n\n        This `class` is associated with Python keywords `return`.\n        It is a subclass of `ast.stmt`.\n        '

    @staticmethod
    def RShift(node: ast.AST) -> TypeIs[ast.RShift]:
        """`Be.RShift`, Right Shift, matches any of `class` `ast.RShift` | `ast.RShift`.

        This `class` is associated with Python delimiters '>>=' and Python operators '>>'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.RShift)

    class _Set:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Set]:
            return isinstance(node, ast.Set)

        @staticmethod
        def eltsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Set] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Set] | bool:
                return isinstance(node, ast.Set) and attributeCondition(node.elts)
            return workhorse
    Set = _Set()
    "`Be.Set` matches `class` `ast.Set`.\n\n        This `class` is associated with Python delimiters '{}'.\n        It is a subclass of `ast.expr`.\n        "

    class _SetComp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.SetComp]:
            return isinstance(node, ast.SetComp)

        @staticmethod
        def eltIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.SetComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.SetComp] | bool:
                return isinstance(node, ast.SetComp) and attributeCondition(node.elt)
            return workhorse

        @staticmethod
        def generatorsIs(attributeCondition: Callable[[list[ast.comprehension]], bool]) -> Callable[[ast.AST], TypeIs[ast.SetComp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.SetComp] | bool:
                return isinstance(node, ast.SetComp) and attributeCondition(node.generators)
            return workhorse
    SetComp = _SetComp()
    "`Be.SetComp`, Set ***c***o***mp***rehension, matches `class` `ast.SetComp`.\n\n        This `class` is associated with Python delimiters '{}'.\n        It is a subclass of `ast.expr`.\n        "

    class _Slice:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Slice]:
            return isinstance(node, ast.Slice)

        @staticmethod
        def lowerIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Slice] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Slice] | bool:
                return isinstance(node, ast.Slice) and attributeCondition(node.lower)
            return workhorse

        @staticmethod
        def upperIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Slice] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Slice] | bool:
                return isinstance(node, ast.Slice) and attributeCondition(node.upper)
            return workhorse

        @staticmethod
        def stepIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Slice] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Slice] | bool:
                return isinstance(node, ast.Slice) and attributeCondition(node.step)
            return workhorse
    Slice = _Slice()
    "`Be.Slice` matches `class` `ast.Slice`.\n\n        This `class` is associated with Python delimiters '[], :'.\n        It is a subclass of `ast.expr`.\n        "

    class _Starred:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Starred]:
            return isinstance(node, ast.Starred)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Starred] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Starred] | bool:
                return isinstance(node, ast.Starred) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.Starred] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Starred] | bool:
                return isinstance(node, ast.Starred) and attributeCondition(node.ctx)
            return workhorse
    Starred = _Starred()
    "`Be.Starred` matches `class` `ast.Starred`.\n\n        This `class` is associated with Python operators '*'.\n        It is a subclass of `ast.expr`.\n        "

    @staticmethod
    def stmt(node: ast.AST) -> TypeIs[ast.stmt]:
        """`Be.stmt`, ***st***ate***m***en***t***, matches any of `ast.Delete` | `ast.FunctionDef` | `ast.Import` | `ast.Pass` | `ast.AsyncFunctionDef` | `ast.Nonlocal` | `ast.TypeAlias` | `ast.Raise` | `ast.With` | `class` `ast.stmt` | `ast.AsyncWith` | `ast.If` | `ast.Continue` | `ast.Assign` | `ast.Expr` | `ast.Try` | `ast.AsyncFor` | `ast.Break` | `ast.Return` | `ast.Match` | `ast.TryStar` | `ast.AnnAssign` | `ast.For` | `ast.While` | `ast.Assert` | `ast.ClassDef` | `ast.ImportFrom` | `ast.Global` | `ast.AugAssign`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.stmt)

    @staticmethod
    def Store(node: ast.AST) -> TypeIs[ast.Store]:
        """`Be.Store` matches `class` `ast.Store`.

        It is a subclass of `ast.expr_context`.
        """
        return isinstance(node, ast.Store)

    @staticmethod
    def Sub(node: ast.AST) -> TypeIs[ast.Sub]:
        """`Be.Sub`, ***Sub***traction, matches any of `ast.Sub` | `class` `ast.Sub`.

        This `class` is associated with Python delimiters '-=' and Python operators '-'.
        It is a subclass of `ast.operator`.
        """
        return isinstance(node, ast.Sub)

    class _Subscript:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Subscript]:
            return isinstance(node, ast.Subscript)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Subscript] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Subscript] | bool:
                return isinstance(node, ast.Subscript) and attributeCondition(node.value)
            return workhorse

        @staticmethod
        def sliceIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.Subscript] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Subscript] | bool:
                return isinstance(node, ast.Subscript) and attributeCondition(node.slice)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.Subscript] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Subscript] | bool:
                return isinstance(node, ast.Subscript) and attributeCondition(node.ctx)
            return workhorse
    Subscript = _Subscript()
    "`Be.Subscript` matches `class` `ast.Subscript`.\n\n        This `class` is associated with Python delimiters '[]'.\n        It is a subclass of `ast.expr`.\n        "

    class _Try:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Try]:
            return isinstance(node, ast.Try)

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.Try] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Try] | bool:
                return isinstance(node, ast.Try) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def handlersIs(attributeCondition: Callable[[list[ast.ExceptHandler]], bool]) -> Callable[[ast.AST], TypeIs[ast.Try] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Try] | bool:
                return isinstance(node, ast.Try) and attributeCondition(node.handlers)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.Try] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Try] | bool:
                return isinstance(node, ast.Try) and attributeCondition(node.orelse)
            return workhorse

        @staticmethod
        def finalbodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.Try] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Try] | bool:
                return isinstance(node, ast.Try) and attributeCondition(node.finalbody)
            return workhorse
    Try = _Try()
    "`Be.Try` matches `class` `ast.Try`.\n\n        This `class` is associated with Python keywords `try`, `except` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _TryStar:

        def __call__(self, node: ast.AST) -> TypeIs[ast.TryStar]:
            return isinstance(node, ast.TryStar)

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.TryStar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TryStar] | bool:
                return isinstance(node, ast.TryStar) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def handlersIs(attributeCondition: Callable[[list[ast.ExceptHandler]], bool]) -> Callable[[ast.AST], TypeIs[ast.TryStar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TryStar] | bool:
                return isinstance(node, ast.TryStar) and attributeCondition(node.handlers)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.TryStar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TryStar] | bool:
                return isinstance(node, ast.TryStar) and attributeCondition(node.orelse)
            return workhorse

        @staticmethod
        def finalbodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.TryStar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TryStar] | bool:
                return isinstance(node, ast.TryStar) and attributeCondition(node.finalbody)
            return workhorse
    TryStar = _TryStar()
    '`Be.TryStar`, Try executing this, protected by `except*` ("except star"), matches `class` `ast.TryStar`.\n\n        This `class` is associated with Python keywords `try`, `except*` and Python delimiters \':\'.\n        It is a subclass of `ast.stmt`.\n        '

    class _Tuple:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Tuple]:
            return isinstance(node, ast.Tuple)

        @staticmethod
        def eltsIs(attributeCondition: Callable[[Sequence[ast.expr]], bool]) -> Callable[[ast.AST], TypeIs[ast.Tuple] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Tuple] | bool:
                return isinstance(node, ast.Tuple) and attributeCondition(node.elts)
            return workhorse

        @staticmethod
        def ctxIs(attributeCondition: Callable[[ast.expr_context], bool]) -> Callable[[ast.AST], TypeIs[ast.Tuple] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Tuple] | bool:
                return isinstance(node, ast.Tuple) and attributeCondition(node.ctx)
            return workhorse
    Tuple = _Tuple()
    "`Be.Tuple` matches `class` `ast.Tuple`.\n\n        This `class` is associated with Python delimiters '()'.\n        It is a subclass of `ast.expr`.\n        "

    @staticmethod
    def type_ignore(node: ast.AST) -> TypeIs[ast.type_ignore]:
        """`Be.type_ignore`, this `type` error, you ignore it, matches any of `class` `ast.type_ignore` | `ast.TypeIgnore`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.type_ignore)

    @staticmethod
    def type_param(node: ast.AST) -> TypeIs[ast.type_param]:
        """`Be.type_param`, type ***param***eter, matches any of `class` `ast.type_param` | `ast.ParamSpec` | `ast.TypeVarTuple` | `ast.TypeVar`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.type_param)

    class _TypeAlias:

        def __call__(self, node: ast.AST) -> TypeIs[ast.TypeAlias]:
            return isinstance(node, ast.TypeAlias)

        @staticmethod
        def nameIs(attributeCondition: Callable[[ast.Name], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeAlias] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeAlias] | bool:
                return isinstance(node, ast.TypeAlias) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def type_paramsIs(attributeCondition: Callable[[Sequence[ast.type_param]], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeAlias] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeAlias] | bool:
                return isinstance(node, ast.TypeAlias) and attributeCondition(node.type_params)
            return workhorse

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeAlias] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeAlias] | bool:
                return isinstance(node, ast.TypeAlias) and attributeCondition(node.value)
            return workhorse
    TypeAlias = _TypeAlias()
    '`Be.TypeAlias`, Type Alias, matches `class` `ast.TypeAlias`.\n\n        It is a subclass of `ast.stmt`.\n        '

    class _TypeIgnore:

        def __call__(self, node: ast.AST) -> TypeIs[ast.TypeIgnore]:
            return isinstance(node, ast.TypeIgnore)

        @staticmethod
        def linenoIs(attributeCondition: Callable[[int], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeIgnore] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeIgnore] | bool:
                return isinstance(node, ast.TypeIgnore) and attributeCondition(node.lineno)
            return workhorse

        @staticmethod
        def tagIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeIgnore] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeIgnore] | bool:
                return isinstance(node, ast.TypeIgnore) and attributeCondition(node.tag)
            return workhorse
    TypeIgnore = _TypeIgnore()
    "`Be.TypeIgnore`, this Type (`type`) error, Ignore it, matches `class` `ast.TypeIgnore`.\n\n        This `class` is associated with Python delimiters ':'.\n        It is a subclass of `ast.type_ignore`.\n        "

    class _TypeVar:

        def __call__(self, node: ast.AST) -> TypeIs[ast.TypeVar]:
            return isinstance(node, ast.TypeVar)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeVar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeVar] | bool:
                return isinstance(node, ast.TypeVar) and attributeCondition(node.name)
            return workhorse

        @staticmethod
        def boundIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeVar] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeVar] | bool:
                return isinstance(node, ast.TypeVar) and attributeCondition(node.bound)
            return workhorse
    TypeVar = _TypeVar()
    '`Be.TypeVar`, Type ***Var***iable, matches `class` `ast.TypeVar`.\n\n        It is a subclass of `ast.type_param`.\n        '

    class _TypeVarTuple:

        def __call__(self, node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
            return isinstance(node, ast.TypeVarTuple)

        @staticmethod
        def nameIs(attributeCondition: Callable[[str], bool]) -> Callable[[ast.AST], TypeIs[ast.TypeVarTuple] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.TypeVarTuple] | bool:
                return isinstance(node, ast.TypeVarTuple) and attributeCondition(node.name)
            return workhorse
    TypeVarTuple = _TypeVarTuple()
    "`Be.TypeVarTuple`, Type ***Var***iable ***Tuple***, matches `class` `ast.TypeVarTuple`.\n\n        This `class` is associated with Python operators '*'.\n        It is a subclass of `ast.type_param`.\n        "

    @staticmethod
    def UAdd(node: ast.AST) -> TypeIs[ast.UAdd]:
        """`Be.UAdd`, ***U***nary ***Add***ition, matches `class` `ast.UAdd`.

        This `class` is associated with Python operators '+'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.UAdd)

    @staticmethod
    def unaryop(node: ast.AST) -> TypeIs[ast.unaryop]:
        """`Be.unaryop`, ***un***ary ***op***erator, matches any of `ast.Invert` | `ast.Not` | `ast.UAdd` | `ast.USub` | `class` `ast.unaryop`.

        It is a subclass of `ast.AST`.
        """
        return isinstance(node, ast.unaryop)

    class _UnaryOp:

        def __call__(self, node: ast.AST) -> TypeIs[ast.UnaryOp]:
            return isinstance(node, ast.UnaryOp)

        @staticmethod
        def opIs(attributeCondition: Callable[[ast.unaryop], bool]) -> Callable[[ast.AST], TypeIs[ast.UnaryOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.UnaryOp] | bool:
                return isinstance(node, ast.UnaryOp) and attributeCondition(node.op)
            return workhorse

        @staticmethod
        def operandIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.UnaryOp] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.UnaryOp] | bool:
                return isinstance(node, ast.UnaryOp) and attributeCondition(node.operand)
            return workhorse
    UnaryOp = _UnaryOp()
    '`Be.UnaryOp`, ***Un***ary ***Op***eration, matches `class` `ast.UnaryOp`.\n\n        It is a subclass of `ast.expr`.\n        '

    @staticmethod
    def USub(node: ast.AST) -> TypeIs[ast.USub]:
        """`Be.USub`, ***U***nary ***Sub***traction, matches `class` `ast.USub`.

        This `class` is associated with Python operators '-'.
        It is a subclass of `ast.unaryop`.
        """
        return isinstance(node, ast.USub)

    class _While:

        def __call__(self, node: ast.AST) -> TypeIs[ast.While]:
            return isinstance(node, ast.While)

        @staticmethod
        def testIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.While] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.While] | bool:
                return isinstance(node, ast.While) and attributeCondition(node.test)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.While] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.While] | bool:
                return isinstance(node, ast.While) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def orelseIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.While] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.While] | bool:
                return isinstance(node, ast.While) and attributeCondition(node.orelse)
            return workhorse
    While = _While()
    '`Be.While` matches `class` `ast.While`.\n\n        This `class` is associated with Python keywords `while`.\n        It is a subclass of `ast.stmt`.\n        '

    class _With:

        def __call__(self, node: ast.AST) -> TypeIs[ast.With]:
            return isinstance(node, ast.With)

        @staticmethod
        def itemsIs(attributeCondition: Callable[[list[ast.withitem]], bool]) -> Callable[[ast.AST], TypeIs[ast.With] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.With] | bool:
                return isinstance(node, ast.With) and attributeCondition(node.items)
            return workhorse

        @staticmethod
        def bodyIs(attributeCondition: Callable[[Sequence[ast.stmt]], bool]) -> Callable[[ast.AST], TypeIs[ast.With] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.With] | bool:
                return isinstance(node, ast.With) and attributeCondition(node.body)
            return workhorse

        @staticmethod
        def type_commentIs(attributeCondition: Callable[[str | None], bool]) -> Callable[[ast.AST], TypeIs[ast.With] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.With] | bool:
                return isinstance(node, ast.With) and attributeCondition(node.type_comment)
            return workhorse
    With = _With()
    "`Be.With` matches `class` `ast.With`.\n\n        This `class` is associated with Python keywords `with` and Python delimiters ':'.\n        It is a subclass of `ast.stmt`.\n        "

    class _withitem:

        def __call__(self, node: ast.AST) -> TypeIs[ast.withitem]:
            return isinstance(node, ast.withitem)

        @staticmethod
        def context_exprIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.withitem] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.withitem] | bool:
                return isinstance(node, ast.withitem) and attributeCondition(node.context_expr)
            return workhorse

        @staticmethod
        def optional_varsIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.withitem] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.withitem] | bool:
                return isinstance(node, ast.withitem) and attributeCondition(node.optional_vars)
            return workhorse
    withitem = _withitem()
    '`Be.withitem`, with item, matches `class` `ast.withitem`.\n\n        This `class` is associated with Python keywords `as`.\n        It is a subclass of `ast.AST`.\n        '

    class _Yield:

        def __call__(self, node: ast.AST) -> TypeIs[ast.Yield]:
            return isinstance(node, ast.Yield)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr | None], bool]) -> Callable[[ast.AST], TypeIs[ast.Yield] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.Yield] | bool:
                return isinstance(node, ast.Yield) and attributeCondition(node.value)
            return workhorse
    Yield = _Yield()
    '`Be.Yield`, Yield an element, matches `class` `ast.Yield`.\n\n        This `class` is associated with Python keywords `yield`.\n        It is a subclass of `ast.expr`.\n        '

    class _YieldFrom:

        def __call__(self, node: ast.AST) -> TypeIs[ast.YieldFrom]:
            return isinstance(node, ast.YieldFrom)

        @staticmethod
        def valueIs(attributeCondition: Callable[[ast.expr], bool]) -> Callable[[ast.AST], TypeIs[ast.YieldFrom] | bool]:

            def workhorse(node: ast.AST) -> TypeIs[ast.YieldFrom] | bool:
                return isinstance(node, ast.YieldFrom) and attributeCondition(node.value)
            return workhorse
    YieldFrom = _YieldFrom()
    '`Be.YieldFrom`, Yield an element From, matches `class` `ast.YieldFrom`.\n\n        This `class` is associated with Python keywords `yield from`.\n        It is a subclass of `ast.expr`.\n        '