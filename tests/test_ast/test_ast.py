from ast import fix_missing_locations, parse
from astToolkit import ConstantValueType, dump, Make
from collections.abc import Callable
from tests import support
from tests.support.ast_helper import ASTTestMixin
from tests.test_ast.snippets import eval_results, eval_tests, exec_results, exec_tests, single_results, single_tests
from tests.test_ast.utils import to_tuple
from textwrap import dedent
from typing import cast, ClassVar
import ast
import textwrap
import unittest

class AST_Tests(unittest.TestCase):
	maxDiff = None

	def _is_ast_node(self, name: str, node: ast.AST) -> bool:
		if not isinstance(node, type):
			return False
		if "ast" not in node.__module__:
			return False
		return name != "AST" and name[0].isupper()

	def _assertTrueorder(self, ast_node: ast.AST, parent_position: tuple[int, int]) -> None:
		if not isinstance(ast_node, ast.AST):
			return
		if isinstance(ast_node, (ast.expr, ast.stmt, ast.excepthandler)):
			node_pos = (ast_node.lineno, ast_node.col_offset)
			self.assertGreaterEqual(node_pos, parent_position)
			parent_position = (ast_node.lineno, ast_node.col_offset)
		for name in ast_node._fields:
			value = getattr(ast_node, name)
			if isinstance(value, list):
				first_pos = parent_position
				if value and name == "decorator_list":
					first_pos = (value[0].lineno, value[0].col_offset)
				for child in value:
					self._assertTrueorder(child, first_pos)
			elif value is not None:
				self._assertTrueorder(value, parent_position)
		self.assertEqual(ast_node._fields, ast_node.__match_args__)

	def test_snippets(self) -> None:
		for listInput, listOutput, kind in (
			(exec_tests, exec_results, "exec"),
			(single_tests, single_results, "single"),
			(eval_tests, eval_results, "eval"),
		):
			for testInput, expectedOutput in zip(listInput, listOutput, strict=True):
				with self.subTest(action="parsing", input=testInput):
					ast_tree = compile(testInput, "?", kind, ast.PyCF_ONLY_AST)
					self.assertEqual(to_tuple(ast_tree), expectedOutput)
					self._assertTrueorder(ast_tree, (0, 0))
				with self.subTest(action="compiling", input=testInput, kind=kind):
					compile(ast_tree, "?", kind)

	def test_ast_validation(self) -> None:
		# compile() is the only function that calls PyAST_Validate  # noqa: ERA001
		snippets_to_validate = exec_tests + single_tests + eval_tests
		for snippet in snippets_to_validate:
			tree = parse(snippet)
			compile(tree, "<string>", "exec")

	def test_arguments(self) -> None:
		x = Make.arguments()
		self.assertEqual(
			x._fields,
			(
				"posonlyargs",
				"args",
				"vararg",
				"kwonlyargs",
				"kw_defaults",
				"kwarg",
				"defaults",
			),
		)
		self.assertEqual(
			x.__annotations__,
			{
				"posonlyargs": list[ast.arg],
				"args": list[ast.arg],
				"vararg": ast.arg | None,
				"kwonlyargs": list[ast.arg],
				"kw_defaults": list[ast.expr],
				"kwarg": ast.arg | None,
				"defaults": list[ast.expr],
			},
		)

		self.assertEqual(x.args, [])
		self.assertIsNone(x.vararg)

	def test_module(self) -> None:
		body = [Make.Expr(Make.Constant(42))]
		x = Make.Module(body, [])
		self.assertEqual(x.body, body)

	def test_no_fields(self) -> None:
		# this used to fail because Sub._fields was None
		x = Make.Sub()
		self.assertEqual(x._fields, ())

	def test_invalid_sum(self) -> None:
		pos = {"lineno": 2, "col_offset": 3}
		m = Make.Module([Make.Expr(Make.expr(**pos), **pos)], [])
		with self.assertRaises(TypeError) as cm:
			compile(m, "<test>", "exec")
		self.assertIn("but got <ast.expr", str(cm.exception))

	def test_invalid_identifier(self) -> None:
		m = Make.Module([Make.Expr(Make.Name(42, Make.Load()))], []) # pyright: ignore[reportArgumentType]
		fix_missing_locations(m)
		with self.assertRaises(TypeError) as cm:
			compile(m, "<test>", "exec")
		self.assertIn("identifier must be of type str", str(cm.exception))

	def test_invalid_constant(self) -> None:
		for invalid_constant in int, (1, 2, int), frozenset((1, 2, int)):
			e = Make.Expression(body=Make.Constant(invalid_constant)) # pyright: ignore[reportArgumentType]
			fix_missing_locations(e)
			with self.assertRaisesRegex(TypeError, "invalid type in Constant: type"):
				compile(e, "<test>", "eval")

	def test_empty_yield_from(self) -> None:
		# Issue 16546: yield from value is not optional.  # noqa: ERA001
		empty_yield_from = parse("def f():\n yield from g()")
		empty_yield_from.body[0].body[0].value.value = None
		with self.assertRaises(ValueError) as cm:
			compile(empty_yield_from, "<test>", "exec")
		self.assertIn("field 'value' is required", str(cm.exception))

class ASTHelpers_Test(unittest.TestCase):
	maxDiff = None

	def test_dump(self) -> None:
		node = parse('spam(eggs, "and cheese")')
		self.assertEqual(
			dump(node),
			"ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load()), "
			"args=[ast.Name(id='eggs', ctx=ast.Load()), ast.Constant(value='and cheese')]))])",
		)
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.Module([ast.Expr(ast.Call(ast.Name('spam', ast.Load()), [ast.Name('eggs', ast.Load()), "
			"ast.Constant('and cheese')]))])",
		)
		self.assertEqual(
			dump(node, include_attributes=True),
			"ast.Module(body=[ast.Expr(value=ast.Call(func=ast.Name(id='spam', ctx=ast.Load(), "
			"lineno=1, col_offset=0, end_lineno=1, end_col_offset=4), "
			"args=[ast.Name(id='eggs', ctx=ast.Load(), lineno=1, col_offset=5, "
			"end_lineno=1, end_col_offset=9), ast.Constant(value='and cheese', "
			"lineno=1, col_offset=11, end_lineno=1, end_col_offset=23)], "
			"lineno=1, col_offset=0, end_lineno=1, end_col_offset=24), "
			"lineno=1, col_offset=0, end_lineno=1, end_col_offset=24)])",
		)

	def test_dump_indent(self) -> None:
		node = parse('spam(eggs, "and cheese")')
# 		self.assertEqual(
# 			dump(node, indent=3),
# 			"""\
# ast.Module(
#    body=[
# 	  ast.Expr(
# 		 value=ast.Call(
# 			func=ast.Name(id='spam', ctx=ast.Load()),
# 			args=[
# 			   ast.Name(id='eggs', ctx=ast.Load()),
# 			   ast.Constant(value='and cheese')]))])""",
# 		)
		self.assertEqual(
			dump(node, annotate_fields=False, indent="\t"),
			"""\
ast.Module(
\t[
\t\tast.Expr(
\t\t\tast.Call(
\t\t\t\tast.Name('spam', ast.Load()),
\t\t\t\t[
\t\t\t\t\tast.Name('eggs', ast.Load()),
\t\t\t\t\tast.Constant('and cheese')]))])""",
		)
# 		self.assertEqual(
# 			dump(node, include_attributes=True, indent=3),
# 			"""\
# ast.Module(
#    body=[
# 	  ast.Expr(
# 		 value=ast.Call(
# 			func=ast.Name(
# 			   id='spam',
# 			   ctx=ast.Load(),
# 			   lineno=1,
# 			   col_offset=0,
# 			   end_lineno=1,
# 			   end_col_offset=4),
# 			args=[
# 			   ast.Name(
# 				  id='eggs',
# 				  ctx=ast.Load(),
# 				  lineno=1,
# 				  col_offset=5,
# 				  end_lineno=1,
# 				  end_col_offset=9),
# 			   ast.Constant(
# 				  value='and cheese',
# 				  lineno=1,
# 				  col_offset=11,
# 				  end_lineno=1,
# 				  end_col_offset=23)],
# 			lineno=1,
# 			col_offset=0,
# 			end_lineno=1,
# 			end_col_offset=24),
# 		 lineno=1,
# 		 col_offset=0,
# 		 end_lineno=1,
# 		 end_col_offset=24)])""",
# 		)

	def test_dump_incomplete(self) -> None:
		node = Make.Raise(lineno=3, col_offset=4)
		self.assertEqual(dump(node), "ast.Raise()")
		self.assertEqual(
			dump(node, include_attributes=True), "ast.Raise(lineno=3, col_offset=4)"
		)
		node = Make.Raise(exc=Make.Name(id="e", context=Make.Load()), lineno=3, col_offset=4)
		self.assertEqual(dump(node), "ast.Raise(exc=ast.Name(id='e', ctx=ast.Load()))")
		self.assertEqual(
			dump(node, annotate_fields=False), "ast.Raise(ast.Name('e', ast.Load()))"
		)
		self.assertEqual(
			dump(node, include_attributes=True),
			"ast.Raise(exc=ast.Name(id='e', ctx=ast.Load()), lineno=3, col_offset=4)",
		)
		self.assertEqual(
			dump(node, annotate_fields=False, include_attributes=True),
			"ast.Raise(ast.Name('e', ast.Load()), lineno=3, col_offset=4)",
		)
		node = Make.Raise(cause=Make.Name(id="e", context=Make.Load()))
		self.assertEqual(dump(node), "ast.Raise(cause=ast.Name(id='e', ctx=ast.Load()))")
		self.assertEqual(
			dump(node, annotate_fields=False), "ast.Raise(cause=ast.Name('e', ast.Load()))"
		)
		# Arguments:  # noqa: ERA001
		node = Make.arguments(list_arg=[Make.arg("x")])
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.arguments([], [ast.arg('x')])",
		)
		node = Make.arguments(posonlyargs=[Make.arg("x")])
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.arguments([ast.arg('x')])",
		)
		node = Make.arguments(posonlyargs=[Make.arg("x")], kwonlyargs=[Make.arg("y")])
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.arguments([ast.arg('x')], kwonlyargs=[ast.arg('y')])",
		)
		node = Make.arguments(list_arg=[Make.arg("x")], kwonlyargs=[Make.arg("y")])
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.arguments([], [ast.arg('x')], kwonlyargs=[ast.arg('y')])",
		)
		node = Make.arguments()
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.arguments()",
		)
		# Classes:  # noqa: ERA001
		node = Make.ClassDef(
			"T",
			[],
			[Make.keyword("a", Make.Constant(None))],
			[],
			[Make.Name("dataclass", context=Make.Load())],
		)
		self.assertEqual(
			dump(node),
			"ast.ClassDef(name='T', keywords=[ast.keyword(arg='a', value=ast.Constant(value=None))], decorator_list=[ast.Name(id='dataclass', ctx=ast.Load())])",
		)
		self.assertEqual(
			dump(node, annotate_fields=False),
			"ast.ClassDef('T', [], [ast.keyword('a', ast.Constant(None))], [], [ast.Name('dataclass', ast.Load())])",
		)

	def test_bad_integer(self) -> None:
		# issue13436: Bad error message with invalid numeric values  # noqa: ERA001
		body = [Make.ImportFrom(dotModule="time", list_alias=[Make.alias(dotModule="sleep")], level=None, lineno=None, col_offset=None)] # pyright: ignore[reportArgumentType]
		mod = Make.Module(body, [])
		with self.assertRaises(ValueError) as cm:
			compile(mod, "test", "exec")
		self.assertIn("invalid integer value: None", str(cm.exception))

	def test_level_as_none(self) -> None:
		body = [Make.ImportFrom(dotModule="time", list_alias=[Make.alias(dotModule="sleep", lineno=0, col_offset=0)], level=None, lineno=0, col_offset=0)] # pyright: ignore[reportArgumentType]
		mod = Make.Module(body, [])
		code = compile(mod, "test", "exec")
		ns = {}
		exec(code, ns)  # noqa: S102
		self.assertIn("sleep", ns)

	def test_recursion_direct(self) -> None:
		e = Make.UnaryOp(op=Make.Not(), lineno=0, col_offset=0, operand=Make.Constant(1))
		e.operand = e
		with self.assertRaises(RecursionError), support.infinite_recursion():
			compile(Make.Expression(e), "<test>", "eval")

	def test_recursion_indirect(self) -> None:
		e = Make.UnaryOp(op=Make.Not(), lineno=0, col_offset=0, operand=Make.Constant(1))
		f = Make.UnaryOp(op=Make.Not(), lineno=0, col_offset=0, operand=Make.Constant(1))
		e.operand = f
		f.operand = e
		with self.assertRaises(RecursionError), support.infinite_recursion():
			compile(Make.Expression(e), "<test>", "eval")

class ASTValidatorTests(unittest.TestCase):
	def mod(self, mod: ast.Module, msg: str | None = None, mode: str = "exec", *, exc: type[BaseException] = ValueError) -> None:
		mod.lineno = mod.col_offset = 0
		fix_missing_locations(mod)
		if msg is None:
			compile(mod, "<test>", mode)
		else:
			with self.assertRaises(exc) as cm:
				compile(mod, "<test>", mode)
			self.assertIn(msg, str(cm.exception))

	def expr(self, node: ast.expr, msg: str | None = None, *, exc: type[BaseException] = ValueError) -> None:
		mod = Make.Module([Make.Expr(node)], [])
		self.mod(mod, msg, exc=exc)

	def stmt(self, stmt: ast.stmt, msg: str | None = None) -> None:
		mod = Make.Module([stmt], [])
		self.mod(mod, msg)

	def test_module(self) -> None:
		m = Make.Interactive([Make.Expr(Make.Name("x", Make.Store()))])
		self.mod(m, "must have Load context", "single")
		m = Make.Expression(Make.Name("x", Make.Store()))
		self.mod(m, "must have Load context", "eval")

	def _check_arguments(self, fac: Callable[[ast.arguments], ast.FunctionDef], check: Callable[[ast.AST, str | None], None]) -> None:
		def arguments(
			args: list[ast.arg] | None = None,
			posonlyargs: list[ast.arg] | None = None,
			vararg: ast.arg | None = None,
			kwonlyargs: list[ast.arg] | None = None,
			kwarg: ast.arg | None = None,
			defaults: list[ast.expr] | None = None,
			kw_defaults: list[ast.expr] | None = None,
		) -> ast.AST:
			if args is None:
				args = []
			if posonlyargs is None:
				posonlyargs = []
			if kwonlyargs is None:
				kwonlyargs = []
			if defaults is None:
				defaults = []
			if kw_defaults is None:
				kw_defaults = []
			args_obj = Make.arguments(
				args, posonlyargs, vararg, kwonlyargs, kw_defaults, kwarg, defaults
			)
			return fac(args_obj)

		args = [Make.arg("x", Make.Name("x", Make.Store()))]
		check(arguments(args=args), "must have Load context")
		check(arguments(posonlyargs=args), "must have Load context")
		check(arguments(kwonlyargs=args), "must have Load context")
		check(
			arguments(defaults=[Make.Constant(3)]), "more positional defaults than args"
		)
		check(
			arguments(kw_defaults=[Make.Constant(4)]),
			"length of kwonlyargs is not the same as kw_defaults",
		)
		args = [Make.arg("x", Make.Name("x", Make.Load()))]
		check(
			arguments(args=args, defaults=[Make.Name("x", Make.Store())]),
			"must have Load context",
		)
		args = [
			Make.arg("a", Make.Name("x", Make.Load())),
			Make.arg("b", Make.Name("y", Make.Load())),
		]
		check(
			arguments(kwonlyargs=args, kw_defaults=[None, Make.Name("x", Make.Store())]),
			"must have Load context",
		)

	def test_funcdef(self) -> None:
		a = Make.arguments([], [], None, [], [], None, [])
		f = Make.FunctionDef("x", a, [], [], None, None)
		self.stmt(f, "empty body on FunctionDef")
		f = Make.FunctionDef("x", a, [Make.Pass()], [Make.Name("x", Make.Store())], None, None)
		self.stmt(f, "must have Load context")
		f = Make.FunctionDef("x", a, [Make.Pass()], [], Make.Name("x", Make.Store()), None)
		self.stmt(f, "must have Load context")
		f = Make.FunctionDef("x", Make.arguments(), [Make.Pass()])
		self.stmt(f)

		def fac(args: ast.arguments) -> ast.FunctionDef:
			return Make.FunctionDef("x", args, [Make.Pass()], [], None, None)

		self._check_arguments(fac, self.stmt)

	def test_funcdef_pattern_matching(self) -> None:
		# gh-104799: New fields on FunctionDef should be added at the end  # noqa: ERA001
		def matcher(node: ast.AST) -> bool:
			match node:
				case ast.FunctionDef(
					"foo",
					ast.arguments(args=[ast.arg("bar")]),
					[ast.Pass()],
					[ast.Name("capybara", ast.Load())],
					ast.Name("pacarana", ast.Load()),
				):
					return True
				case _:
					return False

		code = """
			@capybara
			def foo(bar) -> pacarana:
				pass
		"""
		source = parse(textwrap.dedent(code))
		funcdef = source.body[0]
		self.assertIsInstance(funcdef, ast.FunctionDef)
		self.assertTrue(matcher(funcdef))

	def test_classdef(self) -> None:
		def cls(
			bases: list[ast.expr] | None = None,
			keywords: list[ast.keyword] | None = None,
			body: list[ast.stmt] | None = None,
			decorator_list: list[ast.expr] | None = None,
			type_params: list[ast.type_param] | None = None,
		) -> ast.ClassDef:
			if bases is None:
				bases = []
			if keywords is None:
				keywords = []
			if body is None:
				body = [Make.Pass()]
			if decorator_list is None:
				decorator_list = []
			if type_params is None:
				type_params = []
			return Make.ClassDef(
				"myclass", bases, keywords, body, decorator_list, type_params
			)

		self.stmt(cls(bases=[Make.Name("x", Make.Store())]), "must have Load context")
		self.stmt(
			cls(keywords=[Make.keyword("x", Make.Name("x", Make.Store()))]),
			"must have Load context",
		)
		self.stmt(cls(body=[]), "empty body on ClassDef")
		self.stmt(cls(body=[None]), "None disallowed")
		self.stmt(
			cls(decorator_list=[Make.Name("x", Make.Store())]), "must have Load context"
		)

	def test_delete(self) -> None:
		self.stmt(Make.Delete([]), "empty targets on Delete")
		self.stmt(Make.Delete([None]), "None disallowed") # pyright: ignore[reportArgumentType]
		self.stmt(Make.Delete([Make.Name("x", Make.Load())]), "must have Del context")

	def test_assign(self) -> None:
		self.stmt(Make.Assign([], Make.Constant(3)), "empty targets on Assign")
		self.stmt(Make.Assign([None], Make.Constant(3)), "None disallowed") # pyright: ignore[reportArgumentType]
		self.stmt(
			Make.Assign([Make.Name("x", Make.Load())], Make.Constant(3)),
			"must have Store context",
		)
		self.stmt(
			Make.Assign([Make.Name("x", Make.Store())], Make.Name("y", Make.Store())),
			"must have Load context",
		)

	def test_augassign(self) -> None:
		aug = Make.AugAssign(
			Make.Name("x", Make.Load()), Make.Add(), Make.Name("y", Make.Load())
		)
		self.stmt(aug, "must have Store context")
		aug = Make.AugAssign(
			Make.Name("x", Make.Store()), Make.Add(), Make.Name("y", Make.Store())
		)
		self.stmt(aug, "must have Load context")

	def test_for(self) -> None:
		x = Make.Name("x", Make.Store())
		y = Make.Name("y", Make.Load())
		p = Make.Pass()
		self.stmt(Make.For(x, y, [], []), "empty body on For")
		self.stmt(
			Make.For(Make.Name("x", Make.Load()), y, [p], []), "must have Store context"
		)
		self.stmt(
			Make.For(x, Make.Name("y", Make.Store()), [p], []), "must have Load context"
		)
		e = Make.Expr(Make.Name("x", Make.Store()))
		self.stmt(Make.For(x, y, [e], []), "must have Load context")
		self.stmt(Make.For(x, y, [p], [e]), "must have Load context")

	def test_while(self) -> None:
		self.stmt(Make.While(Make.Constant(3), [], []), "empty body on While")
		self.stmt(
			Make.While(Make.Name("x", Make.Store()), [Make.Pass()], []),
			"must have Load context",
		)
		self.stmt(
			Make.While(
				Make.Constant(3), [Make.Pass()], [Make.Expr(Make.Name("x", Make.Store()))]
			),
			"must have Load context",
		)

	def test_if(self) -> None:
		self.stmt(Make.If(Make.Constant(3), [], []), "empty body on If")
		i = Make.If(Make.Name("x", Make.Store()), [Make.Pass()], [])
		self.stmt(i, "must have Load context")
		i = Make.If(Make.Constant(3), [Make.Expr(Make.Name("x", Make.Store()))], [])
		self.stmt(i, "must have Load context")
		i = Make.If(
			Make.Constant(3), [Make.Pass()], [Make.Expr(Make.Name("x", Make.Store()))]
		)
		self.stmt(i, "must have Load context")

	def test_with(self) -> None:
		p = Make.Pass()
		self.stmt(Make.With([], [p]), "empty items on With")
		i = Make.withitem(Make.Constant(3), None)
		self.stmt(Make.With([i], []), "empty body on With")
		i = Make.withitem(Make.Name("x", Make.Store()), None)
		self.stmt(Make.With([i], [p]), "must have Load context")
		i = Make.withitem(Make.Constant(3), Make.Name("x", Make.Load()))
		self.stmt(Make.With([i], [p]), "must have Store context")

	def test_raise(self) -> None:
		r = Make.Raise(None, Make.Constant(3))
		self.stmt(r, "Raise with cause but no exception")
		r = Make.Raise(Make.Name("x", Make.Store()), None)
		self.stmt(r, "must have Load context")
		r = Make.Raise(Make.Constant(4), Make.Name("x", Make.Store()))
		self.stmt(r, "must have Load context")

	def test_try(self) -> None:
		p = Make.Pass()
		t = Make.Try([], [], [], [p])
		self.stmt(t, "empty body on Try")
		t = Make.Try([Make.Expr(Make.Name("x", Make.Store()))], [], [], [p])
		self.stmt(t, "must have Load context")
		t = Make.Try([p], [], [], [])
		self.stmt(t, "Try has neither except handlers nor finalbody")
		t = Make.Try([p], [], [p], [p])
		self.stmt(t, "Try has orelse but no except handlers")
		t = Make.Try([p], [Make.ExceptHandler(None, "x", [])], [], [])
		self.stmt(t, "empty body on ExceptHandler")
		e = [Make.ExceptHandler(Make.Name("x", Make.Store()), "y", [p])]
		self.stmt(Make.Try([p], e, [], []), "must have Load context")
		e = [Make.ExceptHandler(None, "x", [p])]
		t = Make.Try([p], e, [Make.Expr(Make.Name("x", Make.Store()))], [p])
		self.stmt(t, "must have Load context")
		t = Make.Try([p], e, [p], [Make.Expr(Make.Name("x", Make.Store()))])
		self.stmt(t, "must have Load context")

	def test_try_star(self) -> None:
		p = Make.Pass()
		t = Make.TryStar([], [], [], [p])
		self.stmt(t, "empty body on TryStar")
		t = Make.TryStar([Make.Expr(Make.Name("x", Make.Store()))], [], [], [p])
		self.stmt(t, "must have Load context")
		t = Make.TryStar([p], [], [], [])
		self.stmt(t, "TryStar has neither except handlers nor finalbody")
		t = Make.TryStar([p], [], [p], [p])
		self.stmt(t, "TryStar has orelse but no except handlers")
		t = Make.TryStar([p], [Make.ExceptHandler(None, "x", [])], [], [])
		self.stmt(t, "empty body on ExceptHandler")
		e = [Make.ExceptHandler(Make.Name("x", Make.Store()), "y", [p])]
		self.stmt(Make.TryStar([p], e, [], []), "must have Load context")
		e = [Make.ExceptHandler(None, "x", [p])]
		t = Make.TryStar([p], e, [Make.Expr(Make.Name("x", Make.Store()))], [p])
		self.stmt(t, "must have Load context")
		t = Make.TryStar([p], e, [p], [Make.Expr(Make.Name("x", Make.Store()))])
		self.stmt(t, "must have Load context")

	def test_assert(self) -> None:
		self.stmt(
			Make.Assert(Make.Name("x", Make.Store()), None), "must have Load context"
		)
		assrt = Make.Assert(Make.Name("x", Make.Load()), Make.Name("y", Make.Store()))
		self.stmt(assrt, "must have Load context")

	def test_importfrom(self) -> None:
		imp = Make.ImportFrom(None, [Make.alias("x", None)], -42)
		self.stmt(imp, "Negative ImportFrom level")
		self.stmt(Make.ImportFrom(None, [], 0), "empty names on ImportFrom")

	def test_global(self) -> None:
		self.stmt(Make.Global([]), "empty names on Global")

	def test_nonlocal(self) -> None:
		self.stmt(Make.Nonlocal([]), "empty names on Nonlocal")

	def test_expr(self) -> None:
		e = Make.Expr(Make.Name("x", Make.Store()))
		self.stmt(e, "must have Load context")

	def test_boolop(self) -> None:
		b = Make.BoolOp(Make.And(), [])
		self.expr(b, "less than 2 values")
		b = Make.BoolOp(Make.And(), [Make.Constant(3)])
		self.expr(b, "less than 2 values")
		b = Make.BoolOp(Make.And(), [Make.Constant(4), None]) # pyright: ignore[reportArgumentType]
		self.expr(b, "None disallowed")
		b = Make.BoolOp(Make.And(), [Make.Constant(4), Make.Name("x", Make.Store())])
		self.expr(b, "must have Load context")

	def test_unaryop(self) -> None:
		u = Make.UnaryOp(Make.Not(), Make.Name("x", Make.Store()))
		self.expr(u, "must have Load context")

	def test_lambda(self) -> None:
		a = Make.arguments([], [], None, [], [], None, [])
		self.expr(Make.Lambda(a, Make.Name("x", Make.Store())), "must have Load context")

		def fac(args: ast.arguments) -> ast.Lambda:
			return Make.Lambda(args, Make.Name("x", Make.Load()))

		self._check_arguments(fac, self.expr)

	def test_ifexp(self) -> None:
		load = Make.Name("x", Make.Load())
		store = Make.Name("y", Make.Store())
		for args in (store, load, load), (load, store, load), (load, load, store):
			self.expr(Make.IfExp(*args), "must have Load context")

	def test_dict(self) -> None:
		d = Make.Dict([], [Make.Name("x", Make.Load())])
		self.expr(d, "same number of keys as values")
		d = Make.Dict([Make.Name("x", Make.Load())], [None]) # pyright: ignore[reportArgumentType]
		self.expr(d, "None disallowed")

	def test_set(self) -> None:
		self.expr(Make.Set([None]), "None disallowed") # pyright: ignore[reportArgumentType]
		s = Make.Set([Make.Name("x", Make.Store())])
		self.expr(s, "must have Load context")

	def _check_comprehension(self, fac: Callable[[ast.arguments], ast.FunctionDef]) -> None:
		self.expr(fac([]), "comprehension with no generators")
		g = Make.comprehension(
			Make.Name("x", Make.Load()), Make.Name("x", Make.Load()), [], 0
		)
		self.expr(fac([g]), "must have Store context")
		g = Make.comprehension(
			Make.Name("x", Make.Store()), Make.Name("x", Make.Store()), [], 0
		)
		self.expr(fac([g]), "must have Load context")
		x = Make.Name("x", Make.Store())
		y = Make.Name("y", Make.Load())
		g = Make.comprehension(x, y, [None], 0) # pyright: ignore[reportArgumentType]
		self.expr(fac([g]), "None disallowed")
		g = Make.comprehension(x, y, [Make.Name("x", Make.Store())], 0)
		self.expr(fac([g]), "must have Load context")

	def _simple_comp(self, fac: Callable[[ast.arguments], ast.FunctionDef]) -> None:
		g = Make.comprehension(
			Make.Name("x", Make.Store()), Make.Name("x", Make.Load()), [], 0
		)
		self.expr(fac(Make.Name("x", Make.Store()), [g]), "must have Load context")

		def wrap(gens: list[ast.comprehension]) -> ast.AST:
			return fac(Make.Name("x", Make.Store()), gens)

		self._check_comprehension(wrap)

	def test_listcomp(self) -> None:
		self._simple_comp(ast.ListComp)

	def test_setcomp(self) -> None:
		self._simple_comp(ast.SetComp)

	def test_generatorexp(self) -> None:
		self._simple_comp(ast.GeneratorExp)

	def test_dictcomp(self) -> None:
		g = Make.comprehension(
			Make.Name("y", Make.Store()), Make.Name("p", Make.Load()), [], 0
		)
		c = Make.DictComp(Make.Name("x", Make.Store()), Make.Name("y", Make.Load()), [g])
		self.expr(c, "must have Load context")
		c = Make.DictComp(Make.Name("x", Make.Load()), Make.Name("y", Make.Store()), [g])
		self.expr(c, "must have Load context")

		def factory(comps: list[ast.comprehension]) -> ast.DictComp:
			k = Make.Name("x", Make.Load())
			v = Make.Name("y", Make.Load())
			return Make.DictComp(k, v, comps)

		self._check_comprehension(factory)

	def test_yield(self) -> None:
		self.expr(Make.Yield(Make.Name("x", Make.Store())), "must have Load")
		self.expr(Make.YieldFrom(Make.Name("x", Make.Store())), "must have Load")

	def test_compare(self) -> None:
		left = Make.Name("x", Make.Load())
		comp = Make.Compare(left, [Make.In()], [])
		self.expr(comp, "no comparators")
		comp = Make.Compare(left, [Make.In()], [Make.Constant(4), Make.Constant(5)])
		self.expr(comp, "different number of comparators and operands")
		comp = Make.Compare(Make.Constant("blah"), [Make.In()], [left])
		self.expr(comp)
		comp = Make.Compare(left, [Make.In()], [Make.Constant("blah")])
		self.expr(comp)

	def test_call(self) -> None:
		func = Make.Name("x", Make.Load())
		args = [Make.Name("y", Make.Load())]
		keywords = [Make.keyword("w", Make.Name("z", Make.Load()))]
		call = Make.Call(Make.Name("x", Make.Store()), args, keywords)
		self.expr(call, "must have Load context")
		call = Make.Call(func, [None], keywords) # pyright: ignore[reportArgumentType]
		self.expr(call, "None disallowed")
		bad_keywords = [Make.keyword("w", Make.Name("z", Make.Store()))]
		call = Make.Call(func, args, bad_keywords)
		self.expr(call, "must have Load context")

	def test_attribute(self) -> None:
		attr = Make.Attribute(Make.Name("x", Make.Store()), "y", context=Make.Load())
		self.expr(attr, "must have Load context")

	def test_subscript(self) -> None:
		sub = Make.Subscript(Make.Name("x", Make.Store()), Make.Constant(3), context=Make.Load())
		self.expr(sub, "must have Load context")
		x = Make.Name("x", Make.Load())
		sub = Make.Subscript(x, Make.Name("y", Make.Store()), context=Make.Load())
		self.expr(sub, "must have Load context")
		s = Make.Name("x", Make.Store())
		for args in (s, None, None), (None, s, None), (None, None, s):
			sl = Make.Slice(*args)
			self.expr(Make.Subscript(x, sl, Make.Load()), "must have Load context")
		sl = Make.Tuple([], Make.Load())
		self.expr(Make.Subscript(x, sl, Make.Load()))
		sl = Make.Tuple([s], Make.Load())
		self.expr(Make.Subscript(x, sl, Make.Load()), "must have Load context")

	def test_starred(self) -> None:
		left = Make.List(
			[Make.Starred(Make.Name("x", Make.Load()), Make.Store())], Make.Store()
		)
		assign = Make.Assign([left], Make.Constant(4))
		self.stmt(assign, "must have Store context")

	def _sequence(self, fac: Callable[[ast.arguments], ast.FunctionDef]) -> None:
		self.expr(fac([None], Make.Load()), "None disallowed")
		self.expr(
			fac([Make.Name("x", Make.Store())], Make.Load()), "must have Load context"
		)

	def test_list(self) -> None:
		self._sequence(ast.List)

	def test_tuple(self) -> None:
		self._sequence(ast.Tuple)

	constant_1: ast.Constant = Make.Constant(1)
	pattern_1: ast.MatchValue = Make.MatchValue(constant_1)

	constant_x: ast.Constant = Make.Constant("x")
	pattern_x: ast.MatchValue = Make.MatchValue(constant_x)

	constant_true: ast.Constant = Make.Constant(True)
	pattern_true: ast.MatchSingleton = Make.MatchSingleton(True)

	name_carter: ast.Name = Make.Name("carter", Make.Load())

	_MATCH_PATTERNS: ClassVar[list[ast.pattern]] = [
		Make.MatchValue(Make.Attribute(Make.Attribute(Make.Name("x", Make.Store()), "y", context=Make.Load()), "z", context=Make.Load())),
		Make.MatchValue(Make.Attribute(Make.Attribute(Make.Name("x", Make.Load()), "y", context=Make.Store()), "z", context=Make.Load())),
		Make.MatchValue(Make.Constant(...)),
		Make.MatchValue(Make.Constant(True)),
		Make.MatchValue(Make.Constant((1, 2, 3))),
		Make.MatchSingleton("string"),
		Make.MatchSequence([Make.MatchSingleton("string")]),
		Make.MatchSequence([Make.MatchSequence([Make.MatchSingleton("string")])]),
		Make.MatchMapping([constant_1, constant_true], [pattern_x]),
		Make.MatchMapping([constant_true, constant_1], [pattern_x, pattern_1], rest="True"),
		Make.MatchMapping([constant_true, Make.Starred(Make.Name("lol", Make.Load()), Make.Load())], [pattern_x, pattern_1], rest="legit"),
		Make.MatchClass(Make.Attribute(Make.Attribute(constant_x, "y", context=Make.Load()), "z", context=Make.Load()), patterns=[], kwd_attrs=[], kwd_patterns=[]),
		Make.MatchClass(name_carter, patterns=[], kwd_attrs=["True"], kwd_patterns=[pattern_1]),
		Make.MatchClass(name_carter, patterns=[], kwd_attrs=[], kwd_patterns=[pattern_1]),
		Make.MatchClass(name_carter, patterns=[Make.MatchSingleton("string")], kwd_attrs=[], kwd_patterns=[]),
		Make.MatchClass(name_carter, patterns=[Make.MatchStar()], kwd_attrs=[], kwd_patterns=[]),
		Make.MatchClass(name_carter, patterns=[], kwd_attrs=[], kwd_patterns=[Make.MatchStar()]),
		Make.MatchClass(
			constant_true,  # invalid name
			patterns=[],
			kwd_attrs=["True"],
			kwd_patterns=[pattern_1],
		),
		Make.MatchSequence([Make.MatchStar("True")]),
		Make.MatchAs(name="False"),
		Make.MatchOr([]),
		Make.MatchOr([pattern_1]),
		Make.MatchOr([pattern_1, pattern_x, Make.MatchSingleton("xxx")]),
		Make.MatchAs(name="_"),
		Make.MatchStar(name="x"),
		Make.MatchSequence([Make.MatchStar("_")]),
		Make.MatchMapping([], [], rest="_"),
	]

	def test_match_validation_pattern(self) -> None:
		name_x: ast.Name = Make.Name("x", Make.Load())
		for pattern in self._MATCH_PATTERNS:
			with self.subTest(dump(pattern, indent=4)):
				node = Make.Match(
					subject=name_x,
					cases=[Make.match_case(pattern=pattern, body=[Make.Pass()])],
				)
				node = fix_missing_locations(node)
				module = Make.Module([node], [])
				with self.assertRaises(ValueError):
					compile(module, "<test>", "exec")
class ConstantTests(unittest.TestCase):
	"""Tests on the ast.Constant node type."""

	def compile_constant(self, value: ConstantValueType) -> ConstantValueType:
		tree: ast.Module = parse("x = 123")
		node: ast.Constant = cast("ast.Constant", tree.body[0].value)
		new_node: ast.Constant = Make.Constant(value=value)
		ast.copy_location(new_node, node)
		tree.body[0].value = new_node

		code = compile(tree, "<string>", "exec")

		namespace = {}
		exec(code, namespace)  # noqa: S102
		return namespace["x"]

	def test_validation(self) -> None:
		with self.assertRaises(TypeError) as cm:
			self.compile_constant([1, 2, 3])
		self.assertEqual(str(cm.exception), "got an invalid type in Constant: list")

	def test_singletons(self) -> None:
		for const in (None, False, True, Ellipsis, b"", frozenset()):
			with self.subTest(const=const):
				value = self.compile_constant(const)
				self.assertIs(value, const)

	def test_values(self) -> None:
		nested_tuple = (1,)
		nested_frozenset = frozenset({1})
		for _level in range(3):
			nested_tuple = (nested_tuple, 2)
			nested_frozenset = frozenset({nested_frozenset, 2})
		values = (
			123,
			123.0,
			123j,
			"unicode",
			b"bytes",
			tuple("tuple"),
			frozenset("frozenset"),
			nested_tuple,
			nested_frozenset,
		)
		for value in values:
			with self.subTest(value=value):
				result = self.compile_constant(value)
				self.assertEqual(result, value)

	def test_assign_to_constant(self) -> None:
		tree = parse("x = 1")

		target = tree.body[0].targets[0]
		new_target = Make.Constant(value=1)
		ast.copy_location(new_target, target)
		tree.body[0].targets[0] = new_target

		with self.assertRaises(ValueError) as cm:
			compile(tree, "string", "exec")
		self.assertEqual(
			str(cm.exception),
			"expression which can't be assigned to in Store context",
		)

	def test_string_kind(self) -> None:
		c = parse('"x"', mode="eval").body
		self.assertEqual(c.value, "x")
		self.assertEqual(c.kind, None)

		c = parse('u"x"', mode="eval").body
		self.assertEqual(c.value, "x")
		self.assertEqual(c.kind, "u")

		c = parse('r"x"', mode="eval").body
		self.assertEqual(c.value, "x")
		self.assertEqual(c.kind, None)

		c = parse('b"x"', mode="eval").body
		self.assertEqual(c.value, b"x")
		self.assertEqual(c.kind, None)

class BaseNodeVisitorCases:
	pass

class NodeVisitorTests(BaseNodeVisitorCases, unittest.TestCase):
	visitor_class = ast.NodeVisitor

class NodeTransformerTests(ASTTestMixin, BaseNodeVisitorCases, unittest.TestCase):
	visitor_class = ast.NodeTransformer

	def assertASTTransformation(
		self,
		transformer_class: type[ast.NodeTransformer],
		initial_code: str,
		expected_code: str,
	) -> None:
		initial_ast = parse(dedent(initial_code))
		expected_ast = parse(dedent(expected_code))

		transformer = transformer_class()
		result_ast = fix_missing_locations(transformer.visit(initial_ast))

		self.assertASTEqual(result_ast, expected_ast)

	def test_node_remove_single(self) -> None:
		code = "def func(arg) -> SomeType: ..."
		expected = "def func(arg): ..."

		class SomeTypeRemover(ast.NodeTransformer):
			def visit_Name(self, node: ast.Name) -> None | ast.Name:
				self.generic_visit(node)
				if node.id == "SomeType":
					return None
				return node

		self.assertASTTransformation(SomeTypeRemover, code, expected)

	def test_node_remove_from_list(self) -> None:
		code = """
		def func(arg):
			print(arg)
			yield arg
		"""
		expected = """
		def func(arg):
			print(arg)
		"""

		class YieldRemover(ast.NodeTransformer):
			def visit_Expr(self, node: ast.Expr) -> None | ast.Expr:
				self.generic_visit(node)
				if isinstance(node.value, ast.Yield):
					return None
				return node

		self.assertASTTransformation(YieldRemover, code, expected)

	def test_node_return_list(self) -> None:
		code = """
		class DSL(Base, kw1=True): ...
		"""
		expected = """
		class DSL(Base, kw1=True, kw2=True, kw3=False): ...
		"""

		class ExtendKeywords(ast.NodeTransformer):
			def visit_keyword(self, node: ast.keyword) -> list[ast.keyword] | ast.keyword:
				self.generic_visit(node)
				if node.arg == "kw1":
					return [
						node,
						Make.keyword("kw2", Make.Constant(True)),
						Make.keyword("kw3", Make.Constant(False)),
					]
				return node

		self.assertASTTransformation(ExtendKeywords, code, expected)

	def test_node_mutate(self) -> None:
		code = """
		def func(arg):
			print(arg)
		"""
		expected = """
		def func(arg):
			log(arg)
		"""

		class PrintToLog(ast.NodeTransformer):
			def visit_Call(self, node: ast.Call) -> ast.Call:
				self.generic_visit(node)
				if isinstance(node.func, ast.Name) and node.func.id == "print":
					node.func.id = "log"
				return node

		self.assertASTTransformation(PrintToLog, code, expected)

	def test_node_replace(self) -> None:
		code = """
		def func(arg):
			print(arg)
		"""
		expected = """
		def func(arg):
			logger.log(arg, debug=True)
		"""

		class PrintToLog(ast.NodeTransformer):
			def visit_Call(self, node: ast.Call) -> ast.Call:
				self.generic_visit(node)
				if isinstance(node.func, ast.Name) and node.func.id == "print":
					return Make.Call(
						callee=Make.Attribute(
							Make.Name("logger", context=Make.Load()),
							"log",
							context=Make.Load(),
						),
						listParameters=node.args,
						list_keyword=[Make.keyword("debug", Make.Constant(True))],
					)
				return node

		self.assertASTTransformation(PrintToLog, code, expected)

def compare(left: ast.AST, right: ast.AST) -> bool:
	return dump(left) == dump(right)

class ASTOptimizationTests(unittest.TestCase):
	binop: ClassVar[dict[str, ast.operator]] = {
		"+": Make.Add(),
		"-": Make.Sub(),
		"*": Make.Mult(),
		"/": Make.Div(),
		"%": Make.Mod(),
		"<<": Make.LShift(),
		">>": Make.RShift(),
		"|": Make.BitOr(),
		"^": Make.BitXor(),
		"&": Make.BitAnd(),
		"//": Make.FloorDiv(),
		"**": Make.Pow(),
	}

	unaryop: ClassVar[dict[str, ast.unaryop]] = {
		"~": Make.Invert(),
		"+": Make.UAdd(),
		"-": Make.USub(),
	}

	def wrap_expr(self, expr: ast.expr) -> ast.Module:
		return Make.Module(body=[Make.Expr(value=expr)])

	def wrap_statement(self, statement: ast.stmt) -> ast.Module:
		return Make.Module(body=[statement])

	def assert_ast(self, code: str, non_optimized_target: ast.AST, optimized_target: ast.AST) -> None:
		non_optimized_tree = parse(code, optimize=-1)
		optimized_tree = parse(code, optimize=1)

		# Is a non-optimized tree equal to a non-optimized target?
		self.assertTrue(
			compare(non_optimized_tree, non_optimized_target),
			f"{dump(non_optimized_target)} must equal "
			f"{dump(non_optimized_tree)}",
		)

		# Is a optimized tree equal to a non-optimized target?
		self.assertFalse(
			compare(optimized_tree, non_optimized_target),
			f"{dump(non_optimized_target)} must not equal "
			f"{dump(non_optimized_tree)}"
		)

		# Is a optimized tree is equal to an optimized target?
		self.assertTrue(
			compare(optimized_tree,  optimized_target),
			f"{dump(optimized_target)} must equal "
			f"{dump(optimized_tree)}",
		)

	def create_binop(self, operand: str, left:ast.expr=Make.Constant(1), right:ast.expr=Make.Constant(1)) -> ast.BinOp:  # noqa: B008
			return Make.BinOp(left=left, op=self.binop[operand], right=right)

	def test_folding_binop(self) -> None:
		code = "1 %s 1"
		operators = self.binop.keys()

		for op in operators:
			result_code = code % op
			non_optimized_target = self.wrap_expr(self.create_binop(op))
			optimized_target = self.wrap_expr(Make.Constant(value=eval(result_code)))  # noqa: S307

			with self.subTest(
				result_code=result_code,
				non_optimized_target=non_optimized_target,
				optimized_target=optimized_target
			):
				self.assert_ast(result_code, non_optimized_target, optimized_target)

		# Multiplication of constant tuples must be folded
		code = "(1,) * 3"
		non_optimized_target = self.wrap_expr(self.create_binop("*", Make.Tuple(listElements=[Make.Constant(value=1)]), Make.Constant(value=3)))
		optimized_target = self.wrap_expr(Make.Constant(eval(code)))  # noqa: S307

		self.assert_ast(code, non_optimized_target, optimized_target)

	def test_folding_unaryop(self) -> None:
		code = "%s1"
		operators = self.unaryop.keys()

		def create_unaryop(operand: str) -> ast.UnaryOp:
			return Make.UnaryOp(op=self.unaryop[operand], operand=Make.Constant(1))

		for op in operators:
			result_code = code % op
			non_optimized_target = self.wrap_expr(create_unaryop(op))
			optimized_target = self.wrap_expr(Make.Constant(eval(result_code)))  # noqa: S307

			with self.subTest(
				result_code=result_code,
				non_optimized_target=non_optimized_target,
				optimized_target=optimized_target
			):
				self.assert_ast(result_code, non_optimized_target, optimized_target)

	def test_folding_not(self) -> None:
		code = "not (1 %s (1,))"
		operators = {
			"in": Make.In(),
			"is": Make.Is(),
		}
		opt_operators = {
			"is": Make.IsNot(),
			"in": Make.NotIn(),
		}

		def create_notop(operand: str) -> ast.UnaryOp:
			return Make.UnaryOp(op=Make.Not(), operand=Make.Compare(
				left=Make.Constant(value=1),
				ops=[operators[operand]],
				comparators=[Make.Tuple(listElements=[Make.Constant(value=1)])]
			))

		for op in operators:
			result_code = code % op
			non_optimized_target = self.wrap_expr(create_notop(op))
			optimized_target = self.wrap_expr(
				Make.Compare(left=Make.Constant(1), ops=[opt_operators[op]], comparators=[Make.Constant(value=(1,))])
			)

			with self.subTest(
				result_code=result_code,
				non_optimized_target=non_optimized_target,
				optimized_target=optimized_target
			):
				self.assert_ast(result_code, non_optimized_target, optimized_target)

	def test_folding_format(self) -> None:
		code = "'%s' % (a,)"

		non_optimized_target = self.wrap_expr(
			Make.BinOp(
				left=Make.Constant(value="%s"),
				op=Make.Mod(),
				right=Make.Tuple(listElements=[Make.Name(id='a')]))
		)
		optimized_target = self.wrap_expr(
			Make.JoinedStr(
				values=[
					Make.FormattedValue(value=Make.Name(id='a'), conversion=115)
				]
			)
		)

		self.assert_ast(code, non_optimized_target, optimized_target)

	def test_folding_tuple(self) -> None:
		code = "(1,)"

		non_optimized_target = self.wrap_expr(Make.Tuple(listElements=[Make.Constant(1)]))
		optimized_target = self.wrap_expr(Make.Constant(value=(1,)))

		self.assert_ast(code, non_optimized_target, optimized_target)

	def test_folding_comparator(self) -> None:
		code = "1 %s %s1%s"
		operators = [("in", Make.In()), ("not in", Make.NotIn())]
		braces = [
			("[", "]", ast.List, (1,)),
			("{", "}", ast.Set, frozenset({1})),
		]
		for left, right, non_optimized_comparator, optimized_comparator in braces:
			for op, node in operators:
				non_optimized_target = self.wrap_expr(Make.Compare(
					left=Make.Constant(1), ops=[node],
					comparators=[non_optimized_comparator(elts=[Make.Constant(1)])]
				))
				optimized_target = self.wrap_expr(Make.Compare(
					left=Make.Constant(1), ops=[node],
					comparators=[Make.Constant(value=optimized_comparator)]
				))
				self.assert_ast(code % (op, left, right), non_optimized_target, optimized_target)

	def test_folding_iter(self) -> None:
		code = "for _ in %s1%s: pass"
		braces = [
			("[", "]", ast.List, (1,)),
			("{", "}", ast.Set, frozenset({1})),
		]

		for left, right, ast_cls, optimized_iter in braces:
			non_optimized_target = self.wrap_statement(Make.For(
				target=Make.Name(id="_", context=Make.Store()),
				iter=ast_cls(elts=[Make.Constant(1)]),
				body=[Make.Pass()]
			))
			optimized_target = self.wrap_statement(Make.For(
				target=Make.Name(id="_", context=Make.Store()),
				iter=Make.Constant(value=optimized_iter),
				body=[Make.Pass()]
			))

			self.assert_ast(code % (left, right), non_optimized_target, optimized_target)

	def test_folding_subscript(self) -> None:
		code = "(1,)[0]"

		non_optimized_target = self.wrap_expr(
			Make.Subscript(value=Make.Tuple(listElements=[Make.Constant(value=1)]), slice=Make.Constant(value=0))
		)
		optimized_target = self.wrap_expr(Make.Constant(value=1))

		self.assert_ast(code, non_optimized_target, optimized_target)

	def test_folding_type_param_in_function_def(self) -> None:
		code = "def foo[%s = 1 + 1](): pass"

		unoptimized_binop = self.create_binop("+")
		unoptimized_type_params = [
			("T", "T", ast.TypeVar),
			("**P", "P", ast.ParamSpec),
			("*Ts", "Ts", ast.TypeVarTuple),
		]

		for theType, name, type_param in unoptimized_type_params:
			result_code = code % theType
			optimized_target = self.wrap_statement(Make.FunctionDef(name='foo', argumentSpecification=Make.arguments(), body=[Make.Pass()], type_params=[type_param(name=name, default_value=Make.Constant(2))]))
			non_optimized_target = self.wrap_statement(Make.FunctionDef(name='foo', argumentSpecification=Make.arguments(), body=[Make.Pass()], type_params=[type_param(name=name, default_value=unoptimized_binop)]))
			self.assert_ast(result_code, non_optimized_target, optimized_target)

	def test_folding_type_param_in_class_def(self) -> None:
		code = "class foo[%s = 1 + 1]: pass"

		unoptimized_binop = self.create_binop("+")
		unoptimized_type_params = [
			("T", "T", ast.TypeVar),
			("**P", "P", ast.ParamSpec),
			("*Ts", "Ts", ast.TypeVarTuple),
		]

		for theType, name, type_param in unoptimized_type_params:
			result_code = code % theType
			optimized_target = self.wrap_statement(Make.ClassDef(name='foo', body=[Make.Pass()], type_params=[type_param(name=name, default_value=Make.Constant(2))]))
			non_optimized_target = self.wrap_statement(Make.ClassDef(name='foo', body=[Make.Pass()], type_params=[type_param(name=name, default_value=unoptimized_binop)]))
			self.assert_ast(result_code, non_optimized_target, optimized_target)

	def test_folding_type_param_in_type_alias(self) -> None:
		code = "type foo[%s = 1 + 1] = 1"

		unoptimized_binop = self.create_binop("+")
		unoptimized_type_params = [
			("T", "T", ast.TypeVar),
			("**P", "P", ast.ParamSpec),
			("*Ts", "Ts", ast.TypeVarTuple),
		]

		for theType, name, type_param in unoptimized_type_params:
			result_code = code % theType
			optimized_target = self.wrap_statement(Make.TypeAlias(name=Make.Name(id='foo', context=Make.Store()), type_params=[type_param(name=name, default_value=Make.Constant(2))], value=Make.Constant(value=1)))
			non_optimized_target = self.wrap_statement(Make.TypeAlias(name=Make.Name(id='foo', context=Make.Store()), type_params=[type_param(name=name, default_value=unoptimized_binop)], value=Make.Constant(value=1)))
			self.assert_ast(result_code, non_optimized_target, optimized_target)

if __name__ == "__main__":
	unittest.main()
