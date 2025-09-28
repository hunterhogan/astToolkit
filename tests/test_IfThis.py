"""Tests for the IfThis class predicates using parametrized tests and DRY principles."""

from astToolkit import Be, IfThis, Make
import pytest


class TestIfThisBasic:
    """Test suite for basic IfThis methods."""

    @pytest.mark.parametrize("input_val,expected", [
        ("test_name", True),
        ("different_name", False),
        (None, False),
    ])
    def test_isIdentifier_with_string(self, input_val, expected):
        """Test isIdentifier with string identifier."""
        predicate = IfThis.isIdentifier("test_name")
        assert predicate(input_val) is expected

    @pytest.mark.parametrize("input_val,expected", [
        (None, True),
        ("some_name", False),
    ])
    def test_isIdentifier_with_none(self, input_val, expected):
        """Test isIdentifier with None identifier."""
        predicate = IfThis.isIdentifier(None)
        assert predicate(input_val) is expected

    @pytest.mark.parametrize("test_value,node_value,expected", [
        (42, 42, True),
        (42, 24, False),
        ("hello", "hello", True),
        ("hello", "world", False),
        (None, None, True),
        (None, 42, False),
    ])
    def test_isConstant_value(self, test_value, node_value, expected):
        """Test isConstant_value with various values."""
        constant_node = Make.Constant(node_value)
        predicate = IfThis.isConstant_value(test_value)
        assert predicate(constant_node) is expected

    def test_isConstant_value_wrong_node_type(self):
        """Test isConstant_value with wrong node type."""
        name_node = Make.Name("test")
        predicate = IfThis.isConstant_value(42)
        assert predicate(name_node) is False


class TestIfThisIdentifierMethods:
    """Test suite for identifier-based IfThis methods using fixtures."""

    def test_identifier_methods(self, identifierTestData):
        """Test identifier methods using parametrized data."""
        method_name, test_id, node_factory, expected = identifierTestData
        
        # Get the method from IfThis
        method = getattr(IfThis, method_name)
        
        # Create the predicate
        predicate = method(test_id)
        
        # Create the test node
        node = node_factory(test_id)
        
        # Test the predicate
        assert predicate(node) is expected, f"{method_name}({test_id}) should return {expected}"

    @pytest.mark.parametrize("method_name,test_id", [
        ("isNameIdentifier", "test_var"),
        ("isFunctionDefIdentifier", "test_func"), 
        ("isClassDefIdentifier", "TestClass"),
        ("isCallIdentifier", "print"),
        ("is_argIdentifier", "param"),
        ("is_keywordIdentifier", "key"),
    ])
    def test_identifier_methods_wrong_node_type(self, method_name, test_id):
        """Test identifier methods with wrong node types."""
        method = getattr(IfThis, method_name)
        predicate = method(test_id)
        wrong_node = Make.Constant(42)  # Wrong node type for all these methods
        assert predicate(wrong_node) is False


class TestIfThisSimpleMethods:
    """Test suite for simple predicate IfThis methods using fixtures."""

    def test_simple_methods(self, simplePredicateTestData):
        """Test simple predicate methods using parametrized data."""
        method_name, args, node_factory, expected = simplePredicateTestData
        
        # Get the method from IfThis
        method = getattr(IfThis, method_name)
        
        # Create the predicate
        predicate = method(*args)
        
        # Create the test node
        node = node_factory()
        
        # Test the predicate
        assert predicate(node) is expected, f"{method_name}({args}) should return {expected}"

    def test_direct_methods(self, directPredicateTestData):
        """Test direct predicate methods that take node directly."""
        method_name, node_factory, expected = directPredicateTestData
        
        # Get the method from IfThis
        method = getattr(IfThis, method_name)
        
        # Create the test node
        node = node_factory()
        
        # Test the method directly
        result = method(node)
        assert result is expected, f"{method_name}(node) should return {expected}"


class TestIfThisComplexMethods:
    """Test suite for complex predicate IfThis methods using fixtures."""

    def test_complex_methods(self, complexPredicateTestData):
        """Test complex predicate methods using parametrized data."""
        method_name, args, node_factory, expected = complexPredicateTestData
        
        # Get the method from IfThis
        method = getattr(IfThis, method_name)
        
        # Create the predicate
        predicate = method(*args)
        
        # Create the test node
        node = node_factory()
        
        # Test the predicate
        assert predicate(node) is expected, f"{method_name}({args}) should return {expected}"

    @pytest.mark.parametrize("namespace,identifier", [
        ("obj", "method"),
        ("self", "value"), 
        ("cls", "name"),
    ])
    def test_isAttributeNamespaceIdentifier_positive(self, namespace, identifier):
        """Test isAttributeNamespaceIdentifier with matching cases."""
        attr_node = Make.Attribute(Make.Name(namespace), identifier)
        predicate = IfThis.isAttributeNamespaceIdentifier(namespace, identifier)
        assert predicate(attr_node) is True

    def test_isIfUnaryNotAttributeNamespaceIdentifier_positive(self):
        """Test isIfUnaryNotAttributeNamespaceIdentifier with matching case."""
        if_node = Make.If(
            test=Make.UnaryOp(
                op=Make.Not(), 
                operand=Make.Attribute(Make.Name("obj"), "flag")
            ),
            body=[Make.Pass()]
        )
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(if_node) is True

    def test_isIfUnaryNotAttributeNamespaceIdentifier_negative(self):
        """Test isIfUnaryNotAttributeNamespaceIdentifier with non-matching case."""
        if_node = Make.If(test=Make.Name("condition"), body=[Make.Pass()])
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(if_node) is False


class TestIfThisLogicalMethods:
    """Test suite for logical combination IfThis methods."""

    @pytest.mark.parametrize("predicates,node,expected", [
        # All predicates match
        ([Be.Name, lambda n: hasattr(n, 'id') and n.id == "test"], Make.Name("test"), True),
        # Some predicates don't match  
        ([Be.Name, lambda n: hasattr(n, 'id') and n.id == "other"], Make.Name("test"), False),
        # No predicates (edge case)
        ([], Make.Name("test"), True),  # all() returns True for empty sequence
    ])
    def test_isAllOf(self, predicates, node, expected):
        """Test isAllOf with various predicate combinations."""
        combined = IfThis.isAllOf(*predicates)
        assert combined(node) is expected

    @pytest.mark.parametrize("predicates,node,expected", [
        # At least one predicate matches
        ([Be.Constant, Be.Name], Make.Name("test"), True),
        # No predicates match
        ([Be.Constant, Be.FunctionDef], Make.Name("test"), False),
        # No predicates (edge case) 
        ([], Make.Name("test"), False),  # any() returns False for empty sequence
    ])
    def test_isAnyOf(self, predicates, node, expected):
        """Test isAnyOf with various predicate combinations."""
        combined = IfThis.isAnyOf(*predicates)
        assert combined(node) is expected


class TestIfThisTreeMethods:
    """Test suite for tree analysis IfThis methods."""

    def test_matchesNoDescendant_positive(self):
        """Test matchesNoDescendant when no descendant matches predicate."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        name_predicate = lambda node: Be.Name(node) and getattr(node, 'id', None) == "y"
        predicate = IfThis.matchesNoDescendant(name_predicate)
        assert predicate(assign_node) is True

    def test_matchesNoDescendant_negative(self):
        """Test matchesNoDescendant when a descendant matches predicate."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        name_predicate = lambda node: Be.Name(node) and getattr(node, 'id', None) == "x"
        predicate = IfThis.matchesNoDescendant(name_predicate)
        assert predicate(assign_node) is False

    def test_matchesMeButNotAnyDescendant_positive(self):
        """Test matchesMeButNotAnyDescendant when node matches but descendants don't."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        assign_predicate = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(assign_predicate)
        assert predicate(assign_node) is True

    def test_matchesMeButNotAnyDescendant_negative(self):
        """Test matchesMeButNotAnyDescendant when node doesn't match."""
        name_node = Make.Name("x")
        assign_predicate = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(assign_predicate)
        assert predicate(name_node) is False

    @pytest.mark.parametrize("node1,node2,expected", [
        (Make.Name("x"), Make.Name("x"), True),
        (Make.Name("x"), Make.Name("y"), False),
        (Make.Constant(42), Make.Constant(42), True),
        (Make.Constant(42), Make.Constant(24), False),
    ])
    def test_unparseIs(self, node1, node2, expected):
        """Test unparseIs with various node combinations."""
        predicate = IfThis.unparseIs(node1)
        assert predicate(node2) is expected


class TestIfThisAdvancedCases:
    """Test suite for advanced IfThis usage scenarios."""

    def test_nested_identifier_patterns(self):
        """Test isNestedNameIdentifier with various node types."""
        test_id = "test_var"
        predicate = IfThis.isNestedNameIdentifier(test_id)
        
        # Should match Name
        name_node = Make.Name(test_id)
        assert predicate(name_node) is True
        
        # Should match Attribute with matching value
        attr_node = Make.Attribute(Make.Name(test_id), "method")
        assert predicate(attr_node) is True
        
        # Should not match Attribute with non-matching value
        attr_node_no_match = Make.Attribute(Make.Name("other_var"), "method")
        assert predicate(attr_node_no_match) is False

    def test_isAssignAndTargets0Is_patterns(self):
        """Test isAssignAndTargets0Is with various target predicates."""
        assign_node = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        
        # Matching target predicate
        target_predicate = lambda node: Be.Name(node) and getattr(node, 'id', None) == "x"
        predicate = IfThis.isAssignAndTargets0Is(target_predicate)
        assert predicate(assign_node) is True
        
        # Non-matching target predicate
        wrong_target_predicate = lambda node: Be.Name(node) and getattr(node, 'id', None) == "y"
        wrong_predicate = IfThis.isAssignAndTargets0Is(wrong_target_predicate)
        assert wrong_predicate(assign_node) is False
        
        # Wrong node type
        name_node = Make.Name("x")
        assert predicate(name_node) is False

    def test_complex_predicate_composition(self):
        """Test complex predicate compositions with real-world scenarios."""
        # Create a function with assignment in body
        func_node = Make.FunctionDef(
            name="test_func",
            body=[Make.Assign(
                targets=[Make.Name("x", context=Make.Store())],
                value=Make.Constant(42)
            )]
        )
        
        # Complex predicate combining multiple conditions
        complex_predicate = IfThis.isAllOf(
            Be.FunctionDef,
            lambda node: getattr(node, 'name', None) == "test_func",
            lambda node: len(getattr(node, 'body', [])) > 0
        )
        assert complex_predicate(func_node) is True
        
        # Should fail if any condition doesn't match
        different_func = Make.FunctionDef(name="other_func", body=[Make.Pass()])
        assert complex_predicate(different_func) is False