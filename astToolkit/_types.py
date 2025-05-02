from astToolkit import astDOTParamSpec, astDOTTryStar, astDOTtype_param, astDOTTypeAlias, astDOTTypeVar, astDOTTypeVarTuple
from typing import Any, TypeAlias as typing_TypeAlias, TypeVar as typing_TypeVar
import ast

# TODO understand typing.

# NOTE Prototype of an idea to subclass composable methods so that typing information
# can extend beyond the top level of the ast node.
# To cover all cases, quantity of necessary classes = sum of (for each class: for each attribute: attribute * number of valid types). If an attribute has type ast.expr, for example, then there are 27 valid types just for that attribute. There would be thousands of subclasses like ImaCallToName.
# class ImaCallToName(ast.Call):
# 	func: ast.Name 	# pyright: ignore[reportIncompatibleVariableOverride]

# Type hints through TypeAlias or type "hints" through the identifier name.
ast_expr_Slice: typing_TypeAlias = ast.expr
ast_Identifier: typing_TypeAlias = str
str_nameDOTname: typing_TypeAlias = str

# Limited success with TypeVar.
个 = typing_TypeVar('个', bound = ast.AST, covariant = True)
个return = typing_TypeVar('个return', covariant = True)
NodeORattribute = typing_TypeVar('NodeORattribute', bound = ast.AST | ast_Identifier | str_nameDOTname | bool | Any | None, covariant = True)

# For my reference, all ast classes by subgroup:
Ima_ast_boolop: typing_TypeAlias = ast.boolop | ast.And | ast.Or
Ima_ast_cmpop: typing_TypeAlias = ast.cmpop | ast.Eq | ast.NotEq | ast.Lt | ast.LtE | ast.Gt | ast.GtE | ast.Is | ast.IsNot | ast.In | ast.NotIn
Ima_ast_excepthandler: typing_TypeAlias = ast.excepthandler | ast.ExceptHandler
Ima_ast_expr_context: typing_TypeAlias = ast.expr_context | ast.Load | ast.Store | ast.Del
Ima_ast_expr: typing_TypeAlias = ast.expr | ast.Attribute | ast.Await | ast.BinOp | ast.BoolOp | ast.Call | ast.Compare | ast.Constant | ast.Dict | ast.DictComp | ast.FormattedValue | ast.GeneratorExp | ast.IfExp | ast.JoinedStr | ast.Lambda | ast.List | ast.ListComp | ast.Name | ast.NamedExpr | ast.Set | ast.SetComp | ast.Slice | ast.Starred | ast.Subscript | ast.Tuple | ast.UnaryOp | ast.Yield | ast.YieldFrom
Ima_ast_mod: typing_TypeAlias = ast.mod | ast.Expression | ast.FunctionType | ast.Interactive | ast.Module
Ima_ast_operator: typing_TypeAlias = ast.operator | ast.Add | ast.Sub | ast.Mult | ast.MatMult | ast.Div | ast.Mod | ast.Pow | ast.LShift | ast.RShift | ast.BitOr | ast.BitXor | ast.BitAnd | ast.FloorDiv
iMa_ast_pattern: typing_TypeAlias = ast.pattern | ast.MatchAs | ast.MatchClass | ast.MatchMapping | ast.MatchOr | ast.MatchSequence | ast.MatchSingleton | ast.MatchStar | ast.MatchValue
Ima_ast_stmt: typing_TypeAlias = ast.stmt | ast.AnnAssign | ast.Assert | ast.Assign | ast.AsyncFor | ast.AsyncFunctionDef | ast.AsyncWith | ast.AugAssign | ast.Break | ast.ClassDef | ast.Continue | ast.Delete | ast.Expr | ast.For | ast.FunctionDef | ast.Global | ast.If | ast.Import | ast.ImportFrom | ast.Match | ast.Nonlocal | ast.Pass | ast.Raise | ast.Return | ast.Try | astDOTTryStar | astDOTTypeAlias | ast.While | ast.With
Ima_ast_type_ignore: typing_TypeAlias = ast.type_ignore | ast.TypeIgnore
Ima_ast_type_param: typing_TypeAlias = astDOTtype_param | astDOTParamSpec | astDOTTypeVar | astDOTTypeVarTuple
Ima_ast_unaryop: typing_TypeAlias = ast.unaryop | ast.Invert | ast.Not | ast.UAdd | ast.USub

Ima_ast_orphan = ast.alias | ast.arg | ast.arguments | ast.comprehension | ast.keyword | ast.match_case | ast.withitem
