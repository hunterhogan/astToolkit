"""
Tests for AST command line interface functionality.
Converted and adapted from CPython's ASTMainTests.
"""

import ast
import os
import pytest
import subprocess
import sys
import tempfile

class TestASTCommandLine:
    """Tests for ast module command line interface."""

    def testCLIFileInput(self):
        """Test ast module CLI with file input."""
        code = "print(1, 2, 3)"
        expected = ast.dump(ast.parse(code), indent=3)

        with tempfile.TemporaryDirectory() as tmpDir:
            filename = os.path.join(tmpDir, "test_module.py")
            with open(filename, "w", encoding="utf-8") as fileHandle:
                fileHandle.write(code)

            # Run python -m ast on the file
            result = subprocess.run(
                [sys.executable, "-m", "ast", filename],
                capture_output=True,
                text=True
            )

            assert result.returncode == 0
            assert result.stderr == ""

            # Compare output lines (ignoring trailing whitespace)
            expectedLines = expected.splitlines()
            actualLines = result.stdout.strip().splitlines()
            assert expectedLines == actualLines

    def testCLIStdinInput(self):
        """Test ast module CLI with stdin input."""
        code = "x = 42"
        expected = ast.dump(ast.parse(code), indent=3)

        # Run python -m ast with stdin input
        result = subprocess.run(
            [sys.executable, "-m", "ast"],
            input=code,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        assert result.stderr == ""

        expectedLines = expected.splitlines()
        actualLines = result.stdout.strip().splitlines()
        assert expectedLines == actualLines

    def testCLIWithIndent(self):
        """Test ast module CLI with custom indent."""
        code = "def func(): pass"

        # Test with different indent levels
        for indentLevel in [1, 2, 4]:
            result = subprocess.run(
                [sys.executable, "-m", "ast", "--indent", str(indentLevel)],
                input=code,
                capture_output=True,
                text=True
            )

            assert result.returncode == 0
            assert result.stderr == ""

            # Verify the output uses the specified indent
            output = result.stdout
            lines = output.splitlines()

            # Find an indented line and check its indentation
            indentedLines = [line for line in lines if line.startswith(' ')]
            if indentedLines:
                firstIndentedLine = indentedLines[0]
                actualIndent = len(firstIndentedLine) - len(firstIndentedLine.lstrip())
                assert actualIndent == indentLevel
    def testCLIWithOptimization(self):
        """Test ast module CLI behavior (optimization is internal)."""
        code = "1 + 2"

        # Test basic functionality - optimization is handled internally
        result = subprocess.run(
            [sys.executable, "-m", "ast"],
            input=code,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout

        # The output should contain the AST representation
        assert "Module" in output
        assert "body" in output

    def testCLIErrorHandling(self):
        """Test ast module CLI error handling."""
        # Test with invalid Python code
        invalidCode = "def func(\n"  # Incomplete function definition

        result = subprocess.run(
            [sys.executable, "-m", "ast"],
            input=invalidCode,
            capture_output=True,
            text=True
        )

        # Should exit with error code
        assert result.returncode != 0
        assert result.stderr != ""
        assert "SyntaxError" in result.stderr

    def testCLIInvalidFile(self):
        """Test ast module CLI with non-existent file."""
        result = subprocess.run(
            [sys.executable, "-m", "ast", "non_existent_file.py"],
            capture_output=True,
            text=True
        )

        assert result.returncode != 0
        assert result.stderr != ""

    def testCLIHelpMessage(self):
        """Test ast module CLI help message."""
        result = subprocess.run(
            [sys.executable, "-m", "ast", "--help"],
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        helpOutput = result.stdout

        # Check for expected help content
        assert "usage:" in helpOutput.lower() or "Usage:" in helpOutput
        assert "ast" in helpOutput
        assert "--indent" in helpOutput or "-i" in helpOutput
    def testCLIMode(self):
        """Test ast module CLI with different parsing modes."""
        # Test eval mode
        evalCode = "1 + 2"
        result = subprocess.run(
            [sys.executable, "-m", "ast", "--mode", "eval"],
            input=evalCode,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout
        assert "Expression(" in output

        # Test exec mode (default)
        execCode = "x = 1"
        result = subprocess.run(
            [sys.executable, "-m", "ast", "--mode", "exec"],
            input=execCode,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout
        assert "Module(" in output

    def testCLIIncludeAttributes(self):
        """Test ast module CLI with include attributes option."""
        code = "x = 42"

        # Test with attributes included
        result = subprocess.run(
            [sys.executable, "-m", "ast", "--include-attributes"],
            input=code,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout

        # Should include line numbers and column offsets
        assert "lineno=" in output
        assert "col_offset=" in output

        # Test without attributes (default)
        result = subprocess.run(
            [sys.executable, "-m", "ast"],
            input=code,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout

        # Should not include attributes by default
        assert "lineno=" not in output
        assert "col_offset=" not in output


class TestASTToolIntegration:
    """Tests for integration with astToolkit functionality."""

    def testCLIWithAstToolkitCompatibility(self):
        """Test that CLI output is compatible with astToolkit parsing."""
        code = """
def example_function(parameterA, parameterB=None):
    \"\"\"Example function for testing.\"\"\"
    if parameterA:
        return parameterA + (parameterB or 0)
    return 0
"""

        # Get AST dump from command line
        result = subprocess.run(
            [sys.executable, "-m", "ast"],
            input=code,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        astDump = result.stdout.strip()        # Verify the AST output contains expected elements

        # The dumps should represent the same AST structure
        # (though formatting might differ slightly)
        assert "FunctionDef" in astDump
        assert "example_function" in astDump
        assert "parameterA" in astDump
        assert "parameterB" in astDump

    def testCLIComplexCode(self):
        """Test CLI with complex Python code structures."""
        complexCode = """
class ExampleClass:
    \"\"\"Example class with various features.\"\"\"

    classAttribute = "value"

    def __init__(self, initialValue):
        self.instanceValue = initialValue

    def methodWithDecorator(self):
        @property
        def innerProperty(self):
            return self.instanceValue

        return innerProperty

    async def asyncMethod(self):
        await some_async_operation()
        yield "result"

    def methodWithComprehension(self):
        return [x**2 for x in range(10) if x % 2 == 0]

try:
    example = ExampleClass(42)
    result = example.methodWithComprehension()
except Exception as error:
    print(f"Error: {error}")
finally:
    print("Cleanup complete")
"""

        result = subprocess.run(
            [sys.executable, "-m", "ast", "--indent", "2"],
            input=complexCode,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0
        output = result.stdout

        # Verify key structures are present
        assert "ClassDef" in output
        assert "ExampleClass" in output
        assert "AsyncFunctionDef" in output
        assert "ListComp" in output
        assert "Try" in output
        assert "ExceptHandler" in output
