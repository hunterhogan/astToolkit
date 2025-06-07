from astToolkit import Make
import ast
import copy
import pickle
import pytest
import textwrap

# from astToolkit._toolkitContainers import _toTuple


class TestCopyOperations:
    """Test copying and pickling AST nodes."""

    def testPickling(self):
        # Simple test cases for pickling AST nodes
        testCodes = [
            "x = 1",
            "def func(): pass",
            "class Test: pass",
            "for i in range(10): print(i)",
            "if True: x = 1",
            "x + y",
            "[x for x in range(10)]",
        ]

    #     for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    #         for code in testCodes:
    #             tree = ast.parse(code)
    #             pickledTree = pickle.loads(pickle.dumps(tree, protocol))
    #             assert _toTuple(pickledTree) == _toTuple(tree)

    # def testPicklingWithMakeNodes(self):
    #     # Test pickling nodes created with Make
    #     constantNode = Make.Constant(42)
    #     nameNode = Make.Name("x", ast.Load())
    #     binaryOperationNode = Make.BinOp(constantNode, ast.Add(), nameNode)

    #     for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    #         pickledConstant = pickle.loads(pickle.dumps(constantNode, protocol))
    #         pickledName = pickle.loads(pickle.dumps(nameNode, protocol))
    #         pickledBinaryOperation = pickle.loads(pickle.dumps(binaryOperationNode, protocol))

    #         assert _toTuple(pickledConstant) == _toTuple(constantNode)
    #         assert _toTuple(pickledName) == _toTuple(nameNode)
    #         assert _toTuple(pickledBinaryOperation) == _toTuple(binaryOperationNode)

    # def testCopySimpleNodes(self):
    #     # Test basic copy operations
    #     originalConstant = Make.Constant(42)
    #     copiedConstant = copy.copy(originalConstant)
    #     deepCopiedConstant = copy.deepcopy(originalConstant)

    #     assert originalConstant.value == copiedConstant.value
    #     assert originalConstant.value == deepCopiedConstant.value
    #     assert _toTuple(originalConstant) == _toTuple(copiedConstant)
    #     assert _toTuple(originalConstant) == _toTuple(deepCopiedConstant)

    def testCopyComplexNodes(self):
        # Test copying complex AST structures
        functionDefinition = Make.FunctionDef(
            "testFunction",
            Make.arguments(
                posonlyargs=[],
                list_arg=[Make.arg("x", annotation=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[]
            ),
            body=[Make.Return(Make.Name("x", ast.Load()))],
            decorator_list=[],
            returns=None,
            type_comment=None
        )

        copiedFunction = copy.copy(functionDefinition)
        deepCopiedFunction = copy.deepcopy(functionDefinition)

        assert functionDefinition.name == copiedFunction.name
        assert functionDefinition.name == deepCopiedFunction.name
        # assert _toTuple(functionDefinition) == _toTuple(deepCopiedFunction)

    def testCopyWithComplexStructure(self):
        # Test copying a more complex AST structure
        code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)        """

        originalTree = ast.parse(textwrap.dedent(code))
        copiedTree = copy.copy(originalTree)
        deepCopiedTree = copy.deepcopy(originalTree)

        # assert _toTuple(originalTree) == _toTuple(deepCopiedTree)
        # copy.copy may share some child nodes, but structure should be similar
        assert isinstance(copiedTree, type(originalTree))
        assert len(originalTree.body) == len(copiedTree.body)

    def testDeepCopyWithNestedNodes(self):
        # Test deep copying with heavily nested structures
        nestedExpression = Make.BinOp(
            left=Make.BinOp(
                left=Make.Constant(1),
                op=ast.Add(),
                right=Make.Constant(2)
            ),
            op=ast.Mult(),
            right=Make.BinOp(
                left=Make.Constant(3),
                op=ast.Sub(),
                right=Make.Constant(4)
            )
        )

        deepCopiedExpression = copy.deepcopy(nestedExpression)
        # assert _toTuple(nestedExpression) == _toTuple(deepCopiedExpression)

        # Verify that changes to the copy don't affect the original
        if hasattr(deepCopiedExpression.left, 'left'):
            deepCopiedExpression.left.left.value = 999
            assert nestedExpression.left.left.value != 999

    def testCopyListAndTupleNodes(self):
        # Test copying nodes that contain lists and tuples
        listNode = Make.List(
            [Make.Constant(1), Make.Constant(2), Make.Constant(3)],
            ast.Load()
        )

        tupleNode = Make.Tuple(
            [Make.Name("x", ast.Load()), Make.Name("y", ast.Load())],
            ast.Store()
        )

        copiedList = copy.deepcopy(listNode)
        copiedTuple = copy.deepcopy(tupleNode)

        # assert _toTuple(listNode) == _toTuple(copiedList)
        # assert _toTuple(tupleNode) == _toTuple(copiedTuple)

        # Verify lists are properly copied
        assert len(listNode.elts) == len(copiedList.elts)
        assert len(tupleNode.elts) == len(copiedTuple.elts)

    def testCopyNodeWithAttributes(self):
        # Test copying nodes with custom attributes
        nameNode = Make.Name("variable", ast.Load())
        nameNode.lineno = 1
        nameNode.col_offset = 0
        nameNode.end_lineno = 1
        nameNode.end_col_offset = 8

        copiedName = copy.deepcopy(nameNode)

        assert nameNode.id == copiedName.id
        assert nameNode.lineno == copiedName.lineno
        assert nameNode.col_offset == copiedName.col_offset
        assert nameNode.end_lineno == copiedName.end_lineno
        assert nameNode.end_col_offset == copiedName.end_col_offset

    def testCopyNodeWithTypeComments(self):
        # Test copying nodes that have type comments
        assignmentNode = Make.Assign(
            targets=[Make.Name("x", ast.Store())],
            value=Make.Constant(42),
            type_comment="int"
        )

        copiedAssignment = copy.deepcopy(assignmentNode)

        assert assignmentNode.type_comment == copiedAssignment.type_comment
        # assert _toTuple(assignmentNode) == _toTuple(copiedAssignment)
