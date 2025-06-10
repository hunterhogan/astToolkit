from astToolkit import Make
from test.test_ast.snippets import exec_tests
from test.test_ast.utils import to_tuple
import ast
import copy
import pickle
import pytest
import textwrap

class TestCopy:
    """Test copying and pickling AST nodes."""

    def test_pickling(self):
        for protocolLevel in range(pickle.HIGHEST_PROTOCOL + 1):
            for codeText in exec_tests[:5]:  # Test subset for performance
                astTree = compile(codeText, "?", "exec", 0x400)
                pickledAst = pickle.loads(pickle.dumps(astTree, protocolLevel))
                assert to_tuple(pickledAst) == to_tuple(astTree)

    def test_pickling_make_nodes(self):
        """Test that Make-generated nodes can be pickled and unpickled."""
        # Create some Make nodes
        makeName = Make.Name("testVar", ast.Load())
        makeConstant = Make.Constant(42)
        makeBinOp = Make.BinOp(makeName, ast.Add(), makeConstant)
        makeExpr = Make.Expr(makeBinOp)
        makeModule = Make.Module([makeExpr], [])

        for protocolLevel in range(pickle.HIGHEST_PROTOCOL + 1):
            # Test individual nodes
            pickledName = pickle.loads(pickle.dumps(makeName, protocolLevel))
            assert ast.dump(pickledName) == ast.dump(makeName)

            pickledConstant = pickle.loads(pickle.dumps(makeConstant, protocolLevel))
            assert ast.dump(pickledConstant) == ast.dump(makeConstant)

            # Test complex structure
            pickledModule = pickle.loads(pickle.dumps(makeModule, protocolLevel))
            assert ast.dump(pickledModule) == ast.dump(makeModule)

    def test_copy_make_nodes(self):
        """Test that Make-generated nodes can be copied."""
        # Create complex Make structure
        nameA = Make.Name("a", ast.Load())
        nameB = Make.Name("b", ast.Load())
        nameC = Make.Name("c", ast.Store())

        binOpNode = Make.BinOp(nameA, ast.Add(), nameB)
        assignNode = Make.Assign([nameC], binOpNode)
        moduleNode = Make.Module([assignNode], [])

        # Test shallow copy
        shallowCopy = copy.copy(moduleNode)
        assert ast.dump(shallowCopy) == ast.dump(moduleNode)

        # Test deep copy
        deepCopy = copy.deepcopy(moduleNode)
        assert ast.dump(deepCopy) == ast.dump(moduleNode)

        # Verify independence of deep copy
        deepCopy.body[0].targets[0].id = "modified"
        assert moduleNode.body[0].targets[0].id == "c"  # Original unchanged    def test_copy_with_attributes(self):
        """Test copying nodes with position attributes."""
        # Create Make node with custom attributes
        makeName = Make.Name("x", ast.Store(), lineno=1, col_offset=0)
        makeLeft = Make.Constant(1, lineno=1, col_offset=4)
        makeRight = Make.Constant(2, lineno=1, col_offset=8)
        makeBinOp = Make.BinOp(makeLeft, ast.Add(), makeRight, lineno=1, col_offset=4)
        makeAssign = Make.Assign([makeName], makeBinOp, lineno=1, col_offset=0)
        makeModule = Make.Module([makeAssign], [])

        # Test deep copy preserves attributes
        copiedModule = copy.deepcopy(makeModule)
        copiedAssign = copiedModule.body[0]

        assert copiedAssign.lineno == 1
        assert copiedAssign.col_offset == 0
        assert copiedAssign.value.lineno == 1
        assert copiedAssign.value.col_offset == 4

    # def test_copy_with_complex_structures(self):
    #     """Test copying nodes with complex nested structures."""
    #     # Create a function definition with Make
    #     argA = Make.arg("a", Make.Name("int", ast.Load()))
    #     argB = Make.arg("b", Make.Name("str", ast.Load()))
    #     argumentsNode = Make.arguments([argA], [], [], [argB], [Make.Constant("default")], None, [])

    #     returnStmt = Make.Return(Make.BinOp(Make.Name("a", ast.Load()), ast.Add(), Make.Constant(1)))
    #     functionDef = Make.FunctionDef("testFunction", argumentsNode, [returnStmt], [], None)
    #     moduleNode = Make.Module([functionDef], [])

    #     # Test deep copy
    #     copiedModule = copy.deepcopy(moduleNode)

    #     # Verify structure is preserved
    #     copiedFunction = copiedModule.body[0]
    #     assert copiedFunction.name == "testFunction"
    #     assert len(copiedFunction.args.args) == 1
    #     assert len(copiedFunction.args.kwonlyargs) == 1
    #     assert copiedFunction.args.args[0].arg == "a"
    #     assert copiedFunction.args.kwonlyargs[0].arg == "b"

    #     # Verify independence
    #     copiedFunction.name = "modifiedFunction"
    #     assert moduleNode.body[0].name == "testFunction"  # Original unchanged

    def test_copy_inheritance_compatibility(self):
        """Test that copied Make nodes maintain AST compatibility."""
        makeName = Make.Name("testVar", ast.Load())
        makeConstant = Make.Constant(100)
        makeBinOp = Make.BinOp(makeName, ast.Mult(), makeConstant)

        copiedBinOp = copy.deepcopy(makeBinOp)

        # Test that copied nodes are still valid AST nodes
        assert isinstance(copiedBinOp, ast.BinOp)
        assert isinstance(copiedBinOp.left, ast.Name)
        assert isinstance(copiedBinOp.op, ast.Mult)
        assert isinstance(copiedBinOp.right, ast.Constant)

        # Test that they can be compiled
        exprNode = Make.Expression(copiedBinOp)
        ast.fix_missing_locations(exprNode)
        compiledCode = compile(exprNode, "<test>", "eval")
        assert compiledCode is not None

    def test_copy_edge_cases(self):
        """Test copying with edge cases and special node types."""
        # Test with optional fields
        makeRaise = Make.Raise()  # No exc or cause
        copiedRaise = copy.deepcopy(makeRaise)
        assert copiedRaise.exc is None
        assert copiedRaise.cause is None

        # Test with list fields
        makeList = Make.List([Make.Constant(1), Make.Constant(2), Make.Constant(3)],
                            ast.Load())
        copiedList = copy.deepcopy(makeList)
        assert len(copiedList.elts) == 3
        assert all(isinstance(elt, ast.Constant) for elt in copiedList.elts)

        # Test with keyword arguments
        makeKeyword = Make.keyword("arg", Make.Constant("value"))
        makeCall = Make.Call(Make.Name("func", ast.Load()), [], [makeKeyword])
        copiedCall = copy.deepcopy(makeCall)
        assert len(copiedCall.keywords) == 1
        assert copiedCall.keywords[0].arg == "arg"

    def test_copy_performance_large_tree(self):
        """Test copying performance with larger AST structures."""
        # Create a larger structure using Make
        statements = []
        for i in range(20):  # Create 20 assignment statements
            target = Make.Name(f"var{i}", ast.Store())
            value = Make.BinOp(Make.Constant(i), ast.Mult(), Make.Constant(2))
            assign = Make.Assign([target], value)
            statements.append(assign)

        largeModule = Make.Module(statements, [])

        # Test that copying completes without issues
        copiedModule = copy.deepcopy(largeModule)
        assert len(copiedModule.body) == 20
        assert all(isinstance(stmt, ast.Assign) for stmt in copiedModule.body)

        # Verify some specific copied values
        assert copiedModule.body[5].targets[0].id == "var5"
        assert copiedModule.body[10].value.left.value == 10
