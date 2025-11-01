"""Tests for the Then class action functions using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Make, Then
from collections.abc import Callable, Sequence
from typing import Any
import ast
import pytest

class TestThenAppendTo:
	"""Test suite for Then.appendTo method."""

	@pytest.mark.parametrize("listNodesToAppend,expectedCountNodes", [
		([Make.Name("variableNorthward"), Make.Name("variableSouthward")], 2),
		([Make.Constant(233), Make.Constant(89), Make.Constant(13)], 3),  # Fibonacci numbers
		([Make.FunctionDef(name="functionEastward")], 1),
		([], 0),
	])
	def testAppendToWithVariousNodes(self, listNodesToAppend: list[ast.AST], expectedCountNodes: int) -> None:
		"""Test appendTo with various node types using cardinal directions and Fibonacci numbers."""
		listCollected: list[Any] = []
		actionAppend: Callable[[ast.AST], ast.AST] = Then.appendTo(listCollected)

		for nodeTarget in listNodesToAppend:
			nodeReturned = actionAppend(nodeTarget)
			assert nodeReturned is nodeTarget, "appendTo should return the same node unchanged"

		assert len(listCollected) == expectedCountNodes, f"Expected {expectedCountNodes} nodes in list, got {len(listCollected)}"
		assert listCollected == listNodesToAppend, "Collected nodes should match appended nodes"

	def testAppendToPreservesNodeIdentity(self) -> None:
		"""Test that appendTo preserves node identity for read-only traversal."""
		nodeOriginal = Make.Name("identifierPrimary")
		listCollected: list[Any] = []
		actionAppend = Then.appendTo(listCollected)

		nodeReturned = actionAppend(nodeOriginal)

		assert nodeReturned is nodeOriginal, "appendTo must preserve node identity"
		assert listCollected[0] is nodeOriginal, "Collected node must be the same object"

	@pytest.mark.parametrize("nodeType,factoryNode", [
		("Name", lambda: Make.Name("variableAlpha")),
		("Constant", lambda: Make.Constant(377)),  # Fibonacci number
		("FunctionDef", lambda: Make.FunctionDef(name="functionBeta")),
		("ClassDef", lambda: Make.ClassDef(name="ClassGamma")),
	])
	def testAppendToWithDifferentNodeTypes(self, nodeType: str, factoryNode: Callable[[], ast.AST]) -> None:
		"""Test appendTo works with different AST node types."""
		listCollected: list[Any] = []
		actionAppend = Then.appendTo(listCollected)
		nodeTarget = factoryNode()

		nodeReturned = actionAppend(nodeTarget)

		assert nodeReturned is nodeTarget
		assert len(listCollected) == 1
		assert listCollected[0] is nodeTarget

class TestThenExtractIt:
	"""Test suite for Then.extractIt method."""

	@pytest.mark.parametrize("nodeToExtract", [
		Make.Name("variableNorthward"),
		Make.Constant(233),  # Fibonacci number
		Make.FunctionDef(name="functionEastward"),
		Make.ClassDef(name="ClassWestward"),
		Make.Assign(targets=[Make.Name("targetSouthward", context=Make.Store())], value=Make.Constant(89)),
	])
	def testExtractItIdentityOperation(self, nodeToExtract: ast.AST) -> None:
		"""Test extractIt returns nodes unchanged (identity function)."""
		nodeReturned = Then.extractIt(nodeToExtract)
		assert nodeReturned is nodeToExtract, "extractIt must return the exact same node"

	def testExtractItPreservesNodeStructure(self) -> None:
		"""Test extractIt preserves complex node structure."""
		nodeFunctionComplex = Make.FunctionDef(
			name="functionComplex",
			argumentSpecification=Make.arguments(
				list_arg=[Make.arg("parameterAlpha"), Make.arg("parameterBeta")]
			),
			body=[
				Make.Assign(
					targets=[Make.Name("resultGamma", context=Make.Store())],
					value=Make.Constant(610)  # Fibonacci number
				)
			]
		)

		nodeReturned = Then.extractIt(nodeFunctionComplex)

		assert nodeReturned is nodeFunctionComplex
		assert nodeReturned.name == "functionComplex"
		assert len(nodeReturned.args.args) == 2
		assert len(nodeReturned.body) == 1

class TestThenInsertThisAbove:
	"""Test suite for Then.insertThisAbove method."""

	@pytest.mark.parametrize("listNodesToInsert,nodeTarget,expectedLengthSequence", [
		([Make.Pass()], Make.Return(Make.Constant(233)), 2),  # Fibonacci number
		([Make.Pass(), Make.Pass()], Make.Return(Make.Constant(89)), 3),  # Fibonacci number
		([Make.Assign(targets=[Make.Name("variableAlpha", context=Make.Store())], value=Make.Constant(13))], Make.Return(Make.Name("variableAlpha")), 2),
	])
	def testInsertThisAboveCreatesCorrectSequence(self, listNodesToInsert: Sequence[ast.AST], nodeTarget: ast.AST, expectedLengthSequence: int) -> None:
		"""Test insertThisAbove creates sequence with nodes above target."""
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listNodesToInsert)
		sequenceResult = actionInsert(nodeTarget)

		assert len(sequenceResult) == expectedLengthSequence, f"Expected sequence length {expectedLengthSequence}, got {len(sequenceResult)}"
		# Verify inserted nodes are first
		for indexNode, nodeInserted in enumerate(listNodesToInsert):
			assert sequenceResult[indexNode] is nodeInserted, f"Node at index {indexNode} should be inserted node"
		# Verify target node is last
		assert sequenceResult[-1] is nodeTarget, "Target node should be last in sequence"

	def testInsertThisAboveLogicalPrecedence(self) -> None:
		"""Test insertThisAbove creates logical precedence (inserted nodes come first)."""
		nodeSetup = Make.Assign(
			targets=[Make.Name("variableSetup", context=Make.Store())],
			value=Make.Constant(987)  # Fibonacci number
		)
		nodeMain = Make.Return(Make.Name("variableSetup"))

		actionInsert = Then.insertThisAbove([nodeSetup])
		sequenceResult = actionInsert(nodeMain)

		assert sequenceResult[0] is nodeSetup, "Setup node should precede main node"
		assert sequenceResult[1] is nodeMain, "Main node should follow setup node"

	@pytest.mark.parametrize("countNodesToInsert", [1, 2, 3, 5])
	def testInsertThisAboveWithVariousCountsOfNodes(self, countNodesToInsert: int) -> None:
		"""Test insertThisAbove with various numbers of nodes to insert."""
		listNodesToInsert = [Make.Pass() for _ in range(countNodesToInsert)]
		nodeTarget = Make.Return(Make.Constant(1597))  # Fibonacci number
		actionInsert = Then.insertThisAbove(listNodesToInsert)

		sequenceResult = actionInsert(nodeTarget)

		assert len(sequenceResult) == countNodesToInsert + 1
		assert sequenceResult[-1] is nodeTarget

class TestThenInsertThisBelow:
	"""Test suite for Then.insertThisBelow method."""

	@pytest.mark.parametrize("listNodesToInsert,nodeTarget,expectedLengthSequence", [
		([Make.Pass()], Make.Return(Make.Constant(233)), 2),  # Fibonacci number
		([Make.Pass(), Make.Pass()], Make.Return(Make.Constant(89)), 3),  # Fibonacci number
		([Make.Assign(targets=[Make.Name("variableBeta", context=Make.Store())], value=Make.Constant(13))], Make.Return(Make.Name("variableBeta")), 2),
	])
	def testInsertThisBelowCreatesCorrectSequence(self, listNodesToInsert: Sequence[ast.AST], nodeTarget: ast.AST, expectedLengthSequence: int) -> None:
		"""Test insertThisBelow creates sequence with nodes below target."""
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listNodesToInsert)
		sequenceResult = actionInsert(nodeTarget)

		assert len(sequenceResult) == expectedLengthSequence, f"Expected sequence length {expectedLengthSequence}, got {len(sequenceResult)}"
		# Verify target node is first
		assert sequenceResult[0] is nodeTarget, "Target node should be first in sequence"
		# Verify inserted nodes follow
		for indexNode, nodeInserted in enumerate(listNodesToInsert):
			assert sequenceResult[indexNode + 1] is nodeInserted, f"Node at index {indexNode + 1} should be inserted node"

	def testInsertThisBelowLogicalFollowing(self) -> None:
		"""Test insertThisBelow creates logical following (inserted nodes come after)."""
		nodeMain = Make.Assign(
			targets=[Make.Name("variableResult", context=Make.Store())],
			value=Make.Constant(610)  # Fibonacci number
		)
		nodeCleanup = Make.Expr(Make.Call(Make.Name("cleanupResources")))

		actionInsert = Then.insertThisBelow([nodeCleanup])
		sequenceResult = actionInsert(nodeMain)

		assert sequenceResult[0] is nodeMain, "Main node should precede cleanup node"
		assert sequenceResult[1] is nodeCleanup, "Cleanup node should follow main node"

	@pytest.mark.parametrize("countNodesToInsert", [1, 2, 3, 5])
	def testInsertThisBelowWithVariousCountsOfNodes(self, countNodesToInsert: int) -> None:
		"""Test insertThisBelow with various numbers of nodes to insert."""
		nodeTarget = Make.Return(Make.Constant(2584))  # Fibonacci number
		listNodesToInsert = [Make.Pass() for _ in range(countNodesToInsert)]
		actionInsert = Then.insertThisBelow(listNodesToInsert)

		sequenceResult = actionInsert(nodeTarget)

		assert len(sequenceResult) == countNodesToInsert + 1
		assert sequenceResult[0] is nodeTarget

class TestThenRemoveIt:
	"""Test suite for Then.removeIt method."""

	@pytest.mark.parametrize("nodeToRemove", [
		Make.Name("variableNorthward"),
		Make.Constant(233),  # Fibonacci number
		Make.FunctionDef(name="functionEastward"),
		Make.Pass(),
		Make.Assign(targets=[Make.Name("variableWestward", context=Make.Store())], value=Make.Constant(89)),
	])
	def testRemoveItReturnsNone(self, nodeToRemove: ast.AST) -> None:
		"""Test removeIt returns None to signal deletion."""
		resultRemoval = Then.removeIt(nodeToRemove)
		assert resultRemoval is None, "removeIt must return None to signal node deletion"

	def testRemoveItIgnoresNodeContent(self) -> None:
		"""Test removeIt ignores node content and always returns None."""
		nodeComplexFunction = Make.FunctionDef(
			name="functionComplexAlpha",
			argumentSpecification=Make.arguments(list_arg=[Make.arg("parameterPrimary"), Make.arg("parameterSecondary")]),
			body=[
				Make.Assign(
					targets=[Make.Name("resultTertiary", context=Make.Store())],
					value=Make.BinOp(
						left=Make.Name("parameterPrimary"),
						op=Make.Add(),
						right=Make.Name("parameterSecondary")
					)
				),
				Make.Return(Make.Name("resultTertiary"))
			]
		)

		resultRemoval = Then.removeIt(nodeComplexFunction)
		assert resultRemoval is None, "removeIt must return None regardless of node complexity"

class TestThenReplaceWith:
	"""Test suite for Then.replaceWith method."""

	@pytest.mark.parametrize("nodeReplacement,nodeOriginal", [
		(Make.Name("variableNew"), Make.Name("variableOld")),
		(Make.Constant(233), Make.Constant(89)),  # Fibonacci numbers
		(Make.Add(), Make.Mult()),
		(Make.Pass(), Make.Return(Make.Constant(13))),
	])
	def testReplaceWithReturnsReplacementNode(self, nodeReplacement: ast.AST, nodeOriginal: ast.AST) -> None:
		"""Test replaceWith returns the replacement node, discarding original."""
		actionReplace: Callable[[Any], ast.AST] = Then.replaceWith(nodeReplacement)
		nodeReturned = actionReplace(nodeOriginal)

		assert nodeReturned is nodeReplacement, "replaceWith must return the replacement node"
		assert nodeReturned is not nodeOriginal, "Returned node must not be the original node"

	def testReplaceWithIgnoresOriginalNode(self) -> None:
		"""Test replaceWith ignores the original node completely."""
		nodeReplacement = Make.Name("variableReplacement")
		nodeOriginalComplex = Make.FunctionDef(
			name="functionComplexOriginal",
			argumentSpecification=Make.arguments(list_arg=[Make.arg("parameterAlpha")]),
			body=[Make.Return(Make.Constant(377))]  # Fibonacci number
		)

		actionReplace = Then.replaceWith(nodeReplacement)
		nodeReturned = actionReplace(nodeOriginalComplex)

		assert nodeReturned is nodeReplacement
		assert not hasattr(nodeReturned, 'args'), "Replacement node should not have original node's attributes"

	@pytest.mark.parametrize("nodeReplacement", [
		Make.Name("variableNorthward"),
		Make.Constant(610),  # Fibonacci number
		Make.BinOp(left=Make.Constant(2), op=Make.Mult(), right=Make.Constant(3)),
	])
	def testReplaceWithConsistentReplacement(self, nodeReplacement: ast.AST) -> None:
		"""Test replaceWith always returns same replacement regardless of input."""
		actionReplace = Then.replaceWith(nodeReplacement)

		# Call with different original nodes
		listNodesOriginal = [
			Make.Name("variableAlpha"),
			Make.Constant(987),  # Fibonacci number
			Make.Pass()
		]

		for nodeOriginal in listNodesOriginal:
			nodeReturned = actionReplace(nodeOriginal)
			assert nodeReturned is nodeReplacement, "Same replacement should be returned for all originals"

class TestThenUpdateKeyValueIn:
	"""Test suite for Then.updateKeyValueIn method."""

	def testUpdateKeyValueInUsesSetdefault(self) -> None:
		"""Test updateKeyValueIn uses setdefault (doesn't overwrite existing keys)."""
		dictionaryTarget: dict[str, int] = {}

		def extractKey(nodeTarget: ast.AST) -> str:
			return "keyConstant"

		def extractValue(nodeTarget: ast.AST) -> int:
			return getattr(nodeTarget, 'value', 0)

		actionUpdate = Then.updateKeyValueIn(extractKey, extractValue, dictionaryTarget)

		# First update
		nodeFirst = Make.Constant(233)  # Fibonacci number
		actionUpdate(nodeFirst)
		assert dictionaryTarget["keyConstant"] == 233

		# Second update with same key should not overwrite
		nodeSecond = Make.Constant(987)  # Different Fibonacci number
		actionUpdate(nodeSecond)
		assert dictionaryTarget["keyConstant"] == 233, "setdefault should not overwrite existing key"

	def testUpdateKeyValueInReturnsDictionary(self) -> None:
		"""Test updateKeyValueIn returns the dictionary after each update."""
		dictionaryTarget: dict[str, str] = {}

		actionUpdate = Then.updateKeyValueIn(
			lambda nodeTarget: getattr(nodeTarget, 'name', 'unknown'),
			lambda nodeTarget: nodeTarget.__class__.__name__,
			dictionaryTarget
		)

		nodeFunctionFirst = Make.FunctionDef(name="functionAlpha")
		dictionaryFirst = actionUpdate(nodeFunctionFirst)

		assert dictionaryFirst is dictionaryTarget
		assert "functionAlpha" in dictionaryFirst

		nodeFunctionSecond = Make.FunctionDef(name="functionBeta")
		dictionarySecond = actionUpdate(nodeFunctionSecond)

		assert dictionarySecond is dictionaryTarget
		assert "functionBeta" in dictionarySecond
		assert len(dictionaryTarget) == 2

	@pytest.mark.parametrize("listFunctionsKey,listFunctionsValue,listNodesInput,expectedDictionary", [
		(
			# Keys are node types, values are counts
			[lambda nodeTarget: nodeTarget.__class__.__name__],
			[lambda nodeTarget: 1],
			[Make.Name("variableAlpha"), Make.Name("variableBeta"), Make.Constant(89)],
			{"Name": 1, "Constant": 1}  # setdefault means only first occurrence counts
		),
		(
			# Keys are identifiers, values are node types
			[lambda nodeTarget: getattr(nodeTarget, 'id', 'noId')],
			[lambda nodeTarget: nodeTarget.__class__.__name__],
			[Make.Name("variableNorthward"), Make.Name("variableSouthward")],
			{"variableNorthward": "Name", "variableSouthward": "Name"}
		),
	])
	def testUpdateKeyValueInWithVariousExtractors(
		self,
		listFunctionsKey: list[Callable[[ast.AST], Any]],
		listFunctionsValue: list[Callable[[ast.AST], Any]],
		listNodesInput: list[ast.AST],
		expectedDictionary: dict[Any, Any]
	) -> None:
		"""Test updateKeyValueIn with various key and value extractor functions."""
		dictionaryTarget: dict[Any, Any] = {}
		functionKey = listFunctionsKey[0]
		functionValue = listFunctionsValue[0]

		actionUpdate = Then.updateKeyValueIn(functionKey, functionValue, dictionaryTarget)

		for nodeInput in listNodesInput:
			actionUpdate(nodeInput)

		assert dictionaryTarget == expectedDictionary, f"Expected {expectedDictionary}, got {dictionaryTarget}"

class TestThenIntegrationScenarios:
	"""Test suite for integration scenarios combining Then methods."""

	def testAppendToAndExtractItComposition(self) -> None:
		"""Test composing appendTo with extractIt pattern."""
		listCollected: list[ast.AST] = []
		actionAppend = Then.appendTo(listCollected)

		nodeFirst = Make.Name("variableAlpha")
		nodeReturned = actionAppend(nodeFirst)

# extractIt would return the same node
		nodeExtracted = Then.extractIt(nodeReturned)

		assert nodeExtracted is nodeFirst
		assert listCollected[0] is nodeFirst

	def testMultipleActionsOnSameNode(self) -> None:
		"""Test applying multiple Then actions to the same node."""
		nodeTarget = Make.Name("variableTarget")

		# extractIt preserves
		nodeAfterExtract = Then.extractIt(nodeTarget)
		assert nodeAfterExtract is nodeTarget

		# appendTo preserves
		listCollected: list[ast.AST] = []
		nodeAfterAppend = Then.appendTo(listCollected)(nodeTarget)
		assert nodeAfterAppend is nodeTarget

		# replaceWith changes
		nodeReplacement = Make.Constant(1597)  # Fibonacci number
		nodeAfterReplace = Then.replaceWith(nodeReplacement)(nodeTarget)
		assert nodeAfterReplace is nodeReplacement

		# removeIt deletes
		resultAfterRemove = Then.removeIt(nodeTarget)
		assert resultAfterRemove is None

	def testInsertionMethodsCreateIndependentSequences(self) -> None:
		"""Test that insertThisAbove and insertThisBelow create independent sequences."""
		nodeTarget = Make.Return(Make.Constant(4181))  # Fibonacci number
		nodeInsertAbove = Make.Pass()
		nodeInsertBelow = Make.Pass()

		actionInsertAbove = Then.insertThisAbove([nodeInsertAbove])
		sequenceAbove = actionInsertAbove(nodeTarget)

		actionInsertBelow = Then.insertThisBelow([nodeInsertBelow])
		sequenceBelow = actionInsertBelow(nodeTarget)

# Above: inserted nodes first, then target
		assert sequenceAbove[0] is nodeInsertAbove
		assert sequenceAbove[1] is nodeTarget

# Below: target first, then inserted nodes
		assert sequenceBelow[0] is nodeTarget
		assert sequenceBelow[1] is nodeInsertBelow

		# Sequences are independent
		assert len(sequenceAbove) == 2
		assert len(sequenceBelow) == 2
