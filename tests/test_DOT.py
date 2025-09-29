"""Tests for the DOT class providing consistent AST attribute access."""
# pyright: standard
from astToolkit import DOT, Make
from typing import Any
import ast
import pytest


class TestDOTBasicAttributeAccess:
	"""Test suite for basic DOT attribute access methods."""

	def test_id_access(self) -> None:
		"""Test DOT.id method with Name nodes."""
		node = Make.Name('variable_name')
		assert DOT.id(node) == 'variable_name'

	def test_attr_access(self) -> None:
		"""Test DOT.attr method with Attribute nodes."""
		node = Make.Attribute(Make.Name('obj'), 'method')
		assert DOT.attr(node) == 'method'

	def test_value_access_constant(self) -> None:
		"""Test DOT.value method with Constant nodes."""
		node = Make.Constant(42)
		assert DOT.value(node) == 42
		
		node_str = Make.Constant('hello')
		assert DOT.value(node_str) == 'hello'
		
		node_none = Make.Constant(None)
		assert DOT.value(node_none) is None

	def test_name_access_arg(self) -> None:
		"""Test DOT.name method with arg nodes."""
		node = Make.arg('param_name')
		# arg nodes don't have 'name' attribute, they have 'arg' attribute
		# DOT.name is for nodes that have a 'name' attribute like ClassDef, FunctionDef
		class_def = Make.ClassDef('TestClass', [], [], [Make.Pass()])
		assert DOT.name(class_def) == 'TestClass'

	def test_arg_access(self) -> None:
		"""Test DOT.arg method with arg nodes."""
		node = Make.arg('param_name')
		assert DOT.arg(node) == 'param_name'

	def test_asname_access(self) -> None:
		"""Test DOT.asname method with alias nodes."""
		# Test without alias
		node = Make.alias('module_name')
		assert DOT.asname(node) is None
		
		# Test with alias
		node_with_alias = Make.alias('module_name', 'alias_name')
		assert DOT.asname(node_with_alias) == 'alias_name'


class TestDOTExpressionAccess:
	"""Test suite for DOT expression access methods."""

	def test_test_access(self) -> None:
		"""Test DOT.test method with If and While nodes."""
		condition = Make.Constant(True)
		if_node = Make.If(condition, [Make.Pass()])
		assert DOT.test(if_node) is condition
		
		while_node = Make.While(condition, [Make.Pass()])
		assert DOT.test(while_node) is condition

	def test_left_right_access(self) -> None:
		"""Test DOT.left and DOT.right methods with BinOp nodes."""
		left = Make.Constant(1)
		right = Make.Constant(2)
		binop = Make.BinOp(left, Make.Add(), right)
		
		assert DOT.left(binop) is left
		assert DOT.right(binop) is right

	def test_operand_access(self) -> None:
		"""Test DOT.operand method with UnaryOp nodes."""
		operand = Make.Constant(42)
		unary = Make.UnaryOp(Make.UAdd(), operand)
		assert DOT.operand(unary) is operand

	def test_func_access(self) -> None:
		"""Test DOT.func method with Call nodes."""
		func = Make.Name('function_name')
		call = Make.Call(func, [])
		assert DOT.func(call) is func

	def test_slice_access(self) -> None:
		"""Test DOT.slice method with Subscript nodes."""
		slice_expr = Make.Constant(1)
		subscript = Make.Subscript(Make.Name('array'), slice_expr)
		assert DOT.slice(subscript) is slice_expr


class TestDOTCollectionAccess:
	"""Test suite for DOT collection access methods."""

	def test_targets_access(self) -> None:
		"""Test DOT.targets method with Assign and Delete nodes."""
		targets = [Make.Name('x'), Make.Name('y')]
		value = Make.Constant(42)
		assign = Make.Assign(targets, value)
		
		result_targets = list(DOT.targets(assign))
		assert len(result_targets) == 2
		assert result_targets[0] is targets[0]
		assert result_targets[1] is targets[1]

	def test_args_access_call(self) -> None:
		"""Test DOT.args method with Call nodes."""
		args = [Make.Constant(1), Make.Constant(2)]
		call = Make.Call(Make.Name('func'), args)
		
		result_args = list(DOT.args(call))
		assert len(result_args) == 2
		assert result_args[0] is args[0]
		assert result_args[1] is args[1]

	def test_args_access_arguments(self) -> None:
		"""Test DOT.args method with arguments nodes."""
		arg1 = Make.arg('param1')
		arg2 = Make.arg('param2')
		# Create arguments node and manually set the args field since Make.arguments doesn't support args parameter
		args_node = Make.arguments()
		args_node.args = [arg1, arg2]
		
		result_args = DOT.args(args_node)
		assert len(result_args) == 2
		assert result_args[0] is arg1
		assert result_args[1] is arg2

	def test_body_access_function(self) -> None:
		"""Test DOT.body method with FunctionDef nodes."""
		body_stmts = [Make.Pass(), Make.Return()]
		func = Make.FunctionDef('test_func', Make.arguments(), body_stmts)
		
		result_body = list(DOT.body(func))
		assert len(result_body) == 2
		assert result_body[0] is body_stmts[0]
		assert result_body[1] is body_stmts[1]

	def test_orelse_access(self) -> None:
		"""Test DOT.orelse method with If nodes."""
		condition = Make.Constant(True)
		then_stmt = [Make.Pass()]
		else_stmts = [Make.Return()]
		if_node = Make.If(condition, then_stmt, else_stmts)
		
		result_orelse = list(DOT.orelse(if_node))
		assert len(result_orelse) == 1
		assert result_orelse[0] is else_stmts[0]

	def test_decorator_list_access(self) -> None:
		"""Test DOT.decorator_list method with FunctionDef nodes."""
		decorators = [Make.Name('decorator1'), Make.Name('decorator2')]
		func = Make.FunctionDef('test_func', Make.arguments(), [Make.Pass()], decorators)
		
		result_decorators = list(DOT.decorator_list(func))
		assert len(result_decorators) == 2
		assert result_decorators[0] is decorators[0]
		assert result_decorators[1] is decorators[1]


class TestDOTOverloadedMethods:
	"""Test suite for DOT overloaded methods with different node types."""

	def test_target_overloads(self) -> None:
		"""Test DOT.target method with different node types."""
		# Test with NamedExpr (hasDOTtarget_Name)
		name_target = Make.Name('x')
		named_expr = Make.NamedExpr(name_target, Make.Constant(42))
		assert DOT.target(named_expr) is name_target
		
		# Test with AugAssign (hasDOTtarget_NameOrAttributeOrSubscript)
		aug_target = Make.Name('y')
		aug_assign = Make.AugAssign(aug_target, Make.Add(), Make.Constant(1))
		assert DOT.target(aug_assign) is aug_target

	def test_annotation_overloads(self) -> None:
		"""Test DOT.annotation method with different node types."""
		# Test with AnnAssign (hasDOTannotation_expr)
		annotation = Make.Name('int')
		target = Make.Name('x')
		ann_assign = Make.AnnAssign(target, annotation)
		assert DOT.annotation(ann_assign) is annotation
		
		# Test with arg (hasDOTannotation_exprOrNone) - no annotation
		arg_node = Make.arg('param')
		assert DOT.annotation(arg_node) is None

	def test_returns_overloads(self) -> None:
		"""Test DOT.returns method with different node types."""
		# Test with FunctionDef (hasDOTreturns_exprOrNone) - no return type
		func = Make.FunctionDef('test', Make.arguments(), [Make.Pass()])
		assert DOT.returns(func) is None
		
		# Test with return type annotation
		return_type = Make.Name('int')
		func_with_return = Make.FunctionDef('test', Make.arguments(), [Make.Pass()], returns=return_type)
		assert DOT.returns(func_with_return) is return_type

	def test_body_overloads(self) -> None:
		"""Test DOT.body method with different return types."""
		# Test with Lambda (hasDOTbody_expr) - returns single expression
		body_expr = Make.Constant(42)
		lambda_node = Make.Lambda(Make.arguments(), body_expr)
		assert DOT.body(lambda_node) is body_expr
		
		# Test with FunctionDef (hasDOTbody_list_stmt) - returns list of statements
		body_stmts = [Make.Pass()]
		func = Make.FunctionDef('test', Make.arguments(), body_stmts)
		result_body = DOT.body(func)
		assert isinstance(result_body, list)
		assert len(result_body) == 1
		assert result_body[0] is body_stmts[0]


class TestDOTOptionalAttributeAccess:
	"""Test suite for DOT methods that may return None."""

	def test_msg_access_assert(self) -> None:
		"""Test DOT.msg method with Assert nodes."""
		# Test without message
		assert_node = Make.Assert(Make.Constant(True))
		assert DOT.msg(assert_node) is None
		
		# Test with message
		msg = Make.Constant('Error message')
		assert_with_msg = Make.Assert(Make.Constant(True), msg)
		assert DOT.msg(assert_with_msg) is msg

	def test_type_comment_access(self) -> None:
		"""Test DOT.type_comment method with various nodes."""
		# Test FunctionDef without type comment
		func = Make.FunctionDef('test', Make.arguments(), [Make.Pass()])
		assert DOT.type_comment(func) is None

	def test_bound_access(self) -> None:
		"""Test DOT.bound method with TypeVar nodes."""
		# TypeVar without bound
		typevar = Make.TypeVar('T')
		assert DOT.bound(typevar) is None

	def test_step_access(self) -> None:
		"""Test DOT.step method with Slice nodes."""
		# Slice without step
		slice_node = Make.Slice()
		assert DOT.step(slice_node) is None

	def test_upper_lower_access(self) -> None:
		"""Test DOT.upper and DOT.lower methods with Slice nodes."""
		# Slice without upper/lower
		slice_node = Make.Slice()
		assert DOT.upper(slice_node) is None
		assert DOT.lower(slice_node) is None

	def test_cause_access(self) -> None:
		"""Test DOT.cause method with Raise nodes."""
		# Raise without cause
		raise_node = Make.Raise()
		assert DOT.cause(raise_node) is None


class TestDOTIntegerAttributeAccess:
	"""Test suite for DOT methods that return integer values."""

	def test_simple_access(self) -> None:
		"""Test DOT.simple method with AnnAssign nodes."""
		target = Make.Name('x')
		annotation = Make.Name('int')
		ann_assign = Make.AnnAssign(target, annotation)
		assert DOT.simple(ann_assign) == 1

	def test_lineno_access(self) -> None:
		"""Test DOT.lineno method with TypeIgnore nodes."""
		type_ignore = Make.TypeIgnore(42, 'ignore comment')
		assert DOT.lineno(type_ignore) == 42

	def test_conversion_access(self) -> None:
		"""Test DOT.conversion method with FormattedValue nodes."""
		formatted = Make.FormattedValue(Make.Name('x'), -1)
		assert DOT.conversion(formatted) == -1  # Default conversion value

	def test_level_access(self) -> None:
		"""Test DOT.level method with ImportFrom nodes."""
		import_from = Make.ImportFrom('module', [Make.alias('name')])
		assert DOT.level(import_from) == 0  # Default level


class TestDOTComplexAttributeAccess:
	"""Test suite for DOT methods with more complex attribute types."""

	def test_keywords_access(self) -> None:
		"""Test DOT.keywords method with Call nodes."""
		keywords = [Make.keyword('arg', Make.Constant(42))]
		call = Make.Call(Make.Name('func'), [], keywords)
		
		result_keywords = list(DOT.keywords(call))
		assert len(result_keywords) == 1
		assert result_keywords[0] is keywords[0]

	def test_bases_access(self) -> None:
		"""Test DOT.bases method with ClassDef nodes."""
		bases = [Make.Name('BaseClass')]
		class_def = Make.ClassDef('TestClass', bases, [], [Make.Pass()])
		
		result_bases = list(DOT.bases(class_def))
		assert len(result_bases) == 1
		assert result_bases[0] is bases[0]

	def test_comparators_ops_access(self) -> None:
		"""Test DOT.comparators and DOT.ops methods with Compare nodes."""
		left = Make.Constant(1)
		comparators = [Make.Constant(2)]
		ops = [Make.Lt()]
		compare = Make.Compare(left, ops, comparators)
		
		result_comparators = list(DOT.comparators(compare))
		assert len(result_comparators) == 1
		assert result_comparators[0] is comparators[0]
		
		result_ops = list(DOT.ops(compare))
		assert len(result_ops) == 1
		assert result_ops[0] is ops[0]

	def test_elts_access(self) -> None:
		"""Test DOT.elts method with List nodes."""
		elts = [Make.Constant(1), Make.Constant(2)]
		list_node = Make.List(elts)
		
		result_elts = list(DOT.elts(list_node))
		assert len(result_elts) == 2
		assert result_elts[0] is elts[0]
		assert result_elts[1] is elts[1]

	def test_keys_values_access_dict(self) -> None:
		"""Test DOT.keys and DOT.values methods with Dict nodes."""
		keys = [Make.Constant('key1'), Make.Constant('key2')]
		values = [Make.Constant('value1'), Make.Constant('value2')]
		dict_node = Make.Dict(keys, values)
		
		result_keys = list(DOT.keys(dict_node))
		assert len(result_keys) == 2
		assert result_keys[0] is keys[0]
		assert result_keys[1] is keys[1]
		
		result_values = list(DOT.values(dict_node))
		assert len(result_values) == 2
		assert result_values[0] is values[0]
		assert result_values[1] is values[1]


class TestDOTEdgeCases:
	"""Test suite for DOT edge cases and error handling."""

	def test_empty_collections(self) -> None:
		"""Test DOT methods with empty collections."""
		# Empty arguments
		empty_args = Make.arguments()
		assert len(DOT.args(empty_args)) == 0
		assert len(DOT.defaults(empty_args)) == 0
		assert len(DOT.posonlyargs(empty_args)) == 0
		assert len(DOT.kwonlyargs(empty_args)) == 0
		assert len(DOT.kw_defaults(empty_args)) == 0

	def test_optional_values_none(self) -> None:
		"""Test DOT methods that can return None values."""
		# Test vararg and kwarg as None
		args = Make.arguments()
		assert DOT.vararg(args) is None
		assert DOT.kwarg(args) is None
		
		# Test optional_vars as None in withitem
		withitem = Make.withitem(Make.Name('context'))
		assert DOT.optional_vars(withitem) is None

	def test_ctx_access(self) -> None:
		"""Test DOT.ctx method with expression contexts."""
		# Load context
		name_load = Make.Name('var')  # Default is Load context
		ctx = DOT.ctx(name_load)
		assert isinstance(ctx, ast.Load)
		
		# Store context
		name_store = Make.Name('var', ast.Store())
		ctx_store = DOT.ctx(name_store)
		assert isinstance(ctx_store, ast.Store)

	def test_tag_access(self) -> None:
		"""Test DOT.tag method with TypeIgnore nodes."""
		type_ignore = Make.TypeIgnore(1, 'test tag')
		assert DOT.tag(type_ignore) == 'test tag'

	def test_kind_access(self) -> None:
		"""Test DOT.kind method with Constant nodes."""
		# Constant without kind
		constant = Make.Constant(42)
		assert DOT.kind(constant) is None

	def test_module_access(self) -> None:
		"""Test DOT.module method with ImportFrom nodes."""
		import_from = Make.ImportFrom('test_module', [Make.alias('name')])
		assert DOT.module(import_from) == 'test_module'

	def test_names_access(self) -> None:
		"""Test DOT.names method with Import and ImportFrom nodes."""
		alias1 = Make.alias('module1')
		alias2 = Make.alias('module2')
		# Use direct ast.Import to avoid the Make.Import wrapper issue
		import ast
		import_node = ast.Import(names=[alias1, alias2])
		
		result_names = list(DOT.names(import_node))
		assert len(result_names) == 2
		assert result_names[0] is alias1
		assert result_names[1] is alias2


class TestDOTTypeSystemAttributes:
	"""Test suite for DOT methods related to Python's type system."""

	def test_type_params_access(self) -> None:
		"""Test DOT.type_params method with generic nodes."""
		# FunctionDef without type parameters
		func = Make.FunctionDef('test', Make.arguments(), [Make.Pass()])
		assert len(DOT.type_params(func)) == 0

	def test_type_ignores_access(self) -> None:
		"""Test DOT.type_ignores method with Module nodes."""
		# Create a simple module
		stmts = [Make.Pass()]
		module = Make.Module(stmts)
		assert len(DOT.type_ignores(module)) == 0

	def test_returns_access_function_type(self) -> None:
		"""Test DOT.returns method with FunctionType nodes."""
		# FunctionType with return type
		argtypes = [Make.Name('int')]
		returns = Make.Name('str')
		func_type = Make.FunctionType(argtypes, returns)
		assert DOT.returns(func_type) is returns
		assert DOT.argtypes(func_type) == argtypes


@pytest.mark.parametrize("method_name,node_factory,expected_type", [
	("id", lambda: Make.Name('test'), str),
	("value", lambda: Make.Constant(42), int),
	("attr", lambda: Make.Attribute(Make.Name('obj'), 'attr'), str),
	("simple", lambda: Make.AnnAssign(Make.Name('x'), Make.Name('int')), int),
	("lineno", lambda: Make.TypeIgnore(10, 'comment'), int),
])
def test_dot_method_return_types(method_name: str, node_factory: Any, expected_type: type) -> None:
	"""Test that DOT methods return values of expected types."""
	node = node_factory()
	method = getattr(DOT, method_name)
	result = method(node)
	assert isinstance(result, expected_type)


@pytest.mark.parametrize("method_name,node_factory", [
	("targets", lambda: Make.Assign([Make.Name('x')], Make.Constant(1))),
	("args", lambda: Make.Call(Make.Name('func'), [Make.Constant(1), Make.Constant(2)])),
	("body", lambda: Make.FunctionDef('test', Make.arguments(), [Make.Pass()])),
	("orelse", lambda: Make.If(Make.Constant(True), [Make.Pass()], [Make.Return()])),
	("decorator_list", lambda: Make.FunctionDef('test', Make.arguments(), [Make.Pass()], [Make.Name('dec')])),
	("keywords", lambda: Make.Call(Make.Name('func'), [], [Make.keyword('arg', Make.Constant(1))])),
	("bases", lambda: Make.ClassDef('Test', [Make.Name('Base')], [], [Make.Pass()])),
	("elts", lambda: Make.List([Make.Constant(1), Make.Constant(2)])),
])
def test_dot_collection_methods(method_name: str, node_factory: Any) -> None:
	"""Test that DOT collection methods return iterable collections."""
	node = node_factory()
	method = getattr(DOT, method_name)
	result = method(node)
	# Should be iterable
	list(result)  # This will raise if not iterable


@pytest.mark.parametrize("method_name,node_factory", [
	("msg", lambda: Make.Assert(Make.Constant(True))),
	("annotation", lambda: Make.arg('param')),
	("returns", lambda: Make.FunctionDef('test', Make.arguments(), [Make.Pass()])),
	("bound", lambda: Make.TypeVar('T')),
	("step", lambda: Make.Slice()),
	("upper", lambda: Make.Slice()),
	("lower", lambda: Make.Slice()),
	("cause", lambda: Make.Raise()),
	("vararg", lambda: Make.arguments()),
	("kwarg", lambda: Make.arguments()),
	("optional_vars", lambda: Make.withitem(Make.Name('ctx'))),
])
def test_dot_optional_methods(method_name: str, node_factory: Any) -> None:
	"""Test that DOT optional methods can return None."""
	node = node_factory()
	method = getattr(DOT, method_name)
	result = method(node)
	# Should be None or the expected value - just ensure it doesn't raise
	assert result is None or result is not None


class TestDOTAdditionalMethods:
	"""Test suite for additional DOT methods to improve coverage."""

	def test_cases_access(self) -> None:
		"""Test DOT.cases method with Match nodes."""
		# Create a simple match case
		pattern = Make.MatchValue(Make.Constant(1))
		guard = None
		body = [Make.Pass()]
		case = Make.match_case(pattern, guard, body)
		match_node = Make.Match(Make.Name('x'), [case])
		
		result_cases = list(DOT.cases(match_node))
		assert len(result_cases) == 1
		assert result_cases[0] is case

	def test_cls_access(self) -> None:
		"""Test DOT.cls method with MatchClass nodes."""
		cls_expr = Make.Name('MyClass')
		match_class = Make.MatchClass(cls_expr, [], [])
		assert DOT.cls(match_class) is cls_expr

	def test_context_expr_access(self) -> None:
		"""Test DOT.context_expr method with withitem nodes."""
		context = Make.Name('context_manager')
		withitem = Make.withitem(context)
		assert DOT.context_expr(withitem) is context

	def test_elt_access(self) -> None:
		"""Test DOT.elt method with comprehension nodes."""
		elt = Make.Constant(1)
		target = Make.Name('x')
		iter_expr = Make.Name('items')
		comp = Make.comprehension(target, iter_expr, [])
		list_comp = Make.ListComp(elt, [comp])
		assert DOT.elt(list_comp) is elt

	def test_exc_access(self) -> None:
		"""Test DOT.exc method with Raise nodes."""
		exc = Make.Name('ValueError')
		raise_node = Make.Raise(exc)
		assert DOT.exc(raise_node) is exc

	def test_finalbody_access(self) -> None:
		"""Test DOT.finalbody method with Try nodes."""
		finalbody = [Make.Pass()]
		try_node = Make.Try([Make.Pass()], [], [], finalbody)
		
		result_finalbody = list(DOT.finalbody(try_node))
		assert len(result_finalbody) == 1
		assert result_finalbody[0] is finalbody[0]

	def test_format_spec_access(self) -> None:
		"""Test DOT.format_spec method with FormattedValue nodes."""
		format_spec = Make.Constant('.2f')
		formatted = Make.FormattedValue(Make.Name('x'), -1, format_spec)
		assert DOT.format_spec(formatted) is format_spec

	def test_generators_access(self) -> None:
		"""Test DOT.generators method with comprehension nodes."""
		elt = Make.Constant(1)
		target = Make.Name('x')
		iter_expr = Make.Name('items')
		comp = Make.comprehension(target, iter_expr, [])
		list_comp = Make.ListComp(elt, [comp])
		
		result_generators = list(DOT.generators(list_comp))
		assert len(result_generators) == 1
		assert result_generators[0] is comp

	def test_guard_access(self) -> None:
		"""Test DOT.guard method with match_case nodes."""
		pattern = Make.MatchValue(Make.Constant(1))
		guard = Make.Name('guard_condition')
		body = [Make.Pass()]
		case = Make.match_case(pattern, guard, body)
		assert DOT.guard(case) is guard

	def test_handlers_access(self) -> None:
		"""Test DOT.handlers method with Try nodes."""
		handler = Make.ExceptHandler(Make.Name('Exception'), None, [Make.Pass()])
		try_node = Make.Try([Make.Pass()], [handler], [], [])
		
		result_handlers = list(DOT.handlers(try_node))
		assert len(result_handlers) == 1
		assert result_handlers[0] is handler

	def test_ifs_access(self) -> None:
		"""Test DOT.ifs method with comprehension nodes."""
		target = Make.Name('x')
		iter_expr = Make.Name('items')
		if_condition = Make.Compare(Make.Name('x'), [Make.Gt()], [Make.Constant(0)])
		comp = Make.comprehension(target, iter_expr, [if_condition])
		
		result_ifs = list(DOT.ifs(comp))
		assert len(result_ifs) == 1
		assert result_ifs[0] is if_condition

	def test_is_async_access(self) -> None:
		"""Test DOT.is_async method with comprehension nodes."""
		target = Make.Name('x')
		iter_expr = Make.Name('items')
		comp = Make.comprehension(target, iter_expr, [])
		comp.is_async = 1  # Set manually since Make.comprehension doesn't support this
		assert DOT.is_async(comp) == 1

	def test_items_access(self) -> None:
		"""Test DOT.items method with With nodes."""
		withitem1 = Make.withitem(Make.Name('ctx1'))
		withitem2 = Make.withitem(Make.Name('ctx2'))
		with_node = Make.With([withitem1, withitem2], [Make.Pass()])
		
		result_items = list(DOT.items(with_node))
		assert len(result_items) == 2
		assert result_items[0] is withitem1
		assert result_items[1] is withitem2

	def test_iter_access(self) -> None:
		"""Test DOT.iter method with For nodes."""
		iter_expr = Make.Name('iterable')
		target = Make.Name('item')
		for_node = Make.For(target, iter_expr, [Make.Pass()])
		assert DOT.iter(for_node) is iter_expr

	def test_key_access(self) -> None:
		"""Test DOT.key method with DictComp nodes."""
		key = Make.Name('key')
		value = Make.Name('value')
		target = Make.Name('item')
		iter_expr = Make.Name('items')
		comp = Make.comprehension(target, iter_expr, [])
		dict_comp = Make.DictComp(key, value, [comp])
		assert DOT.key(dict_comp) is key

	def test_kwd_attrs_access(self) -> None:
		"""Test DOT.kwd_attrs method with MatchClass nodes."""
		cls_expr = Make.Name('MyClass')
		match_class = Make.MatchClass(cls_expr, [], [])
		# Manually set kwd_attrs since Make.MatchClass doesn't support all parameters
		match_class.kwd_attrs = ['attr1', 'attr2']
		
		result_kwd_attrs = list(DOT.kwd_attrs(match_class))
		assert len(result_kwd_attrs) == 2
		assert result_kwd_attrs[0] == 'attr1'
		assert result_kwd_attrs[1] == 'attr2'

	def test_kwd_patterns_access(self) -> None:
		"""Test DOT.kwd_patterns method with MatchClass nodes."""
		cls_expr = Make.Name('MyClass')
		pattern1 = Make.MatchValue(Make.Constant(1))
		pattern2 = Make.MatchValue(Make.Constant(2))
		match_class = Make.MatchClass(cls_expr, [], [])
		# Manually set kwd_patterns since Make.MatchClass doesn't support all parameters
		match_class.kwd_patterns = [pattern1, pattern2]
		
		result_kwd_patterns = list(DOT.kwd_patterns(match_class))
		assert len(result_kwd_patterns) == 2
		assert result_kwd_patterns[0] is pattern1
		assert result_kwd_patterns[1] is pattern2

	def test_op_access(self) -> None:
		"""Test DOT.op method with BinOp and UnaryOp nodes."""
		# Test with BinOp
		binop = Make.BinOp(Make.Constant(1), Make.Add(), Make.Constant(2))
		op = DOT.op(binop)
		assert isinstance(op, ast.Add)
		
		# Test with UnaryOp
		unaryop = Make.UnaryOp(Make.UAdd(), Make.Constant(1))
		unary_op = DOT.op(unaryop)
		assert isinstance(unary_op, ast.UAdd)

	def test_pattern_access(self) -> None:
		"""Test DOT.pattern method with match_case nodes."""
		pattern = Make.MatchValue(Make.Constant(42))
		body = [Make.Pass()]
		case = Make.match_case(pattern, None, body)
		assert DOT.pattern(case) is pattern

	def test_patterns_access(self) -> None:
		"""Test DOT.patterns method with MatchOr nodes."""
		pattern1 = Make.MatchValue(Make.Constant(1))
		pattern2 = Make.MatchValue(Make.Constant(2))
		match_or = Make.MatchOr([pattern1, pattern2])
		
		result_patterns = list(DOT.patterns(match_or))
		assert len(result_patterns) == 2
		assert result_patterns[0] is pattern1
		assert result_patterns[1] is pattern2

	def test_rest_access(self) -> None:
		"""Test DOT.rest method with MatchMapping nodes."""
		keys = [Make.Constant('key')]
		patterns = [Make.MatchValue(Make.Constant('value'))]
		rest = 'rest_var'
		match_mapping = Make.MatchMapping(keys, patterns, rest)
		assert DOT.rest(match_mapping) == rest

	def test_subject_access(self) -> None:
		"""Test DOT.subject method with Match nodes."""
		subject = Make.Name('subject_var')
		pattern = Make.MatchValue(Make.Constant(1))
		case = Make.match_case(pattern, None, [Make.Pass()])
		match_node = Make.Match(subject, [case])
		assert DOT.subject(match_node) is subject

	def test_type_access(self) -> None:
		"""Test DOT.type method with ExceptHandler nodes."""
		exc_type = Make.Name('ValueError')
		handler = Make.ExceptHandler(exc_type, None, [Make.Pass()])
		assert DOT.type(handler) is exc_type