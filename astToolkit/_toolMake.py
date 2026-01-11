# ruff: noqa: A002
"""Automatically generated file, so changes may be overwritten."""
from astToolkit import (
	ast_attributes, ast_attributes_int, ast_attributes_type_comment, ConstantValueType, identifierDotAttribute)
from collections.abc import Iterable, Sequence
from typing import overload, Unpack
import ast
import sys

class Make:
    """Create a `class` `ast.AST` `object` or an `ast.AST` subclass `object`.

    I describe `keywordArguments` of `Make` methods here.

    Parameters
    ----------
    col_offset : int
        (***col***umn offset) Position information specifying the column where an AST object begins.
    end_col_offset : (int | None) | int
        (end ***col***umn offset) Position information specifying the column where an AST object ends.
    end_lineno : (int | None) | int
        (end line _**n**umer**o**_ (_Latin_ "number")) Position information specifying the line number where an AST
        object ends.
    level : int = 0
        (relative import level) An absolute import is 'level' 0. A relative import is `level` deep.
    lineno : int
        (line _**n**umer**o**_ (_Latin_ "number")) Position information manually specifying the line number where an AST
        object begins.
    type_comment : str
        (a `type` annotation in a comment) Optional string with the type annotation as a comment or `# noqa: `.

    Notes
    -----
    Every non-deprecated subclass of `ast.AST` (Abstract Syntax Tree), has a corresponding method in `Make`, and for each `class`, you can set the value of each
    attribute. But, what is an "attribute"? In the `ast` universe, one word may have many different meanings, and if you want to avoid confusion, you should pay
    close attention to capitalization, leading underscores, and context. In Python, an "attribute" is a property of an `object`. In `class` `Make`, when you
    create an `ast.AST` subclass `object`, you can set the value of any attribute of that `object`. The `ast` universe divides attributes into two categories,
    `_attributes` and `_fields` (or `_field*`).

    The attributes in category `_attributes` are `lineno` (line _**n**umer**o**_ (_Latin_ "number")),
    `col_offset` (***col***umn offset), `end_lineno` (end line _**n**umer**o**_ (_Latin_ "number")), and `end_col_offset` (end ***col***umn offset). These
    attributes of an `ast` `object` represent the physical location of the text when rendered as Python code. With abstract syntax trees, as opposed to concrete
    syntax trees for example, you rarely need to work directly with physical locations, therefore `_attributes` are almost always relegated to
    `**keywordArguments` in `Make` methods. For a counter example, see `Make.TypeIgnore` (this Type (`type`) error, Ignore it), for which `lineno` is a named
    parameter.

    In an attempt to distinguish the attributes of `ast.AST` subclasses that are not in the category `_attributes` from the four attributes in
    the category `_attributes`, all other attributes of `ast.AST` subclasses are in category `_fields` (or sometimes, category `_field*`, such as
    `_field_types`).

    You probably want to try to avoid confusing these concepts and categories with similarly named things, including `ast.Attribute`,
    `ast.Attribute.attr` (***attr***ibute), `getattr`, `setattr`, `ast.MatchClass.kwd_attrs` (***k***ey***w***or***d*** ***attr***ibute***s***), and
    `_Attributes` (no, really, it's a thing).
    """

    @staticmethod
    def _boolopJoinMethod(ast_operator: type[ast.boolop], expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr | ast.BoolOp:
        """'Join' expressions with a boolean operator.

        (AI generated docstring.)

        This private method provides the core logic for boolean operator joining used by `And.join()` and `Or.join()`
        methods. It handles edge cases like empty sequences and single expressions while creating properly nested
        `ast.BoolOp` structures for multiple expressions. If you are looking for public join functionality, use the
        specific boolean operator classes (`Make.And.join()`, `Make.Or.join()`) instead of this internal method.

        Parameters
        ----------
        ast_operator : type[ast.boolop]
            The boolean operator type (`ast.And` or `ast.Or`) to use for joining.
        expressions : Sequence[ast.expr]
            Sequence of expressions to join with the boolean operator.

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the joined boolean operation, or the original expression if only one
            provided.
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
        """'Join' expressions with a binary operator.

        (AI generated docstring.)

        This private method provides the core logic for binary operator joining used by operator classes like
        `Add.join()`, `BitOr.join()`, etc. It creates left-associative nested `ast.BinOp` structures by chaining
        expressions from left to right. If you are looking for public join functionality, use the specific operator
        classes (`Make.Add.join()`, `Make.BitOr.join()`, etc.) instead of this internal method.

        Parameters
        ----------
        ast_operator : type[ast.operator]
            The binary operator type (like `ast.Add`, `ast.BitOr`) to use for joining.
        expressions : Iterable[ast.expr]
            Collection of expressions to join with the binary operator.

        Returns
        -------
        joinedExpression : ast.expr
            Single expression representing the left-associative chained binary operations, or empty string constant if
            no expressions provided.
        """
        listExpressions: list[ast.expr] = list(expressions)
        if not listExpressions:
            listExpressions.append(Make.Constant('', **keywordArguments))
        expressionsJoined: ast.expr = listExpressions[0]
        for expression in listExpressions[1:]:
            expressionsJoined = ast.BinOp(left=expressionsJoined, op=ast_operator(), right=expression, **keywordArguments)
        return expressionsJoined

    class Add(ast.Add):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def alias(dotModule: str, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.alias:
        """Import alias AST `object` representing name mapping in import statements.

        (AI generated docstring.)

        The `ast.alias` `object` represents name mappings used in `import` and `from ... import` statements. It handles
        both direct imports (`import math`) and aliased imports (`import re as regex`).

        Parameters
        ----------
        name :
            The actual module, class, or function name being imported.
        asName :
            Optional as Name to use instead of the original name. This corresponds to `ast.alias.asname`.

        Returns
        -------
        importAlias : ast.alias
            AST `object` representing an import name mapping with optional aliasing.
        """
        return ast.alias(name=dotModule, asname=asName, **keywordArguments)

    class And(ast.And):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BoolOp` (***Bool***ean ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating an `ast.BoolOp` (***Bool***ean ***Op***eration) `object` that logically 'joins' the `Sequence`.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Sequence[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing ast.BoolOp structures:
            ast.BoolOp(
                op=ast.And(),
            values=[ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')]
            )

            # Simply use:
            astToolkit.And.join([ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')])

            # Both produce the same AST structure but the join()
            method eliminates the manual construction.
            ```
            """
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def AnnAssign(target: ast.Name | ast.Attribute | ast.Subscript, annotation: ast.expr, value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.AnnAssign:
        """Annotated assignment AST `object` for type-annotated variable assignments.

        (AI generated docstring.)

        The `ast.AnnAssign` (***Ann***otated ***Assign***ment) `object` represents variable assignments with type
        annotations, such as `name: int = 42` or `config: dict[str, Any]`. This is the preferred form for annotated
        assignments in modern Python code.

        Parameters
        ----------
        target :
            The assignment target, which must be a simple name, attribute access, or subscript operation that can
            receive the annotated assignment.
        annotation :
            The type annotation expression specifying the variable's expected type.
        value :
            Optional initial value expression for the annotated variable.

        Returns
        -------
        annotatedAssignment : ast.AnnAssign
            AST `object` representing a type-annotated variable assignment.
        """
        return ast.AnnAssign(target=target, annotation=annotation, value=value, simple=int(isinstance(target, ast.Name)), **keywordArguments)

    @staticmethod
    def arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str, annotation: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.arg:
        """Make an `ast.arg` object representing individual arguments in function signatures.

        (AI generated docstring.)

        The `ast.arg` (abstract syntax tree) object represents a single parameter in function definitions, including
        positional, keyword-only, and special parameters like `*arguments` and `**keywordArguments`. Contains the
        parameter name and optional type annotation.

        Parameters
        ----------
        Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo :
            Parameter name as string. This corresponds to `ast.arg.arg`; and in an `ast.FunctionDef`
            ({diminutive2etymology['FunctionDef']}) `object`, it corresponds to `ast.FunctionDef.args.args[n].arg.arg`,
            which has the same semantic value as `Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo`.
        annotation :
            Optional type annotation expression for the parameter.

        Returns
        -------
        argumentDefinition : ast.arg
            AST object representing a single function parameter with optional typing.
        """
        return ast.arg(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, annotation=annotation, **keywordArguments)

    @staticmethod
    def arguments(posonlyargs: list[ast.arg] | None=None, list_arg: list[ast.arg] | None=None, vararg: ast.arg | None=None, kwonlyargs: list[ast.arg] | None=None, kw_defaults: Sequence[ast.expr | None] | None=None, kwarg: ast.arg | None=None, defaults: Sequence[ast.expr] | None=None) -> ast.arguments:
        """Make a function signature AST object containing all parameter specifications.

        (AI generated docstring.)

        The `ast.arguments` object represents the complete parameter specification for function definitions, organizing
        different parameter types including positional-only, regular, keyword-only, variadic, and default values.

        Parameters
        ----------
        posonlyargs :
            (***pos***itional-only ***arg***ument***s***) List of positional-only parameters (before /).
        list_arg :
            (list of ast.***arg***ument) List of positional parameters. This corresponds to `ast.arguments.args`.
        vararg :
            (***var***iadic ***arg***ument) Single parameter for *arguments variadic arguments.
        kwonlyargs :
            (***k***ey***w***ord-only ***arg***ument***s***) List of keyword-only parameters (after * or *arguments).
        kw_defaults :
            (***k***ey***w***ord defaults) Default values for keyword-only parameters; None indicates required.
        kwarg :
            (***k***ey***w***ord ***arg***ument) Single parameter for '**keywordArguments' keyword arguments.
        defaults :
            Default values for regular positional parameters.

        Returns
        -------
        functionSignature : ast.arguments
            AST object representing complete function parameter specification.
        """
        return ast.arguments(posonlyargs=posonlyargs or [], args=list_arg or [], vararg=vararg, kwonlyargs=kwonlyargs or [], kw_defaults=list(kw_defaults) if kw_defaults else [], kwarg=kwarg, defaults=list(defaults) if defaults else [])

    @staticmethod
    def Assert(test: ast.expr, msg: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Assert:
        """Create an `ast.Assert` node for assertion statements.

        (AI generated docstring.)

        The `Assert` node represents an `assert` statement that evaluates a test expression and optionally raises
        `AssertionError` with a message if the test fails. This is primarily used for debugging and testing purposes.

        Parameters
        ----------
        test :
            Expression to evaluate for truthiness.
        msg :
            (***m***e***s***sa***g***e) Optional expression for the assertion error message.

        Returns
        -------
        nodeAssert : ast.Assert
            The constructed assertion node.
        """
        return ast.Assert(test=test, msg=msg, **keywordArguments)

    @staticmethod
    def Assign(targets: Sequence[ast.expr], value: ast.expr, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.Assign:
        """Make an assignment AST `object` for variable assignments without type annotations.

        (AI generated docstring.)

        The `ast.Assign` `object` represents traditional variable assignments like `x = 5`, `a = b = c`, or `items[0] =
        newValue`. It supports multiple assignment targets and complex assignment patterns.

        Parameters
        ----------
        targets :
            Sequence of assignment targets that will receive the value. Multiple targets enable chained assignments like
            `a = b = value`.
        value :
            The expression whose result will be assigned to all targets.

        Returns
        -------
        assignment : ast.Assign
            AST `object` representing a variable assignment operation.
        """
        return ast.Assign(targets=list(targets), value=value, **keywordArguments)

    @staticmethod
    def AST() -> ast.AST:
        """Make a base AST node object representing the abstract syntax tree foundation.

        (AI generated docstring.)

        The `ast.AST` object serves as the base class for all AST node types in Python's abstract syntax tree. This
        method creates a minimal AST instance, though in practice you will typically use specific node type factories
        like `Make.Name()`, `Make.Call()`, etc. Most users seeking AST node creation should use the specific factory
        methods for concrete node types rather than this base AST constructor.

        Returns
        -------
        baseNode : ast.AST
            The fundamental AST object from which all other nodes inherit.
        """
        return ast.AST()

    @staticmethod
    def AsyncFor(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFor:
        """Asynchronous for loop AST `object` for iterating over async iterables.

        (AI generated docstring.)

        The `ast.AsyncFor` (***Async***hronous For loop) `object` represents `async for` loops that iterate over
        asynchronous iterators and async generators. These loops can only exist within async functions and automatically
        handle await operations.

        Parameters
        ----------
        target :
            The loop variable that receives each item from the async iterable.
        iter :
            (***iter***able) The asynchronous iterable expression being iterated over.
        body :
            Sequence of statements executed for each iteration of the async loop.
        orelse :
            (or Else execute this) Optional statements executed when the loop completes normally without encountering a
            break statement.

        Returns
        -------
        asyncForLoop : ast.AsyncFor
            AST `object` representing an asynchronous for loop construct.
        """
        return ast.AsyncFor(target=target, iter=iter, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def AsyncFunctionDef(name: str, argumentSpecification: ast.arguments | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, returns: ast.expr | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFunctionDef:
        """Asynchronous function definition AST object for `async def` declarations.

        (AI generated docstring.)

        The `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition) object represents asynchronous
        function definitions using the `async def` syntax. Supports coroutines, async generators, and other asynchronous
        operations with await expressions.

        Parameters
        ----------
        name :
            Function name as string identifier.
        args :
            Function parameter specification.
        body :
            List of statements forming the function body.
        decorator_list :
            List of decorator expressions applied to function.
        returns :
            (this returns) Optional return type annotation expression.
        type_params :
            (type ***param***eter***s***) List of type parameters for generic functions (Python 3.12+).

        Returns
        -------
        asyncFunction : ast.AsyncFunctionDef
            AST object representing an asynchronous function definition.
        """
        return ast.AsyncFunctionDef(name=name, args=argumentSpecification or ast.arguments(), body=list(body) if body else [], decorator_list=list(decorator_list) if decorator_list else [], returns=returns, type_params=list(type_params) if type_params else [], **keywordArguments)

    @staticmethod
    def AsyncWith(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncWith:
        """Asynchronous context manager AST `object` for async resource management.

        (AI generated docstring.)

        The `ast.AsyncWith` (***Async***hronous With statement) `object` represents `async with` statements that manage
        asynchronous context managers. These ensure proper setup and cleanup of async resources like database
        connections or file handles.

        Parameters
        ----------
        items :
            Sequence of context manager items, each specifying an async context manager and optional variable binding
            for the managed resource.
        body :
            Sequence of statements executed within the async context manager scope.

        Returns
        -------
        asyncWithStatement : ast.AsyncWith
            AST `object` representing an asynchronous context manager statement.
        """
        return ast.AsyncWith(items=items, body=list(body), **keywordArguments)

    @staticmethod
    def Attribute(value: ast.expr, *attribute: str, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
        """Attribute access AST `object` representing dot notation in Python code.

        (AI generated docstring.)

        The `ast.Attribute` `object` represents attribute access using dot notation, such as `object.attribute` or
        chained access like `module.class.method`. This method supports chaining multiple attributes by passing
        additional attribute names.

        Parameters
        ----------
        value :
            The base expression before the first dot.
        attribute :
            One or more attribute names to chain together with dot notation.
        context :
            Are you loading from, storing to, or deleting the `ast.Attribute`? Values may be `ast.Load()`,
            `ast.Store()`, or `ast.Del()`, meaning 'Delete' the `ast.Attribute`. `context` corresponds to
            `ast.Attribute.ctx`.

        Returns
        -------
        attributeAccess : ast.Attribute
            AST `object` representing attribute access with potential chaining.
        """
        ctx = context or ast.Load()

        def addDOTattribute(chain: ast.expr, identifier: str, ctx: ast.expr_context, **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
            return ast.Attribute(value=chain, attr=identifier, ctx=ctx, **keywordArguments)
        buffaloBuffalo = addDOTattribute(value, attribute[0], ctx, **keywordArguments)
        for identifier in attribute[1:None]:
            buffaloBuffalo = addDOTattribute(buffaloBuffalo, identifier, ctx, **keywordArguments)
        return buffaloBuffalo

    @staticmethod
    def AugAssign(target: ast.Name | ast.Attribute | ast.Subscript, op: ast.operator, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.AugAssign:
        """Augmented assignment AST `object` for compound assignment operations.

        (AI generated docstring.)

        The `ast.AugAssign` (***Aug***mented ***Assign***ment) `object` represents augmented assignment operators like
        `+=`, `-=`, `*=`, `/=`, and others that combine an operation with assignment. These provide concise syntax for
        modifying variables in-place.

        Parameters
        ----------
        target :
            The assignment target being modified, which must be a name, attribute access, or subscript that supports in-
            place modification.
        op :
            (***op***erator) The binary operator defining the augmentation operation, such as `ast.Add()` for `+=` or
            `ast.Mult()` (***Mult***iplication) for `*=`.
        value :
            The expression whose result will be combined with the target using the specified operator.

        Returns
        -------
        augmentedAssignment : ast.AugAssign
            AST `object` representing a compound assignment operation.
        """
        return ast.AugAssign(target=target, op=op, value=value, **keywordArguments)

    @staticmethod
    def Await(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Await:
        """Await expression AST `object` for asynchronous operations.

        (AI generated docstring.)

        The `ast.Await` (***Await*** the asynchronous operation) `object` represents the keyword `await` used with
        asynchronous expressions in Python. It can only be used within async functions and suspends execution until the
        awaited coroutine completes.

        Parameters
        ----------
        value :
            The expression to await, typically a coroutine or awaitable `object`.

        Returns
        -------
        awaitExpression : ast.Await
            AST `object` representing an await expression for asynchronous code.
        """
        return ast.Await(value=value, **keywordArguments)

    @staticmethod
    def BinOp(left: ast.expr, op: ast.operator, right: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.BinOp:
        """Make a binary operation AST `object` representing operators between two expressions.

        (AI generated docstring.)

        The `ast.BinOp` (***Bin***ary ***Op***eration) `object` represents binary operations like addition, subtraction,
        multiplication, and other two-operand operations. The operation type is determined by the `op` parameter using
        specific operator classes.

        Parameters
        ----------
        left :
            The left-hand operand expression.
        op :
            The binary operator, such as `ast.Add()`, `ast.Sub()`, `ast.Mult()`, etc.
        right :
            The right-hand operand expression.

        Returns
        -------
        binaryOperation : ast.BinOp
            AST `object` representing a binary operation between two expressions.
        """
        return ast.BinOp(left=left, op=op, right=right, **keywordArguments)

    class BitAnd(ast.BitAnd):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitOr(ast.BitOr):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitXor(ast.BitXor):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def BoolOp(op: ast.boolop, values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.BoolOp:
        """Make a boolean operation AST `object` for logical operations with multiple operands.

        (AI generated docstring.)

        The `ast.BoolOp` (***Bool***ean ***Op***eration) `object` represents boolean operations like keywords `and` and
        `or` that can operate on multiple expressions. Unlike binary operators, boolean operations can chain multiple
        values together efficiently.

        Parameters
        ----------
        op :
            (***bool***ean ***op***erator) The boolean operator, either `ast.And()` or `ast.Or()`.
        values :
            Sequence of expressions to combine with the boolean operator.

        Returns
        -------
        booleanOperation : ast.BoolOp
            (***Bool***ean ***Op***eration) AST `object` representing a boolean operation with multiple operands.
        """
        return ast.BoolOp(op=op, values=list(values), **keywordArguments)

    @staticmethod
    def boolop() -> ast.boolop:
        """Make a base boolean operator abstract class for logical operations.

        (AI generated docstring.)

        The `ast.boolop` (***bool***ean ***op***erator) class serves as the abstract base for boolean operators like
        `ast.And` and `ast.Or`. This method creates a minimal boolop instance, though in practice you will typically use
        specific boolean operator factories like `Make.And()`, `Make.Or()`, or their join methods.          Most users
        seeking boolean operation creation should use the specific operator classes or `Make.BoolOp()` rather than this
        abstract base constructor.

        Returns
        -------
        baseBooleanOperator :
            (***bool***ean ***op***erator) AST `object` representing a base boolean operator.
        """
        return ast.boolop()

    @staticmethod
    def Break(**keywordArguments: Unpack[ast_attributes]) -> ast.Break:
        """Create an `ast.Break` node for break statements.

        (AI generated docstring.)

        The `Break` node represents a `break` statement that terminates the nearest enclosing loop. Can only be used
        within loop constructs.

        Returns
        -------
        nodeBreak : ast.Break
            The constructed break statement node.
        """
        return ast.Break(**keywordArguments)

    @staticmethod
    def Call(callee: ast.expr, listParameters: Sequence[ast.expr] | None=None, list_keyword: list[ast.keyword] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Call:
        """Make a function call AST `object` representing function invocation with arguments.

        (AI generated docstring.)

        The `ast.Call` `object` represents function calls, method calls, and constructor invocations. It supports both
        positional and keyword arguments and handles various calling conventions including unpacking operators.

        Parameters
        ----------
        callee :
            The callable expression, typically a function name or method access.
        listParameters :
            Sequence of positional argument expressions.
        list_keyword :
            Sequence of keyword arguments as `ast.keyword`.

        Returns
        -------
        functionCall : ast.Call
            AST `object` representing a function call with specified arguments.
        """
        return ast.Call(func=callee, args=list(listParameters) if listParameters else [], keywords=list_keyword or [], **keywordArguments)

    @staticmethod
    def ClassDef(name: str, bases: Sequence[ast.expr] | None=None, list_keyword: list[ast.keyword] | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.ClassDef:
        """Make a class definition AST object for `class` declarations with inheritance and metadata.

        (AI generated docstring.)

        The `ast.ClassDef` object represents class definitions including base classes, metaclass specifications,
        decorators, and the class body. Supports both traditional and modern Python class features.

        Parameters
        ----------
        name :
            Class name as string identifier.
        bases :
            List of base class expressions for inheritance.
        keywords :
            (list of ast.***keyword***) including metaclass specifications.
        body :
            List of statements forming the class body.
        decorator_list :
            List of decorator expressions applied to class.
        type_params :
            (type ***param***eter***s***) List of type parameters for generic classes (Python 3.12+).

        Returns
        -------
        classDefinition :
            AST object representing a complete class definition with metadata.

        Examples
        --------
        ```
        # Creates AST equivalent to: class Vehicle: pass
        simpleClass = Make.ClassDef('Vehicle', body=[Make.Pass()])

        # Creates AST
        equivalent to: class Bicycle(Vehicle, metaclass=ABCMeta): pass
        inheritedClass = Make.ClassDef(
            'Bicycle',
        bases=[Make.Name('Vehicle')],
            keywords=[Make.keyword('metaclass', Make.Name('ABCMeta'))],
            body=[Make.Pass()]
        )
        ```
        """
        return ast.ClassDef(name=name, bases=list(bases) if bases else [], keywords=list_keyword or [], body=list(body) if body else [], decorator_list=list(decorator_list) if decorator_list else [], type_params=list(type_params) if type_params else [], **keywordArguments)

    @staticmethod
    def cmpop() -> ast.cmpop:
        """`class` `ast.cmpop`, ***c***o***mp***arison ***op***erator, is the parent (or 'base') class of all comparison operator classes used in `ast.Compare`.

        (AI generated docstring.)

        It is the abstract parent for: `ast.Eq`, `ast.NotEq`, `ast.Lt`, `ast.LtE`, `ast.Gt`, `ast.GtE`, `ast.Is`,
        `ast.IsNot`, `ast.In`, `ast.NotIn`. This factory method makes a generic comparison operator `object` that can be
        used in the antecedent-action pattern with visitor classes.

        Returns
        -------
        comparisonOperator : ast.cmpop
            Abstract comparison operator `object` that serves as the base `class` for all Python comparison operators in
            AST structures.
        """
        return ast.cmpop()

    @staticmethod
    def Compare(left: ast.expr, ops: Sequence[ast.cmpop], comparators: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Compare:
        """Make a comparison AST `object` for chained comparison operations.

        (AI generated docstring.)

        The `ast.Compare` `object` represents comparison operations including equality, inequality, and ordering
        comparisons. It supports chained comparisons like `a < b <= c` through sequences of operators and comparators.
        All comparison operators: `ast.Eq` (is ***Eq***ual to), `ast.NotEq` (is Not ***Eq***ual to), `ast.Lt` (is Less
        than), `ast.LtE` (is Less than or Equal to), `ast.Gt` (is Greater than), `ast.GtE` (is Greater than or Equal
        to), `ast.Is`, `ast.IsNot`, `ast.In`, `ast.NotIn` (is Not ***In***cluded in or does Not have membership In).

        Parameters
        ----------
        left :
            (left-hand-side operand) The leftmost expression in the comparison chain.
        ops :
            (***op***erator***s***) Sequence of comparison operators from the complete list above.
        comparators :
            Sequence of expressions to compare against, one for each operator.

        Returns
        -------
        comparison :
            AST `object` representing a comparison operation with potential chaining.

        Examples
        --------
        ```python
        # Creates AST equivalent to: `temperature == 72`
        temperatureCheck = Make.Compare(
            left=Make.Name('temperature'),
        ops=[Make.Eq()],
            comparators=[Make.Constant(72)]
        )

        # Creates AST equivalent to: `0 <= inventory < 100`
        inventoryRange = Make.Compare(
            left=Make.Constant(0),
            ops=[Make.LtE(), Make.Lt()],
        comparators=[Make.Name('inventory'), Make.Constant(100)]
        )
        ```
        """
        return ast.Compare(left=left, ops=list(ops), comparators=list(comparators), **keywordArguments)

    @staticmethod
    def comprehension(target: ast.expr, iter: ast.expr, ifs: Sequence[ast.expr], is_async: int=0) -> ast.comprehension:
        """Make a comprehension clause AST object for `for` clauses in list/set/dict comprehensions.

        (AI generated docstring.)

        The `ast.comprehension` object represents individual `for` clauses within comprehension expressions. Contains
        the iteration target, source, conditional filters, and async specification for generator expressions.

        Parameters
        ----------
        target :
            Variable expression receiving each iteration value.
        iter :
            (***iter***able) Iterable expression being traversed.
        ifs :
            (if clauses) List of conditional expressions filtering iteration results.
        is_async :
            (is ***async***hronous) Integer flag (0 or 1) indicating async comprehension.

        Returns
        -------
        comprehensionClause : ast.comprehension
            AST object representing a single for clause in comprehensions.
        """
        return ast.comprehension(target=target, iter=iter, ifs=list(ifs), is_async=is_async)

    @staticmethod
    def Constant(value: ConstantValueType, kind: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Constant:
        """Make a constant value AST `object` for literal values in Python code.

        (AI generated docstring.)

        The `ast.Constant` `object` represents literal constant values like numbers, strings, booleans, and None. It
        replaces the deprecated specific literal and provides a unified representation for all constant values.

        Parameters
        ----------
        value :
            The constant value.
        kind :
            Optional string hint for specialized constant handling.

        Returns
        -------
        constantValue : ast.Constant
            AST `object` representing a literal constant value.
        """
        return ast.Constant(value=value, kind=kind, **keywordArguments)

    @staticmethod
    def Continue(**keywordArguments: Unpack[ast_attributes]) -> ast.Continue:
        """Create an `ast.Continue` node for continue statements.

        (AI generated docstring.)

        The `Continue` node represents a `continue` statement that skips the remainder of the current iteration and
        continues with the next iteration of the nearest enclosing loop.

        Returns
        -------
        nodeContinue : ast.Continue
            The constructed continue statement node.
        """
        return ast.Continue(**keywordArguments)

    @staticmethod
    def Del() -> ast.Del:
        """Make a delete context for removing expressions from memory.

        (AI generated docstring.)

        The `ast.Del` (***Del***ete) context indicates expressions are deletion targets in `del` statements. Note that
        `ast.Del` is the expression context, not the `del` keyword itself - `ast.Delete` represents the `del` statement.

        Returns
        -------
        deleteContext :
            AST context object indicating deletion operations on expressions.

        Examples
        --------
        Creates AST equivalent to deletion: del bicycle.wheel
        ```python
        wheelDeletion = Make.Attribute(Make.Name('bicycle'), 'wheel',
        Make.Del())
        ```
        """
        return ast.Del()

    @staticmethod
    def Delete(targets: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Delete:
        """Create an `ast.Delete` node for deletion statements.

        (AI generated docstring.)

        The `Delete` node represents a `del` statement that removes references to objects. Can delete variables,
        attributes, subscripts, or slices.

        Parameters
        ----------
        targets :
            List of expressions identifying what to delete.

        Returns
        -------
        nodeDelete : ast.Delete
            The constructed deletion statement node.
        """
        return ast.Delete(targets=list(targets), **keywordArguments)

    @staticmethod
    def Dict(keys: Sequence[ast.expr | None] | None=None, values: Sequence[ast.expr] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Dict:
        """Combine `keys` and `values` into an AST (Abstract Syntax Tree) representation of the Python built-in `class` `dict` (***dict***ionary).

        (AI generated docstring.)

        The `ast.Dict` (***Dict***ionary) `object` represents dictionary literals using curly brace notation. It
        supports both regular key-value pairs and dictionary unpacking operations where keys can be None to indicate
        unpacking expressions.

        Parameters
        ----------
        keys :
            Sequence of key expressions or None for unpacking operations.
        values :
            Sequence of value expressions corresponding to the keys.

        Returns
        -------
        dictionaryLiteral : ast.Dict
            (***Dict***ionary) AST `object` representing a dictionary literal with specified key-value pairs.
        """
        return ast.Dict(keys=list(keys) if keys else [], values=list(values) if values else [], **keywordArguments)

    @staticmethod
    def DictComp(key: ast.expr, value: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.DictComp:
        """Make a dictionary comprehension AST `object` for dynamic dictionary construction.

        (AI generated docstring.)

        The `ast.DictComp` (***Dict***ionary ***c***o***mp***rehension) `object` represents dictionary comprehensions
        that make dictionaries using iterator expressions. It combines key-value generation with filtering and nested
        iteration capabilities.

        Parameters
        ----------
        key :
            Expression that generates dictionary keys.
        value :
            Expression that generates dictionary values.
        generators :
            Sequence of `ast.comprehension` defining iteration and filtering.

        Returns
        -------
        dictionaryComprehension :
            (***Dict***ionary ***c***o***mp***rehension) AST `object` representing a dictionary comprehension
            expression.

        Examples
        --------
        ```
        # Creates AST equivalent to: `{{recipe: difficulty for recipe in cookbook}}`
        recipeDifficulty = Make.DictComp(
        key=Make.Name('recipe'),
            value=Make.Name('difficulty'),
            generators=[Make.comprehension(
        target=Make.Name('recipe'),
                iter=Make.Name('cookbook'),
                ifs=[]
            )]
        )
        ```
        """
        return ast.DictComp(key=key, value=value, generators=generators, **keywordArguments)

    class Div(ast.Div):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Eq() -> ast.Eq:
        """'Eq', meaning 'is ***Eq***ual to', is the `object` representation of Python comparison operator '`==`'.

        (AI generated docstring.)

        `class` `ast.Eq` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in `class`
        `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        equalityOperator : ast.Eq
            AST `object` representing the '`==`' equality comparison operator for use in `ast.Compare`.
        """
        return ast.Eq()

    @staticmethod
    def ExceptHandler(type: ast.expr | None=None, name: str | None=None, body: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.ExceptHandler:
        """Exception handler clause for try-except statements.

        (AI generated docstring.)

        The `ast.ExceptHandler` (***Except***ion ***Handler***) object represents individual `except` clauses that catch
        and handle specific exceptions. It defines the exception type to catch, optional variable binding, and
        statements to execute when matched.

        Parameters
        ----------
        type :
            Exception type expression to catch; None catches all exceptions.
        name :
            Variable name string to bind caught exception; None for no binding.
        body :
            List of statements to execute when exception is caught.

        Returns
        -------
        exceptionHandler : ast.ExceptHandler
            AST object representing an except clause in try-except statements.
        """
        return ast.ExceptHandler(type=type, name=name, body=list(body) if body else [], **keywordArguments)

    @staticmethod
    def excepthandler(**keywordArguments: Unpack[ast_attributes]) -> ast.excepthandler:
        """Exception handler abstract base class for try-except constructs.

        (AI generated docstring.)

        The `ast.excepthandler` (***except***ion ***handler***) abstract base class represents exception handling
        clauses in try-except statements. This is the foundation for `ast.ExceptHandler` which implements the actual
        exception catching logic.

        Returns
        -------
        exceptionHandler : ast.excepthandler
            Abstract AST object for exception handling clause classification.
        """
        return ast.excepthandler(**keywordArguments)

    @staticmethod
    def expr(**keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """Abstract ***expr***ession `object` for base expression operations.

        (AI generated docstring.)

        The `ast.expr` class serves as the abstract base class for all expression objects in Python's AST. Unlike
        `ast.stmt` which represents statements that perform actions, `ast.expr` represents expressions that evaluate to
        values and can be used within larger expressions or as parts of statements.          Expressions vs Statements:
        - **expr**: Evaluates to a value and can be composed into larger expressions. Examples include literals (`42`,
        `"hello"`), operations (`x + y`), function calls (`len(data)`), and attribute access (`obj.method`).         -
        **stmt**: Performs an action and does not evaluate to a usable value. Examples include assignments (`x = 5`),
        control flow (`if`, `for`, `while`), function definitions (`def`), and imports (`import`).

        Returns
        -------
        expression :
            Abstract expression `object` that serves as the base class for all Python expressions in AST structures.
        """
        return ast.expr(**keywordArguments)

    @staticmethod
    def Expr(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Expr:
        """Create an `ast.Expr` node for expression statements.

        (AI generated docstring.)

        The `Expr` node represents a statement that consists of a single expression whose value is discarded. This is
        used for expressions evaluated for their side effects rather than their return value.

        Parameters
        ----------
        value :
            Expression to evaluate as a statement.

        Returns
        -------
        nodeExpr : ast.Expr
            The constructed expression statement node.
        """
        return ast.Expr(value=value, **keywordArguments)

    @staticmethod
    def expr_context() -> ast.expr_context:
        """Expression context abstract base class for expression usage patterns.

        (AI generated docstring.)

        The `ast.expr_context` (***expr***ession ***context***) abstract base class represents how expressions are used
        in code: whether they load values, store values, or delete them. This is the foundation for `ast.Load`,
        `ast.Store`, and `ast.Del` contexts.

        Returns
        -------
        expressionContext : ast.expr_context
            Abstract AST context object for expression usage classification.
        """
        return ast.expr_context()

    @staticmethod
    def Expression(body: ast.expr) -> ast.Expression:
        """Create an `ast.Expression` node for expression-only modules.

        (AI generated docstring.)

        The `Expression` node represents a module that contains only a single expression. This is used in contexts where
        only an expression is expected, such as with `eval()` or interactive mode single expressions.

        Parameters
        ----------
        body :
            The single expression that forms the module body

        Returns
        -------
        nodeExpression : ast.Expression
            The constructed expression module node
        """
        return ast.Expression(body=body)

    class FloorDiv(ast.FloorDiv):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def For(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.For:
        """Make a for loop AST `object` for iterating over iterable expressions.

        (AI generated docstring.)

        The `ast.For` `object` represents traditional `for` loops that iterate over sequences, generators, or any
        iterable object. It supports optional else clauses that execute when the loop completes normally.

        Parameters
        ----------
        target :
            The loop variable that receives each item from the iterable expression.
        iter :
            (***iter***able) The iterable expression being iterated over, such as a list, range, or generator.
        body :
            Sequence of statements executed for each iteration of the loop.
        orelse :
            (or Else execute this) Optional statements executed when the loop completes normally without encountering a
            break statement.

        Returns
        -------
        forLoop : ast.For
            AST `object` representing a for loop iteration construct.
        """
        return ast.For(target=target, iter=iter, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def FormattedValue(value: ast.expr, conversion: int, format_spec: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.FormattedValue:
        """Make a formatted value AST `object` for f-string interpolation components.

        (AI generated docstring.)

        The `ast.FormattedValue` `object` represents individual expressions within f-string literals, including format
        specifications and conversion options. It handles the interpolation mechanics of formatted string literals.

        Parameters
        ----------
        value :
            The expression to be formatted and interpolated.
        conversion :
            Conversion flag (0=no conversion, 115='s', 114='r', 97='a').
        format_spec :
            (format ***spec***ification) Optional format specification expression.

        Returns
        -------
        formattedValue : ast.FormattedValue
            AST `object` representing a formatted value within an f-string expression.
        """
        return ast.FormattedValue(value=value, conversion=conversion, format_spec=format_spec, **keywordArguments)

    @staticmethod
    def FunctionDef(name: str, argumentSpecification: ast.arguments | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, returns: ast.expr | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.FunctionDef:
        """Make a function definition AST object for standard `def` declarations with typing support.

        (AI generated docstring.)

        The `ast.FunctionDef` object represents standard function definitions including parameters, return annotations,
        decorators, and function body. Supports modern Python typing features and generic type parameters.

        Parameters
        ----------
        name :
            Function name as string identifier.
        args :
            Function parameter specification.
        body :
            List of statements forming the function body.
        decorator_list :
            List of decorator expressions applied to function.
        returns :
            (this returns) Optional return type annotation expression.
        type_params :
            (type ***param***eter***s***) List of type parameters for generic functions (Python 3.12+).

        Returns
        -------
        functionDefinition :
            AST object representing a complete function definition with metadata.

        Examples
        --------
        ```
        # Creates AST equivalent to: def cook(): pass
        simpleFunction = Make.FunctionDef('cook', body=[Make.Pass()])

        # Creates AST
        equivalent to: def bake(recipe: str, temperature: int = 350) -> bool: return True
        typedFunction = Make.FunctionDef(
            'bake',
        Make.arguments(
                args=[Make.arg('recipe', Make.Name('str')), Make.arg('temperature', Make.Name('int'))],
        defaults=[Make.Constant(350)]
            ),
            [Make.Return(Make.Constant(True))],
            returns=Make.Name('bool')
        )
        ```
        """
        return ast.FunctionDef(name=name, args=argumentSpecification or ast.arguments(), body=list(body) if body else [], decorator_list=list(decorator_list) if decorator_list else [], returns=returns, type_params=list(type_params) if type_params else [], **keywordArguments)

    @staticmethod
    def FunctionType(argtypes: Sequence[ast.expr], returns: ast.expr) -> ast.FunctionType:
        """Create an `ast.FunctionType` node for function type annotations.

        (AI generated docstring.)

        The `FunctionType` node represents function type annotations of the form `(arg_types) -> return_type`. This is
        used in type annotations and variable annotations for callable types.

        Parameters
        ----------
        argtypes :
            (***arg***ument types) List of expressions representing argument types
        returns :
            (this returns) Expression representing the return type

        Returns
        -------
        nodeFunctionType : ast.FunctionType
            The constructed function type annotation node
        """
        return ast.FunctionType(argtypes=list(argtypes), returns=returns)

    @staticmethod
    def GeneratorExp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.GeneratorExp:
        """Make a generator expression object for memory-efficient iteration.

        (AI generated docstring.)

        The `ast.GeneratorExp` (Generator ***Exp***ression) object represents generator expressions that create iterator
        objects without constructing intermediate collections. It provides lazy evaluation and memory efficiency for
        large datasets.

        Parameters
        ----------
        element :
            Expression that generates each element of the generator.
        generators :
            Sequence of `ast.comprehension` objects defining iteration and filtering.

        Returns
        -------
        generatorExpression : ast.GeneratorExp
            AST object representing a generator expression for lazy evaluation.
        """
        return ast.GeneratorExp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Global(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Global:
        """Create an `ast.Global` node for global declarations.

        (AI generated docstring.)

        The `Global` node represents a `global` statement that declares variables as referring to global scope rather
        than local scope. This affects variable lookup and assignment within the current function.

        Parameters
        ----------
        names :
            List of variable names to declare as global.

        Returns
        -------
        nodeGlobal : ast.Global
            The constructed global declaration node.
        """
        return ast.Global(names=names, **keywordArguments)

    @staticmethod
    def Gt() -> ast.Gt:
        """'Gt', meaning 'Greater than', is the `object` representation of Python operator '`>`'.

        (AI generated docstring.)

        `class` `ast.Gt` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in `class`
        `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        greaterThanOperator : ast.Gt
            AST `object` representing the '`>`' greater-than comparison operator for use in `ast.Compare`.
        """
        return ast.Gt()

    @staticmethod
    def GtE() -> ast.GtE:
        """'GtE', meaning 'is Greater than or Equal to', is the `object` representation of Python comparison operator '`>=`'.

        (AI generated docstring.)

        `class` `ast.GtE` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in
        `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        greaterThanOrEqualOperator : ast.GtE
            AST `object` representing the '`>=`' greater-than-or-equal comparison operator for use in `ast.Compare`.
        """
        return ast.GtE()

    @staticmethod
    def If(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.If:
        """Make a conditional statement AST `object` for branching execution paths.

        (AI generated docstring.)

        The `ast.If` `object` represents `if` statements that conditionally execute code blocks based on boolean test
        expressions. It supports optional else clauses for alternative execution paths.

        Parameters
        ----------
        test :
            The boolean expression that determines which branch to execute.
        body :
            Sequence of statements executed when the test expression evaluates to True.
        orElse :
            (or Else execute this) Optional statements executed when the test expression evaluates to False. This
            parameter corresponds with `ast.If.orelse` (or else execute this).

        Returns
        -------
        conditionalStatement :
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
                [Make.Assign([Make.Name('grade')],
        Make.Constant('B'))],
                [Make.Assign([Make.Name('grade')], Make.Constant('C'))]
            )]
        )
        ```
        """
        return ast.If(test=test, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def IfExp(test: ast.expr, body: ast.expr, orElse: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.IfExp:
        """Make a 'ChooseThis `if` ConditionIsTrue `else` ChooseThat' conditional expression.

        (AI generated docstring.)

        The `ast.IfExp` (If ***Exp***ression) `object` represents inline conditional expressions using the ternary
        operator syntax `execute_if_true if condition else execute_if_false`.

        Parameters
        ----------
        test :
            The `True`/`False` condition expression.
        body :
            If `test` is `True`, the interpreter executes this singular expression.
        orElse :
            (or Else execute this) If `test` is `False`, the interpreter executes this singular expression. This
            parameter corresponds with `ast.IfExp.orelse` (or else execute this).

        Returns
        -------
        conditionalExpression :
            `ast.AST` ({diminutive2etymology['AST']}) `object` representing an inline conditional expression.

        Examples
        --------
        ```python
        # To create the `ast.AST` representation of `maxVolume if amplified else defaultVolume`:
        Make.IfExp(
            test =
        Make.Name('amplified'),
            body = Make.Name('maxVolume'),
            orElse = Make.Name('defaultVolume')
        )

        # To create the
        `ast.AST` representation of `"sunny" if weather > 70 else "cloudy"`:
        Make.IfExp(
            test = Make.Compare(Make.Name('weather'), [
        Make.Gt() ], [ Make.Constant(70) ]),
            body = Make.Constant("sunny"),
            orElse = Make.Constant("cloudy")
        )
        ```
        """
        return ast.IfExp(test=test, body=body, orelse=orElse, **keywordArguments)

    @staticmethod
    def Import(dotModule: identifierDotAttribute, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Import:
        """Make an `ast.Import` `object` representing a single `import` statement.

        (AI generated docstring.)

        The `ast.Import` `object` represents one `import` statement with zero or more module names separated by commas.
        Each module name is an `ast.alias` `object`. The series of module names is stored in `ast.Import.names` as a
        `list` of `ast.alias`.      Nevertheless, with `Make.Import`, you must create exactly one `ast.alias` `object`
        to be placed in `ast.Import.names`.

        Parameters
        ----------
        dotModule :
            (package.Module notation) The name of the module to import: the name may be in dot notation, also called
            attribute access; the name may be an absolute or relative import. This parameter corresponds with
            `ast.alias.name` in `ast.Import.names[0]`; or, written as one dot-notation statement, it corresponds with
            `ast.Import.names[0].name`.
        asName :
            (as Name) The identifier of the module in the local scope: `asName` must be a valid identifier, so it cannot
            be in dot notation. This parameter corresponds with `ast.alias.asname` in `ast.Import.names[0]`; or, written
            as one dot-notation statement, it corresponds with `ast.Import.names[0].asname`.

        Returns
        -------
        importStatement :
            An `ast.Import` `object` with one `ast.alias` `object` representing a single `import` statement with a
            single module name.

        Examples
        --------
        ```python
        # To represent: `import os`
        Make.Import(dotModule = 'os')

        # To represent: `import re as regex`
        Make.Import(dotModule = 're', asName = 'regex')

        # To represent: `import collections.abc`
        Make.Import(dotModule = 'collections.abc')
        # To represent: `import scipy.signal.windows as SciPy`
        Make.Import(dotModule = 'scipy.signal.windows', asName = 'SciPy')
        ```
        """
        return ast.Import(names=[Make.alias(dotModule, asName)], **keywordArguments)

    @staticmethod
    def ImportFrom(dotModule: str | None, list_alias: list[ast.alias], level: int=0, **keywordArguments: Unpack[ast_attributes]) -> ast.ImportFrom:
        """Make a from-import statement AST `object` for selective module imports.

        (AI generated docstring.)

        The `ast.ImportFrom` `object` represents `from ... import` statements that selectively import specific names
        from modules. It supports relative imports and multiple import aliases.

        Parameters
        ----------
        module :
            The source module name using dot notation, or None for relative imports that rely solely on the level
            parameter.
        names :
            List of alias objects specifying which names to import and their optional aliases.
        level :
            (relative import level) Import level controlling relative vs absolute imports. Zero indicates absolute
            import, positive values indicate relative import depth.

        Returns
        -------
        fromImportStatement : ast.ImportFrom
            AST `object` representing a selective module import statement.
        """
        return ast.ImportFrom(module=dotModule, names=list_alias, level=level, **keywordArguments)

    @staticmethod
    def In() -> ast.In:
        """'In', meaning 'is ***In***cluded in' or 'has membership In', is the `object` representation of Python keyword '`in`'.

        (AI generated docstring.)

        `class` `ast.In` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in `class`
        `ast.Compare`, parameter '`ops`', ***op***erator***s***. The Python interpreter declares *This* `object` 'is
        ***In***cluded in' *That* `iterable` if *This* `object` matches a part of *That* `iterable`.

        Returns
        -------
        membershipOperator : ast.In
            AST `object` representing the keyword '`in`' membership test operator for use in `ast.Compare`.
        """
        return ast.In()

    @staticmethod
    def Interactive(body: Sequence[ast.stmt]) -> ast.Interactive:
        """Create an `ast.Interactive` ({diminutive2etymology['Interactive']}) node for interactive mode modules.

        (AI generated docstring.)

        The `Interactive` node represents a module intended for interactive execution, such as in the Python REPL.
        Unlike regular modules, interactive modules can contain multiple statements that are executed sequentially.

        Parameters
        ----------
        body :
            List of statements forming the interactive module body

        Returns
        -------
        nodeInteractive : ast.Interactive
            The constructed interactive module node
        """
        return ast.Interactive(body=list(body))

    @staticmethod
    def Invert() -> ast.Invert:
        """Make a bitwise complement operator representing Python '`~`' operator.

        (AI generated docstring.)

        Class `ast.Invert` is a subclass of `ast.unaryop` and represents the bitwise complement or inversion operator
        '`~`' in Python source code. This operator performs bitwise NOT operation, flipping all bits of its operand.
        Used within `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        bitwiseComplementOperator : ast.Invert
            AST `object` representing the '`~`' bitwise complement operator for use in `ast.UnaryOp`.
        """
        return ast.Invert()

    @staticmethod
    def Is() -> ast.Is:
        """'Is', meaning 'Is identical to', is the `object` representation of Python keyword '`is`'.

        `class` `ast.Is` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in `class`
        `ast.Compare`, parameter '`ops`', ***op***erator***s***.          The Python interpreter declares *This* logical
        `object` 'Is identical to' *That* logical `object` if they use the same physical memory location. Therefore,
        modifying one `object` will necessarily modify the other `object`.          What's the difference between
        equality and identity? - The work of Jane Austen 'is Equal to' the work of Franz Kafka. - The work of Mark Twain
        'is Equal to' the work of Samuel Clemens. - And Mark Twain 'Is identical to' Samuel Clemens: because they are
        the same person.

        Returns
        -------
        identityOperator :
            AST `object` representing the '`is`' identity comparison operator for use in `ast.Compare`.

        Examples
        --------
        ```python
        # Logically equivalent to: `... valueAttributes is None ...` comparisonNode =
        Make.Compare(
        left=Make.Name('valueAttributes'), ops=[Make.Is()], comparators=[Make.Constant(None)]
        )
        ```

        In the first example, the two
        statements are logically equal but they cannot be identical.
        """
        return ast.Is()

    @staticmethod
    def IsNot() -> ast.IsNot:
        """'IsNot', meaning 'Is Not identical to', is the `object` representation of Python keywords '`is not`'.

        (AI generated docstring.)

        `class` `ast.IsNot` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator',         and only used
        in `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.          The Python interpreter declares
        *This* logical `object` 'Is Not identical to' *That* logical         `object` if they do not use the same
        physical memory location.          What's the difference between equality and identity? - The work of Jane
        Austen 'is Equal to'         the work of Franz Kafka. - The work of Mark Twain 'is Equal to' the work of Samuel
        Clemens.         - And Mark Twain 'Is identical to' Samuel Clemens: because they are the same person.
        Python programmers frequently use '`is not None`' because keyword `None` does not have a         physical memory
        location, so `if chicken is not None`, `chicken` must have a physical memory         location (and be in the
        current scope and blah blah blah...).

        Returns
        -------
        identityNegationOperator :
            AST `object` representing the '`is not`' identity comparison operator for use in `ast.Compare`.

        Examples
        --------
        ```python
        # Logically equivalent to: `... chicken is not None ...` comparisonNode =
        Make.Compare(
            left=Make.Name('chicken'),
        ops=[Make.IsNot()], comparators=[Make.Constant(None)]
        )
        ```

        In the first example, the two statements are logically equal but
        they cannot be identical.
        """
        return ast.IsNot()

    @staticmethod
    def JoinedStr(values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.JoinedStr:
        """Make a joined string AST `object` for f-string literal construction.

        (AI generated docstring.)

        The `ast.JoinedStr` (Joined ***Str***ing) `object` represents f-string literals that combine constant text with
        interpolated expressions. It coordinates multiple string components and formatted values into a single string
        literal.

        Parameters
        ----------
        values :
            Sequence of string components, including `ast.Constant` and `ast.FormattedValue` objects.

        Returns
        -------
        joinedString : ast.JoinedStr
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
        """Make a keyword argument AST object for named parameters in function calls.

        (AI generated docstring.)

        The `ast.keyword` object represents keyword arguments passed to function calls or class constructors. Contains
        the parameter name and corresponding value expression, including support for **keywordArguments unpacking.

        Parameters
        ----------
        Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo :
            Parameter name string; None for **keywordArguments unpacking. This corresponds to `ast.keyword.arg`.
        value :
            Expression providing the argument value.

        Returns
        -------
        keywordArgument :
            AST object representing a named argument in function calls.

        Examples
        --------
        Creates AST equivalent to: temperature=350
        ```python
        namedArgument = Make.keyword('temperature', Make.Constant(350))
        ```
        Creates AST equivalent to: **settings (keyword arguments unpacking)
        ```python
        unpackedArguments = Make.keyword(None,
        Make.Name('settings'))
        ```
        """
        return ast.keyword(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, value=value, **keywordArguments)

    @staticmethod
    def Lambda(argumentSpecification: ast.arguments, body: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Lambda:
        """Make a lambda function AST `object` for anonymous function expressions.

        (AI generated docstring.)

        The `ast.Lambda` (Lambda function) `object` represents lambda expressions that define anonymous functions with a
        single expression body. Lambda functions are limited to expressions and cannot contain statements or multiple
        lines.

        Parameters
        ----------
        argumentSpecification :
            The function arguments specification as `ast.arguments`.
        body :
            Single expression that forms the lambda function body.

        Returns
        -------
        lambdaFunction : ast.Lambda
            AST `object` representing an anonymous lambda function expression.
        """
        return ast.Lambda(args=argumentSpecification, body=body, **keywordArguments)

    @staticmethod
    def List(listElements: Sequence[ast.expr] | None=None, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.List:
        """Make a list literal AST `object` with ordered element collection.

        (AI generated docstring.)

        The `ast.List` `object` represents list literals using square bracket notation. It creates ordered, mutable
        collections and supports various contexts like loading values, storing to variables, or deletion operations.

        Parameters
        ----------
        listElements :
            Sequence of expressions that become list elements.
        context :
            Expression context for how the list is used.

        Returns
        -------
        listLiteral : ast.List
            AST `object` representing a list literal with specified elements.
        """
        return ast.List(elts=list(listElements) if listElements else [], ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def ListComp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.ListComp:
        """Make a list comprehension AST `object` for dynamic list construction.

        (AI generated docstring.)

        The `ast.ListComp` (List ***c***o***mp***rehension) `object` represents list comprehensions that create lists
        using iterator expressions. It provides concise syntax for filtering and transforming collections into new
        lists.

        Parameters
        ----------
        element :
            (***e***lemen***t***) Expression that generates each element of the resulting list.
        generators :
            Sequence of `ast.comprehension` objects defining iterator and filtering.

        Returns
        -------
        listComprehension : ast.ListComp
            AST `object` representing a list comprehension expression.
        """
        return ast.ListComp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Load() -> ast.Load:
        """Make a load context for reading expression values.

        (AI generated docstring.)

        The `ast.Load` context indicates expressions are being read or evaluated to retrieve their values. This is the
        default context for most expressions like `bicycle.wheel` when accessing the wheel attribute value.

        Returns
        -------
        loadContext : ast.Load
            AST context object indicating value retrieval operations.
        """
        return ast.Load()

    class LShift(ast.LShift):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Lt() -> ast.Lt:
        """'Lt', meaning 'is Less than', is the `object` representation of Python comparison operator '`<`'.

        (AI generated docstring.)

        `class` `ast.Lt` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in `class`
        `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        lessThanOperator : ast.Lt
            AST `object` representing the '`<`' less-than comparison operator for use in `ast.Compare`.
        """
        return ast.Lt()

    @staticmethod
    def LtE() -> ast.LtE:
        """'LtE', meaning 'is Less than or Equal to', is the `object` representation of Python comparison operator '`<=`'.

        (AI generated docstring.)

        `class` `ast.LtE` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in
        `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        lessThanOrEqualOperator : ast.LtE
            AST `object` representing the '`<=`' less-than-or-equal comparison operator for use in `ast.Compare`.
        """
        return ast.LtE()

    @staticmethod
    def Match(subject: ast.expr, cases: list[ast.match_case] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Match:
        """Make a match statement AST object for pattern matching with multiple cases.

        (AI generated docstring.)

        The `ast.Match` (Match this) object represents match statements that perform pattern matching against a subject
        expression. Contains the value being matched and a list of case clauses with their patterns and corresponding
        actions.

        Parameters
        ----------
        subject :
            Expression being matched against the case patterns.
        cases :
            (match case) List of match_case objects defining pattern-action pairs.

        Returns
        -------
        matchStatement : ast.Match
            AST object representing a complete pattern matching statement.
        """
        return ast.Match(subject=subject, cases=cases or [], **keywordArguments)

    @staticmethod
    def match_case(pattern: ast.pattern, guard: ast.expr | None=None, body: Sequence[ast.stmt] | None=None) -> ast.match_case:
        """Make a match case clause AST object for individual cases in `match` statements.

        (AI generated docstring.)

        The `ast.match_case` (match case) object represents individual case clauses within match statements. Contains
        the pattern to match, optional guard condition, and statements to execute when the pattern matches successfully.

        Parameters
        ----------
        pattern :
            Pattern expression defining what values match this case.
        guard :
            Optional conditional expression for additional filtering.
        body :
            List of statements to execute when pattern matches.

        Returns
        -------
        matchCase : ast.match_case
            AST object representing a single case clause in match statements.
        """
        return ast.match_case(pattern=pattern, guard=guard, body=list(body) if body else [])

    @staticmethod
    def MatchAs(pattern: ast.pattern | None=None, name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchAs:
        """Create an `ast.MatchAs` node representing a capture pattern or wildcard.

        (AI generated docstring.)

        The `ast.MatchAs` (Match As) node represents match patterns that capture values or serve as wildcards. This
        includes bare name patterns like `bicycle` that capture the matched value, "as" patterns like `Point(x, y) as
        location` that match a pattern and capture the result, and the wildcard pattern `_`.

        Parameters
        ----------
        pattern :
            Optional pattern to match against. When `None`, creates a capture pattern (bare name) if `name` is provided,
            or wildcard if both are `None`.
        name :
            Optional identifier to bind the matched value. When `None` and pattern is also `None`, creates the wildcard
            pattern.

        Returns
        -------
        matchAsNode : ast.MatchAs
            An `ast.MatchAs` node with the specified pattern and name.
        """
        return ast.MatchAs(pattern=pattern, name=name, **keywordArguments)

    @staticmethod
    def MatchClass(cls: ast.expr, patterns: Sequence[ast.pattern] | None=None, kwd_attrs: list[str] | None=None, kwd_patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchClass: # pyright: ignore[reportSelfClsParameterName]
        """Create an `ast.MatchClass` node for matching class instances.

        (AI generated docstring.)

        The `ast.MatchClass` (Match Class) node represents patterns that match instances of a specific class, checking
        both the class type and extracting values from the instance's attributes. This enables structural pattern
        matching against objects.

        Parameters
        ----------
        cls :
            (***cl***a***s***s) Expression identifying the class to match against.
        patterns :
            Sequence of pattern nodes for positional matching against class-defined attributes.
        kwd_attrs :
            (***k***ey***w***or***d*** ***attr***ibute***s***) List of attribute names for keyword-style matching.
        kwd_patterns :
            (***k***ey***w***or***d*** ***patterns***) Sequence of pattern nodes corresponding to the keyword
            attributes.

        Returns
        -------
        matchClassNode : ast.MatchClass
            An `ast.MatchClass` node configured for the specified class and patterns.
        """
        return ast.MatchClass(cls=cls, patterns=list(patterns) if patterns else [], kwd_attrs=kwd_attrs or [], kwd_patterns=list(kwd_patterns) if kwd_patterns else [], **keywordArguments)

    @staticmethod
    def MatchMapping(keys: Sequence[ast.expr] | None=None, patterns: Sequence[ast.pattern] | None=None, rest: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchMapping:
        """Create an `ast.MatchMapping` node for matching dictionary-like objects.

        (AI generated docstring.)

        The `ast.MatchMapping` (Match Mapping) node represents patterns that match mapping objects like dictionaries,
        checking for specific keys and extracting their values. The pattern can also capture remaining unmapped keys.

        Parameters
        ----------
        keys :
            Sequence of expression nodes representing the keys to match.
        patterns :
            Sequence of pattern nodes corresponding to the values associated with each key.
        rest :
            (the rest of the mapping elements) Optional identifier to capture remaining mapping elements not otherwise
            matched.

        Returns
        -------
        matchMappingNode : ast.MatchMapping
            An `ast.MatchMapping` node for the specified key-value patterns and optional rest capture.
        """
        return ast.MatchMapping(keys=list(keys) if keys else [], patterns=list(patterns) if patterns else [], rest=rest, **keywordArguments)

    @staticmethod
    def MatchOr(patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchOr:
        """Create an `ast.MatchOr` node for alternative pattern matching.

        (AI generated docstring.)

        The `ast.MatchOr` (Match this Or that) node represents or-patterns that match if any of the alternative
        subpatterns succeed. The pattern tries each alternative in sequence until one matches or all fail.

        Parameters
        ----------
        patterns :
            Sequence of alternative pattern nodes. The match succeeds if any subpattern matches the subject.

        Returns
        -------
        matchOrNode : ast.MatchOr
            An `ast.MatchOr` node containing the alternative patterns.
        """
        return ast.MatchOr(patterns=list(patterns) if patterns else [], **keywordArguments)

    @staticmethod
    def MatchSequence(patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSequence:
        """Create an `ast.MatchSequence` node for matching sequences.

        (AI generated docstring.)

        The `ast.MatchSequence` (Match this Sequence) node represents patterns that match sequence objects like lists
        and tuples, checking both length and element patterns. Supports both fixed-length and variable-length sequence
        matching.

        Parameters
        ----------
        patterns :
            Sequence of pattern nodes to match against sequence elements. If any pattern is `MatchStar`, enables
            variable-length matching; otherwise requires exact length match.

        Returns
        -------
        matchSequenceNode : ast.MatchSequence
            An `ast.MatchSequence` node for the specified element patterns.
        """
        return ast.MatchSequence(patterns=list(patterns) if patterns else [], **keywordArguments)

    @staticmethod
    def MatchSingleton(value: bool | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSingleton: # noqa: FBT001
        """Create an `ast.MatchSingleton` node for matching singleton values.

        (AI generated docstring.)

        The `ast.MatchSingleton` (Match Singleton) node represents patterns that match singleton constants by identity
        rather than equality. This pattern succeeds only if the match subject is the exact same object as the specified
        constant.

        Parameters
        ----------
        value :
            The singleton constant to match against. Must be `None`, `True`, or `False`. Matching uses identity
            comparison (`is`) rather than equality comparison (`==`).

        Returns
        -------
        matchSingletonNode : ast.MatchSingleton
            An `ast.MatchSingleton` node for the specified singleton value.
        """
        return ast.MatchSingleton(value=value, **keywordArguments)

    @staticmethod
    def MatchStar(name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchStar:
        """Create an `ast.MatchStar` node for capturing sequence remainder.

        (AI generated docstring.)

        The `ast.MatchStar` (Match Star) node represents star patterns that capture remaining elements in variable-
        length sequence patterns. This enables flexible sequence matching where some elements are specifically matched
        and others are collected.

        Parameters
        ----------
        name :
            Optional identifier to bind the remaining sequence elements. When `None`, the remaining elements are matched
            but not captured.

        Returns
        -------
        matchStarNode : ast.MatchStar
            An `ast.MatchStar` node with the specified capture name.
        """
        return ast.MatchStar(name=name, **keywordArguments)

    @staticmethod
    def MatchValue(value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchValue:
        """Create an `ast.MatchValue` node for matching literal values.

        (AI generated docstring.)

        The `ast.MatchValue` (Match Value) node represents patterns that match by equality comparison against a literal
        value or expression. The pattern succeeds if the match subject equals the evaluated value expression.

        Parameters
        ----------
        value :
            Expression node representing the value to match against. Typically a constant, name, or attribute access.
            The expression is evaluated and compared using equality (`==`).

        Returns
        -------
        matchValueNode : ast.MatchValue
            An `ast.MatchValue` node for the specified value expression.
        """
        return ast.MatchValue(value=value, **keywordArguments)

    class MatMult(ast.MatMult):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def mod() -> ast.mod:
        """Create an abstract `ast.mod` (***mod***ule) `object`."""
        return ast.mod()

    class Mod(ast.Mod):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Module(body: Sequence[ast.stmt], type_ignores: list[ast.TypeIgnore] | None=None) -> ast.Module:
        """Make a module AST object representing complete Python modules with statements and type ignores.

        (AI generated docstring.)

        The `ast.Module` object represents entire Python modules as parsed from source files. Contains all top-level
        statements and tracks type ignore comments for static analysis tools and type checkers.

        Parameters
        ----------
        body :
            List of statements forming the module content.
        type_ignores :
            (type ***ignore*** comments) List of TypeIgnore objects for `# noqa: ` comments.

        Returns
        -------
        moduleDefinition :
            AST object representing a complete Python module structure.

        Examples
        --------
        Creates AST equivalent to: x = 42
        ```python
        simpleModule = Make.Module([Make.Assign([Make.Name('x')], Make.Constant(42))])
        ```
        Creates AST equivalent to module with function and assignment
        ```python
        moduleWithFunction = Make.Module([
        Make.FunctionDef('calculate', body=[Make.Return(Make.Constant(100))]),
            Make.Assign([Make.Name('result')], Make.Call(Make.Name('calculate'),
        []))
        ])
        ```
        """
        return ast.Module(body=list(body), type_ignores=type_ignores or [])

    class Mult(ast.Mult):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Name(id: str, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Name:
        """Make a name AST `object` for variable and identifier references.

        (AI generated docstring.)

        The `ast.Name` `object` represents identifiers like variable names, function names, and class names in Python
        code. The context parameter determines whether the name is being loaded, stored to, or deleted.

        Parameters
        ----------
        id :
            (***id***entifier) The identifier string representing the name.
        context :
            Expression context specifying how the name is used.

        Returns
        -------
        nameReference : ast.Name
            AST `object` representing an identifier reference with specified context.
        """
        return ast.Name(id=id, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def NamedExpr(target: ast.Name, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.NamedExpr:
        """Make a named expression AST `object` for assignment expressions (walrus operator).

        (AI generated docstring.)

        The `ast.NamedExpr` (Named ***Expr***ession) `object` represents assignment expressions using the walrus
        operator `:=` introduced in Python 3.8. It allows assignment within expressions and is commonly used in
        comprehensions and conditional statements.

        Parameters
        ----------
        target :
            The `ast.Name` `object` representing the variable being assigned to.
        value :
            The expression whose value is assigned to the target.

        Returns
        -------
        namedExpression :
            AST `object` representing an assignment expression with the walrus operator.

        Examples
        --------
        ```python
        # Creates AST equivalent to: `(inventory := len(warehouse)) > 10`
        inventoryCheck = Make.Compare(
        left=Make.NamedExpr(
                target=Make.Name('inventory', ast.Store()),
                value=Make.Call(Make.Name('len'),
        [Make.Name('warehouse')])
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

        (AI generated docstring.)

        The `Nonlocal` node represents a `nonlocal` statement that declares variables as referring to the nearest
        enclosing scope that is not global. This is used in nested functions to modify variables from outer scopes.

        Parameters
        ----------
        names :
            List of variable names to declare as nonlocal.

        Returns
        -------
        nodeNonlocal : ast.Nonlocal
            The constructed nonlocal declaration node.
        """
        return ast.Nonlocal(names=names, **keywordArguments)

    @staticmethod
    def Not() -> ast.Not:
        """Make a logical negation operator representing Python keyword '`not`'.

        (AI generated docstring.)

        Class `ast.Not` is a subclass of `ast.unaryop` and represents the logical negation operator keyword '`not`' in
        Python source code. This operator returns the boolean inverse of its operand's truthiness. Used within
        `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        logicalNegationOperator : ast.Not
            AST `object` representing the keyword '`not`' logical negation operator for use in `ast.UnaryOp`.
        """
        return ast.Not()

    @staticmethod
    def NotEq() -> ast.NotEq:
        """'NotEq' meaning 'is ***Not*** ***Eq***ual to', is the `object` representation of Python comparison operator '`!=`'.

        (AI generated docstring.)

        `class` `ast.NotEq` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in
        `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***.

        Returns
        -------
        inequalityOperator : ast.NotEq
            AST `object` representing the '`!=`' inequality comparison operator for use in `ast.Compare`.
        """
        return ast.NotEq()

    @staticmethod
    def NotIn() -> ast.NotIn:
        """'NotIn', meaning 'is Not ***In***cluded in' or 'does Not have membership In', is the `object` representation of Python keywords '`not in`'.

        (AI generated docstring.)

        `class` `ast.NotIn` is a subclass of `ast.cmpop`, '***c***o***mp***arison ***op***erator', and only used in
        `class` `ast.Compare`, parameter '`ops`', ***op***erator***s***. The Python interpreter declares *This* `object`
        'is Not ***In***cluded in' *That* `iterable` if *This* `object` does not match a part of *That* `iterable`.

        Returns
        -------
        negativeMembershipOperator : ast.NotIn
            AST `object` representing the keywords '`not in`' negative membership test operator for use in
            `ast.Compare`.
        """
        return ast.NotIn()

    @staticmethod
    def operator() -> ast.operator:
        """Create an `ast.operator` node for arithmetic and bitwise operations.

        (AI generated docstring.)

        The `operator` method creates operator nodes used in binary operations, unary operations, and comparison
        operations. These represent the specific operation to be performed.

        Returns
        -------
        nodeOperator : ast.operator
            The constructed operator node
        """
        return ast.operator()

    class Or(ast.Or):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BoolOp` (***Bool***ean ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating an `ast.BoolOp` (***Bool***ean ***Op***eration) `object` that logically 'joins' the `Sequence`.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Sequence[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing ast.BoolOp structures:
            ast.BoolOp(
                op=ast.And(),
            values=[ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')]
            )

            # Simply use:
            astToolkit.And.join([ast.Name('Lions'), ast.Name('tigers'), ast.Name('bears')])

            # Both produce the same AST structure but the join()
            method eliminates the manual construction.
            ```
            """
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)
    if sys.version_info >= (3, 13):

        @staticmethod
        def ParamSpec(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
            """Make a parameter specification type parameter for generic callable types.

        (AI generated docstring.)

        The `ast.ParamSpec` (***Param***eter ***Spec***ification) object represents parameter specification type
        parameters used in generic callable types. Captures both positional and keyword argument signatures for type-
        safe function composition and higher-order functions.

        Parameters
        ----------
        name :
            Type parameter name as string identifier.
        default_value :
            Optional default type expression (Python 3.13+).

        Returns
        -------
        parameterSpecification : ast.ParamSpec
            AST object representing a parameter specification type parameter.
        """
            return ast.ParamSpec(name=name, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def ParamSpec(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
            """Make a parameter specification type parameter for generic callable types.

        (AI generated docstring.)

        The `ast.ParamSpec` (***Param***eter ***Spec***ification) object represents parameter specification type
        parameters used in generic callable types. Captures both positional and keyword argument signatures for type-
        safe function composition and higher-order functions.

        Parameters
        ----------
        name :
            Type parameter name as string identifier.
        default_value :
            Optional default type expression (Python 3.13+).

        Returns
        -------
        parameterSpecification : ast.ParamSpec
            AST object representing a parameter specification type parameter.
        """
            return ast.ParamSpec(name=name, **keywordArguments)

    @staticmethod
    def Pass(**keywordArguments: Unpack[ast_attributes]) -> ast.Pass:
        """Create an `ast.Pass` node for pass statements.

        (AI generated docstring.)

        The `Pass` node represents a `pass` statement, which is a null operation that does nothing when executed. It
        serves as syntactic placeholder where a statement is required but no action is needed.

        Returns
        -------
        nodePass : ast.Pass
            The constructed pass statement node.
        """
        return ast.Pass(**keywordArguments)

    @staticmethod
    def pattern(**keywordArguments: Unpack[ast_attributes_int]) -> ast.pattern:
        """Create a base `ast.pattern` node.

        (AI generated docstring.)

        Creates a generic `ast.pattern` node that serves as the abstract base for all pattern types in match statements.
        This method is typically used for creating pattern node instances programmatically when the specific pattern
        type is determined at runtime.

        Returns
        -------
        patternNode : ast.pattern
            A base `ast.pattern` node with the specified attributes.
        """
        return ast.pattern(**keywordArguments)

    class Pow(ast.Pow):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Raise(exc: ast.expr | None=None, cause: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Raise:
        """Create an `ast.Raise` node for raise statements.

        (AI generated docstring.)

        The `Raise` node represents a `raise` statement that raises an exception. Can re-raise the current exception,
        raise a new exception, or raise with an explicit cause chain.

        Parameters
        ----------
        exc :
            (***exc***eption) Optional expression for the exception to raise.
        cause :
            Optional expression for the exception cause.

        Returns
        -------
        nodeRaise : ast.Raise
            The constructed raise statement node.
        """
        return ast.Raise(exc=exc, cause=cause, **keywordArguments)

    @staticmethod
    def Return(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Return:
        """Make a return statement AST object for function value returns and early exits.

        (AI generated docstring.)

        The `ast.Return` object represents return statements that exit functions and optionally provide return values.
        Used for both value-returning functions and procedures that return None implicitly or explicitly.

        Parameters
        ----------
        value :
            Optional expression providing the return value; None for empty return.

        Returns
        -------
        returnStatement : ast.Return
            AST object representing a function return with optional value.
        """
        return ast.Return(value=value, **keywordArguments)

    class RShift(ast.RShift):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Set(listElements: Sequence[ast.expr] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Set:
        """Make a set literal AST `object` for unordered unique element collections.

        (AI generated docstring.)

        The `ast.Set` `object` represents set literals using curly brace notation. It creates unordered collections of
        unique elements with efficient membership testing and set operations.

        Parameters
        ----------
        listElements :
            Sequence of expressions that become set elements.

        Returns
        -------
        setLiteral : ast.Set
            AST `object` representing a set literal with specified unique elements.
        """
        return ast.Set(elts=list(listElements) if listElements else [], **keywordArguments)

    @staticmethod
    def SetComp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.SetComp:
        """Make a set comprehension AST `object` for dynamic set construction.

        (AI generated docstring.)

        The `ast.SetComp` (Set ***c***o***mp***rehension) `object` represents set comprehensions that create sets using
        iterator expressions. It automatically handles uniqueness while providing concise syntax for filtering and
        transforming collections.

        Parameters
        ----------
        element :
            Expression that generates each element of the resulting set.
        generators :
            Sequence of `ast.comprehension` objects defining iteration and filtering.

        Returns
        -------
        setComprehension : ast.SetComp
            AST `object` representing a set comprehension expression.
        """
        return ast.SetComp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Slice(lower: ast.expr | None=None, upper: ast.expr | None=None, step: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Slice:
        """Make a slice AST `object` for sequence slicing operations.

        (AI generated docstring.)

        The `ast.Slice` `object` represents slice expressions used with subscription operations to extract subsequences
        from collections. It supports the full Python slicing syntax with optional start, stop, and step parameters.

        Parameters
        ----------
        lower :
            (lower bound) Optional expression for slice start position.
        upper :
            (upper bound) Optional expression for slice end position.
        step :
            Optional expression for slice step size.

        Returns
        -------
        sliceExpression : ast.Slice
            AST `object` representing a slice operation for sequence subscripting.
        """
        return ast.Slice(lower=lower, upper=upper, step=step, **keywordArguments)

    @staticmethod
    def Starred(value: ast.expr, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Starred:
        """Make a starred expression AST `object` for unpacking operations.

        (AI generated docstring.)

        The `ast.Starred` `object` represents starred expressions using the `*` operator for unpacking iterables in
        various contexts like function calls, assignments, and collection literals.

        Parameters
        ----------
        value :
            The expression to be unpacked with the star operator.
        context :
            Expression context determining how the starred expression is used.

        Returns
        -------
        starredExpression :
            AST `object` representing a starred expression for unpacking operations.

        Examples
        --------
        ```python
        # Creates AST equivalent to: `*ingredients` in function call
        unpackIngredients = Make.Starred(Make.Name('ingredients'))
        # Creates AST equivalent to: `*remaining` in assignment like `first, *remaining = groceries`
        unpackRemaining =
        Make.Starred(Make.Name('remaining'), ast.Store())
        ```
        """
        return ast.Starred(value=value, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def stmt(**keywordArguments: Unpack[ast_attributes]) -> ast.stmt:
        """`class` `ast.stmt` (***st***ate***m***en***t***) is the base class for all statement nodes.

        (AI generated docstring.)

        Parameters
        ----------
        **keywordArguments :
            Positional attributes.

        Returns
        -------
        nodeStmt : ast.stmt
            The constructed statement node.
        """
        return ast.stmt(**keywordArguments)

    @staticmethod
    def Store() -> ast.Store:
        """Make a store context for assigning values to expressions.

        (AI generated docstring.)

        The `ast.Store` context indicates expressions are assignment targets receiving new values. Used in assignments,
        loop targets, and function parameters where expressions store rather than load values.

        Returns
        -------
        storeContext :
            AST context object indicating value assignment operations.

        Examples
        --------
        Creates AST equivalent to assignment: bicycle.wheel = newWheel
        ```python
        wheelAssignment = Make.Attribute(Make.Name('bicycle'), 'wheel',
        Make.Store())
        ```
        """
        return ast.Store()

    class Sub(ast.Sub):
        """Identical to the `ast` (abstract syntax tree) class but with a method, `join()`, that 'joins' expressions using the `ast.BinOp` (***Bin***ary ***Op***eration) class."""

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Make a single `ast.expr` (***expr***ession) from a `Sequence` of `ast.expr` by creating nested `ast.BinOp` (***Bin***ary ***Op***eration) `object` that are logically 'joined' by the `ast.operator` subclass.

            Like str.join() (***str***ing) but for AST (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Collection of expressions to join.
            **keywordArguments : ast_attributes


            Returns
            -------
            joinedExpression : ast.expr
                Single expression representing the joined expressions.

            Examples
            --------
            ```python
            # Instead of manually constructing nested ast.BinOp structures:
            ast.BinOp(
                left=ast.BinOp(
            left=ast.Name('Crosby')
                    , op=ast.BitOr()
                    , right=ast.Name('Stills'))
                , op=ast.BitOr()
            , right=ast.Name('Nash')
            )

            # Simply use:
            astToolkit.BitOr().join([ast.Name('Crosby'), ast.Name('Stills'),
            ast.Name('Nash')])

            # Both produce the same AST structure but the join() method eliminates the manual nesting.
            ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Subscript(value: ast.expr, slice: ast.expr, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Subscript:
        """Make a subscript AST `object` for indexing and slicing operations.

        (AI generated docstring.)

        The `ast.Subscript` `object` represents subscription operations using square brackets for indexing, slicing, and
        key access in dictionaries and other subscriptable objects.

        Parameters
        ----------
        value :
            The expression being subscripted (e.g., list, dict, string).
        slice :
            The subscript expression, which can be an index, slice, or key.
        context :
            Expression context for how the subscript is used.

        Returns
        -------
        subscriptExpression : ast.Subscript
            AST `object` representing a subscription operation with brackets.
        """
        return ast.Subscript(value=value, slice=slice, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def Try(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt] | None=None, finalbody: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Try:
        """Make a try-except statement AST `object` for exception handling and resource cleanup.

        (AI generated docstring.)

        The `ast.Try` `object` represents `try-except` statements that handle exceptions and provide cleanup mechanisms.
        It supports multiple exception handlers, optional else clauses, and finally blocks for guaranteed cleanup.

        Parameters
        ----------
        body :
            Sequence of statements in the try block that may raise exceptions.
        handlers :
            List of exception handler objects that catch and process specific exception types or patterns.
        orelse :
            (or Else execute this) Optional statements executed when the try block completes without raising exceptions.
        finalbody :
            (final body) Optional statements always executed for cleanup, regardless of whether exceptions occurred.

        Returns
        -------
        tryStatement : ast.Try
            AST `object` representing an exception handling statement with optional cleanup.
        """
        return ast.Try(body=list(body), handlers=handlers, orelse=list(orElse) if orElse else [], finalbody=list(finalbody) if finalbody else [], **keywordArguments)

    @staticmethod
    def TryStar(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt] | None=None, finalbody: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.TryStar:
        """Make a try-except* statement AST `object` for exception group handling.

        (AI generated docstring.)

        The `ast.TryStar` (Try executing this, protected by `except*` ("except star")) `object` represents `try-except*`
        statements introduced in Python 3.11 for handling exception groups. It enables catching and processing multiple
        related exceptions that occur simultaneously.

        Parameters
        ----------
        body :
            Sequence of statements in the try block that may raise exception groups.
        handlers :
            List of exception handler objects that catch and process specific exception types within exception groups.
        orelse :
            (or Else execute this) Optional statements executed when the try block completes without raising exceptions.
        finalbody :
            (final body) Optional statements always executed for cleanup, regardless of whether exception groups
            occurred.

        Returns
        -------
        tryStarStatement : ast.TryStar
            AST `object` representing an exception group handling statement with optional cleanup.
        """
        return ast.TryStar(body=list(body), handlers=handlers, orelse=list(orElse) if orElse else [], finalbody=list(finalbody) if finalbody else [], **keywordArguments)

    @staticmethod
    def Tuple(listElements: Sequence[ast.expr] | None=None, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Tuple:
        """Make a tuple literal AST `object` for ordered immutable collections.

        (AI generated docstring.)

        The `ast.Tuple` `object` represents tuple literals using parentheses or comma separation. Tuples are immutable,
        ordered collections often used for multiple assignments and function return values.

        Parameters
        ----------
        listElements :
            Sequence of expressions that become tuple elements.
        context :
            Expression context for how the tuple is used.

        Returns
        -------
        tupleLiteral : ast.Tuple
            AST `object` representing a tuple literal with specified elements.
        """
        return ast.Tuple(elts=list(listElements) if listElements else [], ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def type_ignore() -> ast.type_ignore:
        """`class` `ast.type_ignore` (this `type` error, you ignore it) is the base class for `ast.TypeIgnore`.

        (AI generated docstring.)
        """
        return ast.type_ignore()

    @staticmethod
    def type_param(**keywordArguments: Unpack[ast_attributes_int]) -> ast.type_param:
        """Abstract type parameter base for generic type constructs.

        (AI generated docstring.)

        The `ast.type_param` (type ***param***eter) object serves as the abstract base for type parameters including
        TypeVar, ParamSpec, and TypeVarTuple. Provides common functionality for generic type definitions in classes,
        functions, and type aliases.

        Returns
        -------
        typeParameter : ast.type_param
            Abstract AST object representing the base of type parameter hierarchy.
        """
        return ast.type_param(**keywordArguments)

    @staticmethod
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias:
        """Make a type alias definition AST object for `type` statement declarations.

        (AI generated docstring.)

        The `ast.TypeAlias` (Type Alias) object represents type alias definitions using the `type` statement syntax.
        Associates a name with a type expression, supporting generic type parameters for flexible type definitions.

        Parameters
        ----------
        name :
            Name expression (typically ast.Name) for the alias identifier.
        type_params :
            (type ***param***eter***s***) List of type parameters for generic aliases.
        value :
            Type expression defining what the alias represents.

        Returns
        -------
        typeAliasDefinition : ast.TypeAlias
            AST object representing a complete type alias declaration.
        """
        return ast.TypeAlias(name=name, type_params=list(type_params), value=value, **keywordArguments)

    @staticmethod
    def TypeIgnore(lineno: int, tag: str) -> ast.TypeIgnore:
        """Make a type ignore comment AST object for `# noqa: ` directives.

        (AI generated docstring.)

        The `ast.TypeIgnore` (this Type (`type`) error, Ignore it) object represents `# noqa: ` comments that
        instruct static type checkers to skip type analysis for specific lines. Includes optional tags for categorizing
        different types of ignores.

        Parameters
        ----------
        lineno :
            (line _**n**umer**o**_ (_Latin_ "number")) Line number where the ignore comment appears.
        tag :
            Optional string tag for categorizing the ignore (e.g., '[assignment]').

        Returns
        -------
        typeIgnoreDirective :
            AST object representing a type checker ignore comment.

        Examples
        --------
        Creates AST equivalent to: # noqa:  (on line 42)
        ```python
        simpleIgnore = Make.TypeIgnore(42, '')
        ```

        Creates AST
        equivalent to: # pyright: ignore[assignment] (on line 15)
        ```python
        taggedIgnore = Make.TypeIgnore(15, '[assignment]')
        ```
        """
        return ast.TypeIgnore(lineno=lineno, tag=tag)
    if sys.version_info >= (3, 13):

        @staticmethod
        def TypeVar(name: str, bound: ast.expr | None=None, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
            """Make a type variable parameter for generic types with optional bounds and defaults.

        (AI generated docstring.)

        The `ast.TypeVar` (Type ***Var***iable) object represents type variable parameters used in generic classes,
        functions, and type aliases. Supports type bounds, constraints, and default values for flexible generic
        programming.

        Parameters
        ----------
        name :
            Type variable name as string identifier.
        bound :
            Optional type expression constraining allowed types.
        default_value :
            Optional default type expression (Python 3.13+).

        Returns
        -------
        typeVariable : ast.TypeVar
            AST object representing a type variable with optional constraints.
        """
            return ast.TypeVar(name=name, bound=bound, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def TypeVar(name: str, bound: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
            """Make a type variable parameter for generic types with optional bounds and defaults.

        (AI generated docstring.)

        The `ast.TypeVar` (Type ***Var***iable) object represents type variable parameters used in generic classes,
        functions, and type aliases. Supports type bounds, constraints, and default values for flexible generic
        programming.

        Parameters
        ----------
        name :
            Type variable name as string identifier.
        bound :
            Optional type expression constraining allowed types.
        default_value :
            Optional default type expression (Python 3.13+).

        Returns
        -------
        typeVariable : ast.TypeVar
            AST object representing a type variable with optional constraints.
        """
            return ast.TypeVar(name=name, bound=bound, **keywordArguments)
    if sys.version_info >= (3, 13):

        @staticmethod
        def TypeVarTuple(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
            """Make a type variable tuple for variadic generic types.

        (AI generated docstring.)

        The `ast.TypeVarTuple` (Type ***Var***iable ***Tuple***) object represents type variable tuples used for
        variadic generic types that accept variable numbers of type arguments. Enables generic types that work with
        arbitrary-length type sequences.

        Parameters
        ----------
        name :
            Type variable tuple name as string identifier.
        default_value :
            Optional default type tuple expression (Python 3.13+).

        Returns
        -------
        typeVariableTuple : ast.TypeVarTuple
            AST object representing a variadic type variable.
        """
            return ast.TypeVarTuple(name=name, default_value=default_value, **keywordArguments)
    else:

        @staticmethod
        def TypeVarTuple(name: str, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
            """Make a type variable tuple for variadic generic types.

        (AI generated docstring.)

        The `ast.TypeVarTuple` (Type ***Var***iable ***Tuple***) object represents type variable tuples used for
        variadic generic types that accept variable numbers of type arguments. Enables generic types that work with
        arbitrary-length type sequences.

        Parameters
        ----------
        name :
            Type variable tuple name as string identifier.
        default_value :
            Optional default type tuple expression (Python 3.13+).

        Returns
        -------
        typeVariableTuple : ast.TypeVarTuple
            AST object representing a variadic type variable.
        """
            return ast.TypeVarTuple(name=name, **keywordArguments)

    @staticmethod
    def UAdd() -> ast.UAdd:
        """Unary addition operator representing Python '`+`' operator.

        (AI generated docstring.)

        Class `ast.UAdd` (***U***nary ***Add***ition) is a subclass of `ast.unaryop` and represents the unary positive
        operator '`+`' in Python source code. This operator explicitly indicates a positive numeric value. Used within
        `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        unaryPositiveOperator : ast.UAdd
            AST `object` representing the '`+`' unary positive operator for use in `ast.UnaryOp`.
        """
        return ast.UAdd()

    @staticmethod
    def UnaryOp(op: ast.unaryop, operand: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.UnaryOp:
        """Unary operation AST `object` for single-operand operations.

        (AI generated docstring.)

        The `ast.UnaryOp` (***Un***ary ***Op***eration) `object` represents unary operations that take a single operand,
        such as negation, logical not, bitwise inversion, and positive sign operations.

        Parameters
        ----------
        op :
            (***op***erator) The unary operator like `ast.UAdd()`, `ast.USub()`, `ast.Not()`, `ast.Invert()`.
        operand :
            The expression that the unary operator is applied to.

        Returns
        -------
        unaryOperation : ast.UnaryOp
            (***Un***ary ***Op***eration) AST `object` representing a unary operation on a single expression.
        """
        return ast.UnaryOp(op=op, operand=operand, **keywordArguments)

    @staticmethod
    def unaryop() -> ast.unaryop:
        """Abstract unary operator `object` for use in AST construction.

        (AI generated docstring.)

        Class `ast.unaryop` (***un***ary ***op***erator) is the base for all unary operators in Python's AST. It serves
        as the abstract parent for specific unary operators: `ast.Invert`, `ast.Not`, `ast.UAdd`, `ast.USub`. This
        factory method makes a generic unary operator `object` that can be used in the antecedent-action pattern with
        visitor classes.          Unlike `ast.cmpop` which handles binary comparison operations between two operands,
        `ast.unaryop` represents operators that act on a single operand. Both serve as abstract base classes but for
        different categories of operations: `ast.cmpop` for comparisons and `ast.unaryop` for unary transformations.

        Returns
        -------
        unaryOperator :
            Abstract unary operator `object` that serves as the base `class` for all Python unary operators in AST
            structures.
        """
        return ast.unaryop()

    @staticmethod
    def USub() -> ast.USub:
        """Unary subtraction operator representing Python '`-`' operator.

        (AI generated docstring.)

        Class `ast.USub` (***U***nary ***Sub***traction) is a subclass of `ast.unaryop` and represents the unary
        negation operator '`-`' in Python source code. This operator makes the arithmetic negative of its operand. Used
        within `ast.UnaryOp` as the `op` parameter.

        Returns
        -------
        unaryNegativeOperator : ast.USub
            AST `object` representing the '`-`' unary negation operator for use in `ast.UnaryOp`.
        """
        return ast.USub()

    @staticmethod
    def While(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.While:
        """Make a while loop AST `object` for condition-based iteration.

        (AI generated docstring.)

        The `ast.While` `object` represents `while` loops that repeatedly execute a block of statements as long as a
        test condition remains True. It supports optional else clauses that execute when the loop exits normally.

        Parameters
        ----------
        test :
            The boolean expression evaluated before each iteration to determine whether the loop should continue
            executing.
        body :
            Sequence of statements executed repeatedly while the test condition is True.
        orelse :
            (or Else execute this) Optional statements executed when the loop exits normally without encountering a
            break statement.

        Returns
        -------
        whileLoop : ast.While
            AST `object` representing a condition-based iteration statement.
        """
        return ast.While(test=test, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def With(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.With:
        """Make a context manager statement AST `object` for resource management and cleanup.

        (AI generated docstring.)

        The `ast.With` `object` represents `with` statements that manage resources using context managers. These ensure
        proper setup and cleanup of resources like files, database connections, or locks.

        Parameters
        ----------
        items :
            Sequence of context manager items, each specifying a context manager expression and optional variable
            binding for the managed resource.
        body :
            Sequence of statements executed within the context manager scope.

        Returns
        -------
        withStatement : ast.With
            AST `object` representing a context manager statement for resource management.
        """
        return ast.With(items=items, body=list(body), **keywordArguments)

    @staticmethod
    def withitem(context_expr: ast.expr, optional_vars: ast.expr | None=None) -> ast.withitem:
        """Make a context manager item AST object for individual items in `with` statements.

        (AI generated docstring.)

        The `ast.withitem` (with item) object represents individual context manager specifications within `with`
        statements. Contains the context expression and optional variable binding for the context manager's return
        value.

        Parameters
        ----------
        context_expr :
            (***context*** ***expr***ession) Expression providing the context manager object.
        optional_vars :
            (optional ***var***iable***s***) Optional variable expression for `as` binding.

        Returns
        -------
        contextItem : ast.withitem
            AST object representing a single context manager in with statements.
        """
        return ast.withitem(context_expr=context_expr, optional_vars=optional_vars)

    @staticmethod
    def Yield(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Yield:
        """Make a yield expression AST `object` for generator function values.

        (AI generated docstring.)

        The `ast.Yield` (Yield an element) `object` represents yield expressions that produce values in generator
        functions. It suspends function execution and yields a value to the caller, allowing resumption from the same
        point.

        Parameters
        ----------
        value :
            Optional expression to yield; None yields None value.

        Returns
        -------
        yieldExpression : ast.Yield
            (Yield an element) AST `object` representing a yield expression for generator functions.
        """
        return ast.Yield(value=value, **keywordArguments)

    @staticmethod
    def YieldFrom(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.YieldFrom:
        """Make a yield from expression AST `object` for delegating to sub-generators.

        (AI generated docstring.)

        The `ast.YieldFrom` (Yield an element From) `object` represents `yield from` expressions that delegate generator
        execution to another iterable or generator. It provides efficient sub-generator delegation introduced in Python
        3.3.

        Parameters
        ----------
        value :
            The iterable or generator expression to delegate to.

        Returns
        -------
        yieldFromExpression : ast.YieldFrom
            (Yield an element From) AST `object` representing a yield from expression for generator delegation.
        """
        return ast.YieldFrom(value=value, **keywordArguments)
