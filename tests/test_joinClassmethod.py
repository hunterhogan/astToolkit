from astToolkit import ast_attributes, Make
from collections.abc import Callable
from typing import cast
import ast
import pytest

constant_expression_5 = Make.Constant(5)
constant_expression_7 = Make.Constant(7)
constant_expression_11 = Make.Constant(11)

keyword_arguments_set_A: ast_attributes = {"lineno": 3, "col_offset": 8, "end_lineno": 3, "end_col_offset": 12}
keyword_arguments_set_B: ast_attributes = {"lineno": 17, "col_offset": 19, "end_lineno": 17, "end_col_offset": 25}


def construct_expected_ast_node(ast_operator_type: type[ast.operator], input_expressions_iterable: list[ast.expr], keyword_arguments_for_operation: ast_attributes) -> ast.expr:
    processed_expressions_list = list(input_expressions_iterable)
    if not processed_expressions_list:
        return Make.Constant('', **keyword_arguments_for_operation)

    current_joined_expression = processed_expressions_list[0]
    for next_expression_to_join in processed_expressions_list[1:]:
        current_joined_expression = ast.BinOp(
            left=current_joined_expression,
            op=ast_operator_type(),
            right=next_expression_to_join,
            **keyword_arguments_for_operation
        )
    return current_joined_expression

listBoolOpIdentifiers: list[str] = sorted([subclass.__name__ for subclass in ast.boolop.__subclasses__()])
listOperatorIdentifiers: list[str] = sorted([subclass.__name__ for subclass in ast.operator.__subclasses__()])

listBoolOpJoinImplementationAndAstPairs = [
    (Make.__dict__[identifier], ast.__dict__[identifier])
    for identifier in listBoolOpIdentifiers
    if identifier in Make.__dict__
]

listOperatorJoinImplementationAndAstPairs = [
    (Make.__dict__[identifier], ast.__dict__[identifier])
    for identifier in listOperatorIdentifiers
    if identifier in Make.__dict__
]

list_join_method_test_scenarios_params: list[object] = []
raw_scenarios: list[tuple[str, list[ast.expr], ast_attributes]] = [
    ("empty_list_no_kwargs", [], {}),
    ("empty_list_with_kwargs", [], keyword_arguments_set_A),
    ("single_expr_no_kwargs", [constant_expression_5], {}),
    ("single_expr_with_kwargs", [constant_expression_5], keyword_arguments_set_A),
    ("two_exprs_no_kwargs", [constant_expression_5, constant_expression_7], {}),
    ("two_exprs_with_kwargs", [constant_expression_5, constant_expression_7], keyword_arguments_set_A),
    ("three_exprs_no_kwargs", [constant_expression_5, constant_expression_7, constant_expression_11], {}),
    ("three_exprs_with_kwargs", [constant_expression_5, constant_expression_7, constant_expression_11], keyword_arguments_set_B),
    (
        "single_expr_with_internal_attrs_and_kwargs",
        [Make.Constant(13, lineno=23, col_offset=29, end_lineno=23, end_col_offset=35)],
        keyword_arguments_set_A,
    ),
    (
        "two_exprs_with_internal_attrs_and_kwargs",
        [
            Make.Constant(13, lineno=23, col_offset=29, end_lineno=23, end_col_offset=35),
            Make.Constant(31, lineno=37, col_offset=41, end_lineno=37, end_col_offset=47)
        ],
        keyword_arguments_set_A,
    )
]

for scenario_id, expressions, kwargs in raw_scenarios:
    # Create a builder that captures the specific expressions and kwargs for this scenario
    def builder(op_type: type[ast.operator], bound_expressions: list[ast.expr] = expressions, bound_kwargs: ast_attributes = kwargs):
        return construct_expected_ast_node(op_type, bound_expressions, bound_kwargs)
    list_join_method_test_scenarios_params.append(
        pytest.param(scenario_id, expressions, kwargs, builder, id=scenario_id)
    )


@pytest.mark.parametrize("JoinImplementerClass, ast_operator_type", listOperatorJoinImplementationAndAstPairs)
@pytest.mark.parametrize("scenario_identifier, expressions_for_join_method, keyword_arguments_for_join_method, expected_ast_constructor", list_join_method_test_scenarios_params)
def test_join_method(
    JoinImplementerClass: type,
    ast_operator_type: type[ast.operator],
    scenario_identifier: str,
    expressions_for_join_method: list[ast.expr],
    keyword_arguments_for_join_method: ast_attributes,
    expected_ast_constructor: Callable[[type[ast.operator]], ast.expr]

):
    join_method = getattr(JoinImplementerClass, 'join')
    actual_ast_node = cast(ast.expr, join_method(expressions_for_join_method, **keyword_arguments_for_join_method))
    expected_ast_node = expected_ast_constructor(ast_operator_type)

    dump_of_actual_ast_node = ast.dump(actual_ast_node)
    dump_of_expected_ast_node = ast.dump(expected_ast_node)

    assert dump_of_actual_ast_node == dump_of_expected_ast_node, (
        f"Test {scenario_identifier} for {JoinImplementerClass.__name__} failed.\n"
        f"Input expressions: {[ast.dump(expression_node) for expression_node in expressions_for_join_method]}\n"
        f"Input kwargs: {keyword_arguments_for_join_method}\n"
        f"Expected AST dump: {dump_of_expected_ast_node}\n"
        f"Actual AST dump: {dump_of_actual_ast_node}"
    )
