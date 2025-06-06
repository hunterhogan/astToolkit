"""This file is generated automatically, so changes to this file will be lost."""
from astToolkit import (
	ast_attributes, ast_attributes_int, ast_attributes_type_comment, ConstantValueType,
	identifierDotAttribute,
)
from collections.abc import Iterable, Sequence
from typing import overload
from typing_extensions import Unpack
import ast
import sys

class Make:
    """
    Factory methods for creating properly configured AST nodes with enhanced usability.
    (AI generated docstring)

    The `Make` class provides 160+ static methods for constructing Python AST nodes with correct
    attributes and type annotations. This is the primary factory component of the astToolkit
    package, designed to simplify AST node creation through enhanced parameter naming and
    composable operations.

    Key features include parameter renaming for better usability while maintaining access to all
    AST constructor parameters, enhanced functionality such as variadic parameters that create
    chained structures, and consistent `**keywordArguments` access to position and type information
    across all methods.

    Common AST attributes accessible through `**keywordArguments`:

        col_offset (0): Position information specifying the column where an AST object begins.
        end_col_offset (None): Position information specifying the column where an AST object ends.
        end_lineno (None): Position information specifying the line number where an AST object ends.
        level (0): Module import depth level that controls relative vs absolute imports. Default 0 indicates absolute import.
        lineno: Position information manually specifying the line number where an AST object begins.
        type_comment (None): Optional string with the type annotation as a comment or `# type: ignore`.

    The Make class supports the antecedent-action pattern where factory methods serve as actions
    combined with predicates from `Be`, `IfThis`, and `ClassIsAndAttribute` classes through visitor
    classes like `NodeTourist` and `NodeChanger`.
    """

    @staticmethod
    def _boolopJoinMethod(ast_operator: type[ast.boolop], expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr | ast.BoolOp:
        """
        Single `ast.expr` from a sequence of `ast.expr` by forming an `ast.BoolOp` that logically "joins" expressions using the `ast.BoolOp` subclass.

        Like str.join() but for AST expressions.

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
        listExpressions: list[ast.expr] = list(expressions)
        match len(listExpressions):
            case 0:
                expressionsJoined = Make.Constant('', **keywordArguments)
            case 1:
                expressionsJoined = listExpressions[0]
            case _:
                expressionsJoined = Make.BoolOp(ast_operator(), listExpressions, **keywordArguments)
        return expressionsJoined

    @staticmethod
    def _operatorJoinMethod(ast_operator: type[ast.operator], expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def alias(name: str, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.alias:
        """
        Import alias AST `object` representing name mapping in import statements.
        (AI generated docstring)

        The `ast.alias` `object` represents name mappings used in `import` and
        `from ... import` statements. It handles both direct imports (`import math`)
        and aliased imports (`import numpy as np`).

        Parameters:
            name: The actual module, class, or function name being imported.
            asName (None): Optional alias name to use instead of the original name.
                This corresponds to `ast.alias.asname`.

        Returns
        -------
        importAlias: ast.alias
            AST `object` representing an import name mapping with optional aliasing.
        """
        return ast.alias(name=name, asname=asName, **keywordArguments)

    class And(ast.And):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BoolOp` class."""

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a sequence of `ast.expr` by forming an `ast.BoolOp` that logically "joins" expressions using the `ast.BoolOp` subclass.

        Like str.join() but for AST expressions.

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
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def AnnAssign(target: ast.Name | ast.Attribute | ast.Subscript, annotation: ast.expr, value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.AnnAssign:
        """
        Annotated assignment AST `object` for type-annotated variable assignments.
        (AI generated docstring)

        The `ast.AnnAssign` `object` represents variable assignments with type annotations,
        such as `name: int = 42` or `config: dict[str, Any]`. This is the preferred
        form for annotated assignments in modern Python code.

        Parameters:
            target: The assignment target, which must be a simple name, attribute access,
                or subscript operation that can receive the annotated assignment.
            annotation: The type annotation expression specifying the variable's expected type.
            value (None): Optional initial value expression for the annotated variable.

        Returns
        -------
        annotatedAssignment: ast.AnnAssign
            AST `object` representing a type-annotated variable assignment.
        """
        return ast.AnnAssign(target=target, annotation=annotation, value=value, simple=int(isinstance(target, ast.Name)), **keywordArguments)

    @staticmethod
    def arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str, annotation: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.arg:
        """
        Function parameter AST object representing individual arguments (**arg**ument) in function signatures.
        (AI generated docstring)

        The `ast.arg` object represents a single parameter in function definitions,
        including positional, keyword-only, and special parameters like `*args` and `**kwargs`.
        Contains the parameter name and optional type annotation.

        Parameters:
            Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: Parameter name as string. This corresponds to `ast.arg.arg`.
            annotation (None): Optional type annotation expression for the parameter.

        Returns:
            argumentDefinition: ast.arg
            AST object representing a single function parameter with optional typing.
        """
        return ast.arg(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, annotation=annotation, **keywordArguments)

    @staticmethod
    def arguments(posonlyargs: list[ast.arg]=[], list_arg: list[ast.arg]=[], vararg: ast.arg | None=None, kwonlyargs: list[ast.arg]=[], kw_defaults: Sequence[ast.expr | None]=[None], kwarg: ast.arg | None=None, defaults: Sequence[ast.expr]=[]) -> ast.arguments:
        """
        Function signature AST object containing all parameter specifications (**arg**ument**s**).
        (AI generated docstring)

        The `ast.arguments` object represents the complete parameter specification
        for function definitions, organizing different parameter types including
        positional-only, regular, keyword-only, variadic, and default values.

        Parameters:
            posonlyargs ([]): List of positional-only parameters (before /).
            list_arg ([]): List of regular positional parameters. This corresponds to `ast.arguments.args`.
            vararg (None): Single parameter for *args variadic arguments.
            kwonlyargs ([]): List of keyword-only parameters (after * or *args).
            kw_defaults ([None]): Default values for keyword-only parameters; None indicates required.
            kwarg (None): Single parameter for **kwargs keyword arguments.
            defaults ([]): Default values for regular positional parameters.

        Returns:
            functionSignature: ast.arguments
            AST object representing complete function parameter specification.
        """
        return ast.arguments(posonlyargs=posonlyargs, args=list_arg, vararg=vararg, kwonlyargs=kwonlyargs, kw_defaults=list(kw_defaults), kwarg=kwarg, defaults=list(defaults))

    @staticmethod
    def Assert(test: ast.expr, msg: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Assert:
        """Create an `ast.Assert` node for assertion statements.

        The `Assert` node represents an `assert` statement that evaluates a test
        expression and optionally raises `AssertionError` with a message if the
        test fails. This is primarily used for debugging and testing purposes.

        Parameters
            test: Expression to evaluate for truthiness
            msg (None): Optional expression for the assertion error message

        Returns
            nodeAssert: The constructed assertion node
        """
        return ast.Assert(test=test, msg=msg, **keywordArguments)

    @staticmethod
    def Assign(targets: Sequence[ast.expr], value: ast.expr, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.Assign:
        """
        Assignment AST `object` for variable assignments without type annotations.
        (AI generated docstring)

        The `ast.Assign` `object` represents traditional variable assignments like
        `x = 5`, `a = b = c`, or `items[0] = newValue`. It supports multiple assignment
        targets and complex assignment patterns.

        Parameters:
            targets: Sequence of assignment targets that will receive the value.
                Multiple targets enable chained assignments like `a = b = value`.
            value: The expression whose result will be assigned to all targets.

        Returns
        -------
        assignment: ast.Assign
            AST `object` representing a variable assignment operation.
        """
        return ast.Assign(targets=list(targets), value=value, **keywordArguments)

    @staticmethod
    def AST() -> ast.AST:
        """
        Base AST node object representing the abstract syntax tree foundation.
        (AI generated docstring)

        The `ast.AST` object serves as the base class for all AST node types in Python's
        abstract syntax tree. This method creates a minimal AST instance, though in practice
        you will typically use specific node type factories like `Make.Name()`, `Make.Call()`,
        etc.

        Most users seeking AST node creation should use the specific factory methods for
        concrete node types rather than this base AST constructor.

        Returns:
            baseNode: The fundamental AST object from which all other nodes inherit.
        """
        return ast.AST()

    @staticmethod
    def AsyncFor(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFor:
        """
        Asynchronous for loop AST `object` for iterating over async iterables.
        (AI generated docstring)

        The `ast.AsyncFor` `object` represents `async for` loops that iterate over
        asynchronous iterators and async generators. These loops can only exist
        within async functions and automatically handle await operations.

        Parameters:
            target: The loop variable that receives each item from the async iterable.
            iter: The asynchronous iterable expression being iterated over.
            body: Sequence of statements executed for each iteration of the async loop.
            orElse ([]): Optional statements executed when the loop completes normally
                without encountering a break statement. This corresponds to `ast.AsyncFor.orelse`.

        Returns
        -------
        asyncForLoop: ast.AsyncFor
            AST `object` representing an asynchronous for loop construct.
        """
        return ast.AsyncFor(target=target, iter=iter, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def AsyncFunctionDef(name: str, argumentSpecification: ast.arguments=ast.arguments(), body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFunctionDef:
        """
        Asynchronous function definition AST object for `async def` declarations.
        (AI generated docstring)

        The `ast.AsyncFunctionDef` object represents asynchronous function definitions
        using the `async def` syntax. Supports coroutines, async generators, and
        other asynchronous operations with await expressions.

        Parameters:
            name: Function name as string identifier.
            argumentSpecification (ast.arguments()): Function parameter specification. This corresponds to `ast.AsyncFunctionDef.args`.
            body ([]): List of statements forming the function body.
            decorator_list ([]): List of decorator expressions applied to function.
            returns (None): Optional return type annotation expression.
            type_params ([]): List of type parameters for generic functions (Python 3.12+).

        Returns:
            asyncFunction: ast.AsyncFunctionDef
            AST object representing an asynchronous function definition.
        """
        return ast.AsyncFunctionDef(name=name, args=argumentSpecification, body=list(body), decorator_list=list(decorator_list), returns=returns, type_params=list(type_params), **keywordArguments)

    @staticmethod
    def AsyncWith(items: Sequence[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncWith:
        """
        Asynchronous context manager AST `object` for async resource management.
        (AI generated docstring)

        The `ast.AsyncWith` `object` represents `async with` statements that manage
        asynchronous context managers. These ensure proper setup and cleanup of
        async resources like database connections or file handles.

        Parameters:
            items: Sequence of context manager items, each specifying an async context
                manager and optional variable binding for the managed resource.
            body: Sequence of statements executed within the async context manager scope.

        Returns
        -------
        asyncWithStatement: ast.AsyncWith
            AST `object` representing an asynchronous context manager statement.
        """
        return ast.AsyncWith(items=list(items), body=list(body), **keywordArguments)

    @staticmethod
    def Attribute(value: ast.expr, *attribute: str, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
        """
        Attribute access AST `object` representing dot notation in Python code.
        (AI generated docstring)

        The `ast.Attribute` `object` represents attribute access using dot notation, such as
        `object.attribute` or chained access like `module.class.method`. This method
        supports chaining multiple attributes by passing additional attribute names.

        Parameters:
            value: The base expression before the first dot, typically an `ast.Name` or another expression.
            attribute: One or more attribute names to chain together with dot notation.
            context (`ast.Load()`): Are you loading from, storing to, or deleting the `ast.Attribute`?
                Values may be `ast.Load()`, `ast.Store()`, or `ast.Del()`, meaning 'Delete' the `ast.Attribute`.
                `context` corresponds to `ast.Attribute.ctx`.

        Returns
        -------
        attributeAccess: ast.Attribute
            AST `object` representing attribute access with potential chaining.
        """

        def addDOTattribute(chain: ast.expr, identifier: str, context: ast.expr_context, **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
            return ast.Attribute(value=chain, attr=identifier, ctx=context, **keywordArguments)
        buffaloBuffalo = addDOTattribute(value, attribute[0], context, **keywordArguments)
        for identifier in attribute[1:None]:
            buffaloBuffalo = addDOTattribute(buffaloBuffalo, identifier, context, **keywordArguments)
        return buffaloBuffalo

    @staticmethod
    def AugAssign(target: ast.Name | ast.Attribute | ast.Subscript, op: ast.operator, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.AugAssign:
        """
        Augmented assignment AST `object` for compound assignment operations.
        (AI generated docstring)

        The `ast.AugAssign` `object` represents augmented assignment operators like
        `+=`, `-=`, `*=`, `/=`, and others that combine an operation with assignment.
        These provide concise syntax for modifying variables in-place.

        Parameters:
            target: The assignment target being modified, which must be a name,
                attribute access, or subscript that supports in-place modification.
            op: The binary operator defining the augmentation operation, such as
                `ast.Add()` for `+=` or `ast.Mult()` for `*=`.
            value: The expression whose result will be combined with the target
                using the specified operator.

        Returns
        -------
        augmentedAssignment: ast.AugAssign
            AST `object` representing a compound assignment operation.
        """
        return ast.AugAssign(target=target, op=op, value=value, **keywordArguments)

    @staticmethod
    def Await(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Await:
        """
        Await expression AST `object` for asynchronous operations.
        (AI generated docstring)

        The `ast.Await` `object` represents the keyword `await` used with asynchronous
        expressions in Python. It can only be used within async functions and
        suspends execution until the awaited coroutine completes.

        Parameters:
            value: The expression to await, typically a coroutine or awaitable `object`.

        Returns
        -------
        awaitExpression: ast.Await
            AST `object` representing an await expression for asynchronous code.
        """
        return ast.Await(value=value, **keywordArguments)

    @staticmethod
    def BinOp(left: ast.expr, op: ast.operator, right: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.BinOp:
        """
        Binary operation AST `object` representing operators between two expressions.
        (AI generated docstring)

        The `ast.BinOp` `object` represents binary operations like addition, subtraction,
        multiplication, and other two-operand operations. The operation type is
        determined by the `op` parameter using specific operator classes.

        Parameters:
            left: The left-hand operand expression.
            op: The binary operator, such as `ast.Add()`, `ast.Sub()`, `ast.Mult()`, etc.
            right: The right-hand operand expression.

        Returns
        -------
        binaryOperation: ast.BinOp
            AST `object` representing a binary operation between two expressions.
        """
        return ast.BinOp(left=left, op=op, right=right, **keywordArguments)

    class BitAnd(ast.BitAnd):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitOr(ast.BitOr):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitXor(ast.BitXor):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def boolop() -> ast.boolop:
        """
        Base boolean operator abstract class for logical operations.
        (AI generated docstring)

        The `ast.boolop` class serves as the abstract base for boolean operators like
        `ast.And` and `ast.Or`. This method creates a minimal boolop instance, though
        in practice you will typically use specific boolean operator factories like
        `Make.And()`, `Make.Or()`, or their join methods.

        Most users seeking boolean operation creation should use the specific operator
        classes or `Make.BoolOp()` rather than this abstract base constructor.

        Returns:
            baseBooleanOperator: The fundamental boolean operator object from which
                concrete operators inherit.
        """
        return ast.boolop()

    @staticmethod
    def BoolOp(op: ast.boolop, values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.BoolOp:
        """
        Boolean operation AST `object` for logical operations with multiple operands.
        (AI generated docstring)

        The `ast.BoolOp` `object` represents boolean operations like keywords `and` and `or` that
        can operate on multiple expressions. Unlike binary operators, boolean operations
        can chain multiple values together efficiently.

        Parameters:
            op: The boolean operator, either `ast.And()` or `ast.Or()`.
            values: Sequence of expressions to combine with the boolean operator.

        Returns
        -------
        booleanOperation: ast.BoolOp
            AST `object` representing a boolean operation with multiple operands.
        """
        return ast.BoolOp(op=op, values=list(values), **keywordArguments)

    @staticmethod
    def Break(**keywordArguments: Unpack[ast_attributes]) -> ast.Break:
        """Create an `ast.Break` node for break statements.

        The `Break` node represents a `break` statement that terminates the
        nearest enclosing loop. Can only be used within loop constructs.

        Returns
            nodeBreak: The constructed break statement node
        """
        return ast.Break(**keywordArguments)

    @staticmethod
    def Call(callee: ast.expr, listParameters: Sequence[ast.expr]=[], list_keyword: Sequence[ast.keyword]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Call:
        """
        Function call AST `object` representing function invocation with arguments.
        (AI generated docstring)

        The `ast.Call` `object` represents function calls, method calls, and constructor
        invocations. It supports both positional and keyword arguments and handles
        various calling conventions including unpacking operators.

        Parameters:
            callee: The callable expression, typically a function name or method access.
            listParameters ([]): Sequence of positional argument expressions.
            list_keyword ([]): Sequence of keyword arguments as `ast.keyword`.

        Returns
        -------
        functionCall: ast.Call
            AST `object` representing a function call with specified arguments.
        """
        return ast.Call(func=callee, args=list(listParameters), keywords=list(list_keyword), **keywordArguments)

    @staticmethod
    def ClassDef(name: str, bases: Sequence[ast.expr]=[], list_keyword: Sequence[ast.keyword]=[], body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.ClassDef:
        """
        Class definition AST object for `class` declarations with inheritance and metadata.
        (AI generated docstring)

        The `ast.ClassDef` object represents class definitions including base classes,
        metaclass specifications, decorators, and the class body. Supports both
        traditional and modern Python class features.

        Parameters:
            name: Class name as string identifier.
            bases ([]): List of base class expressions for inheritance.
            list_keyword ([]): List of keyword arguments including metaclass specifications. This corresponds to `ast.ClassDef.keywords`.
            body ([]): List of statements forming the class body.
            decorator_list ([]): List of decorator expressions applied to class.
            type_params ([]): List of type parameters for generic classes (Python 3.12+).

        Returns:
            classDefinition: ast.ClassDef
            AST object representing a complete class definition with metadata.

        Examples:
            # Creates AST equivalent to: class Vehicle: pass
            simpleClass = Make.ClassDef('Vehicle', body=[Make.Pass()])

            # Creates AST equivalent to: class Bicycle(Vehicle, metaclass=ABCMeta): pass
            inheritedClass = Make.ClassDef(
                'Bicycle',
                bases=[Make.Name('Vehicle')],
                list_keyword=[Make.keyword('metaclass', Make.Name('ABCMeta'))],
                body=[Make.Pass()]
            )
        """
        return ast.ClassDef(name=name, bases=list(bases), keywords=list(list_keyword), body=list(body), decorator_list=list(decorator_list), type_params=list(type_params), **keywordArguments)

    @staticmethod
    def cmpop() -> ast.cmpop:
        """
        Abstract ***c***o***mp***arison ***op***erator `object` for use in AST construction.
        (AI generated docstring)

        Class `ast.cmpop` is the base for all comparison operators in Python's AST.
        It serves as the abstract parent for specific comparison operators: `ast.Eq`, `ast.NotEq`,
        `ast.Lt`, `ast.LtE`, `ast.Gt`, `ast.GtE`, `ast.Is`, `ast.IsNot`, `ast.In`, `ast.NotIn`.
        This factory method makes a generic comparison operator `object` that can be used
        in the antecedent-action pattern with visitor classes.

        Returns
        -------
        comparisonOperator: ast.cmpop
            Abstract comparison operator `object` that serves as the base `class` for all
            Python comparison operators in AST structures.
        """
        return ast.cmpop()

    @staticmethod
    def Compare(left: ast.expr, ops: Sequence[ast.cmpop], comparators: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Compare:
        """
        Comparison AST `object` for chained comparison operations.
        (AI generated docstring)

        The `ast.Compare` `object` represents comparison operations including equality,
        inequality, and ordering comparisons. It supports chained comparisons like
        `a < b <= c` through sequences of operators and comparators.

        All comparison operators: `ast.Eq`, `ast.NotEq`, `ast.Lt`, `ast.LtE`,
        `ast.Gt`, `ast.GtE`, `ast.Is`, `ast.IsNot`, `ast.In`, `ast.NotIn`.

        Parameters:
            left: The leftmost expression in the comparison chain.
            ops: Sequence of comparison operators from the complete list above.
            comparators: Sequence of expressions to compare against, one for each operator.

        Returns
        -------
        comparison: ast.Compare
            AST `object` representing a comparison operation with potential chaining.

        Examples
        --------
        ```python
        # Makes AST equivalent to: `x == 42`
        equality = Make.Compare(
            left=Make.Name('x'),
            ops=[Make.Eq()],
            comparators=[Make.Constant(42)]
        )

        # Makes AST equivalent to: `0 <= value < 100`
        rangeCheck = Make.Compare(
            left=Make.Constant(0),
            ops=[Make.LtE(), Make.Lt()],
            comparators=[Make.Name('value'), Make.Constant(100)]
        )
        ```
        """
        return ast.Compare(left=left, ops=list(ops), comparators=list(comparators), **keywordArguments)

    @staticmethod
    def comprehension(target: ast.expr, iter: ast.expr, ifs: Sequence[ast.expr], is_async: int) -> ast.comprehension:
        """
        Comprehension clause AST object for `for` clauses in list/set/dict comprehensions.
        (AI generated docstring)

        The `ast.comprehension` object represents individual `for` clauses within
        comprehension expressions. Contains the iteration target, source, conditional
        filters, and async specification for generator expressions.

        Parameters:
            target: Variable expression receiving each iteration value.
            iter: Iterable expression being traversed.
            ifs: List of conditional expressions filtering iteration results.
            is_async: Integer flag (0 or 1) indicating async comprehension.

        Returns:
            comprehensionClause: ast.comprehension
            AST object representing a single for clause in comprehensions.
        """
        return ast.comprehension(target=target, iter=iter, ifs=list(ifs), is_async=is_async)

    @staticmethod
    def Constant(value: ConstantValueType, kind: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Constant:
        """
        Constant value AST `object` for literal values in Python code.
        (AI generated docstring)

        The `ast.Constant` `object` represents literal constant values like numbers,
        strings, booleans, and None. It replaces the deprecated specific literal
        and provides a unified representation for all constant values.

        Parameters:
            value: The constant value (int, float, str, bool, None, bytes, etc.).
            kind (None): Optional string hint for specialized constant handling.

        Returns
        -------
        constantValue: ast.Constant
            AST `object` representing a literal constant value.
        """
        return ast.Constant(value=value, kind=kind, **keywordArguments)

    @staticmethod
    def Continue(**keywordArguments: Unpack[ast_attributes]) -> ast.Continue:
        """Create an `ast.Continue` node for continue statements.

        The `Continue` node represents a `continue` statement that skips the
        remainder of the current iteration and continues with the next iteration
        of the nearest enclosing loop.

        Returns
            nodeContinue: The constructed continue statement node
        """
        return ast.Continue(**keywordArguments)

    @staticmethod
    def Del() -> ast.Del:
        """
        Delete context for removing expressions from memory.
        (AI generated docstring)

        The `ast.Del` context indicates expressions are deletion targets in `del`
        statements. Note that `ast.Del` is the expression context, not the `del`
        keyword itself - `ast.Delete` represents the `del` statement.

        Returns:
            deleteContext: ast.Del
            AST context object indicating deletion operations on expressions.

        Examples:
            # Creates AST equivalent to deletion: del bicycle.wheel
            wheelDeletion = Make.Attribute(Make.Name('bicycle'), 'wheel', Make.Del())
        """
        return ast.Del()

    @staticmethod
    def Delete(targets: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Delete:
        """Create an `ast.Delete` node for deletion statements.

        The `Delete` node represents a `del` statement that removes references
        to objects. Can delete variables, attributes, subscripts, or slices.

        Parameters
            targets: List of expressions identifying what to delete

        Returns
            nodeDelete: The constructed deletion statement node
        """
        return ast.Delete(targets=list(targets), **keywordArguments)

    @staticmethod
    def Dict(keys: Sequence[ast.expr | None]=[None], values: Sequence[ast.expr]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Dict:
        """
        Dictionary literal AST `object` with key-value pairs.
        (AI generated docstring)

        The `ast.Dict` `object` represents dictionary literals using curly brace notation.
        It supports both regular key-value pairs and dictionary unpacking operations
        where keys can be None to indicate unpacking expressions.

        Parameters:
            keys ([None]): Sequence of key expressions or None for unpacking operations.
            values ([]): Sequence of value expressions corresponding to the keys.

        Returns
        -------
        dictionaryLiteral: ast.Dict
            AST `object` representing a dictionary literal with specified key-value pairs.
        """
        return ast.Dict(keys=list(keys), values=list(values), **keywordArguments)

    @staticmethod
    def DictComp(key: ast.expr, value: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.DictComp:
        """
        Dictionary comprehension AST `object` for dynamic dictionary construction.
        (AI generated docstring)

        The `ast.DictComp` `object` represents dictionary comprehensions that make
        dictionaries using iterator expressions. It combines key-value generation
        with filtering and nested iteration capabilities.

        Parameters:
            key: Expression that generates dictionary keys.
            value: Expression that generates dictionary values.
            generators: Sequence of `ast.comprehension` defining iteration and filtering.

        Returns
        -------
        dictionaryComprehension: ast.DictComp
            AST `object` representing a dictionary comprehension expression.

        Examples
        --------
        ```python
        # Makes AST equivalent to: `{x: x**2 for x in range(10)}`
        squares = Make.DictComp(
            key=Make.Name('x'),
            value=Make.BinOp(Make.Name('x'), Make.Pow(), Make.Constant(2)),
            generators=[Make.comprehension(
                target=Make.Name('x'),
                iter=Make.Call(Make.Name('range'), [Make.Constant(10)]),
                ifs=[]
            )]
        )
        ```
        """
        return ast.DictComp(key=key, value=value, generators=list(generators), **keywordArguments)

    class Div(ast.Div):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Eq() -> ast.Eq:
        """
        'Eq', meaning 'is ***Eq***ual to', is the `object` representation of Python comparison operator '`==`'.

        `class` `ast.Eq` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        equalityOperator:
            AST `object` representing the '`==`' equality comparison operator for use
            in `ast.Compare`.
        """
        return ast.Eq()

    @staticmethod
    def excepthandler(**keywordArguments: Unpack[ast_attributes]) -> ast.excepthandler:
        """
        Exception handler abstract base class for try-except constructs.
        (AI generated docstring)

        The `ast.excepthandler` abstract base class represents exception handling
        clauses in try-except statements. This is the foundation for `ast.ExceptHandler`
        which implements the actual exception catching logic.

        Returns:
            exceptionHandler: ast.excepthandler
            Abstract AST object for exception handling clause classification.
        """
        return ast.excepthandler(**keywordArguments)

    @staticmethod
    def ExceptHandler(type: ast.expr | None=None, name: str | None=None, body: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.ExceptHandler:
        """
        Exception handler clause for try-except statements.
        (AI generated docstring)

        The `ast.ExceptHandler` object represents individual `except` clauses that
        catch and handle specific exceptions. It defines the exception type to catch,
        optional variable binding, and statements to execute when matched.

        Parameters:
            type (None): Exception type expression to catch; None catches all exceptions.
            name (None): Variable name string to bind caught exception; None for no binding.
            body ([]): List of statements to execute when exception is caught.

        Returns:
            exceptionHandler: ast.ExceptHandler
            AST object representing an except clause in try-except statements.
        """
        return ast.ExceptHandler(type=type, name=name, body=list(body), **keywordArguments)

    @staticmethod
    def expr(**keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """
        Abstract ***expr***ession `object` for base expression operations.
        (AI generated docstring)

        The `ast.expr` class serves as the abstract base class for all expression
        objects in Python's AST. Unlike `ast.stmt` which represents statements that
        perform actions, `ast.expr` represents expressions that evaluate to values
        and can be used within larger expressions or as parts of statements.

        Expressions vs Statements:
        - **expr**: Evaluates to a value and can be composed into larger expressions.
          Examples include literals (`42`, `"hello"`), operations (`x + y`),
          function calls (`len(data)`), and attribute access (`obj.method`).
        - **stmt**: Performs an action and does not evaluate to a usable value.
          Examples include assignments (`x = 5`), control flow (`if`, `for`, `while`),
          function definitions (`def`), and imports (`import`).

        Returns
        -------
        expression: ast.expr
            Abstract expression `object` that serves as the base class for all
            Python expressions in AST structures.
        """
        return ast.expr(**keywordArguments)

    @staticmethod
    def Expr(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Expr:
        """Create an `ast.Expr` node for expression statements.

        The `Expr` node represents a statement that consists of a single expression
        whose value is discarded. This is used for expressions evaluated for their
        side effects rather than their return value.

        Parameters
            value: Expression to evaluate as a statement

        Returns
            nodeExpr: The constructed expression statement node
        """
        return ast.Expr(value=value, **keywordArguments)

    @staticmethod
    def expr_context() -> ast.expr_context:
        """
        Expression context abstract base class for expression usage patterns.
        (AI generated docstring)

        The `ast.expr_context` abstract base class represents how expressions are used
        in code: whether they load values, store values, or delete them. This is the
        foundation for `ast.Load`, `ast.Store`, and `ast.Del` contexts.

        Returns:
            expressionContext: ast.expr_context
            Abstract AST context object for expression usage classification.
        """
        return ast.expr_context()

    @staticmethod
    def Expression(body: ast.expr) -> ast.Expression:
        """Create an `ast.Expression` node for expression-only modules.

        The `Expression` node represents a module that contains only a single
        expression. This is used in contexts where only an expression is expected,
        such as with `eval()` or interactive mode single expressions.

        Parameters
            body: The single expression that forms the module body

        Returns
            nodeExpression: The constructed expression module node
        """
        return ast.Expression(body=body)

    class FloorDiv(ast.FloorDiv):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def For(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.For:
        """
        For loop AST `object` for iterating over iterable expressions.
        (AI generated docstring)

        The `ast.For` `object` represents traditional `for` loops that iterate over
        sequences, generators, or any iterable object. It supports optional else
        clauses that execute when the loop completes normally.

        Parameters:
            target: The loop variable that receives each item from the iterable expression.
            iter: The iterable expression being iterated over, such as a list, range, or generator.
            body: Sequence of statements executed for each iteration of the loop.
            orElse ([]): Optional statements executed when the loop completes normally
                without encountering a break statement. This corresponds to `ast.For.orelse`.

        Returns
        -------
        forLoop: ast.For
            AST `object` representing a for loop iteration construct.
        """
        return ast.For(target=target, iter=iter, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def FormattedValue(value: ast.expr, conversion: int, format_spec: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.FormattedValue:
        """
        Formatted value AST `object` for f-string interpolation components.
        (AI generated docstring)

        The `ast.FormattedValue` `object` represents individual expressions within
        f-string literals, including format specifications and conversion options.
        It handles the interpolation mechanics of formatted string literals.

        Parameters:
            value: The expression to be formatted and interpolated.
            conversion: Conversion flag (0=no conversion, 115='s', 114='r', 97='a').
            format_spec (None): Optional format specification expression.

        Returns
        -------
        formattedValue: ast.FormattedValue
            AST `object` representing a formatted value within an f-string expression.
        """
        return ast.FormattedValue(value=value, conversion=conversion, format_spec=format_spec, **keywordArguments)

    @staticmethod
    def FunctionDef(name: str, argumentSpecification: ast.arguments=ast.arguments(), body: Sequence[ast.stmt]=[], decorator_list: Sequence[ast.expr]=[], returns: ast.expr | None=None, type_params: Sequence[ast.type_param]=[], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.FunctionDef:
        """
        Function definition AST object for standard `def` declarations with typing support.
        (AI generated docstring)

        The `ast.FunctionDef` object represents standard function definitions including
        parameters, return annotations, decorators, and function body. Supports modern
        Python typing features and generic type parameters.

        Parameters:
            name: Function name as string identifier.
            argumentSpecification (ast.arguments()): Function parameter specification. This corresponds to `ast.FunctionDef.args`.
            body ([]): List of statements forming the function body.
            decorator_list ([]): List of decorator expressions applied to function.
            returns (None): Optional return type annotation expression.
            type_params ([]): List of type parameters for generic functions (Python 3.12+).

        Returns:
            functionDefinition: ast.FunctionDef
            AST object representing a complete function definition with metadata.

        Examples:
            # Creates AST equivalent to: def cook(): pass
            simpleFunction = Make.FunctionDef('cook', body=[Make.Pass()])

            # Creates AST equivalent to: def bake(recipe: str, temperature: int = 350) -> bool: return True
            typedFunction = Make.FunctionDef(
                'bake',
                Make.arguments(
                    list_arg=[Make.arg('recipe', Make.Name('str')), Make.arg('temperature', Make.Name('int'))],
                    defaults=[Make.Constant(350)]
                ),
                [Make.Return(Make.Constant(True))],
                returns=Make.Name('bool')
            )
        """
        return ast.FunctionDef(name=name, args=argumentSpecification, body=list(body), decorator_list=list(decorator_list), returns=returns, type_params=list(type_params), **keywordArguments)

    @staticmethod
    def FunctionType(argtypes: Sequence[ast.expr], returns: ast.expr) -> ast.FunctionType:
        """Create an `ast.FunctionType` node for function type annotations.

        The `FunctionType` node represents function type annotations of the form
        `(arg_types) -> return_type`. This is used in type annotations and
        variable annotations for callable types.

        Parameters
            argtypes: List of expressions representing argument types
            returns: Expression representing the return type

        Returns
            nodeFunctionType: The constructed function type annotation node
        """
        return ast.FunctionType(argtypes=list(argtypes), returns=returns)

    @staticmethod
    def GeneratorExp(element: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.GeneratorExp:
        """
        Generator ***expr***ession object for memory-efficient iteration.
        (AI generated docstring)

        The `ast.GeneratorExp` object represents generator expressions that create
        iterator objects without constructing intermediate collections. It provides
        lazy evaluation and memory efficiency for large datasets.

        Parameters:
            element: Expression that generates each element of the generator.
            generators: Sequence of `ast.comprehension` objects defining iteration and filtering.

        Returns
        -------
        generatorExpression: ast.GeneratorExp
            AST object representing a generator expression for lazy evaluation.

        Examples
        --------
        ```python
        # Creates AST equivalent to: `(x*2 for x in numbers if x > 0)`
        doubledPositive = Make.GeneratorExp(
            element=Make.BinOp(Make.Name('x'), Make.Mult(), Make.Constant(2)),
            generators=[Make.comprehension(
                target=Make.Name('x'),
                iter=Make.Name('numbers'),
                ifs=[Make.Compare(Make.Name('x'), [Make.Gt()], [Make.Constant(0)])]
            )]
        )
        ```
        """
        return ast.GeneratorExp(elt=element, generators=list(generators), **keywordArguments)

    @staticmethod
    def Global(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Global:
        """Create an `ast.Global` node for global declarations.

        The `Global` node represents a `global` statement that declares variables
        as referring to global scope rather than local scope. This affects variable
        lookup and assignment within the current function.

        Parameters
            names: List of variable names to declare as global

        Returns
            nodeGlobal: The constructed global declaration node
        """
        return ast.Global(names=names, **keywordArguments)

    @staticmethod
    def Gt() -> ast.Gt:
        """
        'Gt', meaning 'Greater than', is the `object` representation of Python operator '`>`'.

        `class` `ast.Gt` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        greaterThanOperator:
            AST `object` representing the '`>`' greater-than comparison operator for use
            in `ast.Compare`.
        """
        return ast.Gt()

    @staticmethod
    def GtE() -> ast.GtE:
        """
        'GtE', meaning 'is Greater than or Equal to', is the `object` representation of Python comparison operator '`>=`'.

        `class` `ast.GtE` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        greaterThanOrEqualOperator:
            AST `object` representing the '`>=`' greater-than-or-equal comparison operator
            for use in `ast.Compare`.
        """
        return ast.GtE()

    @staticmethod
    def If(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.If:
        """
        Conditional statement AST `object` for branching execution paths.
        (AI generated docstring)

        The `ast.If` `object` represents `if` statements that conditionally execute
        code blocks based on boolean test expressions. It supports optional else
        clauses for alternative execution paths.

        Parameters:
            test: The boolean expression that determines which branch to execute.
            body: Sequence of statements executed when the test expression evaluates to True.
            orElse ([]): Optional statements executed when the test expression evaluates
                to False. This corresponds to `ast.If.orelse`.

        Returns
        -------
        conditionalStatement: ast.If
            AST `object` representing a conditional branching statement.

        Examples
        --------
        ```python
        # Creates AST for: if userLoggedIn:
        #                     showDashboard()
        simpleIf = Make.If(
            Make.Name('userLoggedIn'),
            [Make.Expr(Make.Call(Make.Name('showDashboard')))]
        )

        # Creates AST for: if temperature > 100:
        #                     activateCooling()
        #                 else:
        #                     maintainTemperature()
        ifElse = Make.If(
            Make.Compare(Make.Name('temperature'), [Make.Gt()], [Make.Constant(100)]),
            [Make.Expr(Make.Call(Make.Name('activateCooling')))],
            [Make.Expr(Make.Call(Make.Name('maintainTemperature')))]
        )

        # Creates AST for nested if-elif-else chains
        ifElifElse = Make.If(
            Make.Compare(Make.Name('score'), [Make.GtE()], [Make.Constant(90)]),
            [Make.Assign([Make.Name('grade')], Make.Constant('A'))],
            [Make.If(
                Make.Compare(Make.Name('score'), [Make.GtE()], [Make.Constant(80)]),
                [Make.Assign([Make.Name('grade')], Make.Constant('B'))],
                [Make.Assign([Make.Name('grade')], Make.Constant('C'))]
            )]
        )
        ```
        """
        return ast.If(test=test, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def IfExp(test: ast.expr, body: ast.expr, orElse: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.IfExp:
        """
        Conditional ***expr***ession `object` for inline if-else operations.
        (AI generated docstring)

        The `ast.IfExp` `object` represents conditional expressions using the ternary
        operator syntax `value_if_true if condition else value_if_false`. It
        provides inline conditional logic without full if-statement structures.

        Parameters:
            test: The condition expression to evaluate for truthiness.
            body: Expression to return when the condition is true.
            orElse: Expression to return when the condition is false.

        Returns:
            conditionalExpression: ast.IfExp
                AST `object` representing an inline conditional expression.

        Examples:
            ```python
            # Creates AST equivalent to: `"positive" if x > 0 else "non-positive"`
            signDescription = Make.IfExp(
                test=Make.Compare(Make.Name('x'), [Make.Gt()], [Make.Constant(0)]),
                body=Make.Constant("positive"),
                orElse=Make.Constant("non-positive")
            )

            # Creates AST equivalent to: `max_value if enabled else default_value`
            conditionalValue = Make.IfExp(
                test=Make.Name('enabled'),
                body=Make.Name('max_value'),
                orElse=Make.Name('default_value')
            )
            ```
        """
        return ast.IfExp(test=test, body=body, orelse=orElse, **keywordArguments)

    @staticmethod
    def Import(dotModule: identifierDotAttribute, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Import:
        return ast.Import(names=[Make.alias(dotModule, asName)], **keywordArguments)

    @staticmethod
    def ImportFrom(dotModule: str | None, list_alias: list[ast.alias], level: int=0, **keywordArguments: Unpack[ast_attributes]) -> ast.ImportFrom:
        """
        From-import statement AST `object` for selective module imports.
        (AI generated docstring)

        The `ast.ImportFrom` `object` represents `from ... import` statements that
        selectively import specific names from modules. It supports relative imports
        and multiple import aliases.

        Parameters:
            dotModule: The source module name using dot notation, or None for relative
                imports that rely solely on the level parameter.
            list_alias: List of alias objects specifying which names to import and
                their optional aliases. This corresponds to `ast.ImportFrom.names`.
            level (0): Import level controlling relative vs absolute imports. Zero indicates
                absolute import, positive values indicate relative import depth.

        Returns
        -------
        fromImportStatement: ast.ImportFrom
            AST `object` representing a selective module import statement.
        """
        return ast.ImportFrom(module=dotModule, names=list_alias, level=level, **keywordArguments)

    @staticmethod
    def In() -> ast.In:
        """
        'In', meaning 'is ***In***cluded in' or 'has membership In', is the `object` representation of Python keyword '`in`'.

        `class` `ast.In` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***. The Python interpreter
        declares *This* `object` 'is ***In***cluded in' *That* `iterable` if *This* `object` matches a part of *That* `iterable`.

        Returns
        -------
        membershipOperator:
            AST `object` representing the keyword '`in`' membership test operator for use
            in `ast.Compare`.
        """
        return ast.In()

    @staticmethod
    def Interactive(body: Sequence[ast.stmt]) -> ast.Interactive:
        """Create an `ast.Interactive` node for interactive mode modules.

        The `Interactive` node represents a module intended for interactive
        execution, such as in the Python REPL. Unlike regular modules, interactive
        modules can contain multiple statements that are executed sequentially.

        Parameters
            body: List of statements forming the interactive module body

        Returns
            nodeInteractive: The constructed interactive module node
        """
        return ast.Interactive(body=list(body))

    @staticmethod
    def Invert() -> ast.Invert:
        """
        Bitwise complement operator representing Python '`~`' operator.
        (AI generated docstring)

        Class `ast.Invert` is a subclass of `ast.unaryop` and represents the bitwise complement
        or inversion operator '`~`' in Python source code. This operator performs bitwise
        NOT operation, flipping all bits of its operand. Used within `ast.UnaryOp`
        as the `op` parameter.

        Returns
        -------
        bitwiseComplementOperator: ast.Invert
            AST `object` representing the '`~`' bitwise complement operator for use
            in `ast.UnaryOp`.
        """
        return ast.Invert()

    @staticmethod
    def Is() -> ast.Is:
        """
        'Is', meaning 'Is identical to', is the `object` representation of Python keyword '`is`'.

        `class` `ast.Is` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        The Python interpreter declares *This* logical `object` 'Is identical to' *That* logical `object` if they use the same physical memory location. Therefore, modifying one `object` will necessarily modify the other `object`.

        What's the difference between equality and identity?
        - The work of Jane Austen 'is Equal to' the work of Franz Kafka.
        - The work of Mark Twain 'is Equal to' the work of Samuel Clemens.
        - And Mark Twain 'Is identical to' Samuel Clemens: because they are the same person.

        Returns
        -------
        identityOperator:
            AST `object` representing the '`is`' identity comparison operator for use in `ast.Compare`.

        Examples
        --------
        ```python
        # Logically equivalent to: `... valueAttributes is None ...`
        comparisonNode = Make.Compare(
            left=Make.Name('valueAttributes'),
            ops=[Make.Is()],
            comparators=[Make.Constant(None)]
        )
        ```

            In the first example, the two statements are logically equal but they cannot be identical.
        """
        return ast.Is()

    @staticmethod
    def IsNot() -> ast.IsNot:
        """
        'IsNot', meaning 'Is Not identical to', is the `object` representation of Python keywords '`is not`'.

        `class` `ast.IsNot` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        The Python interpreter declares *This* logical `object` 'Is Not identical to' *That* logical `object` if they do not use the same physical memory location.

        What's the difference between equality and identity?
        - The work of Jane Austen 'is Equal to' the work of Franz Kafka.
        - The work of Mark Twain 'is Equal to' the work of Samuel Clemens.
        - And Mark Twain 'Is identical to' Samuel Clemens: because they are the same person.

        Python programmers frequently use '`is not None`' because keyword `None` does not have a physical memory location, so `if chicken is not None`, `chicken` must have a physical memory location (and be in the current scope and blah blah blah...).

        Returns
        -------
        identityNegationOperator:
            AST `object` representing the '`is not`' identity comparison operator for use in `ast.Compare`.

        Examples
        --------
        ```python
        # Logically equivalent to: `... chicken is not None ...`
        comparisonNode = Make.Compare(
            left=Make.Name('chicken'),
            ops=[Make.IsNot()],
            comparators=[Make.Constant(None)]
        )
        ```

            In the first example, the two statements are logically equal but they cannot be identical.
        """
        return ast.IsNot()

    @staticmethod
    def JoinedStr(values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.JoinedStr:
        """
        Joined string `object` for f-string literal construction.
        (AI generated docstring)

        The `ast.JoinedStr` `object` represents f-string literals that combine constant
        text with interpolated expressions. It coordinates multiple string components
        and formatted values into a single string literal.

        Parameters:
            values: Sequence of string components, including `ast.Constant` and `ast.FormattedValue` objects.

        Returns
        -------
        joinedString: ast.JoinedStr
            AST `object` representing an f-string literal with interpolated values.
        """
        return ast.JoinedStr(values=list(values), **keywordArguments)

    @staticmethod
    @overload
    def keyword(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str | None, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword:
        ...

    @staticmethod
    @overload
    def keyword(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str | None=None, *, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword:
        ...

    @staticmethod
    def keyword(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str | None, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.keyword: # pyright: ignore[reportInconsistentOverload]
        """
        Keyword argument AST object for named parameters in function calls.
        (AI generated docstring)

        The `ast.keyword` object represents keyword arguments passed to function calls
        or class constructors. Contains the parameter name and corresponding value
        expression, including support for **kwargs unpacking.

        Parameters:
            Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: Parameter name string; None for **kwargs unpacking. This corresponds to `ast.keyword.arg`.
            value: Expression providing the argument value.

        Returns:
            keywordArgument: ast.keyword
            AST object representing a named argument in function calls.

        Examples:
            # Creates AST equivalent to: temperature=350
            namedArgument = Make.keyword('temperature', Make.Constant(350))

            # Creates AST equivalent to: **settings (kwargs unpacking)
            unpackedArguments = Make.keyword(None, Make.Name('settings'))
        """
        return ast.keyword(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, value=value, **keywordArguments)

    @staticmethod
    def Lambda(argumentSpecification: ast.arguments, body: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Lambda:
        """
        Lambda function `object` for anonymous function expressions.
        (AI generated docstring)

        The `ast.Lambda` `object` represents lambda expressions that define anonymous
        functions with a single expression body. Lambda functions are limited to
        expressions and cannot contain statements or multiple lines.

        Parameters:
            argumentSpecification: The function arguments specification as `ast.arguments`.
            body: Single expression that forms the lambda function body.

        Returns:
            lambdaFunction: ast.Lambda
                AST `object` representing an anonymous lambda function expression.
        """
        return ast.Lambda(args=argumentSpecification, body=body, **keywordArguments)

    @staticmethod
    def List(listElements: Sequence[ast.expr]=[], context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.List:
        """
        List literal `object` with ordered element collection.
        (AI generated docstring)

        The `ast.List` `object` represents list literals using square bracket notation.
        It creates ordered, mutable collections and supports various contexts like
        loading values, storing to variables, or deletion operations.

        Parameters:
            listElements ([]): Sequence of expressions that become list elements.
            context (ast.Load()): Expression context for how the list is used.

        Returns:
            listLiteral: ast.List
            AST `object` representing a list literal with specified elements.
        """
        return ast.List(elts=list(listElements), ctx=context, **keywordArguments)

    @staticmethod
    def ListComp(element: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.ListComp:
        """
        List ***c***o***mp***rehension `object` for dynamic list construction.
        (AI generated docstring)

        The `ast.ListComp` `object` represents list comprehensions that create lists
        using iterator expressions. It provides concise syntax for filtering and
        transforming collections into new lists.

        Parameters:
            element: Expression that generates each element of the resulting list.
            generators: Sequence of `ast.comprehension` objects defining iteration and filtering.

        Returns:
            listComprehension: ast.ListComp
            AST `object` representing a list comprehension expression.
        """
        return ast.ListComp(elt=element, generators=list(generators), **keywordArguments)

    @staticmethod
    def Load() -> ast.Load:
        """
        Load context for reading expression values.
        (AI generated docstring)

        The `ast.Load` context indicates expressions are being read or evaluated
        to retrieve their values. This is the default context for most expressions
        like `bicycle.wheel` when accessing the wheel attribute value.

        Returns:
            loadContext: ast.Load
            AST context object indicating value retrieval operations.
        """
        return ast.Load()

    class LShift(ast.LShift):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Lt() -> ast.Lt:
        """
        'Lt', meaning 'is Less than', is the `object` representation of Python comparison operator '`<`'.

        `class` `ast.Lt` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        lessThanOperator:
            AST `object` representing the '`<`' less-than comparison operator for use
            in `ast.Compare`.
        """
        return ast.Lt()

    @staticmethod
    def LtE() -> ast.LtE:
        """
        'LtE', meaning 'is Less than or Equal to', is the `object` representation of Python comparison operator '`<=`'.

        `class` `ast.LtE` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        lessThanOrEqualOperator:
            AST `object` representing the '`<=`' less-than-or-equal comparison operator
            for use in `ast.Compare`.
        """
        return ast.LtE()

    @staticmethod
    def Match(subject: ast.expr, cases: Sequence[ast.match_case]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Match:
        """
        Match statement AST object for pattern matching with multiple cases.
        (AI generated docstring)

        The `ast.Match` object represents match statements that perform pattern matching
        against a subject expression. Contains the value being matched and a list of
        case clauses with their patterns and corresponding actions.

        Parameters:
            subject: Expression being matched against the case patterns.
            cases ([]): List of match_case objects defining pattern-action pairs.

        Returns:
            matchStatement: ast.Match
            AST object representing a complete pattern matching statement.
        """
        return ast.Match(subject=subject, cases=list(cases), **keywordArguments)

    @staticmethod
    def match_case(pattern: ast.pattern, guard: ast.expr | None=None, body: Sequence[ast.stmt]=[]) -> ast.match_case:
        """
        Match case clause AST object for individual cases in `match` statements (**match** **case**).
        (AI generated docstring)

        The `ast.match_case` object represents individual case clauses within match
        statements. Contains the pattern to match, optional guard condition, and
        statements to execute when the pattern matches successfully.

        Parameters:
            pattern: Pattern expression defining what values match this case.
            guard (None): Optional conditional expression for additional filtering.
            body ([]): List of statements to execute when pattern matches.

        Returns:
            matchCase: ast.match_case
            AST object representing a single case clause in match statements.
        """
        return ast.match_case(pattern=pattern, guard=guard, body=list(body))

    @staticmethod
    def MatchAs(pattern: ast.pattern | None=None, name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchAs:
        """Create an `ast.MatchAs` node representing a capture pattern or wildcard.

        (AI generated docstring)

        The `ast.MatchAs` node represents match patterns that capture values or
        serve as wildcards. This includes bare name patterns like `bicycle` that
        capture the matched value, "as" patterns like `Point(x, y) as location`
        that match a pattern and capture the result, and the wildcard pattern `_`.

        Parameters:
            pattern: Optional pattern to match against. When `None`, creates a
                capture pattern (bare name) if `name` is provided, or wildcard
                if both are `None`.
            name: Optional identifier to bind the matched value. When `None` and
                pattern is also `None`, creates the wildcard pattern.

        Returns:
            matchAsNode: An `ast.MatchAs` node with the specified pattern and name.
        """
        return ast.MatchAs(pattern=pattern, name=name, **keywordArguments)

    @staticmethod
    def MatchClass(cls: ast.expr, patterns: Sequence[ast.pattern]=[], kwd_attrs: list[str]=[], kwd_patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchClass: # pyright: ignore[reportSelfClsParameterName]
        """Create an `ast.MatchClass` node for matching class instances.

        (AI generated docstring)

        The `ast.MatchClass` node represents patterns that match instances of a
        specific class, checking both the class type and extracting values from
        the instance's attributes. This enables structural pattern matching
        against objects.

        Parameters:
            cls: Expression identifying the class to match against, typically a
                `Make.Name` or `Make.Attribute` node.
            patterns ([]): Sequence of pattern nodes for positional matching
                against class-defined attributes.
            kwd_attrs ([]): List of attribute names for keyword-style matching.
                This corresponds to `ast.MatchClass.kwd_attrs`.
            kwd_patterns ([]): Sequence of pattern nodes corresponding to the
                keyword attributes. This corresponds to `ast.MatchClass.kwd_patterns`.

        Returns:
            matchClassNode: An `ast.MatchClass` node configured for the specified
                class and patterns.
        """
        return ast.MatchClass(cls=cls, patterns=list(patterns), kwd_attrs=kwd_attrs, kwd_patterns=list(kwd_patterns), **keywordArguments)

    @staticmethod
    def MatchMapping(keys: Sequence[ast.expr]=[], patterns: Sequence[ast.pattern]=[], rest: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchMapping:
        """Create an `ast.MatchMapping` node for matching dictionary-like objects.

        (AI generated docstring)

        The `ast.MatchMapping` node represents patterns that match mapping objects
        like dictionaries, checking for specific keys and extracting their values.
        The pattern can also capture remaining unmapped keys.

        Parameters:
            keys ([]): Sequence of expression nodes representing the keys to match.
                Each key expression is evaluated and must be present in the mapping.
            patterns ([]): Sequence of pattern nodes corresponding to the values
                associated with each key.
            rest: Optional identifier name to capture remaining mapping elements
                not matched by the specified keys.

        Returns:
            matchMappingNode: An `ast.MatchMapping` node for the specified key-value
                patterns and optional rest capture.
        """
        return ast.MatchMapping(keys=list(keys), patterns=list(patterns), rest=rest, **keywordArguments)

    @staticmethod
    def MatchOr(patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchOr:
        """Create an `ast.MatchOr` node for alternative pattern matching.

        (AI generated docstring)

        The `ast.MatchOr` node represents or-patterns that match if any of the
        alternative subpatterns succeed. The pattern tries each alternative in
        sequence until one matches or all fail.

        Parameters:
            patterns ([]): Sequence of alternative pattern nodes. The match
                succeeds if any subpattern matches the subject.

        Returns:
            matchOrNode: An `ast.MatchOr` node containing the alternative patterns.
        """
        return ast.MatchOr(patterns=list(patterns), **keywordArguments)

    @staticmethod
    def MatchSequence(patterns: Sequence[ast.pattern]=[], **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSequence:
        """Create an `ast.MatchSequence` node for matching sequences.

        (AI generated docstring)

        The `ast.MatchSequence` node represents patterns that match sequence objects
        like lists and tuples, checking both length and element patterns. Supports
        both fixed-length and variable-length sequence matching.

        Parameters:
            patterns ([]): Sequence of pattern nodes to match against sequence
                elements. If any pattern is `MatchStar`, enables variable-length
                matching; otherwise requires exact length match.

        Returns:
            matchSequenceNode: An `ast.MatchSequence` node for the specified element
                patterns.
        """
        return ast.MatchSequence(patterns=list(patterns), **keywordArguments)

    @staticmethod
    def MatchSingleton(value: bool | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSingleton:
        """Create an `ast.MatchSingleton` node for matching singleton values.

        (AI generated docstring)

        The `ast.MatchSingleton` node represents patterns that match singleton
        constants by identity rather than equality. This pattern succeeds only
        if the match subject is the exact same object as the specified constant.

        Parameters:
            value: The singleton constant to match against. Must be `None`, `True`,
                or `False`. Matching uses identity comparison (`is`) rather than
                equality comparison (`==`).

        Returns:
            matchSingletonNode: An `ast.MatchSingleton` node for the specified
                singleton value.
        """
        return ast.MatchSingleton(value=value, **keywordArguments)

    @staticmethod
    def MatchStar(name: str | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchStar:
        """Create an `ast.MatchStar` node for capturing sequence remainder.

        (AI generated docstring)

        The `ast.MatchStar` node represents star patterns that capture remaining
        elements in variable-length sequence patterns. This enables flexible
        sequence matching where some elements are specifically matched and others
        are collected.

        Parameters:
            name: Optional identifier to bind the remaining sequence elements.
                When `None`, the remaining elements are matched but not captured.

        Returns:
            matchStarNode: An `ast.MatchStar` node with the specified capture name.
        """
        return ast.MatchStar(name=name, **keywordArguments)

    @staticmethod
    def MatchValue(value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchValue:
        """Create an `ast.MatchValue` node for matching literal values.

        (AI generated docstring)

        The `ast.MatchValue` node represents patterns that match by equality
        comparison against a literal value or expression. The pattern succeeds
        if the match subject equals the evaluated value expression.

        Parameters:
            value: Expression node representing the value to match against.
                Typically a constant, name, or attribute access. The expression
                is evaluated and compared using equality (`==`).

        Returns:
            matchValueNode: An `ast.MatchValue` node for the specified value
                expression.
        """
        return ast.MatchValue(value=value, **keywordArguments)

    class MatMult(ast.MatMult):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def mod() -> ast.mod:
        """Create an appropriate `ast.mod` node based on the body content.

        The `mod` method creates the appropriate module type node based on the
        provided body. This is a convenience method that determines whether to
        create a `Module`, `Expression`, or `Interactive` node.

        Parameters
            body: Either a list of statements or a single expression

        Returns
            nodeMod: The constructed module node of appropriate type
        """
        return ast.mod()

    class Mod(ast.Mod):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Module(body: Sequence[ast.stmt], type_ignores: list[ast.TypeIgnore]=[]) -> ast.Module:
        """
        Module AST object representing complete Python modules with statements and type ignores.
        (AI generated docstring)

        The `ast.Module` object represents entire Python modules as parsed from source
        files. Contains all top-level statements and tracks type ignore comments for
        static analysis tools and type checkers.

        Parameters:
            body: List of statements forming the module content.
            type_ignores ([]): List of TypeIgnore objects for `# type: ignore` comments.

        Returns:
            moduleDefinition: ast.Module
            AST object representing a complete Python module structure.

        Examples:
            # Creates AST equivalent to: x = 42
            simpleModule = Make.Module([Make.Assign([Make.Name('x')], Make.Constant(42))])

            # Creates AST equivalent to module with function and assignment
            moduleWithFunction = Make.Module([
                Make.FunctionDef('calculate', body=[Make.Return(Make.Constant(100))]),
                Make.Assign([Make.Name('result')], Make.Call(Make.Name('calculate'), []))
            ])
        """
        return ast.Module(body=list(body), type_ignores=type_ignores)

    class Mult(ast.Mult):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Name(id: str, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Name:
        """
        Name `object` for variable and identifier references.
        (AI generated docstring)

        The `ast.Name` `object` represents identifiers like variable names, function names,
        and class names in Python code. The context parameter determines whether the
        name is being loaded, stored to, or deleted.

        Parameters:
            id: The identifier string representing the name.
            context (ast.Load()): Expression context specifying how the name is used.

        Returns:
            nameReference: ast.Name
            AST `object` representing an identifier reference with specified context.
        """
        return ast.Name(id=id, ctx=context, **keywordArguments)

    @staticmethod
    def NamedExpr(target: ast.Name, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.NamedExpr:
        """
        Named ***expr***ession `object` for assignment expressions (walrus operator).
        (AI generated docstring)

        The `ast.NamedExpr` `object` represents assignment expressions using the walrus
        operator `:=` introduced in Python 3.8. It allows assignment within expressions
        and is commonly used in comprehensions and conditional statements.

        Parameters:
            target: The `ast.Name` `object` representing the variable being assigned to.
            value: The expression whose value is assigned to the target.

        Returns:
            namedExpression: ast.NamedExpr
            AST `object` representing an assignment expression with the walrus operator.

        Examples:
            ```python
            # Creates AST equivalent to: `(length := len(data)) > 10`
            lengthCheck = Make.Compare(
                left=Make.NamedExpr(
                    target=Make.Name('length', ast.Store()),
                    value=Make.Call(Make.Name('len'), [Make.Name('data')])
                ),
                ops=[Make.Gt()],
                comparators=[Make.Constant(10)]
            )
            ```
        """
        return ast.NamedExpr(target=target, value=value, **keywordArguments)

    @staticmethod
    def Nonlocal(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Nonlocal:
        """Create an `ast.Nonlocal` node for nonlocal declarations.

        The `Nonlocal` node represents a `nonlocal` statement that declares
        variables as referring to the nearest enclosing scope that is not global.
        This is used in nested functions to modify variables from outer scopes.

        Parameters
            names: List of variable names to declare as nonlocal

        Returns
            nodeNonlocal: The constructed nonlocal declaration node
        """
        return ast.Nonlocal(names=names, **keywordArguments)

    @staticmethod
    def Not() -> ast.Not:
        """
        Logical negation operator representing Python keyword '`not`'.
        (AI generated docstring)

        Class `ast.Not` is a subclass of `ast.unaryop` and represents the logical negation
        operator keyword '`not`' in Python source code. This operator returns the boolean
        inverse of its operand's truthiness. Used within `ast.UnaryOp` as the
        `op` parameter.

        Returns
        -------
        logicalNegationOperator: ast.Not
            AST `object` representing the keyword '`not`' logical negation operator for use
            in `ast.UnaryOp`.
        """
        return ast.Not()

    @staticmethod
    def NotEq() -> ast.NotEq:
        """
        'NotEq' meaning 'is ***Not*** ***Eq***ual to', is the `object` representation of Python comparison operator '`!=`'.

        `class` `ast.NotEq` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        inequalityOperator:
            AST `object` representing the '`!=`' inequality comparison operator for use
            in `ast.Compare`.
        """
        return ast.NotEq()

    @staticmethod
    def NotIn() -> ast.NotIn:
        """
        'NotIn', meaning 'is Not ***In***cluded in' or 'does Not have membership In', is the `object` representation of Python keywords '`not in`'.

        `class` `ast.NotIn` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and
        only used in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***. The Python interpreter
        declares *This* `object` 'is Not ***In***cluded in' *That* `iterable` if *This* `object` does not match a part of *That* `iterable`.

        Returns
        -------
        negativeMembershipOperator:
            AST `object` representing the keywords '`not in`' negative membership test operator
            for use in `ast.Compare`.
        """
        return ast.NotIn()

    @staticmethod
    def operator() -> ast.operator:
        """Create an `ast.operator` node for arithmetic and bitwise operations.

        The `operator` method creates operator nodes used in binary operations,
        unary operations, and comparison operations. These represent the specific
        operation to be performed.

        Parameters
            op_type: The operator class to instantiate

        Returns
            nodeOperator: The constructed operator node
        """
        return ast.operator()

    class Or(ast.Or):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BoolOp` class."""

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a sequence of `ast.expr` by forming an `ast.BoolOp` that logically "joins" expressions using the `ast.BoolOp` subclass.

        Like str.join() but for AST expressions.

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
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)
    match sys.version_info:
        case version if version >= (3, 13):

            @staticmethod
            def ParamSpec(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec: # pyright: ignore[reportRedeclaration]
                """
        Parameter specification type parameter for generic callable types (**Param**eter **Spec**ification).
        (AI generated docstring)

        The `ast.ParamSpec` object represents parameter specification type parameters
        used in generic callable types. Captures both positional and keyword argument
        signatures for type-safe function composition and higher-order functions.

        Parameters:
            name: Type parameter name as string identifier.
            default_value (None): Optional default type expression (Python 3.13+).

        Returns:
            parameterSpecification: ast.ParamSpec
            AST object representing a parameter specification type parameter.
        """
                return ast.ParamSpec(name=name, default_value=default_value, **keywordArguments)
        case _:

            @staticmethod
            def ParamSpec(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
                """
        Parameter specification type parameter for generic callable types (**Param**eter **Spec**ification).
        (AI generated docstring)

        The `ast.ParamSpec` object represents parameter specification type parameters
        used in generic callable types. Captures both positional and keyword argument
        signatures for type-safe function composition and higher-order functions.

        Parameters:
            name: Type parameter name as string identifier.
            default_value (None): Optional default type expression (Python 3.13+).

        Returns:
            parameterSpecification: ast.ParamSpec
            AST object representing a parameter specification type parameter.
        """
                return ast.ParamSpec(name=name, **keywordArguments)

    @staticmethod
    def Pass(**keywordArguments: Unpack[ast_attributes]) -> ast.Pass:
        """Create an `ast.Pass` node for pass statements.

        The `Pass` node represents a `pass` statement, which is a null operation
        that does nothing when executed. It serves as syntactic placeholder where
        a statement is required but no action is needed.

        Returns
            nodePass: The constructed pass statement node
        """
        return ast.Pass(**keywordArguments)

    @staticmethod
    def pattern(**keywordArguments: Unpack[ast_attributes_int]) -> ast.pattern:
        """Create a base `ast.pattern` node.

        (AI generated docstring)

        Creates a generic `ast.pattern` node that serves as the abstract base
        for all pattern types in match statements. This method is typically
        used for creating pattern node instances programmatically when the
        specific pattern type is determined at runtime.

        Returns:
            patternNode: A base `ast.pattern` node with the specified attributes.
        """
        return ast.pattern(**keywordArguments)

    class Pow(ast.Pow):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Raise(exc: ast.expr | None=None, cause: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Raise:
        """Create an `ast.Raise` node for raise statements.

        The `Raise` node represents a `raise` statement that raises an exception.
        Can re-raise the current exception, raise a new exception, or raise with
        an explicit cause chain.

        Parameters
            exc (None): Optional expression for the exception to raise
            cause (None): Optional expression for the exception cause

        Returns
            nodeRaise: The constructed raise statement node
        """
        return ast.Raise(exc=exc, cause=cause, **keywordArguments)

    @staticmethod
    def Return(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Return:
        """
        Return statement AST object for function value returns and early exits.
        (AI generated docstring)

        The `ast.Return` object represents return statements that exit functions and
        optionally provide return values. Used for both value-returning functions
        and procedures that return None implicitly or explicitly.

        Parameters:
            value (None): Optional expression providing the return value; None for empty return.

        Returns:
            returnStatement: ast.Return
            AST object representing a function return with optional value.
        """
        return ast.Return(value=value, **keywordArguments)

    class RShift(ast.RShift):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Set(listElements: Sequence[ast.expr]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Set:
        """
        Set literal `object` for unordered unique element collections.
        (AI generated docstring)

        The `ast.Set` `object` represents set literals using curly brace notation.
        It creates unordered collections of unique elements with efficient
        membership testing and set operations.

        Parameters:
            listElements ([]): Sequence of expressions that become set elements.

        Returns:
            setLiteral: ast.Set
            AST `object` representing a set literal with specified unique elements.
        """
        return ast.Set(elts=list(listElements), **keywordArguments)

    @staticmethod
    def SetComp(element: ast.expr, generators: Sequence[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.SetComp:
        """
        Set ***c***o***mp***rehension `object` for dynamic set construction.
        (AI generated docstring)

        The `ast.SetComp` `object` represents set comprehensions that create sets
        using iterator expressions. It automatically handles uniqueness while
        providing concise syntax for filtering and transforming collections.

        Parameters:
            element: Expression that generates each element of the resulting set.
            generators: Sequence of `ast.comprehension` objects defining iteration and filtering.

        Returns:
            setComprehension: ast.SetComp
            AST `object` representing a set comprehension expression.
        """
        return ast.SetComp(elt=element, generators=list(generators), **keywordArguments)

    @staticmethod
    def Slice(lower: ast.expr | None=None, upper: ast.expr | None=None, step: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Slice:
        """
        Slice `object` for sequence slicing operations.
        (AI generated docstring)

        The `ast.Slice` `object` represents slice expressions used with subscription
        operations to extract subsequences from collections. It supports the full
        Python slicing syntax with optional start, stop, and step parameters.

        Parameters:
            lower (None): Optional expression for slice start position.
            upper (None): Optional expression for slice end position.
            step (None): Optional expression for slice step size.

        Returns:
            sliceExpression: ast.Slice
            AST `object` representing a slice operation for sequence subscripting.
        """
        return ast.Slice(lower=lower, upper=upper, step=step, **keywordArguments)

    @staticmethod
    def Starred(value: ast.expr, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Starred:
        """
        Starred ***expr***ession `object` for unpacking operations.
        (AI generated docstring)

        The `ast.Starred` `object` represents starred expressions using the `*` operator
        for unpacking iterables in various contexts like function calls, assignments,
        and collection literals.

        Parameters:
            value: The expression to be unpacked with the star operator.
            context (ast.Load()): Expression context determining how the starred expression is used.

        Returns:
            starredExpression: ast.Starred
            AST `object` representing a starred expression for unpacking operations.

        Examples:
            ```python
            # Creates AST equivalent to: `*args` in function call
            unpackArgs = Make.Starred(Make.Name('args'))

            # Creates AST equivalent to: `*rest` in assignment like `first, *rest = items`
            unpackRest = Make.Starred(Make.Name('rest'), ast.Store())
            ```
        """
        return ast.Starred(value=value, ctx=context, **keywordArguments)

    @staticmethod
    def stmt(**keywordArguments: Unpack[ast_attributes]) -> ast.stmt:
        """Create a statement node of the specified type.

        The `stmt` method provides a generic interface for creating any statement
        node type. This is a convenience method that delegates to the appropriate
        specific constructor based on the statement type.

        Parameters
            stmt_type: The statement class to instantiate
            **kwargs: Keyword arguments specific to the statement type

        Returns
            nodeStmt: The constructed statement node
        """
        return ast.stmt(**keywordArguments)

    @staticmethod
    def Store() -> ast.Store:
        """
        Store context for assigning values to expressions.
        (AI generated docstring)

        The `ast.Store` context indicates expressions are assignment targets
        receiving new values. Used in assignments, loop targets, and function
        parameters where expressions store rather than load values.

        Returns:
            storeContext: ast.Store
            AST context object indicating value assignment operations.

        Examples:
            # Creates AST equivalent to assignment: bicycle.wheel = newWheel
            wheelAssignment = Make.Attribute(Make.Name('bicycle'), 'wheel', Make.Store())
        """
        return ast.Store()

    class Sub(ast.Sub):
        """Identical to the `ast` class but with a method, `join()`, that "joins" expressions using the `ast.BinOp` class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """
        Single `ast.expr` from a collection of `ast.expr` by forming nested `ast.BinOp` that are logically "joined" using the `ast.operator` subclass.

        Like str.join() but for AST expressions.

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
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Subscript(value: ast.expr, slice: ast.expr, context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Subscript:
        """
        Subscript `object` for indexing and slicing operations.
        (AI generated docstring)

        The `ast.Subscript` `object` represents subscription operations using square
        brackets for indexing, slicing, and key access in dictionaries and other
        subscriptable objects.

        Parameters:
            value: The expression being subscripted (e.g., list, dict, string).
            slice: The subscript expression, which can be an index, slice, or key.
            context (ast.Load()): Expression context for how the subscript is used.

        Returns:
            subscriptExpression: ast.Subscript
            AST `object` representing a subscription operation with brackets.
        """
        return ast.Subscript(value=value, slice=slice, ctx=context, **keywordArguments)

    @staticmethod
    def Try(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt]=[], finalbody: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.Try:
        """
        Try-except statement AST `object` for exception handling and resource cleanup.
        (AI generated docstring)

        The `ast.Try` `object` represents `try-except` statements that handle exceptions
        and provide cleanup mechanisms. It supports multiple exception handlers, optional
        else clauses, and finally blocks for guaranteed cleanup.

        Parameters:
            body: Sequence of statements in the try block that may raise exceptions.
            handlers: List of exception handler objects that catch and process specific
                exception types or patterns.
            orElse ([]): Optional statements executed when the try block completes without
                raising exceptions. This corresponds to `ast.Try.orelse`.
            finalbody ([]): Optional statements always executed for cleanup, regardless
                of whether exceptions occurred. This corresponds to `ast.Try.finalbody`.

        Returns
        -------
        tryStatement: ast.Try
            AST `object` representing an exception handling statement with optional cleanup.
        """
        return ast.Try(body=list(body), handlers=handlers, orelse=list(orElse), finalbody=list(finalbody), **keywordArguments)

    @staticmethod
    def TryStar(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt]=[], finalbody: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.TryStar:
        """
        Try-except* statement AST `object` for exception group handling.
        (AI generated docstring)

        The `ast.TryStar` `object` represents `try-except*` statements introduced in
        Python 3.11 for handling exception groups. It enables catching and processing
        multiple related exceptions that occur simultaneously.

        Parameters:
            body: Sequence of statements in the try block that may raise exception groups.
            handlers: List of exception handler objects that catch and process specific
                exception types within exception groups.
            orElse ([]): Optional statements executed when the try block completes without
                raising exceptions. This corresponds to `ast.TryStar.orelse`.
            finalbody ([]): Optional statements always executed for cleanup, regardless
                of whether exception groups occurred. This corresponds to `ast.TryStar.finalbody`.

        Returns
        -------
        tryStarStatement: ast.TryStar
            AST `object` representing an exception group handling statement with optional cleanup.
        """
        return ast.TryStar(body=list(body), handlers=handlers, orelse=list(orElse), finalbody=list(finalbody), **keywordArguments)

    @staticmethod
    def Tuple(listElements: Sequence[ast.expr]=[], context: ast.expr_context=ast.Load(), **keywordArguments: Unpack[ast_attributes]) -> ast.Tuple:
        """
        Tuple literal `object` for ordered immutable collections.
        (AI generated docstring)

        The `ast.Tuple` `object` represents tuple literals using parentheses or comma
        separation. Tuples are immutable, ordered collections often used for
        multiple assignments and function return values.

        Parameters:
            listElements ([]): Sequence of expressions that become tuple elements.
            context (ast.Load()): Expression context for how the tuple is used.

        Returns:
            tupleLiteral: ast.Tuple
            AST `object` representing a tuple literal with specified elements.
        """
        return ast.Tuple(elts=list(listElements), ctx=context, **keywordArguments)

    @staticmethod
    def type_ignore() -> ast.type_ignore:
        """Create an `ast.type_ignore` node for type checker ignore comments.

        The `type_ignore` node represents type checker ignore directives that
        suppress type checking warnings for specific lines. This is used with
        comments like `# type: ignore`.

        Parameters
            lineno: Line number where the ignore directive applies
            tag: Tag identifying the specific type ignore directive

        Returns
            nodeTypeIgnore: The constructed type ignore node
        """
        return ast.type_ignore()

    @staticmethod
    def type_param(**keywordArguments: Unpack[ast_attributes_int]) -> ast.type_param:
        """
        Abstract type parameter base for generic type constructs (**type** **param**eter).
        (AI generated docstring)

        The `ast.type_param` object serves as the abstract base for type parameters
        including TypeVar, ParamSpec, and TypeVarTuple. Provides common functionality
        for generic type definitions in classes, functions, and type aliases.

        Returns:
            typeParameter: ast.type_param
            Abstract AST object representing the base of type parameter hierarchy.
        """
        return ast.type_param(**keywordArguments)

    @staticmethod
    @overload
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param]=[], *, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.TypeAlias:
        ...

    @staticmethod
    @overload
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.TypeAlias:
        ...

    @staticmethod
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias: # pyright: ignore[reportInconsistentOverload]
        """
        Type alias definition AST object for `type` statement declarations.
        (AI generated docstring)

        The `ast.TypeAlias` object represents type alias definitions using the `type`
        statement syntax. Associates a name with a type expression, supporting
        generic type parameters for flexible type definitions.

        Parameters:
            name: Name expression (typically ast.Name) for the alias identifier.
            type_params ([]): List of type parameters for generic aliases.
            value: Type expression defining what the alias represents.

        Returns:
            typeAliasDefinition: ast.TypeAlias
            AST object representing a complete type alias declaration.
        """
        return ast.TypeAlias(name=name, type_params=list(type_params), value=value, **keywordArguments)

    @staticmethod
    def TypeIgnore(lineno: int, tag: str) -> ast.TypeIgnore:
        """
        Type ignore comment AST object for `# type: ignore` directives.
        (AI generated docstring)

        The `ast.TypeIgnore` object represents `# type: ignore` comments that
        instruct static type checkers to skip type analysis for specific lines.
        Includes optional tags for categorizing different types of ignores.

        Parameters:
            lineno: Line number where the ignore comment appears.
            tag: Optional string tag for categorizing the ignore (e.g., '[assignment]').

        Returns:
            typeIgnoreDirective: ast.TypeIgnore
            AST object representing a type checker ignore comment.

        Examples:
            # Creates AST equivalent to: # type: ignore (on line 42)
            simpleIgnore = Make.TypeIgnore(42, '')

            # Creates AST equivalent to: # pyright: ignore[assignment] (on line 15)
            taggedIgnore = Make.TypeIgnore(15, '[assignment]')
        """
        return ast.TypeIgnore(lineno=lineno, tag=tag)
    match sys.version_info:
        case version if version >= (3, 13):

            @staticmethod
            def TypeVar(name: str, bound: ast.expr | None=None, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar: # pyright: ignore[reportRedeclaration]
                """
        Type variable parameter for generic types with optional bounds and defaults (**Type** **Var**iable).
        (AI generated docstring)

        The `ast.TypeVar` object represents type variable parameters used in generic
        classes, functions, and type aliases. Supports type bounds, constraints,
        and default values for flexible generic programming.

        Parameters:
            name: Type variable name as string identifier.
            bound (None): Optional type expression constraining allowed types.
            default_value (None): Optional default type expression (Python 3.13+).

        Returns:
            typeVariable: ast.TypeVar
            AST object representing a type variable with optional constraints.
        """
                return ast.TypeVar(name=name, bound=bound, default_value=default_value, **keywordArguments)
        case _:

            @staticmethod
            def TypeVar(name: str, bound: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
                """
        Type variable parameter for generic types with optional bounds and defaults (**Type** **Var**iable).
        (AI generated docstring)

        The `ast.TypeVar` object represents type variable parameters used in generic
        classes, functions, and type aliases. Supports type bounds, constraints,
        and default values for flexible generic programming.

        Parameters:
            name: Type variable name as string identifier.
            bound (None): Optional type expression constraining allowed types.
            default_value (None): Optional default type expression (Python 3.13+).

        Returns:
            typeVariable: ast.TypeVar
            AST object representing a type variable with optional constraints.
        """
                return ast.TypeVar(name=name, bound=bound, **keywordArguments)
    match sys.version_info:
        case version if version >= (3, 13):

            @staticmethod
            def TypeVarTuple(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple: # pyright: ignore[reportRedeclaration]
                """
        Type variable tuple for variadic generic types (**Type** **Var**iable **Tuple**).
        (AI generated docstring)

        The `ast.TypeVarTuple` object represents type variable tuples used for
        variadic generic types that accept variable numbers of type arguments.
        Enables generic types that work with arbitrary-length type sequences.

        Parameters:
            name: Type variable tuple name as string identifier.
            default_value (None): Optional default type tuple expression (Python 3.13+).

        Returns:
            typeVariableTuple: ast.TypeVarTuple
            AST object representing a variadic type variable.
        """
                return ast.TypeVarTuple(name=name, default_value=default_value, **keywordArguments)
        case _:

            @staticmethod
            def TypeVarTuple(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
                """
        Type variable tuple for variadic generic types (**Type** **Var**iable **Tuple**).
        (AI generated docstring)

        The `ast.TypeVarTuple` object represents type variable tuples used for
        variadic generic types that accept variable numbers of type arguments.
        Enables generic types that work with arbitrary-length type sequences.

        Parameters:
            name: Type variable tuple name as string identifier.
            default_value (None): Optional default type tuple expression (Python 3.13+).

        Returns:
            typeVariableTuple: ast.TypeVarTuple
            AST object representing a variadic type variable.
        """
                return ast.TypeVarTuple(name=name, **keywordArguments)

    @staticmethod
    def UAdd() -> ast.UAdd:
        """
        'UAdd', meaning 'Unary Addition', operator representing Python '`+`' operator.
        (AI generated docstring)

        Class `ast.UAdd` is a subclass of `ast.unaryop` and represents the unary positive
        operator '`+`' in Python source code. This operator explicitly indicates
        a positive numeric value. Used within `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        unaryPositiveOperator: ast.UAdd
            AST `object` representing the '`+`' unary positive operator for use
            in `ast.UnaryOp`.
        """
        return ast.UAdd()

    @staticmethod
    def unaryop() -> ast.unaryop:
        """
        Abstract ***un***ary ***op***erator `object` for use in AST construction.
        (AI generated docstring)

        Class `ast.unaryop` is the base for all unary operators in Python's AST.
        It serves as the abstract parent for specific unary operators: `ast.Invert`,
        `ast.Not`, `ast.UAdd`, `ast.USub`. This factory method makes a generic
        unary operator `object` that can be used in the antecedent-action pattern with visitor classes.

        Unlike `ast.cmpop` which handles binary comparison operations between two operands,
        `ast.unaryop` represents operators that act on a single operand. Both serve as abstract
        base classes but for different categories of operations: `ast.cmpop` for comparisons
        and `ast.unaryop` for unary transformations.

        Returns
        -------
        unaryOperator: ast.unaryop
            Abstract unary operator `object` that serves as the base `class` for all
            Python unary operators in AST structures.
        """
        return ast.unaryop()

    @staticmethod
    def UnaryOp(op: ast.unaryop, operand: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.UnaryOp:
        """
        Unary ***op***eration `object` for single-operand operations.
        (AI generated docstring)

        The `ast.UnaryOp` `object` represents unary operations that take a single operand,
        such as negation, logical not, bitwise inversion, and positive sign operations.

        Parameters:
            op: The unary operator like `ast.UAdd()`, `ast.USub()`, `ast.Not()`, `ast.Invert()`.
            operand: The expression that the unary operator is applied to.

        Returns:
            unaryOperation: ast.UnaryOp
            AST `object` representing a unary operation on a single expression.
        """
        return ast.UnaryOp(op=op, operand=operand, **keywordArguments)

    @staticmethod
    def USub() -> ast.USub:
        """
        'USub', meaning 'Unary Subtraction', operator representing Python '`-`' operator.
        (AI generated docstring)

        Class `ast.USub` is a subclass of `ast.unaryop` and represents the unary negation
        operator '`-`' in Python source code. This operator makes the arithmetic
        negative of its operand. Used within `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        unaryNegativeOperator: ast.USub
            AST `object` representing the '`-`' unary negation operator for use
            in `ast.UnaryOp`.
        """
        return ast.USub()

    @staticmethod
    def While(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt]=[], **keywordArguments: Unpack[ast_attributes]) -> ast.While:
        """
        While loop AST `object` for condition-based iteration.
        (AI generated docstring)

        The `ast.While` `object` represents `while` loops that repeatedly execute
        a block of statements as long as a test condition remains True. It supports
        optional else clauses that execute when the loop exits normally.

        Parameters:
            test: The boolean expression evaluated before each iteration to determine
                whether the loop should continue executing.
            body: Sequence of statements executed repeatedly while the test condition is True.
            orElse ([]): Optional statements executed when the loop exits normally
                without encountering a break statement. This corresponds to `ast.While.orelse`.

        Returns
        -------
        whileLoop: ast.While
            AST `object` representing a condition-based iteration statement.
        """
        return ast.While(test=test, body=list(body), orelse=list(orElse), **keywordArguments)

    @staticmethod
    def With(items: Sequence[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.With:
        """
        Context manager statement AST `object` for resource management and cleanup.
        (AI generated docstring)

        The `ast.With` `object` represents `with` statements that manage resources
        using context managers. These ensure proper setup and cleanup of resources
        like files, database connections, or locks.

        Parameters:
            items: Sequence of context manager items, each specifying a context manager
                expression and optional variable binding for the managed resource.
            body: Sequence of statements executed within the context manager scope.

        Returns:
            withStatement: ast.With
            AST `object` representing a context manager statement for resource management.
        """
        return ast.With(items=list(items), body=list(body), **keywordArguments)

    @staticmethod
    def withitem(context_expr: ast.expr, optional_vars: ast.expr | None=None) -> ast.withitem:
        """
        Context manager item AST object for individual items in `with` statements.
        (AI generated docstring)

        The `ast.withitem` object represents individual context manager specifications
        within `with` statements. Contains the context expression and optional variable
        binding for the context manager's return value.

        Parameters:
            context_expr: Expression providing the context manager object.
            optional_vars (None): Optional variable expression for `as` binding.

        Returns:
            contextItem: ast.withitem
            AST object representing a single context manager in with statements.
        """
        return ast.withitem(context_expr=context_expr, optional_vars=optional_vars)

    @staticmethod
    def Yield(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Yield:
        """
        Yield ***expr***ession `object` for generator function values.
        (AI generated docstring)

        The `ast.Yield` `object` represents yield expressions that produce values in
        generator functions. It suspends function execution and yields a value
        to the caller, allowing resumption from the same point.

        Parameters:
            value (None): Optional expression to yield; None yields None value.

        Returns:
            yieldExpression: ast.Yield
            AST `object` representing a yield expression for generator functions.
        """
        return ast.Yield(value=value, **keywordArguments)

    @staticmethod
    def YieldFrom(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.YieldFrom:
        """
        Yield from ***expr***ession `object` for delegating to sub-generators.
        (AI generated docstring)

        The `ast.YieldFrom` `object` represents `yield from` expressions that delegate
        generator execution to another iterable or generator. It provides efficient
        sub-generator delegation introduced in Python 3.3.

        Parameters:
            value: The iterable or generator expression to delegate to.

        Returns:
            yieldFromExpression: ast.YieldFrom
            AST `object` representing a yield from expression for generator delegation.
        """
        return ast.YieldFrom(value=value, **keywordArguments)