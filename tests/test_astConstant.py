"""
Tests for astToolkit.Make.Constant() method and related functionality.
Converted and adapted from CPython's ast module tests.
"""

from astToolkit import Make
import ast
import dis
import pytest

class TestConstant:
    """Tests for the Make.Constant node factory method."""

    def compileConstant(self, value):
        """Helper method to compile a constant value and return the result."""
        tree = ast.parse("x = 123")

        node = tree.body[0].value
        newNode = Make.Constant(value=value)
        ast.copy_location(newNode, node)
        tree.body[0].value = newNode

        code = compile(tree, "<string>", "exec")

        namespace = {}
        exec(code, namespace)
        return namespace["x"]

    def test_validation(self):
        """Test that invalid types raise TypeError."""
        with pytest.raises(TypeError) as excinfo:
            self.compileConstant([1, 2, 3])
        assert "got an invalid type in Constant: list" in str(excinfo.value)

    def test_singletons(self):
        """Test that singleton constants are preserved."""
        singletonConstants = (None, False, True, Ellipsis, b"", frozenset())

        for constantValue in singletonConstants:
            value = self.compileConstant(constantValue)
            assert value is constantValue

    def test_values(self):
        """Test various constant value types."""
        nestedTuple = (1,)
        nestedFrozenset = frozenset({1})
        for level in range(3):
            nestedTuple = (nestedTuple, 2)
            nestedFrozenset = frozenset({nestedFrozenset, 2})

        values = (
            123,
            123.0,
            123j,
            "unicode",
            b"bytes",
            tuple("tuple"),
            frozenset("frozenset"),
            nestedTuple,
            nestedFrozenset,
        )

        for value in values:
            result = self.compileConstant(value)
            assert result == value

    def test_assignToConstant(self):
        """Test that constants cannot be assigned to."""
        tree = ast.parse("x = 1")

        target = tree.body[0].targets[0]
        newTarget = Make.Constant(value=1)
        ast.copy_location(newTarget, target)
        tree.body[0].targets[0] = newTarget

        with pytest.raises(ValueError) as excinfo:
            compile(tree, "string", "exec")
        assert "expression which can't be assigned to in Store context" in str(excinfo.value)

    def test_getDocstring(self):
        """Test ast.get_docstring works with Make.Constant."""
        tree = ast.parse("'docstring'\nx = 1")
        assert ast.get_docstring(tree) == "docstring"

    def test_literalEval(self):
        """Test ast.literal_eval works with Make.Constant."""
        tree = ast.parse("1 + 2")
        binop = tree.body[0].value

        newLeft = Make.Constant(value=10)
        ast.copy_location(newLeft, binop.left)
        binop.left = newLeft

        newRight = Make.Constant(value=20j)
        ast.copy_location(newRight, binop.right)
        binop.right = newRight

        assert ast.literal_eval(binop) == 10 + 20j

    def test_stringKind(self):
        """Test that string kind is properly handled."""
        # Regular string
        constantNode = ast.parse('"x"', mode="eval").body
        assert constantNode.value == "x"
        assert constantNode.kind is None

        # Unicode string (deprecated syntax but still works)
        constantNode = ast.parse('u"x"', mode="eval").body
        assert constantNode.value == "x"
        assert constantNode.kind == "u"

        # Raw string
        constantNode = ast.parse('r"x"', mode="eval").body
        assert constantNode.value == "x"
        assert constantNode.kind is None

        # Bytes
        constantNode = ast.parse('b"x"', mode="eval").body
        assert constantNode.value == b"x"
        assert constantNode.kind is None

    def test_constantCreation(self):
        """Test basic Make.Constant creation."""
        # Test with value only
        constantNode = Make.Constant(42)
        assert constantNode.value == 42
        assert constantNode.kind is None

        # Test with value and kind
        constantNode = Make.Constant("test", kind="u")
        assert constantNode.value == "test"
        assert constantNode.kind == "u"

        # Test with position information
        constantNode = Make.Constant(42, lineno=1, col_offset=0)
        assert constantNode.value == 42
        assert constantNode.lineno == 1
        assert constantNode.col_offset == 0

    def test_constantWithPositionArguments(self):
        """Test Make.Constant with position arguments through **keywordArguments."""
        positionArguments = {
            "lineno": 5,
            "col_offset": 10,
            "end_lineno": 5,
            "end_col_offset": 15
        }

        constantNode = Make.Constant("test", **positionArguments)
        assert constantNode.value == "test"
        assert constantNode.lineno == 5
        assert constantNode.col_offset == 10
        assert constantNode.end_lineno == 5
        assert constantNode.end_col_offset == 15

    @pytest.mark.parametrize("value,expected_type", [
        (42, int),
        (3.14, float),
        (1+2j, complex),
        ("string", str),
        (b"bytes", bytes),
        (True, bool),
        (False, bool),
        (None, type(None)),
        (..., type(...)),
    ])
    def test_constantValueTypes(self, value, expected_type):
        """Test that Make.Constant preserves value types."""
        constantNode = Make.Constant(value)
        assert isinstance(constantNode.value, expected_type)
        assert constantNode.value == value


class TestConstantIntegration:
    """Integration tests for Make.Constant with other AST operations."""

    def test_constantInAssignment(self):
        """Test Make.Constant in assignment contexts."""
        # Create an assignment with Make.Constant
        targetNode = ast.Name("x", ast.Store())
        valueNode = Make.Constant(42)
        assignmentNode = ast.Assign([targetNode], valueNode)

        # Wrap in module and compile
        moduleNode = ast.Module([assignmentNode], [])
        ast.fix_missing_locations(moduleNode)

        code = compile(moduleNode, "<test>", "exec")
        namespace = {}
        exec(code, namespace)

        assert namespace["x"] == 42

    def test_constantInExpression(self):
        """Test Make.Constant in expression contexts."""
        left = Make.Constant(10)
        right = Make.Constant(5)
        binopNode = ast.BinOp(left, ast.Add(), right)

        exprNode = ast.Expression(binopNode)
        ast.fix_missing_locations(exprNode)

        code = compile(exprNode, "<test>", "eval")
        result = eval(code)

        assert result == 15

    def test_constantComparison(self):
        """Test Make.Constant nodes compare correctly."""
        const1 = Make.Constant(42)
        const2 = Make.Constant(42)
        const3 = Make.Constant(43)

        # Test AST dump equality (structural equality)
        assert ast.dump(const1) == ast.dump(const2)
        assert ast.dump(const1) != ast.dump(const3)

        # Test value equality
        assert const1.value == const2.value
        assert const1.value != const3.value
