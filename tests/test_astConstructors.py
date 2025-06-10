"""
Tests for astToolkit.Make AST constructor methods.
Converted and adapted from CPython's ast module tests.
"""

from astToolkit import Make
import ast
import pytest
import warnings

class TestASTConstructors:
    """Tests for Make factory methods that construct AST nodes."""

    def test_functionDef(self):
        """Test Make.FunctionDef constructor."""
        argumentSpecification = Make.arguments()
        assert argumentSpecification.args == []
        assert argumentSpecification.posonlyargs == []

        # Test basic function definition
        functionNode = Make.FunctionDef(name="foo", argumentSpecification=argumentSpecification)
        assert functionNode.name == "foo"
        assert functionNode.decorator_list == []
        assert functionNode.body == []
        assert functionNode.returns is None

    def test_functionDefWithBody(self):
        """Test Make.FunctionDef with body statements."""
        argumentSpecification = Make.arguments()
        bodyStatement = Make.Pass()

        functionNode = Make.FunctionDef(
            name="testFunction",
            argumentSpecification=argumentSpecification,
            body=[bodyStatement]
        )

        assert functionNode.name == "testFunction"
        assert len(functionNode.body) == 1
        assert isinstance(functionNode.body[0], ast.Pass)

    def test_functionDefWithDecorators(self):
        """Test Make.FunctionDef with decorators."""
        argumentSpecification = Make.arguments()
        decoratorNode = Make.Name("decorator", ast.Load())

        functionNode = Make.FunctionDef(
            name="decoratedFunction",
            argumentSpecification=argumentSpecification,
            decorator_list=[decoratorNode]        )
        assert functionNode.name == "decoratedFunction"
        assert len(functionNode.decorator_list) == 1
        assert isinstance(functionNode.decorator_list[0], ast.Name)
        assert functionNode.decorator_list[0].id == "decorator"

    def test_functionDefWithReturns(self):
        """Test Make.FunctionDef with return type annotation."""
        argumentSpecification = Make.arguments()
        returnAnnotation = Make.Name("int", ast.Load())

        functionNode = Make.FunctionDef(
            name="typedFunction",
            argumentSpecification=argumentSpecification,
            returns=returnAnnotation
        )

        assert functionNode.name == "typedFunction"
        assert functionNode.returns.id == "int"

    def test_nameExpressionContext(self):
        """Test Make Name nodes with different expression contexts."""
        # Default context should be Load
        nameNode = Make.Name("x")
        assert nameNode.id == "x"
        assert isinstance(nameNode.ctx, ast.Load)

        # Explicit Store context
        nameNode2 = Make.Name("x", ast.Store())
        assert nameNode2.id == "x"
        assert isinstance(nameNode2.ctx, ast.Store)

        # Explicit Del context via keyword
        nameNode3 = Make.Name("x", context=ast.Del())
        assert nameNode3.id == "x"
        assert isinstance(nameNode3.ctx, ast.Del)

    def test_arguments(self):
        """Test Make.arguments constructor."""
        # Empty arguments
        argumentsNode = Make.arguments()
        assert argumentsNode.posonlyargs == []
        assert argumentsNode.args == []
        assert argumentsNode.vararg is None
        assert argumentsNode.kwonlyargs == []
        assert argumentsNode.kw_defaults == []
        assert argumentsNode.kwarg is None
        assert argumentsNode.defaults == []

        # Arguments with parameters
        argNode = Make.arg("parameterName")
        argumentsNode = Make.arguments(
            list_arg=[argNode],
            defaults=[Make.Constant(42)]
        )

        assert len(argumentsNode.args) == 1
        assert argumentsNode.args[0].arg == "parameterName"
        assert len(argumentsNode.defaults) == 1
        assert argumentsNode.defaults[0].value == 42

    def test_arg(self):
        """Test Make.arg constructor."""
        # Basic argument
        argNode = Make.arg("argumentName")
        assert argNode.arg == "argumentName"
        assert argNode.annotation is None

        # Argument with annotation
        annotationNode = Make.Name("int", ast.Load())
        argNode = Make.arg("typedArgument", annotation=annotationNode)
        assert argNode.arg == "typedArgument"
        assert argNode.annotation.id == "int"

    def test_classDef(self):
        """Test Make.ClassDef constructor."""
        # Basic class
        classNode = Make.ClassDef(name="TestClass")
        assert classNode.name == "TestClass"
        assert classNode.bases == []
        assert classNode.keywords == []
        assert classNode.decorator_list == []
        assert classNode.body == []

        # Class with base
        baseNode = Make.Name("BaseClass", ast.Load())
        classNode = Make.ClassDef(name="DerivedClass", bases=[baseNode])
        assert classNode.name == "DerivedClass"
        assert len(classNode.bases) == 1
        assert classNode.bases[0].id == "BaseClass"

    def test_assign(self):
        """Test Make.Assign constructor."""
        targetNode = Make.Name("variable", ast.Store())
        valueNode = Make.Constant(42)

        assignNode = Make.Assign([targetNode], valueNode)
        assert len(assignNode.targets) == 1
        assert assignNode.targets[0].id == "variable"
        assert assignNode.value.value == 42

    def test_annAssign(self):
        """Test Make.AnnAssign constructor."""
        targetNode = Make.Name("variable", ast.Store())
        annotationNode = Make.Name("int", ast.Load())
        valueNode = Make.Constant(42)

        annAssignNode = Make.AnnAssign(targetNode, annotationNode, valueNode)
        assert annAssignNode.target.id == "variable"
        assert annAssignNode.annotation.id == "int"
        assert annAssignNode.value.value == 42

    def test_augAssign(self):
        """Test Make.AugAssign constructor."""
        targetNode = Make.Name("variable", ast.Store())
        operatorNode = ast.Add()
        valueNode = Make.Constant(1)

        augAssignNode = Make.AugAssign(targetNode, operatorNode, valueNode)
        assert augAssignNode.target.id == "variable"
        assert isinstance(augAssignNode.op, ast.Add)
        assert augAssignNode.value.value == 1

    def test_call(self):
        """Test Make.Call constructor."""
        calleeNode = Make.Name("function", ast.Load())
        argNode = Make.Constant(42)

        callNode = Make.Call(calleeNode, [argNode])
        assert callNode.func.id == "function"
        assert len(callNode.args) == 1
        assert callNode.args[0].value == 42
        assert callNode.keywords == []

    def test_callWithKeywords(self):
        """Test Make.Call with keyword arguments."""
        calleeNode = Make.Name("function", ast.Load())
        keywordNode = ast.keyword("param", Make.Constant(42))

        callNode = Make.Call(calleeNode, [], [keywordNode])
        assert callNode.func.id == "function"
        assert callNode.args == []
        assert len(callNode.keywords) == 1
        assert callNode.keywords[0].arg == "param"
        assert callNode.keywords[0].value.value == 42

    def test_attribute(self):
        """Test Make.Attribute constructor."""
        valueNode = Make.Name("object", ast.Load())

        # Single attribute
        attributeNode = Make.Attribute(valueNode, "method")
        assert attributeNode.value.id == "object"
        assert attributeNode.attr == "method"
        assert isinstance(attributeNode.ctx, ast.Load)

        # Multiple chained attributes (using variadic parameters)
        attributeNode = Make.Attribute(valueNode, "attr1", "attr2")
        # This should create object.attr1.attr2
        assert attributeNode.attr == "attr2"
        assert attributeNode.value.attr == "attr1"
        assert attributeNode.value.value.id == "object"

    def test_binOp(self):
        """Test Make.BinOp constructor."""
        leftNode = Make.Constant(10)
        rightNode = Make.Constant(5)
        operatorNode = ast.Add()

        binOpNode = Make.BinOp(leftNode, operatorNode, rightNode)
        assert binOpNode.left.value == 10
        assert isinstance(binOpNode.op, ast.Add)
        assert binOpNode.right.value == 5

    def test_boolOp(self):
        """Test Make.BoolOp constructor."""
        value1 = Make.Constant(True)
        value2 = Make.Constant(False)
        operatorNode = ast.And()

        boolOpNode = Make.BoolOp(operatorNode, [value1, value2])
        assert isinstance(boolOpNode.op, ast.And)
        assert len(boolOpNode.values) == 2
        assert boolOpNode.values[0].value is True
        assert boolOpNode.values[1].value is False

    def test_compare(self):
        """Test Make.Compare constructor."""
        leftNode = Make.Constant(5)
        rightNode = Make.Constant(10)
        operatorNode = ast.Lt()

        compareNode = Make.Compare(leftNode, [operatorNode], [rightNode])
        assert compareNode.left.value == 5
        assert len(compareNode.ops) == 1
        assert isinstance(compareNode.ops[0], ast.Lt)
        assert len(compareNode.comparators) == 1
        assert compareNode.comparators[0].value == 10

    def test_ifStatement(self):
        """Test Make.If constructor."""
        testNode = Make.Constant(True)
        bodyNode = Make.Pass()

        ifNode = Make.If(testNode, [bodyNode])
        assert ifNode.test.value is True
        assert len(ifNode.body) == 1
        assert isinstance(ifNode.body[0], ast.Pass)
        assert ifNode.orelse == []

    def test_ifStatementWithElse(self):
        """Test Make.If with else clause."""
        testNode = Make.Constant(True)
        bodyNode = Make.Pass()
        elseNode = Make.Pass()

        ifNode = Make.If(testNode, [bodyNode], [elseNode])
        assert ifNode.test.value is True
        assert len(ifNode.body) == 1
        assert len(ifNode.orelse) == 1
        assert isinstance(ifNode.orelse[0], ast.Pass)

    def test_forLoop(self):
        """Test Make.For constructor."""
        targetNode = Make.Name("item", ast.Store())
        iterNode = Make.Name("items", ast.Load())
        bodyNode = Make.Pass()

        forNode = Make.For(targetNode, iterNode, [bodyNode])
        assert forNode.target.id == "item"
        assert forNode.iter.id == "items"
        assert len(forNode.body) == 1
        assert isinstance(forNode.body[0], ast.Pass)
        assert forNode.orelse == []

    def test_whileLoop(self):
        """Test Make.While constructor."""
        testNode = Make.Constant(True)
        bodyNode = Make.Pass()

        whileNode = Make.While(testNode, [bodyNode])
        assert whileNode.test.value is True
        assert len(whileNode.body) == 1
        assert isinstance(whileNode.body[0], ast.Pass)
        assert whileNode.orelse == []

    def test_withStatement(self):
        """Test Make.With constructor."""
        contextExpr = Make.Name("context", ast.Load())
        withItem = ast.withitem(contextExpr, None)
        bodyNode = Make.Pass()

        withNode = Make.With([withItem], [bodyNode])
        assert len(withNode.items) == 1
        assert withNode.items[0].context_expr.id == "context"
        assert withNode.items[0].optional_vars is None
        assert len(withNode.body) == 1
        assert isinstance(withNode.body[0], ast.Pass)


class TestMakePositionalArguments:
    """Tests for positional argument handling in Make methods."""

    def test_constantWithPositionalArguments(self):
        """Test that Make.Constant properly handles **keywordArguments."""
        positionInfo = {
            "lineno": 1,
            "col_offset": 0,
            "end_lineno": 1,
            "end_col_offset": 2
        }

        constantNode = Make.Constant(42, **positionInfo)
        assert constantNode.value == 42
        assert constantNode.lineno == 1
        assert constantNode.col_offset == 0
        assert constantNode.end_lineno == 1
        assert constantNode.end_col_offset == 2

    def test_nameWithPositionalArguments(self):
        """Test that Make.Name properly handles **keywordArguments."""
        positionInfo = {
            "lineno": 5,
            "col_offset": 10
        }

        nameNode = Make.Name("variable", **positionInfo)
        assert nameNode.id == "variable"
        assert nameNode.lineno == 5
        assert nameNode.col_offset == 10

    def test_functionDefWithPositionalArguments(self):
        """Test that Make.FunctionDef properly handles **keywordArguments."""
        positionInfo = {
            "lineno": 1,
            "col_offset": 0,
            "type_comment": "# type: ignore"
        }

        argumentSpecification = Make.arguments()
        functionNode = Make.FunctionDef(
            name="testFunction",
            argumentSpecification=argumentSpecification,
            **positionInfo
        )

        assert functionNode.name == "testFunction"
        assert functionNode.lineno == 1
        assert functionNode.col_offset == 0
        assert functionNode.type_comment == "# type: ignore"


@pytest.mark.parametrize("makeMethodName,expectedAstType", [
    ("Constant", ast.Constant),
    ("Name", ast.Name),
    ("BinOp", ast.BinOp),
    ("BoolOp", ast.BoolOp),
    ("Compare", ast.Compare),
    ("Call", ast.Call),
    ("Attribute", ast.Attribute),
    ("FunctionDef", ast.FunctionDef),
    ("ClassDef", ast.ClassDef),
    ("If", ast.If),
    ("For", ast.For),
    ("While", ast.While),
    ("Assign", ast.Assign),
    ("AnnAssign", ast.AnnAssign),
    ("AugAssign", ast.AugAssign),
])
def test_makeMethodsReturnCorrectTypes(makeMethodName, expectedAstType):
    """Test that Make methods return the correct AST node types."""
    makeMethod = getattr(Make, makeMethodName)

    # Create nodes with minimal required arguments
    if makeMethodName == "Constant":
        node = makeMethod(42)
    elif makeMethodName == "Name":
        node = makeMethod("test")
    elif makeMethodName == "BinOp":
        node = makeMethod(Make.Constant(1), ast.Add(), Make.Constant(2))
    elif makeMethodName == "BoolOp":
        node = makeMethod(ast.And(), [Make.Constant(True)])
    elif makeMethodName == "Compare":
        node = makeMethod(Make.Constant(1), [ast.Lt()], [Make.Constant(2)])
    elif makeMethodName == "Call":
        node = makeMethod(Make.Name("func"))
    elif makeMethodName == "Attribute":
        node = makeMethod(Make.Name("obj"), "attr")
    elif makeMethodName == "FunctionDef":
        node = makeMethod("func", Make.arguments())
    elif makeMethodName == "ClassDef":
        node = makeMethod("Class")
    elif makeMethodName == "If":
        node = makeMethod(Make.Constant(True), [Make.Pass()])
    elif makeMethodName == "For":
        node = makeMethod(Make.Name("x", ast.Store()), Make.Name("items"), [Make.Pass()])
    elif makeMethodName == "While":
        node = makeMethod(Make.Constant(True), [Make.Pass()])
    elif makeMethodName == "Assign":
        node = makeMethod([Make.Name("x", ast.Store())], Make.Constant(1))
    elif makeMethodName == "AnnAssign":
        node = makeMethod(Make.Name("x", ast.Store()), Make.Name("int"), Make.Constant(1))
    elif makeMethodName == "AugAssign":
        node = makeMethod(Make.Name("x", ast.Store()), ast.Add(), Make.Constant(1))

    assert isinstance(node, expectedAstType), f"Make.{makeMethodName} should return {expectedAstType.__name__}"
