"""Tests for the IfThis class predicates."""

from astToolkit import Be, IfThis, Make
from tests.dataSamples.Make import allSubclasses
from typing import Any
import ast
import pytest


class TestIfThis:
    """Test suite for IfThis predicate functions."""

    def test_isIdentifier_positive(self) -> None:
        """Test isIdentifier with matching identifiers."""
        predicate = IfThis.isIdentifier("test_name")
        assert predicate("test_name") is True
        
        predicate_none = IfThis.isIdentifier(None)
        assert predicate_none(None) is True

    def test_isIdentifier_negative(self) -> None:
        """Test isIdentifier with non-matching identifiers."""
        predicate = IfThis.isIdentifier("test_name")
        assert predicate("different_name") is False
        assert predicate(None) is False
        
        predicate_none = IfThis.isIdentifier(None)
        assert predicate_none("some_name") is False

    def test_isConstant_value_positive(self) -> None:
        """Test isConstant_value with matching values."""
        # Test with integer constant
        constant_node = Make.Constant(42)
        predicate_int = IfThis.isConstant_value(42)
        assert predicate_int(constant_node) is True
        
        # Test with string constant
        constant_str = Make.Constant("hello")
        predicate_str = IfThis.isConstant_value("hello")
        assert predicate_str(constant_str) is True
        
        # Test with None constant
        constant_none = Make.Constant(None)
        predicate_none = IfThis.isConstant_value(None)
        assert predicate_none(constant_none) is True

    def test_isConstant_value_negative(self) -> None:
        """Test isConstant_value with non-matching values."""
        constant_node = Make.Constant(42)
        predicate = IfThis.isConstant_value(24)
        assert predicate(constant_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("test")
        assert predicate(name_node) is False

    def test_isNameIdentifier_positive(self) -> None:
        """Test isNameIdentifier with matching names."""
        name_node = Make.Name("test_var")
        predicate = IfThis.isNameIdentifier("test_var")
        assert predicate(name_node) is True

    def test_isNameIdentifier_negative(self) -> None:
        """Test isNameIdentifier with non-matching names."""
        name_node = Make.Name("test_var")
        predicate = IfThis.isNameIdentifier("different_var")
        assert predicate(name_node) is False
        
        # Test with wrong node type
        constant_node = Make.Constant(42)
        assert predicate(constant_node) is False

    def test_isFunctionDefIdentifier_positive(self) -> None:
        """Test isFunctionDefIdentifier with matching function names."""
        func_node = Make.FunctionDef(name="my_function")
        predicate = IfThis.isFunctionDefIdentifier("my_function")
        assert predicate(func_node) is True

    def test_isFunctionDefIdentifier_negative(self) -> None:
        """Test isFunctionDefIdentifier with non-matching function names."""
        func_node = Make.FunctionDef(name="my_function")
        predicate = IfThis.isFunctionDefIdentifier("other_function")
        assert predicate(func_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("my_function")
        assert predicate(name_node) is False

    def test_isClassDefIdentifier_positive(self) -> None:
        """Test isClassDefIdentifier with matching class names."""
        class_node = Make.ClassDef(name="MyClass")
        predicate = IfThis.isClassDefIdentifier("MyClass")
        assert predicate(class_node) is True

    def test_isClassDefIdentifier_negative(self) -> None:
        """Test isClassDefIdentifier with non-matching class names."""
        class_node = Make.ClassDef(name="MyClass")
        predicate = IfThis.isClassDefIdentifier("OtherClass")
        assert predicate(class_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("MyClass")
        assert predicate(name_node) is False

    def test_isCallIdentifier_positive(self) -> None:
        """Test isCallIdentifier with matching function call names."""
        call_node = Make.Call(callee=Make.Name("print"))
        predicate = IfThis.isCallIdentifier("print")
        assert predicate(call_node) is True

    def test_isCallIdentifier_negative(self) -> None:
        """Test isCallIdentifier with non-matching function call names."""
        call_node = Make.Call(callee=Make.Name("print"))
        predicate = IfThis.isCallIdentifier("input")
        assert predicate(call_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("print")
        assert predicate(name_node) is False

    def test_isAttributeNamespaceIdentifier_positive(self) -> None:
        """Test isAttributeNamespaceIdentifier with matching namespace and identifier."""
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        predicate = IfThis.isAttributeNamespaceIdentifier("obj", "method")
        assert predicate(attr_node) is True

    def test_isAttributeNamespaceIdentifier_negative(self) -> None:
        """Test isAttributeNamespaceIdentifier with non-matching namespace or identifier."""
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        predicate_wrong_ns = IfThis.isAttributeNamespaceIdentifier("other_obj", "method")
        assert predicate_wrong_ns(attr_node) is False
        
        predicate_wrong_attr = IfThis.isAttributeNamespaceIdentifier("obj", "other_method")
        assert predicate_wrong_attr(attr_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("obj")
        predicate = IfThis.isAttributeNamespaceIdentifier("obj", "method")
        assert predicate(name_node) is False

    def test_isCallAttributeNamespaceIdentifier_positive(self) -> None:
        """Test isCallAttributeNamespaceIdentifier with matching calls."""
        call_node = Make.Call(callee=Make.Attribute(Make.Name("obj"), "method"))
        predicate = IfThis.isCallAttributeNamespaceIdentifier("obj", "method")
        assert predicate(call_node) is True

    def test_isCallAttributeNamespaceIdentifier_negative(self) -> None:
        """Test isCallAttributeNamespaceIdentifier with non-matching calls."""
        call_node = Make.Call(callee=Make.Attribute(Make.Name("obj"), "method"))
        predicate = IfThis.isCallAttributeNamespaceIdentifier("other_obj", "method")
        assert predicate(call_node) is False
        
        # Test with wrong node type
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        assert predicate(attr_node) is False

    def test_is_argIdentifier_positive(self) -> None:
        """Test is_argIdentifier with matching argument names."""
        arg_node = Make.arg("param_name")
        predicate = IfThis.is_argIdentifier("param_name")
        assert predicate(arg_node) is True

    def test_is_argIdentifier_negative(self) -> None:
        """Test is_argIdentifier with non-matching argument names."""
        arg_node = Make.arg("param_name")
        predicate = IfThis.is_argIdentifier("other_param")
        assert predicate(arg_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("param_name")
        assert predicate(name_node) is False

    def test_is_keywordIdentifier_positive(self) -> None:
        """Test is_keywordIdentifier with matching keyword argument names."""
        keyword_node = Make.keyword("key", Make.Constant("value"))
        predicate = IfThis.is_keywordIdentifier("key")
        assert predicate(keyword_node) is True
        
        # Test with None keyword
        keyword_none = Make.keyword(None, Make.Constant("value"))
        predicate_none = IfThis.is_keywordIdentifier(None)
        assert predicate_none(keyword_none) is True

    def test_is_keywordIdentifier_negative(self) -> None:
        """Test is_keywordIdentifier with non-matching keyword argument names."""
        keyword_node = Make.keyword("key", Make.Constant("value"))
        predicate = IfThis.is_keywordIdentifier("other_key")
        assert predicate(keyword_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("key")
        assert predicate(name_node) is False

    def test_isAssignAndTargets0Is_positive(self) -> None:
        """Test isAssignAndTargets0Is with matching assignment target."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        target_predicate = lambda node: Be.Name(node) and node.id == "x"
        predicate = IfThis.isAssignAndTargets0Is(target_predicate)
        assert predicate(assign_node) is True

    def test_isAssignAndTargets0Is_negative(self) -> None:
        """Test isAssignAndTargets0Is with non-matching assignment target."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        target_predicate = lambda node: Be.Name(node) and node.id == "y"
        predicate = IfThis.isAssignAndTargets0Is(target_predicate)
        assert predicate(assign_node) is False
        
        # Test with wrong node type
        name_node = Make.Name("x")
        assert predicate(name_node) is False

    def test_isAllOf_positive(self) -> None:
        """Test isAllOf with all predicates matching."""
        name_node = Make.Name("test_var")
        predicate1 = Be.Name
        predicate2 = lambda node: hasattr(node, 'id') and node.id == "test_var"
        combined = IfThis.isAllOf(predicate1, predicate2)
        assert combined(name_node) is True

    def test_isAllOf_negative(self) -> None:
        """Test isAllOf with some predicates not matching."""
        name_node = Make.Name("test_var")
        predicate1 = Be.Name
        predicate2 = lambda node: hasattr(node, 'id') and node.id == "other_var"
        combined = IfThis.isAllOf(predicate1, predicate2)
        assert combined(name_node) is False

    def test_isAnyOf_positive(self) -> None:
        """Test isAnyOf with at least one predicate matching."""
        name_node = Make.Name("test_var")
        predicate1 = Be.Constant  # This will be False
        predicate2 = Be.Name      # This will be True
        combined = IfThis.isAnyOf(predicate1, predicate2)
        assert combined(name_node) is True

    def test_isAnyOf_negative(self) -> None:
        """Test isAnyOf with no predicates matching."""
        name_node = Make.Name("test_var")
        predicate1 = Be.Constant
        predicate2 = Be.FunctionDef
        combined = IfThis.isAnyOf(predicate1, predicate2)
        assert combined(name_node) is False

    def test_isAttributeIdentifier_positive(self) -> None:
        """Test isAttributeIdentifier with matching nested identifier."""
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        predicate = IfThis.isAttributeIdentifier("obj")
        assert predicate(attr_node) is True

    def test_isAttributeIdentifier_negative(self) -> None:
        """Test isAttributeIdentifier with non-matching nested identifier."""
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        predicate = IfThis.isAttributeIdentifier("other_obj")
        assert predicate(attr_node) is False

    def test_isAttributeName_positive(self) -> None:
        """Test isAttributeName with Attribute node containing Name value."""
        attr_node = Make.Attribute(Make.Name("obj"), "method")
        assert IfThis.isAttributeName(attr_node) is True

    def test_isAttributeName_negative(self) -> None:
        """Test isAttributeName with wrong node types."""
        # Wrong node type
        name_node = Make.Name("obj")
        assert IfThis.isAttributeName(name_node) is False
        
        # Attribute with non-Name value
        attr_node = Make.Attribute(Make.Constant(42), "method")
        assert IfThis.isAttributeName(attr_node) is False

    def test_isCallToName_positive(self) -> None:
        """Test isCallToName with Call node containing Name function."""
        call_node = Make.Call(callee=Make.Name("print"))
        assert IfThis.isCallToName(call_node) is True

    def test_isCallToName_negative(self) -> None:
        """Test isCallToName with wrong node types."""
        # Wrong node type
        name_node = Make.Name("print")
        assert IfThis.isCallToName(name_node) is False
        
        # Call with non-Name function
        call_node = Make.Call(callee=Make.Attribute(Make.Name("obj"), "method"))
        assert IfThis.isCallToName(call_node) is False

    def test_isNestedNameIdentifier_positive(self) -> None:
        """Test isNestedNameIdentifier with various node types."""
        # Test with Name
        name_node = Make.Name("test_var")
        predicate = IfThis.isNestedNameIdentifier("test_var")
        assert predicate(name_node) is True
        
        # Test with Attribute
        attr_node = Make.Attribute(Make.Name("test_var"), "method")
        assert predicate(attr_node) is True

    def test_isNestedNameIdentifier_negative(self) -> None:
        """Test isNestedNameIdentifier with non-matching identifiers."""
        name_node = Make.Name("test_var")
        predicate = IfThis.isNestedNameIdentifier("other_var")
        assert predicate(name_node) is False

    def test_isStarredIdentifier_positive(self) -> None:
        """Test isStarredIdentifier with matching starred expression."""
        starred_node = Make.Starred(value=Make.Name("args"))
        predicate = IfThis.isStarredIdentifier("args")
        assert predicate(starred_node) is True

    def test_isStarredIdentifier_negative(self) -> None:
        """Test isStarredIdentifier with non-matching starred expression."""
        starred_node = Make.Starred(value=Make.Name("args"))
        predicate = IfThis.isStarredIdentifier("kwargs")
        assert predicate(starred_node) is False

    def test_isSubscriptIdentifier_positive(self) -> None:
        """Test isSubscriptIdentifier with matching subscript expression."""
        subscript_node = Make.Subscript(value=Make.Name("arr"), slice=Make.Constant(0))
        predicate = IfThis.isSubscriptIdentifier("arr")
        assert predicate(subscript_node) is True

    def test_isSubscriptIdentifier_negative(self) -> None:
        """Test isSubscriptIdentifier with non-matching subscript expression."""
        subscript_node = Make.Subscript(value=Make.Name("arr"), slice=Make.Constant(0))
        predicate = IfThis.isSubscriptIdentifier("list")
        assert predicate(subscript_node) is False

    def test_isUnaryNotAttributeNamespaceIdentifier_positive(self) -> None:
        """Test isUnaryNotAttributeNamespaceIdentifier with matching UnaryOp NOT expression."""
        unary_node = Make.UnaryOp(op=Make.Not(), operand=Make.Attribute(Make.Name("obj"), "flag"))
        predicate = IfThis.isUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(unary_node) is True

    def test_isUnaryNotAttributeNamespaceIdentifier_negative(self) -> None:
        """Test isUnaryNotAttributeNamespaceIdentifier with non-matching expressions."""
        unary_node = Make.UnaryOp(op=Make.Not(), operand=Make.Attribute(Make.Name("obj"), "flag"))
        predicate = IfThis.isUnaryNotAttributeNamespaceIdentifier("other_obj", "flag")
        assert predicate(unary_node) is False
        
        # Test with wrong operator
        unary_node_wrong_op = Make.UnaryOp(op=Make.UAdd(), operand=Make.Attribute(Make.Name("obj"), "flag"))
        predicate = IfThis.isUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(unary_node_wrong_op) is False

    def test_isIfUnaryNotAttributeNamespaceIdentifier_positive(self) -> None:
        """Test isIfUnaryNotAttributeNamespaceIdentifier with matching If statement."""
        if_node = Make.If(test=Make.UnaryOp(op=Make.Not(), operand=Make.Attribute(Make.Name("obj"), "flag")), body=[Make.Pass()])
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(if_node) is True

    def test_isIfUnaryNotAttributeNamespaceIdentifier_negative(self) -> None:
        """Test isIfUnaryNotAttributeNamespaceIdentifier with non-matching If statement."""
        if_node = Make.If(test=Make.Name("condition"), body=[Make.Pass()])
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(if_node) is False

    def test_unparseIs_positive(self) -> None:
        """Test unparseIs with matching unparsed code."""
        node1 = Make.Name("x")
        node2 = Make.Name("x")
        predicate = IfThis.unparseIs(node1)
        assert predicate(node2) is True

    def test_unparseIs_negative(self) -> None:
        """Test unparseIs with non-matching unparsed code."""
        node1 = Make.Name("x")
        node2 = Make.Name("y")
        predicate = IfThis.unparseIs(node1)
        assert predicate(node2) is False

    def test_matchesNoDescendant_positive(self) -> None:
        """Test matchesNoDescendant when no descendant matches predicate."""
        # Simple node with no descendants matching predicate
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        name_predicate = lambda node: Be.Name(node) and node.id == "y"
        predicate = IfThis.matchesNoDescendant(name_predicate)
        assert predicate(assign_node) is True

    def test_matchesNoDescendant_negative(self) -> None:
        """Test matchesNoDescendant when a descendant matches predicate."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        name_predicate = lambda node: Be.Name(node) and node.id == "x"
        predicate = IfThis.matchesNoDescendant(name_predicate)
        assert predicate(assign_node) is False

    def test_matchesMeButNotAnyDescendant_positive(self) -> None:
        """Test matchesMeButNotAnyDescendant when node matches but descendants don't."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        assign_predicate = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(assign_predicate)
        assert predicate(assign_node) is True

    def test_matchesMeButNotAnyDescendant_negative(self) -> None:
        """Test matchesMeButNotAnyDescendant when node doesn't match."""
        name_node = Make.Name("x")
        assign_predicate = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(assign_predicate)
        assert predicate(name_node) is False


# Additional edge case tests
class TestIfThisEdgeCases:
    """Test edge cases and error conditions for IfThis predicates."""

    def test_empty_predicates_isAllOf(self) -> None:
        """Test isAllOf with no predicates."""
        name_node = Make.Name("test")
        combined = IfThis.isAllOf()
        assert combined(name_node) is True  # all() returns True for empty sequence

    def test_empty_predicates_isAnyOf(self) -> None:
        """Test isAnyOf with no predicates."""
        name_node = Make.Name("test")
        combined = IfThis.isAnyOf()
        assert combined(name_node) is False  # any() returns False for empty sequence

    def test_complex_nested_structure(self) -> None:
        """Test predicates with complex nested AST structures."""
        # Create a complex nested structure: obj.method(arg1, key=value)
        call_node = Make.Call(
            callee=Make.Attribute(Make.Name("obj"), "method"),
            listParameters=[Make.Name("arg1")],
            list_keyword=[Make.keyword("key", Make.Constant("value"))]
        )
        
        # Test various predicates on this structure
        assert IfThis.isCallAttributeNamespaceIdentifier("obj", "method")(call_node) is True
        assert IfThis.isCallIdentifier("method")(call_node) is False  # func is Attribute, not Name
        assert IfThis.isCallToName(call_node) is False  # func is Attribute, not Name

    def test_predicate_composition(self) -> None:
        """Test complex predicate compositions."""
        func_node = Make.FunctionDef(name="test_func", body=[Make.Assign(targets=[Make.Name("x", context=Make.Store())], value=Make.Constant(42))])
        
        # Combine multiple predicates
        complex_predicate = IfThis.isAllOf(
            Be.FunctionDef,
            lambda node: node.name == "test_func",
            lambda node: len(node.body) > 0
        )
        assert complex_predicate(func_node) is True
        
        # Test with isAnyOf
        any_predicate = IfThis.isAnyOf(
            lambda node: Be.ClassDef(node),
            lambda node: Be.FunctionDef(node) and node.name == "test_func"
        )
        assert any_predicate(func_node) is True