"""Tests for the Then class action functions using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Make, Then
from collections.abc import Sequence
from typing import Any, TYPE_CHECKING
import pytest
import ast

if TYPE_CHECKING:
    from collections.abc import Callable


class TestThenAppendTo:
    """Test suite for Then.appendTo method."""

    def testAppendToBasic(self) -> None:
        """Test basic functionality of appendTo."""
        collection: list[Any] = []
        node = Make.Name("test_var")
        
        action = Then.appendTo(collection)
        result = action(node)
        
        # Node should be returned unchanged
        assert result is node
        # Node should be appended to collection
        assert len(collection) == 1
        assert collection[0] is node

    def testAppendToMultipleNodes(self) -> None:
        """Test appendTo with multiple nodes."""
        collection: list[Any] = []
        node1 = Make.Name("var1")
        node2 = Make.Name("var2")
        node3 = Make.Constant(42)
        
        action = Then.appendTo(collection)
        
        result1 = action(node1)
        result2 = action(node2)
        result3 = action(node3)
        
        # All nodes should be returned unchanged
        assert result1 is node1
        assert result2 is node2
        assert result3 is node3
        
        # All nodes should be in collection in order
        assert len(collection) == 3
        assert collection[0] is node1
        assert collection[1] is node2
        assert collection[2] is node3

    def testAppendToPreExistingList(self) -> None:
        """Test appendTo with pre-existing items in list."""
        existing_item = "existing"
        collection: list[Any] = [existing_item]
        node = Make.Name("new_item")
        
        action = Then.appendTo(collection)
        result = action(node)
        
        assert result is node
        assert len(collection) == 2
        assert collection[0] == existing_item
        assert collection[1] is node

    def testAppendToTypePreservation(self) -> None:
        """Test that appendTo preserves node types correctly."""
        collection: list[Any] = []
        
        # Test with different AST node types
        name_node = Make.Name("test")
        constant_node = Make.Constant("hello")  
        assign_node = Make.Assign([Make.Name("x")], Make.Constant(1))
        
        action = Then.appendTo(collection)
        
        result1 = action(name_node)
        result2 = action(constant_node)
        result3 = action(assign_node)
        
        assert isinstance(result1, ast.Name)
        assert isinstance(result2, ast.Constant)
        assert isinstance(result3, ast.Assign)
        
        assert len(collection) == 3
        assert isinstance(collection[0], ast.Name)
        assert isinstance(collection[1], ast.Constant)
        assert isinstance(collection[2], ast.Assign)


class TestThenExtractIt:
    """Test suite for Then.extractIt method."""

    def testExtractItIdentity(self) -> None:
        """Test that extractIt returns nodes unchanged."""
        node = Make.Name("test_var")
        result = Then.extractIt(node)
        assert result is node

    @pytest.mark.parametrize("node_factory", [
        lambda: Make.Name("test"),
        lambda: Make.Constant(42),
        lambda: Make.Constant("string"),
        lambda: Make.Constant(None),
        lambda: Make.Assign([Make.Name("x")], Make.Constant(1)),
        lambda: Make.If(Make.Constant(True), [Make.Pass()]),
        lambda: Make.FunctionDef("test_func"),
        lambda: Make.ClassDef("TestClass"),
    ])
    def testExtractItDifferentNodeTypes(self, node_factory: "Callable[[], ast.AST]") -> None:
        """Test extractIt with different AST node types."""
        node = node_factory()
        result = Then.extractIt(node)
        assert result is node
        assert type(result) is type(node)

    def testExtractItNonASTTypes(self) -> None:
        """Test extractIt with non-AST types."""
        # Should work with any type since it's generic
        string_value = "test"
        int_value = 42
        list_value = [1, 2, 3]
        dict_value = {"key": "value"}
        
        assert Then.extractIt(string_value) is string_value
        assert Then.extractIt(int_value) is int_value
        assert Then.extractIt(list_value) is list_value
        assert Then.extractIt(dict_value) is dict_value


class TestThenInsertThisAbove:
    """Test suite for Then.insertThisAbove method."""

    def testInsertThisAboveSingleNode(self) -> None:
        """Test inserting a single node above target."""
        target_node = Make.Pass()
        insert_node = Make.Assign([Make.Name("x")], Make.Constant(1))
        
        action = Then.insertThisAbove([insert_node])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] is insert_node
        assert result[1] is target_node

    def testInsertThisAboveMultipleNodes(self) -> None:
        """Test inserting multiple nodes above target."""
        target_node = Make.Pass()
        insert_node1 = Make.Assign([Make.Name("x")], Make.Constant(1))
        insert_node2 = Make.Assign([Make.Name("y")], Make.Constant(2))
        
        action = Then.insertThisAbove([insert_node1, insert_node2])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0] is insert_node1
        assert result[1] is insert_node2
        assert result[2] is target_node

    def testInsertThisAboveEmptySequence(self) -> None:
        """Test inserting empty sequence above target."""
        target_node = Make.Pass()
        
        action = Then.insertThisAbove([])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] is target_node

    def testInsertThisAboveOrderPreservation(self) -> None:
        """Test that insertion order is preserved."""
        target_node = Make.Pass()
        nodes_to_insert = [
            Make.Assign([Make.Name("a")], Make.Constant(1)),
            Make.Assign([Make.Name("b")], Make.Constant(2)),
            Make.Assign([Make.Name("c")], Make.Constant(3)),
        ]
        
        action = Then.insertThisAbove(nodes_to_insert)
        result = action(target_node)
        
        assert len(result) == 4
        for i, inserted_node in enumerate(nodes_to_insert):
            assert result[i] is inserted_node
        assert result[-1] is target_node


class TestThenInsertThisBelow:
    """Test suite for Then.insertThisBelow method."""

    def testInsertThisBelowSingleNode(self) -> None:
        """Test inserting a single node below target."""
        target_node = Make.Pass()
        insert_node = Make.Assign([Make.Name("x")], Make.Constant(1))
        
        action = Then.insertThisBelow([insert_node])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] is target_node
        assert result[1] is insert_node

    def testInsertThisBelowMultipleNodes(self) -> None:
        """Test inserting multiple nodes below target."""
        target_node = Make.Pass()
        insert_node1 = Make.Assign([Make.Name("x")], Make.Constant(1))
        insert_node2 = Make.Assign([Make.Name("y")], Make.Constant(2))
        
        action = Then.insertThisBelow([insert_node1, insert_node2])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0] is target_node
        assert result[1] is insert_node1
        assert result[2] is insert_node2

    def testInsertThisBelowEmptySequence(self) -> None:
        """Test inserting empty sequence below target."""
        target_node = Make.Pass()
        
        action = Then.insertThisBelow([])
        result = action(target_node)
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] is target_node

    def testInsertThisBelowOrderPreservation(self) -> None:
        """Test that insertion order is preserved."""
        target_node = Make.Pass()
        nodes_to_insert = [
            Make.Assign([Make.Name("a")], Make.Constant(1)),
            Make.Assign([Make.Name("b")], Make.Constant(2)),
            Make.Assign([Make.Name("c")], Make.Constant(3)),
        ]
        
        action = Then.insertThisBelow(nodes_to_insert)
        result = action(target_node)
        
        assert len(result) == 4
        assert result[0] is target_node
        for i, inserted_node in enumerate(nodes_to_insert):
            assert result[i + 1] is inserted_node


class TestThenRemoveIt:
    """Test suite for Then.removeIt method."""

    def testRemoveItReturnsNone(self) -> None:
        """Test that removeIt always returns None."""
        test_nodes = [
            Make.Name("test"),
            Make.Constant(42),
            Make.Assign([Make.Name("x")], Make.Constant(1)),
            Make.Pass(),
            Make.If(Make.Constant(True), [Make.Pass()]),
        ]
        
        for node in test_nodes:
            result = Then.removeIt(node)
            assert result is None

    def testRemoveItWithComplexNode(self) -> None:
        """Test removeIt with complex AST structures."""
        complex_node = Make.FunctionDef(
            name="complex_function",
            argumentSpecification=Make.arguments([Make.arg("param1"), Make.arg("param2")]),
            body=[
                Make.Assign([Make.Name("local_var")], Make.Constant("value")),
                Make.If(
                    Make.Compare(Make.Name("param1"), [Make.Gt()], [Make.Constant(0)]),
                    [Make.Return(Make.Name("param1"))],
                    [Make.Return(Make.Constant(0))]
                )
            ]
        )
        
        result = Then.removeIt(complex_node)
        assert result is None


class TestThenReplaceWith:
    """Test suite for Then.replaceWith method."""

    def testReplaceWithBasic(self) -> None:
        """Test basic replacement functionality."""
        original_node = Make.Name("old_name")
        replacement_node = Make.Name("new_name")
        
        action = Then.replaceWith(replacement_node)
        result = action(original_node)
        
        assert result is replacement_node
        assert result is not original_node

    def testReplaceWithDifferentTypes(self) -> None:
        """Test replacement with different AST node types."""
        original_node = Make.Name("variable")
        replacement_node = Make.Constant(42)
        
        action = Then.replaceWith(replacement_node)
        result = action(original_node)
        
        assert result is replacement_node
        assert isinstance(result, ast.Constant)
        assert not isinstance(result, ast.Name)

    def testReplaceWithComplexNodes(self) -> None:
        """Test replacement with complex AST structures."""
        original_node = Make.Pass()
        replacement_node = Make.If(
            Make.Constant(True),
            [Make.Assign([Make.Name("x")], Make.Constant(1))],
            [Make.Pass()]
        )
        
        action = Then.replaceWith(replacement_node)
        result = action(original_node)
        
        assert result is replacement_node
        assert isinstance(result, ast.If)

    def testReplaceWithNonASTTypes(self) -> None:
        """Test replacement with non-AST types."""
        original_node = Make.Name("test")
        replacement_value = "replacement_string"
        
        action = Then.replaceWith(replacement_value)
        result = action(original_node)
        
        assert result == replacement_value
        assert result is replacement_value

    def testReplaceWithIgnoresOriginal(self) -> None:
        """Test that replaceWith completely ignores the original node."""
        original_nodes = [
            Make.Name("test1"),
            Make.Constant(42),
            Make.Pass(),
        ]
        replacement_node = Make.Name("replacement")
        
        action = Then.replaceWith(replacement_node)
        
        for original in original_nodes:
            result = action(original)
            assert result is replacement_node


class TestThenUpdateKeyValueIn:
    """Test suite for Then.updateKeyValueIn method."""

    def testUpdateKeyValueInBasic(self) -> None:
        """Test basic dictionary update functionality."""
        dictionary: dict[str, str] = {}
        node = Make.Name("test_var")
        
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: "name_node" if isinstance(n, ast.Name) else "other"
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        result = action(node)
        
        assert result is dictionary
        assert len(dictionary) == 1
        assert dictionary["test_var"] == "name_node"

    def testUpdateKeyValueInMultipleNodes(self) -> None:
        """Test dictionary update with multiple nodes."""
        dictionary: dict[str, str] = {}
        
        nodes = [
            Make.Name("var1"),
            Make.Name("var2"),
            Make.Name("var3"),
        ]
        
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: f"name_{n.id}" if isinstance(n, ast.Name) else "other"
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        
        for node in nodes:
            result = action(node)
            assert result is dictionary
        
        assert len(dictionary) == 3
        assert dictionary["var1"] == "name_var1"
        assert dictionary["var2"] == "name_var2"
        assert dictionary["var3"] == "name_var3"

    def testUpdateKeyValueInSetdefaultBehavior(self) -> None:
        """Test that updateKeyValueIn uses setdefault (doesn't overwrite existing keys)."""
        dictionary: dict[str, str] = {"existing_key": "original_value"}
        node = Make.Name("existing_key")
        
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: "new_value"
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        result = action(node)
        
        assert result is dictionary
        assert len(dictionary) == 1
        assert dictionary["existing_key"] == "original_value"  # Should not be overwritten

    def testUpdateKeyValueInComplexTypes(self) -> None:
        """Test dictionary update with complex key/value types."""
        dictionary: dict[type, int] = {}
        
        nodes = [
            Make.Name("test"),
            Make.Constant(42),
            Make.Assign([Make.Name("x")], Make.Constant(1)),
            Make.Name("another"),  # Same type as first, should not overwrite
        ]
        
        key_func = lambda n: type(n)
        value_func = lambda n: 1
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        
        for node in nodes:
            result = action(node)
            assert result is dictionary
        
        # Should have entries for ast.Name, ast.Constant, ast.Assign
        assert len(dictionary) == 3
        assert ast.Name in dictionary
        assert ast.Constant in dictionary  
        assert ast.Assign in dictionary
        assert dictionary[ast.Name] == 1
        assert dictionary[ast.Constant] == 1
        assert dictionary[ast.Assign] == 1

    def testUpdateKeyValueInPreExistingDictionary(self) -> None:
        """Test dictionary update with pre-existing entries."""
        dictionary: dict[str, int] = {"pre_existing": 100}
        node = Make.Name("new_entry")
        
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: 42
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        result = action(node)
        
        assert result is dictionary
        assert len(dictionary) == 2
        assert dictionary["pre_existing"] == 100
        assert dictionary["new_entry"] == 42

    def testUpdateKeyValueInReturnsBehavior(self) -> None:
        """Test that updateKeyValueIn always returns the same dictionary instance."""
        dictionary: dict[str, str] = {}
        nodes = [Make.Name("test1"), Make.Name("test2")]
        
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: "value"
        
        action = Then.updateKeyValueIn(key_func, value_func, dictionary)
        
        results = []
        for node in nodes:
            result = action(node)
            results.append(result)
        
        # All results should be the same dictionary instance
        for result in results:
            assert result is dictionary


class TestThenIntegration:
    """Integration tests for Then methods working together."""

    def testThenMethodsWithRealUseCase(self) -> None:
        """Test Then methods in a realistic AST processing scenario."""
        # Simulate collecting function names, then replacing them
        collected_functions: list[ast.FunctionDef] = []
        
        # Create some AST nodes
        func1 = Make.FunctionDef("old_function")
        func2 = Make.FunctionDef("another_function")
        
        # Test appendTo
        collect_action = Then.appendTo(collected_functions)
        
        result1 = collect_action(func1)
        result2 = collect_action(func2)
        
        assert result1 is func1
        assert result2 is func2
        assert len(collected_functions) == 2
        
        # Test replaceWith
        new_func = Make.FunctionDef("new_function")
        replace_action = Then.replaceWith(new_func)
        
        replaced = replace_action(func1)
        assert replaced is new_func
        assert replaced is not func1

    def testThenMethodsChaining(self) -> None:
        """Test that Then methods can be used in sequence."""
        # This simulates a workflow where we collect, then transform
        collection: list[ast.Name] = []
        mapping: dict[str, str] = {}
        
        node = Make.Name("original_name")
        
        # First, collect the node
        collect_action = Then.appendTo(collection)
        result1 = collect_action(node)
        
        # Then, update a mapping
        key_func = lambda n: n.id if isinstance(n, ast.Name) else "unknown"
        value_func = lambda n: f"processed_{n.id}" if isinstance(n, ast.Name) else "unknown"
        update_action = Then.updateKeyValueIn(key_func, value_func, mapping)
        result2 = update_action(node)
        
        # Finally, replace it
        replacement = Make.Name("new_name")
        replace_action = Then.replaceWith(replacement)
        result3 = replace_action(node)
        
        # Verify all steps worked
        assert result1 is node
        assert result2 is mapping
        assert result3 is replacement
        assert len(collection) == 1
        assert collection[0] is node
        assert mapping["original_name"] == "processed_original_name"