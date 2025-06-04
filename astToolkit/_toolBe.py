"""This file is generated automatically, so changes to this file will be lost."""
from typing_extensions import TypeIs
import ast

class Be:
    """Type guard functions for safe AST node identification and type narrowing.
    (AI generated docstring)

    Provides static methods that perform runtime type checking for all AST node types
    while enabling compile-time type narrowing through `TypeIs` annotations. Forms
    the foundation of type-safe AST analysis and transformation throughout the toolkit.

    Each method takes an `ast.AST` node and returns a `TypeIs` that confirms both
    runtime type safety and enables static type checkers to narrow the node type in
    conditional contexts. This eliminates the need for unsafe casting while providing
    comprehensive coverage of Python's AST node hierarchy.

    Methods correspond directly to Python AST node types, following the naming convention
    of the AST classes themselves. Coverage includes expression nodes (`Add`, `Call`,
    `Name`), statement nodes (`Assign`, `FunctionDef`, `Return`), operator nodes
    (`And`, `Or`, `Not`), and structural nodes (`Module`, `arguments`, `keyword`).

    The class serves as the primary type-checking component in the antecedent-action
    pattern, where predicates identify target nodes and actions specify operations.
    Type guards from this class are commonly used as building blocks in `IfThis`
    predicates and directly as `findThis` parameters in visitor classes.

    Parameters:

        node: AST node to test for specific type membership

    Returns:

        typeIs: `TypeIs` enabling both runtime validation and static type narrowing

    Examples:

        Type-safe node processing with automatic type narrowing:

            if Be.FunctionDef(node):
                functionName = node.name  # Type-safe access to name attribute
                parameterCount = len(node.args.args)

        Building complex predicates for visitor patterns:

            NodeTourist(Be.Return, Then.extractIt(DOT.value)).visit(functionNode)

        Combining type guards in conditional logic:

            if Be.Call(node) and Be.Name(node.func):
                callableName = node.func.id  # Type-safe access to function name
    """

    @staticmethod
    def Add(node: ast.AST) -> TypeIs[ast.Add]:
        return isinstance(node, ast.Add)

    @staticmethod
    def alias(node: ast.AST) -> TypeIs[ast.alias]:
        return isinstance(node, ast.alias)

    @staticmethod
    def And(node: ast.AST) -> TypeIs[ast.And]:
        return isinstance(node, ast.And)

    @staticmethod
    def AnnAssign(node: ast.AST) -> TypeIs[ast.AnnAssign]:
        return isinstance(node, ast.AnnAssign)

    @staticmethod
    def arg(node: ast.AST) -> TypeIs[ast.arg]:
        return isinstance(node, ast.arg)

    @staticmethod
    def arguments(node: ast.AST) -> TypeIs[ast.arguments]:
        return isinstance(node, ast.arguments)

    @staticmethod
    def Assert(node: ast.AST) -> TypeIs[ast.Assert]:
        return isinstance(node, ast.Assert)

    @staticmethod
    def Assign(node: ast.AST) -> TypeIs[ast.Assign]:
        return isinstance(node, ast.Assign)

    @staticmethod
    def AST(node: ast.AST) -> TypeIs[ast.AST]:
        return isinstance(node, ast.AST)

    @staticmethod
    def AsyncFor(node: ast.AST) -> TypeIs[ast.AsyncFor]:
        return isinstance(node, ast.AsyncFor)

    @staticmethod
    def AsyncFunctionDef(node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
        return isinstance(node, ast.AsyncFunctionDef)

    @staticmethod
    def AsyncWith(node: ast.AST) -> TypeIs[ast.AsyncWith]:
        return isinstance(node, ast.AsyncWith)

    @staticmethod
    def Attribute(node: ast.AST) -> TypeIs[ast.Attribute]:
        return isinstance(node, ast.Attribute)

    @staticmethod
    def AugAssign(node: ast.AST) -> TypeIs[ast.AugAssign]:
        return isinstance(node, ast.AugAssign)

    @staticmethod
    def Await(node: ast.AST) -> TypeIs[ast.Await]:
        return isinstance(node, ast.Await)

    @staticmethod
    def BinOp(node: ast.AST) -> TypeIs[ast.BinOp]:
        return isinstance(node, ast.BinOp)

    @staticmethod
    def BitAnd(node: ast.AST) -> TypeIs[ast.BitAnd]:
        return isinstance(node, ast.BitAnd)

    @staticmethod
    def BitOr(node: ast.AST) -> TypeIs[ast.BitOr]:
        return isinstance(node, ast.BitOr)

    @staticmethod
    def BitXor(node: ast.AST) -> TypeIs[ast.BitXor]:
        return isinstance(node, ast.BitXor)

    @staticmethod
    def boolop(node: ast.AST) -> TypeIs[ast.boolop]:
        return isinstance(node, ast.boolop)

    @staticmethod
    def BoolOp(node: ast.AST) -> TypeIs[ast.BoolOp]:
        return isinstance(node, ast.BoolOp)

    @staticmethod
    def Break(node: ast.AST) -> TypeIs[ast.Break]:
        return isinstance(node, ast.Break)

    @staticmethod
    def Call(node: ast.AST) -> TypeIs[ast.Call]:
        return isinstance(node, ast.Call)

    @staticmethod
    def ClassDef(node: ast.AST) -> TypeIs[ast.ClassDef]:
        return isinstance(node, ast.ClassDef)

    @staticmethod
    def cmpop(node: ast.AST) -> TypeIs[ast.cmpop]:
        return isinstance(node, ast.cmpop)

    @staticmethod
    def Compare(node: ast.AST) -> TypeIs[ast.Compare]:
        return isinstance(node, ast.Compare)

    @staticmethod
    def comprehension(node: ast.AST) -> TypeIs[ast.comprehension]:
        return isinstance(node, ast.comprehension)

    @staticmethod
    def Constant(node: ast.AST) -> TypeIs[ast.Constant]:
        return isinstance(node, ast.Constant)

    @staticmethod
    def Continue(node: ast.AST) -> TypeIs[ast.Continue]:
        return isinstance(node, ast.Continue)

    @staticmethod
    def Del(node: ast.AST) -> TypeIs[ast.Del]:
        return isinstance(node, ast.Del)

    @staticmethod
    def Delete(node: ast.AST) -> TypeIs[ast.Delete]:
        return isinstance(node, ast.Delete)

    @staticmethod
    def Dict(node: ast.AST) -> TypeIs[ast.Dict]:
        return isinstance(node, ast.Dict)

    @staticmethod
    def DictComp(node: ast.AST) -> TypeIs[ast.DictComp]:
        return isinstance(node, ast.DictComp)

    @staticmethod
    def Div(node: ast.AST) -> TypeIs[ast.Div]:
        return isinstance(node, ast.Div)

    @staticmethod
    def Eq(node: ast.AST) -> TypeIs[ast.Eq]:
        return isinstance(node, ast.Eq)

    @staticmethod
    def excepthandler(node: ast.AST) -> TypeIs[ast.excepthandler]:
        return isinstance(node, ast.excepthandler)

    @staticmethod
    def ExceptHandler(node: ast.AST) -> TypeIs[ast.ExceptHandler]:
        return isinstance(node, ast.ExceptHandler)

    @staticmethod
    def expr(node: ast.AST) -> TypeIs[ast.expr]:
        return isinstance(node, ast.expr)

    @staticmethod
    def Expr(node: ast.AST) -> TypeIs[ast.Expr]:
        return isinstance(node, ast.Expr)

    @staticmethod
    def expr_context(node: ast.AST) -> TypeIs[ast.expr_context]:
        return isinstance(node, ast.expr_context)

    @staticmethod
    def Expression(node: ast.AST) -> TypeIs[ast.Expression]:
        return isinstance(node, ast.Expression)

    @staticmethod
    def FloorDiv(node: ast.AST) -> TypeIs[ast.FloorDiv]:
        return isinstance(node, ast.FloorDiv)

    @staticmethod
    def For(node: ast.AST) -> TypeIs[ast.For]:
        return isinstance(node, ast.For)

    @staticmethod
    def FormattedValue(node: ast.AST) -> TypeIs[ast.FormattedValue]:
        return isinstance(node, ast.FormattedValue)

    @staticmethod
    def FunctionDef(node: ast.AST) -> TypeIs[ast.FunctionDef]:
        return isinstance(node, ast.FunctionDef)

    @staticmethod
    def FunctionType(node: ast.AST) -> TypeIs[ast.FunctionType]:
        return isinstance(node, ast.FunctionType)

    @staticmethod
    def GeneratorExp(node: ast.AST) -> TypeIs[ast.GeneratorExp]:
        return isinstance(node, ast.GeneratorExp)

    @staticmethod
    def Global(node: ast.AST) -> TypeIs[ast.Global]:
        return isinstance(node, ast.Global)

    @staticmethod
    def Gt(node: ast.AST) -> TypeIs[ast.Gt]:
        return isinstance(node, ast.Gt)

    @staticmethod
    def GtE(node: ast.AST) -> TypeIs[ast.GtE]:
        return isinstance(node, ast.GtE)

    @staticmethod
    def If(node: ast.AST) -> TypeIs[ast.If]:
        return isinstance(node, ast.If)

    @staticmethod
    def IfExp(node: ast.AST) -> TypeIs[ast.IfExp]:
        return isinstance(node, ast.IfExp)

    @staticmethod
    def Import(node: ast.AST) -> TypeIs[ast.Import]:
        return isinstance(node, ast.Import)

    @staticmethod
    def ImportFrom(node: ast.AST) -> TypeIs[ast.ImportFrom]:
        return isinstance(node, ast.ImportFrom)

    @staticmethod
    def In(node: ast.AST) -> TypeIs[ast.In]:
        return isinstance(node, ast.In)

    @staticmethod
    def Interactive(node: ast.AST) -> TypeIs[ast.Interactive]:
        return isinstance(node, ast.Interactive)

    @staticmethod
    def Invert(node: ast.AST) -> TypeIs[ast.Invert]:
        return isinstance(node, ast.Invert)

    @staticmethod
    def Is(node: ast.AST) -> TypeIs[ast.Is]:
        return isinstance(node, ast.Is)

    @staticmethod
    def IsNot(node: ast.AST) -> TypeIs[ast.IsNot]:
        return isinstance(node, ast.IsNot)

    @staticmethod
    def JoinedStr(node: ast.AST) -> TypeIs[ast.JoinedStr]:
        return isinstance(node, ast.JoinedStr)

    @staticmethod
    def keyword(node: ast.AST) -> TypeIs[ast.keyword]:
        return isinstance(node, ast.keyword)

    @staticmethod
    def Lambda(node: ast.AST) -> TypeIs[ast.Lambda]:
        return isinstance(node, ast.Lambda)

    @staticmethod
    def List(node: ast.AST) -> TypeIs[ast.List]:
        return isinstance(node, ast.List)

    @staticmethod
    def ListComp(node: ast.AST) -> TypeIs[ast.ListComp]:
        return isinstance(node, ast.ListComp)

    @staticmethod
    def Load(node: ast.AST) -> TypeIs[ast.Load]:
        return isinstance(node, ast.Load)

    @staticmethod
    def LShift(node: ast.AST) -> TypeIs[ast.LShift]:
        return isinstance(node, ast.LShift)

    @staticmethod
    def Lt(node: ast.AST) -> TypeIs[ast.Lt]:
        return isinstance(node, ast.Lt)

    @staticmethod
    def LtE(node: ast.AST) -> TypeIs[ast.LtE]:
        return isinstance(node, ast.LtE)

    @staticmethod
    def Match(node: ast.AST) -> TypeIs[ast.Match]:
        return isinstance(node, ast.Match)

    @staticmethod
    def match_case(node: ast.AST) -> TypeIs[ast.match_case]:
        return isinstance(node, ast.match_case)

    @staticmethod
    def MatchAs(node: ast.AST) -> TypeIs[ast.MatchAs]:
        return isinstance(node, ast.MatchAs)

    @staticmethod
    def MatchClass(node: ast.AST) -> TypeIs[ast.MatchClass]:
        return isinstance(node, ast.MatchClass)

    @staticmethod
    def MatchMapping(node: ast.AST) -> TypeIs[ast.MatchMapping]:
        return isinstance(node, ast.MatchMapping)

    @staticmethod
    def MatchOr(node: ast.AST) -> TypeIs[ast.MatchOr]:
        return isinstance(node, ast.MatchOr)

    @staticmethod
    def MatchSequence(node: ast.AST) -> TypeIs[ast.MatchSequence]:
        return isinstance(node, ast.MatchSequence)

    @staticmethod
    def MatchSingleton(node: ast.AST) -> TypeIs[ast.MatchSingleton]:
        return isinstance(node, ast.MatchSingleton)

    @staticmethod
    def MatchStar(node: ast.AST) -> TypeIs[ast.MatchStar]:
        return isinstance(node, ast.MatchStar)

    @staticmethod
    def MatchValue(node: ast.AST) -> TypeIs[ast.MatchValue]:
        return isinstance(node, ast.MatchValue)

    @staticmethod
    def MatMult(node: ast.AST) -> TypeIs[ast.MatMult]:
        return isinstance(node, ast.MatMult)

    @staticmethod
    def mod(node: ast.AST) -> TypeIs[ast.mod]:
        return isinstance(node, ast.mod)

    @staticmethod
    def Mod(node: ast.AST) -> TypeIs[ast.Mod]:
        return isinstance(node, ast.Mod)

    @staticmethod
    def Module(node: ast.AST) -> TypeIs[ast.Module]:
        return isinstance(node, ast.Module)

    @staticmethod
    def Mult(node: ast.AST) -> TypeIs[ast.Mult]:
        return isinstance(node, ast.Mult)

    @staticmethod
    def Name(node: ast.AST) -> TypeIs[ast.Name]:
        return isinstance(node, ast.Name)

    @staticmethod
    def NamedExpr(node: ast.AST) -> TypeIs[ast.NamedExpr]:
        return isinstance(node, ast.NamedExpr)

    @staticmethod
    def Nonlocal(node: ast.AST) -> TypeIs[ast.Nonlocal]:
        return isinstance(node, ast.Nonlocal)

    @staticmethod
    def Not(node: ast.AST) -> TypeIs[ast.Not]:
        return isinstance(node, ast.Not)

    @staticmethod
    def NotEq(node: ast.AST) -> TypeIs[ast.NotEq]:
        return isinstance(node, ast.NotEq)

    @staticmethod
    def NotIn(node: ast.AST) -> TypeIs[ast.NotIn]:
        return isinstance(node, ast.NotIn)

    @staticmethod
    def operator(node: ast.AST) -> TypeIs[ast.operator]:
        return isinstance(node, ast.operator)

    @staticmethod
    def Or(node: ast.AST) -> TypeIs[ast.Or]:
        return isinstance(node, ast.Or)

    @staticmethod
    def ParamSpec(node: ast.AST) -> TypeIs[ast.ParamSpec]:
        return isinstance(node, ast.ParamSpec)

    @staticmethod
    def Pass(node: ast.AST) -> TypeIs[ast.Pass]:
        return isinstance(node, ast.Pass)

    @staticmethod
    def pattern(node: ast.AST) -> TypeIs[ast.pattern]:
        return isinstance(node, ast.pattern)

    @staticmethod
    def Pow(node: ast.AST) -> TypeIs[ast.Pow]:
        return isinstance(node, ast.Pow)

    @staticmethod
    def Raise(node: ast.AST) -> TypeIs[ast.Raise]:
        return isinstance(node, ast.Raise)

    @staticmethod
    def Return(node: ast.AST) -> TypeIs[ast.Return]:
        return isinstance(node, ast.Return)

    @staticmethod
    def RShift(node: ast.AST) -> TypeIs[ast.RShift]:
        return isinstance(node, ast.RShift)

    @staticmethod
    def Set(node: ast.AST) -> TypeIs[ast.Set]:
        return isinstance(node, ast.Set)

    @staticmethod
    def SetComp(node: ast.AST) -> TypeIs[ast.SetComp]:
        return isinstance(node, ast.SetComp)

    @staticmethod
    def Slice(node: ast.AST) -> TypeIs[ast.Slice]:
        return isinstance(node, ast.Slice)

    @staticmethod
    def Starred(node: ast.AST) -> TypeIs[ast.Starred]:
        return isinstance(node, ast.Starred)

    @staticmethod
    def stmt(node: ast.AST) -> TypeIs[ast.stmt]:
        return isinstance(node, ast.stmt)

    @staticmethod
    def Store(node: ast.AST) -> TypeIs[ast.Store]:
        return isinstance(node, ast.Store)

    @staticmethod
    def Sub(node: ast.AST) -> TypeIs[ast.Sub]:
        return isinstance(node, ast.Sub)

    @staticmethod
    def Subscript(node: ast.AST) -> TypeIs[ast.Subscript]:
        return isinstance(node, ast.Subscript)

    @staticmethod
    def Try(node: ast.AST) -> TypeIs[ast.Try]:
        return isinstance(node, ast.Try)

    @staticmethod
    def TryStar(node: ast.AST) -> TypeIs[ast.TryStar]:
        return isinstance(node, ast.TryStar)

    @staticmethod
    def Tuple(node: ast.AST) -> TypeIs[ast.Tuple]:
        return isinstance(node, ast.Tuple)

    @staticmethod
    def type_ignore(node: ast.AST) -> TypeIs[ast.type_ignore]:
        return isinstance(node, ast.type_ignore)

    @staticmethod
    def type_param(node: ast.AST) -> TypeIs[ast.type_param]:
        return isinstance(node, ast.type_param)

    @staticmethod
    def TypeAlias(node: ast.AST) -> TypeIs[ast.TypeAlias]:
        return isinstance(node, ast.TypeAlias)

    @staticmethod
    def TypeIgnore(node: ast.AST) -> TypeIs[ast.TypeIgnore]:
        return isinstance(node, ast.TypeIgnore)

    @staticmethod
    def TypeVar(node: ast.AST) -> TypeIs[ast.TypeVar]:
        return isinstance(node, ast.TypeVar)

    @staticmethod
    def TypeVarTuple(node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
        return isinstance(node, ast.TypeVarTuple)

    @staticmethod
    def UAdd(node: ast.AST) -> TypeIs[ast.UAdd]:
        return isinstance(node, ast.UAdd)

    @staticmethod
    def unaryop(node: ast.AST) -> TypeIs[ast.unaryop]:
        return isinstance(node, ast.unaryop)

    @staticmethod
    def UnaryOp(node: ast.AST) -> TypeIs[ast.UnaryOp]:
        return isinstance(node, ast.UnaryOp)

    @staticmethod
    def USub(node: ast.AST) -> TypeIs[ast.USub]:
        return isinstance(node, ast.USub)

    @staticmethod
    def While(node: ast.AST) -> TypeIs[ast.While]:
        return isinstance(node, ast.While)

    @staticmethod
    def With(node: ast.AST) -> TypeIs[ast.With]:
        return isinstance(node, ast.With)

    @staticmethod
    def withitem(node: ast.AST) -> TypeIs[ast.withitem]:
        return isinstance(node, ast.withitem)

    @staticmethod
    def Yield(node: ast.AST) -> TypeIs[ast.Yield]:
        return isinstance(node, ast.Yield)

    @staticmethod
    def YieldFrom(node: ast.AST) -> TypeIs[ast.YieldFrom]:
        return isinstance(node, ast.YieldFrom)