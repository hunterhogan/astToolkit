from astToolkit import dump, Make
import ast
import pytest

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

    def test_dump_with_indent(self):
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

    def test_dump_show_empty(self):
        def check_node(nodeInstance, emptyExpected, fullExpected, **kwargs):
            assert dump(nodeInstance, show_empty=False, **kwargs) == emptyExpected
            assert dump(nodeInstance, show_empty=True, **kwargs) == fullExpected

        def check_text(codeText, emptyExpected, fullExpected, **kwargs):
            check_node(ast.parse(codeText), emptyExpected, fullExpected, **kwargs)

        check_node(
            ast.Add(),
            emptyExpected="ast.Add()",
            fullExpected="ast.Add()"
        )

        check_node(
            ast.alias(name='name'),
            emptyExpected="ast.alias(name='name')",
            fullExpected="ast.alias(name='name', asname=None)"
        )

        check_node(
            ast.And(),
            emptyExpected="ast.And()",
            fullExpected="ast.And()"
        )

        check_node(
            ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), simple=0),
            emptyExpected="ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), simple=0)",
            fullExpected="ast.AnnAssign(target=ast.Name(id='target', ctx=ast.Load()), annotation=ast.Name(id='annotation', ctx=ast.Load()), value=None, simple=0)"
        )

        check_node(
            ast.arg(arg='arg'),
            emptyExpected="ast.arg(arg='arg')",
            fullExpected="ast.arg(arg='arg', annotation=None, type_comment=None)"
        )

        check_node(
            ast.arguments(),
            emptyExpected="ast.arguments()",
            fullExpected="ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])"
        )

        check_node(
            ast.Assert(test=ast.Constant(value=None)),
            emptyExpected="ast.Assert(test=ast.Constant(value=None))",
            fullExpected="ast.Assert(test=ast.Constant(value=None, kind=None), msg=None)"
        )

        check_node(
            ast.Assign(value=ast.Constant(value=None)),
            emptyExpected="ast.Assign(value=ast.Constant(value=None))",
            fullExpected="ast.Assign(targets=[], value=ast.Constant(value=None, kind=None), type_comment=None)"
        )

        check_node(
            ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load())),
            emptyExpected="ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()))",
            fullExpected="ast.AsyncFor(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)"
        )

        check_node(
            ast.AsyncFunctionDef(name='name', args=ast.arguments()),
            emptyExpected="ast.AsyncFunctionDef(name='name', args=ast.arguments())",
            fullExpected="ast.AsyncFunctionDef(name='name', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
        )

        check_node(
            ast.AsyncWith(),
            emptyExpected="ast.AsyncWith()",
            fullExpected="ast.AsyncWith(items=[], body=[], type_comment=None)"
        )

        check_node(
            ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load()),
            emptyExpected="ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load())",
            fullExpected="ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='attr', ctx=ast.Load())"
        )

        check_node(
            ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None)),
            emptyExpected="ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None))",
            fullExpected="ast.AugAssign(target=ast.Name(id='target', ctx=ast.Load()), op=ast.Add(), value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.Await(value=ast.Constant(value=None)),
            emptyExpected="ast.Await(value=ast.Constant(value=None))",
            fullExpected="ast.Await(value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.BinOp(left=ast.Constant(value=None), op=ast.Add(), right=ast.Constant(value=None)),
            emptyExpected="ast.BinOp(left=ast.Constant(value=None), op=ast.Add(), right=ast.Constant(value=None))",
            fullExpected="ast.BinOp(left=ast.Constant(value=None, kind=None), op=ast.Add(), right=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.BitAnd(),
            emptyExpected="ast.BitAnd()",
            fullExpected="ast.BitAnd()"
        )

        check_node(
            ast.BitOr(),
            emptyExpected="ast.BitOr()",
            fullExpected="ast.BitOr()"
        )

        check_node(
            ast.BitXor(),
            emptyExpected="ast.BitXor()",
            fullExpected="ast.BitXor()"
        )

        check_node(
            ast.boolop(),
            emptyExpected="ast.boolop()",
            fullExpected="ast.boolop()"
        )

        check_node(
            ast.BoolOp(op=ast.And()),
            emptyExpected="ast.BoolOp(op=ast.And())",
            fullExpected="ast.BoolOp(op=ast.And(), values=[])"
        )

        check_node(
            ast.Break(),
            emptyExpected="ast.Break()",
            fullExpected="ast.Break()"
        )

        check_node(
            ast.Call(func=ast.Name(id='func', ctx=ast.Load())),
            emptyExpected="ast.Call(func=ast.Name(id='func', ctx=ast.Load()))",
            fullExpected="ast.Call(func=ast.Name(id='func', ctx=ast.Load()), args=[], keywords=[])"
        )

        check_node(
            ast.ClassDef(name='name'),
            emptyExpected="ast.ClassDef(name='name')",
            fullExpected="ast.ClassDef(name='name', bases=[], keywords=[], body=[], decorator_list=[], type_params=[])"
        )

        check_node(
            ast.cmpop(),
            emptyExpected="ast.cmpop()",
            fullExpected="ast.cmpop()"
        )

        check_node(
            ast.Compare(left=ast.Constant(value=None)),
            emptyExpected="ast.Compare(left=ast.Constant(value=None))",
            fullExpected="ast.Compare(left=ast.Constant(value=None, kind=None), ops=[], comparators=[])"
        )

        check_node(
            ast.comprehension(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), is_async=0),
            emptyExpected="ast.comprehension(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), is_async=0)",
            fullExpected="ast.comprehension(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), ifs=[], is_async=0)"
        )

        check_node(
            ast.Constant(value=None),
            emptyExpected="ast.Constant(value=None)",
            fullExpected="ast.Constant(value=None, kind=None)"
        )

        check_node(
            ast.Continue(),
            emptyExpected="ast.Continue()",
            fullExpected="ast.Continue()"
        )

        check_node(
            ast.Del(),
            emptyExpected="ast.Del()",
            fullExpected="ast.Del()"
        )

        check_node(
            ast.Delete(),
            emptyExpected="ast.Delete()",
            fullExpected="ast.Delete(targets=[])"
        )

        check_node(
            ast.Dict(),
            emptyExpected="ast.Dict()",
            fullExpected="ast.Dict(keys=[], values=[])"
        )

        check_node(
            ast.DictComp(key=ast.Constant(value=None), value=ast.Constant(value=None)),
            emptyExpected="ast.DictComp(key=ast.Constant(value=None), value=ast.Constant(value=None))",
            fullExpected="ast.DictComp(key=ast.Constant(value=None, kind=None), value=ast.Constant(value=None, kind=None), generators=[])"
        )

        check_node(
            ast.Div(),
            emptyExpected="ast.Div()",
            fullExpected="ast.Div()"
        )

        check_node(
            ast.Eq(),
            emptyExpected="ast.Eq()",
            fullExpected="ast.Eq()"
        )

        check_node(
            ast.excepthandler(),
            emptyExpected="ast.excepthandler()",
            fullExpected="ast.excepthandler()"
        )

        check_node(
            ast.ExceptHandler(),
            emptyExpected="ast.ExceptHandler()",
            fullExpected="ast.ExceptHandler(type=None, name=None, body=[])"
        )

        check_node(
            ast.expr_context(),
            emptyExpected="ast.expr_context()",
            fullExpected="ast.expr_context()"
        )

        check_node(
            ast.expr(),
            emptyExpected="ast.expr()",
            fullExpected="ast.expr()"
        )

        check_node(
            ast.Expr(value=ast.Constant(value=None)),
            emptyExpected="ast.Expr(value=ast.Constant(value=None))",
            fullExpected="ast.Expr(value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.Expression(body=ast.Constant(value=None)),
            emptyExpected="ast.Expression(body=ast.Constant(value=None))",
            fullExpected="ast.Expression(body=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.FloorDiv(),
            emptyExpected="ast.FloorDiv()",
            fullExpected="ast.FloorDiv()"
        )

        check_node(
            ast.For(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load())),
            emptyExpected="ast.For(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()))",
            fullExpected="ast.For(target=ast.Name(id='target', ctx=ast.Load()), iter=ast.Name(id='iter', ctx=ast.Load()), body=[], orelse=[], type_comment=None)"
        )

        check_node(
            ast.FormattedValue(value=ast.Constant(value=None), conversion=0),
            emptyExpected="ast.FormattedValue(value=ast.Constant(value=None), conversion=0)",
            fullExpected="ast.FormattedValue(value=ast.Constant(value=None, kind=None), conversion=0, format_spec=None)"
        )

        check_node(
            ast.FunctionDef(name='name', args=ast.arguments()),
            emptyExpected="ast.FunctionDef(name='name', args=ast.arguments())",
            fullExpected="ast.FunctionDef(name='name', args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None, type_comment=None, type_params=[])"
        )

        check_node(
            ast.FunctionType(returns=ast.Constant(value=None)),
            emptyExpected="ast.FunctionType(returns=ast.Constant(value=None))",
            fullExpected="ast.FunctionType(argtypes=[], returns=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.GeneratorExp(elt=ast.Constant(value=None)),
            emptyExpected="ast.GeneratorExp(elt=ast.Constant(value=None))",
            fullExpected="ast.GeneratorExp(elt=ast.Constant(value=None, kind=None), generators=[])"
        )

        check_node(
            ast.Global(),
            emptyExpected="ast.Global()",
            fullExpected="ast.Global(names=[])"
        )

        check_node(
            ast.Gt(),
            emptyExpected="ast.Gt()",
            fullExpected="ast.Gt()"
        )

        check_node(
            ast.GtE(),
            emptyExpected="ast.GtE()",
            fullExpected="ast.GtE()"
        )

        check_node(
            ast.If(test=ast.Constant(value=None)),
            emptyExpected="ast.If(test=ast.Constant(value=None))",
            fullExpected="ast.If(test=ast.Constant(value=None, kind=None), body=[], orelse=[])"
        )

        check_node(
            ast.IfExp(test=ast.Constant(value=None), body=ast.Constant(value=None), orelse=ast.Constant(value=None)),
            emptyExpected="ast.IfExp(test=ast.Constant(value=None), body=ast.Constant(value=None), orelse=ast.Constant(value=None))",
            fullExpected="ast.IfExp(test=ast.Constant(value=None, kind=None), body=ast.Constant(value=None, kind=None), orelse=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.Import(),
            emptyExpected="ast.Import()",
            fullExpected="ast.Import(names=[])"
        )

        check_node(
            ast.ImportFrom(level=0),
            emptyExpected="ast.ImportFrom(level=0)",
            fullExpected="ast.ImportFrom(module=None, names=[], level=0)"
        )

        check_node(
            ast.In(),
            emptyExpected="ast.In()",
            fullExpected="ast.In()"
        )

        check_node(
            ast.Interactive(),
            emptyExpected="ast.Interactive()",
            fullExpected="ast.Interactive(body=[])"
        )

        check_node(
            ast.Invert(),
            emptyExpected="ast.Invert()",
            fullExpected="ast.Invert()"
        )

        check_node(
            ast.Is(),
            emptyExpected="ast.Is()",
            fullExpected="ast.Is()"
        )

        check_node(
            ast.IsNot(),
            emptyExpected="ast.IsNot()",
            fullExpected="ast.IsNot()"
        )

        check_node(
            ast.JoinedStr(),
            emptyExpected="ast.JoinedStr()",
            fullExpected="ast.JoinedStr(values=[])"
        )

        check_node(
            ast.keyword(value=ast.Constant(value=None)),
            emptyExpected="ast.keyword(value=ast.Constant(value=None))",
            fullExpected="ast.keyword(arg=None, value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.Lambda(args=ast.arguments(), body=ast.Constant(value=None)),
            emptyExpected="ast.Lambda(args=ast.arguments(), body=ast.Constant(value=None))",
            fullExpected="ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.List(ctx=ast.Load()),
            emptyExpected="ast.List(ctx=ast.Load())",
            fullExpected="ast.List(elts=[], ctx=ast.Load())"
        )

        check_node(
            ast.ListComp(elt=ast.Constant(value=None)),
            emptyExpected="ast.ListComp(elt=ast.Constant(value=None))",
            fullExpected="ast.ListComp(elt=ast.Constant(value=None, kind=None), generators=[])"
        )

        check_node(
            ast.Load(),
            emptyExpected="ast.Load()",
            fullExpected="ast.Load()"
        )

        check_node(
            ast.LShift(),
            emptyExpected="ast.LShift()",
            fullExpected="ast.LShift()"
        )

        check_node(
            ast.Lt(),
            emptyExpected="ast.Lt()",
            fullExpected="ast.Lt()"
        )

        check_node(
            ast.LtE(),
            emptyExpected="ast.LtE()",
            fullExpected="ast.LtE()"
        )

        check_node(
            ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=None))),
            emptyExpected="ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=None)))",
            fullExpected="ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=None, kind=None)), guard=None, body=[])"
        )

        check_node(
            ast.Match(subject=ast.Constant(value=None)),
            emptyExpected="ast.Match(subject=ast.Constant(value=None))",
            fullExpected="ast.Match(subject=ast.Constant(value=None, kind=None), cases=[])"
        )

        check_node(
            ast.MatchAs(),
            emptyExpected="ast.MatchAs()",
            fullExpected="ast.MatchAs(pattern=None, name=None)"
        )

        check_node(
            ast.MatchClass(cls=ast.Name(id='cls', ctx=ast.Load())),
            emptyExpected="ast.MatchClass(cls=ast.Name(id='cls', ctx=ast.Load()))",
            fullExpected="ast.MatchClass(cls=ast.Name(id='cls', ctx=ast.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[])"
        )

        check_node(
            ast.MatchMapping(),
            emptyExpected="ast.MatchMapping()",
            fullExpected="ast.MatchMapping(keys=[], patterns=[], rest=None)"
        )

        check_node(
            ast.MatchOr(),
            emptyExpected="ast.MatchOr()",
            fullExpected="ast.MatchOr(patterns=[])"
        )

        check_node(
            ast.MatchSequence(),
            emptyExpected="ast.MatchSequence()",
            fullExpected="ast.MatchSequence(patterns=[])"
        )

        check_node(
            ast.MatchSingleton(value=None),
            emptyExpected="ast.MatchSingleton(value=None)",
            fullExpected="ast.MatchSingleton(value=None)"
        )

        check_node(
            ast.MatchStar(),
            emptyExpected="ast.MatchStar()",
            fullExpected="ast.MatchStar(name=None)"
        )

        check_node(
            ast.MatchValue(value=ast.Constant(value=None)),
            emptyExpected="ast.MatchValue(value=ast.Constant(value=None))",
            fullExpected="ast.MatchValue(value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.MatMult(),
            emptyExpected="ast.MatMult()",
            fullExpected="ast.MatMult()"
        )

        check_node(
            ast.Mod(),
            emptyExpected="ast.Mod()",
            fullExpected="ast.Mod()"
        )

        check_node(
            ast.mod(),
            emptyExpected="ast.mod()",
            fullExpected="ast.mod()"
        )

        check_node(
            ast.Module(),
            emptyExpected="ast.Module()",
            fullExpected="ast.Module(body=[], type_ignores=[])"
        )

        check_node(
            ast.Mult(),
            emptyExpected="ast.Mult()",
            fullExpected="ast.Mult()"
        )

        check_node(
            ast.Name(id='id', ctx=ast.Load()),
            emptyExpected="ast.Name(id='id', ctx=ast.Load())",
            fullExpected="ast.Name(id='id', ctx=ast.Load())"
        )

        check_node(
            ast.NamedExpr(target=ast.Name(id='target', ctx=ast.Load()), value=ast.Constant(value=None)),
            emptyExpected="ast.NamedExpr(target=ast.Name(id='target', ctx=ast.Load()), value=ast.Constant(value=None))",
            fullExpected="ast.NamedExpr(target=ast.Name(id='target', ctx=ast.Load()), value=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.Nonlocal(),
            emptyExpected="ast.Nonlocal()",
            fullExpected="ast.Nonlocal(names=[])"
        )

        check_node(
            ast.Not(),
            emptyExpected="ast.Not()",
            fullExpected="ast.Not()"
        )

        check_node(
            ast.NotEq(),
            emptyExpected="ast.NotEq()",
            fullExpected="ast.NotEq()"
        )

        check_node(
            ast.NotIn(),
            emptyExpected="ast.NotIn()",
            fullExpected="ast.NotIn()"
        )

        check_node(
            ast.operator(),
            emptyExpected="ast.operator()",
            fullExpected="ast.operator()"
        )

        check_node(
            ast.Or(),
            emptyExpected="ast.Or()",
            fullExpected="ast.Or()"
        )

        check_node(
            ast.ParamSpec(name='name'),
            emptyExpected="ast.ParamSpec(name='name')",
            fullExpected="ast.ParamSpec(name='name', default_value=None)"
        )

        check_node(
            ast.Pass(),
            emptyExpected="ast.Pass()",
            fullExpected="ast.Pass()"
        )

        check_node(
            ast.pattern(),
            emptyExpected="ast.pattern()",
            fullExpected="ast.pattern()"
        )

        check_node(
            ast.Pow(),
            emptyExpected="ast.Pow()",
            fullExpected="ast.Pow()"
        )

        check_node(
            ast.Raise(),
            emptyExpected="ast.Raise()",
            fullExpected="ast.Raise(exc=None, cause=None)"
        )

        check_node(
            ast.Return(),
            emptyExpected="ast.Return()",
            fullExpected="ast.Return(value=None)"
        )

        check_node(
            ast.RShift(),
            emptyExpected="ast.RShift()",
            fullExpected="ast.RShift()"
        )

        check_node(
            ast.Set(),
            emptyExpected="ast.Set()",
            fullExpected="ast.Set(elts=[])"
        )

        check_node(
            ast.SetComp(elt=ast.Constant(value=None)),
            emptyExpected="ast.SetComp(elt=ast.Constant(value=None))",
            fullExpected="ast.SetComp(elt=ast.Constant(value=None, kind=None), generators=[])"
        )

        check_node(
            ast.Slice(),
            emptyExpected="ast.Slice()",
            fullExpected="ast.Slice(lower=None, upper=None, step=None)"
        )

        check_node(
            ast.Starred(value=ast.Name(id='value', ctx=ast.Load()), ctx=ast.Load()),
            emptyExpected="ast.Starred(value=ast.Name(id='value', ctx=ast.Load()), ctx=ast.Load())",
            fullExpected="ast.Starred(value=ast.Name(id='value', ctx=ast.Load()), ctx=ast.Load())"
        )

        check_node(
            ast.stmt(),
            emptyExpected="ast.stmt()",
            fullExpected="ast.stmt()"
        )

        check_node(
            ast.Store(),
            emptyExpected="ast.Store()",
            fullExpected="ast.Store()"
        )

        check_node(
            ast.Sub(),
            emptyExpected="ast.Sub()",
            fullExpected="ast.Sub()"
        )

        check_node(
            ast.Subscript(value=ast.Name(id='value', ctx=ast.Load()), slice=ast.Constant(value=None), ctx=ast.Load()),
            emptyExpected="ast.Subscript(value=ast.Name(id='value', ctx=ast.Load()), slice=ast.Constant(value=None), ctx=ast.Load())",
            fullExpected="ast.Subscript(value=ast.Name(id='value', ctx=ast.Load()), slice=ast.Constant(value=None, kind=None), ctx=ast.Load())"
        )

        check_node(
            ast.Try(),
            emptyExpected="ast.Try()",
            fullExpected="ast.Try(body=[], handlers=[], orelse=[], finalbody=[])"
        )

        check_node(
            ast.TryStar(),
            emptyExpected="ast.TryStar()",
            fullExpected="ast.TryStar(body=[], handlers=[], orelse=[], finalbody=[])"
        )

        check_node(
            ast.Tuple(ctx=ast.Load()),
            emptyExpected="ast.Tuple(ctx=ast.Load())",
            fullExpected="ast.Tuple(elts=[], ctx=ast.Load())"
        )

        check_node(
            ast.type_ignore(),
            emptyExpected="ast.type_ignore()",
            fullExpected="ast.type_ignore()"
        )

        check_node(
            ast.type_param(),
            emptyExpected="ast.type_param()",
            fullExpected="ast.type_param()"
        )

        check_node(
            ast.TypeAlias(name=ast.Name(id='name', ctx=ast.Load()), value=ast.Name(id='value', ctx=ast.Load())),
            emptyExpected="ast.TypeAlias(name=ast.Name(id='name', ctx=ast.Load()), value=ast.Name(id='value', ctx=ast.Load()))",
            fullExpected="ast.TypeAlias(name=ast.Name(id='name', ctx=ast.Load()), type_params=[], value=ast.Name(id='value', ctx=ast.Load()))"
        )

        check_node(
            ast.TypeIgnore(lineno=1, tag=''),
            emptyExpected="ast.TypeIgnore(lineno=1, tag='')",
            fullExpected="ast.TypeIgnore(lineno=1, tag='')"
        )

        check_node(
            ast.TypeVar(name='name'),
            emptyExpected="ast.TypeVar(name='name')",
            fullExpected="ast.TypeVar(name='name', bound=None, default_value=None)"
        )

        check_node(
            ast.TypeVarTuple(name='name'),
            emptyExpected="ast.TypeVarTuple(name='name')",
            fullExpected="ast.TypeVarTuple(name='name', default_value=None)"
        )

        check_node(
            ast.UAdd(),
            emptyExpected="ast.UAdd()",
            fullExpected="ast.UAdd()"
        )

        check_node(
            ast.unaryop(),
            emptyExpected="ast.unaryop()",
            fullExpected="ast.unaryop()"
        )

        check_node(
            ast.UnaryOp(op=ast.Not(), operand=ast.Constant(value=None)),
            emptyExpected="ast.UnaryOp(op=ast.Not(), operand=ast.Constant(value=None))",
            fullExpected="ast.UnaryOp(op=ast.Not(), operand=ast.Constant(value=None, kind=None))"
        )

        check_node(
            ast.USub(),
            emptyExpected="ast.USub()",
            fullExpected="ast.USub()"
        )

        check_node(
            ast.While(test=ast.Constant(value=None)),
            emptyExpected="ast.While(test=ast.Constant(value=None))",
            fullExpected="ast.While(test=ast.Constant(value=None, kind=None), body=[], orelse=[])"
        )

        check_node(
            ast.With(),
            emptyExpected="ast.With()",
            fullExpected="ast.With(items=[], body=[], type_comment=None)"
        )

        check_node(
            ast.withitem(context_expr=ast.Name(id='name', ctx=ast.Load())),
            emptyExpected="ast.withitem(context_expr=ast.Name(id='name', ctx=ast.Load()))",
            fullExpected="ast.withitem(context_expr=ast.Name(id='name', ctx=ast.Load()), optional_vars=None)"
        )

        check_node(
            ast.Yield(),
            emptyExpected="ast.Yield()",
            fullExpected="ast.Yield(value=None)"
        )

        check_node(
            ast.YieldFrom(value=ast.Constant(value=None)),
            emptyExpected="ast.YieldFrom(value=ast.Constant(value=None))",
            fullExpected="ast.YieldFrom(value=ast.Constant(value=None, kind=None))"
        )        # Add check_text tests to ensure code parsing and dumping works correctly
        check_text(
            'spam(eggs, "and cheese")',
            emptyExpected="ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load()), args=[ast.Name(id='eggs', ctx=ast.Load()), ast.Constant(value='and cheese')]))])",
            fullExpected="ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load()), args=[ast.Name(id='eggs', ctx=ast.Load()), ast.Constant(value='and cheese', kind=None)], keywords=[]))], type_ignores=[])"
        )

        check_text(
            'spam(eggs, text="and cheese")',
            emptyExpected="ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load()), args=[ast.Name(id='eggs', ctx=ast.Load())], keywords=[ast.keyword(arg='text', value=ast.Constant(value='and cheese'))]))])",
            fullExpected="ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load()), args=[ast.Name(id='eggs', ctx=ast.Load())], keywords=[ast.keyword(arg='text', value=ast.Constant(value='and cheese', kind=None))]))], type_ignores=[])"
        )

        check_text(
            "import _ast as ast; from module import sub",
            emptyExpected="ast.Module(body=[ast.Import(names=[ast.alias(name='_ast', asname='ast')]), ast.ImportFrom(module='module', names=[ast.alias(name='sub')], level=0)])",
            fullExpected="ast.Module(body=[ast.Import(names=[ast.alias(name='_ast', asname='ast')]), ast.ImportFrom(module='module', names=[ast.alias(name='sub', asname=None)], level=0)], type_ignores=[])"
        )

        check_text(
            "def a(b: int = 0, *, c): ...",
            emptyExpected="ast.Module(body=[ast.FunctionDef(name='a', args=ast.arguments(args=[ast.arg(arg='b', annotation=ast.Name(id='int', ctx=ast.Load()))], kwonlyargs=[ast.arg(arg='c')], kw_defaults=[None], defaults=[ast.Constant(value=0)]), body=[ast.Expr(value=ast.Constant(value=Ellipsis))])])",
            fullExpected="ast.Module(body=[ast.FunctionDef(name='a', args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='b', annotation=ast.Name(id='int', ctx=ast.Load()), type_comment=None)], vararg=None, kwonlyargs=[ast.arg(arg='c', annotation=None, type_comment=None)], kw_defaults=[None], kwarg=None, defaults=[ast.Constant(value=0, kind=None)]), body=[ast.Expr(value=ast.Constant(value=Ellipsis, kind=None))], decorator_list=[], returns=None, type_comment=None, type_params=[])], type_ignores=[])"
        )

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

    def test_fix_missing_locations_validation(self):
        sourceAst = ast.parse('write("spam")')
        spamCall = Make.Call(Make.Name("spam", ast.Load()), [Make.Constant("eggs")], [])
        sourceAst.body.append(Make.Expr(spamCall))

        assert sourceAst == ast.fix_missing_locations(sourceAst)

        # Verify that missing location attributes are filled in
        secondExpr = sourceAst.body[1]
        assert hasattr(secondExpr, 'lineno')
        assert hasattr(secondExpr, 'col_offset')
        assert secondExpr.lineno == 1
        assert secondExpr.col_offset == 0

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
        keywordNode = next(iterator)
        assert ast.dump(keywordNode) == "keyword(arg='eggs', value=Constant(value='leek'))"

        # Test with Make nodes
        makeSpam = Make.Name("spam", ast.Load())
        makeCall = Make.Call(makeSpam, [Make.Constant(23), Make.Constant(42)],
                           [Make.keyword("eggs", Make.Constant("leek"))])
        makeChildNodes = list(ast.iter_child_nodes(makeCall))
        assert len(makeChildNodes) == 4
        assert makeChildNodes[0].id == "spam"
        assert makeChildNodes[1].value == 23

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
        # Test emptyExpected module
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

    def test_literal_eval_complex_numbers(self):
        # Issue #4907 - complex number literal evaluation
        assert ast.literal_eval("6j") == 6j
        assert ast.literal_eval("-6j") == -6j
        assert ast.literal_eval("6.75j") == 6.75j
        assert ast.literal_eval("-6.75j") == -6.75j
        assert ast.literal_eval("3+6j") == 3+6j
        assert ast.literal_eval("-3+6j") == -3+6j
        assert ast.literal_eval("3-6j") == 3-6j
        assert ast.literal_eval("-3-6j") == -3-6j
        assert ast.literal_eval("3.25+6.75j") == 3.25+6.75j
        assert ast.literal_eval("-3.25+6.75j") == -3.25+6.75j
        assert ast.literal_eval("3.25-6.75j") == 3.25-6.75j
        assert ast.literal_eval("-3.25-6.75j") == -3.25-6.75j
        assert ast.literal_eval("(3+6j)") == 3+6j

        # Test invalid complex expressions
        with pytest.raises(ValueError):
            ast.literal_eval("-6j+3")
        with pytest.raises(ValueError):
            ast.literal_eval("-6j+3j")
        with pytest.raises(ValueError):
            ast.literal_eval("3+-6j")
        with pytest.raises(ValueError):
            ast.literal_eval("3+(0+6j)")
        with pytest.raises(ValueError):
            ast.literal_eval("-(3+6j)")

    def test_literal_eval_edge_cases(self):
        # Test negative zero
        assert repr(ast.literal_eval("-0.0")) == "-0.0"

        # Test invalid operations
        with pytest.raises(ValueError):
            ast.literal_eval("++6")
        with pytest.raises(ValueError):
            ast.literal_eval("+True")
        with pytest.raises(ValueError):
            ast.literal_eval("2+3")

    def test_literal_eval_malformed_dict(self):
        # Test malformed dictionary nodes
        malformedKeysMoreThanValues = ast.Dict(
            keys=[ast.Constant(1), ast.Constant(2)],
            values=[ast.Constant(3)]
        )
        with pytest.raises(ValueError):
            ast.literal_eval(malformedKeysMoreThanValues)

        malformedValuesMoreThanKeys = ast.Dict(
            keys=[ast.Constant(1)],
            values=[ast.Constant(2), ast.Constant(3)]
        )
        with pytest.raises(ValueError):
            ast.literal_eval(malformedValuesMoreThanKeys)

    def test_literal_eval_trailing_whitespace(self):
        assert ast.literal_eval("    -1") == -1
        assert ast.literal_eval("\t\t-1") == -1
        assert ast.literal_eval(" \t -1") == -1

        with pytest.raises(IndentationError):
            ast.literal_eval("\n -1")

    def test_multi_line_docstring_positions(self):
        nodeAst = ast.parse(
            '"""line one\nline two"""\n\n'
            'def foo():\n  """line one\n  line two"""\n\n'
            '  def bar():\n    """line one\n    line two"""\n'
            '  """line one\n  line two"""\n'
            '"""line one\nline two"""\n\n'
        )

        # Test position attributes for multi-line docstrings
        assert nodeAst.body[0].col_offset == 0
        assert nodeAst.body[0].lineno == 1
        assert nodeAst.body[1].body[0].col_offset == 2
        assert nodeAst.body[1].body[0].lineno == 5
        assert nodeAst.body[1].body[1].body[0].col_offset == 4
        assert nodeAst.body[1].body[1].body[0].lineno == 9
        assert nodeAst.body[1].body[2].col_offset == 2
        assert nodeAst.body[1].body[2].lineno == 11
        assert nodeAst.body[2].col_offset == 0
        assert nodeAst.body[2].lineno == 13

    def test_elif_stmt_positions(self):
        # Test elif statement position tracking
        nodeAst = ast.parse("if a:\n    pass\nelif b:\n    pass\n")
        elifStmt = nodeAst.body[0].orelse[0]
        assert elifStmt.lineno == 3
        assert elifStmt.col_offset == 0

        # Test elif with else
        nodeWithElse = ast.parse("if a:\n    pass\nelif b:\n    pass\nelse:\n    pass\n")
        elifStmtWithElse = nodeWithElse.body[0].orelse[0]
        assert elifStmtWithElse.lineno == 3
        assert elifStmtWithElse.col_offset == 0

    def test_starred_expr_positions(self):
        nodeAst = ast.parse("f(*[0, 1])")
        starredExpr = nodeAst.body[0].value.args[0]
        assert starredExpr.end_lineno == 1
        assert starredExpr.end_col_offset == 9

    def test_increment_lineno_on_module_with_type_comments(self):
        sourceCode = """\
a = 1
b = 2 # type: ignore
c = 3
d = 4 # type: ignore@tag
"""
        sourceAst = ast.parse(sourceCode, type_comments=True)
        ast.increment_lineno(sourceAst, n=5)

        # Check type ignore comments are updated
        assert len(sourceAst.type_ignores) >= 2
        assert sourceAst.type_ignores[0].lineno == 7
        assert sourceAst.type_ignores[1].lineno == 9
        if hasattr(sourceAst.type_ignores[1], 'tag'):
            assert sourceAst.type_ignores[1].tag == "@tag"

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
