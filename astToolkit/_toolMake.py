# ruff: noqa: A002
"""Automatically generated file, so changes may be overwritten."""
from __future__ import annotations

from typing import overload, TYPE_CHECKING
import ast
import sys
import warnings

if TYPE_CHECKING:
    from astToolkit.theTypes import ast_attributes, ast_attributes_int, ast_attributes_type_comment, ast_ConstantValue
    from collections.abc import Iterable, Sequence
    from hunterMakesPy import identifierDotAttribute
    from typing import Unpack
    import builtins
warnings.filterwarnings('ignore', category=DeprecationWarning, message='Instantiating abstract AST node class*')

class Make:
    """Create an `ast.AST` (Abstract Syntax Tree) object or an instance of a subclass.

    I describe `keywordArguments` of `Make` methods here.

    Parameters
    ----------
    col_offset : int
        (***col***umn offset) Zero-based UTF-8 byte offset where the source begins.
    end_col_offset : int | None
        (end ***col***umn offset) Zero-based UTF-8 byte offset just after the end of the source on
        `end_lineno`.
    end_lineno : int | None
        (end line _**n**umer**o**_ (_Latin_ "number")) One-based line number where the source ends.
    lineno : int
        (line _**n**umer**o**_ (_Latin_ "number")) One-based line number where the source begins.

    Source Positions and Syntax Fields
    ----------------------------------
    What is an attribute? In Python, an attribute is a named         property of an object. In the
    `ast` (abstract syntax tree) universe, one word may have many different         meanings. Pay
    close attention to capitalization, leading underscores, and context.

            The syntax fields appear in `_fields`, and their types appear in `_field_types`. For
    example, the `attr`         (***attr***ibute) field of `ast.Attribute` holds the name after the
    dot. Other uses of the word         attribute include `getattr`, `setattr`, and
    `ast.MatchClass.kwd_attrs` (***k***ey***w***or***d*** ***attr***ibute***s***).

            The source positions, when available, appear in `_attributes`. They refer to the original
    source, including         when the text contains characters that use multiple UTF-8 bytes. For an
    exception to the usual placement of         source positions in `**keywordArguments`, see
    `Make.TypeIgnore` (this Type (`type`) error, Ignore it), which has         a named `lineno` (line
    _**n**umer**o**_ (_Latin_ "number")) field.
    """

    @staticmethod
    def _boolopJoinMethod(ast_operator: type[ast.boolop], expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr | ast.BoolOp:
        """I use this method to join expressions with a Boolean operator.

        (AI generated docstring)

        `Make.And.join()` and `Make.Or.join()` use one `ast.BoolOp` (***Bool***ean ***Op***eration)
        for two or more expressions.

        Parameters
        ----------
        ast_operator : type[ast.boolop]
            Boolean operator class, `ast.And` or `ast.Or` (`ast.boolop`, ***bool***ean
            ***op***erator).
        expressions : Sequence[ast.expr]
            Operands in evaluation order (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Source positions for the constructed expression.

        Returns
        -------
        joinedExpression : ast.expr
            One `ast.BoolOp` (***Bool***ean ***Op***eration) for two or more operands, the original
            operand for a single input, or an empty string literal for an empty input.
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
        """I use this method to join expressions with a binary operator.

        (AI generated docstring)

        Operator classes such as `Make.Add` use this method to join expressions into left-associated
        `ast.BinOp` (***Bin***ary ***Op***eration) operations.

        Parameters
        ----------
        ast_operator : type[ast.operator]
            Binary operator class such as `ast.Add` or `ast.BitOr`.
        expressions : Iterable[ast.expr]
            Operands in evaluation order (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Source positions for every constructed expression.

        Returns
        -------
        joinedExpression : ast.expr
            Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands, the
            original operand for a single input, or an empty string literal for an empty input.
        """
        listExpressions: list[ast.expr] = list(expressions)
        if not listExpressions:
            listExpressions.append(Make.Constant('', **keywordArguments))
        expressionsJoined: ast.expr = listExpressions[0]
        for expression in listExpressions[1:]:
            expressionsJoined = ast.BinOp(left=expressionsJoined, op=ast_operator(), right=expression, **keywordArguments)
        return expressionsJoined

    class Add(ast.Add):
        """Make an `ast.Add` operator for `+`.

        This subclass of `ast.Add` adds `join()`, which combines expressions into nested `ast.BinOp`
        (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def alias(dotModule: str, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.alias:
        """Make an `ast.alias` object for a single name mapping in an import statement.

        (AI generated docstring)

        An `ast.alias` represents one imported name, with an optional `as` binding.

        Parameters
        ----------
        dotModule : str
            (package.Module notation) Name to import. Use a dotted module path in `import` or a member
            name in `from ... import`. Use `'*'` for a wildcard in a `from ... import` statement. This
            is `ast.alias.name`.
        asName : str | None = None
            (as Name) Local identifier supplied by `as`. Omit it to use the binding implied by the
            import. This is `ast.alias.asname` (as name).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        importAlias : ast.alias
            An `ast.alias` object mapping one import name with an optional local alias.
        """
        return ast.alias(name=dotModule, asname=asName, **keywordArguments)

    class And(ast.And):
        """Make an `ast.And` operator for `and`.

        This subclass of `ast.And` adds `join()`, which combines expressions into one `ast.BoolOp`
        (***Bool***ean ***Op***eration).
        """

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in one `ast.BoolOp` (***Bool***ean ***Op***eration).

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Sequence[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for the constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                One `ast.BoolOp` (***Bool***ean ***Op***eration) for two or more operands, the
                original operand for a single input, or an empty string literal for an empty input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent Lions and tigers and bears.
                ast.BoolOp(
                    op=ast.And(),
                    values=[Make.Name('Lions'), Make.Name('tigers'), Make.Name('bears')],
                )
                Make.And.join([Make.Name('Lions'), Make.Name('tigers'), Make.Name('bears')])
                ```
            """
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def AnnAssign(target: ast.Name | ast.Attribute | ast.Subscript, annotation: ast.expr, value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.AnnAssign:
        """Make an `ast.AnnAssign` (***Ann***otated ***Assign***ment) for an annotated assignment.

        (AI generated docstring)

        An `ast.AnnAssign` (***Ann***otated ***Assign***ment) represents `name: int = 42` or an
        annotation without an assignment, such as `name: int`. For a name target, `Make.AnnAssign`
        sets `simple=1`, the form used for an unparenthesized name. Attribute and subscription targets
        use `simple=0`.

        Parameters
        ----------
        target : ast.Name | ast.Attribute | ast.Subscript
            Assignment target in `Make.Store()` context. Use an `ast.Name`, `ast.Attribute`, or
            `ast.Subscript`.
        annotation : ast.expr
            Annotation expression following `:` (`ast.expr`, ***expr***ession).
        value : ast.expr | None = None
            Value expression following `=`. Omit it for an annotation without an assignment.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        annotatedAssignment : ast.AnnAssign
            The statement for the supplied annotation and optional value.
        """
        return ast.AnnAssign(target=target, annotation=annotation, value=value, simple=int(isinstance(target, ast.Name)), **keywordArguments)

    @staticmethod
    def arg(Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo: str, annotation: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.arg:
        """Make an `ast.arg` (***arg***ument) for one parameter in a function definition.

        (AI generated docstring)

        An `ast.arg` (***arg***ument) represents a single parameter, including a positional-only,
        keyword-only, `*args`, or `**kwargs` parameter. Supply defaults separately in
        `Make.arguments`.

        Parameters
        ----------
        Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo : str
            Name of the parameter, stored in `ast.arg.arg` (***arg***ument).
        annotation : ast.expr | None = None
            Annotation expression following `:` (`ast.expr`, ***expr***ession).
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text from a `# type: ...` comment on
            this parameter.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        argumentDefinition : ast.arg
            An `ast.arg` (***arg***ument) object representing one function parameter with an optional
            type annotation.

        Parameter Naming
        ----------------
        For the first positional-or-keyword parameter of `functionDefinition`,
        `functionDefinition.args.args[0].arg` gives the parameter name. The first `args`
        (***arg***ument***s***) holds the `ast.arguments` specification, and the second holds the list
        of `ast.arg` (***arg***ument) objects.
        """
        return ast.arg(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, annotation=annotation, **keywordArguments)

    @staticmethod
    def arguments(posonlyargs: list[ast.arg] | None=None, list_arg: list[ast.arg] | None=None, vararg: ast.arg | None=None, kwonlyargs: list[ast.arg] | None=None, kw_defaults: Sequence[ast.expr | None] | None=None, kwarg: ast.arg | None=None, defaults: Sequence[ast.expr] | None=None) -> ast.arguments:
        """Make an `ast.arguments` specification for a function or `lambda`.

        (AI generated docstring)

        The `ast.arguments` specification collects the parameters by calling convention and stores
        their default expressions in separate lists.

        Parameters
        ----------
        posonlyargs : list[ast.arg] = []
            (***pos***itional-only ***arg***ument***s***) Positional-only parameters that appear
            before the `/` separator (`ast.arg`, ***arg***ument).
        list_arg : list[ast.arg] = []
            (list of ast.***arg***ument) Positional-or-keyword parameters. This is
            `ast.arguments.args` (***arg***ument***s***).
        vararg : ast.arg | None = None
            (***var***iadic ***arg***ument) The single `*args` parameter that collects extra
            positional arguments.
        kwonlyargs : list[ast.arg] = []
            (***k***ey***w***ord-only ***arg***ument***s***) Keyword-only parameters that appear after
            `*` or `*args`.
        kw_defaults : Sequence[ast.expr | None] = []
            (***k***ey***w***ord defaults) Default expressions aligned with `kwonlyargs`. Use `None`
            for each required parameter and `Make.Constant(None)` for an explicit `None` default
            (`ast.expr`, ***expr***ession).
        kwarg : ast.arg | None = None
            (***k***ey***w***ord ***arg***ument) The single `**kwargs` parameter that collects extra
            keyword arguments.
        defaults : Sequence[ast.expr] = []
            Default expressions for the last parameters in the combined `posonlyargs` and `list_arg`
            lists, in that order.

        Returns
        -------
        functionSignature : ast.arguments
            An `ast.arguments` object holding the complete parameter specification.
        """
        return ast.arguments(posonlyargs=posonlyargs or [], args=list_arg or [], vararg=vararg, kwonlyargs=kwonlyargs or [], kw_defaults=list(kw_defaults) if kw_defaults else [], kwarg=kwarg, defaults=list(defaults) if defaults else [])

    @staticmethod
    def Assert(test: ast.expr, msg: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Assert:
        """Make an `ast.Assert` for an `assert` statement.

        (AI generated docstring)

        An `ast.Assert` represents a condition checked at runtime. A false test raises
        `AssertionError`. Python omits assertions when compiling with optimization enabled.

        Parameters
        ----------
        test : ast.expr
            Expression whose truth value is checked (`ast.expr`, ***expr***ession).
        msg : ast.expr | None = None
            (***m***e***s***sa***g***e) Expression evaluated when the test is false. Its value becomes
            the argument to `AssertionError`.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        assertStatement : ast.Assert
            An `ast.Assert` object representing an assertion statement.
        """
        return ast.Assert(test=test, msg=msg, **keywordArguments)

    @staticmethod
    def Assign(targets: Sequence[ast.expr], value: ast.expr, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.Assign:
        """Make an `ast.Assign` for an assignment statement.

        (AI generated docstring)

        An `ast.Assign` represents a simple assignment such as `x = 5`, an unpacking assignment such
        as `a, b = pair`, or a chained assignment such as `a = b = value`.

        Parameters
        ----------
        targets : Sequence[ast.expr]
            One or more assignment targets in `Make.Store()` context. Use one tuple or list target for
            unpacking, or separate targets for chained assignment (`ast.expr`, ***expr***ession).
        value : ast.expr
            Expression evaluated once. Python assigns the result to each target in order.
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text from a `# type: ...` comment on
            the assignment.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        assignment : ast.Assign
            An `ast.Assign` object representing a variable assignment.
        """
        return ast.Assign(targets=list(targets), value=value, **keywordArguments)

    @staticmethod
    def AST() -> ast.AST:
        """Make an instance of the base class `ast.AST` (Abstract Syntax Tree).

        (AI generated docstring)

        Use a specific factory such as `Make.Name`, `Make.Call`, or `Make.Assign` to represent Python
        syntax.

        Returns
        -------
        astAST : ast.AST
            An instance of the common base class for Python syntax objects.
        """
        return ast.AST()

    @staticmethod
    def AsyncFor(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFor:
        """Make an `ast.AsyncFor` (***Async***hronous For loop) for an `async for` loop.

        (AI generated docstring)

        An `ast.AsyncFor` (***Async***hronous For loop) consumes an asynchronous iterable. The
        optional `orElse` (or Else execute this) clause runs when the asynchronous iterator is
        exhausted.

        Parameters
        ----------
        target : ast.expr
            Assignment target in `Make.Store()` context that receives each item (`ast.expr`,
            ***expr***ession).
        iter : ast.expr
            (***iter***able) Expression that supplies the asynchronous iterable.
        body : Sequence[ast.stmt]
            Statements executed once per item (`ast.stmt`, ***st***ate***m***en***t***).
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed on exhaustion. `break` skips them. This is
            `ast.AsyncFor.orelse` (`AsyncFor` ***Async***hronous For loop, `orelse` or else execute
            this).
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text for the loop target, from a `#
            type: ...` comment.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        asyncForLoop : ast.AsyncFor
            An `ast.AsyncFor` (***Async***hronous For loop) object representing an asynchronous `for`
            loop.

        Async Context
        -------------
        Use `async for` inside an `async def` body. To compile it at the top level, pass
        `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` to `compile()`.
        """
        return ast.AsyncFor(target=target, iter=iter, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def AsyncFunctionDef(name: str, argumentSpecification: ast.arguments | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, returns: ast.expr | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncFunctionDef:
        """Make an `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition) for `async def`.

        (AI generated docstring)

        An `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition) represents a
        coroutine function or, when its body contains `yield`, an asynchronous generator function.

        Parameters
        ----------
        name : str
            Function name as a string identifier.
        argumentSpecification : ast.arguments = Make.arguments()
            Complete parameter specification from `Make.arguments`. Omit it for a function with no
            parameters. This is `ast.AsyncFunctionDef.args` (`AsyncFunctionDef` ***Async***hronous
            Function ***Def***inition, `args` ***arg***ument***s***).
        body : Sequence[ast.stmt] = []
            Statements in the function body. Supply `Make.Pass()` for a body with no other statements
            (`ast.stmt`, ***st***ate***m***en***t***).
        decorator_list : Sequence[ast.expr] = []
            Decorator expressions in source order. Python applies them from the last decorator to the
            first. (`ast.expr`, ***expr***ession)
        returns : ast.expr | None = None
            (this returns) Return annotation following `->`.
        type_params : Sequence[ast.type_param] = []
            (type ***param***eter***s***) Type parameters declared in brackets after the function name
            (`ast.type_param`, type ***param***eter).
        type_comment : str | None = None
            (a `type` annotation in a comment) Function signature text from a `# type: ...` comment,
            such as `'(int) -> str'`.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        asyncFunction : ast.AsyncFunctionDef
            An `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition) object
            representing an asynchronous function definition.
        """
        return ast.AsyncFunctionDef(name=name, args=argumentSpecification or ast.arguments(), body=list(body) if body else [], decorator_list=list(decorator_list) if decorator_list else [], returns=returns, type_params=list(type_params) if type_params else [], **keywordArguments)

    @staticmethod
    def AsyncWith(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.AsyncWith:
        """Make an `ast.AsyncWith` (***Async***hronous With statement) for an `async with` statement.

        (AI generated docstring)

        An `ast.AsyncWith` (***Async***hronous With statement) manages one or more asynchronous
        context managers. Each `ast.withitem` (with item) provides a manager expression and an
        optional `as` target for the value returned by `__aenter__`.

        Parameters
        ----------
        items : list[ast.withitem]
            Context manager specifications in entry order (`ast.withitem`, with item).
        body : Sequence[ast.stmt]
            Statements executed after entering all the context managers (`ast.stmt`,
            ***st***ate***m***en***t***).
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text for the `as` targets, from a `#
            type: ...` comment.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        asyncWithStatement : ast.AsyncWith
            An `ast.AsyncWith` (***Async***hronous With statement) object representing an asynchronous
            context manager statement.

        Async Context
        -------------
        Use `async with` inside an `async def` body. To compile it at the top level, pass
        `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` to `compile()`.
        """
        return ast.AsyncWith(items=items, body=list(body), **keywordArguments)

    @staticmethod
    def Attribute(value: ast.expr, attribute: str, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Attribute:
        """Make an `ast.Attribute` object for dot notation attribute access.

        (AI generated docstring)

        The `ast.Attribute` object represents attribute access using dot notation such as
        `object.method` or `module.Class`.

        Parameters
        ----------
        value : ast.expr
            Base expression providing the object on which attribute access begins (`ast.expr`,
            ***expr***ession).
        attribute : str
            Name following `.`. This is `ast.Attribute.attr` (***attr***ibute).
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` to read, `Make.Store()` to assign, or `Make.Del()` (***Del***ete) to
            delete. This is `ast.Attribute.ctx` (***c***on***t***e***x***t) (`ast.expr_context`,
            ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        attributeAccess : ast.Attribute
            An `ast.Attribute` object representing the attribute access.
        """
        return ast.Attribute(value=value, attr=attribute, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def AugAssign(target: ast.Name | ast.Attribute | ast.Subscript, op: ast.operator, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.AugAssign:
        """Make an `ast.AugAssign` (***Aug***mented ***Assign***ment) for augmented assignment.

        (AI generated docstring)

        An `ast.AugAssign` (***Aug***mented ***Assign***ment) represents an operation such as `total
        += item`. Python evaluates the target once and assigns the operation's result back to it.
        Augmented assignment delimiters include `+=`, `-=`, `*=`, `@=`, `/=`, `//=`, `%=`, `**=`,
        `|=`, `&=`, `^=`, `<<=`, `>>=`.

        Parameters
        ----------
        target : ast.Name | ast.Attribute | ast.Subscript
            One `ast.Name`, `ast.Attribute`, or `ast.Subscript` in `Make.Store()` context.
        op : ast.operator
            (***op***erator) Binary operator for the augmented assignment. For example, `Make.Add()`
            represents the operation in `+=`.
        value : ast.expr
            Right-hand operand of the operation (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        augmentedAssignment : ast.AugAssign
            An `ast.AugAssign` (***Aug***mented ***Assign***ment) object representing a compound
            assignment statement.
        """
        return ast.AugAssign(target=target, op=op, value=value, **keywordArguments)

    @staticmethod
    def Await(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Await:
        """Make an `ast.Await` (***Await*** the asynchronous operation) expression.

        (AI generated docstring)

        An `ast.Await` (***Await*** the asynchronous operation) can suspend a coroutine until an
        awaitable produces a result.

        Parameters
        ----------
        value : ast.expr
            Expression that evaluates to an awaitable, such as a call to an `async def` function
            (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        awaitExpression : ast.Await
            An `ast.Await` (***Await*** the asynchronous operation) object representing a suspension
            point in a coroutine.

        Async Context
        -------------
        Use `await` (***await*** the asynchronous operation) inside an `async def` body. To compile it
        at the top level, pass `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` to `compile()`.
        """
        return ast.Await(value=value, **keywordArguments)

    @staticmethod
    def BinOp(left: ast.expr, op: ast.operator, right: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.BinOp:
        """Make an `ast.BinOp` (***Bin***ary ***Op***eration) for a binary operation.

        (AI generated docstring)

        An `ast.BinOp` (***Bin***ary ***Op***eration) represents one operation on two operands, such
        as `a + b` or `a | b`. Use an operator class's `join()` to build a left-associated series of
        operations.

        Parameters
        ----------
        left : ast.expr
            (left-hand-side operand) Left operand (`ast.expr`, ***expr***ession).
        op : ast.operator
            (***op***erator) Binary operator, such as `Make.Add()`, `Make.Sub()` (***Sub***traction),
            or `Make.MatMult()` (***Mat***rix ***Mult***iplication).
        right : ast.expr
            (right-hand-side operand) Right operand.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        binaryOperation : ast.BinOp
            An `ast.BinOp` (***Bin***ary ***Op***eration) object representing a two-operand
            arithmetic, bitwise, or other binary operation.

        See Also
        --------
        `Make.Add.join`
            Build a series of additions.
        """
        return ast.BinOp(left=left, op=op, right=right, **keywordArguments)

    class BitAnd(ast.BitAnd):
        """Make an `ast.BitAnd` (***Bit***wise And) operator for `&`.

        This subclass of `ast.BitAnd` (***Bit***wise And) adds `join()`, which combines expressions
        into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitOr(ast.BitOr):
        """Make an `ast.BitOr` (***Bit***wise Or) operator for `|`.

        This subclass of `ast.BitOr` (***Bit***wise Or) adds `join()`, which combines expressions into
        nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class BitXor(ast.BitXor):
        """Make an `ast.BitXor` (***Bit***wise e***X***clusive Or) operator for `^`.

        This subclass of `ast.BitXor` (***Bit***wise e***X***clusive Or) adds `join()`, which combines
        expressions into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def BoolOp(op: ast.boolop, values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.BoolOp:
        """Make an `ast.BoolOp` (***Bool***ean ***Op***eration) for an `and` or `or` expression.

        (AI generated docstring)

        An `ast.BoolOp` (***Bool***ean ***Op***eration) stores all operands in an unparenthesized
        chain such as `a and b and c`. Python evaluates them from left to right until the result is
        determined and returns the last operand evaluated.

        Parameters
        ----------
        op : ast.boolop
            (***op***erator) Operator for the entire chain. Use `Make.And()` or `Make.Or()`
            (`ast.boolop`, ***bool***ean ***op***erator).
        values : Sequence[ast.expr]
            Two or more operand expressions in evaluation order (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        booleanOperation : ast.BoolOp
            The expression combining all operands in order.

        See Also
        --------
        `Make.And.join`
            Join expressions with `and`.
        `Make.Or.join`
            Join expressions with `or`.
        """
        return ast.BoolOp(op=op, values=list(values), **keywordArguments)

    @staticmethod
    def boolop() -> ast.boolop:
        """Make an instance of the base class `ast.boolop` (***bool***ean ***op***erator).

        (AI generated docstring)

        Use `Make.And()` or `Make.Or()` to supply a concrete operator to `Make.BoolOp` (***Bool***ean
        ***Op***eration).

        Returns
        -------
        baseBooleanOperator : ast.boolop
            A base `ast.boolop` (***bool***ean ***op***erator) object.
        """
        return ast.boolop()

    @staticmethod
    def Break() -> ast.Break:
        """Make an `ast.Break` object for a `break` statement.

        (AI generated docstring)

        A `break` statement exits the nearest enclosing loop and skips its `else` clause.

        Returns
        -------
        breakStatement : ast.Break
            An `ast.Break` object representing a loop termination statement.
        """
        return ast.Break()

    @staticmethod
    def Call(callee: ast.expr, listParameters: Sequence[ast.expr] | None=None, list_keyword: list[ast.keyword] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Call:
        """Make an `ast.Call` for a call expression.

        (AI generated docstring)

        An `ast.Call` represents a call such as `callback(a, *items, key=val, **options)`.

        Parameters
        ----------
        callee : ast.expr
            Expression that evaluates to the callable. This is `ast.Call.func` (***func***tion)
            (`ast.expr`, ***expr***ession).
        listParameters : Sequence[ast.expr] = []
            Positional argument expressions in call order. Use `Make.Starred` for each `*iterable`
            argument. This is `ast.Call.args` (***arg***ument***s***).
        list_keyword : list[ast.keyword] = []
            (list of ast.***keyword***) Keyword arguments in call order. Use `Make.keyword(None,
            value)` for `**mapping`. This is `ast.Call.keywords`.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        functionCall : ast.Call
            An `ast.Call` object representing a call expression with positional and keyword arguments.
        """
        return ast.Call(func=callee, args=list(listParameters) if listParameters else [], keywords=list_keyword or [], **keywordArguments)

    @staticmethod
    def ClassDef(name: str, bases: Sequence[ast.expr] | None=None, list_keyword: list[ast.keyword] | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.ClassDef:
        """Make an `ast.ClassDef` (***Class*** ***Def***inition) for a class statement.

        (AI generated docstring)

        An `ast.ClassDef` (***Class*** ***Def***inition) can include base classes, class keywords,
        decorators, and a list of type parameters for a generic class.

        Parameters
        ----------
        name : str
            Class name as a string identifier.
        bases : Sequence[ast.expr] = []
            Sequence of base class expressions for inheritance. An empty sequence produces a class
            with no explicit bases (`ast.expr`, ***expr***ession).
        list_keyword : list[ast.keyword] = []
            (list of ast.***keyword***) Class keywords such as `metaclass=ABCMeta`. This is
            `ast.ClassDef.keywords` (***Class*** ***Def***inition).
        body : Sequence[ast.stmt] = []
            Statements in the class body. Supply `Make.Pass()` for a class body with no other
            statements (`ast.stmt`, ***st***ate***m***en***t***).
        decorator_list : Sequence[ast.expr] = []
            Decorator expressions in source order. Python applies them from the last decorator to the
            first.
        type_params : Sequence[ast.type_param] = []
            (type ***param***eter***s***) Type parameters declared in brackets after the class name.
            (`ast.type_param`, type ***param***eter)
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        classDefinition : ast.ClassDef
            An `ast.ClassDef` (***Class*** ***Def***inition) object representing a complete class
            declaration.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Creates AST equivalent to: class Vehicle: pass
            simpleClass = Make.ClassDef('Vehicle', body=[Make.Pass()])

            # Creates AST equivalent to: class Bicycle(Vehicle, metaclass=ABCMeta): pass
            inheritedClass = Make.ClassDef(
                'Bicycle',
                bases=[Make.Name('Vehicle')],
                list_keyword=[Make.keyword('metaclass', Make.Name('ABCMeta'))],
                body=[Make.Pass()]
            )
            ```
        """
        return ast.ClassDef(name=name, bases=list(bases) if bases else [], keywords=list_keyword or [], body=list(body) if body else [], decorator_list=list(decorator_list) if decorator_list else [], type_params=list(type_params) if type_params else [], **keywordArguments)

    @staticmethod
    def cmpop() -> ast.cmpop:
        """Make an instance of the base class `ast.cmpop` (***c***o***mp***arison ***op***erator).

        (AI generated docstring)

        Use a concrete comparison operator such as `Make.Eq()` (is ***Eq***ual to) or `Make.Lt()` (is
        ***L***ess ***t***han) in `Make.Compare`.

        Returns
        -------
        comparisonOperator : ast.cmpop
            A base `ast.cmpop` (***c***o***mp***arison ***op***erator) object.
        """
        return ast.cmpop()

    @staticmethod
    def Compare(left: ast.expr, ops: Sequence[ast.cmpop], comparators: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Compare:
        """Make an `ast.Compare` object for a comparison expression, including chained comparisons.

        (AI generated docstring)

        An `ast.Compare` represents a comparison such as `x == 0` or a chain such as `0 <= x < 100`. A
        chain compares adjacent operands from left to right, evaluates each intermediate operand once,
        and stops at the first false comparison.

        Parameters
        ----------
        left : ast.expr
            (left-hand-side operand) Leftmost operand (`ast.expr`, ***expr***ession).
        ops : Sequence[ast.cmpop]
            (***op***erator***s***) One or more comparison operators, with one operator per entry in
            `comparators` (`ast.cmpop`, ***c***o***mp***arison ***op***erator).
        comparators : Sequence[ast.expr]
            Operands following `left`, in source order. For `a < b <= c`, supply `[b, c]`.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        comparison : ast.Compare
            An `ast.Compare` object representing a comparison or chained comparison expression.

        Examples
        --------
            ```python
            from astToolkit import Make

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
        """Make an `ast.comprehension` for one `for` clause and its filters.

        (AI generated docstring)

        The `generators` list of a comprehension or generator expression holds these clauses. Write
        them in source order, from the outermost to the innermost loop.

        Parameters
        ----------
        target : ast.expr
            Assignment target in `Make.Store()` context that receives each item (`ast.expr`,
            ***expr***ession).
        iter : ast.expr
            (***iter***able) Expression supplying the iterable or asynchronous iterable.
        ifs : Sequence[ast.expr]
            (if clauses) Filter expressions following this `for` clause. All must be truthy for an
            item to proceed. An empty sequence applies no filter.
        is_async : int = 0
            (is ***async***hronous) Use `1` for `async for` or `0` for `for`.

        Returns
        -------
        comprehensionClause : ast.comprehension
            An `ast.comprehension` object representing one `for` clause with optional filters.
        """
        return ast.comprehension(target=target, iter=iter, ifs=list(ifs), is_async=is_async)

    @staticmethod
    def Constant(value: ast_ConstantValue, kind: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Constant:
        """Make an `ast.Constant` object for a literal value in Python source.

        (AI generated docstring)

        An `ast.Constant` stores a literal's Python value. Use `Make.UnaryOp` (***Un***ary
        ***Op***eration) for a sign attached to a numeric literal in source.

        Parameters
        ----------
        value : ast_ConstantValue
            Literal value, such as an integer, float, complex number, string, bytes, `True`, `False`,
            `None`, or `Ellipsis`.
        kind : str | None = None
            Use `'u'` for a `u`-prefixed string literal. Omit `kind` for other literals.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        constantValue : ast.Constant
            An `ast.Constant` object holding the specified literal value.
        """
        return ast.Constant(value=value, kind=kind, **keywordArguments)

    @staticmethod
    def Continue() -> ast.Continue:
        """Make an `ast.Continue` object for a `continue` statement.

        (AI generated docstring)

        A `continue` statement skips the rest of the current iteration of the nearest enclosing loop.

        Returns
        -------
        continueStatement : ast.Continue
            An `ast.Continue` object representing a loop continuation statement.
        """
        return ast.Continue()

    @staticmethod
    def Del() -> ast.Del:
        """Make an `ast.Del` (***Del***ete) context for a deletion target.

        (AI generated docstring)

        Use `Make.Del()` (***Del***ete) as `context` on an expression passed to `Make.Delete`, such as
        an attribute in `del bicycle.wheel`.

        Returns
        -------
        deleteContext : ast.Del
            Expression context for deletion.
        """
        return ast.Del()

    @staticmethod
    def Delete(targets: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.Delete:
        """Make an `ast.Delete` for a `del` statement.

        (AI generated docstring)

        A `del` statement can remove a name binding, an attribute, an item, or a slice.

        Parameters
        ----------
        targets : Sequence[ast.expr]
            One or more targets in `Make.Del()` (***Del***ete) context, in deletion order.
            (`ast.expr`, ***expr***ession)
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        deleteStatement : ast.Delete
            The `del` statement for the supplied targets.
        """
        return ast.Delete(targets=list(targets), **keywordArguments)

    @staticmethod
    def Dict(keys: Sequence[ast.expr | None] | None=None, values: Sequence[ast.expr] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Dict:
        """Make an `ast.Dict` (***Dict***ionary) for a dictionary display.

        (AI generated docstring)

        An `ast.Dict` (***Dict***ionary) represents entries such as `{'name': value, **options}`. Each
        key has a corresponding expression in `values`. Later entries replace earlier entries with the
        same key.

        Parameters
        ----------
        keys : Sequence[ast.expr | None] = []
            Key expressions. Use `None` as the key for each `**mapping` entry (`ast.expr`,
            ***expr***ession).
        values : Sequence[ast.expr] = []
            Value expressions paired with `keys`. For an unpacking entry, provide the mapping
            expression.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        dictionaryLiteral : ast.Dict
            `AST` (Abstract Syntax Tree) object representing a dictionary literal with specified
            key-value pairs.
        """
        return ast.Dict(keys=list(keys) if keys else [], values=list(values) if values else [], **keywordArguments)

    @staticmethod
    def DictComp(key: ast.expr, value: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.DictComp:
        """Make an `ast.DictComp` (***Dict***ionary ***c***o***mp***rehension) expression.

        (AI generated docstring)

        An `ast.DictComp` (***Dict***ionary ***c***o***mp***rehension) represents key-value generation
        such as `{recipe: difficulty for recipe in cookbook}`. For dictionary unpacking, such as
        `{**mapping for mapping in mappings}`, pass the mapping expression as `key` and `None` as
        `value` [1].

        Parameters
        ----------
        key : ast.expr
            Expression for each key, or for the mapping to unpack when `value` is `None` (`ast.expr`,
            ***expr***ession).
        value : ast.expr | None
            Expression for each value. Use `None` to represent `**` unpacking. The factory forwards
            `None` to `ast.DictComp` (***Dict***ionary ***c***o***mp***rehension) even though its
            annotation lists only `ast.expr`.
        generators : list[ast.comprehension]
            `for` clauses and filters in source order.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        dictionaryComprehension : ast.DictComp
            `AST` (Abstract Syntax Tree) object representing a dictionary comprehension expression.

        See Also
        --------
        `Make.comprehension`
            Create one `for` clause and its filters.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Creates AST equivalent to: `{recipe: difficulty for recipe in cookbook}`
            recipeDifficulty = Make.DictComp(
                key=Make.Name('recipe'),
                value=Make.Name('difficulty'),
                generators=[Make.comprehension(
                    target=Make.Name('recipe', Make.Store()),
                    iter=Make.Name('cookbook'),
                    ifs=[]
                )]
            )
            ```

        References
        ----------
        [1] Unpacking in comprehensions
            https://docs.python.org/3.15/reference/expressions.html#unpacking-in-comprehensions
        """
        return ast.DictComp(key=key, value=value, generators=generators, **keywordArguments)

    class Div(ast.Div):
        """Make an `ast.Div` (***Div***ision) operator for `/`.

        This subclass of `ast.Div` (***Div***ision) adds `join()`, which combines expressions into
        nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Eq() -> ast.Eq:
        """Make an `ast.Eq` (is ***Eq***ual to) comparison operator.

        (AI generated docstring)

        Use `ast.Eq` (is ***Eq***ual to) in the `ops` (***op***erator***s***) of `Make.Compare` to
        represent `==`.

        Returns
        -------
        equalityOperator : ast.Eq
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.Eq()

    @staticmethod
    def ExceptHandler(type: ast.expr | None=None, name: str | None=None, body: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.ExceptHandler:
        """Make an `ast.ExceptHandler` (***Except***ion ***Handler***) clause.

        (AI generated docstring)

        The enclosing `ast.Try` represents `except`. The enclosing `ast.TryStar` (Try executing this,
        protected by `except*` ("except star")) represents `except*` and handles matching members of
        an exception group.

        Parameters
        ----------
        type : ast.expr | None = None
            Exception type expression or tuple of types. Omit it for a bare `except` (`ast.expr`,
            ***expr***ession).
        name : str | None = None
            Identifier after `as`, if supplied.
        body : Sequence[ast.stmt] = []
            Statements executed when the handler matches (`ast.stmt`, ***st***ate***m***en***t***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        exceptionHandler : ast.ExceptHandler
            `AST` (Abstract Syntax Tree) object representing an except clause in try-except
            statements.
        """
        return ast.ExceptHandler(type=type, name=name, body=list(body) if body else [], **keywordArguments)

    @staticmethod
    def excepthandler(**keywordArguments: Unpack[ast_attributes]) -> ast.excepthandler:
        """Make an instance of the base class `ast.excepthandler` (***except***ion ***handler***).

        (AI generated docstring)

        Use `Make.ExceptHandler` (***Except***ion ***Handler***) to make a concrete handler for
        `Make.Try` or `Make.TryStar` (Try executing this, protected by `except*` ("except star")).

        Parameters
        ----------
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        exceptionHandler : ast.excepthandler
            Abstract `AST` (Abstract Syntax Tree) object for exception handling clause classification.
        """
        return ast.excepthandler(**keywordArguments)

    @staticmethod
    def Expr(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Expr:
        """Make an `ast.Expr` (***Expr***ession) for an expression statement.

        (AI generated docstring)

        Use an `ast.Expr` (***Expr***ession) to put an expression in a statement list, such as a call
        made for its side effects or a string used as a docstring.

        Parameters
        ----------
        value : ast.expr
            Expression evaluated as a standalone statement (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        expressionStatement : ast.Expr
            A statement containing the supplied expression.
        """
        return ast.Expr(value=value, **keywordArguments)

    @staticmethod
    def expr(**keywordArguments: Unpack[ast_attributes]) -> ast.expr:
        """Make an instance of the base class `ast.expr` (***expr***ession).

        (AI generated docstring)

        Use a concrete expression factory, such as `Make.Name` or `Make.Call`, to represent syntax
        that evaluates to a value. Use `Make.Expr` (***Expr***ession) to place an expression where
        Python expects a statement.

        Parameters
        ----------
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        expression : ast.expr
            An instance of the common base class for expressions.

        See Also
        --------
        `Make.Expr`
            Use an expression as a statement.
        """
        return ast.expr(**keywordArguments)

    @staticmethod
    def expr_context() -> ast.expr_context:
        """Make an instance of the base class `ast.expr_context` (***expr***ession ***context***).

        (AI generated docstring)

        Use `Make.Load()`, `Make.Store()`, or `Make.Del()` (***Del***ete) to mark an expression as a
        read, an assignment target, or a deletion target.

        Returns
        -------
        expressionContext : ast.expr_context
            Abstract `AST` (Abstract Syntax Tree) context object for expression usage classification.
        """
        return ast.expr_context()

    @staticmethod
    def Expression(body: ast.expr) -> ast.Expression:
        """Make an `ast.Expression` for compilation in `eval` mode.

        (AI generated docstring)

        An `ast.Expression` is the outermost object returned by `ast.parse(..., mode='eval')`.

        Parameters
        ----------
        body : ast.expr
            Single expression to evaluate (`ast.expr`, ***expr***ession).

        Returns
        -------
        expression : ast.Expression
            The expression and its `eval`-mode container.
        """
        return ast.Expression(body=body)

    class FloorDiv(ast.FloorDiv):
        """Make an `ast.FloorDiv` (Floor ***Div***ision) operator for `//`.

        This subclass of `ast.FloorDiv` (Floor ***Div***ision) adds `join()`, which combines
        expressions into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def For(target: ast.expr, iter: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.For:
        """Make an `ast.For` for a `for` loop.

        (AI generated docstring)

        An `ast.For` consumes an iterable. The optional `orElse` (or Else execute this) clause runs
        when the iterator is exhausted.

        Parameters
        ----------
        target : ast.expr
            Assignment target in `Make.Store()` context that receives each item (`ast.expr`,
            ***expr***ession).
        iter : ast.expr
            (***iter***able) Expression that supplies the iterable.
        body : Sequence[ast.stmt]
            Statements executed once per item (`ast.stmt`, ***st***ate***m***en***t***).
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed on exhaustion. `break` skips them. This is
            `ast.For.orelse` (or else execute this).
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text for the loop target, from a `#
            type: ...` comment.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        forLoop : ast.For
            `AST` (Abstract Syntax Tree) object representing a for loop iteration construct.
        """
        return ast.For(target=target, iter=iter, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def FormattedValue(value: ast.expr, conversion: int, format_spec: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.FormattedValue:
        """Make an `ast.FormattedValue` for a replacement field in an f-string.

        (AI generated docstring)

        Use `Make.JoinedStr` (Joined ***Str***ing) to combine replacement fields and literal text into
        an f-string.

        Parameters
        ----------
        value : ast.expr
            Expression inside the braces (`ast.expr`, ***expr***ession).
        conversion : int
            Use `-1` for no explicit conversion, or `ord('s')`, `ord('r')`, or `ord('a')` for `!s`,
            `!r`, or `!a`.
        format_spec : ast.expr | None = None
            (format ***spec***ification) Format specification following `:` as an `ast.JoinedStr`
            (Joined ***Str***ing). Omit it when the field has no format specification.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        formattedValue : ast.FormattedValue
            `AST` (Abstract Syntax Tree) object representing a formatted value within an f-string
            expression.
        """
        return ast.FormattedValue(value=value, conversion=conversion, format_spec=format_spec, **keywordArguments)

    @staticmethod
    def FunctionDef(name: str, argumentSpecification: ast.arguments | None=None, body: Sequence[ast.stmt] | None=None, decorator_list: Sequence[ast.expr] | None=None, returns: ast.expr | None=None, type_params: Sequence[ast.type_param] | None=None, **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.FunctionDef:
        """Make an `ast.FunctionDef` (Function ***Def***inition) for a function.

        (AI generated docstring)

        An `ast.FunctionDef` (Function ***Def***inition) can include a parameter specification,
        decorators, a return annotation, and type parameters for a generic function.

        Parameters
        ----------
        name : str
            Function name as string identifier.
        argumentSpecification : ast.arguments = Make.arguments()
            Complete parameter specification from `Make.arguments`. Omit it for a function with no
            parameters. This is `ast.FunctionDef.args` (`FunctionDef` Function ***Def***inition,
            `args` ***arg***ument***s***).
        body : Sequence[ast.stmt] = []
            Statements in the function body. Supply `Make.Pass()` for a body with no other statements
            (`ast.stmt`, ***st***ate***m***en***t***).
        decorator_list : Sequence[ast.expr] = []
            Decorator expressions in source order. Python applies them from the last decorator to the
            first. (`ast.expr`, ***expr***ession)
        returns : ast.expr | None = None
            (this returns) Return annotation following `->`.
        type_params : Sequence[ast.type_param] = []
            (type ***param***eter***s***) Type parameters declared in brackets after the function name
            (`ast.type_param`, type ***param***eter).
        type_comment : str | None = None
            (a `type` annotation in a comment) Function signature text from a `# type: ...` comment,
            such as `'(int) -> str'`.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        functionDefinition : ast.FunctionDef
            `AST` (Abstract Syntax Tree) object representing a complete function definition with
            metadata.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Creates AST equivalent to: def cook(): pass
            simpleFunction = Make.FunctionDef('cook', body=[Make.Pass()])

            # Define bake with an annotated signature and a default temperature.
            typedFunction = Make.FunctionDef(
                'bake',
                Make.arguments(
                    list_arg=[Make.arg('recipe', Make.Name('str')), Make.arg('temperature', Make.Name('int'))],
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
        """Make an `ast.FunctionType` (Function Type) for a function type comment.

        (AI generated docstring)

        An `ast.FunctionType` (Function Type) represents text such as `(int, str) -> bool`, as
        returned by `ast.parse(..., mode='func_type')`. To attach the comment to a function, supply
        the text as `type_comment` (a `type` annotation in a comment) to `Make.FunctionDef` (Function
        ***Def***inition).

        Parameters
        ----------
        argtypes : Sequence[ast.expr]
            (***arg***ument types) Parameter type expressions in order (`ast.expr`, ***expr***ession).
        returns : ast.expr
            (this returns) Return type expression following `->`.

        Returns
        -------
        functionType : ast.FunctionType
            The parameter types and return type from a function type comment.
        """
        return ast.FunctionType(argtypes=list(argtypes), returns=returns)

    @staticmethod
    def GeneratorExp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.GeneratorExp:
        """Make an `ast.GeneratorExp` (Generator ***Exp***ression) for a generator expression.

        (AI generated docstring)

        An `ast.GeneratorExp` (Generator ***Exp***ression) represents an expression such as
        `(item.name for item in items)`. Python evaluates the first iterable when creating the
        generator, then produces values as the generator advances.

        Parameters
        ----------
        element : ast.expr
            Expression that produces a value. For `(*items for items in groups)`, use `Make.Starred`
            to yield each unpacked item. This is `ast.GeneratorExp.elt` (`GeneratorExp` Generator
            ***Exp***ression, `elt` ***e***lemen***t***) (`ast.expr`, ***expr***ession).
        generators : list[ast.comprehension]
            `for` clauses and filters in source order.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        generatorExpression : ast.GeneratorExp
            `AST` (Abstract Syntax Tree) object representing a generator expression for lazy
            evaluation.
        """
        return ast.GeneratorExp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Global(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Global:
        """Make an `ast.Global` for a `global` declaration.

        (AI generated docstring)

        A `global` declaration directs references and assignments to the specified names to module
        scope throughout the enclosing code block.

        Parameters
        ----------
        names : list[str]
            Identifiers declared global.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        globalStatement : ast.Global
            The declaration for the supplied names.
        """
        return ast.Global(names=names, **keywordArguments)

    @staticmethod
    def Gt() -> ast.Gt:
        """Make an `ast.Gt` (is ***G***reater ***t***han) comparison operator.

        (AI generated docstring)

        Use `ast.Gt` (is ***G***reater ***t***han) in the `ops` (***op***erator***s***) of
        `Make.Compare` to represent `>`.

        Returns
        -------
        greaterThanOperator : ast.Gt
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.Gt()

    @staticmethod
    def GtE() -> ast.GtE:
        """Make an `ast.GtE` (is ***G***reater ***t***han or ***E***qual to) comparison operator.

        (AI generated docstring)

        Use `ast.GtE` (is ***G***reater ***t***han or ***E***qual to) in the `ops`
        (***op***erator***s***) of `Make.Compare` to represent `>=`.

        Returns
        -------
        greaterThanOrEqualOperator : ast.GtE
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.GtE()

    @staticmethod
    def If(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.If:
        """Make an `ast.If` for an `if` statement.

        (AI generated docstring)

        Use another `ast.If` as the only statement in `orElse` (or Else execute this) to represent an
        `elif` clause.

        Parameters
        ----------
        test : ast.expr
            Condition expression evaluated for truth (`ast.expr`, ***expr***ession).
        body : Sequence[ast.stmt]
            Statements executed when `test` is truthy (`ast.stmt`, ***st***ate***m***en***t***).
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed when `test` is falsy. This is `ast.If.orelse`
            (or else execute this).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        conditionalStatement : ast.If
            `AST` (Abstract Syntax Tree) object representing a conditional branching statement.

        Examples
        --------
            ```python
            from astToolkit import Make

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
                [Make.Assign([Make.Name('grade', Make.Store())], Make.Constant('A'))],
                [Make.If(
                    Make.Compare(Make.Name('score'), [Make.GtE()], [Make.Constant(80)]),
                    [Make.Assign([Make.Name('grade', Make.Store())], Make.Constant('B'))],
                    [Make.Assign([Make.Name('grade', Make.Store())], Make.Constant('C'))]
                )]
            )
            ```
        """
        return ast.If(test=test, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def IfExp(test: ast.expr, body: ast.expr, orElse: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.IfExp:
        """Make an `ast.IfExp` (If ***Exp***ression) for a conditional expression.

        (AI generated docstring)

        An `ast.IfExp` (If ***Exp***ression) represents `valueIfTrue if condition else valueIfFalse`.
        Python evaluates the condition and then evaluates only the selected expression.

        Parameters
        ----------
        test : ast.expr
            Condition expression evaluated for truth (`ast.expr`, ***expr***ession).
        body : ast.expr
            Expression selected when `test` is truthy.
        orElse : ast.expr
            (or Else execute this) Expression selected when `test` is falsy. This is
            `ast.IfExp.orelse` (`IfExp` If ***Exp***ression, `orelse` or else execute this).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        conditionalExpression : ast.IfExp
            The conditional expression with both alternatives.

        Examples
        --------
            ```python
            from astToolkit import Make

            # To create the `ast.AST` representation of `maxVolume if amplified else defaultVolume`:
            Make.IfExp(
                test = Make.Name('amplified'),
                body = Make.Name('maxVolume'),
                orElse = Make.Name('defaultVolume')
            )

            # To create the `ast.AST` representation of `"sunny" if weather > 70 else "cloudy"`:
            Make.IfExp(
                test = Make.Compare(Make.Name('weather'), [ Make.Gt() ], [ Make.Constant(70) ]),
                body = Make.Constant("sunny"),
                orElse = Make.Constant("cloudy")
            )
            ```
        """
        return ast.IfExp(test=test, body=body, orelse=orElse, **keywordArguments)
    if sys.version_info >= (3, 15):

        @staticmethod
        def Import(dotModule: identifierDotAttribute, asName: str | None=None, is_lazy: bool | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Import:
            """Make an `ast.Import` for one module in an `import` statement.

            (AI generated docstring)

            `Make.Import` supplies the single `ast.alias` stored in `ast.Import.names`. A plain `import`
            accepts an absolute module path such as `collections.abc`. Use `Make.ImportFrom` for relative
            imports.

            Parameters
            ----------
            dotModule : identifierDotAttribute
                (package.Module notation) Absolute module name, optionally dotted. This is
                `ast.Import.names[0].name`.
            asName : str | None = None
                (as Name) Local identifier after `as`. When omitted, the import binds the first component
                of `dotModule`. This is `ast.Import.names[0].asname` (as name).
            is_lazy : bool | None = None
                Use `True` to represent the `lazy` prefix. Omit it or use `False` for a regular `import`
                statement. Explicit lazy imports require module scope and exclude `try` blocks [1].
            **keywordArguments : ast_attributes
                Optional source positions. See `Make` for line numbers and byte offsets.

            Returns
            -------
            importStatement : ast.Import
                An `ast.Import` object with one `ast.alias` object representing a single `import`
                statement with a single module name.

            See Also
            --------
            `Make.ImportFrom`
                Import names from a module.

            Examples
            --------
                ```python
                from astToolkit import Make

                # To represent: `import os`
                Make.Import(dotModule = 'os')

                # To represent: `import re as regex`
                Make.Import(dotModule = 're', asName = 'regex')

                # To represent: `import collections.abc`
                Make.Import(dotModule = 'collections.abc')

                # To represent: `import scipy.signal.windows as SciPy`
                Make.Import(dotModule = 'scipy.signal.windows', asName = 'SciPy')
                ```

            References
            ----------
            [1] Lazy imports.
                https://docs.python.org/3.15/reference/simple_stmts.html#lazy-imports
            """
            return ast.Import(names=[Make.alias(dotModule, asName)], is_lazy=is_lazy, **keywordArguments)
    else:

        @staticmethod
        def Import(dotModule: identifierDotAttribute, asName: str | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Import:
            """Make an `ast.Import` for one module in an `import` statement.

            (AI generated docstring)

            `Make.Import` supplies the single `ast.alias` stored in `ast.Import.names`. A plain `import`
            accepts an absolute module path such as `collections.abc`. Use `Make.ImportFrom` for relative
            imports.

            Parameters
            ----------
            dotModule : identifierDotAttribute
                (package.Module notation) Absolute module name, optionally dotted. This is
                `ast.Import.names[0].name`.
            asName : str | None = None
                (as Name) Local identifier after `as`. When omitted, the import binds the first component
                of `dotModule`. This is `ast.Import.names[0].asname` (as name).
            is_lazy : bool | None = None
                Use `True` to represent the `lazy` prefix. Omit it or use `False` for a regular `import`
                statement. Explicit lazy imports require module scope and exclude `try` blocks [1].
            **keywordArguments : ast_attributes
                Optional source positions. See `Make` for line numbers and byte offsets.

            Returns
            -------
            importStatement : ast.Import
                An `ast.Import` object with one `ast.alias` object representing a single `import`
                statement with a single module name.

            See Also
            --------
            `Make.ImportFrom`
                Import names from a module.

            Examples
            --------
                ```python
                from astToolkit import Make

                # To represent: `import os`
                Make.Import(dotModule = 'os')

                # To represent: `import re as regex`
                Make.Import(dotModule = 're', asName = 'regex')

                # To represent: `import collections.abc`
                Make.Import(dotModule = 'collections.abc')

                # To represent: `import scipy.signal.windows as SciPy`
                Make.Import(dotModule = 'scipy.signal.windows', asName = 'SciPy')
                ```

            References
            ----------
            [1] Lazy imports.
                https://docs.python.org/3.15/reference/simple_stmts.html#lazy-imports
            """
            return ast.Import(names=[Make.alias(dotModule, asName)], **keywordArguments)
    if sys.version_info >= (3, 15):

        @staticmethod
        def ImportFrom(dotModule: str | None, list_alias: list[ast.alias], level: int=0, is_lazy: bool | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.ImportFrom:
            """Make an `ast.ImportFrom` for a `from ... import` statement.

            (AI generated docstring)

            An `ast.ImportFrom` represents one source module and one or more names from it. For a relative
            import, supply the leading dots as `level` (relative import level).

            Parameters
            ----------
            dotModule : str | None
                (package.Module notation) Module name without leading dots. Use `None` for a statement
                such as `from . import sibling`. This is `ast.ImportFrom.module`.
            list_alias : list[ast.alias]
                Imported names and any local aliases from `Make.alias`. Use `[Make.alias('*')]` for a
                wildcard import. This is `ast.ImportFrom.names`.
            level : int = 0
                (relative import level) Number of leading dots. `0` means an absolute import, `1` means
                the current package, and `2` means the parent package.
            is_lazy : bool | None = None
                Use `True` to represent the `lazy` prefix. Omit it or use `False` for a regular `from ...
                import` statement. Explicit lazy imports require module scope and exclude `try` blocks,
                wildcard imports, and future imports [1].
            **keywordArguments : ast_attributes
                Optional source positions. See `Make` for line numbers and byte offsets.

            Returns
            -------
            fromImportStatement : ast.ImportFrom
                `AST` (Abstract Syntax Tree) object representing a selective module import statement.

            See Also
            --------
            `Make.Import`
                Import a module by its absolute name.

            References
            ----------
            [1] Lazy imports.
                https://docs.python.org/3.15/reference/simple_stmts.html#lazy-imports
            """
            return ast.ImportFrom(module=dotModule, names=list_alias, level=level, is_lazy=is_lazy, **keywordArguments)
    else:

        @staticmethod
        def ImportFrom(dotModule: str | None, list_alias: list[ast.alias], level: int=0, **keywordArguments: Unpack[ast_attributes]) -> ast.ImportFrom:
            """Make an `ast.ImportFrom` for a `from ... import` statement.

            (AI generated docstring)

            An `ast.ImportFrom` represents one source module and one or more names from it. For a relative
            import, supply the leading dots as `level` (relative import level).

            Parameters
            ----------
            dotModule : str | None
                (package.Module notation) Module name without leading dots. Use `None` for a statement
                such as `from . import sibling`. This is `ast.ImportFrom.module`.
            list_alias : list[ast.alias]
                Imported names and any local aliases from `Make.alias`. Use `[Make.alias('*')]` for a
                wildcard import. This is `ast.ImportFrom.names`.
            level : int = 0
                (relative import level) Number of leading dots. `0` means an absolute import, `1` means
                the current package, and `2` means the parent package.
            is_lazy : bool | None = None
                Use `True` to represent the `lazy` prefix. Omit it or use `False` for a regular `from ...
                import` statement. Explicit lazy imports require module scope and exclude `try` blocks,
                wildcard imports, and future imports [1].
            **keywordArguments : ast_attributes
                Optional source positions. See `Make` for line numbers and byte offsets.

            Returns
            -------
            fromImportStatement : ast.ImportFrom
                `AST` (Abstract Syntax Tree) object representing a selective module import statement.

            See Also
            --------
            `Make.Import`
                Import a module by its absolute name.

            References
            ----------
            [1] Lazy imports.
                https://docs.python.org/3.15/reference/simple_stmts.html#lazy-imports
            """
            return ast.ImportFrom(module=dotModule, names=list_alias, level=level, **keywordArguments)

    @staticmethod
    def In() -> ast.In:
        """Make an `ast.In` comparison operator.

        (AI generated docstring)

        Use `ast.In` in the `ops` (***op***erator***s***) of `Make.Compare` to represent `in`. Python
        tests the left operand for membership in the right operand.

        Returns
        -------
        membershipOperator : ast.In
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.In()

    @staticmethod
    def Interactive(body: Sequence[ast.stmt]) -> ast.Interactive:
        """Make an `ast.Interactive` (Interactive mode) for compilation in `single` mode.

        (AI generated docstring)

        An `ast.Interactive` (Interactive mode) is the outermost object returned by `ast.parse(...,
        mode='single')`. Interactive execution displays the result of an expression statement when the
        result is other than `None`.

        Parameters
        ----------
        body : Sequence[ast.stmt]
            Statements to execute in interactive mode (`ast.stmt`, ***st***ate***m***en***t***).

        Returns
        -------
        interactive : ast.Interactive
            The statements and their `single`-mode container.
        """
        return ast.Interactive(body=list(body))

    @staticmethod
    def Interpolation(value: ast.expr, string: builtins.str, conversion: int, format_spec: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Interpolation:
        """Make an `ast.Interpolation` for a replacement field in a t-string.

        (AI generated docstring)

        Use `Make.TemplateStr` (Template ***Str***ing) to combine replacement fields with literal
        text. Each field records its expression, original source text, conversion, and format
        specification.

        Parameters
        ----------
        value : ast.expr
            Expression inside the braces (`ast.expr`, ***expr***ession).
        string : str | None
            Original source text of the expression, stored in `ast.Interpolation.str` (***str***ing).
            `None` asks `ast.unparse()` to regenerate the text from `value` [1]. The factory accepts
            `None` at runtime while its annotation lists `str`.
        conversion : int
            Use `-1` for no explicit conversion, or `ord('s')`, `ord('r')`, or `ord('a')` for `!s`,
            `!r`, or `!a`.
        format_spec : ast.expr | None = None
            (format ***spec***ification) Format specification following `:` as an `ast.JoinedStr`
            (Joined ***Str***ing). Omit it when the field has no format specification.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        interpolation : ast.Interpolation
            `AST` (Abstract Syntax Tree) object representing an interpolation component of a template
            string.

        References
        ----------
        [1] `ast.Interpolation`.
            https://docs.python.org/3.15/library/ast.html#ast.Interpolation
        """
        return ast.Interpolation(value=value, str=string, conversion=conversion, format_spec=format_spec, **keywordArguments)

    @staticmethod
    def Invert() -> ast.Invert:
        """Make an `ast.Invert` operator for `~value`.

        (AI generated docstring)

        Use `ast.Invert` as `op` (***op***erator) in `Make.UnaryOp` (***Un***ary ***Op***eration). For
        an integer `x`, `~x` evaluates to `-(x + 1)`.

        Returns
        -------
        bitwiseComplementOperator : ast.Invert
            `AST` (Abstract Syntax Tree) object representing the '`~`' bitwise complement operator for
            use in `ast.UnaryOp` (***Un***ary ***Op***eration).
        """
        return ast.Invert()

    @staticmethod
    def Is() -> ast.Is:
        """'Is', meaning 'Is identical to', is the `object` representation of Python keyword '`is`'.

        `ast.Is` is a subclass of `ast.cmpop` (***c***o***mp***arison ***op***erator). Use it in the
        `ops` (***op***erator***s***) of `Make.Compare` to represent `is`. Both operands must refer to
        the same object for the comparison to be true.

        What's the difference between equality and identity? The work of Jane Austen 'is Equal to' the
        work of Franz Kafka. The work of Mark Twain 'is Equal to' the work of Samuel Clemens. And Mark
        Twain 'Is identical to' Samuel Clemens because they are the same person.

        Returns
        -------
        identityOperator : ast.Is
            The `is` operator for use in `ast.Compare`.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Equivalent to valueAttributes is None.
            Make.Compare(
                left=Make.Name('valueAttributes'), ops=[Make.Is()], comparators=[Make.Constant(None)]
            )
            ```
        """
        return ast.Is()

    @staticmethod
    def IsNot() -> ast.IsNot:
        """Make an `ast.IsNot` operator for `is not`.

        (AI generated docstring)

        Use `ast.IsNot` in the `ops` (***op***erator***s***) of `Make.Compare` to represent `is not`.
        Python evaluates `a is not b` as true when the operands refer to different objects. For
        example, `chicken is not None` checks whether `chicken` refers to an object other than the
        `None` singleton.

        Returns
        -------
        identityNegationOperator : ast.IsNot
            The identity comparison operator for use in `ast.Compare`.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Equivalent to chicken is not None.
            Make.Compare(
                left=Make.Name('chicken'), ops=[Make.IsNot()], comparators=[Make.Constant(None)]
            )
            ```
        """
        return ast.IsNot()

    @staticmethod
    def JoinedStr(values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.JoinedStr:
        """Make an `ast.JoinedStr` (Joined ***Str***ing) for an f-string.

        (AI generated docstring)

        An `ast.JoinedStr` (Joined ***Str***ing) combines literal text and formatted values in source
        order. You can also use it for the format specification of a replacement field.

        Parameters
        ----------
        values : Sequence[ast.expr]
            Use an `ast.Constant` containing a string for each literal part and an
            `ast.FormattedValue` for each replacement field (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        joinedString : ast.JoinedStr
            `AST` (Abstract Syntax Tree) object representing an f-string literal with interpolated
            values.
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
        """Make an `ast.keyword` for a keyword argument or `**` unpacking.

        (AI generated docstring)

        Use an `ast.keyword` in a call or class definition to represent forms such as
        `temperature=350` or `**settings`.

        Parameters
        ----------
        Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo : str | None
            Keyword name, stored in `ast.keyword.arg` (***arg***ument). Pass `None` explicitly for
            `**mapping`.
        value : ast.expr
            Argument value expression. For `**mapping`, this is the expression that provides the
            mapping (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        keywordArgument : ast.keyword
            `AST` (Abstract Syntax Tree) object representing a named argument in function calls.

        Examples
        --------
        Creates AST equivalent to temperature=350.
            ```python
            from astToolkit import Make

            namedArgument = Make.keyword('temperature', Make.Constant(350))
            ```

        Creates AST equivalent to **settings (keyword arguments unpacking).
            ```python
            from astToolkit import Make

            unpackedArguments = Make.keyword(None, Make.Name('settings'))
            ```
        """
        return ast.keyword(arg=Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo, value=value, **keywordArguments)

    @staticmethod
    def Lambda(argumentSpecification: ast.arguments, body: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.Lambda:
        """Make an `ast.Lambda` (Lambda function) for a `lambda` expression.

        (AI generated docstring)

        A `lambda` creates a function whose result is the value of its body expression.

        Parameters
        ----------
        argumentSpecification : ast.arguments
            Parameter specification from `Make.arguments`. This is `ast.Lambda.args` (`Lambda` Lambda
            function, `args` ***arg***ument***s***).
        body : ast.expr
            Expression evaluated on each call (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        lambdaFunction : ast.Lambda
            `AST` (Abstract Syntax Tree) object representing an anonymous lambda function expression.
        """
        return ast.Lambda(args=argumentSpecification, body=body, **keywordArguments)

    @staticmethod
    def List(listElements: Sequence[ast.expr] | None=None, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.List:
        """Make an `ast.List` for a list display or unpacking target.

        (AI generated docstring)

        An `ast.List` represents bracketed forms such as `[a, b]`. The context indicates how Python
        uses the expression.

        Parameters
        ----------
        listElements : Sequence[ast.expr] = []
            Element expressions in order. This is `ast.List.elts` (***e***lemen***t***s) (`ast.expr`,
            ***expr***ession).
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` to build a list, `Make.Store()` for an assignment target, or
            `Make.Del()` (***Del***ete) for a deletion target. This is `ast.List.ctx`
            (***c***on***t***e***x***t) (`ast.expr_context`, ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        listLiteral : ast.List
            `AST` (Abstract Syntax Tree) object representing a list literal with specified elements.
        """
        return ast.List(elts=list(listElements) if listElements else [], ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def ListComp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.ListComp:
        """Make an `ast.ListComp` (List ***c***o***mp***rehension) for a list comprehension.

        (AI generated docstring)

        An `ast.ListComp` (List ***c***o***mp***rehension) represents a list comprehension such as
        `[item.name for item in items]`.

        Parameters
        ----------
        element : ast.expr
            Expression that supplies each element. Use `Make.Starred` for unpacking, as in `[*items
            for items in groups]`. This is `ast.ListComp.elt` (`ListComp` List
            ***c***o***mp***rehension, `elt` ***e***lemen***t***) (`ast.expr`, ***expr***ession).
        generators : list[ast.comprehension]
            `for` clauses and filters in source order.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        listComprehension : ast.ListComp
            `AST` (Abstract Syntax Tree) object representing a list comprehension expression.
        """
        return ast.ListComp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Load() -> ast.Load:
        """Make an `ast.Load` context for reading a value.

        (AI generated docstring)

        Use `Make.Load()` to represent an expression such as `bicycle.wheel` when it retrieves the
        wheel attribute. Value references made by `Make.Name` and `Make.Attribute` use this context by
        default.

        Returns
        -------
        loadContext : ast.Load
            `AST` (Abstract Syntax Tree) context object indicating value retrieval operations.
        """
        return ast.Load()

    class LShift(ast.LShift):
        """Make an `ast.LShift` (***L***eft Shift) operator for `<<`.

        This subclass of `ast.LShift` (***L***eft Shift) adds `join()`, which combines expressions
        into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Lt() -> ast.Lt:
        """Make an `ast.Lt` (is ***L***ess ***t***han) comparison operator.

        (AI generated docstring)

        Use `ast.Lt` (is ***L***ess ***t***han) in the `ops` (***op***erator***s***) of `Make.Compare`
        to represent `<`.

        Returns
        -------
        lessThanOperator : ast.Lt
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.Lt()

    @staticmethod
    def LtE() -> ast.LtE:
        """Make an `ast.LtE` (is ***L***ess ***t***han or ***E***qual to) comparison operator.

        (AI generated docstring)

        Use `ast.LtE` (is ***L***ess ***t***han or ***E***qual to) in the `ops`
        (***op***erator***s***) of `Make.Compare` to represent `<=`.

        Returns
        -------
        lessThanOrEqualOperator : ast.LtE
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.LtE()

    @staticmethod
    def Match(subject: ast.expr, cases: list[ast.match_case] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Match:
        """Make an `ast.Match` (Match this) for a `match` statement.

        (AI generated docstring)

        An `ast.Match` (Match this) evaluates the subject once and tries the cases in source order.
        The first case whose pattern matches and whose guard succeeds supplies the body to execute.

        Parameters
        ----------
        subject : ast.expr
            Expression that supplies the value to match (`ast.expr`, ***expr***ession).
        cases : list[ast.match_case] = []
            Case clauses in source order. Supply at least one `Make.match_case` (match case) for a
            complete statement.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        matchStatement : ast.Match
            `AST` (Abstract Syntax Tree) object representing a complete pattern matching statement.
        """
        return ast.Match(subject=subject, cases=cases or [], **keywordArguments)

    @staticmethod
    def match_case(pattern: ast.pattern, guard: ast.expr | None=None, body: Sequence[ast.stmt] | None=None) -> ast.match_case:
        """Make an `ast.match_case` (match case) for one `case` clause.

        (AI generated docstring)

        A case selects a body when its pattern matches and its optional guard is truthy.

        Parameters
        ----------
        pattern : ast.pattern
            Pattern applied to the subject of the enclosing `match`.
        guard : ast.expr | None = None
            Condition evaluated after the pattern matches and its names are bound (`ast.expr`,
            ***expr***ession).
        body : Sequence[ast.stmt] = []
            Statements executed when the case is selected (`ast.stmt`, ***st***ate***m***en***t***).

        Returns
        -------
        matchCase : ast.match_case
            `AST` (Abstract Syntax Tree) object representing a single case clause in match statements.
        """
        return ast.match_case(pattern=pattern, guard=guard, body=list(body) if body else [])

    @staticmethod
    def MatchAs(pattern: ast.pattern | None=None, name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchAs:
        """Make an `ast.MatchAs` (Match As) for an `as` pattern or a capture.

        (AI generated docstring)

        An `ast.MatchAs` (Match As) can represent `Point(x, y) as location`, a capture such as
        `location`, or the wildcard `_`.

        Parameters
        ----------
        pattern : ast.pattern | None = None
            Pattern to match before binding `name`. Supply `name` with any explicit `pattern`.
        name : str | None = None
            Identifier to bind to the matched subject. When both fields are `None`, the result
            represents `_`.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchAs : ast.MatchAs
            An `ast.MatchAs` (Match As) object with the specified pattern and name.
        """
        return ast.MatchAs(pattern=pattern, name=name, **keywordArguments)

    @staticmethod
    def MatchClass(cls: ast.expr, patterns: Sequence[ast.pattern] | None=None, kwd_attrs: list[str] | None=None, kwd_patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchClass: # pyright: ignore[reportSelfClsParameterName]
        """Make an `ast.MatchClass` (Match Class) for a class pattern.

        (AI generated docstring)

        An `ast.MatchClass` (Match Class) represents a pattern such as `Point(x, y=0)`. Python checks
        the subject with `isinstance()` and matches attribute values against the supplied subpatterns.

        Parameters
        ----------
        cls : ast.expr
            (***cl***a***s***s) Expression identifying the class, such as `Point` or `geometry.Point`
            (`ast.expr`, ***expr***ession).
        patterns : Sequence[ast.pattern] = []
            Positional subpatterns. For most classes, `__match_args__` determines the corresponding
            attributes.
        kwd_attrs : list[str] = []
            (***k***ey***w***or***d*** ***attr***ibute***s***) Attribute names from keyword
            subpatterns, in source order.
        kwd_patterns : Sequence[ast.pattern] = []
            (***k***ey***w***or***d*** ***patterns***) Subpatterns paired with `kwd_attrs`, in the
            same order.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchClass : ast.MatchClass
            An `ast.MatchClass` (Match Class) object configured for the specified class and patterns.
        """
        return ast.MatchClass(cls=cls, patterns=list(patterns) if patterns else [], kwd_attrs=kwd_attrs or [], kwd_patterns=list(kwd_patterns) if kwd_patterns else [], **keywordArguments)

    @staticmethod
    def MatchMapping(keys: Sequence[ast.expr] | None=None, patterns: Sequence[ast.pattern] | None=None, rest: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchMapping:
        """Make an `ast.MatchMapping` (Match Mapping) for a mapping pattern.

        (AI generated docstring)

        An `ast.MatchMapping` (Match Mapping) represents a pattern such as `{'name': name, **extra}`.
        A mapping can match when it contains additional keys.

        Parameters
        ----------
        keys : Sequence[ast.expr] = []
            Literal or dotted-name key expressions (`ast.expr`, ***expr***ession).
        patterns : Sequence[ast.pattern] = []
            Patterns for the values associated with `keys`, in the same order.
        rest : str | None = None
            (the rest of the mapping elements) Capture name after `**`. When supplied, it receives a
            dictionary of the remaining items.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchMapping : ast.MatchMapping
            An `ast.MatchMapping` (Match Mapping) object for the specified key-value patterns and
            optional rest capture.
        """
        return ast.MatchMapping(keys=list(keys) if keys else [], patterns=list(patterns) if patterns else [], rest=rest, **keywordArguments)

    @staticmethod
    def MatchOr(patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchOr:
        """Make an `ast.MatchOr` (Match this Or that) for alternative patterns.

        (AI generated docstring)

        An `ast.MatchOr` (Match this Or that) represents alternatives separated by `|`. Python tries
        them from left to right. Every alternative must bind the same names.

        Parameters
        ----------
        patterns : Sequence[ast.pattern] = []
            Two or more alternatives in matching order.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchOr : ast.MatchOr
            An `ast.MatchOr` (Match this Or that) object containing the alternative patterns.
        """
        return ast.MatchOr(patterns=list(patterns) if patterns else [], **keywordArguments)

    @staticmethod
    def MatchSequence(patterns: Sequence[ast.pattern] | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSequence:
        """Make an `ast.MatchSequence` (Match this Sequence) for a sequence pattern.

        (AI generated docstring)

        An `ast.MatchSequence` (Match this Sequence) represents patterns such as `[first, *rest]` or
        `(x, y)`. Sequence patterns exclude strings, bytes, and byte arrays.

        Parameters
        ----------
        patterns : Sequence[ast.pattern] = []
            Element patterns in order. One `ast.MatchStar` (Match Star) can capture a variable-length
            portion of the sequence.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchSequence : ast.MatchSequence
            An `ast.MatchSequence` (Match this Sequence) object for the specified element patterns.
        """
        return ast.MatchSequence(patterns=list(patterns) if patterns else [], **keywordArguments)

    @staticmethod
    def MatchSingleton(value: bool | None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchSingleton: # noqa: FBT001
        """Make an `ast.MatchSingleton` (Match Singleton) for a singleton pattern.

        (AI generated docstring)

        An `ast.MatchSingleton` (Match Singleton) compares the subject by identity with `None`,
        `True`, or `False`.

        Parameters
        ----------
        value : bool | None
            Singleton to match. Use `None`, `True`, or `False`.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchSingleton : ast.MatchSingleton
            An `ast.MatchSingleton` (Match Singleton) object for the specified singleton value.
        """
        return ast.MatchSingleton(value=value, **keywordArguments)

    @staticmethod
    def MatchStar(name: str | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchStar:
        """Make an `ast.MatchStar` (Match Star) for a starred sequence pattern.

        (AI generated docstring)

        An `ast.MatchStar` (Match Star) represents `*rest` or `*_` inside a sequence pattern. It
        matches the elements left after the fixed positions on either side are accounted for.

        Parameters
        ----------
        name : str | None = None
            Capture name for the list of remaining elements. Use `None` for `*_`.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchStar : ast.MatchStar
            An `ast.MatchStar` (Match Star) object with the specified capture name.
        """
        return ast.MatchStar(name=name, **keywordArguments)

    @staticmethod
    def MatchValue(value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.MatchValue:
        """Make an `ast.MatchValue` (Match Value) for a value pattern.

        (AI generated docstring)

        An `ast.MatchValue` (Match Value) compares the subject with a literal or the value of a dotted
        name using `==`. Use `Make.MatchSingleton` (Match Singleton) for `None`, `True`, and `False`.

        Parameters
        ----------
        value : ast.expr
            Literal expression or dotted name such as `Color.RED` (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        matchValue : ast.MatchValue
            An `ast.MatchValue` (Match Value) object for the specified value expression.
        """
        return ast.MatchValue(value=value, **keywordArguments)

    class MatMult(ast.MatMult):
        """Make an `ast.MatMult` (***Mat***rix ***Mult***iplication) operator for `@`.

        This subclass of `ast.MatMult` (***Mat***rix ***Mult***iplication) adds `join()`, which
        combines expressions into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    class Mod(ast.Mod):
        """Make an `ast.Mod` (***Mod***ulo) operator for `%`.

        This subclass of `ast.Mod` (***Mod***ulo) adds `join()`, which combines expressions into
        nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def mod() -> ast.mod:
        """Create an abstract `ast.mod` (***mod***ule) `object`."""
        return ast.mod()

    @staticmethod
    def Module(body: Sequence[ast.stmt], type_ignores: list[ast.TypeIgnore] | None=None) -> ast.Module:
        """Make an `ast.Module` for a sequence of top-level statements.

        (AI generated docstring)

        An `ast.Module` represents source compiled in `exec` mode. You can also store the module's `#
        type: ignore` comments.

        Parameters
        ----------
        body : Sequence[ast.stmt]
            Top-level statements in source order (`ast.stmt`, ***st***ate***m***en***t***).
        type_ignores : list[ast.TypeIgnore] = []
            (type ***ignore*** comments) Line-specific `ast.TypeIgnore` (this Type (`type`) error,
            Ignore it) directives for `# type: ignore` comments.

        Returns
        -------
        moduleDefinition : ast.Module
            `AST` (Abstract Syntax Tree) object representing a complete Python module structure.

        Examples
        --------
        Creates AST equivalent to x = 42.
            ```python
            from astToolkit import Make

            simpleModule = Make.Module([Make.Assign([Make.Name('x', Make.Store())], Make.Constant(42))])
            ```

        Creates AST equivalent to module with function and assignment
            ```python
            from astToolkit import Make

            moduleWithFunction = Make.Module([
                Make.FunctionDef('calculate', body=[Make.Return(Make.Constant(100))]),
                Make.Assign([Make.Name('result', Make.Store())], Make.Call(Make.Name('calculate'), []))
            ])
            ```
        """
        return ast.Module(body=list(body), type_ignores=type_ignores or [])

    class Mult(ast.Mult):
        """Make an `ast.Mult` (***Mult***iplication) operator for `*`.

        This subclass of `ast.Mult` (***Mult***iplication) adds `join()`, which combines expressions
        into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Name(id: str, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Name:
        """Make an `ast.Name` for an identifier in an expression.

        (AI generated docstring)

        An `ast.Name` represents a bare name such as `inventory`. The context indicates a read, an
        assignment target, or a deletion target.

        Parameters
        ----------
        id : str
            (***id***entifier) Identifier string, such as `inventory`. Use `Make.Attribute` for a
            dotted reference.
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` to read, `Make.Store()` to assign, or `Make.Del()` (***Del***ete) to
            delete. This is `ast.Name.ctx` (***c***on***t***e***x***t) (`ast.expr_context`,
            ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        nameReference : ast.Name
            `AST` (Abstract Syntax Tree) object representing an identifier reference with specified
            context.
        """
        return ast.Name(id=id, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def NamedExpr(target: ast.Name, value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.NamedExpr:
        """Make an `ast.NamedExpr` (Named ***Expr***ession) for an assignment expression.

        (AI generated docstring)

        An `ast.NamedExpr` (Named ***Expr***ession) represents a form such as `(inventory := count)`.
        Python assigns the expression's value to the name and returns that same value.

        Parameters
        ----------
        target : ast.Name
            Name in `Make.Store()` context that receives the value.
        value : ast.expr
            Expression evaluated for assignment and returned by the assignment expression (`ast.expr`,
            ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        namedExpression : ast.NamedExpr
            `AST` (Abstract Syntax Tree) object representing an assignment expression with the walrus
            operator.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Creates AST equivalent to: `(inventory := len(warehouse)) > 10`
            inventoryCheck = Make.Compare(
                left=Make.NamedExpr(
                    target=Make.Name('inventory', Make.Store()),
                    value=Make.Call(Make.Name('len'), [Make.Name('warehouse')])
                ),
                ops=[Make.Gt()],
                comparators=[Make.Constant(10)]
            )
            ```
        """
        return ast.NamedExpr(target=target, value=value, **keywordArguments)

    @staticmethod
    def Nonlocal(names: list[str], **keywordArguments: Unpack[ast_attributes]) -> ast.Nonlocal:
        """Make an `ast.Nonlocal` for a `nonlocal` declaration.

        (AI generated docstring)

        Each declared name refers to an existing binding in the nearest enclosing function scope that
        binds it.

        Parameters
        ----------
        names : list[str]
            Identifiers declared nonlocal.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        nonlocalStatement : ast.Nonlocal
            The declaration for the supplied names.
        """
        return ast.Nonlocal(names=names, **keywordArguments)

    @staticmethod
    def Not() -> ast.Not:
        """Make an `ast.Not` operator for `not value`.

        (AI generated docstring)

        Use `ast.Not` as `op` (***op***erator) in `Make.UnaryOp` (***Un***ary ***Op***eration). Python
        evaluates `not value` as true when `value` is falsy.

        Returns
        -------
        logicalNegationOperator : ast.Not
            `AST` (Abstract Syntax Tree) object representing the keyword '`not`' logical negation
            operator for use in `ast.UnaryOp` (***Un***ary ***Op***eration).
        """
        return ast.Not()

    @staticmethod
    def NotEq() -> ast.NotEq:
        """Make an `ast.NotEq` (is Not ***Eq***ual to) comparison operator.

        (AI generated docstring)

        Use `ast.NotEq` (is Not ***Eq***ual to) in the `ops` (***op***erator***s***) of `Make.Compare`
        to represent `!=`.

        Returns
        -------
        inequalityOperator : ast.NotEq
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.NotEq()

    @staticmethod
    def NotIn() -> ast.NotIn:
        """Make an `ast.NotIn` (is Not ***In***cluded in or does Not have membership In) operator.

        (AI generated docstring)

        Use `ast.NotIn` (is Not ***In***cluded in or does Not have membership In) in the `ops`
        (***op***erator***s***) of `Make.Compare` to represent `not in`. Python tests the left operand
        for membership in the right operand.

        Returns
        -------
        negativeMembershipOperator : ast.NotIn
            The operator to put in `ast.Compare.ops` (***op***erator***s***).
        """
        return ast.NotIn()

    @staticmethod
    def operator() -> ast.operator:
        """Make an instance of the base class `ast.operator`.

        (AI generated docstring)

        Use a concrete binary operator such as `Make.Add()` or `Make.BitOr()` (***Bit***wise Or) in
        `Make.BinOp` (***Bin***ary ***Op***eration) or `Make.AugAssign` (***Aug***mented
        ***Assign***ment).

        Returns
        -------
        binaryOperator : ast.operator
            An instance of the common base class for binary operators.
        """
        return ast.operator()

    class Or(ast.Or):
        """Make an `ast.Or` operator for `or`.

        This subclass of `ast.Or` adds `join()`, which combines expressions into one `ast.BoolOp`
        (***Bool***ean ***Op***eration).
        """

        @classmethod
        def join(cls, expressions: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in one `ast.BoolOp` (***Bool***ean ***Op***eration).

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions.

            Parameters
            ----------
            expressions : Sequence[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for the constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                One `ast.BoolOp` (***Bool***ean ***Op***eration) for two or more operands, the
                original operand for a single input, or an empty string literal for an empty input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent Lions and tigers and bears.
                ast.BoolOp(
                    op=ast.And(),
                    values=[Make.Name('Lions'), Make.Name('tigers'), Make.Name('bears')],
                )
                Make.And.join([Make.Name('Lions'), Make.Name('tigers'), Make.Name('bears')])
                ```
            """
            return Make._boolopJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def ParamSpec(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.ParamSpec:
        """Make an `ast.ParamSpec` (***Param***eter ***Spec***ification) type parameter.

        (AI generated docstring)

        An `ast.ParamSpec` (***Param***eter ***Spec***ification) represents a type parameter such as
        `**P` in a generic declaration. It can preserve a callable's positional and keyword parameter
        types.

        Parameters
        ----------
        name : str
            Type parameter name without the `**` prefix.
        default_value : ast.expr | None = None
            Default parameter list expression, such as `[int, str]`, when supplied (`ast.expr`,
            ***expr***ession).
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        parameterSpecification : ast.ParamSpec
            `AST` (Abstract Syntax Tree) object representing a parameter specification type parameter.
        """
        return ast.ParamSpec(name=name, default_value=default_value, **keywordArguments)

    @staticmethod
    def Pass() -> ast.Pass:
        """Make an `ast.Pass` for a `pass` statement.

        (AI generated docstring)

        Use `Make.Pass()` where Python requires a statement and the body needs no action.

        Returns
        -------
        passStatement : ast.Pass
            A `pass` statement.
        """
        return ast.Pass()

    @staticmethod
    def pattern(**keywordArguments: Unpack[ast_attributes_int]) -> ast.pattern:
        """Make an instance of the base class `ast.pattern`.

        (AI generated docstring)

        Use a concrete pattern factory such as `Make.MatchClass` (Match Class) or `Make.MatchValue`
        (Match Value) to build a case pattern.

        Parameters
        ----------
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        pattern : ast.pattern
            A base `ast.pattern` object with the specified attributes.
        """
        return ast.pattern(**keywordArguments)

    class Pow(ast.Pow):
        """Make an `ast.Pow` (***Pow***er) operator for `**`.

        This subclass of `ast.Pow` (***Pow***er) adds `join()`, which combines expressions into nested
        `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Raise(exc: ast.expr | None=None, cause: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Raise:
        """Make an `ast.Raise` for a `raise` statement.

        (AI generated docstring)

        An `ast.Raise` represents `raise`, `raise exc`, or `raise exc from cause`.

        Parameters
        ----------
        exc : ast.expr | None = None
            (***exc***eption) Expression that supplies an exception instance or class. Omit it to
            re-raise the active exception (`ast.expr`, ***expr***ession).
        cause : ast.expr | None = None
            Expression following `from`. Use `Make.Constant(None)` for `from None`, which suppresses
            display of the implicit exception context.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        raiseStatement : ast.Raise
            The `raise` statement with the supplied exception and cause.
        """
        return ast.Raise(exc=exc, cause=cause, **keywordArguments)

    @staticmethod
    def Return(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Return:
        """Make an `ast.Return` for a `return` statement.

        (AI generated docstring)

        A `return` statement exits the enclosing function. In a generator, it ends iteration.

        Parameters
        ----------
        value : ast.expr | None = None
            Expression returned by the function. Omit it for a bare `return`. An asynchronous
            generator requires the bare form (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        returnStatement : ast.Return
            `AST` (Abstract Syntax Tree) object representing a function return with optional value.
        """
        return ast.Return(value=value, **keywordArguments)

    class RShift(ast.RShift):
        """Make an `ast.RShift` (***R***ight Shift) operator for `>>`.

        This subclass of `ast.RShift` (***R***ight Shift) adds `join()`, which combines expressions
        into nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Set(listElements: Sequence[ast.expr] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Set:
        """Make an `ast.Set` for a set display.

        (AI generated docstring)

        An `ast.Set` represents set displays such as `{a, b}` or `{a, *items}`. An empty set
        expression unparses as `{*()}`.

        Parameters
        ----------
        listElements : Sequence[ast.expr] = []
            Element expressions in source order. This is `ast.Set.elts` (***e***lemen***t***s)
            (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        setLiteral : ast.Set
            `AST` (Abstract Syntax Tree) object representing a set literal with specified unique
            elements.
        """
        return ast.Set(elts=list(listElements) if listElements else [], **keywordArguments)

    @staticmethod
    def SetComp(element: ast.expr, generators: list[ast.comprehension], **keywordArguments: Unpack[ast_attributes]) -> ast.SetComp:
        """Make an `ast.SetComp` (Set ***c***o***mp***rehension) for a set comprehension.

        (AI generated docstring)

        An `ast.SetComp` (Set ***c***o***mp***rehension) represents a set comprehension such as
        `{item.name for item in items}`.

        Parameters
        ----------
        element : ast.expr
            Expression that supplies each element. Use `Make.Starred` for unpacking, as in `{*items
            for items in groups}`. This is `ast.SetComp.elt` (`SetComp` Set ***c***o***mp***rehension,
            `elt` ***e***lemen***t***) (`ast.expr`, ***expr***ession).
        generators : list[ast.comprehension]
            `for` clauses and filters in source order.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        setComprehension : ast.SetComp
            `AST` (Abstract Syntax Tree) object representing a set comprehension expression.
        """
        return ast.SetComp(elt=element, generators=generators, **keywordArguments)

    @staticmethod
    def Slice(lower: ast.expr | None=None, upper: ast.expr | None=None, step: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Slice:
        """Make an `ast.Slice` for a slice inside a subscription.

        (AI generated docstring)

        Use an `ast.Slice` as `slice` in `Make.Subscript` to represent forms such as
        `items[start:stop:step]`.

        Parameters
        ----------
        lower : ast.expr | None = None
            (lower bound) Start expression before the first `:`. Omit it for an open start
            (`ast.expr`, ***expr***ession).
        upper : ast.expr | None = None
            (upper bound) Stop expression after the first `:`. For built-in sequences, the stop
            position is exclusive.
        step : ast.expr | None = None
            Stride expression after the second `:`. Built-in sequences use a stride of `1` when
            omitted.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        sliceExpression : ast.Slice
            `AST` (Abstract Syntax Tree) object representing a slice operation for sequence
            subscripting.
        """
        return ast.Slice(lower=lower, upper=upper, step=step, **keywordArguments)

    @staticmethod
    def Starred(value: ast.expr, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Starred:
        """Make an `ast.Starred` for the `*` form of an expression or target.

        (AI generated docstring)

        Use an `ast.Starred` for unpacking in calls and displays or to capture remaining items in an
        assignment target.

        Parameters
        ----------
        value : ast.expr
            Iterable expression to unpack, or target that receives the remaining items (`ast.expr`,
            ***expr***ession).
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` for unpacking an iterable or `Make.Store()` for an assignment target.
            This is `ast.Starred.ctx` (***c***on***t***e***x***t) (`ast.expr_context`,
            ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        starredExpression : ast.Starred
            `AST` (Abstract Syntax Tree) object representing a starred expression for unpacking
            operations.

        Examples
        --------
            ```python
            from astToolkit import Make

            # Call cook(*ingredients).
            cookCall = Make.Call(Make.Name('cook'), [Make.Starred(Make.Name('ingredients'))])

            # Assign first, *remaining = groceries.
            targets = Make.Tuple(
                [Make.Name('first', Make.Store()),
                 Make.Starred(Make.Name('remaining', Make.Store()), Make.Store())],
                Make.Store(),
            )
            unpackGroceries = Make.Assign([targets], Make.Name('groceries'))
            ```
        """
        return ast.Starred(value=value, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def stmt(**keywordArguments: Unpack[ast_attributes]) -> ast.stmt:
        """Make an instance of the base class `ast.stmt` (***st***ate***m***en***t***).

        (AI generated docstring)

        Use a concrete statement factory such as `Make.Assign` or `Make.Return` to represent an
        executable statement.

        Parameters
        ----------
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        statement : ast.stmt
            An instance of the common base class for statements.
        """
        return ast.stmt(**keywordArguments)

    @staticmethod
    def Store() -> ast.Store:
        """Make an `ast.Store` context for an assignment target.

        (AI generated docstring)

        Use `Make.Store()` for targets that receive a value in assignments, loops, comprehensions, or
        an `as` clause of a `with` statement.

        Returns
        -------
        storeContext : ast.Store
            Expression context for an assignment target.
        """
        return ast.Store()

    class Sub(ast.Sub):
        """Make an `ast.Sub` (***Sub***traction) operator for `-`.

        This subclass of `ast.Sub` (***Sub***traction) adds `join()`, which combines expressions into
        nested `ast.BinOp` (***Bin***ary ***Op***eration) operations.
        """

        @classmethod
        def join(cls, expressions: Iterable[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.expr:
            """Join expressions in left-associated `ast.BinOp` (***Bin***ary ***Op***eration) operations.

            Like `str.join()` (***str***ing) but for `AST` (Abstract Syntax Tree) expressions. Joining
            `a`, `b`, and `c` with `Make.Sub.join()` represents `(a - b) - c`.

            Parameters
            ----------
            expressions : Iterable[ast.expr]
                Operands in evaluation order (`ast.expr`, ***expr***ession).
            **keywordArguments : ast_attributes
                Source positions for every constructed expression. A single input keeps its existing
                positions.

            Returns
            -------
            joinedExpression : ast.expr
                Nested `ast.BinOp` (***Bin***ary ***Op***eration) operations for two or more operands,
                the original operand for a single input, or an empty string literal for an empty
                input.

            Examples
            --------
                ```python
                import ast
                from astToolkit import Make

                # Both expressions represent (Crosby | Stills) | Nash.
                ast.BinOp(
                    left=ast.BinOp(left=Make.Name('Crosby'), op=ast.BitOr(), right=Make.Name('Stills')),
                    op=ast.BitOr(),
                    right=Make.Name('Nash'),
                )
                Make.BitOr.join([Make.Name('Crosby'), Make.Name('Stills'), Make.Name('Nash')])
                ```
            """
            return Make._operatorJoinMethod(cls, expressions, **keywordArguments)

    @staticmethod
    def Subscript(value: ast.expr, slice: ast.expr, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Subscript:
        """Make an `ast.Subscript` for a subscription such as `items[key]`.

        (AI generated docstring)

        The expression in brackets can supply a key, index, slice, or tuple of subscription arguments.

        Parameters
        ----------
        value : ast.expr
            Expression for the object being subscripted (`ast.expr`, ***expr***ession).
        slice : ast.expr
            Expression inside brackets. Use `Make.Slice` for colon-separated bounds or `Make.Tuple`
            for comma-separated arguments.
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` to read, `Make.Store()` to assign, or `Make.Del()` (***Del***ete) to
            delete. This is `ast.Subscript.ctx` (***c***on***t***e***x***t) (`ast.expr_context`,
            ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        subscriptExpression : ast.Subscript
            `AST` (Abstract Syntax Tree) object representing a subscription operation with brackets.
        """
        return ast.Subscript(value=value, slice=slice, ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def TemplateStr(values: Sequence[ast.expr], **keywordArguments: Unpack[ast_attributes]) -> ast.TemplateStr:
        """Make an `ast.TemplateStr` (Template ***Str***ing) for a t-string.

        (AI generated docstring)

        A t-string evaluates to a template containing literal text and structured interpolations. You
        can use each interpolation's value and formatting information when processing the template.

        Parameters
        ----------
        values : Sequence[ast.expr]
            Use `ast.Constant` strings for literal text and `ast.Interpolation` objects for
            replacement fields, in source order (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        templateString : ast.TemplateStr
            `AST` (Abstract Syntax Tree) object representing a template string.
        """
        return ast.TemplateStr(values=list(values), **keywordArguments)

    @staticmethod
    def Try(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt] | None=None, finalbody: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Try:
        """Make an `ast.Try` for a `try` statement.

        (AI generated docstring)

        An `ast.Try` can handle exceptions with `except`, run an `else` body after normal completion,
        or run a `finally` body on exit.

        Parameters
        ----------
        body : Sequence[ast.stmt]
            Statements in the `try` block (`ast.stmt`, ***st***ate***m***en***t***).
        handlers : list[ast.ExceptHandler]
            `except` clauses in matching order. Use an empty list for `try ... finally` without
            handlers (`ast.ExceptHandler`, ***Except***ion ***Handler***).
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed if the `try` block reaches its end normally.
            Requires at least one handler. This is `ast.Try.orelse` (or else execute this).
        finalbody : Sequence[ast.stmt] = []
            (final body) `finally` statements executed when control leaves the `try` statement.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        tryStatement : ast.Try
            `AST` (Abstract Syntax Tree) object representing an exception handling statement with
            optional cleanup.
        """
        return ast.Try(body=list(body), handlers=handlers, orelse=list(orElse) if orElse else [], finalbody=list(finalbody) if finalbody else [], **keywordArguments)

    @staticmethod
    def TryStar(body: Sequence[ast.stmt], handlers: list[ast.ExceptHandler], orElse: Sequence[ast.stmt] | None=None, finalbody: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.TryStar:
        """Make an `ast.TryStar` (Try executing this, protected by `except*` ("except star")) statement.

        (AI generated docstring)

        An `ast.TryStar` (Try executing this, protected by `except*` ("except star")) represents
        handlers that each receive the subgroup of exceptions matching their type. A single exception
        can also match an `except*` clause as a group of one.

        Parameters
        ----------
        body : Sequence[ast.stmt]
            Statements in the `try` block (`ast.stmt`, ***st***ate***m***en***t***).
        handlers : list[ast.ExceptHandler]
            One or more `except*` clauses in matching order, supplied as `ast.ExceptHandler`
            (***Except***ion ***Handler***) objects with an exception type.
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed if the `try` block reaches its end normally.
            This is `ast.TryStar.orelse` (`TryStar` Try executing this, protected by `except*`
            ("except star"), `orelse` or else execute this).
        finalbody : Sequence[ast.stmt] = []
            (final body) `finally` statements executed when control leaves the `try` statement.
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        tryStarStatement : ast.TryStar
            `AST` (Abstract Syntax Tree) object representing an exception group handling statement
            with optional cleanup.
        """
        return ast.TryStar(body=list(body), handlers=handlers, orelse=list(orElse) if orElse else [], finalbody=list(finalbody) if finalbody else [], **keywordArguments)

    @staticmethod
    def Tuple(listElements: Sequence[ast.expr] | None=None, context: ast.expr_context | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Tuple:
        """Make an `ast.Tuple` for a tuple display or unpacking target.

        (AI generated docstring)

        An `ast.Tuple` represents comma-separated forms such as `(x, y)` or `(x,)`, as well as the
        empty tuple `()`.

        Parameters
        ----------
        listElements : Sequence[ast.expr] = []
            Element expressions in order. This is `ast.Tuple.elts` (***e***lemen***t***s) (`ast.expr`,
            ***expr***ession).
        context : ast.expr_context = Make.Load()
            Use `Make.Load()` to build a tuple, `Make.Store()` for an assignment target, or
            `Make.Del()` (***Del***ete) for a deletion target. This is `ast.Tuple.ctx`
            (***c***on***t***e***x***t) (`ast.expr_context`, ***expr***ession ***context***).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        tupleLiteral : ast.Tuple
            `AST` (Abstract Syntax Tree) object representing a tuple literal with specified elements.
        """
        return ast.Tuple(elts=list(listElements) if listElements else [], ctx=context or ast.Load(), **keywordArguments)

    @staticmethod
    def type_ignore() -> ast.type_ignore:
        """Make an instance of the base class `ast.type_ignore` (this `type` error, you ignore it).

        (AI generated docstring)

        Use `Make.TypeIgnore` (this Type (`type`) error, Ignore it) for a `# type: ignore` comment in
        a module.

        Returns
        -------
        typeIgnore : ast.type_ignore
            An instance of the common base class for type ignore directives.
        """
        return ast.type_ignore()

    @staticmethod
    def type_param(**keywordArguments: Unpack[ast_attributes_int]) -> ast.type_param:
        """Make an instance of the base class `ast.type_param` (type ***param***eter).

        (AI generated docstring)

        Use `Make.TypeVar` (Type ***Var***iable), `Make.ParamSpec` (***Param***eter
        ***Spec***ification), or `Make.TypeVarTuple` (Type ***Var***iable ***Tuple***) for a type
        parameter in a generic declaration.

        Parameters
        ----------
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        typeParameter : ast.type_param
            Abstract `AST` (Abstract Syntax Tree) object representing the base of type parameter
            hierarchy.
        """
        return ast.type_param(**keywordArguments)

    @staticmethod
    def TypeAlias(name: ast.Name, type_params: Sequence[ast.type_param], value: ast.expr, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeAlias:
        """Make an `ast.TypeAlias` (Type Alias) for a `type` statement.

        (AI generated docstring)

        An `ast.TypeAlias` (Type Alias) represents a declaration such as `type Vector[T] = list[T]`.

        Parameters
        ----------
        name : ast.Name
            Name of the alias as an `ast.Name` in `Make.Store()` context.
        type_params : Sequence[ast.type_param]
            (type ***param***eter***s***) Type parameters declared in brackets after the name. Use an
            empty sequence for a non-generic alias (`ast.type_param`, type ***param***eter).
        value : ast.expr
            Expression defining the aliased type (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        typeAliasDefinition : ast.TypeAlias
            `AST` (Abstract Syntax Tree) object representing a complete type alias declaration.
        """
        return ast.TypeAlias(name=name, type_params=list(type_params), value=value, **keywordArguments)

    @staticmethod
    def TypeIgnore(lineno: int, tag: str) -> ast.TypeIgnore:
        """Make an `ast.TypeIgnore` (this Type (`type`) error, Ignore it) directive.

        (AI generated docstring)

        Add an `ast.TypeIgnore` (this Type (`type`) error, Ignore it) to `Make.Module` to record an
        ignore directive at a specific source line.

        Parameters
        ----------
        lineno : int
            (line _**n**umer**o**_ (_Latin_ "number")) One-based source line of the directive.
        tag : str
            Text following `ignore`, such as `'[assignment]'`. Use `''` for an unqualified ignore.

        Returns
        -------
        typeIgnoreDirective : ast.TypeIgnore
            `AST` (Abstract Syntax Tree) object representing a type checker ignore comment.

        Examples
        --------
        Creates AST equivalent to # type: ignore (on line 42).
            ```python
            from astToolkit import Make

            simpleIgnore = Make.TypeIgnore(42, '')
            ```

        Creates AST equivalent to # type: ignore[assignment] (on line 15).
            ```python
            from astToolkit import Make

            taggedIgnore = Make.TypeIgnore(15, '[assignment]')
            ```
        """
        return ast.TypeIgnore(lineno=lineno, tag=tag)

    @staticmethod
    def TypeVar(name: str, bound: ast.expr | None=None, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVar:
        """Make an `ast.TypeVar` (Type ***Var***iable) for a type variable.

        (AI generated docstring)

        An `ast.TypeVar` (Type ***Var***iable) represents a type parameter such as `T`, `T: Base`, or
        `T: (int, str)`.

        Parameters
        ----------
        name : str
            Type variable name.
        bound : ast.expr | None = None
            Upper-bound expression, or an `ast.Tuple` of allowed types for constraints. Omit it for an
            unrestricted type variable (`ast.expr`, ***expr***ession).
        default_value : ast.expr | None = None
            Default type expression following `=`.
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        typeVariable : ast.TypeVar
            `AST` (Abstract Syntax Tree) object representing a type variable with optional
            constraints.
        """
        return ast.TypeVar(name=name, bound=bound, default_value=default_value, **keywordArguments)

    @staticmethod
    def TypeVarTuple(name: str, default_value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes_int]) -> ast.TypeVarTuple:
        """Make an `ast.TypeVarTuple` (Type ***Var***iable ***Tuple***) for a variadic type parameter.

        (AI generated docstring)

        An `ast.TypeVarTuple` (Type ***Var***iable ***Tuple***) represents a type parameter such as
        `*Ts` that accepts a sequence of type arguments.

        Parameters
        ----------
        name : str
            Type parameter name without the `*` prefix.
        default_value : ast.expr | None = None
            Default type sequence expression, such as `*tuple[int, str]` or `()` (`ast.expr`,
            ***expr***ession).
        **keywordArguments : ast_attributes_int
            Optional source positions. Supply integer end positions when setting them. See `Make`.

        Returns
        -------
        typeVariableTuple : ast.TypeVarTuple
            `AST` (Abstract Syntax Tree) object representing a variadic type variable.
        """
        return ast.TypeVarTuple(name=name, default_value=default_value, **keywordArguments)

    @staticmethod
    def UAdd() -> ast.UAdd:
        """Make an `ast.UAdd` (***U***nary ***Add***ition) operator for `+value`.

        (AI generated docstring)

        Use `ast.UAdd` (***U***nary ***Add***ition) as `op` (***op***erator) in `Make.UnaryOp`
        (***Un***ary ***Op***eration). Unary `+` leaves a built-in numeric operand's sign as it was.

        Returns
        -------
        unaryPositiveOperator : ast.UAdd
            `AST` (Abstract Syntax Tree) object representing the '`+`' unary positive operator for use
            in `ast.UnaryOp` (***Un***ary ***Op***eration).
        """
        return ast.UAdd()

    @staticmethod
    def UnaryOp(op: ast.unaryop, operand: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.UnaryOp:
        """Make an `ast.UnaryOp` (***Un***ary ***Op***eration) for an operation on one operand.

        (AI generated docstring)

        An `ast.UnaryOp` (***Un***ary ***Op***eration) represents prefix operations such as `-value`,
        `not value`, and `~value`.

        Parameters
        ----------
        op : ast.unaryop
            (***op***erator) Unary operator, such as `Make.UAdd()` (***U***nary ***Add***ition),
            `Make.USub()` (***U***nary ***Sub***traction), `Make.Not()`, or `Make.Invert()`
            (`ast.unaryop`, ***un***ary ***op***erator).
        operand : ast.expr
            Expression operated on (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        unaryOperation : ast.UnaryOp
            `AST` (Abstract Syntax Tree) object representing a unary operation on a single expression.
        """
        return ast.UnaryOp(op=op, operand=operand, **keywordArguments)

    @staticmethod
    def unaryop() -> ast.unaryop:
        """Make an instance of the base class `ast.unaryop` (***un***ary ***op***erator).

        (AI generated docstring)

        Use `Make.Invert()`, `Make.Not()`, `Make.UAdd()` (***U***nary ***Add***ition), or
        `Make.USub()` (***U***nary ***Sub***traction) as a concrete operator in `Make.UnaryOp`
        (***Un***ary ***Op***eration).

        Returns
        -------
        unaryOperator : ast.unaryop
            Abstract unary operator object that serves as the base class for all Python unary
            operators in `AST` (Abstract Syntax Tree) structures.
        """
        return ast.unaryop()

    @staticmethod
    def USub() -> ast.USub:
        """Make an `ast.USub` (***U***nary ***Sub***traction) operator for `-value`.

        (AI generated docstring)

        Use `ast.USub` (***U***nary ***Sub***traction) as `op` (***op***erator) in `Make.UnaryOp`
        (***Un***ary ***Op***eration) to represent arithmetic negation.

        Returns
        -------
        unaryNegativeOperator : ast.USub
            `AST` (Abstract Syntax Tree) object representing the '`-`' unary negation operator for use
            in `ast.UnaryOp` (***Un***ary ***Op***eration).
        """
        return ast.USub()

    @staticmethod
    def While(test: ast.expr, body: Sequence[ast.stmt], orElse: Sequence[ast.stmt] | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.While:
        """Make an `ast.While` for a `while` loop.

        (AI generated docstring)

        A `while` loop checks the condition before each iteration and runs the body while the
        condition is truthy.

        Parameters
        ----------
        test : ast.expr
            Condition expression evaluated before each iteration (`ast.expr`, ***expr***ession).
        body : Sequence[ast.stmt]
            Statements executed while `test` is truthy (`ast.stmt`, ***st***ate***m***en***t***).
        orElse : Sequence[ast.stmt] = []
            (or Else execute this) Statements executed when the test is falsy. `break` skips them.
            This is `ast.While.orelse` (or else execute this).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        whileLoop : ast.While
            `AST` (Abstract Syntax Tree) object representing a condition-based iteration statement.
        """
        return ast.While(test=test, body=list(body), orelse=list(orElse) if orElse else [], **keywordArguments)

    @staticmethod
    def With(items: list[ast.withitem], body: Sequence[ast.stmt], **keywordArguments: Unpack[ast_attributes_type_comment]) -> ast.With:
        """Make an `ast.With` for a `with` statement.

        (AI generated docstring)

        A `with` statement enters context managers in source order and exits them in reverse order.
        Each item can assign the result of `__enter__` to an `as` target.

        Parameters
        ----------
        items : list[ast.withitem]
            Context manager specifications from `Make.withitem` (with item), in entry order.
        body : Sequence[ast.stmt]
            Statements executed after entering all the context managers (`ast.stmt`,
            ***st***ate***m***en***t***).
        type_comment : str | None = None
            (a `type` annotation in a comment) Type annotation text for the `as` targets, from a `#
            type: ...` comment.
        **keywordArguments : ast_attributes_type_comment
            Optional source positions and `type_comment`. See `Make` for source positions.

        Returns
        -------
        withStatement : ast.With
            `AST` (Abstract Syntax Tree) object representing a context manager statement for resource
            management.
        """
        return ast.With(items=items, body=list(body), **keywordArguments)

    @staticmethod
    def withitem(context_expr: ast.expr, optional_vars: ast.expr | None=None) -> ast.withitem:
        """Make an `ast.withitem` (with item) for one context manager in a `with` statement.

        (AI generated docstring)

        Use an `ast.withitem` (with item) for forms such as `manager` or `manager as resource` in
        `Make.With` or `Make.AsyncWith` (***Async***hronous With statement).

        Parameters
        ----------
        context_expr : ast.expr
            (***context*** ***expr***ession) Expression that supplies the context manager (`ast.expr`,
            ***expr***ession).
        optional_vars : ast.expr | None = None
            (optional ***var***iable***s***) Assignment target after `as`, in `Make.Store()` context.
            Omit it to leave the result of entering the manager unbound.

        Returns
        -------
        contextItem : ast.withitem
            `AST` (Abstract Syntax Tree) object representing a single context manager in with
            statements.
        """
        return ast.withitem(context_expr=context_expr, optional_vars=optional_vars)

    @staticmethod
    def Yield(value: ast.expr | None=None, **keywordArguments: Unpack[ast_attributes]) -> ast.Yield:
        """Make an `ast.Yield` (Yield an element) for a `yield` expression.

        (AI generated docstring)

        A `yield` expression suspends the generator and produces a value. On resumption, the
        expression evaluates to the value sent into the generator, or to `None` when advanced
        normally.

        Parameters
        ----------
        value : ast.expr | None = None
            Expression whose value the generator yields. Omit it for a bare `yield`, which yields
            `None` (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        yieldExpression : ast.Yield
            `AST` (Abstract Syntax Tree) object representing a yield expression for generator
            functions.
        """
        return ast.Yield(value=value, **keywordArguments)

    @staticmethod
    def YieldFrom(value: ast.expr, **keywordArguments: Unpack[ast_attributes]) -> ast.YieldFrom:
        """Make an `ast.YieldFrom` (Yield an element From) for a `yield from` expression.

        (AI generated docstring)

        A `yield from` expression delegates to another iterable. When iteration ends, the expression
        takes the iterator's `StopIteration.value` as its result. Use it in a synchronous generator.

        Parameters
        ----------
        value : ast.expr
            Expression supplying the iterable to delegate to (`ast.expr`, ***expr***ession).
        **keywordArguments : ast_attributes
            Optional source positions. See `Make` for line numbers and byte offsets.

        Returns
        -------
        yieldFromExpression : ast.YieldFrom
            `AST` (Abstract Syntax Tree) object representing a yield from expression for generator
            delegation.
        """
        return ast.YieldFrom(value=value, **keywordArguments)
