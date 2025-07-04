# ruff: noqa: A001
from astToolkit import ConstantValueType
from collections.abc import Sequence
from typing import Any
from typing_extensions import TypeIs
import ast

class Find:

    @classmethod
    def at(cls, getable: Any, index: int, /) -> object:
        return getable.__getitem__(index)

    class Add:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Add]:
            return isinstance(node, ast.Add)

    class alias:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.alias]:
            return isinstance(node, ast.alias)

        class name:

            @classmethod
            def __call__(cls, node: ast.alias) -> str:
                return node.name

        class asname:

            @classmethod
            def __call__(cls, node: ast.alias) -> str | None:
                return node.asname

    class And:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.And]:
            return isinstance(node, ast.And)

    class AnnAssign:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AnnAssign]:
            return isinstance(node, ast.AnnAssign)

        class target:

            @classmethod
            def __call__(cls, node: ast.AnnAssign) -> ast.Name | ast.Attribute | ast.Subscript:
                return node.target

        class annotation:

            @classmethod
            def __call__(cls, node: ast.AnnAssign) -> ast.expr:
                return node.annotation

        class value:

            @classmethod
            def __call__(cls, node: ast.AnnAssign) -> ast.expr | None:
                return node.value

        class simple:

            @classmethod
            def __call__(cls, node: ast.AnnAssign) -> int:
                return node.simple

    class arg:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.arg]:
            return isinstance(node, ast.arg)

        class arg:

            @classmethod
            def __call__(cls, node: ast.arg) -> str:
                return node.arg

        class annotation:

            @classmethod
            def __call__(cls, node: ast.arg) -> ast.expr | None:
                return node.annotation

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.arg) -> str | None:
                return node.type_comment

    class arguments:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.arguments]:
            return isinstance(node, ast.arguments)

        class posonlyargs:

            @classmethod
            def __call__(cls, node: ast.arguments) -> list[ast.arg]:
                return node.posonlyargs

        class args:

            @classmethod
            def __call__(cls, node: ast.arguments) -> list[ast.arg]:
                return node.args

        class vararg:

            @classmethod
            def __call__(cls, node: ast.arguments) -> ast.arg | None:
                return node.vararg

        class kwonlyargs:

            @classmethod
            def __call__(cls, node: ast.arguments) -> list[ast.arg]:
                return node.kwonlyargs

        class kw_defaults:

            @classmethod
            def __call__(cls, node: ast.arguments) -> Sequence[ast.expr | None]:
                return node.kw_defaults

        class kwarg:

            @classmethod
            def __call__(cls, node: ast.arguments) -> ast.arg | None:
                return node.kwarg

        class defaults:

            @classmethod
            def __call__(cls, node: ast.arguments) -> Sequence[ast.expr]:
                return node.defaults

    class Assert:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Assert]:
            return isinstance(node, ast.Assert)

        class test:

            @classmethod
            def __call__(cls, node: ast.Assert) -> ast.expr:
                return node.test

        class msg:

            @classmethod
            def __call__(cls, node: ast.Assert) -> ast.expr | None:
                return node.msg

    class Assign:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Assign]:
            return isinstance(node, ast.Assign)

        class targets:

            @classmethod
            def __call__(cls, node: ast.Assign) -> Sequence[ast.expr]:
                return node.targets

        class value:

            @classmethod
            def __call__(cls, node: ast.Assign) -> ast.expr:
                return node.value

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.Assign) -> str | None:
                return node.type_comment

    class AST:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AST]:
            return isinstance(node, ast.AST)

    class AsyncFor:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AsyncFor]:
            return isinstance(node, ast.AsyncFor)

        class target:

            @classmethod
            def __call__(cls, node: ast.AsyncFor) -> ast.expr:
                return node.target

        class iter:

            @classmethod
            def __call__(cls, node: ast.AsyncFor) -> ast.expr:
                return node.iter

        class body:

            @classmethod
            def __call__(cls, node: ast.AsyncFor) -> Sequence[ast.stmt]:
                return node.body

        class orelse:

            @classmethod
            def __call__(cls, node: ast.AsyncFor) -> Sequence[ast.stmt]:
                return node.orelse

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.AsyncFor) -> str | None:
                return node.type_comment

    class AsyncFunctionDef:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AsyncFunctionDef]:
            return isinstance(node, ast.AsyncFunctionDef)

        class name:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> str:
                return node.name

        class args:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> ast.arguments:
                return node.args

        class body:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> Sequence[ast.stmt]:
                return node.body

        class decorator_list:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> Sequence[ast.expr]:
                return node.decorator_list

        class returns:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> ast.expr | None:
                return node.returns

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> str | None:
                return node.type_comment

        class type_params:

            @classmethod
            def __call__(cls, node: ast.AsyncFunctionDef) -> Sequence[ast.type_param]:
                return node.type_params

    class AsyncWith:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AsyncWith]:
            return isinstance(node, ast.AsyncWith)

        class items:

            @classmethod
            def __call__(cls, node: ast.AsyncWith) -> list[ast.withitem]:
                return node.items

        class body:

            @classmethod
            def __call__(cls, node: ast.AsyncWith) -> Sequence[ast.stmt]:
                return node.body

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.AsyncWith) -> str | None:
                return node.type_comment

    class Attribute:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Attribute]:
            return isinstance(node, ast.Attribute)

        class value:

            @classmethod
            def __call__(cls, node: ast.Attribute) -> ast.expr:
                return node.value

        class attr:

            @classmethod
            def __call__(cls, node: ast.Attribute) -> str:
                return node.attr

        class ctx:

            @classmethod
            def __call__(cls, node: ast.Attribute) -> ast.expr_context:
                return node.ctx

    class AugAssign:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.AugAssign]:
            return isinstance(node, ast.AugAssign)

        class target:

            @classmethod
            def __call__(cls, node: ast.AugAssign) -> ast.Name | ast.Attribute | ast.Subscript:
                return node.target

        class op:

            @classmethod
            def __call__(cls, node: ast.AugAssign) -> ast.operator:
                return node.op

        class value:

            @classmethod
            def __call__(cls, node: ast.AugAssign) -> ast.expr:
                return node.value

    class Await:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Await]:
            return isinstance(node, ast.Await)

        class value:

            @classmethod
            def __call__(cls, node: ast.Await) -> ast.expr:
                return node.value

    class BinOp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.BinOp]:
            return isinstance(node, ast.BinOp)

        class left:

            @classmethod
            def __call__(cls, node: ast.BinOp) -> ast.expr:
                return node.left

        class op:

            @classmethod
            def __call__(cls, node: ast.BinOp) -> ast.operator:
                return node.op

        class right:

            @classmethod
            def __call__(cls, node: ast.BinOp) -> ast.expr:
                return node.right

    class BitAnd:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.BitAnd]:
            return isinstance(node, ast.BitAnd)

    class BitOr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.BitOr]:
            return isinstance(node, ast.BitOr)

    class BitXor:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.BitXor]:
            return isinstance(node, ast.BitXor)

    class BoolOp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.BoolOp]:
            return isinstance(node, ast.BoolOp)

        class op:

            @classmethod
            def __call__(cls, node: ast.BoolOp) -> ast.boolop:
                return node.op

        class values:

            @classmethod
            def __call__(cls, node: ast.BoolOp) -> Sequence[ast.expr]:
                return node.values

    class boolop:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.boolop]:
            return isinstance(node, ast.boolop)

    class Break:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Break]:
            return isinstance(node, ast.Break)

    class Call:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Call]:
            return isinstance(node, ast.Call)

        class func:

            @classmethod
            def __call__(cls, node: ast.Call) -> ast.expr:
                return node.func

        class args:

            @classmethod
            def __call__(cls, node: ast.Call) -> Sequence[ast.expr]:
                return node.args

        class keywords:

            @classmethod
            def __call__(cls, node: ast.Call) -> list[ast.keyword]:
                return node.keywords

    class ClassDef:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.ClassDef]:
            return isinstance(node, ast.ClassDef)

        class name:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> str:
                return node.name

        class bases:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> Sequence[ast.expr]:
                return node.bases

        class keywords:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> list[ast.keyword]:
                return node.keywords

        class body:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> Sequence[ast.stmt]:
                return node.body

        class decorator_list:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> Sequence[ast.expr]:
                return node.decorator_list

        class type_params:

            @classmethod
            def __call__(cls, node: ast.ClassDef) -> Sequence[ast.type_param]:
                return node.type_params

    class cmpop:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.cmpop]:
            return isinstance(node, ast.cmpop)

    class Compare:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Compare]:
            return isinstance(node, ast.Compare)

        class left:

            @classmethod
            def __call__(cls, node: ast.Compare) -> ast.expr:
                return node.left

        class ops:

            @classmethod
            def __call__(cls, node: ast.Compare) -> Sequence[ast.cmpop]:
                return node.ops

        class comparators:

            @classmethod
            def __call__(cls, node: ast.Compare) -> Sequence[ast.expr]:
                return node.comparators

    class comprehension:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.comprehension]:
            return isinstance(node, ast.comprehension)

        class target:

            @classmethod
            def __call__(cls, node: ast.comprehension) -> ast.expr:
                return node.target

        class iter:

            @classmethod
            def __call__(cls, node: ast.comprehension) -> ast.expr:
                return node.iter

        class ifs:

            @classmethod
            def __call__(cls, node: ast.comprehension) -> Sequence[ast.expr]:
                return node.ifs

        class is_async:

            @classmethod
            def __call__(cls, node: ast.comprehension) -> int:
                return node.is_async

    class Constant:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Constant]:
            return isinstance(node, ast.Constant)

        class value:

            @classmethod
            def __call__(cls, node: ast.Constant) -> ConstantValueType:
                return node.value

        class kind:

            @classmethod
            def __call__(cls, node: ast.Constant) -> str | None:
                return node.kind

    class Continue:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Continue]:
            return isinstance(node, ast.Continue)

    class Del:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Del]:
            return isinstance(node, ast.Del)

    class Delete:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Delete]:
            return isinstance(node, ast.Delete)

        class targets:

            @classmethod
            def __call__(cls, node: ast.Delete) -> Sequence[ast.expr]:
                return node.targets

    class Dict:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Dict]:
            return isinstance(node, ast.Dict)

        class keys:

            @classmethod
            def __call__(cls, node: ast.Dict) -> Sequence[ast.expr | None]:
                return node.keys

        class values:

            @classmethod
            def __call__(cls, node: ast.Dict) -> Sequence[ast.expr]:
                return node.values

    class DictComp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.DictComp]:
            return isinstance(node, ast.DictComp)

        class key:

            @classmethod
            def __call__(cls, node: ast.DictComp) -> ast.expr:
                return node.key

        class value:

            @classmethod
            def __call__(cls, node: ast.DictComp) -> ast.expr:
                return node.value

        class generators:

            @classmethod
            def __call__(cls, node: ast.DictComp) -> list[ast.comprehension]:
                return node.generators

    class Div:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Div]:
            return isinstance(node, ast.Div)

    class Eq:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Eq]:
            return isinstance(node, ast.Eq)

    class ExceptHandler:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.ExceptHandler]:
            return isinstance(node, ast.ExceptHandler)

        class type:

            @classmethod
            def __call__(cls, node: ast.ExceptHandler) -> ast.expr | None:
                return node.type

        class name:

            @classmethod
            def __call__(cls, node: ast.ExceptHandler) -> str | None:
                return node.name

        class body:

            @classmethod
            def __call__(cls, node: ast.ExceptHandler) -> Sequence[ast.stmt]:
                return node.body

    class excepthandler:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.excepthandler]:
            return isinstance(node, ast.excepthandler)

    class expr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.expr]:
            return isinstance(node, ast.expr)

    class Expr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Expr]:
            return isinstance(node, ast.Expr)

        class value:

            @classmethod
            def __call__(cls, node: ast.Expr) -> ast.expr:
                return node.value

    class expr_context:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.expr_context]:
            return isinstance(node, ast.expr_context)

    class Expression:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Expression]:
            return isinstance(node, ast.Expression)

        class body:

            @classmethod
            def __call__(cls, node: ast.Expression) -> ast.expr:
                return node.body

    class FloorDiv:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.FloorDiv]:
            return isinstance(node, ast.FloorDiv)

    class For:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.For]:
            return isinstance(node, ast.For)

        class target:

            @classmethod
            def __call__(cls, node: ast.For) -> ast.expr:
                return node.target

        class iter:

            @classmethod
            def __call__(cls, node: ast.For) -> ast.expr:
                return node.iter

        class body:

            @classmethod
            def __call__(cls, node: ast.For) -> Sequence[ast.stmt]:
                return node.body

        class orelse:

            @classmethod
            def __call__(cls, node: ast.For) -> Sequence[ast.stmt]:
                return node.orelse

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.For) -> str | None:
                return node.type_comment

    class FormattedValue:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.FormattedValue]:
            return isinstance(node, ast.FormattedValue)

        class value:

            @classmethod
            def __call__(cls, node: ast.FormattedValue) -> ast.expr:
                return node.value

        class conversion:

            @classmethod
            def __call__(cls, node: ast.FormattedValue) -> int:
                return node.conversion

        class format_spec:

            @classmethod
            def __call__(cls, node: ast.FormattedValue) -> ast.expr | None:
                return node.format_spec

    class FunctionDef:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.FunctionDef]:
            return isinstance(node, ast.FunctionDef)

        class name:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> str:
                return node.name

        class args:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> ast.arguments:
                return node.args

        class body:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> Sequence[ast.stmt]:
                return node.body

        class decorator_list:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> Sequence[ast.expr]:
                return node.decorator_list

        class returns:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> ast.expr | None:
                return node.returns

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> str | None:
                return node.type_comment

        class type_params:

            @classmethod
            def __call__(cls, node: ast.FunctionDef) -> Sequence[ast.type_param]:
                return node.type_params

    class FunctionType:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.FunctionType]:
            return isinstance(node, ast.FunctionType)

        class argtypes:

            @classmethod
            def __call__(cls, node: ast.FunctionType) -> Sequence[ast.expr]:
                return node.argtypes

        class returns:

            @classmethod
            def __call__(cls, node: ast.FunctionType) -> ast.expr:
                return node.returns

    class GeneratorExp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.GeneratorExp]:
            return isinstance(node, ast.GeneratorExp)

        class elt:

            @classmethod
            def __call__(cls, node: ast.GeneratorExp) -> ast.expr:
                return node.elt

        class generators:

            @classmethod
            def __call__(cls, node: ast.GeneratorExp) -> list[ast.comprehension]:
                return node.generators

    class Global:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Global]:
            return isinstance(node, ast.Global)

        class names:

            @classmethod
            def __call__(cls, node: ast.Global) -> list[str]:
                return node.names

    class Gt:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Gt]:
            return isinstance(node, ast.Gt)

    class GtE:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.GtE]:
            return isinstance(node, ast.GtE)

    class If:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.If]:
            return isinstance(node, ast.If)

        class test:

            @classmethod
            def __call__(cls, node: ast.If) -> ast.expr:
                return node.test

        class body:

            @classmethod
            def __call__(cls, node: ast.If) -> Sequence[ast.stmt]:
                return node.body

        class orelse:

            @classmethod
            def __call__(cls, node: ast.If) -> Sequence[ast.stmt]:
                return node.orelse

    class IfExp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.IfExp]:
            return isinstance(node, ast.IfExp)

        class test:

            @classmethod
            def __call__(cls, node: ast.IfExp) -> ast.expr:
                return node.test

        class body:

            @classmethod
            def __call__(cls, node: ast.IfExp) -> ast.expr:
                return node.body

        class orelse:

            @classmethod
            def __call__(cls, node: ast.IfExp) -> ast.expr:
                return node.orelse

    class Import:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Import]:
            return isinstance(node, ast.Import)

        class names:

            @classmethod
            def __call__(cls, node: ast.Import) -> list[ast.alias]:
                return node.names

    class ImportFrom:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.ImportFrom]:
            return isinstance(node, ast.ImportFrom)

        class module:

            @classmethod
            def __call__(cls, node: ast.ImportFrom) -> str | None:
                return node.module

        class names:

            @classmethod
            def __call__(cls, node: ast.ImportFrom) -> list[ast.alias]:
                return node.names

        class level:

            @classmethod
            def __call__(cls, node: ast.ImportFrom) -> int:
                return node.level

    class In:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.In]:
            return isinstance(node, ast.In)

    class Interactive:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Interactive]:
            return isinstance(node, ast.Interactive)

        class body:

            @classmethod
            def __call__(cls, node: ast.Interactive) -> Sequence[ast.stmt]:
                return node.body

    class Invert:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Invert]:
            return isinstance(node, ast.Invert)

    class Is:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Is]:
            return isinstance(node, ast.Is)

    class IsNot:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.IsNot]:
            return isinstance(node, ast.IsNot)

    class JoinedStr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.JoinedStr]:
            return isinstance(node, ast.JoinedStr)

        class values:

            @classmethod
            def __call__(cls, node: ast.JoinedStr) -> Sequence[ast.expr]:
                return node.values

    class keyword:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.keyword]:
            return isinstance(node, ast.keyword)

        class arg:

            @classmethod
            def __call__(cls, node: ast.keyword) -> str | None:
                return node.arg

        class value:

            @classmethod
            def __call__(cls, node: ast.keyword) -> ast.expr:
                return node.value

    class Lambda:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Lambda]:
            return isinstance(node, ast.Lambda)

        class args:

            @classmethod
            def __call__(cls, node: ast.Lambda) -> ast.arguments:
                return node.args

        class body:

            @classmethod
            def __call__(cls, node: ast.Lambda) -> ast.expr:
                return node.body

    class List:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.List]:
            return isinstance(node, ast.List)

        class elts:

            @classmethod
            def __call__(cls, node: ast.List) -> Sequence[ast.expr]:
                return node.elts

        class ctx:

            @classmethod
            def __call__(cls, node: ast.List) -> ast.expr_context:
                return node.ctx

    class ListComp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.ListComp]:
            return isinstance(node, ast.ListComp)

        class elt:

            @classmethod
            def __call__(cls, node: ast.ListComp) -> ast.expr:
                return node.elt

        class generators:

            @classmethod
            def __call__(cls, node: ast.ListComp) -> list[ast.comprehension]:
                return node.generators

    class Load:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Load]:
            return isinstance(node, ast.Load)

    class LShift:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.LShift]:
            return isinstance(node, ast.LShift)

    class Lt:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Lt]:
            return isinstance(node, ast.Lt)

    class LtE:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.LtE]:
            return isinstance(node, ast.LtE)

    class Match:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Match]:
            return isinstance(node, ast.Match)

        class subject:

            @classmethod
            def __call__(cls, node: ast.Match) -> ast.expr:
                return node.subject

        class cases:

            @classmethod
            def __call__(cls, node: ast.Match) -> list[ast.match_case]:
                return node.cases

    class match_case:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.match_case]:
            return isinstance(node, ast.match_case)

        class pattern:

            @classmethod
            def __call__(cls, node: ast.match_case) -> ast.pattern:
                return node.pattern

        class guard:

            @classmethod
            def __call__(cls, node: ast.match_case) -> ast.expr | None:
                return node.guard

        class body:

            @classmethod
            def __call__(cls, node: ast.match_case) -> Sequence[ast.stmt]:
                return node.body

    class MatchAs:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchAs]:
            return isinstance(node, ast.MatchAs)

        class pattern:

            @classmethod
            def __call__(cls, node: ast.MatchAs) -> ast.pattern | None:
                return node.pattern

        class name:

            @classmethod
            def __call__(cls, node: ast.MatchAs) -> str | None:
                return node.name

    class MatchClass:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchClass]:
            return isinstance(node, ast.MatchClass)

        class cls:

            @classmethod
            def __call__(cls, node: ast.MatchClass) -> ast.expr:
                return node.cls

        class patterns:

            @classmethod
            def __call__(cls, node: ast.MatchClass) -> Sequence[ast.pattern]:
                return node.patterns

        class kwd_attrs:

            @classmethod
            def __call__(cls, node: ast.MatchClass) -> list[str]:
                return node.kwd_attrs

        class kwd_patterns:

            @classmethod
            def __call__(cls, node: ast.MatchClass) -> Sequence[ast.pattern]:
                return node.kwd_patterns

    class MatchMapping:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchMapping]:
            return isinstance(node, ast.MatchMapping)

        class keys:

            @classmethod
            def __call__(cls, node: ast.MatchMapping) -> Sequence[ast.expr]:
                return node.keys

        class patterns:

            @classmethod
            def __call__(cls, node: ast.MatchMapping) -> Sequence[ast.pattern]:
                return node.patterns

        class rest:

            @classmethod
            def __call__(cls, node: ast.MatchMapping) -> str | None:
                return node.rest

    class MatchOr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchOr]:
            return isinstance(node, ast.MatchOr)

        class patterns:

            @classmethod
            def __call__(cls, node: ast.MatchOr) -> Sequence[ast.pattern]:
                return node.patterns

    class MatchSequence:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchSequence]:
            return isinstance(node, ast.MatchSequence)

        class patterns:

            @classmethod
            def __call__(cls, node: ast.MatchSequence) -> Sequence[ast.pattern]:
                return node.patterns

    class MatchSingleton:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchSingleton]:
            return isinstance(node, ast.MatchSingleton)

        class value:

            @classmethod
            def __call__(cls, node: ast.MatchSingleton) -> bool | None:
                return node.value

    class MatchStar:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchStar]:
            return isinstance(node, ast.MatchStar)

        class name:

            @classmethod
            def __call__(cls, node: ast.MatchStar) -> str | None:
                return node.name

    class MatchValue:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatchValue]:
            return isinstance(node, ast.MatchValue)

        class value:

            @classmethod
            def __call__(cls, node: ast.MatchValue) -> ast.expr:
                return node.value

    class MatMult:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.MatMult]:
            return isinstance(node, ast.MatMult)

    class mod:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.mod]:
            return isinstance(node, ast.mod)

    class Mod:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Mod]:
            return isinstance(node, ast.Mod)

    class Module:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Module]:
            return isinstance(node, ast.Module)

        class body:

            @classmethod
            def __call__(cls, node: ast.Module) -> Sequence[ast.stmt]:
                return node.body

        class type_ignores:

            @classmethod
            def __call__(cls, node: ast.Module) -> list[ast.TypeIgnore]:
                return node.type_ignores

    class Mult:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Mult]:
            return isinstance(node, ast.Mult)

    class Name:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Name]:
            return isinstance(node, ast.Name)

        class id:

            @classmethod
            def __call__(cls, node: ast.Name) -> str:
                return node.id

        class ctx:

            @classmethod
            def __call__(cls, node: ast.Name) -> ast.expr_context:
                return node.ctx

    class NamedExpr:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.NamedExpr]:
            return isinstance(node, ast.NamedExpr)

        class target:

            @classmethod
            def __call__(cls, node: ast.NamedExpr) -> ast.Name:
                return node.target

        class value:

            @classmethod
            def __call__(cls, node: ast.NamedExpr) -> ast.expr:
                return node.value

    class Nonlocal:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Nonlocal]:
            return isinstance(node, ast.Nonlocal)

        class names:

            @classmethod
            def __call__(cls, node: ast.Nonlocal) -> list[str]:
                return node.names

    class Not:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Not]:
            return isinstance(node, ast.Not)

    class NotEq:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.NotEq]:
            return isinstance(node, ast.NotEq)

    class NotIn:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.NotIn]:
            return isinstance(node, ast.NotIn)

    class operator:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.operator]:
            return isinstance(node, ast.operator)

    class Or:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Or]:
            return isinstance(node, ast.Or)

    class ParamSpec:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.ParamSpec]:
            return isinstance(node, ast.ParamSpec)

        class name:

            @classmethod
            def __call__(cls, node: ast.ParamSpec) -> str:
                return node.name

        class default_value:

            @classmethod
            def __call__(cls, node: ast.ParamSpec) -> ast.expr | None:
                return node.default_value

    class Pass:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Pass]:
            return isinstance(node, ast.Pass)

    class pattern:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.pattern]:
            return isinstance(node, ast.pattern)

    class Pow:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Pow]:
            return isinstance(node, ast.Pow)

    class Raise:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Raise]:
            return isinstance(node, ast.Raise)

        class exc:

            @classmethod
            def __call__(cls, node: ast.Raise) -> ast.expr | None:
                return node.exc

        class cause:

            @classmethod
            def __call__(cls, node: ast.Raise) -> ast.expr | None:
                return node.cause

    class Return:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Return]:
            return isinstance(node, ast.Return)

        class value:

            @classmethod
            def __call__(cls, node: ast.Return) -> ast.expr | None:
                return node.value

    class RShift:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.RShift]:
            return isinstance(node, ast.RShift)

    class Set:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Set]:
            return isinstance(node, ast.Set)

        class elts:

            @classmethod
            def __call__(cls, node: ast.Set) -> Sequence[ast.expr]:
                return node.elts

    class SetComp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.SetComp]:
            return isinstance(node, ast.SetComp)

        class elt:

            @classmethod
            def __call__(cls, node: ast.SetComp) -> ast.expr:
                return node.elt

        class generators:

            @classmethod
            def __call__(cls, node: ast.SetComp) -> list[ast.comprehension]:
                return node.generators

    class Slice:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Slice]:
            return isinstance(node, ast.Slice)

        class lower:

            @classmethod
            def __call__(cls, node: ast.Slice) -> ast.expr | None:
                return node.lower

        class upper:

            @classmethod
            def __call__(cls, node: ast.Slice) -> ast.expr | None:
                return node.upper

        class step:

            @classmethod
            def __call__(cls, node: ast.Slice) -> ast.expr | None:
                return node.step

    class Starred:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Starred]:
            return isinstance(node, ast.Starred)

        class value:

            @classmethod
            def __call__(cls, node: ast.Starred) -> ast.expr:
                return node.value

        class ctx:

            @classmethod
            def __call__(cls, node: ast.Starred) -> ast.expr_context:
                return node.ctx

    class stmt:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.stmt]:
            return isinstance(node, ast.stmt)

    class Store:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Store]:
            return isinstance(node, ast.Store)

    class Sub:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Sub]:
            return isinstance(node, ast.Sub)

    class Subscript:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Subscript]:
            return isinstance(node, ast.Subscript)

        class value:

            @classmethod
            def __call__(cls, node: ast.Subscript) -> ast.expr:
                return node.value

        class slice:

            @classmethod
            def __call__(cls, node: ast.Subscript) -> ast.expr:
                return node.slice

        class ctx:

            @classmethod
            def __call__(cls, node: ast.Subscript) -> ast.expr_context:
                return node.ctx

    class Try:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Try]:
            return isinstance(node, ast.Try)

        class body:

            @classmethod
            def __call__(cls, node: ast.Try) -> Sequence[ast.stmt]:
                return node.body

        class handlers:

            @classmethod
            def __call__(cls, node: ast.Try) -> list[ast.ExceptHandler]:
                return node.handlers

        class orelse:

            @classmethod
            def __call__(cls, node: ast.Try) -> Sequence[ast.stmt]:
                return node.orelse

        class finalbody:

            @classmethod
            def __call__(cls, node: ast.Try) -> Sequence[ast.stmt]:
                return node.finalbody

    class TryStar:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.TryStar]:
            return isinstance(node, ast.TryStar)

        class body:

            @classmethod
            def __call__(cls, node: ast.TryStar) -> Sequence[ast.stmt]:
                return node.body

        class handlers:

            @classmethod
            def __call__(cls, node: ast.TryStar) -> list[ast.ExceptHandler]:
                return node.handlers

        class orelse:

            @classmethod
            def __call__(cls, node: ast.TryStar) -> Sequence[ast.stmt]:
                return node.orelse

        class finalbody:

            @classmethod
            def __call__(cls, node: ast.TryStar) -> Sequence[ast.stmt]:
                return node.finalbody

    class Tuple:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Tuple]:
            return isinstance(node, ast.Tuple)

        class elts:

            @classmethod
            def __call__(cls, node: ast.Tuple) -> Sequence[ast.expr]:
                return node.elts

        class ctx:

            @classmethod
            def __call__(cls, node: ast.Tuple) -> ast.expr_context:
                return node.ctx

    class type_ignore:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.type_ignore]:
            return isinstance(node, ast.type_ignore)

    class type_param:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.type_param]:
            return isinstance(node, ast.type_param)

    class TypeAlias:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.TypeAlias]:
            return isinstance(node, ast.TypeAlias)

        class name:

            @classmethod
            def __call__(cls, node: ast.TypeAlias) -> ast.Name:
                return node.name

        class type_params:

            @classmethod
            def __call__(cls, node: ast.TypeAlias) -> Sequence[ast.type_param]:
                return node.type_params

        class value:

            @classmethod
            def __call__(cls, node: ast.TypeAlias) -> ast.expr:
                return node.value

    class TypeIgnore:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.TypeIgnore]:
            return isinstance(node, ast.TypeIgnore)

        class lineno:

            @classmethod
            def __call__(cls, node: ast.TypeIgnore) -> int:
                return node.lineno

        class tag:

            @classmethod
            def __call__(cls, node: ast.TypeIgnore) -> str:
                return node.tag

    class TypeVar:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.TypeVar]:
            return isinstance(node, ast.TypeVar)

        class name:

            @classmethod
            def __call__(cls, node: ast.TypeVar) -> str:
                return node.name

        class bound:

            @classmethod
            def __call__(cls, node: ast.TypeVar) -> ast.expr | None:
                return node.bound

        class default_value:

            @classmethod
            def __call__(cls, node: ast.TypeVar) -> ast.expr | None:
                return node.default_value

    class TypeVarTuple:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.TypeVarTuple]:
            return isinstance(node, ast.TypeVarTuple)

        class name:

            @classmethod
            def __call__(cls, node: ast.TypeVarTuple) -> str:
                return node.name

        class default_value:

            @classmethod
            def __call__(cls, node: ast.TypeVarTuple) -> ast.expr | None:
                return node.default_value

    class UAdd:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.UAdd]:
            return isinstance(node, ast.UAdd)

    class UnaryOp:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.UnaryOp]:
            return isinstance(node, ast.UnaryOp)

        class op:

            @classmethod
            def __call__(cls, node: ast.UnaryOp) -> ast.unaryop:
                return node.op

        class operand:

            @classmethod
            def __call__(cls, node: ast.UnaryOp) -> ast.expr:
                return node.operand

    class unaryop:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.unaryop]:
            return isinstance(node, ast.unaryop)

    class USub:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.USub]:
            return isinstance(node, ast.USub)

    class While:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.While]:
            return isinstance(node, ast.While)

        class test:

            @classmethod
            def __call__(cls, node: ast.While) -> ast.expr:
                return node.test

        class body:

            @classmethod
            def __call__(cls, node: ast.While) -> Sequence[ast.stmt]:
                return node.body

        class orelse:

            @classmethod
            def __call__(cls, node: ast.While) -> Sequence[ast.stmt]:
                return node.orelse

    class With:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.With]:
            return isinstance(node, ast.With)

        class items:

            @classmethod
            def __call__(cls, node: ast.With) -> list[ast.withitem]:
                return node.items

        class body:

            @classmethod
            def __call__(cls, node: ast.With) -> Sequence[ast.stmt]:
                return node.body

        class type_comment:

            @classmethod
            def __call__(cls, node: ast.With) -> str | None:
                return node.type_comment

    class withitem:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.withitem]:
            return isinstance(node, ast.withitem)

        class context_expr:

            @classmethod
            def __call__(cls, node: ast.withitem) -> ast.expr:
                return node.context_expr

        class optional_vars:

            @classmethod
            def __call__(cls, node: ast.withitem) -> ast.expr | None:
                return node.optional_vars

    class Yield:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Yield]:
            return isinstance(node, ast.Yield)

        class value:

            @classmethod
            def __call__(cls, node: ast.Yield) -> ast.expr | None:
                return node.value

    class YieldFrom:

        @classmethod
        def __call__(cls, node: ast.AST) -> TypeIs[ast.YieldFrom]:
            return isinstance(node, ast.YieldFrom)

        class value:

            @classmethod
            def __call__(cls, node: ast.YieldFrom) -> ast.expr:
                return node.value
