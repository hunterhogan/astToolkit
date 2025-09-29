"""Tests for the Then class transformation methods using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Make, Then
from collections.abc import Callable, Sequence
from typing import Any
import ast
import pytest

class TestThenExtractionMethods:
	"""Test suite for Then methods that extract or preserve nodes."""

	@pytest.mark.parametrize("nodeInput", [
		Make.Constant(233),  # Fibonacci number
		Make.Name("variableNorthward"),
		Make.Call(Make.Name("functionEastward")),
		Make.Attribute(Make.Name("objectSouthward"), "propertyWestward"),
	])
	def testExtractItReturnsNodeUnchanged(self, nodeInput: ast.AST) -> None:
		"""Test extractIt returns the same node unchanged."""
		extractedNode: ast.AST = Then.extractIt(nodeInput)
		assert extractedNode is nodeInput, "extractIt should return the exact same node object"

	@pytest.mark.parametrize("nodeToCollect", [Make.Constant(89)])
	def testAppendToAddsNodeToList(self, nodeToCollect: ast.AST) -> None:
		"""Test appendTo adds nodes to collection and returns them unchanged."""
		listCollection: list[ast.AST] = []
		actionAppend: Callable[[ast.AST], ast.AST] = Then.appendTo(listCollection)
		
		returnedNode: ast.AST = actionAppend(nodeToCollect)
		
		assert returnedNode is nodeToCollect, "appendTo should return the same node"
		assert len(listCollection) == 1, "List should contain one element"
		assert listCollection[0] is nodeToCollect, "List should contain the appended node"

	@pytest.mark.parametrize("listNodes", [
		[Make.Name("variablePrimary"), Make.Constant(13), Make.Attribute(Make.Name("objectTertiary"), "methodQuinary")],
		[Make.Pass(), Make.Import([Make.alias("moduleAlpha")])],
		[Make.Constant(377), Make.Name("functionBeta"), Make.Call(Make.Name("callableGamma"))],
	])
	def testAppendToWithMultipleNodes(self, listNodes: list[ast.AST]) -> None:
		"""Test appendTo accumulates multiple nodes in order."""
		listAccumulator: list[ast.AST] = []
		actionAppend: Callable[[ast.AST], ast.AST] = Then.appendTo(listAccumulator)
		
		for node in listNodes:
			returnedNode = actionAppend(node)
			assert returnedNode is node, "Each node should be returned unchanged"
		
		assert len(listAccumulator) == len(listNodes), f"List should contain {len(listNodes)} elements"
		for i, expectedNode in enumerate(listNodes):
			assert listAccumulator[i] is expectedNode, f"Node at index {i} should match expected node"

class TestThenInsertionMethods:
	"""Test suite for Then methods that insert nodes above or below targets."""

	@pytest.mark.parametrize("targetNode,listToInsert", [
		(Make.Name("targetNodeAlpha"), [Make.Constant(377), Make.Name("insertedNodeBeta")]),
		(Make.Call(Make.Name("functionGamma")), [Make.Pass(), Make.Import([Make.alias("moduleDelta")])]),
		(Make.Attribute(Make.Name("objectEpsilon"), "propertyZeta"), [Make.Constant(610)]),
	])
	def testInsertThisAboveCreatesCorrectSequence(self, targetNode: ast.AST, listToInsert: list[ast.AST]) -> None:
		"""Test insertThisAbove places new nodes before the target node."""
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listToInsert)
		sequenceCreated: Sequence[ast.AST] = actionInsert(targetNode)
		
		expectedLength = len(listToInsert) + 1
		assert len(sequenceCreated) == expectedLength, f"Sequence should contain {expectedLength} nodes"
		
		# Check that inserted nodes come first
		for i, expectedInserted in enumerate(listToInsert):
			assert sequenceCreated[i] is expectedInserted, f"Node at index {i} should be inserted node {i}"
		
		# Check that target comes last
		assert sequenceCreated[-1] is targetNode, "Last node should be the target node"

	@pytest.mark.parametrize("targetNode,listToInsert", [
		(Make.Name("targetNodeGamma"), [Make.Constant(987), Make.Name("insertedNodeDelta")]),
		(Make.Call(Make.Name("functionEta")), [Make.Pass()]),
		(Make.Attribute(Make.Name("objectTheta"), "propertyIota"), [Make.Import([Make.alias("moduleKappa")], level=1)]),
	])
	def testInsertThisBelowCreatesCorrectSequence(self, targetNode: ast.AST, listToInsert: list[ast.AST]) -> None:
		"""Test insertThisBelow places new nodes after the target node."""
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listToInsert)
		sequenceCreated: Sequence[ast.AST] = actionInsert(targetNode)
		
		expectedLength = len(listToInsert) + 1
		assert len(sequenceCreated) == expectedLength, f"Sequence should contain {expectedLength} nodes"
		
		# Check that target comes first
		assert sequenceCreated[0] is targetNode, "First node should be the target node"
		
		# Check that inserted nodes come after
		for i, expectedInserted in enumerate(listToInsert):
			assert sequenceCreated[i + 1] is expectedInserted, f"Node at index {i+1} should be inserted node {i}"

	@pytest.mark.parametrize("targetNode", [
		Make.Name("targetNodeLambda"),
		Make.Constant(1597),
		Make.Call(Make.Name("functionMu")),
	])
	def testInsertionMethodsWithEmptyList(self, targetNode: ast.AST) -> None:
		"""Test insertion methods with empty lists of nodes to insert."""
		listEmpty: list[ast.AST] = []
		
		actionAbove: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listEmpty)
		actionBelow: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listEmpty)
		
		sequenceAbove: Sequence[ast.AST] = actionAbove(targetNode)
		sequenceBelow: Sequence[ast.AST] = actionBelow(targetNode)
		
		assert len(sequenceAbove) == 1, "insertThisAbove with empty list should return just target"
		assert sequenceAbove[0] is targetNode, "Sequence should contain only target node"
		assert len(sequenceBelow) == 1, "insertThisBelow with empty list should return just target"  
		assert sequenceBelow[0] is targetNode, "Sequence should contain only target node"

	@pytest.mark.parametrize("targetNode,nodeToInsert", [
		(Make.Name("targetNodeNu"), Make.Constant(2584)),
		(Make.Call(Make.Name("functionXi")), Make.Pass()),
		(Make.Attribute(Make.Name("objectOmicron"), "propertyPi"), Make.Import([Make.alias("moduleRho")])),
	])
	def testInsertionMethodsWithSingleNode(self, targetNode: ast.AST, nodeToInsert: ast.AST) -> None:
		"""Test insertion methods with single node to insert."""
		actionAbove: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove([nodeToInsert])
		actionBelow: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow([nodeToInsert])
		
		sequenceAbove: Sequence[ast.AST] = actionAbove(targetNode)
		sequenceBelow: Sequence[ast.AST] = actionBelow(targetNode)
		
		assert len(sequenceAbove) == 2, "insertThisAbove should return two nodes"
		assert sequenceAbove[0] is nodeToInsert, "First node should be inserted node"
		assert sequenceAbove[1] is targetNode, "Second node should be target node"
		
		assert len(sequenceBelow) == 2, "insertThisBelow should return two nodes"
		assert sequenceBelow[0] is targetNode, "First node should be target node"
		assert sequenceBelow[1] is nodeToInsert, "Second node should be inserted node"

class TestThenRemovalAndReplacementMethods:
	"""Test suite for Then methods that remove or replace nodes."""

	@pytest.mark.parametrize("nodeToRemove", [
		Make.Name("nodeToRemoveEta"),
		Make.Constant(1597),
		Make.Call(Make.Name("functionTheta")),
		Make.Attribute(Make.Name("objectIota"), "propertyKappa"),
	])
	def testRemoveItReturnsNone(self, nodeToRemove: ast.AST) -> None:
		"""Test removeIt returns None to signal node deletion."""
		deletionSignal: None = Then.removeIt(nodeToRemove)
		assert deletionSignal is None, "removeIt should return None to signal deletion"

	@pytest.mark.parametrize("nodeOriginal,nodeReplacement", [
		(Make.Name("originalNodeLambda"), Make.Constant(2584)),
		(Make.Constant(4181), Make.Name("replacementNodeMu")),
		(Make.Call(Make.Name("functionNu")), Make.Attribute(Make.Name("objectXi"), "propertyOmicron")),
		(Make.Attribute(Make.Name("objectPi"), "propertyRho"), Make.Pass()),
	])
	def testReplaceWithReturnsReplacementNode(self, nodeOriginal: ast.AST, nodeReplacement: ast.AST) -> None:
		"""Test replaceWith returns replacement node and ignores original."""
		actionReplace: Callable[[ast.AST], ast.AST] = Then.replaceWith(nodeReplacement)
		substitutedNode: ast.AST = actionReplace(nodeOriginal)
		
		assert substitutedNode is nodeReplacement, "replaceWith should return the replacement node"

	@pytest.mark.parametrize("nodeReplacement", [
		Make.Name("replacementSigma"),
		Make.Constant(6765),
		Make.Call(Make.Name("functionTau")),
	])
	def testReplaceWithIgnoresOriginalNode(self, nodeReplacement: ast.AST) -> None:
		"""Test replaceWith ignores the original node completely."""
		actionReplace: Callable[[ast.AST], ast.AST] = Then.replaceWith(nodeReplacement)
		
		# Test with various original node types - all should return same replacement
		originalNodes = [
			Make.Constant(10946),
			Make.Call(Make.Name("functionUpsilon")),
			Make.Attribute(Make.Name("objectPhi"), "propertyPsi"),
		]
		
		for nodeOriginal in originalNodes:
			substitutedNode = actionReplace(nodeOriginal)
			assert substitutedNode is nodeReplacement, "All originals should be replaced with same node"

class TestThenUpdateMethods:
	"""Test suite for Then methods that update dictionaries with node data."""

	def testUpdateKeyValueInUpdatesDict(self, thenUpdateKeyValueTestData: tuple[type, Callable, Callable, ast.AST, Any, Any]) -> None:
		"""Test updateKeyValueIn extracts and stores key-value pairs from nodes."""
		dictType, keyExtractor, valueExtractor, nodeInput, expectedKey, expectedValue = thenUpdateKeyValueTestData
		dictionaryTarget = dictType()
		
		actionUpdate = Then.updateKeyValueIn(keyExtractor, valueExtractor, dictionaryTarget)
		updatedDict = actionUpdate(nodeInput)
		
		assert updatedDict is dictionaryTarget, "Should return the same dictionary object"
		assert len(dictionaryTarget) == 1, "Dictionary should contain one entry"
		assert dictionaryTarget[expectedKey] == expectedValue, f"Dictionary should contain {expectedKey}: {expectedValue}"

	@pytest.mark.parametrize("listNodes", [
		[Make.Name("variablePi"), Make.Name("variableRho")],
		[Make.Name("nameAlpha"), Make.Name("nameBeta"), Make.Name("nameGamma")],
	])
	def testUpdateKeyValueInWithMultipleNodes(self, listNodes: list[ast.Name]) -> None:
		"""Test updateKeyValueIn with multiple nodes accumulates data correctly."""
		dictionaryAccumulator: dict[str, str] = {}
		
		# Extract node type as key and identifier as value - will cause key collision
		keyExtractor: Callable[[ast.Name], str] = lambda _node: "name_type"
		valueExtractor: Callable[[ast.Name], str] = lambda node: node.id
		
		actionUpdate = Then.updateKeyValueIn(keyExtractor, valueExtractor, dictionaryAccumulator)
		
		for node in listNodes:
			actionUpdate(node)
		
		assert len(dictionaryAccumulator) == 1, "Dictionary should contain one entry (key collision)"
		assert dictionaryAccumulator["name_type"] == listNodes[0].id, "Should preserve first value (setdefault behavior)"

	@pytest.mark.parametrize("existingValue,newValue", [(10946, 17711)])
	def testUpdateKeyValueInUsesSetdefaultBehavior(self, existingValue: int, newValue: int) -> None:
		"""Test updateKeyValueIn uses setdefault to avoid overwriting existing entries."""
		dictionaryPrePopulated: dict[str, int] = {"existing_key": existingValue}  # Fibonacci number
		
		keyExtractor: Callable[[ast.Constant], str] = lambda _node: "existing_key"
		valueExtractor: Callable[[ast.Constant], int] = lambda node: node.value
		
		actionUpdate = Then.updateKeyValueIn(keyExtractor, valueExtractor, dictionaryPrePopulated)
		
		nodeConstant: ast.Constant = Make.Constant(newValue)  # Fibonacci number
		actionUpdate(nodeConstant)
		
		assert dictionaryPrePopulated["existing_key"] == existingValue, "Existing value should not be overwritten"

	@pytest.mark.parametrize("nodeInput,expectedKey,expectedValue", [
		(Make.Name("variableOmega"), ("variableOmega", "Name"), ["VARIABLEOMEGA", "variableomega"]),
		(Make.Name("functionAlpha"), ("functionAlpha", "Name"), ["FUNCTIONALPHA", "functionalpha"]),
		(Make.Name("classBeta"), ("classBeta", "Name"), ["CLASSBETA", "classbeta"]),
	])
	def testUpdateKeyValueInWithComplexKeyValueExtraction(self, nodeInput: ast.Name, expectedKey: tuple[str, str], expectedValue: list[str]) -> None:
		"""Test updateKeyValueIn with more complex key-value extraction scenarios."""
		dictionaryComplex: dict[tuple[str, str], list[str]] = {}
		
		# Create complex extractors that work with Name nodes
		keyExtractor: Callable[[ast.Name], tuple[str, str]] = lambda node: (node.id, type(node).__name__)
		valueExtractor: Callable[[ast.Name], list[str]] = lambda node: [node.id.upper(), node.id.lower()]
		
		actionUpdate = Then.updateKeyValueIn(keyExtractor, valueExtractor, dictionaryComplex)
		updatedDict = actionUpdate(nodeInput)
		
		assert updatedDict is dictionaryComplex
		assert len(dictionaryComplex) == 1
		assert dictionaryComplex[expectedKey] == expectedValue

class TestThenIntegrationScenarios:
	"""Test suite for real-world integration scenarios using Then methods."""

	@pytest.mark.parametrize("listNameNodes", [
		[Make.Name("variableTau"), Make.Name("functionUpsilon"), Make.Name("classPhi")],
		[Make.Name("identifierAlpha"), Make.Name("identifierBeta")],
		[Make.Name("singleVariable")],
	])
	def testAppendToWithNodeTouristLikePattern(self, listNameNodes: list[ast.Name]) -> None:
		"""Test appendTo in a pattern similar to NodeTourist usage."""
		# Simulate collecting all Name nodes from a hypothetical AST traversal
		listCollectedNames: list[ast.Name] = []
		actionCollect: Callable[[ast.Name], ast.Name] = Then.appendTo(listCollectedNames)
		
		# Simulate visiting multiple Name nodes
		for node in listNameNodes:
			returnedNode: ast.Name = actionCollect(node)
			assert returnedNode is node, "Each node should be returned unchanged"
		
		assert len(listCollectedNames) == len(listNameNodes), "All nodes should be collected"
		for i, expectedNode in enumerate(listNameNodes):
			assert listCollectedNames[i] is expectedNode, f"Node at index {i} should match expected node"

	@pytest.mark.parametrize("nodeOriginal,nodeReplacement", [
		(Make.Constant(28657), Make.Name("replacementChi")),
		(Make.Name("originalPsi"), Make.Constant(46368)),
		(Make.Call(Make.Name("functionOmega")), Make.Attribute(Make.Name("objectAlpha"), "propertyBeta")),
	])
	def testChainedTransformationsPattern(self, nodeOriginal: ast.AST, nodeReplacement: ast.AST) -> None:
		"""Test a pattern where multiple Then methods could be used in sequence."""
		# Test that different Then methods can work with the same node types
		
		# Test extraction (identity)
		extractedNode: ast.AST = Then.extractIt(nodeOriginal)
		assert extractedNode is nodeOriginal
		
		# Test replacement
		actionReplace: Callable[[ast.AST], ast.AST] = Then.replaceWith(nodeReplacement)
		replacedNode: ast.AST = actionReplace(nodeOriginal)
		assert replacedNode is nodeReplacement
		
		# Test removal
		removalSignal: None = Then.removeIt(nodeOriginal)
		assert removalSignal is None

	@pytest.mark.parametrize("nodeTarget,nodeComment,nodeImport", [
		(Make.Name("targetPsi"), Make.Expr(Make.Constant("# This is a comment")), Make.Import([Make.alias("moduleOmega")])),
		(Make.Call(Make.Name("functionGamma")), Make.Expr(Make.Constant("# Another comment")), Make.Import([Make.alias("packageDelta")], level=1)),
		(Make.Attribute(Make.Name("objectEpsilon"), "methodZeta"), Make.Expr(Make.Constant("# Third comment")), Make.ImportFrom("moduleEta", [Make.alias("itemTheta")])),
	])
	def testNodeTransformationWithSequenceOperations(self, nodeTarget: ast.AST, nodeComment: ast.Expr, nodeImport: ast.stmt) -> None:
		"""Test sequence operations for AST transformation scenarios."""
		# Create nodes to insert
		listAbove: list[ast.AST] = [nodeComment, nodeImport]
		listBelow: list[ast.AST] = [Make.Pass()]
		
		# Test both insertion directions
		actionAbove: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listAbove)
		actionBelow: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listBelow)
		
		sequenceAbove: Sequence[ast.AST] = actionAbove(nodeTarget)
		sequenceBelow: Sequence[ast.AST] = actionBelow(nodeTarget)
		
		# Verify above insertion
		assert len(sequenceAbove) == 3
		assert sequenceAbove[0] is nodeComment
		assert sequenceAbove[1] is nodeImport
		assert sequenceAbove[2] is nodeTarget
		
		# Verify below insertion
		assert len(sequenceBelow) == 2
		assert sequenceBelow[0] is nodeTarget
		assert isinstance(sequenceBelow[1], ast.Pass)