import ast
import pytest
from astToolkit import dump, Make


class TestASTHelpers:
    maxDiff = None

    def test_parse(self):
        parsedA = ast.parse("foo(1 + 1)")
        parsedB = compile("foo(1 + 1)", "<unknown>", "exec", ast.PyCF_ONLY_AST)
        assert ast.dump(parsedA) == ast.dump(parsedB)

    def test_parse_in_error(self):
        try:
            1 / 0
        except Exception:
            with pytest.raises(SyntaxError) as excinfo:
                ast.literal_eval(r"'\U'")
            assert excinfo.value.__context__ is not None

    def test_dump(self):
        nodeAst = ast.parse('spam(eggs, "and cheese")')
        assert ast.dump(nodeAst) == (
            "Module(body=[Expr(value=Call(func=Name(id='spam', ctx=Load()), "
            "args=[Name(id='eggs', ctx=Load()), Constant(value='and cheese')]))])"
        )
        assert ast.dump(nodeAst, annotate_fields=False) == (
            "Module([Expr(Call(Name('spam', Load()), [Name('eggs', Load()), "
            "Constant('and cheese')]))])"
        )

        # Test with Make-generated nodes
        makeName = Make.Name("spam", ast.Load())
        makeConstant = Make.Constant("and cheese")
        makeCall = Make.Call(makeName, [Make.Name("eggs", ast.Load()), makeConstant], [])
        makeExpr = Make.Expr(makeCall)
        makeModule = Make.Module([makeExpr], [])

        assert ast.dump(makeModule) == ast.dump(nodeAst)

    def test_dump_indent(self):
        nodeAst = ast.parse('spam(eggs, "and cheese")')
        expected_indent_3 = """\
Module(
   body=[
      Expr(
         value=Call(
            func=Name(id='spam', ctx=Load()),
            args=[
               Name(id='eggs', ctx=Load()),
               Constant(value='and cheese')]))])"""

        assert ast.dump(nodeAst, indent=3) == expected_indent_3

        expected_tab = """\
Module(
\t[
\t\tExpr(
\t\t\tCall(
\t\t\t\tName('spam', Load()),
\t\t\t\t[
\t\t\t\t\tName('eggs', Load()),
\t\t\t\t\tConstant('and cheese')]))])"""

        assert ast.dump(nodeAst, annotate_fields=False, indent="\t") == expected_tab

    def test_dump_incomplete(self):
        # Using Make.Raise with minimal arguments
        makeRaise = Make.Raise()
        assert ast.dump(makeRaise) == "Raise()"

        makeRaise = Make.Raise(lineno=3, col_offset=4)
        assert ast.dump(makeRaise, include_attributes=True) == "Raise(lineno=3, col_offset=4)"

        nameE = Make.Name("e", ast.Load())
        makeRaiseWithExc = Make.Raise(exc=nameE, lineno=3, col_offset=4)
        assert ast.dump(makeRaiseWithExc) == "Raise(exc=Name(id='e', ctx=Load()))"
        assert ast.dump(makeRaiseWithExc, annotate_fields=False) == "Raise(Name('e', Load()))"

    # def test_dump_show_empty(self):
    #     def check_node(nodeInstance, emptyExpected, fullExpected, **kwargs):
    #         assert dump(nodeInstance, show_empty=False, **kwargs) == emptyExpected
    #         assert dump(nodeInstance, show_empty=True, **kwargs) == fullExpected

    #     def check_text(codeText, emptyExpected, fullExpected, **kwargs):
    #         check_node(ast.parse(codeText), emptyExpected, fullExpected, **kwargs)

    #     # Test with Make.arguments
    #     makeArguments = Make.arguments()
    #     check_node(
    #         makeArguments,
    #         "ast.arguments()",
    #         "ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])"
    #     )

    #     # Test Make.Name with empty id
    #     makeName = Make.Name("", ast.Load())
    #     check_node(
    #         makeName,
    #         "ast.Name(id='', ctx=ast.Load())",
    #         "ast.Name(id='', ctx=ast.Load())"
    #     )

    #     # Test with Make.Constant
    #     makeConstantNone = Make.Constant(None)
    #     check_node(
    #         makeConstantNone,
    #         "ast.Constant(value=None)",
    #         "ast.Constant(value=None, kind=None)"
    #     )

    #     makeConstantEmpty = Make.Constant("")
    #     check_node(
    #         makeConstantEmpty,
    #         "ast.Constant(value='')",
    #         "ast.Constant(value='', kind=None)"
    #     )

    #     # Expanded tests from draft - binary operators
    #     check_node(
    #         ast.Add(),
    #         "ast.Add()",
    #         "ast.Add()"
    #     )

    #     check_node(
    #         ast.And(),
    #         "ast.And()",
    #         "ast.And()"
    #     )

    #     # Test alias
    #     check_node(
    #         ast.alias(name='name'),
    #         "ast.alias(name='name')",
    #         "ast.alias(name='name', asname=None)"
    #     )

    #     # Test AnnAssign
    #     check_node(
    #         ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), simple=0),
    #         "ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), simple=0)",
    #         "ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), value=None, simple=0)"
    #     )

    #     # Test arg
    #     check_node(
    #         ast.arg(arg='arg'),
    #         "ast.arg(arg='arg')",
    #         "ast.arg(arg='arg', annotation=None, type_comment=None)"
    #     )

    #     # Test Assert
    #     check_node(
    #         ast.Assert(test=ast.Constant(value=None)),
    #         "ast.Assert(test=ast.Constant(value=None))",
    #         "ast.Assert(test=ast.Constant(value=None, kind=None), msg=None)"
    #     )

    #     # Test Assign
    #     check_node(
    #         ast.Assign(value=ast.Constant(value=None)),
    #         "ast.Assign(value=ast.Constant(value=None))",
    #         "ast.Assign(targets=[], value=ast.Constant(value=None, kind=None), type_comment=None)"
    #     )

    #     # Test AsyncFor
    #     check_node(
    #         ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load())),
    #         "ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()))",
    #         "ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)"
    #     )

    #     # Test AsyncFunctionDef
    #     check_node(
    #         ast.AsyncFunctionDef(name='name', args=ast.arguments()),
    #         "ast.AsyncFunctionDef(name='name', args=ast.arguments())",
    #         "ast.AsyncFunctionDef(name='name', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
    #     )

    #     # Test AsyncWith
    #     check_node(
    #         ast.AsyncWith(),
    #         "ast.AsyncWith()",
    #         "ast.AsyncWith(items=[], body=[], type_comment=None)"
    #     )

    #     # Test Attribute
    #     check_node(
    #         ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load()),
    #         "ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load())",
    #         "ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load())"
    #     )

    #     # Test AugAssign
    #     check_node(
    #         ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None)),
    #         "ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None))",
    #         "ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None, kind=None))"
    #     )

    #     # Test Await
    #     check_node(
    #         ast.Await(value=ast.Constant(value=None)),
    #         "ast.Await(value=ast.Constant(value=None))",
    #         "ast.Await(value=ast.Constant(value=None, kind=None))"
    #     )

    def test_copy_location(self):
        sourceAst = ast.parse("1 + 1", mode="eval")
        sourceAst.body.right = ast.copy_location(ast.Constant(2), sourceAst.body.right)
        expected = (
            "Expression(body=BinOp(left=Constant(value=1, lineno=1, col_offset=0, "
            "end_lineno=1, end_col_offset=1), op=Add(), right=Constant(value=2, "
            "lineno=1, col_offset=4, end_lineno=1, end_col_offset=5), lineno=1, "
            "col_offset=0, end_lineno=1, end_col_offset=5))"
        )
        assert ast.dump(sourceAst, include_attributes=True) == expected

        # Test with Make nodes
        spamName = Make.Name("spam", ast.Load())
        makeCall = Make.Call(col_offset=1, lineno=1, end_lineno=1, end_col_offset=1, callee=spamName)
        newCall = ast.copy_location(makeCall, Make.Call(col_offset=None, lineno=None, callee=spamName))
        assert newCall.end_lineno is None
        assert newCall.end_col_offset is None
        assert newCall.lineno == 1
        assert newCall.col_offset == 1

    def test_fix_missing_locations(self):
        sourceAst = ast.parse('write("spam")')
        spamCall = Make.Call(Make.Name("spam", ast.Load()), [Make.Constant("eggs")], [])
        sourceAst.body.append(Make.Expr(spamCall))

        assert sourceAst == ast.fix_missing_locations(sourceAst)

    def test_increment_lineno(self):
        sourceAst = ast.parse("1 + 1", mode="eval")
        assert ast.increment_lineno(sourceAst, n=3) == sourceAst
        expected = (
            "Expression(body=BinOp(left=Constant(value=1, lineno=4, col_offset=0, "
            "end_lineno=4, end_col_offset=1), op=Add(), right=Constant(value=1, "
            "lineno=4, col_offset=4, end_lineno=4, end_col_offset=5), lineno=4, "
            "col_offset=0, end_lineno=4, end_col_offset=5))"
        )
        assert ast.dump(sourceAst, include_attributes=True) == expected

        # Test with Make nodes
        makeCall = Make.Call(Make.Name("test", ast.Load()), [], [], lineno=1)
        assert ast.increment_lineno(makeCall).lineno == 2
        assert ast.increment_lineno(makeCall).end_lineno is None

    def test_iter_fields(self):
        nodeAst = ast.parse("foo()", mode="eval")
        fieldsDict = dict(ast.iter_fields(nodeAst.body))
        assert fieldsDict.pop("func").id == "foo"
        assert fieldsDict == {"keywords": [], "args": []}

        # Test with Make nodes
        makeCall = Make.Call(Make.Name("bar", ast.Load()), [], [])
        makeFieldsDict = dict(ast.iter_fields(makeCall))
        assert makeFieldsDict.pop("func").id == "bar"
        assert makeFieldsDict == {"keywords": [], "args": []}

    def test_iter_child_nodes(self):
        nodeAst = ast.parse("spam(23, 42, eggs='leek')", mode="eval")
        childNodes = list(ast.iter_child_nodes(nodeAst.body))
        assert len(childNodes) == 4

        iterator = ast.iter_child_nodes(nodeAst.body)
        assert next(iterator).id == "spam"
        assert next(iterator).value == 23
        assert next(iterator).value == 42
        assert ast.dump(next(iterator)) == "keyword(arg='eggs', value=Constant(value='leek'))"

        # Test with Make nodes
        makeCall = Make.Call(
            Make.Name("spam", ast.Load()),
            [Make.Constant(23), Make.Constant(42)],
            [Make.keyword("eggs", Make.Constant("leek"))]
        )
        makeChildNodes = list(ast.iter_child_nodes(makeCall))
        assert len(makeChildNodes) == 4

    def test_get_docstring(self):
        # Test module docstring
        nodeAst = ast.parse('"""line one\n  line two"""')
        assert ast.get_docstring(nodeAst) == "line one\nline two"

        # Test class docstring
        classNode = ast.parse('class foo:\n  """line one\n  line two"""')
        assert ast.get_docstring(classNode.body[0]) == "line one\nline two"

        # Test function docstring
        functionNode = ast.parse('def foo():\n  """line one\n  line two"""')
        assert ast.get_docstring(functionNode.body[0]) == "line one\nline two"

        # Test async function docstring
        asyncNode = ast.parse('async def foo():\n  """spam\n  ham"""')
        assert ast.get_docstring(asyncNode.body[0]) == "spam\nham"
        assert ast.get_docstring(asyncNode.body[0], clean=False) == "spam\n  ham"

        # Test TypeError for invalid node
        invalidNode = ast.parse("x")
        with pytest.raises(TypeError):
            ast.get_docstring(invalidNode.body[0])

    def test_get_docstring_none(self):
        # Test empty module
        assert ast.get_docstring(ast.parse("")) is None

        # Test non-docstring assignment
        nodeAst = ast.parse('x = "not docstring"')
        assert ast.get_docstring(nodeAst) is None

        # Test function without docstring
        functionNode = ast.parse("def foo():\n  pass")
        assert ast.get_docstring(functionNode) is None

        # Test class without docstring
        classNode = ast.parse("class foo:\n  pass")
        assert ast.get_docstring(classNode.body[0]) is None

        classWithAssign = ast.parse('class foo:\n  x = "not docstring"')
        assert ast.get_docstring(classWithAssign.body[0]) is None

        classWithMethod = ast.parse("class foo:\n  def bar(self): pass")
        assert ast.get_docstring(classWithMethod.body[0]) is None

    def test_literal_eval(self):
        # Test basic literal evaluation
        assert ast.literal_eval("[1, 2, 3]") == [1, 2, 3]
        assert ast.literal_eval('{"foo": 42}') == {"foo": 42}
        assert ast.literal_eval("(True, False, None)") == (True, False, None)
        assert ast.literal_eval("{1, 2, 3}") == {1, 2, 3}
        assert ast.literal_eval('b"hi"') == b"hi"
        assert ast.literal_eval("set()") == set()

        # Test invalid literal
        with pytest.raises(ValueError):
            ast.literal_eval("foo()")

        # Test numeric literals
        assert ast.literal_eval("6") == 6
        assert ast.literal_eval("+6") == 6
        assert ast.literal_eval("-6") == -6
        assert ast.literal_eval("3.25") == 3.25
        assert ast.literal_eval("+3.25") == 3.25
        assert ast.literal_eval("-3.25") == -3.25

    def test_make_integration_with_ast_helpers(self):
        # Test that Make nodes work seamlessly with ast helper functions

        # Create nodes using Make
        nameNode = Make.Name("x", ast.Load())
        constantNode = Make.Constant(42)
        binOpNode = Make.BinOp(nameNode, ast.Add(), constantNode)

        # Test ast.dump works with Make nodes
        dumpResult = ast.dump(binOpNode)
        assert "BinOp" in dumpResult
        assert "Name(id='x'" in dumpResult
        assert "Constant(value=42)" in dumpResult

        # Test ast.iter_fields works with Make nodes
        fieldsDict = dict(ast.iter_fields(binOpNode))
        assert "left" in fieldsDict
        assert "op" in fieldsDict
        assert "right" in fieldsDict

        # Test ast.iter_child_nodes works with Make nodes
        childNodes = list(ast.iter_child_nodes(binOpNode))
        assert len(childNodes) == 3  # left, op, right

        # Test ast.copy_location works with Make nodes
        sourceNode = ast.parse("x + 1").body[0].value
        copiedNode = ast.copy_location(binOpNode, sourceNode)
        assert hasattr(copiedNode, 'lineno')
        assert hasattr(copiedNode, 'col_offset')
