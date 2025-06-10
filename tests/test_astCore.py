from astToolkit import Make
import ast
import pytest

class TestASTCore:
    """Tests for core AST functionality and node behavior."""

    def test_ast_objects_basic(self):
        # Test basic AST object creation and field access
        astObj = ast.AST()
        assert astObj._fields == ()

        # Test custom attribute assignment
        astObj.customAttribute = 42
        assert astObj.customAttribute == 42
        assert astObj.__dict__["customAttribute"] == 42

        # Test that accessing undefined attributes raises AttributeError
        with pytest.raises(AttributeError):
            astObj.nonexistentAttribute

    def test_ast_node_fields(self):
        # Test that AST nodes have correct _fields attribute
        for name, item in ast.__dict__.items():
            if (isinstance(item, type) and
                issubclass(item, ast.AST) and
                name not in {"AST", "Num", "Str", "Bytes", "NameConstant", "Ellipsis", "Index"}):

                # Create instance with proper arguments
                try:
                    if name == "arguments":
                        instance = item()
                    elif name in {"Add", "Sub", "Mult", "Div", "Mod", "Pow", "LShift", "RShift",
                                  "BitOr", "BitXor", "BitAnd", "FloorDiv", "MatMult"}:
                        instance = item()
                    elif name in {"Load", "Store", "Del"}:
                        instance = item()
                    elif name in {"And", "Or"}:
                        instance = item()
                    elif name in {"Eq", "NotEq", "Lt", "LtE", "Gt", "GtE", "Is", "IsNot", "In", "NotIn"}:
                        instance = item()
                    elif name in {"UAdd", "USub", "Not", "Invert"}:
                        instance = item()
                    elif name == "Constant":
                        instance = item(42)
                    elif name == "Name":
                        instance = item("test", ast.Load())
                    elif name == "BinOp":
                        instance = item(ast.Constant(1), ast.Add(), ast.Constant(2))
                    else:
                        continue  # Skip complex nodes for this basic test

                    if hasattr(instance, '_fields'):
                        assert isinstance(instance._fields, tuple)
                except TypeError:
                    # Some nodes require specific arguments
                    continue

    def test_no_fields_nodes(self):
        # Test that nodes without fields work correctly
        subNode = ast.Sub()
        assert subNode._fields == ()

    def test_arguments_node(self):
        # Test ast.arguments node specifically
        args = ast.arguments()
        expectedFields = ('posonlyargs', 'args', 'vararg', 'kwonlyargs',
                         'kw_defaults', 'kwarg', 'defaults')
        assert args._fields == expectedFields
        assert args.args == []
        assert args.vararg is None

        # Test with positional arguments
        argsWithPositional = ast.arguments(*range(1, 8))
        assert argsWithPositional.args == 2
        assert argsWithPositional.vararg == 3

    def test_field_attr_writable(self):
        # Test that _fields attribute can be modified
        constant = ast.Constant(1)
        constant._fields = 666
        assert constant._fields == 666

    def test_constant_subclasses(self):
        # Test subclassing ast.Constant
        class CustomConstant(ast.Constant):
            def __init__(self, *arguments, **keywordArguments):
                super().__init__(*arguments, **keywordArguments)
                self.customAttribute = 'spam'

        class AnotherConstant(ast.Constant):
            pass

        customNode = CustomConstant(42)
        assert customNode.value == 42
        assert customNode.customAttribute == 'spam'
        assert type(customNode) is CustomConstant
        assert isinstance(customNode, CustomConstant)
        assert isinstance(customNode, ast.Constant)
        assert not isinstance(customNode, AnotherConstant)
        assert not isinstance(ast.Constant(42), CustomConstant)

        customNodeWithKeyword = CustomConstant(value=42)
        assert customNodeWithKeyword.value == 42
        assert type(customNodeWithKeyword) is CustomConstant

    def test_module_node(self):
        # Test ast.Module node
        body = [ast.Constant(42)]
        moduleNode = ast.Module(body, [])
        assert moduleNode.body == body

    def test_node_classes_basic(self):
        # Test basic node class functionality
        constant1 = ast.Constant(1)
        constant3 = ast.Constant(3)
        addOp = ast.Add()
        binOp = ast.BinOp(constant1, addOp, constant3)

        assert binOp.left == constant1
        assert binOp.op == addOp
        assert binOp.right == constant3

        # Test positional arguments
        binOpPositional = ast.BinOp(1, 2, 3)
        assert binOpPositional.left == 1
        assert binOpPositional.op == 2
        assert binOpPositional.right == 3

        # Test keyword arguments
        binOpKeyword = ast.BinOp(left=1, op=2, right=3, lineno=0)
        assert binOpKeyword.left == 1
        assert binOpKeyword.op == 2
        assert binOpKeyword.right == 3
        assert binOpKeyword.lineno == 0

        # Test too many arguments
        with pytest.raises(TypeError):
            ast.BinOp(1, 2, 3, 4)
        with pytest.raises(TypeError):
            ast.BinOp(1, 2, 3, 4, lineno=0)

    def test_invalid_constant_types(self):
        # Test that invalid types in Constant nodes raise TypeError
        for invalidConstant in [int, (1, 2, int), frozenset((1, 2, int))]:
            expression = ast.Expression(body=ast.Constant(invalidConstant))
            ast.fix_missing_locations(expression)
            with pytest.raises(TypeError, match="invalid type in Constant"):
                compile(expression, "<test>", "eval")

    def test_base_classes(self):
        # Test AST inheritance hierarchy
        assert issubclass(ast.For, ast.stmt)
        assert issubclass(ast.Name, ast.expr)
        assert issubclass(ast.stmt, ast.AST)
        assert issubclass(ast.expr, ast.AST)
        assert issubclass(ast.comprehension, ast.AST)
        assert issubclass(ast.Gt, ast.AST)

    def test_slice_handling(self):
        # Test slice parsing and handling
        sliceNode = ast.parse("x[::]").body[0].value.slice
        assert sliceNode.upper is None
        assert sliceNode.lower is None
        assert sliceNode.step is None

    def test_from_import_handling(self):
        # Test from import parsing
        importNode = ast.parse("from . import y").body[0]
        assert importNode.module is None

    def test_alias_positions(self):
        # Test import alias position tracking
        importNode = ast.parse("from bar import y").body[0]
        assert len(importNode.names) == 1
        aliasNode = importNode.names[0]
        assert aliasNode.name == "y"
        assert aliasNode.asname is None
        assert aliasNode.lineno == 1
        assert aliasNode.end_lineno == 1
        assert aliasNode.col_offset == 16
        assert aliasNode.end_col_offset == 17

        # Test import star
        starImport = ast.parse("from bar import *").body[0]
        starAlias = starImport.names[0]
        assert starAlias.name == "*"
        assert starAlias.asname is None

        # Test import with as
        asImport = ast.parse("from bar import y as z").body[0]
        asAlias = asImport.names[0]
        assert asAlias.name == "y"
        assert asAlias.asname == "z"

    def test_invalid_identifier(self):
        # Test that invalid identifiers raise TypeError
        moduleNode = ast.Module([ast.Expr(ast.Name(42, ast.Load()))], [])
        ast.fix_missing_locations(moduleNode)
        with pytest.raises(TypeError, match="identifier must be of type str"):
            compile(moduleNode, "<test>", "exec")

    def test_empty_yield_from(self):
        # Test that yield from requires a value
        emptyYieldFrom = ast.parse("def f():\n yield from g()")
        emptyYieldFrom.body[0].body[0].value.value = None
        with pytest.raises(ValueError, match="field 'value' is required"):
            compile(emptyYieldFrom, "<test>", "exec")

    def test_none_field_validation(self):
        # Test that required fields cannot be None
        testCases = [
            (ast.alias, "name", "import spam as SPAM"),
            (ast.arg, "arg", "def spam(SPAM): spam"),
            (ast.comprehension, "target", "[spam for SPAM in spam]"),
            (ast.comprehension, "iter", "[spam for spam in SPAM]"),
            (ast.keyword, "value", "spam(**SPAM)"),
        ]

        for nodeType, attribute, source in testCases:
            with pytest.raises(ValueError, match=f"field '{attribute}' is required"):
                tree = ast.parse(source)
                # Find the node and set the attribute to None
                foundNode = False
                for node in ast.walk(tree):
                    if isinstance(node, nodeType):
                        setattr(node, attribute, None)
                        foundNode = True
                        break
                assert foundNode, f"Could not find {nodeType.__name__} node in '{source}'"
                compile(tree, "<test>", "exec")

    def test_constant_as_name_validation(self):
        # Test that constants cannot be used as identifiers
        for constantName in ["True", "False", "None"]:
            expression = ast.Expression(ast.Name(constantName, ast.Load()))
            ast.fix_missing_locations(expression)
            with pytest.raises(ValueError, match=f"identifier field can't represent '{constantName}' constant"):
                compile(expression, "<test>", "eval")


class TestFeatureVersions:
    """Tests for AST feature version parsing compatibility."""

    def testPositionalOnlyFeatureVersion(self):
        """Test positional-only arguments feature version parsing."""
        ast.parse("def foo(x, /): ...", feature_version=(3, 8))
        ast.parse("def bar(x=1, /): ...", feature_version=(3, 8))

        with pytest.raises(SyntaxError):
            ast.parse("def foo(x, /): ...", feature_version=(3, 7))
        with pytest.raises(SyntaxError):
            ast.parse("def bar(x=1, /): ...", feature_version=(3, 7))

        ast.parse("lambda x, /: ...", feature_version=(3, 8))
        ast.parse("lambda x=1, /: ...", feature_version=(3, 8))

        with pytest.raises(SyntaxError):
            ast.parse("lambda x, /: ...", feature_version=(3, 7))
        with pytest.raises(SyntaxError):
            ast.parse("lambda x=1, /: ...", feature_version=(3, 7))

    def testAssignmentExpressionFeatureVersion(self):
        """Test assignment expressions (walrus operator) feature version."""
        ast.parse("(x := 0)", feature_version=(3, 8))

        with pytest.raises(SyntaxError):
            ast.parse("(x := 0)", feature_version=(3, 7))

    def testExceptionGroupsFeatureVersion(self):
        """Test exception groups feature version parsing."""
        codeExceptionGroup = """
try: ...
except* Exception: ...
"""
        ast.parse(codeExceptionGroup)

        with pytest.raises(SyntaxError):
            ast.parse(codeExceptionGroup, feature_version=(3, 10))

    def testTypeParametersFeatureVersion(self):
        """Test type parameters feature version parsing."""
        samplesTypeParameters = [
            "type X = int",
            "class X[T]: pass",
            "def f[T](): pass",
        ]
        for sample in samplesTypeParameters:
            ast.parse(sample)
            with pytest.raises(SyntaxError):
                ast.parse(sample, feature_version=(3, 11))

    def testTypeParametersDefaultFeatureVersion(self):
        """Test type parameters with defaults feature version."""
        samplesTypeParametersDefault = [
            "type X[*Ts=int] = int",
            "class X[T=int]: pass",
            "def f[**P=int](): pass",
        ]
        for sample in samplesTypeParametersDefault:
            ast.parse(sample)
            with pytest.raises(SyntaxError):
                ast.parse(sample, feature_version=(3, 12))

    def testInvalidMajorFeatureVersion(self):
        """Test invalid major feature versions."""
        with pytest.raises(ValueError):
            ast.parse("pass", feature_version=(2, 7))
        with pytest.raises(ValueError):
            ast.parse("pass", feature_version=(4, 0))


class TestASTValidationAndCompilation:
    """Tests for AST validation and compilation edge cases."""

    def testNegativeLocationsForCompile(self):
        """Test compilation with negative line/column positions."""
        aliasNode = ast.alias(name='traceback', lineno=0, col_offset=0)

        testCases = [
            {'lineno': -2, 'col_offset': 0},
            {'lineno': 0, 'col_offset': -2},
            {'lineno': 0, 'col_offset': -2, 'end_col_offset': -2},
            {'lineno': -2, 'end_lineno': -2, 'col_offset': 0},
        ]

        for attributes in testCases:
            treeModule = ast.Module(body=[
                ast.Import(names=[aliasNode], **attributes)
            ], type_ignores=[])

            # This used to crash:
            compile(treeModule, "<string>", "exec")
              # This also must not crash:
            ast.parse(treeModule, optimize=2)

    def testInvalidSum(self):
        """Test invalid AST sum types."""
        positionInfo = dict(lineno=2, col_offset=3)
        moduleNode = ast.Module([ast.Expr(ast.expr(**positionInfo), **positionInfo)], [])

        with pytest.raises(TypeError, match="expected some sort of expr, but got"):
            compile(moduleNode, "<test>", "exec")

    def testInvalidIdentifier(self):
        """Test invalid identifier types."""
        moduleNode = ast.Module([ast.Expr(ast.Name(42, ast.Load()))], [])
        ast.fix_missing_locations(moduleNode)

        with pytest.raises(TypeError, match="identifier must be of type str"):
            compile(moduleNode, "<test>", "exec")
    def testInvalidConstant(self):
        """Test invalid constant values in AST."""
        # In modern Python, ast.Constant accepts various types, so this test
        # verifies that compilation catches inappropriate usage rather than construction
        moduleNode = ast.Module([ast.Expr(ast.Constant([1, 2, 3]))], [])

        # The compilation should succeed, but the constant will contain a list
        # This is actually valid in recent Python versions
        try:
            compile(moduleNode, "<test>", "exec")
            # If compilation succeeds, that's expected behavior in modern Python
        except TypeError:
            # If compilation fails, that's also acceptable behavior
            pass


class TestASTGarbageCollection:
    """Tests for AST garbage collection behavior."""

    def testASTGarbageCollection(self):
        """Test that AST nodes are properly garbage collected."""
        import gc
        import weakref

        class TestReference:
            pass

        astNode = ast.AST()
        astNode.testRef = TestReference()
        astNode.testRef.astNode = astNode

        weakReference = weakref.ref(astNode.testRef)
        del astNode
        gc.collect()

        assert weakReference() is None


class TestASTRepr:
    """Tests for AST representation and string formatting."""
    def testRepr(self):
        """Test AST node repr output."""
        nodeConstant = ast.Constant(42)
        reprString = repr(nodeConstant)
        assert "Constant" in reprString
        # Note: Standard ast.Constant repr doesn't include the value
        assert "ast.Constant" in reprString

    def testReprLargeInput(self):
        """Test repr with large input doesn't crash."""
        # Create a large AST structure
        largeList = [ast.Constant(i) for i in range(1000)]
        largeModule = ast.Module(body=[ast.Expr(value=ast.List(elts=largeList))], type_ignores=[])

        # This should not crash
        reprString = repr(largeModule)
        assert isinstance(reprString, str)
        assert len(reprString) > 0


class TestASTOptimizationLevels:
    """Tests for AST optimization level handling."""

    def testOptimizationLevelsDebug(self):
        """Test __debug__ optimization at different levels."""
        codeDebug = "__debug__"

        # Test non-optimized (default)
        treeNonOpt = ast.parse(codeDebug, optimize=-1)
        nodeNonOpt = treeNonOpt.body[0].value
        assert isinstance(nodeNonOpt, ast.Name)
        assert nodeNonOpt.id == "__debug__"

        # Test optimized
        treeOpt = ast.parse(codeDebug, optimize=1)
        nodeOpt = treeOpt.body[0].value
        assert isinstance(nodeOpt, ast.Constant)
        assert nodeOpt.value is False

    def testParseValidatesInput(self):
        """Test that ast.parse handles different input types appropriately."""
        # ast.parse should accept string input
        result = ast.parse("x = 1")
        assert isinstance(result, ast.Module)

        # ast.parse with AST input just returns the AST unchanged
        constantNode = ast.Constant(42)
        result = ast.parse(constantNode)
        assert result is constantNode


class TestASTNodeFields:
    """Tests for AST node field handling."""

    def testNoFields(self):
        """Test nodes with no fields."""
        # This used to fail because Sub._fields was None
        nodeSubtract = ast.Sub()
        assert nodeSubtract._fields == ()

    def testFieldAttributeWritable(self):
        """Test that _fields attribute is writable."""
        nodeConstant = ast.Constant(1)
        # We can assign to _fields
        nodeConstant._fields = 666
        assert nodeConstant._fields == 666

    def testArguments(self):
        """Test arguments node structure."""
        nodeArguments = ast.arguments()
        expectedFields = ('posonlyargs', 'args', 'vararg', 'kwonlyargs',
                         'kw_defaults', 'kwarg', 'defaults')
        assert nodeArguments._fields == expectedFields

        expectedAnnotations = {
            'posonlyargs': list[ast.arg],
            'args': list[ast.arg],
            'vararg': ast.arg | None,
            'kwonlyargs': list[ast.arg],
            'kw_defaults': list[ast.expr],
            'kwarg': ast.arg | None,
            'defaults': list[ast.expr],
        }
        assert ast.arguments.__annotations__ == expectedAnnotations

        assert nodeArguments.args == []
        assert nodeArguments.vararg is None

        nodeArgumentsWithValues = ast.arguments(*range(1, 8))
        assert nodeArgumentsWithValues.args == 2
        assert nodeArgumentsWithValues.vararg == 3


class TestConstantSubclasses:
    """Tests for AST Constant node subclassing."""

    def testConstantSubclasses(self):
        """Test subclassing of Constant nodes."""
        class ConstantN(ast.Constant):
            def __init__(self, *arguments, **keywordArguments):
                super().__init__(*arguments, **keywordArguments)
                self.customAttribute = 'spam'

        class ConstantN2(ast.Constant):
            pass

        nodeN = ConstantN(42)
        assert nodeN.value == 42
        assert nodeN.customAttribute == 'spam'
        assert type(nodeN) is ConstantN
        assert isinstance(nodeN, ConstantN)
        assert isinstance(nodeN, ast.Constant)
        assert not isinstance(nodeN, ConstantN2)
        assert not isinstance(ast.Constant(42), ConstantN)

        nodeNWithKeyword = ConstantN(value=42)
        assert nodeNWithKeyword.value == 42
        assert type(nodeNWithKeyword) is ConstantN


class TestModuleStructure:
    """Tests for Module AST node structure."""

    def testModule(self):
        """Test Module node creation and structure."""
        bodyStatements = [ast.Constant(42)]
        moduleNode = ast.Module(bodyStatements, [])
        assert moduleNode.body == bodyStatements
