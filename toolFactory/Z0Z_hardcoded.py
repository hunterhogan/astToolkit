from pathlib import Path
from typing import TypeAlias as typing_TypeAlias
import ast

ast_Identifier: typing_TypeAlias = str
str_nameDOTname: typing_TypeAlias = str

sys_version_infoMinimum: tuple[int, int] = (3, 10)
sys_version_infoTarget: tuple[int, int] = (3, 13)

listASTClassesPostPythonVersionMinimumHARDCODED: list[ast_Identifier] = ['astDOTParamSpec', 'astDOTTryStar', 'astDOTTypeAlias', 'astDOTTypeVar', 'astDOTTypeVarTuple', 'astDOTtype_param']
listASTClassesPostPythonVersionMinimum = listASTClassesPostPythonVersionMinimumHARDCODED

listASTSubclassesHARDCODED: list[str] = ['_Slice', 'AST', 'binaryop', 'boolop', 'cmpop', 'excepthandler', 'expr_context', 'expr', 'mod', 'operator', 'pattern', 'stmt', 'type_ignore', 'type_param', 'unaryop',]
listASTSubclasses = listASTSubclassesHARDCODED

class FREAKOUT(Exception):
	pass

# filesystem and namespace ===============================================
packageName: ast_Identifier = 'astToolkit'
moduleIdentifierPrefix: str = '_tool'
keywordArgumentsIdentifier: ast_Identifier = 'keywordArguments'

pathRoot = Path('/apps') / packageName
pathPackage = pathRoot / packageName
pathToolFactory = pathRoot / 'toolFactory'
pathTypeshed = pathRoot / 'typeshed' / 'stdlib'

pathFilenameDatabaseAST = pathToolFactory / 'databaseAST.csv'

fileExtension: str = '.py'

# AST class and subclasses ==================================================
listASTClasses = [ast.Add,
ast.alias,
ast.And,
ast.AnnAssign,
ast.arg,
ast.arguments,
ast.Assert,
ast.Assign,
ast.AST,
ast.AsyncFor,
ast.AsyncFunctionDef,
ast.AsyncWith,
ast.Attribute,
ast.AugAssign,
ast.Await,
ast.BinOp,
ast.BitAnd,
ast.BitOr,
ast.BitXor,
ast.BoolOp,
ast.boolop,
ast.Break,
ast.Call,
ast.ClassDef,
ast.cmpop,
ast.Compare,
ast.comprehension,
ast.Constant,
ast.Continue,
ast.Del,
ast.Delete,
ast.Dict,
ast.DictComp,
ast.Div,
ast.Eq,
ast.ExceptHandler,
ast.excepthandler,
ast.expr_context,
ast.Expr,
ast.expr,
ast.Expression,
ast.FloorDiv,
ast.For,
ast.FormattedValue,
ast.FunctionDef,
ast.FunctionType,
ast.GeneratorExp,
ast.Global,
ast.Gt,
ast.GtE,
ast.If,
ast.IfExp,
ast.Import,
ast.ImportFrom,
ast.In,
ast.Interactive,
ast.Invert,
ast.Is,
ast.IsNot,
ast.JoinedStr,
ast.keyword,
ast.Lambda,
ast.List,
ast.ListComp,
ast.Load,
ast.LShift,
ast.Lt,
ast.LtE,
ast.match_case,
ast.Match,
ast.MatchAs,
ast.MatchClass,
ast.MatchMapping,
ast.MatchOr,
ast.MatchSequence,
ast.MatchSingleton,
ast.MatchStar,
ast.MatchValue,
ast.MatMult,
ast.Mod,
ast.mod,
ast.Module,
ast.Mult,
ast.Name,
ast.NamedExpr,
ast.Nonlocal,
ast.Not,
ast.NotEq,
ast.NotIn,
ast.operator,
ast.Or,
ast.ParamSpec,
ast.Pass,
ast.pattern,
ast.Pow,
ast.Raise,
ast.Return,
ast.RShift,
ast.Set,
ast.SetComp,
ast.Slice,
ast.Starred,
ast.stmt,
ast.Store,
ast.Sub,
ast.Subscript,
ast.Try,
ast.TryStar,
ast.Tuple,
ast.type_ignore,
ast.type_param,
ast.TypeAlias,
ast.TypeIgnore,
ast.TypeVar,
ast.TypeVarTuple,
ast.UAdd,
ast.UnaryOp,
ast.unaryop,
ast.USub,
ast.While,
ast.With,
ast.withitem,
ast.Yield,
ast.YieldFrom,
]
"""Python 3.13, not deprecated"""
