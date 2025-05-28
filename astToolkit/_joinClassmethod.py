"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import ast_attributes, Make
from collections.abc import Iterable, Sequence
from typing import Unpack
import ast

def boolopJoinMethod(ast_operator: type[ast.boolop], expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr | ast.BoolOp:
    listExpressions: list[ast.expr] = list(expressions)
    match len(listExpressions):
        case 0:
            expressionsJoined = Make.Constant('', **keywordArguments)
        case 1:
            expressionsJoined = listExpressions[0]
        case _:
            expressionsJoined = Make.BoolOp(ast_operator(), listExpressions, **keywordArguments)
    return expressionsJoined

def operatorJoinMethod(ast_operator: type[ast.operator], expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
    listExpressions: list[ast.expr] = list(expressions)
    if not listExpressions:
        listExpressions.append(Make.Constant('', **keywordArguments))
    expressionsJoined: ast.expr = listExpressions[0]
    for expression in listExpressions[1:]:
        expressionsJoined = ast.BinOp(left=expressionsJoined, op=ast_operator(), right=expression, **keywordArguments)
    return expressionsJoined

class And(ast.And):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BoolOp` class."""

    @classmethod
    def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a sequence of `ast.expr` by forming an `ast.BoolOp`
        that logically "joins" expressions using the `ast.BoolOp` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Sequence[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing ast.BoolOp structures:
        ```
        ast.BoolOp(
            op=ast.And(),
            values=[ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')]
        )
        ```

        Simply use:
        ```
        astToolkit.And.join([ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual construction.
        Handles single expressions and empty sequences gracefully.
        """
        return boolopJoinMethod(cls, expressions, **keywordArguments)

class Or(ast.Or):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BoolOp` class."""

    @classmethod
    def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a sequence of `ast.expr` by forming an `ast.BoolOp`
        that logically "joins" expressions using the `ast.BoolOp` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Sequence[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing ast.BoolOp structures:
        ```
        ast.BoolOp(
            op=ast.And(),
            values=[ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')]
        )
        ```

        Simply use:
        ```
        astToolkit.And.join([ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual construction.
        Handles single expressions and empty sequences gracefully.
        """
        return boolopJoinMethod(cls, expressions, **keywordArguments)

class Add(ast.Add):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitAnd(ast.BitAnd):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitOr(ast.BitOr):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class BitXor(ast.BitXor):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Div(ast.Div):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class FloorDiv(ast.FloorDiv):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class LShift(ast.LShift):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class MatMult(ast.MatMult):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Mod(ast.Mod):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Mult(ast.Mult):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Pow(ast.Pow):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class RShift(ast.RShift):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)

class Sub(ast.Sub):
    """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

    @classmethod
    def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Create a single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp`
        that are logically "joined" using the `ast.operator` subclass. Like str.join() but for AST expressions.

        Parameters
        ----------
        expressions : Iterable[ast.expr]
            Collection of expressions to join.
        **keywordArguments : ast._attributes

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined expressions.

        Examples
        --------
        Instead of manually constructing nested ast.BinOp structures:
        ```
        ast.BinOp(
            left=ast.BinOp(
                left=ast.Name('Crosby')
                , op=ast.BitOr()
                , right=ast.Name('Stills'))
            , op=ast.BitOr()
            , right=ast.Name('Nash')
        )
        ```

        Simply use:
        ```
        astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'), ast.Name('Nash')])
        ```

        Both produce the same AST structure but the join() method eliminates the manual nesting.
        Handles single expressions and empty iterables gracefully.
        """
        return operatorJoinMethod(cls, expressions, **keywordArguments)