"""
Tests for AST optimization functionality.
Converted and adapted from CPython's ASTOptimizationTests.
"""

import ast
import pytest
import sys

class TestASTOptimization:
    """Tests for AST optimization during parsing."""

    def wrapExpression(self, expression):
        """Wrap an expression in a Module for testing."""
        return ast.Module(body=[ast.Expr(value=expression)], type_ignores=[])

    def wrapStatement(self, statement):
        """Wrap a statement in a Module for testing."""
        return ast.Module(body=[statement], type_ignores=[])

    def assertASTOptimization(self, code, nonOptimizedTarget, optimizedTarget):
        """Assert that optimization produces expected results."""
        if sys.version_info >= (3, 13):
            nonOptimizedTree = ast.parse(code, optimize=-1)
            optimizedTree = ast.parse(code, optimize=1)
        else:
            # On older Python versions, optimization is not available
            pytest.skip("AST optimization requires Python 3.13+")

        # Compare non-optimized tree with target
        assert ast.dump(nonOptimizedTree) == ast.dump(nonOptimizedTarget), \
            f"{ast.dump(nonOptimizedTarget)} must equal {ast.dump(nonOptimizedTree)}"

        # Optimized tree should be different from non-optimized
        assert ast.dump(optimizedTree) != ast.dump(nonOptimizedTree), \
            "Optimized tree should differ from non-optimized tree"

        # Compare optimized tree with target
        assert ast.dump(optimizedTree) == ast.dump(optimizedTarget), \
            f"{ast.dump(optimizedTarget)} must equal {ast.dump(optimizedTree)}"

    def testFoldingFormat(self):
        """Test constant folding in format strings."""
        code = "f'{1 + 2}'"

        nonOptimizedTarget = self.wrapExpression(
            ast.JoinedStr(values=[
                ast.FormattedValue(
                    value=ast.BinOp(
                        left=ast.Constant(value=1),
                        op=ast.Add(),
                        right=ast.Constant(value=2)
                    ),
                    conversion=-1,
                    format_spec=None
                )
            ])
        )

        optimizedTarget = self.wrapExpression(
            ast.JoinedStr(values=[
                ast.FormattedValue(
                    value=ast.Constant(value=3),
                    conversion=-1,
                    format_spec=None
                )
            ])
        )

        self.assertASTOptimization(code, nonOptimizedTarget, optimizedTarget)

    def testConstantFolding(self):
        """Test basic constant folding operations."""
        testCases = [
            # Binary operations
            ("1 + 2", ast.BinOp(ast.Constant(1), ast.Add(), ast.Constant(2)), ast.Constant(3)),
            ("3 * 4", ast.BinOp(ast.Constant(3), ast.Mult(), ast.Constant(4)), ast.Constant(12)),
            ("10 - 3", ast.BinOp(ast.Constant(10), ast.Sub(), ast.Constant(3)), ast.Constant(7)),
            ("8 / 2", ast.BinOp(ast.Constant(8), ast.Div(), ast.Constant(2)), ast.Constant(4.0)),

            # Unary operations
            ("-5", ast.UnaryOp(ast.USub(), ast.Constant(5)), ast.Constant(-5)),
            ("+7", ast.UnaryOp(ast.UAdd(), ast.Constant(7)), ast.Constant(7)),
            ("~1", ast.UnaryOp(ast.Invert(), ast.Constant(1)), ast.Constant(-2)),
        ]

        for code, nonOptExpr, optExpr in testCases:
            nonOptTarget = self.wrapExpression(nonOptExpr)
            optTarget = self.wrapExpression(optExpr)
            self.assertASTOptimization(code, nonOptTarget, optTarget)

    def testNoOptimizationCases(self):
        """Test cases where optimization should not occur."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        # Division by zero should not be optimized
        code = "1 / 0"
        tree = ast.parse(code, optimize=1)
        expr = tree.body[0].value
        assert isinstance(expr, ast.BinOp)
        assert isinstance(expr.left, ast.Constant) and expr.left.value == 1
        assert isinstance(expr.op, ast.Div)
        assert isinstance(expr.right, ast.Constant) and expr.right.value == 0

        # Variables should not be folded
        code = "x + y"
        tree = ast.parse(code, optimize=1)
        expr = tree.body[0].value
        assert isinstance(expr, ast.BinOp)
        assert isinstance(expr.left, ast.Name) and expr.left.id == "x"
        assert isinstance(expr.right, ast.Name) and expr.right.id == "y"

    def testBooleanOptimization(self):
        """Test boolean operation optimization."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        # Test True and False folding - note that boolean ops aren't actually optimized this way
        code = "True and False"
        nonOptimizedTree = ast.parse(code, optimize=-1)
        optimizedTree = ast.parse(code, optimize=1)

        # In reality, boolean expressions like "True and False" don't get optimized
        # by the AST parser, so both should be the same
        nonOptExpr = nonOptimizedTree.body[0].value
        optExpr = optimizedTree.body[0].value

        assert isinstance(nonOptExpr, ast.BoolOp)
        assert isinstance(optExpr, ast.BoolOp)  # Not optimized at parse time

    def testStringConcatenation(self):
        """Test string concatenation optimization."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "'hello' + ' world'"

        nonOptimizedTree = ast.parse(code, optimize=-1)
        optimizedTree = ast.parse(code, optimize=1)

        nonOptExpr = nonOptimizedTree.body[0].value
        optExpr = optimizedTree.body[0].value

        # Non-optimized should be BinOp
        assert isinstance(nonOptExpr, ast.BinOp)
        assert isinstance(nonOptExpr.left, ast.Constant)
        assert nonOptExpr.left.value == 'hello'

        # Optimized creates a JoinedStr with the concatenated value
        assert isinstance(optExpr, ast.JoinedStr)
        assert len(optExpr.values) == 1
        assert isinstance(optExpr.values[0], ast.Constant)
        assert optExpr.values[0].value == 'hello world'

    def testTupleOptimization(self):
        """Test tuple constant optimization."""
        code = "(1, 2, 3)"
        nonOptTarget = self.wrapExpression(
            ast.Tuple(elts=[ast.Constant(1), ast.Constant(2), ast.Constant(3)], ctx=ast.Load())
        )
        # Tuples with only constants can be optimized
        optTarget = self.wrapExpression(ast.Constant((1, 2, 3)))
        self.assertASTOptimization(code, nonOptTarget, optTarget)


class TestBasicOptimizationBehavior:
    """Tests for basic AST optimization behavior."""

    def testSimpleConstantFolding(self):
        """Test that simple arithmetic gets optimized."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "2 + 3"

        nonOptTree = ast.parse(code, optimize=-1)
        optTree = ast.parse(code, optimize=1)

        # Non-optimized should have BinOp
        nonOptExpr = nonOptTree.body[0].value
        assert isinstance(nonOptExpr, ast.BinOp)

        # Optimized should have Constant
        optExpr = optTree.body[0].value
        assert isinstance(optExpr, ast.Constant)
        assert optExpr.value == 5

    def testComplexExpression(self):
        """Test that complex expressions aren't always optimized."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "x + 1"

        nonOptTree = ast.parse(code, optimize=-1)
        optTree = ast.parse(code, optimize=1)

        # Both should have BinOp since x is a variable
        nonOptExpr = nonOptTree.body[0].value
        optExpr = optTree.body[0].value

        assert isinstance(nonOptExpr, ast.BinOp)
        assert isinstance(optExpr, ast.BinOp)


class TestOptimizationLevels:
    """Tests for different optimization levels."""

    def testOptimizeNegativeOne(self):
        """Test that optimize=-1 disables all optimizations."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "1 + 2"
        tree = ast.parse(code, optimize=-1)
        expr = tree.body[0].value

        assert isinstance(expr, ast.BinOp)
        assert isinstance(expr.left, ast.Constant) and expr.left.value == 1
        assert isinstance(expr.op, ast.Add)
        assert isinstance(expr.right, ast.Constant) and expr.right.value == 2

    def testOptimizeZero(self):
        """Test that optimize=0 disables optimizations."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "1 + 2"
        tree = ast.parse(code, optimize=0)
        expr = tree.body[0].value

        # At level 0, optimizations are disabled
        assert isinstance(expr, ast.BinOp)
        assert isinstance(expr.left, ast.Constant) and expr.left.value == 1
        assert isinstance(expr.op, ast.Add)
        assert isinstance(expr.right, ast.Constant) and expr.right.value == 2

    def testOptimizeOne(self):
        """Test that optimize=1 enables optimizations."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "1 + 2"
        tree = ast.parse(code, optimize=1)
        expr = tree.body[0].value

        assert isinstance(expr, ast.Constant)
        assert expr.value == 3

    def testOptimizeTwo(self):
        """Test that optimize=2 enables maximum optimizations."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = "__debug__"
        tree = ast.parse(code, optimize=2)
        expr = tree.body[0].value

        # __debug__ should be optimized to False at level 2
        assert isinstance(expr, ast.Constant)
        assert expr.value is False


class TestDocstringOptimization:
    """Tests for docstring optimization behavior."""

    def testModuleDocstring(self):
        """Test that module docstrings are preserved."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = '"Module docstring"'
        tree = ast.parse(code, optimize=1)

        # Docstrings should remain as string constants, not optimized away
        assert len(tree.body) == 1
        expr = tree.body[0]
        assert isinstance(expr, ast.Expr)
        assert isinstance(expr.value, ast.Constant)
        assert expr.value.value == "Module docstring"

    def testFunctionDocstring(self):
        """Test that function docstrings are preserved."""
        if sys.version_info < (3, 13):
            pytest.skip("AST optimization requires Python 3.13+")

        code = '''
def func():
    "Function docstring"
    pass
'''
        tree = ast.parse(code, optimize=1)
        funcDef = tree.body[0]

        # First statement should be the docstring
        assert len(funcDef.body) == 2
        docstring = funcDef.body[0]
        assert isinstance(docstring, ast.Expr)
        assert isinstance(docstring.value, ast.Constant)
        assert docstring.value.value == "Function docstring"
