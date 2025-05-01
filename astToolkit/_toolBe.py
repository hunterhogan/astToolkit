"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import astDOTTryStar, astDOTParamSpec, astDOTtype_param, astDOTTypeAlias, astDOTTypeVar, astDOTTypeVarTuple
from typing import TypeGuard
import ast

class Be:
    """
	Provide type-guard functions for safely verifying AST node types during manipulation.

	The be class contains static methods that perform runtime type verification of AST nodes, returning TypeGuard
	results that enable static type checkers to narrow node types in conditional branches. These type-guards:

	1. Improve code safety by preventing operations on incompatible node types.
	2. Enable IDE tooling to provide better autocompletion and error detection.
	3. Document expected node types in a way that is enforced by the type system.
	4. Support pattern-matching workflows where node types must be verified before access.

	When used with conditional statements, these type-guards allow for precise, type-safe manipulation of AST nodes
	while maintaining full static type checking capabilities, even in complex transformation scenarios.
	"""

    @staticmethod
    def Add(node: ast.AST) -> TypeGuard[ast.Add]:
        return isinstance(node, ast.Add)

    @staticmethod
    def alias(node: ast.AST) -> TypeGuard[ast.alias]:
        return isinstance(node, ast.alias)

    @staticmethod
    def And(node: ast.AST) -> TypeGuard[ast.And]:
        return isinstance(node, ast.And)

    @staticmethod
    def AnnAssign(node: ast.AST) -> TypeGuard[ast.AnnAssign]:
        return isinstance(node, ast.AnnAssign)

    @staticmethod
    def arg(node: ast.AST) -> TypeGuard[ast.arg]:
        return isinstance(node, ast.arg)

    @staticmethod
    def arguments(node: ast.AST) -> TypeGuard[ast.arguments]:
        return isinstance(node, ast.arguments)

    @staticmethod
    def Assert(node: ast.AST) -> TypeGuard[ast.Assert]:
        return isinstance(node, ast.Assert)

    @staticmethod
    def Assign(node: ast.AST) -> TypeGuard[ast.Assign]:
        return isinstance(node, ast.Assign)

    @staticmethod
    def AST(node: ast.AST) -> TypeGuard[ast.AST]:
        return isinstance(node, ast.AST)

    @staticmethod
    def AsyncFor(node: ast.AST) -> TypeGuard[ast.AsyncFor]:
        return isinstance(node, ast.AsyncFor)

    @staticmethod
    def AsyncFunctionDef(node: ast.AST) -> TypeGuard[ast.AsyncFunctionDef]:
        return isinstance(node, ast.AsyncFunctionDef)

    @staticmethod
    def AsyncWith(node: ast.AST) -> TypeGuard[ast.AsyncWith]:
        return isinstance(node, ast.AsyncWith)

    @staticmethod
    def Attribute(node: ast.AST) -> TypeGuard[ast.Attribute]:
        return isinstance(node, ast.Attribute)

    @staticmethod
    def AugAssign(node: ast.AST) -> TypeGuard[ast.AugAssign]:
        return isinstance(node, ast.AugAssign)

    @staticmethod
    def Await(node: ast.AST) -> TypeGuard[ast.Await]:
        return isinstance(node, ast.Await)

    @staticmethod
    def BinOp(node: ast.AST) -> TypeGuard[ast.BinOp]:
        return isinstance(node, ast.BinOp)

    @staticmethod
    def BitAnd(node: ast.AST) -> TypeGuard[ast.BitAnd]:
        return isinstance(node, ast.BitAnd)

    @staticmethod
    def BitOr(node: ast.AST) -> TypeGuard[ast.BitOr]:
        return isinstance(node, ast.BitOr)

    @staticmethod
    def BitXor(node: ast.AST) -> TypeGuard[ast.BitXor]:
        return isinstance(node, ast.BitXor)

    @staticmethod
    def BoolOp(node: ast.AST) -> TypeGuard[ast.BoolOp]:
        return isinstance(node, ast.BoolOp)

    @staticmethod
    def boolop(node: ast.AST) -> TypeGuard[ast.boolop]:
        return isinstance(node, ast.boolop)

    @staticmethod
    def Break(node: ast.AST) -> TypeGuard[ast.Break]:
        return isinstance(node, ast.Break)

    @staticmethod
    def Call(node: ast.AST) -> TypeGuard[ast.Call]:
        return isinstance(node, ast.Call)

    @staticmethod
    def ClassDef(node: ast.AST) -> TypeGuard[ast.ClassDef]:
        return isinstance(node, ast.ClassDef)

    @staticmethod
    def cmpop(node: ast.AST) -> TypeGuard[ast.cmpop]:
        return isinstance(node, ast.cmpop)

    @staticmethod
    def Compare(node: ast.AST) -> TypeGuard[ast.Compare]:
        return isinstance(node, ast.Compare)

    @staticmethod
    def comprehension(node: ast.AST) -> TypeGuard[ast.comprehension]:
        return isinstance(node, ast.comprehension)

    @staticmethod
    def Constant(node: ast.AST) -> TypeGuard[ast.Constant]:
        return isinstance(node, ast.Constant)

    @staticmethod
    def Continue(node: ast.AST) -> TypeGuard[ast.Continue]:
        return isinstance(node, ast.Continue)

    @staticmethod
    def Del(node: ast.AST) -> TypeGuard[ast.Del]:
        return isinstance(node, ast.Del)

    @staticmethod
    def Delete(node: ast.AST) -> TypeGuard[ast.Delete]:
        return isinstance(node, ast.Delete)

    @staticmethod
    def Dict(node: ast.AST) -> TypeGuard[ast.Dict]:
        return isinstance(node, ast.Dict)

    @staticmethod
    def DictComp(node: ast.AST) -> TypeGuard[ast.DictComp]:
        return isinstance(node, ast.DictComp)

    @staticmethod
    def Div(node: ast.AST) -> TypeGuard[ast.Div]:
        return isinstance(node, ast.Div)

    @staticmethod
    def Eq(node: ast.AST) -> TypeGuard[ast.Eq]:
        return isinstance(node, ast.Eq)

    @staticmethod
    def excepthandler(node: ast.AST) -> TypeGuard[ast.excepthandler]:
        return isinstance(node, ast.excepthandler)

    @staticmethod
    def ExceptHandler(node: ast.AST) -> TypeGuard[ast.ExceptHandler]:
        return isinstance(node, ast.ExceptHandler)

    @staticmethod
    def Expr(node: ast.AST) -> TypeGuard[ast.Expr]:
        return isinstance(node, ast.Expr)

    @staticmethod
    def expr(node: ast.AST) -> TypeGuard[ast.expr]:
        return isinstance(node, ast.expr)

    @staticmethod
    def expr_context(node: ast.AST) -> TypeGuard[ast.expr_context]:
        return isinstance(node, ast.expr_context)

    @staticmethod
    def Expression(node: ast.AST) -> TypeGuard[ast.Expression]:
        return isinstance(node, ast.Expression)

    @staticmethod
    def FloorDiv(node: ast.AST) -> TypeGuard[ast.FloorDiv]:
        return isinstance(node, ast.FloorDiv)

    @staticmethod
    def For(node: ast.AST) -> TypeGuard[ast.For]:
        return isinstance(node, ast.For)

    @staticmethod
    def FormattedValue(node: ast.AST) -> TypeGuard[ast.FormattedValue]:
        return isinstance(node, ast.FormattedValue)

    @staticmethod
    def FunctionDef(node: ast.AST) -> TypeGuard[ast.FunctionDef]:
        return isinstance(node, ast.FunctionDef)

    @staticmethod
    def FunctionType(node: ast.AST) -> TypeGuard[ast.FunctionType]:
        return isinstance(node, ast.FunctionType)

    @staticmethod
    def GeneratorExp(node: ast.AST) -> TypeGuard[ast.GeneratorExp]:
        return isinstance(node, ast.GeneratorExp)

    @staticmethod
    def Global(node: ast.AST) -> TypeGuard[ast.Global]:
        return isinstance(node, ast.Global)

    @staticmethod
    def Gt(node: ast.AST) -> TypeGuard[ast.Gt]:
        return isinstance(node, ast.Gt)

    @staticmethod
    def GtE(node: ast.AST) -> TypeGuard[ast.GtE]:
        return isinstance(node, ast.GtE)

    @staticmethod
    def If(node: ast.AST) -> TypeGuard[ast.If]:
        return isinstance(node, ast.If)

    @staticmethod
    def IfExp(node: ast.AST) -> TypeGuard[ast.IfExp]:
        return isinstance(node, ast.IfExp)

    @staticmethod
    def Import(node: ast.AST) -> TypeGuard[ast.Import]:
        return isinstance(node, ast.Import)

    @staticmethod
    def ImportFrom(node: ast.AST) -> TypeGuard[ast.ImportFrom]:
        return isinstance(node, ast.ImportFrom)

    @staticmethod
    def In(node: ast.AST) -> TypeGuard[ast.In]:
        return isinstance(node, ast.In)

    @staticmethod
    def Interactive(node: ast.AST) -> TypeGuard[ast.Interactive]:
        return isinstance(node, ast.Interactive)

    @staticmethod
    def Invert(node: ast.AST) -> TypeGuard[ast.Invert]:
        return isinstance(node, ast.Invert)

    @staticmethod
    def Is(node: ast.AST) -> TypeGuard[ast.Is]:
        return isinstance(node, ast.Is)

    @staticmethod
    def IsNot(node: ast.AST) -> TypeGuard[ast.IsNot]:
        return isinstance(node, ast.IsNot)

    @staticmethod
    def JoinedStr(node: ast.AST) -> TypeGuard[ast.JoinedStr]:
        return isinstance(node, ast.JoinedStr)

    @staticmethod
    def keyword(node: ast.AST) -> TypeGuard[ast.keyword]:
        return isinstance(node, ast.keyword)

    @staticmethod
    def Lambda(node: ast.AST) -> TypeGuard[ast.Lambda]:
        return isinstance(node, ast.Lambda)

    @staticmethod
    def List(node: ast.AST) -> TypeGuard[ast.List]:
        return isinstance(node, ast.List)

    @staticmethod
    def ListComp(node: ast.AST) -> TypeGuard[ast.ListComp]:
        return isinstance(node, ast.ListComp)

    @staticmethod
    def Load(node: ast.AST) -> TypeGuard[ast.Load]:
        return isinstance(node, ast.Load)

    @staticmethod
    def LShift(node: ast.AST) -> TypeGuard[ast.LShift]:
        return isinstance(node, ast.LShift)

    @staticmethod
    def Lt(node: ast.AST) -> TypeGuard[ast.Lt]:
        return isinstance(node, ast.Lt)

    @staticmethod
    def LtE(node: ast.AST) -> TypeGuard[ast.LtE]:
        return isinstance(node, ast.LtE)

    @staticmethod
    def Match(node: ast.AST) -> TypeGuard[ast.Match]:
        return isinstance(node, ast.Match)

    @staticmethod
    def match_case(node: ast.AST) -> TypeGuard[ast.match_case]:
        return isinstance(node, ast.match_case)

    @staticmethod
    def MatchAs(node: ast.AST) -> TypeGuard[ast.MatchAs]:
        return isinstance(node, ast.MatchAs)

    @staticmethod
    def MatchClass(node: ast.AST) -> TypeGuard[ast.MatchClass]:
        return isinstance(node, ast.MatchClass)

    @staticmethod
    def MatchMapping(node: ast.AST) -> TypeGuard[ast.MatchMapping]:
        return isinstance(node, ast.MatchMapping)

    @staticmethod
    def MatchOr(node: ast.AST) -> TypeGuard[ast.MatchOr]:
        return isinstance(node, ast.MatchOr)

    @staticmethod
    def MatchSequence(node: ast.AST) -> TypeGuard[ast.MatchSequence]:
        return isinstance(node, ast.MatchSequence)

    @staticmethod
    def MatchSingleton(node: ast.AST) -> TypeGuard[ast.MatchSingleton]:
        return isinstance(node, ast.MatchSingleton)

    @staticmethod
    def MatchStar(node: ast.AST) -> TypeGuard[ast.MatchStar]:
        return isinstance(node, ast.MatchStar)

    @staticmethod
    def MatchValue(node: ast.AST) -> TypeGuard[ast.MatchValue]:
        return isinstance(node, ast.MatchValue)

    @staticmethod
    def MatMult(node: ast.AST) -> TypeGuard[ast.MatMult]:
        return isinstance(node, ast.MatMult)

    @staticmethod
    def mod(node: ast.AST) -> TypeGuard[ast.mod]:
        return isinstance(node, ast.mod)

    @staticmethod
    def Mod(node: ast.AST) -> TypeGuard[ast.Mod]:
        return isinstance(node, ast.Mod)

    @staticmethod
    def Module(node: ast.AST) -> TypeGuard[ast.Module]:
        return isinstance(node, ast.Module)

    @staticmethod
    def Mult(node: ast.AST) -> TypeGuard[ast.Mult]:
        return isinstance(node, ast.Mult)

    @staticmethod
    def Name(node: ast.AST) -> TypeGuard[ast.Name]:
        return isinstance(node, ast.Name)

    @staticmethod
    def NamedExpr(node: ast.AST) -> TypeGuard[ast.NamedExpr]:
        return isinstance(node, ast.NamedExpr)

    @staticmethod
    def Nonlocal(node: ast.AST) -> TypeGuard[ast.Nonlocal]:
        return isinstance(node, ast.Nonlocal)

    @staticmethod
    def Not(node: ast.AST) -> TypeGuard[ast.Not]:
        return isinstance(node, ast.Not)

    @staticmethod
    def NotEq(node: ast.AST) -> TypeGuard[ast.NotEq]:
        return isinstance(node, ast.NotEq)

    @staticmethod
    def NotIn(node: ast.AST) -> TypeGuard[ast.NotIn]:
        return isinstance(node, ast.NotIn)

    @staticmethod
    def operator(node: ast.AST) -> TypeGuard[ast.operator]:
        return isinstance(node, ast.operator)

    @staticmethod
    def Or(node: ast.AST) -> TypeGuard[ast.Or]:
        return isinstance(node, ast.Or)

    @staticmethod
    def ParamSpec(node: ast.AST) -> TypeGuard[astDOTParamSpec]:
        return isinstance(node, astDOTParamSpec)

    @staticmethod
    def Pass(node: ast.AST) -> TypeGuard[ast.Pass]:
        return isinstance(node, ast.Pass)

    @staticmethod
    def pattern(node: ast.AST) -> TypeGuard[ast.pattern]:
        return isinstance(node, ast.pattern)

    @staticmethod
    def Pow(node: ast.AST) -> TypeGuard[ast.Pow]:
        return isinstance(node, ast.Pow)

    @staticmethod
    def Raise(node: ast.AST) -> TypeGuard[ast.Raise]:
        return isinstance(node, ast.Raise)

    @staticmethod
    def Return(node: ast.AST) -> TypeGuard[ast.Return]:
        return isinstance(node, ast.Return)

    @staticmethod
    def RShift(node: ast.AST) -> TypeGuard[ast.RShift]:
        return isinstance(node, ast.RShift)

    @staticmethod
    def Set(node: ast.AST) -> TypeGuard[ast.Set]:
        return isinstance(node, ast.Set)

    @staticmethod
    def SetComp(node: ast.AST) -> TypeGuard[ast.SetComp]:
        return isinstance(node, ast.SetComp)

    @staticmethod
    def Slice(node: ast.AST) -> TypeGuard[ast.Slice]:
        return isinstance(node, ast.Slice)

    @staticmethod
    def Starred(node: ast.AST) -> TypeGuard[ast.Starred]:
        return isinstance(node, ast.Starred)

    @staticmethod
    def stmt(node: ast.AST) -> TypeGuard[ast.stmt]:
        return isinstance(node, ast.stmt)

    @staticmethod
    def Store(node: ast.AST) -> TypeGuard[ast.Store]:
        return isinstance(node, ast.Store)

    @staticmethod
    def Sub(node: ast.AST) -> TypeGuard[ast.Sub]:
        return isinstance(node, ast.Sub)

    @staticmethod
    def Subscript(node: ast.AST) -> TypeGuard[ast.Subscript]:
        return isinstance(node, ast.Subscript)

    @staticmethod
    def Try(node: ast.AST) -> TypeGuard[ast.Try]:
        return isinstance(node, ast.Try)

    @staticmethod
    def TryStar(node: ast.AST) -> TypeGuard[astDOTTryStar]:
        return isinstance(node, astDOTTryStar)

    @staticmethod
    def Tuple(node: ast.AST) -> TypeGuard[ast.Tuple]:
        return isinstance(node, ast.Tuple)

    @staticmethod
    def type_ignore(node: ast.AST) -> TypeGuard[ast.type_ignore]:
        return isinstance(node, ast.type_ignore)

    @staticmethod
    def type_param(node: ast.AST) -> TypeGuard[astDOTtype_param]:
        return isinstance(node, astDOTtype_param)

    @staticmethod
    def TypeAlias(node: ast.AST) -> TypeGuard[astDOTTypeAlias]:
        return isinstance(node, astDOTTypeAlias)

    @staticmethod
    def TypeIgnore(node: ast.AST) -> TypeGuard[ast.TypeIgnore]:
        return isinstance(node, ast.TypeIgnore)

    @staticmethod
    def TypeVar(node: ast.AST) -> TypeGuard[astDOTTypeVar]:
        return isinstance(node, astDOTTypeVar)

    @staticmethod
    def TypeVarTuple(node: ast.AST) -> TypeGuard[astDOTTypeVarTuple]:
        return isinstance(node, astDOTTypeVarTuple)

    @staticmethod
    def UAdd(node: ast.AST) -> TypeGuard[ast.UAdd]:
        return isinstance(node, ast.UAdd)

    @staticmethod
    def UnaryOp(node: ast.AST) -> TypeGuard[ast.UnaryOp]:
        return isinstance(node, ast.UnaryOp)

    @staticmethod
    def unaryop(node: ast.AST) -> TypeGuard[ast.unaryop]:
        return isinstance(node, ast.unaryop)

    @staticmethod
    def USub(node: ast.AST) -> TypeGuard[ast.USub]:
        return isinstance(node, ast.USub)

    @staticmethod
    def While(node: ast.AST) -> TypeGuard[ast.While]:
        return isinstance(node, ast.While)

    @staticmethod
    def With(node: ast.AST) -> TypeGuard[ast.With]:
        return isinstance(node, ast.With)

    @staticmethod
    def withitem(node: ast.AST) -> TypeGuard[ast.withitem]:
        return isinstance(node, ast.withitem)

    @staticmethod
    def Yield(node: ast.AST) -> TypeGuard[ast.Yield]:
        return isinstance(node, ast.Yield)

    @staticmethod
    def YieldFrom(node: ast.AST) -> TypeGuard[ast.YieldFrom]:
        return isinstance(node, ast.YieldFrom)