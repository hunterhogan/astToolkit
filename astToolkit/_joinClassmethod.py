"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import Make
from collections.abc import Iterable
from typing import Generic, TypedDict, TypeVar as typing_TypeVar, Unpack
import ast
import sys
if sys.version_info >= (3, 13):
    _EndPositionT = typing_TypeVar('_EndPositionT', int, int | None, default=int | None)
else:
    _EndPositionT = typing_TypeVar('_EndPositionT', int, int | None)

class _Attributes(TypedDict, Generic[_EndPositionT], total=False):
    lineno: int
    col_offset: int
    end_lineno: _EndPositionT
    end_col_offset: _EndPositionT

def operatorJoinMethod(ast_operator: type[ast.operator], expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
    listExpressions: list[ast.expr] = list(expressions)
    if not listExpressions:
        listExpressions.append(Make.Constant('', **keywordArguments))
    expressionsJoined: ast.expr = listExpressions[0]
    for expression in listExpressions[1:]:
        expressionsJoined = ast.BinOp(left=expressionsJoined, op=ast_operator(), right=expression, **keywordArguments)
    return expressionsJoined

class Add(ast.Add):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitAnd(ast.BitAnd):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitOr(ast.BitOr):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitXor(ast.BitXor):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Div(ast.Div):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class FloorDiv(ast.FloorDiv):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class LShift(ast.LShift):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class MatMult(ast.MatMult):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Mod(ast.Mod):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Mult(ast.Mult):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Pow(ast.Pow):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class RShift(ast.RShift):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Sub(ast.Sub):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[_Attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass.

        Parameters
        ----------
        expressions: Iterable[ast.expr]
            A collection of `ast.expr` objects to be joined.
        lineno: int
        col_offset: int
        end_lineno: int | None
        end_col_offset: int | None

        Returns
        -------
        joinedExpression: ast.expr
            The resulting `ast.expr` that represents the joined expressions.

        Notes
        -----
        - Like `str.join()`, you probably want to use it with two or more expressions.
        - The method does not validate the elements of the input iterable.
        - If you pass only one expression, it will be returned as is.
        - If you pass no expressions, the behavior is analogous to `str.join([])`, which is an empty iterable, and the method returns `ast.Constant('', **keywordArguments)`.

        Examples
        --------

        This
        ```
        astToolkit.Mult().join([ast.Name('groups'), ast.Attribute(ast.Name('state'), 'leavesTotal'), ast.Constant(14)])
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(
                left=ast.Name(id='groups', ctx=ast.Load())
                , op=ast.Mult()
                , right=ast.Attribute(value=ast.Name(id='state', ctx=ast.Load()), attr='leavesTotal', ctx=ast.Load()))
            , op=ast.Mult()
            , right=ast.Constant(value=14))
        ```
        which unparses as
        ```
        groups * state.leavesTotal * 14
        ```

        This
        ```
        listIdentifiers = ['Assign','Attribute','AugAssign','Await','DictComp','Expr','FormattedValue','keyword','MatchValue','NamedExpr','Starred','Subscript','TypeAlias','YieldFrom']
        list_astAttribute = [Make.Attribute(Make.Name('ast'), identifier) for identifier in listIdentifiers]
        astToolkit.BitOr().join(list_astAttribute)
        ```
        is equivalent to
        ```
        ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(
                                                                left=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Assign', ctx=ast.Load())
                                                                , op=ast.BitOr()
                                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Attribute', ctx=ast.Load()))
                                                            , op=ast.BitOr()
                                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='AugAssign', ctx=ast.Load()))
                                                        , op=ast.BitOr()
                                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Await', ctx=ast.Load()))
                                                    , op=ast.BitOr()
                                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='DictComp', ctx=ast.Load()))
                                                , op=ast.BitOr()
                                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Expr', ctx=ast.Load()))
                                            , op=ast.BitOr()
                                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='FormattedValue', ctx=ast.Load()))
                                        , op=ast.BitOr()
                                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='keyword', ctx=ast.Load()))
                                    , op=ast.BitOr()
                                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='MatchValue', ctx=ast.Load()))
                                , op=ast.BitOr()
                                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='NamedExpr', ctx=ast.Load()))
                            , op=ast.BitOr()
                            , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Starred', ctx=ast.Load()))
                        , op=ast.BitOr()
                        , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='Subscript', ctx=ast.Load()))
                    , op=ast.BitOr()
                    , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='TypeAlias', ctx=ast.Load()))
                , op=ast.BitOr()
                , right=ast.Attribute(value=ast.Name(id='ast', ctx=ast.Load()), attr='YieldFrom', ctx=ast.Load()))

        which unparses as
        ```
        ast.Assign | ast.Attribute | ast.AugAssign | ast.Await | ast.DictComp | ast.Expr | ast.FormattedValue | ast.keyword | ast.MatchValue | ast.NamedExpr | ast.Starred | ast.Subscript | ast.TypeAlias | ast.YieldFrom
        ```
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)