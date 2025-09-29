"""Tests for the Then class transformation methods using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Make, Then
from collections.abc import Callable, Sequence
import ast

class TestThenExtractionMethods:
	"""Test suite for Then methods that extract or preserve nodes."""

	def testExtractItReturnsNodeUnchanged(self) -> None:
		"""Test extractIt returns the same node unchanged."""
		nodeConstant: ast.Constant = Make.Constant(233)  # Fibonacci number
		resultNode: ast.Constant = Then.extractIt(nodeConstant)
		assert resultNode is nodeConstant, "extractIt should return the exact same node object"

	def testExtractItWithVariousNodeTypes(self) -> None:
		"""Test extractIt with different AST node types."""
		nodeName: ast.Name = Make.Name("variableNorthward")
		nodeCall: ast.Call = Make.Call(Make.Name("functionEastward"))
		nodeAttribute: ast.Attribute = Make.Attribute(Make.Name("objectSouthward"), "propertyWestward")
		
		assert Then.extractIt(nodeName) is nodeName
		assert Then.extractIt(nodeCall) is nodeCall  
		assert Then.extractIt(nodeAttribute) is nodeAttribute

	def testAppendToAddsNodeToList(self) -> None:
		"""Test appendTo adds nodes to collection and returns them unchanged."""
		listCollection: list[ast.AST] = []
		actionAppend: Callable[[ast.AST], ast.AST] = Then.appendTo(listCollection)
		
		nodeConstant: ast.Constant = Make.Constant(89)  # Fibonacci number
		resultNode: ast.Constant = actionAppend(nodeConstant)
		
		assert resultNode is nodeConstant, "appendTo should return the same node"
		assert len(listCollection) == 1, "List should contain one element"
		assert listCollection[0] is nodeConstant, "List should contain the appended node"

	def testAppendToWithMultipleNodes(self) -> None:
		"""Test appendTo accumulates multiple nodes in order."""
		listAccumulator: list[ast.AST] = []
		actionAppend: Callable[[ast.AST], ast.AST] = Then.appendTo(listAccumulator)
		
		nodeFirst: ast.Name = Make.Name("variablePrimary")
		nodeSecond: ast.Constant = Make.Constant(13)  # Fibonacci number
		nodeThird: ast.Attribute = Make.Attribute(Make.Name("objectTertiary"), "methodQuinary")
		
		actionAppend(nodeFirst)
		actionAppend(nodeSecond)
		actionAppend(nodeThird)
		
		assert len(listAccumulator) == 3, "List should contain three elements"
		assert listAccumulator[0] is nodeFirst
		assert listAccumulator[1] is nodeSecond
		assert listAccumulator[2] is nodeThird

class TestThenInsertionMethods:
	"""Test suite for Then methods that insert nodes above or below targets."""

	def testInsertThisAboveCreatesCorrectSequence(self) -> None:
		"""Test insertThisAbove places new nodes before the target node."""
		nodeTarget: ast.Name = Make.Name("targetNodeAlpha")
		nodeInsert1: ast.Constant = Make.Constant(377)  # Fibonacci number
		nodeInsert2: ast.Name = Make.Name("insertedNodeBeta")
		
		listToInsert: list[ast.AST] = [nodeInsert1, nodeInsert2]
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listToInsert)
		
		resultSequence: Sequence[ast.AST] = actionInsert(nodeTarget)
		
		assert len(resultSequence) == 3, "Result should contain three nodes"
		assert resultSequence[0] is nodeInsert1, "First node should be first inserted node"
		assert resultSequence[1] is nodeInsert2, "Second node should be second inserted node"
		assert resultSequence[2] is nodeTarget, "Last node should be the target node"

	def testInsertThisBelowCreatesCorrectSequence(self) -> None:
		"""Test insertThisBelow places new nodes after the target node."""
		nodeTarget: ast.Name = Make.Name("targetNodeGamma")
		nodeInsert1: ast.Constant = Make.Constant(610)  # Fibonacci number
		nodeInsert2: ast.Name = Make.Name("insertedNodeDelta")
		
		listToInsert: list[ast.AST] = [nodeInsert1, nodeInsert2]
		actionInsert: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listToInsert)
		
		resultSequence: Sequence[ast.AST] = actionInsert(nodeTarget)
		
		assert len(resultSequence) == 3, "Result should contain three nodes"
		assert resultSequence[0] is nodeTarget, "First node should be the target node"
		assert resultSequence[1] is nodeInsert1, "Second node should be first inserted node"
		assert resultSequence[2] is nodeInsert2, "Last node should be second inserted node"

	def testInsertionMethodsWithEmptyList(self) -> None:
		"""Test insertion methods with empty lists of nodes to insert."""
		nodeTarget: ast.Name = Make.Name("targetNodeEpsilon")
		listEmpty: list[ast.AST] = []
		
		actionAbove: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove(listEmpty)
		actionBelow: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow(listEmpty)
		
		resultAbove: Sequence[ast.AST] = actionAbove(nodeTarget)
		resultBelow: Sequence[ast.AST] = actionBelow(nodeTarget)
		
		assert len(resultAbove) == 1, "insertThisAbove with empty list should return just target"
		assert resultAbove[0] is nodeTarget, "Result should contain only target node"
		assert len(resultBelow) == 1, "insertThisBelow with empty list should return just target"  
		assert resultBelow[0] is nodeTarget, "Result should contain only target node"

	def testInsertionMethodsWithSingleNode(self) -> None:
		"""Test insertion methods with single node to insert."""
		nodeTarget: ast.Name = Make.Name("targetNodeZeta")
		nodeInsert: ast.Constant = Make.Constant(987)  # Fibonacci number
		
		actionAbove: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisAbove([nodeInsert])
		actionBelow: Callable[[ast.AST], Sequence[ast.AST]] = Then.insertThisBelow([nodeInsert])
		
		resultAbove: Sequence[ast.AST] = actionAbove(nodeTarget)
		resultBelow: Sequence[ast.AST] = actionBelow(nodeTarget)
		
		assert len(resultAbove) == 2, "insertThisAbove should return two nodes"
		assert resultAbove[0] is nodeInsert, "First node should be inserted node"
		assert resultAbove[1] is nodeTarget, "Second node should be target node"
		
		assert len(resultBelow) == 2, "insertThisBelow should return two nodes"
		assert resultBelow[0] is nodeTarget, "First node should be target node"
		assert resultBelow[1] is nodeInsert, "Second node should be inserted node"

class TestThenRemovalAndReplacementMethods:
	"""Test suite for Then methods that remove or replace nodes."""

	def testRemoveItReturnsNone(self) -> None:
		"""Test removeIt returns None to signal node deletion."""
		nodeToRemove: ast.Name = Make.Name("nodeToRemoveEta")
		result: None = Then.removeIt(nodeToRemove)
		assert result is None, "removeIt should return None to signal deletion"

	def testRemoveItWithVariousNodeTypes(self) -> None:
		"""Test removeIt returns None regardless of node type."""
		nodeConstant: ast.Constant = Make.Constant(1597)  # Fibonacci number
		nodeCall: ast.Call = Make.Call(Make.Name("functionTheta"))
		nodeAttribute: ast.Attribute = Make.Attribute(Make.Name("objectIota"), "propertyKappa")
		
		assert Then.removeIt(nodeConstant) is None
		assert Then.removeIt(nodeCall) is None
		assert Then.removeIt(nodeAttribute) is None

	def testReplaceWithReturnsReplacementNode(self) -> None:
		"""Test replaceWith returns replacement node and ignores original."""
		nodeOriginal: ast.Name = Make.Name("originalNodeLambda")
		nodeReplacement: ast.Constant = Make.Constant(2584)  # Fibonacci number
		
		actionReplace: Callable[[ast.AST], ast.Constant] = Then.replaceWith(nodeReplacement)
		result: ast.Constant = actionReplace(nodeOriginal)
		
		assert result is nodeReplacement, "replaceWith should return the replacement node"

	def testReplaceWithIgnoresOriginalNode(self) -> None:
		"""Test replaceWith ignores the original node completely."""
		nodeReplacement: ast.Name = Make.Name("replacementNodeMu")
		actionReplace: Callable[[ast.AST], ast.Name] = Then.replaceWith(nodeReplacement)
		
		# Test with various original node types
		nodeOriginal1: ast.Constant = Make.Constant(4181)  # Fibonacci number
		nodeOriginal2: ast.Call = Make.Call(Make.Name("functionNu"))
		nodeOriginal3: ast.Attribute = Make.Attribute(Make.Name("objectXi"), "propertyOmicron")
		
		assert actionReplace(nodeOriginal1) is nodeReplacement
		assert actionReplace(nodeOriginal2) is nodeReplacement  
		assert actionReplace(nodeOriginal3) is nodeReplacement

class TestThenUpdateMethods:
	"""Test suite for Then methods that update dictionaries with node data."""

	def testUpdateKeyValueInUpdatesDict(self) -> None:
		"""Test updateKeyValueIn extracts and stores key-value pairs from nodes."""
		dictionaryTarget: dict[str, int] = {}
		
		# Create key and value extraction functions
		keyExtractor: Callable[[ast.Constant], str] = lambda node: f"constant_{node.value}"
		valueExtractor: Callable[[ast.Constant], int] = lambda node: node.value * 2
		
		actionUpdate: Callable[[ast.Constant], dict[str, int]] = Then.updateKeyValueIn(
			keyExtractor, valueExtractor, dictionaryTarget
		)
		
		nodeConstant: ast.Constant = Make.Constant(6765)  # Fibonacci number
		resultDict: dict[str, int] = actionUpdate(nodeConstant)
		
		expectedKey: str = "constant_6765"
		expectedValue: int = 13530  # 6765 * 2
		
		assert resultDict is dictionaryTarget, "Should return the same dictionary object"
		assert len(dictionaryTarget) == 1, "Dictionary should contain one entry"
		assert dictionaryTarget[expectedKey] == expectedValue, f"Dictionary should contain {expectedKey}: {expectedValue}"

	def testUpdateKeyValueInWithMultipleNodes(self) -> None:
		"""Test updateKeyValueIn with multiple nodes accumulates data correctly."""
		dictionaryAccumulator: dict[str, str] = {}
		
		# Extract node type as key and identifier as value
		keyExtractor: Callable[[ast.Name], str] = lambda _node: "name_type"
		valueExtractor: Callable[[ast.Name], str] = lambda node: node.id
		
		actionUpdate: Callable[[ast.Name], dict[str, str]] = Then.updateKeyValueIn(
			keyExtractor, valueExtractor, dictionaryAccumulator
		)
		
		nodeFirst: ast.Name = Make.Name("variablePi")
		nodeSecond: ast.Name = Make.Name("variableRho")  # This will overwrite due to same key
		
		actionUpdate(nodeFirst)
		actionUpdate(nodeSecond)
		
		assert len(dictionaryAccumulator) == 1, "Dictionary should contain one entry (key collision)"
		assert dictionaryAccumulator["name_type"] == "variablePi", "Should preserve first value (setdefault behavior)"

	def testUpdateKeyValueInUsesSetdefaultBehavior(self) -> None:
		"""Test updateKeyValueIn uses setdefault to avoid overwriting existing entries."""
		dictionaryPrePopulated: dict[str, int] = {"existing_key": 10946}  # Fibonacci number
		
		keyExtractor: Callable[[ast.Constant], str] = lambda _node: "existing_key"
		valueExtractor: Callable[[ast.Constant], int] = lambda node: node.value
		
		actionUpdate: Callable[[ast.Constant], dict[str, int]] = Then.updateKeyValueIn(
			keyExtractor, valueExtractor, dictionaryPrePopulated
		)
		
		nodeConstant: ast.Constant = Make.Constant(17711)  # Fibonacci number
		actionUpdate(nodeConstant)
		
		assert dictionaryPrePopulated["existing_key"] == 10946, "Existing value should not be overwritten"

	def testUpdateKeyValueInWithComplexKeyValueExtraction(self) -> None:
		"""Test updateKeyValueIn with more complex key-value extraction scenarios."""
		dictionaryComplex: dict[tuple[str, str], list[str]] = {}
		
		# Create complex extractors that work with Name nodes
		keyExtractor: Callable[[ast.Name], tuple[str, str]] = lambda node: (node.id, type(node).__name__)
		valueExtractor: Callable[[ast.Name], list[str]] = lambda node: [node.id.upper(), node.id.lower()]
		
		actionUpdate: Callable[[ast.Name], dict[tuple[str, str], list[str]]] = Then.updateKeyValueIn(
			keyExtractor, valueExtractor, dictionaryComplex
		)
		
		nodeName: ast.Name = Make.Name("variableSigma")
		resultDict: dict[tuple[str, str], list[str]] = actionUpdate(nodeName)
		
		expectedKey: tuple[str, str] = ("variableSigma", "Name")
		expectedValue: list[str] = ["VARIABLESIGMA", "variablesigma"]
		
		assert resultDict is dictionaryComplex
		assert len(dictionaryComplex) == 1
		assert dictionaryComplex[expectedKey] == expectedValue

class TestThenIntegrationScenarios:
	"""Test suite for real-world integration scenarios using Then methods."""

	def testAppendToWithNodeTouristLikePattern(self) -> None:
		"""Test appendTo in a pattern similar to NodeTourist usage."""
		# Simulate collecting all Name nodes from a hypothetical AST traversal
		listCollectedNames: list[ast.Name] = []
		actionCollect: Callable[[ast.Name], ast.Name] = Then.appendTo(listCollectedNames)
		
		# Simulate visiting multiple Name nodes
		nameNodes: list[ast.Name] = [
			Make.Name("variableTau"),
			Make.Name("functionUpsilon"),
			Make.Name("classPhi"),
		]
		
		for node in nameNodes:
			returnedNode: ast.Name = actionCollect(node)
			assert returnedNode is node, "Each node should be returned unchanged"
		
		assert len(listCollectedNames) == 3, "All nodes should be collected"
		for i, expectedNode in enumerate(nameNodes):
			assert listCollectedNames[i] is expectedNode, f"Node at index {i} should match expected node"

	def testChainedTransformationsPattern(self) -> None:
		"""Test a pattern where multiple Then methods could be used in sequence."""
		# Test that different Then methods can work with the same node types
		nodeOriginal: ast.Constant = Make.Constant(28657)  # Fibonacci number
		
		# Test extraction (identity)
		extractedNode: ast.Constant = Then.extractIt(nodeOriginal)
		assert extractedNode is nodeOriginal
		
		# Test replacement
		nodeReplacement: ast.Name = Make.Name("replacementChi")
		actionReplace: Callable[[ast.Constant], ast.Name] = Then.replaceWith(nodeReplacement)
		replacedNode: ast.Name = actionReplace(nodeOriginal)
		assert replacedNode is nodeReplacement
		
		# Test removal
		removalResult: None = Then.removeIt(nodeOriginal)
		assert removalResult is None

	def testNodeTransformationWithSequenceOperations(self) -> None:
		"""Test sequence operations for AST transformation scenarios."""
		nodeTarget: ast.Name = Make.Name("targetPsi")
		
		# Create nodes to insert
		nodeComment: ast.Expr = Make.Expr(Make.Constant("# This is a comment"))
		nodeImport: ast.Import = Make.Import([Make.alias("moduleOmega")])
		
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