from astToolkit import Make
from textwrap import dedent
import ast
import pytest

class TestEndPositions:
    """Tests for end position of AST nodes.

    Testing end positions of nodes requires a bit of extra care
    because of how LL parsers work.
    """

    def checkEndPosition(self, astNode, endLineNumber, endColumnOffset):
        assert astNode.end_lineno == endLineNumber
        assert astNode.end_col_offset == endColumnOffset

    def checkContent(self, source, astNode, content):
        assert ast.get_source_segment(source, astNode) == content

    def parseValue(self, sourceString):
        # Use duck-typing to support both single expression
        # and a right hand side of an assignment statement.
        return ast.parse(sourceString).body[0].value

    def testLambda(self):
        sourceString = "lambda x, *y: None"
        lambdaExpression = self.parseValue(sourceString)
        self.checkContent(sourceString, lambdaExpression.body, "None")
        self.checkContent(sourceString, lambdaExpression.args.args[0], "x")
        self.checkContent(sourceString, lambdaExpression.args.vararg, "y")

    def testFunctionDefinition(self):
        sourceString = dedent("""
            def func(x: int,
                     *args: str,
                     z: float = 0,
                     **kwargs: Any) -> bool:
                return True
            """).strip()
        functionDefinition = ast.parse(sourceString).body[0]
        self.checkEndPosition(functionDefinition, 5, 15)
        self.checkContent(sourceString, functionDefinition.body[0], "return True")
        self.checkContent(sourceString, functionDefinition.args.args[0], "x: int")
        self.checkContent(sourceString, functionDefinition.args.args[0].annotation, "int")
        self.checkContent(sourceString, functionDefinition.args.kwarg, "kwargs: Any")
        self.checkContent(sourceString, functionDefinition.args.kwarg.annotation, "Any")

    def testCall(self):
        sourceString = "func(x, y=2, **kw)"
        callExpression = self.parseValue(sourceString)
        self.checkContent(sourceString, callExpression.func, "func")
        self.checkContent(sourceString, callExpression.keywords[0].value, "2")
        self.checkContent(sourceString, callExpression.keywords[1].value, "kw")

    def testCallNoArguments(self):
        sourceString = "x[0]()"
        callExpression = self.parseValue(sourceString)
        self.checkContent(sourceString, callExpression.func, "x[0]")
        self.checkEndPosition(callExpression, 1, 6)

    def testClassDefinition(self):
        sourceString = dedent("""
            class C(A, B):
                x: int = 0
        """).strip()
        classDefinition = ast.parse(sourceString).body[0]
        self.checkEndPosition(classDefinition, 2, 14)
        self.checkContent(sourceString, classDefinition.bases[1], "B")
        self.checkContent(sourceString, classDefinition.body[0], "x: int = 0")

    def testClassKeyword(self):
        sourceString = "class S(metaclass=abc.ABCMeta): pass"
        classDefinition = ast.parse(sourceString).body[0]
        self.checkContent(sourceString, classDefinition.keywords[0].value, "abc.ABCMeta")

    def testMultiLineString(self):
        sourceString = dedent('''
            x = """Some multi-line text.

            It goes on starting from same indent."""
        ''').strip()
        assignmentStatement = ast.parse(sourceString).body[0]
        self.checkEndPosition(assignmentStatement, 3, 40)
        self.checkEndPosition(assignmentStatement.value, 3, 40)

    def testContinuedString(self):
        sourceString = dedent("""
            x = "first part" \\
            "second part"
        """).strip()
        assignmentStatement = ast.parse(sourceString).body[0]
        self.checkEndPosition(assignmentStatement, 2, 13)
        self.checkEndPosition(assignmentStatement.value, 2, 13)

    def testSuites(self):
        # We intentionally put these into the same string to check
        # that empty lines are not part of the suite.
        sourceString = dedent("""
            while True:
                pass

            if one():
                x = None
            elif other():
                y = None
            else:
                z = None

            for x, y in stuff:
                assert True

            try:
                raise RuntimeError
            except TypeError as e:
                pass

            pass
        """).strip()
        moduleAST = ast.parse(sourceString)
        whileLoop = moduleAST.body[0]
        ifStatement = moduleAST.body[1]
        forLoop = moduleAST.body[2]
        tryStatement = moduleAST.body[3]
        passStatement = moduleAST.body[4]

        self.checkEndPosition(whileLoop, 2, 8)
        self.checkEndPosition(ifStatement, 9, 12)
        self.checkEndPosition(forLoop, 12, 15)
        self.checkEndPosition(tryStatement, 17, 8)
        self.checkEndPosition(passStatement, 19, 4)

        self.checkContent(sourceString, whileLoop.test, "True")
        self.checkContent(sourceString, ifStatement.body[0], "x = None")
        self.checkContent(sourceString, ifStatement.orelse[0].test, "other()")
        self.checkContent(sourceString, forLoop.target, "x, y")
        self.checkContent(sourceString, tryStatement.body[0], "raise RuntimeError")
        self.checkContent(sourceString, tryStatement.handlers[0].type, "TypeError")

    def testFormatString(self):
        sourceString = 'x = f"abc {x + y} abc"'
        formatStringExpression = self.parseValue(sourceString)
        binaryOperation = formatStringExpression.values[1].value
        self.checkContent(sourceString, binaryOperation, "x + y")

    def testFormatStringMultiLine(self):
        sourceString = dedent('''
            f"""Some multi-line text.
            {
            arg_one
            +
            arg_two
            }
            It goes on..."""
        ''').strip()
        formatStringExpression = self.parseValue(sourceString)
        binaryOperation = formatStringExpression.values[1].value
        self.checkEndPosition(binaryOperation, 5, 7)
        self.checkContent(sourceString, binaryOperation.left, "arg_one")
        self.checkContent(sourceString, binaryOperation.right, "arg_two")

    def testImportFromMultiLine(self):
        sourceString = dedent("""
            from x.y.z import (
                a, b, c as c
            )
        """).strip()
        importStatement = ast.parse(sourceString).body[0]
        self.checkEndPosition(importStatement, 3, 1)
        self.checkEndPosition(importStatement.names[2], 2, 16)

    def testSlices(self):
        sourceString1 = "f()[1, 2] [0]"
        sourceString2 = "x[ a.b: c.d]"
        sourceStringMultiLine = dedent("""
            x[ a.b: f () ,
               g () : c.d
              ]
        """).strip()
        index1, index2, indexMultiLine = map(self.parseValue, (sourceString1, sourceString2, sourceStringMultiLine))
        self.checkContent(sourceString1, index1.value, "f()[1, 2]")
        self.checkContent(sourceString1, index1.value.slice, "1, 2")
        self.checkContent(sourceString2, index2.slice.lower, "a.b")
        self.checkContent(sourceString2, index2.slice.upper, "c.d")
        self.checkContent(sourceStringMultiLine, indexMultiLine.slice.elts[0].upper, "f ()")
        self.checkContent(sourceStringMultiLine, indexMultiLine.slice.elts[1].lower, "g ()")
        self.checkEndPosition(indexMultiLine, 3, 3)

    def testBinaryOperation(self):
        sourceString = dedent("""
            (1 * 2 + (3 ) +
                 4
            )
        """).strip()
        binaryOperation = self.parseValue(sourceString)
        self.checkEndPosition(binaryOperation, 2, 6)
        self.checkContent(sourceString, binaryOperation.right, "4")
        self.checkContent(sourceString, binaryOperation.left, "1 * 2 + (3 )")
        self.checkContent(sourceString, binaryOperation.left.right, "3")

    def testBooleanOperation(self):
        sourceString = dedent("""
            if (one_condition and
                    (other_condition or yet_another_one)):
                pass
        """).strip()
        booleanOperation = ast.parse(sourceString).body[0].test
        self.checkEndPosition(booleanOperation, 2, 44)
        self.checkContent(sourceString, booleanOperation.values[1], "other_condition or yet_another_one")

    def testTuples(self):
        sourceString1 = "x = () ;"
        sourceString2 = "x = 1 , ;"
        sourceString3 = "x = (1 , 2 ) ;"
        sourceStringMultiLine = dedent("""
            x = (
                a, b,
            )
        """).strip()
        tuple1, tuple2, tuple3, tupleMultiLine = map(self.parseValue, (sourceString1, sourceString2, sourceString3, sourceStringMultiLine))
        self.checkContent(sourceString1, tuple1, "()")
        self.checkContent(sourceString2, tuple2, "1 ,")
        self.checkContent(sourceString3, tuple3, "(1 , 2 )")
        self.checkEndPosition(tupleMultiLine, 3, 1)

    def testAttributeSpaces(self):
        sourceString = "func(x. y .z)"
        callExpression = self.parseValue(sourceString)
        self.checkContent(sourceString, callExpression, sourceString)
        self.checkContent(sourceString, callExpression.args[0], "x. y .z")

    def testRedundantParenthesis(self):
        sourceString = "( ( ( a + b ) ) )"
        valueExpression = ast.parse(sourceString).body[0].value
        assert type(valueExpression).__name__ == "BinOp"
        self.checkContent(sourceString, valueExpression, "a + b")
        sourceString2 = "await " + sourceString
        valueExpression = ast.parse(sourceString2).body[0].value.value
        assert type(valueExpression).__name__ == "BinOp"
        self.checkContent(sourceString2, valueExpression, "a + b")

    def testTrailersWithRedundantParenthesis(self):
        testCases = (
            ("( ( ( a ) ) ) ( )", "Call"),
            ("( ( ( a ) ) ) ( b )", "Call"),
            ("( ( ( a ) ) ) [ b ]", "Subscript"),
            ("( ( ( a ) ) ) . b", "Attribute"),
        )
        for sourceString, nodeType in testCases:
            valueExpression = ast.parse(sourceString).body[0].value
            assert type(valueExpression).__name__ == nodeType
            self.checkContent(sourceString, valueExpression, sourceString)
            sourceString2 = "await " + sourceString
            valueExpression = ast.parse(sourceString2).body[0].value.value
            assert type(valueExpression).__name__ == nodeType
            self.checkContent(sourceString2, valueExpression, sourceString)

    def testDisplays(self):
        sourceString1 = "[{}, {1, }, {1, 2,} ]"
        sourceString2 = "{a: b, f (): g () ,}"
        collection1 = self.parseValue(sourceString1)
        collection2 = self.parseValue(sourceString2)
        self.checkContent(sourceString1, collection1.elts[0], "{}")
        self.checkContent(sourceString1, collection1.elts[1], "{1, }")
        self.checkContent(sourceString1, collection1.elts[2], "{1, 2,}")
        self.checkContent(sourceString2, collection2.keys[1], "f ()")
        self.checkContent(sourceString2, collection2.values[1], "g ()")

    def testComprehensions(self):
        sourceString = dedent("""
            x = [{x for x, y in stuff
                  if cond.x} for stuff in things]
        """).strip()
        comprehension = self.parseValue(sourceString)
        self.checkEndPosition(comprehension, 2, 37)
        self.checkContent(sourceString, comprehension.generators[0].iter, "things")
        self.checkContent(sourceString, comprehension.elt.generators[0].iter, "stuff")
        self.checkContent(sourceString, comprehension.elt.generators[0].ifs[0], "cond.x")
        self.checkContent(sourceString, comprehension.elt.generators[0].target, "x, y")

    def testYieldAwait(self):
        sourceString = dedent("""
            async def f():
                yield x
                await y
        """).strip()
        functionDefinition = ast.parse(sourceString).body[0]
        self.checkContent(sourceString, functionDefinition.body[0].value, "yield x")
        self.checkContent(sourceString, functionDefinition.body[1].value, "await y")

    def testSourceSegmentMulti(self):
        sourceStringOriginal = dedent("""
            x = (
                a, b,
            ) + ()
        """).strip()
        sourceStringTuple = dedent("""
            (
                a, b,
            )
        """).strip()
        binaryOperation = self.parseValue(sourceStringOriginal)
        assert ast.get_source_segment(sourceStringOriginal, binaryOperation.left) == sourceStringTuple

    def testSourceSegmentPadded(self):
        sourceStringOriginal = dedent("""
            class C:
                def fun(self) -> None:
                    "ЖЖЖЖЖ"
        """).strip()
        sourceStringMethod = "    def fun(self) -> None:\n" '        "ЖЖЖЖЖ"'
        classDefinition = ast.parse(sourceStringOriginal).body[0]
        assert ast.get_source_segment(sourceStringOriginal, classDefinition.body[0], padded=True) == sourceStringMethod

    def testSourceSegmentEndings(self):
        sourceString = "v = 1\r\nw = 1\nx = 1\n\ry = 1\rz = 1\r\n"
        variableV, variableW, variableX, variableY, variableZ = ast.parse(sourceString).body
        self.checkContent(sourceString, variableV, "v = 1")
        self.checkContent(sourceString, variableW, "w = 1")
        self.checkContent(sourceString, variableX, "x = 1")
        self.checkContent(sourceString, variableY, "y = 1")
        self.checkContent(sourceString, variableZ, "z = 1")

    def testSourceSegmentTabs(self):
        sourceString = dedent("""
            class C:
              \t\f  def fun(self) -> None:
              \t\f      pass
        """).strip()
        sourceStringMethod = "  \t\f  def fun(self) -> None:\n" "  \t\f      pass"

        classDefinition = ast.parse(sourceString).body[0]
        assert ast.get_source_segment(sourceString, classDefinition.body[0], padded=True) == sourceStringMethod

    def testSourceSegmentNewlines(self):
        sourceString = "def f():\n  pass\ndef g():\r  pass\r\ndef h():\r\n  pass\r\n"
        functionF, functionG, functionH = ast.parse(sourceString).body
        self.checkContent(sourceString, functionF, "def f():\n  pass")
        self.checkContent(sourceString, functionG, "def g():\r  pass")
        self.checkContent(sourceString, functionH, "def h():\r\n  pass")
