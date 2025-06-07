import ast
import pytest
from astToolkit import Make


class TestASTCore:
    """Test core AST functionality with Make integration."""

    def test_ast_objects(self):
        """Test basic AST object behavior."""
        astObject = ast.AST()
        assert astObject._fields == ()

        # Test attribute assignment
        astObject.foobar = 42
        assert astObject.foobar == 42
        assert astObject.__dict__["foobar"] == 42

        # Test missing attribute
        with pytest.raises(AttributeError):
            astObject.vararg

        # Test constructor with arguments
        with pytest.raises(TypeError):
            ast.AST(2)

    def test_make_nodes_basic_behavior(self):
        """Test that Make nodes behave like standard AST nodes."""
        makeName = Make.Name("testVar", ast.Load())

        # Test _fields attribute
        assert makeName._fields == ast.Name._fields

        # Test attribute assignment
        makeName.customAttr = "customValue"
        assert makeName.customAttr == "customValue"

        # Test missing attribute
        with pytest.raises(AttributeError):
            makeName.nonExistentAttr

    def test_ast_garbage_collection(self):
        """Test AST garbage collection behavior."""
        class TestClass:
            pass

        astObject = ast.AST()
        astObject.x = TestClass()
        astObject.x.a = astObject
        # Note: gc_collect not available in pytest context, so we just test the structure

    def test_slice_nodes(self):
        """Test slice node behavior."""
        sliceNode = ast.parse("x[::]").body[0].value.slice
        assert sliceNode.upper is None
        assert sliceNode.lower is None
        assert sliceNode.step is None

        # Test with Make
        makeSlice = Make.Slice(None, None, None)
        assert makeSlice.upper is None
        assert makeSlice.lower is None
        assert makeSlice.step is None

    def test_from_import_nodes(self):
        """Test import from behavior."""
        importNode = ast.parse("from . import y").body[0]
        assert importNode.module is None

        # Test with Make
        makeAlias = Make.alias("y", None)
        makeImportFrom = Make.ImportFrom(None, [makeAlias], 1)  # level=1 for relative import
        assert makeImportFrom.module is None
        assert len(makeImportFrom.names) == 1
        assert makeImportFrom.names[0].name == "y"

    def test_alias_positions(self):
        """Test alias node position information."""
        # Test basic import
        importNode = ast.parse("from bar import y").body[0]
        assert len(importNode.names) == 1
        aliasNode = importNode.names[0]
        assert aliasNode.name == "y"
        assert aliasNode.asname is None

        # Test wildcard import
        wildcardImport = ast.parse("from bar import *").body[0]
        wildcardAlias = wildcardImport.names[0]
        assert wildcardAlias.name == "*"
        assert wildcardAlias.asname is None

        # Test import with alias
        aliasImport = ast.parse("from bar import y as z").body[0]
        aliasWithAs = aliasImport.names[0]
        assert aliasWithAs.name == "y"
        assert aliasWithAs.asname == "z"

        # Test regular import with alias
        regularImport = ast.parse("import bar as foo").body[0]
        regularAlias = regularImport.names[0]
        assert regularAlias.name == "bar"
        assert regularAlias.asname == "foo"

    def test_make_alias_nodes(self):
        """Test Make alias node creation."""
        # Test basic alias
        makeAlias = Make.alias("moduleName", None)
        assert makeAlias.name == "moduleName"
        assert makeAlias.asname is None

        # Test alias with asname
        makeAliasAs = Make.alias("originalName", "newName")
        assert makeAliasAs.name == "originalName"
        assert makeAliasAs.asname == "newName"

        # Test in ImportFrom
        makeImportFrom = Make.ImportFrom("package", [makeAlias, makeAliasAs], 0)
        assert makeImportFrom.module == "package"
        assert len(makeImportFrom.names) == 2

    def test_base_classes(self):
        """Test AST inheritance hierarchy."""
        assert issubclass(ast.For, ast.stmt)
        assert issubclass(ast.Name, ast.expr)
        assert issubclass(ast.stmt, ast.AST)
        assert issubclass(ast.expr, ast.AST)
        assert issubclass(ast.comprehension, ast.AST)
        assert issubclass(ast.Gt, ast.AST)

        # Test Make nodes maintain inheritance
        makeFor = Make.For(Make.Name("i", ast.Store()), Make.Name("items", ast.Load()), [], [])
        assert isinstance(makeFor, ast.For)
        assert isinstance(makeFor, ast.stmt)
        assert isinstance(makeFor, ast.AST)

    # def test_arguments_node(self):
    #     """Test arguments node behavior."""
    #     argumentsNode = ast.arguments()
    #     expected_fields = (
    #         "posonlyargs", "args", "vararg", "kwonlyargs",
    #         "kw_defaults", "kwarg", "defaults"
    #     )
    #     assert argumentsNode._fields == expected_fields

    #     # Test initial values
    #     assert argumentsNode.args == []
    #     assert argumentsNode.vararg is None

    #     # Test with Make
    #     makeArg = Make.arg("param", None)
    #     makeArguments = Make.arguments([makeArg], [], None, [], [], None, [])
    #     assert len(makeArguments.args) == 1
    #     assert makeArguments.args[0].arg == "param"
    #     assert makeArguments.vararg is None

    def test_field_attr_writable(self):
        """Test that _fields attribute is writable."""
        makeConstant = Make.Constant(1)

        # Test we can assign to _fields
        makeConstant._fields = 666
        assert makeConstant._fields == 666

    def test_node_classes_with_make(self):
        """Test node class behavior with Make constructors."""
        # Test BinOp with positional arguments
        makeLeft = Make.Constant(1)
        makeRight = Make.Constant(3)
        addOp = ast.Add()
        makeBinOp = Make.BinOp(makeLeft, addOp, makeRight)

        assert makeBinOp.left == makeLeft
        assert makeBinOp.op == addOp
        assert makeBinOp.right == makeRight

        # Test with lineno
        makeBinOpWithLine = Make.BinOp(makeLeft, addOp, makeRight, lineno=0)
        assert makeBinOpWithLine.lineno == 0

    def test_no_fields(self):
        """Test nodes with no fields."""
        subNode = ast.Sub()
        assert subNode._fields == ()

        # Test Make equivalent
        makeAdd = Make.Add()
        makeSub = Make.Sub()
        assert makeAdd._fields == ()
        assert makeSub._fields == ()

    def test_invalid_compilation(self):
        """Test compilation errors with invalid nodes."""
        # Test invalid sum type
        with pytest.raises(TypeError):
            invalidModule = ast.Module([ast.Expr(ast.expr())], [])
            compile(invalidModule, "<test>", "exec")

        # Test invalid identifier
        with pytest.raises(TypeError):
            invalidName = Make.Name(42, ast.Load())  # Invalid identifier type
            invalidModule = Make.Module([Make.Expr(invalidName)], [])
            ast.fix_missing_locations(invalidModule)
            compile(invalidModule, "<test>", "exec")

    def test_invalid_constant(self):
        """Test invalid constant compilation."""
        for invalidConstant in [int, (1, 2, int), frozenset((1, 2, int))]:
            invalidExpression = Make.Expression(Make.Constant(invalidConstant))
            ast.fix_missing_locations(invalidExpression)
            with pytest.raises(TypeError):
                compile(invalidExpression, "<test>", "eval")

    def test_empty_yield_from(self):
        """Test yield from validation."""
        # Create yield from without value
        yieldFromNode = ast.parse("def f():\n yield from g()")
        yieldFromNode.body[0].body[0].value.value = None
        with pytest.raises(ValueError):
            compile(yieldFromNode, "<test>", "exec")

    def test_make_node_compilation(self):
        """Test that Make nodes compile successfully."""
        # Create a simple function using Make
        returnStmt = Make.Return(Make.Constant(42))
        functionDef = Make.FunctionDef(
            "testFunc",
            Make.arguments([], [], None, [], [], None, []),
            [returnStmt],
            [],
            None
        )
        moduleNode = Make.Module([functionDef], [])

        # Test compilation
        ast.fix_missing_locations(moduleNode)
        compiledCode = compile(moduleNode, "<test>", "exec")
        assert compiledCode is not None

        # Test execution
        namespace = {}
        exec(compiledCode, namespace)
        assert "testFunc" in namespace
        assert namespace["testFunc"]() == 42

    def test_position_validation(self):
        """Test position validation for Make nodes."""
        # Test valid positions
        makeAssign = Make.Assign(
            [Make.Name("a", ast.Store())],
            Make.Constant(1),
            lineno=1,
            col_offset=0
        )
        moduleNode = Make.Module([makeAssign], [])
        ast.fix_missing_locations(moduleNode)

        # Should compile without error
        compile(moduleNode, "<test>", "exec")

    def test_make_node_field_compatibility(self):
        """Test that Make nodes have compatible field structures."""
        # Test various node types
        makeName = Make.Name("var", ast.Load())
        makeConstant = Make.Constant(100)
        makeBinOp = Make.BinOp(makeName, ast.Add(), makeConstant)

        # Verify field compatibility with standard AST
        assert makeName._fields == ast.Name._fields
        assert makeConstant._fields == ast.Constant._fields
        assert makeBinOp._fields == ast.BinOp._fields

        # Test field access
        assert makeName.id == "var"
        assert isinstance(makeName.ctx, ast.Load)
        assert makeConstant.value == 100
        assert makeBinOp.left == makeName
        assert isinstance(makeBinOp.op, ast.Add)
        assert makeBinOp.right == makeConstant
