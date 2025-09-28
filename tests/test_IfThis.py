"""Tests for the IfThis class predicates using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Be, IfThis, Make
from typing import Any, TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    from collections.abc import Callable
    import ast

class TestIfThisBasic:
    """Test suite for basic IfThis methods."""

    @pytest.mark.parametrize("valueInput,expectedResult", [
        ("test_name", True),
        ("different_name", False),
        (None, False),
    ])
    def testIsIdentifierWithString(self, valueInput: str | None, expectedResult: bool) -> None:
        """Test isIdentifier with string identifier."""
        predicate: Callable[[str | None], bool] = IfThis.isIdentifier("test_name")
        assert predicate(valueInput) is expectedResult

    @pytest.mark.parametrize("valueInput,expectedResult", [
        (None, True),
        ("some_name", False),
    ])
    def testIsIdentifierWithNone(self, valueInput: str | None, expectedResult: bool) -> None:
        """Test isIdentifier with None identifier."""
        predicate: Callable[[str | None], bool] = IfThis.isIdentifier(None)
        assert predicate(valueInput) is expectedResult

    @pytest.mark.parametrize("valueTest,valueNode,expectedResult", [
        (42, 42, True),
        (42, 24, False),
        ("hello", "hello", True),
        ("hello", "world", False),
        (None, None, True),
        (None, 42, False),
    ])
    def testIsConstantValue(self, valueTest: Any, valueNode: Any, expectedResult: bool) -> None:
        """Test isConstant_value with various values."""
        nodeConstant: ast.Constant = Make.Constant(valueNode)
        predicate: Callable[[ast.AST], bool] = IfThis.isConstant_value(valueTest)
        assert predicate(nodeConstant) is expectedResult

    def testIsConstantValueWrongNodeType(self) -> None:
        """Test isConstant_value with wrong node type."""
        nodeName: ast.Name = Make.Name("test")
        predicate: Callable[[ast.AST], bool] = IfThis.isConstant_value(42)
        assert predicate(nodeName) is False


class TestIfThisIdentifierMethods:
    """Test suite for identifier-based IfThis methods using fixtures."""

    def testIdentifierMethods(self, identifierTestData: tuple[str, str, "Callable[..., Any]", bool]) -> None:
        """Test identifier methods using parametrized data."""
        nameMethod, identifierTest, factoryNode, expectedResult = identifierTestData

        # Get the method from IfThis
        method = getattr(IfThis, nameMethod)

        # Create the predicate
        predicate = method(identifierTest)

        # Create the test node
        node = factoryNode(identifierTest)

        # Test the predicate
        assert predicate(node) is expectedResult, f"{nameMethod}({identifierTest}) should return {expectedResult}"

    @pytest.mark.parametrize("nameMethod,identifierTest", [
        ("isNameIdentifier", "test_var"),
        ("isFunctionDefIdentifier", "test_func"),
        ("isClassDefIdentifier", "TestClass"),
        ("isCallIdentifier", "print"),
        ("is_argIdentifier", "param"),
        ("is_keywordIdentifier", "key"),
    ])
    def testIdentifierMethodsWrongNodeType(self, nameMethod: str, identifierTest: str) -> None:
        """Test identifier methods with wrong node types."""
        method = getattr(IfThis, nameMethod)
        predicate = method(identifierTest)
        nodeWrong = Make.Constant(42)  # Wrong node type for all these methods
        assert predicate(nodeWrong) is False


class TestIfThisSimpleMethods:
    """Test suite for simple predicate IfThis methods using fixtures."""

    def testSimpleMethods(self, simplePredicateTestData: tuple[str, tuple[Any, ...], "Callable[[], Any]", bool]) -> None:
        """Test simple predicate methods using parametrized data."""
        nameMethod, argumentsList, factoryNode, expectedResult = simplePredicateTestData

        # Get the method from IfThis
        method = getattr(IfThis, nameMethod)

        # Create the predicate
        predicate = method(*argumentsList)

        # Create the test node
        node = factoryNode()

        # Test the predicate
        assert predicate(node) is expectedResult, f"{nameMethod}({argumentsList}) should return {expectedResult}"

    def testDirectMethods(self, directPredicateTestData: tuple[str, "Callable[[], Any]", bool]) -> None:
        """Test direct predicate methods that take node directly."""
        nameMethod, factoryNode, expectedResult = directPredicateTestData

        # Get the method from IfThis
        method = getattr(IfThis, nameMethod)

        # Create the test node
        node = factoryNode()

        # Test the method directly
        result = method(node)
        assert result is expectedResult, f"{nameMethod}(node) should return {expectedResult}"


class TestIfThisComplexMethods:
    """Test suite for complex predicate IfThis methods using fixtures."""

    def testComplexMethods(self, complexPredicateTestData: tuple[str, tuple[Any, ...], "Callable[[], Any]", bool]) -> None:
        """Test complex predicate methods using parametrized data."""
        nameMethod, argumentsList, factoryNode, expectedResult = complexPredicateTestData

        # Get the method from IfThis
        method = getattr(IfThis, nameMethod)

        # Create the predicate
        predicate = method(*argumentsList)

        # Create the test node
        node = factoryNode()

        # Test the predicate
        assert predicate(node) is expectedResult, f"{nameMethod}({argumentsList}) should return {expectedResult}"

    @pytest.mark.parametrize("namespaceObject,identifierAttribute", [
        ("obj", "method"),
        ("self", "value"),
        ("cls", "name"),
    ])
    def testIsAttributeNamespaceIdentifierPositive(self, namespaceObject: str, identifierAttribute: str) -> None:
        """Test isAttributeNamespaceIdentifier with matching cases."""
        nodeAttribute = Make.Attribute(Make.Name(namespaceObject), identifierAttribute)
        predicate = IfThis.isAttributeNamespaceIdentifier(namespaceObject, identifierAttribute)
        assert predicate(nodeAttribute) is True

    def testIsIfUnaryNotAttributeNamespaceIdentifierPositive(self) -> None:
        """Test isIfUnaryNotAttributeNamespaceIdentifier with matching case."""
        nodeIf = Make.If(
            test=Make.UnaryOp(
                op=Make.Not(),
                operand=Make.Attribute(Make.Name("obj"), "flag")
            ),
            body=[Make.Pass()]
        )
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(nodeIf) is True

    def testIsIfUnaryNotAttributeNamespaceIdentifierNegative(self) -> None:
        """Test isIfUnaryNotAttributeNamespaceIdentifier with non-matching case."""
        nodeIf = Make.If(test=Make.Name("condition"), body=[Make.Pass()])
        predicate = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("obj", "flag")
        assert predicate(nodeIf) is False


class TestIfThisLogicalMethods:
    """Test suite for logical combination IfThis methods."""

    @pytest.mark.parametrize("listPredicates,nodeTest,expectedResult", [
        # All predicates match
        ([Be.Name, lambda node: hasattr(node, 'id') and node.id == "test"], Make.Name("test"), True),
        # Some predicates don't match
        ([Be.Name, lambda node: hasattr(node, 'id') and node.id == "other"], Make.Name("test"), False),
        # No predicates (edge case)
        ([], Make.Name("test"), True),  # all() returns True for empty sequence
    ])
    def testIsAllOf(self, listPredicates: list["Callable[..., Any]"], nodeTest: "ast.AST", expectedResult: bool) -> None:
        """Test isAllOf with various predicate combinations."""
        combined = IfThis.isAllOf(*listPredicates)
        assert combined(nodeTest) is expectedResult

    @pytest.mark.parametrize("listPredicates,nodeTest,expectedResult", [
        # At least one predicate matches
        ([Be.Constant, Be.Name], Make.Name("test"), True),
        # No predicates match
        ([Be.Constant, Be.FunctionDef], Make.Name("test"), False),
        # No predicates (edge case)
        ([], Make.Name("test"), False),  # any() returns False for empty sequence
    ])
    def testIsAnyOf(self, listPredicates: list["Callable[..., Any]"], nodeTest: "ast.AST", expectedResult: bool) -> None:
        """Test isAnyOf with various predicate combinations."""
        combined = IfThis.isAnyOf(*listPredicates)
        assert combined(nodeTest) is expectedResult


class TestIfThisTreeMethods:
    """Test suite for tree analysis IfThis methods."""

    def testMatchesNoDescendantPositive(self) -> None:
        """Test matchesNoDescendant when no descendant matches predicate."""
        nodeAssign = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        def predicateNameMatching(node: "ast.AST") -> bool:
            return Be.Name(node) and getattr(node, 'id', None) == "y"
        predicate = IfThis.matchesNoDescendant(predicateNameMatching)
        assert predicate(nodeAssign) is True

    def testMatchesNoDescendantNegative(self) -> None:
        """Test matchesNoDescendant when a descendant matches predicate."""
        nodeAssign = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        def predicateNameMatching(node: "ast.AST") -> bool:
            return Be.Name(node) and getattr(node, 'id', None) == "x"
        predicate = IfThis.matchesNoDescendant(predicateNameMatching)
        assert predicate(nodeAssign) is False

    def testMatchesMeButNotAnyDescendantPositive(self) -> None:
        """Test matchesMeButNotAnyDescendant when node matches but descendants don't."""
        nodeAssign = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )
        predicateAssign = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(predicateAssign)
        assert predicate(nodeAssign) is True

    def testMatchesMeButNotAnyDescendantNegative(self) -> None:
        """Test matchesMeButNotAnyDescendant when node doesn't match."""
        nodeName = Make.Name("x")
        predicateAssign = Be.Assign
        predicate = IfThis.matchesMeButNotAnyDescendant(predicateAssign)
        assert predicate(nodeName) is False

    @pytest.mark.parametrize("nodeFirst,nodeSecond,expectedResult", [
        (Make.Name("x"), Make.Name("x"), True),
        (Make.Name("x"), Make.Name("y"), False),
        (Make.Constant(42), Make.Constant(42), True),
        (Make.Constant(42), Make.Constant(24), False),
    ])
    def testUnparseIs(self, nodeFirst: "ast.AST", nodeSecond: "ast.AST", expectedResult: bool) -> None:
        """Test unparseIs with various node combinations."""
        predicate = IfThis.unparseIs(nodeFirst)
        assert predicate(nodeSecond) is expectedResult


class TestIfThisAdvancedCases:
    """Test suite for advanced IfThis usage scenarios."""

    def testNestedIdentifierPatterns(self) -> None:
        """Test isNestedNameIdentifier with various node types."""
        identifierTest = "test_var"
        predicate = IfThis.isNestedNameIdentifier(identifierTest)

        # Should match Name
        nodeName = Make.Name(identifierTest)
        assert predicate(nodeName) is True

        # Should match Attribute with matching value
        nodeAttribute = Make.Attribute(Make.Name(identifierTest), "method")
        assert predicate(nodeAttribute) is True

        # Should not match Attribute with non-matching value
        nodeAttributeNoMatch = Make.Attribute(Make.Name("other_var"), "method")
        assert predicate(nodeAttributeNoMatch) is False

    def testIsAssignAndTargets0IsPatterns(self) -> None:
        """Test isAssignAndTargets0Is with various target predicates."""
        nodeAssign = Make.Assign(
            targets=[Make.Name("x", context=Make.Store())],
            value=Make.Constant(42)
        )

        # Matching target predicate
        def predicateTargetMatching(node: "ast.AST") -> bool:
            return Be.Name(node) and getattr(node, 'id', None) == "x"
        predicate = IfThis.isAssignAndTargets0Is(predicateTargetMatching)
        assert predicate(nodeAssign) is True

        # Non-matching target predicate
        def predicateTargetWrong(node: "ast.AST") -> bool:
            return Be.Name(node) and getattr(node, 'id', None) == "y"
        predicateWrong = IfThis.isAssignAndTargets0Is(predicateTargetWrong)
        assert predicateWrong(nodeAssign) is False

        # Wrong node type
        nodeName = Make.Name("x")
        assert predicate(nodeName) is False

    def testComplexPredicateComposition(self) -> None:
        """Test complex predicate compositions with real-world scenarios."""
        # Create a function with assignment in body
        nodeFunction = Make.FunctionDef(
            name="test_func",
            body=[Make.Assign(
                targets=[Make.Name("x", context=Make.Store())],
                value=Make.Constant(42)
            )]
        )

        # Complex predicate combining multiple conditions
        predicateComplex = IfThis.isAllOf(
            Be.FunctionDef,
            lambda node: getattr(node, 'name', None) == "test_func",
            lambda node: len(getattr(node, 'body', [])) > 0
        )
        assert predicateComplex(nodeFunction) is True

        # Should fail if any condition doesn't match
        functionDifferent = Make.FunctionDef(name="other_func", body=[Make.Pass()])
        assert predicateComplex(functionDifferent) is False
