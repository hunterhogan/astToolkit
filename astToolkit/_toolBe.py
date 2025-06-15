"""This file is generated automatically, so changes to this file will be lost."""
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

    Parameters:

        node: AST node to test for specific type membership

    Returns:

        typeIs: `TypeIs` enabling both runtime validation and static type narrowing

    Examples:

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
        """`Be.Add` matches any of `class` `ast.Add` | `ast.Add`.
        This `class` is associated with Python delimiters '+=' and Python operators '+'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Add)

    @staticmethod
    def alias(node: ast.AST) -> TypeIs[ast.alias]:
        """`Be.alias` matches `class` `ast.alias`.
        It has attributes `name`, `asname`.
        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.alias)

    @staticmethod
    def And(node: ast.AST) -> TypeIs[ast.And]:
        """`Be.And` matches any of `class` `ast.And` | `ast.And`.
        This `class` is associated with Python keywords `and`.
        It is a subclass of `ast.boolop`."""
        return isinstance(node, ast.And)

    @staticmethod
    def AnnAssign(node: ast.AST) -> TypeIs[ast.AnnAssign]:
        """`Be.AnnAssign`, ***Ann***otated ***Assign***ment, matches `class` `ast.AnnAssign`.
        It has attributes `target`, `annotation`, `value`, `simple`.
        This `class` is associated with Python delimiters ':, ='.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.AnnAssign)

    @staticmethod
    def arg(node: ast.AST) -> TypeIs[ast.arg]:
        """`Be.arg`, ***arg***ument, matches `class` `ast.arg`.
        It has attributes `arg`, `annotation`, `type_comment`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.arg)

    @staticmethod
    def arguments(node: ast.AST) -> TypeIs[ast.arguments]:
        """`Be.arguments` matches `class` `ast.arguments`.
        It has attributes `posonlyargs`, `args`, `vararg`, `kwonlyargs`, `kw_defaults`, `kwarg`, `defaults`.
        This `class` is associated with Python delimiters ','.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.arguments)

    @staticmethod
    def Assert(node: ast.AST) -> TypeIs[ast.Assert]:
        """`Be.Assert` matches `class` `ast.Assert`.
        It has attributes `test`, `msg`.
        This `class` is associated with Python keywords `assert`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Assert)

    @staticmethod
    def Assign(node: ast.AST) -> TypeIs[ast.Assign]:
        """`Be.Assign` matches `class` `ast.Assign`.
        It has attributes `targets`, `value`, `type_comment`.
        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Assign)

    @staticmethod
    def AST(node: ast.AST) -> TypeIs[ast.AST]:
        """`Be.AST`, Abstract Syntax Tree, matches any of `class` `ast.AST` | `ast._NoParent` | `ast.alias` | `ast.arg` | `ast.arguments` | `ast.boolop` | `ast.cmpop` | `ast.comprehension` | `ast.excepthandler` | `ast.Exec` | `ast.expr_context` | `ast.expr` | `ast.keyword` | `ast.match_case` | `ast.mod` | `ast.NodeList` | `ast.operator` | `ast.pattern` | `ast.slice` | `ast.stmt` | `ast.type_ignore` | `ast.type_param` | `ast.unaryop` | `ast.withitem`.
        It is a subclass of `ast.object`."""
        return isinstance(node, ast.AST)

    @staticmethod
    def AsyncFor(node: ast.AST) -> TypeIs[ast.AsyncFor]:
        """`Be.AsyncFor`, ***Async***hronous For loop, matches `class` `ast.AsyncFor`.
        It has attributes `target`, `iter`, `body`, `orelse`, `type_comment`.
        This `class` is associated with Python keywords `async for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.AsyncFor)

    @staticmethod
    def AsyncFunctionDef(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
        """`Be.AsyncFunctionDef`, ***Async***hronous Function ***Def***inition, matches `class` `ast.AsyncFunctionDef`.
        It has attributes `name`, `args`, `body`, `decorator_list`, `returns`, `type_comment`, `type_params`.
        This `class` is associated with Python keywords `async def` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.AsyncFunctionDef)

    @staticmethod
    def AsyncWith(node: ast.AST) -> TypeIs[ast.AsyncWith]:
        """`Be.AsyncWith`, ***Async***hronous With statement, matches `class` `ast.AsyncWith`.
        It has attributes `items`, `body`, `type_comment`.
        This `class` is associated with Python keywords `async with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.AsyncWith)

    @staticmethod
    def Attribute(node: ast.AST) -> TypeIs[ast.Attribute]:
        """`Be.Attribute` matches `class` `ast.Attribute`.
        It has attributes `value`, `attr`, `ctx`.
        This `class` is associated with Python delimiters '.'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Attribute)

    @staticmethod
    def AugAssign(node: ast.AST) -> TypeIs[ast.AugAssign]:
        """`Be.AugAssign`, ***Aug***mented ***Assign***ment, matches `class` `ast.AugAssign`.
        It has attributes `target`, `op`, `value`.
        This `class` is associated with Python delimiters '+=, -=, *=, /=, //=, %=, **=, |=, &=, ^=, <<=, >>='.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.AugAssign)

    @staticmethod
    def Await(node: ast.AST) -> TypeIs[ast.Await]:
        """`Be.Await`, ***Await*** the asynchronous operation, matches `class` `ast.Await`.
        It has attributes `value`.
        This `class` is associated with Python keywords `await`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Await)

    @staticmethod
    def BinOp(node: ast.AST) -> TypeIs[ast.BinOp]:
        """`Be.BinOp`, ***Bin***ary ***Op***eration, matches `class` `ast.BinOp`.
        It has attributes `left`, `op`, `right`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.BinOp)

    @staticmethod
    def BitAnd(node: ast.AST) -> TypeIs[ast.BitAnd]:
        """`Be.BitAnd`, ***Bit***wise And, matches any of `class` `ast.BitAnd` | `ast.BitAnd`.
        This `class` is associated with Python operators '&'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.BitAnd)

    @staticmethod
    def BitOr(node: ast.AST) -> TypeIs[ast.BitOr]:
        """`Be.BitOr`, ***Bit***wise Or, matches any of `class` `ast.BitOr` | `ast.BitOr`.
        This `class` is associated with Python operators '|'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.BitOr)

    @staticmethod
    def BitXor(node: ast.AST) -> TypeIs[ast.BitXor]:
        """`Be.BitXor`, ***Bit***wise e***X***clusive Or, matches any of `class` `ast.BitXor` | `ast.BitXor`.
        This `class` is associated with Python operators '^'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.BitXor)

    @staticmethod
    def boolop(node: ast.AST) -> TypeIs[ast.boolop]:
        """`Be.boolop`, ***bool***ean ***op***erator, matches any of `class` `ast.boolop` | `ast.And` | `ast.Or`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.boolop)

    @staticmethod
    def BoolOp(node: ast.AST) -> TypeIs[ast.BoolOp]:
        """`Be.BoolOp`, ***Bool***ean ***Op***eration, matches `class` `ast.BoolOp`.
        It has attributes `op`, `values`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.BoolOp)

    @staticmethod
    def Break(node: ast.AST) -> TypeIs[ast.Break]:
        """`Be.Break` matches `class` `ast.Break`.
        This `class` is associated with Python keywords `break`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Break)

    @staticmethod
    def Call(node: ast.AST) -> TypeIs[ast.Call]:
        """`Be.Call` matches `class` `ast.Call`.
        It has attributes `func`, `args`, `keywords`.
        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Call)

    @staticmethod
    def ClassDef(node: ast.AST) -> TypeIs[ast.ClassDef]:
        """`Be.ClassDef`, ***Class*** ***Def***inition, matches `class` `ast.ClassDef`.
        It has attributes `name`, `bases`, `keywords`, `body`, `decorator_list`, `type_params`.
        This `class` is associated with Python keywords `class` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.ClassDef)

    @staticmethod
    def cmpop(node: ast.AST) -> TypeIs[ast.cmpop]:
        """`Be.cmpop`, ***c***o***mp***arison ***op***erator, matches any of `class` `ast.cmpop` | `ast.Eq` | `ast.Gt` | `ast.GtE` | `ast.In` | `ast.Is` | `ast.IsNot` | `ast.Lt` | `ast.LtE` | `ast.NotEq` | `ast.NotIn`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.cmpop)

    @staticmethod
    def Compare(node: ast.AST) -> TypeIs[ast.Compare]:
        """`Be.Compare` matches `class` `ast.Compare`.
        It has attributes `left`, `ops`, `comparators`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Compare)

    @staticmethod
    def comprehension(node: ast.AST) -> TypeIs[ast.comprehension]:
        """`Be.comprehension` matches `class` `ast.comprehension`.
        It has attributes `target`, `iter`, `ifs`, `is_async`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.comprehension)

    @staticmethod
    def Constant(node: ast.AST) -> TypeIs[ast.Constant]:
        """`Be.Constant` matches any of `class` `ast.Constant` | `ast.Bytes` | `ast.Bytes` | `ast.Ellipsis` | `ast.Ellipsis` | `ast.NameConstant` | `ast.NameConstant` | `ast.Num` | `ast.Num` | `ast.Str` | `ast.Str`.
        It has attributes `value`, `kind`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Constant)

    @staticmethod
    def Continue(node: ast.AST) -> TypeIs[ast.Continue]:
        """`Be.Continue` matches `class` `ast.Continue`.
        This `class` is associated with Python keywords `continue`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Continue)

    @staticmethod
    def Del(node: ast.AST) -> TypeIs[ast.Del]:
        """`Be.Del`, ***Del***ete, matches `class` `ast.Del`.
        It is a subclass of `ast.expr_context`."""
        return isinstance(node, ast.Del)

    @staticmethod
    def Delete(node: ast.AST) -> TypeIs[ast.Delete]:
        """`Be.Delete` matches `class` `ast.Delete`.
        It has attributes `targets`.
        This `class` is associated with Python keywords `del`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Delete)

    @staticmethod
    def Dict(node: ast.AST) -> TypeIs[ast.Dict]:
        """`Be.Dict`, ***Dict***ionary, matches `class` `ast.Dict`.
        It has attributes `keys`, `values`.
        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Dict)

    @staticmethod
    def DictComp(node: ast.AST) -> TypeIs[ast.DictComp]:
        """`Be.DictComp`, ***Dict***ionary ***c***o***mp***rehension, matches `class` `ast.DictComp`.
        It has attributes `key`, `value`, `generators`.
        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.DictComp)

    @staticmethod
    def Div(node: ast.AST) -> TypeIs[ast.Div]:
        """`Be.Div`, ***Div***ision, matches any of `class` `ast.Div` | `ast.Div`.
        This `class` is associated with Python delimiters '/=' and Python operators '/'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Div)

    @staticmethod
    def Eq(node: ast.AST) -> TypeIs[ast.Eq]:
        """`Be.Eq`, is ***Eq***ual to, matches `class` `ast.Eq`.
        This `class` is associated with Python operators '=='.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.Eq)

    @staticmethod
    def excepthandler(node: ast.AST) -> TypeIs[ast.excepthandler]:
        """`Be.excepthandler`, ***except***ion ***handler***, matches any of `class` `ast.excepthandler` | `ast.ExceptHandler`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.excepthandler)

    @staticmethod
    def ExceptHandler(node: ast.AST) -> TypeIs[ast.ExceptHandler]:
        """`Be.ExceptHandler`, ***Except***ion ***Handler***, matches `class` `ast.ExceptHandler`.
        It has attributes `type`, `name`, `body`.
        This `class` is associated with Python keywords `except`.
        It is a subclass of `ast.excepthandler`."""
        return isinstance(node, ast.ExceptHandler)

    @staticmethod
    def expr(node: ast.AST) -> TypeIs[ast.expr]:
        """`Be.expr`, ***expr***ession, matches any of `class` `ast.expr` | `ast.Attribute` | `ast.Await` | `ast.BinOp` | `ast.BoolOp` | `ast.Call` | `ast.Compare` | `ast.Constant` | `ast.Dict` | `ast.DictComp` | `ast.FormattedValue` | `ast.GeneratorExp` | `ast.IfExp` | `ast.JoinedStr` | `ast.Lambda` | `ast.List` | `ast.ListComp` | `ast.Name` | `ast.NamedExpr` | `ast.Set` | `ast.SetComp` | `ast.Slice` | `ast.Starred` | `ast.Subscript` | `ast.Tuple` | `ast.UnaryOp` | `ast.Yield` | `ast.YieldFrom`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.expr)

    @staticmethod
    def Expr(node: ast.AST) -> TypeIs[ast.Expr]:
        """`Be.Expr`, ***Expr***ession, matches `class` `ast.Expr`.
        It has attributes `value`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Expr)

    @staticmethod
    def expr_context(node: ast.AST) -> TypeIs[ast.expr_context]:
        """`Be.expr_context`, ***expr***ession ***context***, matches any of `class` `ast.expr_context` | `ast.AugLoad` | `ast.AugStore` | `ast.Del` | `ast.Load` | `ast.Param` | `ast.Store`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.expr_context)

    @staticmethod
    def Expression(node: ast.AST) -> TypeIs[ast.Expression]:
        """`Be.Expression` matches `class` `ast.Expression`.
        It has attributes `body`.
        It is a subclass of `ast.mod`."""
        return isinstance(node, ast.Expression)

    @staticmethod
    def FloorDiv(node: ast.AST) -> TypeIs[ast.FloorDiv]:
        """`Be.FloorDiv`, Floor ***Div***ision, matches any of `class` `ast.FloorDiv` | `ast.FloorDiv`.
        This `class` is associated with Python delimiters '//=' and Python operators '//'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.FloorDiv)

    @staticmethod
    def For(node: ast.AST) -> TypeIs[ast.For]:
        """`Be.For` matches `class` `ast.For`.
        It has attributes `target`, `iter`, `body`, `orelse`, `type_comment`.
        This `class` is associated with Python keywords `for` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.For)

    @staticmethod
    def FormattedValue(node: ast.AST) -> TypeIs[ast.FormattedValue]:
        """`Be.FormattedValue` matches `class` `ast.FormattedValue`.
        It has attributes `value`, `conversion`, `format_spec`.
        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.FormattedValue)

    @staticmethod
    def FunctionDef(node: ast.AST) -> TypeIs[ast.FunctionDef]:
        """`Be.FunctionDef`, Function ***Def***inition, matches `class` `ast.FunctionDef`.
        It has attributes `name`, `args`, `body`, `decorator_list`, `returns`, `type_comment`, `type_params`.
        This `class` is associated with Python keywords `def` and Python delimiters '()'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.FunctionDef)

    @staticmethod
    def FunctionType(node: ast.AST) -> TypeIs[ast.FunctionType]:
        """`Be.FunctionType`, Function Type, matches `class` `ast.FunctionType`.
        It has attributes `argtypes`, `returns`.
        It is a subclass of `ast.mod`."""
        return isinstance(node, ast.FunctionType)

    @staticmethod
    def GeneratorExp(node: ast.AST) -> TypeIs[ast.GeneratorExp]:
        """`Be.GeneratorExp`, Generator ***Exp***ression, matches `class` `ast.GeneratorExp`.
        It has attributes `elt`, `generators`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.GeneratorExp)

    @staticmethod
    def Global(node: ast.AST) -> TypeIs[ast.Global]:
        """`Be.Global` matches `class` `ast.Global`.
        It has attributes `names`.
        This `class` is associated with Python keywords `global`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Global)

    @staticmethod
    def Gt(node: ast.AST) -> TypeIs[ast.Gt]:
        """`Be.Gt`, is Greater than, matches `class` `ast.Gt`.
        This `class` is associated with Python operators '>'.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.Gt)

    @staticmethod
    def GtE(node: ast.AST) -> TypeIs[ast.GtE]:
        """`Be.GtE`, is Greater than or Equal to, matches `class` `ast.GtE`.
        This `class` is associated with Python operators '>='.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.GtE)

    @staticmethod
    def If(node: ast.AST) -> TypeIs[ast.If]:
        """`Be.If` matches `class` `ast.If`.
        It has attributes `test`, `body`, `orelse`.
        This `class` is associated with Python keywords `if` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.If)

    @staticmethod
    def IfExp(node: ast.AST) -> TypeIs[ast.IfExp]:
        """`Be.IfExp`, If ***Exp***ression, matches `class` `ast.IfExp`.
        It has attributes `test`, `body`, `orelse`.
        This `class` is associated with Python keywords `if`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.IfExp)

    @staticmethod
    def Import(node: ast.AST) -> TypeIs[ast.Import]:
        """`Be.Import` matches `class` `ast.Import`.
        It has attributes `names`.
        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Import)

    @staticmethod
    def ImportFrom(node: ast.AST) -> TypeIs[ast.ImportFrom]:
        """`Be.ImportFrom` matches `class` `ast.ImportFrom`.
        It has attributes `module`, `names`, `level`.
        This `class` is associated with Python keywords `import`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.ImportFrom)

    @staticmethod
    def In(node: ast.AST) -> TypeIs[ast.In]:
        """`Be.In` matches `class` `ast.In`.
        This `class` is associated with Python keywords `in`.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.In)

    @staticmethod
    def Interactive(node: ast.AST) -> TypeIs[ast.Interactive]:
        """`Be.Interactive`, Interactive mode, matches `class` `ast.Interactive`.
        It has attributes `body`.
        It is a subclass of `ast.mod`."""
        return isinstance(node, ast.Interactive)

    @staticmethod
    def Invert(node: ast.AST) -> TypeIs[ast.Invert]:
        """`Be.Invert` matches `class` `ast.Invert`.
        This `class` is associated with Python operators '~'.
        It is a subclass of `ast.unaryop`."""
        return isinstance(node, ast.Invert)

    @staticmethod
    def Is(node: ast.AST) -> TypeIs[ast.Is]:
        """`Be.Is` matches `class` `ast.Is`.
        This `class` is associated with Python keywords `is`.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.Is)

    @staticmethod
    def IsNot(node: ast.AST) -> TypeIs[ast.IsNot]:
        """`Be.IsNot` matches `class` `ast.IsNot`.
        This `class` is associated with Python keywords `is not`.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.IsNot)

    @staticmethod
    def JoinedStr(node: ast.AST) -> TypeIs[ast.JoinedStr]:
        """`Be.JoinedStr`, Joined ***Str***ing, matches `class` `ast.JoinedStr`.
        It has attributes `values`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.JoinedStr)

    @staticmethod
    def keyword(node: ast.AST) -> TypeIs[ast.keyword]:
        """`Be.keyword` matches `class` `ast.keyword`.
        It has attributes `arg`, `value`.
        This `class` is associated with Python delimiters '='.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.keyword)

    @staticmethod
    def Lambda(node: ast.AST) -> TypeIs[ast.Lambda]:
        """`Be.Lambda`, Lambda function, matches `class` `ast.Lambda`.
        It has attributes `args`, `body`.
        This `class` is associated with Python keywords `lambda` and Python delimiters ':'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Lambda)

    @staticmethod
    def List(node: ast.AST) -> TypeIs[ast.List]:
        """`Be.List` matches `class` `ast.List`.
        It has attributes `elts`, `ctx`.
        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.List)

    @staticmethod
    def ListComp(node: ast.AST) -> TypeIs[ast.ListComp]:
        """`Be.ListComp`, List ***c***o***mp***rehension, matches `class` `ast.ListComp`.
        It has attributes `elt`, `generators`.
        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.ListComp)

    @staticmethod
    def Load(node: ast.AST) -> TypeIs[ast.Load]:
        """`Be.Load` matches `class` `ast.Load`.
        It is a subclass of `ast.expr_context`."""
        return isinstance(node, ast.Load)

    @staticmethod
    def LShift(node: ast.AST) -> TypeIs[ast.LShift]:
        """`Be.LShift`, Left Shift, matches any of `class` `ast.LShift` | `ast.LShift`.
        This `class` is associated with Python delimiters '<<=' and Python operators '<<'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.LShift)

    @staticmethod
    def Lt(node: ast.AST) -> TypeIs[ast.Lt]:
        """`Be.Lt`, is Less than, matches `class` `ast.Lt`.
        This `class` is associated with Python operators '<'.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.Lt)

    @staticmethod
    def LtE(node: ast.AST) -> TypeIs[ast.LtE]:
        """`Be.LtE`, is Less than or Equal to, matches `class` `ast.LtE`.
        This `class` is associated with Python operators '<='.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.LtE)

    @staticmethod
    def Match(node: ast.AST) -> TypeIs[ast.Match]:
        """`Be.Match`, Match this, matches `class` `ast.Match`.
        It has attributes `subject`, `cases`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Match)

    @staticmethod
    def match_case(node: ast.AST) -> TypeIs[ast.match_case]:
        """`Be.match_case`, match case, matches `class` `ast.match_case`.
        It has attributes `pattern`, `guard`, `body`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.match_case)

    @staticmethod
    def MatchAs(node: ast.AST) -> TypeIs[ast.MatchAs]:
        """`Be.MatchAs`, Match As, matches `class` `ast.MatchAs`.
        It has attributes `pattern`, `name`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchAs)

    @staticmethod
    def MatchClass(node: ast.AST) -> TypeIs[ast.MatchClass]:
        """`Be.MatchClass`, Match Class, matches `class` `ast.MatchClass`.
        It has attributes `cls`, `patterns`, `kwd_attrs`, `kwd_patterns`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchClass)

    @staticmethod
    def MatchMapping(node: ast.AST) -> TypeIs[ast.MatchMapping]:
        """`Be.MatchMapping`, Match Mapping, matches `class` `ast.MatchMapping`.
        It has attributes `keys`, `patterns`, `rest`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchMapping)

    @staticmethod
    def MatchOr(node: ast.AST) -> TypeIs[ast.MatchOr]:
        """`Be.MatchOr`, Match this Or that, matches `class` `ast.MatchOr`.
        It has attributes `patterns`.
        This `class` is associated with Python delimiters ':' and Python operators '|'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchOr)

    @staticmethod
    def MatchSequence(node: ast.AST) -> TypeIs[ast.MatchSequence]:
        """`Be.MatchSequence`, Match this Sequence, matches `class` `ast.MatchSequence`.
        It has attributes `patterns`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchSequence)

    @staticmethod
    def MatchSingleton(node: ast.AST) -> TypeIs[ast.MatchSingleton]:
        """`Be.MatchSingleton`, Match Singleton, matches `class` `ast.MatchSingleton`.
        It has attributes `value`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchSingleton)

    @staticmethod
    def MatchStar(node: ast.AST) -> TypeIs[ast.MatchStar]:
        """`Be.MatchStar`, Match Star, matches `class` `ast.MatchStar`.
        It has attributes `name`.
        This `class` is associated with Python delimiters ':' and Python operators '*'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchStar)

    @staticmethod
    def MatchValue(node: ast.AST) -> TypeIs[ast.MatchValue]:
        """`Be.MatchValue`, Match Value, matches `class` `ast.MatchValue`.
        It has attributes `value`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.pattern`."""
        return isinstance(node, ast.MatchValue)

    @staticmethod
    def MatMult(node: ast.AST) -> TypeIs[ast.MatMult]:
        """`Be.MatMult`, ***Mat***rix ***Mult***iplication, matches any of `class` `ast.MatMult` | `ast.MatMult`.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.MatMult)

    @staticmethod
    def mod(node: ast.AST) -> TypeIs[ast.mod]:
        """`Be.mod`, ***mod***ule, matches any of `class` `ast.mod` | `ast.Expression` | `ast.FunctionType` | `ast.Interactive` | `ast.Module` | `ast.Suite`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.mod)

    @staticmethod
    def Mod(node: ast.AST) -> TypeIs[ast.Mod]:
        """`Be.Mod`, ***Mod***ulo, matches any of `class` `ast.Mod` | `ast.Mod`.
        This `class` is associated with Python delimiters '%=' and Python operators '%'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Mod)

    @staticmethod
    def Module(node: ast.AST) -> TypeIs[ast.Module]:
        """`Be.Module` matches `class` `ast.Module`.
        It has attributes `body`, `type_ignores`.
        It is a subclass of `ast.mod`."""
        return isinstance(node, ast.Module)

    @staticmethod
    def Mult(node: ast.AST) -> TypeIs[ast.Mult]:
        """`Be.Mult`, ***Mult***iplication, matches any of `class` `ast.Mult` | `ast.Mult`.
        This `class` is associated with Python delimiters '*=' and Python operators '*'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Mult)

    @staticmethod
    def Name(node: ast.AST) -> TypeIs[ast.Name]:
        """`Be.Name` matches `class` `ast.Name`.
        It has attributes `id`, `ctx`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Name)

    @staticmethod
    def NamedExpr(node: ast.AST) -> TypeIs[ast.NamedExpr]:
        """`Be.NamedExpr`, Named ***Expr***ession, matches `class` `ast.NamedExpr`.
        It has attributes `target`, `value`.
        This `class` is associated with Python operators ':='.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.NamedExpr)

    @staticmethod
    def Nonlocal(node: ast.AST) -> TypeIs[ast.Nonlocal]:
        """`Be.Nonlocal` matches `class` `ast.Nonlocal`.
        It has attributes `names`.
        This `class` is associated with Python keywords `nonlocal`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Nonlocal)

    @staticmethod
    def Not(node: ast.AST) -> TypeIs[ast.Not]:
        """`Be.Not` matches `class` `ast.Not`.
        This `class` is associated with Python keywords `not`.
        It is a subclass of `ast.unaryop`."""
        return isinstance(node, ast.Not)

    @staticmethod
    def NotEq(node: ast.AST) -> TypeIs[ast.NotEq]:
        """`Be.NotEq`, is Not ***Eq***ual to, matches `class` `ast.NotEq`.
        This `class` is associated with Python operators '!='.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.NotEq)

    @staticmethod
    def NotIn(node: ast.AST) -> TypeIs[ast.NotIn]:
        """`Be.NotIn`, is Not ***In***cluded in or does Not have membership In, matches `class` `ast.NotIn`.
        This `class` is associated with Python keywords `not in`.
        It is a subclass of `ast.cmpop`."""
        return isinstance(node, ast.NotIn)

    @staticmethod
    def operator(node: ast.AST) -> TypeIs[ast.operator]:
        """`Be.operator` matches any of `class` `ast.operator` | `ast.Add` | `ast.BitAnd` | `ast.BitOr` | `ast.BitXor` | `ast.Div` | `ast.FloorDiv` | `ast.LShift` | `ast.MatMult` | `ast.Mod` | `ast.Mult` | `ast.Pow` | `ast.RShift` | `ast.Sub`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.operator)

    @staticmethod
    def Or(node: ast.AST) -> TypeIs[ast.Or]:
        """`Be.Or` matches any of `class` `ast.Or` | `ast.Or`.
        This `class` is associated with Python keywords `or`.
        It is a subclass of `ast.boolop`."""
        return isinstance(node, ast.Or)

    @staticmethod
    def ParamSpec(node: ast.AST) -> TypeIs[ast.ParamSpec]:
        """`Be.ParamSpec`, ***Param***eter ***Spec***ification, matches `class` `ast.ParamSpec`.
        It has attributes `name`, `default_value`.
        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.type_param`."""
        return isinstance(node, ast.ParamSpec)

    @staticmethod
    def Pass(node: ast.AST) -> TypeIs[ast.Pass]:
        """`Be.Pass` matches `class` `ast.Pass`.
        This `class` is associated with Python keywords `pass`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Pass)

    @staticmethod
    def pattern(node: ast.AST) -> TypeIs[ast.pattern]:
        """`Be.pattern` matches any of `class` `ast.pattern` | `ast.MatchAs` | `ast.MatchClass` | `ast.MatchMapping` | `ast.MatchOr` | `ast.MatchSequence` | `ast.MatchSingleton` | `ast.MatchStar` | `ast.MatchValue`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.pattern)

    @staticmethod
    def Pow(node: ast.AST) -> TypeIs[ast.Pow]:
        """`Be.Pow`, ***Pow***er, matches any of `class` `ast.Pow` | `ast.Pow`.
        This `class` is associated with Python delimiters '**=' and Python operators '**'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Pow)

    @staticmethod
    def Raise(node: ast.AST) -> TypeIs[ast.Raise]:
        """`Be.Raise` matches `class` `ast.Raise`.
        It has attributes `exc`, `cause`.
        This `class` is associated with Python keywords `raise`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Raise)

    @staticmethod
    def Return(node: ast.AST) -> TypeIs[ast.Return]:
        """`Be.Return` matches `class` `ast.Return`.
        It has attributes `value`.
        This `class` is associated with Python keywords `return`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Return)

    @staticmethod
    def RShift(node: ast.AST) -> TypeIs[ast.RShift]:
        """`Be.RShift`, Right Shift, matches any of `class` `ast.RShift` | `ast.RShift`.
        This `class` is associated with Python delimiters '>>=' and Python operators '>>'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.RShift)

    @staticmethod
    def Set(node: ast.AST) -> TypeIs[ast.Set]:
        """`Be.Set` matches `class` `ast.Set`.
        It has attributes `elts`.
        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Set)

    @staticmethod
    def SetComp(node: ast.AST) -> TypeIs[ast.SetComp]:
        """`Be.SetComp`, Set ***c***o***mp***rehension, matches `class` `ast.SetComp`.
        It has attributes `elt`, `generators`.
        This `class` is associated with Python delimiters '{}'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.SetComp)

    @staticmethod
    def Slice(node: ast.AST) -> TypeIs[ast.Slice]:
        """`Be.Slice` matches `class` `ast.Slice`.
        It has attributes `lower`, `upper`, `step`.
        This `class` is associated with Python delimiters '[], :'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Slice)

    @staticmethod
    def Starred(node: ast.AST) -> TypeIs[ast.Starred]:
        """`Be.Starred` matches `class` `ast.Starred`.
        It has attributes `value`, `ctx`.
        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Starred)

    @staticmethod
    def stmt(node: ast.AST) -> TypeIs[ast.stmt]:
        """`Be.stmt`, ***st***ate***m***en***t***, matches any of `class` `ast.stmt` | `ast.AnnAssign` | `ast.Assert` | `ast.Assign` | `ast.AsyncFor` | `ast.AsyncFunctionDef` | `ast.AsyncWith` | `ast.AugAssign` | `ast.Break` | `ast.ClassDef` | `ast.Continue` | `ast.Delete` | `ast.Expr` | `ast.For` | `ast.FunctionDef` | `ast.Global` | `ast.If` | `ast.Import` | `ast.ImportFrom` | `ast.Match` | `ast.Nonlocal` | `ast.Pass` | `ast.Raise` | `ast.Return` | `ast.Try` | `ast.TryStar` | `ast.TypeAlias` | `ast.While` | `ast.With`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.stmt)

    @staticmethod
    def Store(node: ast.AST) -> TypeIs[ast.Store]:
        """`Be.Store` matches `class` `ast.Store`.
        It is a subclass of `ast.expr_context`."""
        return isinstance(node, ast.Store)

    @staticmethod
    def Sub(node: ast.AST) -> TypeIs[ast.Sub]:
        """`Be.Sub`, ***Sub***traction, matches any of `class` `ast.Sub` | `ast.Sub`.
        This `class` is associated with Python delimiters '-=' and Python operators '-'.
        It is a subclass of `ast.operator`."""
        return isinstance(node, ast.Sub)

    @staticmethod
    def Subscript(node: ast.AST) -> TypeIs[ast.Subscript]:
        """`Be.Subscript` matches `class` `ast.Subscript`.
        It has attributes `value`, `slice`, `ctx`.
        This `class` is associated with Python delimiters '[]'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Subscript)

    @staticmethod
    def Try(node: ast.AST) -> TypeIs[ast.Try]:
        """`Be.Try` matches `class` `ast.Try`.
        It has attributes `body`, `handlers`, `orelse`, `finalbody`.
        This `class` is associated with Python keywords `try`, `except` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.Try)

    @staticmethod
    def TryStar(node: ast.AST) -> TypeIs[ast.TryStar]:
        """`Be.TryStar`, Try executing this, protected by `except*` ("except star"), matches `class` `ast.TryStar`.
        It has attributes `body`, `handlers`, `orelse`, `finalbody`.
        This `class` is associated with Python keywords `try`, `except*` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.TryStar)

    @staticmethod
    def Tuple(node: ast.AST) -> TypeIs[ast.Tuple]:
        """`Be.Tuple` matches `class` `ast.Tuple`.
        It has attributes `elts`, `ctx`.
        This `class` is associated with Python delimiters '()'.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Tuple)

    @staticmethod
    def type_ignore(node: ast.AST) -> TypeIs[ast.type_ignore]:
        """`Be.type_ignore`, this `type` error, you ignore it, matches any of `class` `ast.type_ignore` | `ast.TypeIgnore`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.type_ignore)

    @staticmethod
    def type_param(node: ast.AST) -> TypeIs[ast.type_param]:
        """`Be.type_param`, type ***param***eter, matches any of `class` `ast.type_param` | `ast.ParamSpec` | `ast.TypeVar` | `ast.TypeVarTuple`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.type_param)

    @staticmethod
    def TypeAlias(node: ast.AST) -> TypeIs[ast.TypeAlias]:
        """`Be.TypeAlias`, Type Alias, matches `class` `ast.TypeAlias`.
        It has attributes `name`, `type_params`, `value`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.TypeAlias)

    @staticmethod
    def TypeIgnore(node: ast.AST) -> TypeIs[ast.TypeIgnore]:
        """`Be.TypeIgnore`, this Type (`type`) error, Ignore it, matches `class` `ast.TypeIgnore`.
        It has attributes `lineno`, `tag`.
        This `class` is associated with Python delimiters ':'.
        It is a subclass of `ast.type_ignore`."""
        return isinstance(node, ast.TypeIgnore)

    @staticmethod
    def TypeVar(node: ast.AST) -> TypeIs[ast.TypeVar]:
        """`Be.TypeVar`, Type ***Var***iable, matches `class` `ast.TypeVar`.
        It has attributes `name`, `bound`, `default_value`.
        It is a subclass of `ast.type_param`."""
        return isinstance(node, ast.TypeVar)

    @staticmethod
    def TypeVarTuple(node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
        """`Be.TypeVarTuple`, Type ***Var***iable ***Tuple***, matches `class` `ast.TypeVarTuple`.
        It has attributes `name`, `default_value`.
        This `class` is associated with Python operators '*'.
        It is a subclass of `ast.type_param`."""
        return isinstance(node, ast.TypeVarTuple)

    @staticmethod
    def UAdd(node: ast.AST) -> TypeIs[ast.UAdd]:
        """`Be.UAdd`, ***U***nary ***Add***ition, matches `class` `ast.UAdd`.
        This `class` is associated with Python operators '+'.
        It is a subclass of `ast.unaryop`."""
        return isinstance(node, ast.UAdd)

    @staticmethod
    def unaryop(node: ast.AST) -> TypeIs[ast.unaryop]:
        """`Be.unaryop`, ***un***ary ***op***erator, matches any of `class` `ast.unaryop` | `ast.Invert` | `ast.Not` | `ast.UAdd` | `ast.USub`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.unaryop)

    @staticmethod
    def UnaryOp(node: ast.AST) -> TypeIs[ast.UnaryOp]:
        """`Be.UnaryOp`, ***Un***ary ***Op***eration, matches `class` `ast.UnaryOp`.
        It has attributes `op`, `operand`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.UnaryOp)

    @staticmethod
    def USub(node: ast.AST) -> TypeIs[ast.USub]:
        """`Be.USub`, ***U***nary ***Sub***traction, matches `class` `ast.USub`.
        This `class` is associated with Python operators '-'.
        It is a subclass of `ast.unaryop`."""
        return isinstance(node, ast.USub)

    @staticmethod
    def While(node: ast.AST) -> TypeIs[ast.While]:
        """`Be.While` matches `class` `ast.While`.
        It has attributes `test`, `body`, `orelse`.
        This `class` is associated with Python keywords `while`.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.While)

    @staticmethod
    def With(node: ast.AST) -> TypeIs[ast.With]:
        """`Be.With` matches `class` `ast.With`.
        It has attributes `items`, `body`, `type_comment`.
        This `class` is associated with Python keywords `with` and Python delimiters ':'.
        It is a subclass of `ast.stmt`."""
        return isinstance(node, ast.With)

    @staticmethod
    def withitem(node: ast.AST) -> TypeIs[ast.withitem]:
        """`Be.withitem`, with item, matches `class` `ast.withitem`.
        It has attributes `context_expr`, `optional_vars`.
        This `class` is associated with Python keywords `as`.
        It is a subclass of `ast.AST`."""
        return isinstance(node, ast.withitem)

    @staticmethod
    def Yield(node: ast.AST) -> TypeIs[ast.Yield]:
        """`Be.Yield`, Yield an element, matches `class` `ast.Yield`.
        It has attributes `value`.
        This `class` is associated with Python keywords `yield`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.Yield)

    @staticmethod
    def YieldFrom(node: ast.AST) -> TypeIs[ast.YieldFrom]:
        """`Be.YieldFrom`, Yield an element From, matches `class` `ast.YieldFrom`.
        It has attributes `value`.
        This `class` is associated with Python keywords `yield from`.
        It is a subclass of `ast.expr`."""
        return isinstance(node, ast.YieldFrom)