"""Tests for the Grab class using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Grab, Make
from collections.abc import Callable
from typing import Any
import ast
import pytest

class TestGrabAttributeMethods:
	"""Test suite for Grab attribute modification methods."""

	def testAttributeModificationMethods(self, grabAttributeTestData: tuple[str, Callable[[], ast.AST], Callable[[Any], Any], Any]) -> None:
		"""Test attribute modification methods using parametrized data."""
		methodNameGrab, factoryNodeOriginal, actionTransform, expectedAttributeValue = grabAttributeTestData

		# Get the method from Grab
		methodGrab = getattr(Grab, methodNameGrab)

		# Create the original node
		nodeOriginal = factoryNodeOriginal()

		# Create the action
		actionGrab = methodGrab(actionTransform)

		# Apply the action
		nodeModified = actionGrab(nodeOriginal)

		# Verify the node is modified in place
		assert nodeModified is nodeOriginal, f"{methodNameGrab} should modify node in place"

		# Get the attribute name (remove "Attribute" suffix)
		attributeName = methodNameGrab[:-9] if methodNameGrab.endswith("Attribute") else methodNameGrab

		# Verify the attribute value
		actualAttributeValue = getattr(nodeModified, attributeName)
		assert actualAttributeValue == expectedAttributeValue, f"{methodNameGrab} should set {attributeName} to {expectedAttributeValue}, got {actualAttributeValue}"

	@pytest.mark.parametrize("methodNameGrab,factoryNode,actionTransform", [
		("idAttribute", lambda: Make.Name("variableAlpha"), lambda identifierOld: identifierOld.upper()),
		("argAttribute", lambda: Make.arg("paramBeta"), lambda identifierOld: identifierOld + "_modified"),
		("attrAttribute", lambda: Make.Attribute(Make.Name("objGamma"), "attrDelta"), lambda identifierOld: "new_" + identifierOld),
	])
	def testAttributeModificationPreservesOtherAttributes(self, methodNameGrab: str, factoryNode: Callable[[], ast.AST], actionTransform: Callable[[str], str]) -> None:
		"""Test that attribute modification preserves other attributes."""
		nodeOriginal = factoryNode()

		# Store original state of other attributes
		dictionaryOriginalAttributes = {attributeName: getattr(nodeOriginal, attributeName, None) for attributeName in dir(nodeOriginal) if not attributeName.startswith('_')}

		# Apply the modification
		methodGrab = getattr(Grab, methodNameGrab)
		actionGrab = methodGrab(actionTransform)
		nodeModified = actionGrab(nodeOriginal)

		# Get the modified attribute name
		attributeNameModified = methodNameGrab[:-9] if methodNameGrab.endswith("Attribute") else methodNameGrab

		# Verify other attributes are unchanged
		for attributeName, valueOriginal in dictionaryOriginalAttributes.items():
			if attributeName != attributeNameModified:
				valueModified = getattr(nodeModified, attributeName, None)
				if valueOriginal is not None:
					assert valueModified == valueOriginal, f"Attribute {attributeName} should remain unchanged"

class TestGrabIndexMethod:
	"""Test suite for Grab.index method."""

	def testIndexModification(self, grabIndexTestData: tuple[str, Callable[[], list[ast.AST]], int, Callable[[ast.AST], ast.AST | list[ast.AST] | None], list[str]]) -> None:
		"""Test index method using parametrized data."""
		descriptionTest, factoryListOriginal, indexTarget, actionTransform, listExpectedIdentifiers = grabIndexTestData

		# Create the original list
		listOriginal = factoryListOriginal()

		# Create the action
		actionGrab = Grab.index(indexTarget, actionTransform)

		# Apply the action
		listModified = actionGrab(listOriginal)

		# Verify the result
		assert isinstance(listModified, list), "Grab.index should return a list"
		listActualIdentifiers = [node.id for node in listModified]
		assert listActualIdentifiers == listExpectedIdentifiers, f"{descriptionTest}: expected {listExpectedIdentifiers}, got {listActualIdentifiers}"

	@pytest.mark.parametrize("indexTarget,actionDescription", [
		(0, "first_element"),
		(2, "last_element"),
		(-1, "negative_index"),
	])
	def testIndexAtVariousPositions(self, indexTarget: int, actionDescription: str) -> None:
		"""Test index method at various positions using Fibonacci numbers."""
		listOriginal = [Make.Name("fib8"), Make.Name("fib13"), Make.Name("fib21")]

		actionGrab = Grab.index(indexTarget, lambda node: Make.Name(node.id.upper()))
		listModified = actionGrab(listOriginal)

		# Verify the correct element was modified
		assert listModified[indexTarget].id == listOriginal[indexTarget].id.upper(), f"Element at index {indexTarget} should be modified"

	def testIndexDeleteAllElements(self) -> None:
		"""Test index method to delete all elements sequentially."""
		listOriginal = [Make.Name("alpha"), Make.Name("beta"), Make.Name("gamma")]

		# Delete elements one by one
		actionDelete = Grab.index(0, lambda node: None)
		listAfterFirst = actionDelete(listOriginal)
		assert len(listAfterFirst) == 2, "Should have 2 elements after first deletion"

		listAfterSecond = actionDelete(listAfterFirst)
		assert len(listAfterSecond) == 1, "Should have 1 element after second deletion"

		listAfterThird = actionDelete(listAfterSecond)
		assert len(listAfterThird) == 0, "Should have 0 elements after third deletion"

	def testIndexExpansionMultipleTimes(self) -> None:
		"""Test index method with multiple expansions."""
		listOriginal = [Make.Name("north"), Make.Name("south")]

		# Expand first element
		actionExpand = Grab.index(0, lambda node: [Make.Name("west"), Make.Name("east")])
		listExpanded = actionExpand(listOriginal)
		assert len(listExpanded) == 3, "Should have 3 elements after first expansion"
		assert [n.id for n in listExpanded] == ["west", "east", "south"], "Expansion should replace element with list"

class TestGrabAndDoAllOfMethod:
	"""Test suite for Grab.andDoAllOf method."""

	def testAndDoAllOfWithChainedActions(self) -> None:
		"""Test andDoAllOf with chained attribute modifications."""
		nodeOriginal = Make.Name("variableAlpha")

		actionChained = Grab.andDoAllOf([
			Grab.idAttribute(lambda identifierOld: identifierOld + "_step1"),
			Grab.idAttribute(lambda identifierOld: identifierOld + "_step2"),
			Grab.idAttribute(lambda identifierOld: identifierOld + "_step3"),
		])

		nodeModified = actionChained(nodeOriginal)

		assert nodeModified is nodeOriginal, "andDoAllOf should modify node in place"
		assert nodeModified.id == "variableAlpha_step1_step2_step3", "Actions should be applied in sequence"

	def testAndDoAllOfWithEmptyList(self) -> None:
		"""Test andDoAllOf with empty action list."""
		nodeOriginal = Make.Name("variableBeta")

		actionChained = Grab.andDoAllOf([])
		nodeModified = actionChained(nodeOriginal)

		assert nodeModified is nodeOriginal, "andDoAllOf should return same node"
		assert nodeModified.id == "variableBeta", "Node should be unchanged"

	def testAndDoAllOfWithSingleAction(self) -> None:
		"""Test andDoAllOf with single action."""
		nodeOriginal = Make.arg("paramGamma")

		actionChained = Grab.andDoAllOf([
			Grab.argAttribute(lambda identifierOld: identifierOld.upper()),
		])

		nodeModified = actionChained(nodeOriginal)

		assert nodeModified is nodeOriginal, "andDoAllOf should modify node in place"
		assert nodeModified.arg == "PARAMGAMMA", "Single action should be applied"

	@pytest.mark.parametrize("countActions,suffixExpected", [
		(2, "_1_2"),
		(5, "_1_2_3_4_5"),
		(8, "_1_2_3_4_5_6_7_8"),  # Fibonacci number
	])
	def testAndDoAllOfWithVariousActionCounts(self, countActions: int, suffixExpected: str) -> None:
		"""Test andDoAllOf with various numbers of actions using Fibonacci numbers."""
		nodeOriginal = Make.Name("base")

		listActions = [
			Grab.idAttribute(lambda identifierOld, index=indexAction: identifierOld + f"_{index}")
			for indexAction in range(1, countActions + 1)
		]

		actionChained = Grab.andDoAllOf(listActions)
		nodeModified = actionChained(nodeOriginal)

		assert nodeModified.id == f"base{suffixExpected}", f"Should apply {countActions} actions in sequence"

	def testAndDoAllOfWithDifferentAttributeTypes(self) -> None:
		"""Test andDoAllOf modifying different attributes sequentially."""
		nodeFunctionDef = Make.FunctionDef(name="functionAlpha", body=[Make.Pass()])

		actionChained = Grab.andDoAllOf([
			Grab.nameAttribute(lambda identifierOld: identifierOld + "Modified"),
			Grab.bodyAttribute(lambda listBody: listBody + [Make.Return(Make.Constant(None))]),
		])

		nodeModified = actionChained(nodeFunctionDef)

		assert nodeModified.name == "functionAlphaModified", "Name should be modified"
		assert len(nodeModified.body) == 2, "Body should have 2 statements"
		assert isinstance(nodeModified.body[1], ast.Return), "Second statement should be Return"

class TestGrabComplexScenarios:
	"""Test suite for complex Grab usage scenarios."""

	def testNestedGrabOperations(self) -> None:
		"""Test nesting Grab operations for complex transformations."""
		nodeFunctionDef = Make.FunctionDef(
			name="functionProcessor",
			argumentSpecification=Make.arguments(list_arg=[Make.arg("paramAlpha"), Make.arg("paramBeta")]),
			body=[Make.Pass()]
		)

		# Modify function name
		actionModifyName = Grab.nameAttribute(lambda identifierOld: "processed_" + identifierOld)
		nodeModified = actionModifyName(nodeFunctionDef)

		assert nodeModified.name == "processed_functionProcessor", "Function name should be modified"

		# Modify first argument name through nested structure
		# We need to access args.args[0] and modify its arg attribute
		nodeModified.args.args[0] = Grab.argAttribute(lambda identifierOld: identifierOld.upper())(nodeModified.args.args[0])
		assert nodeModified.args.args[0].arg == "PARAMALPHA", "First argument should be uppercase"

	def testGrabWithListComprehensions(self) -> None:
		"""Test Grab with list comprehensions for batch transformations."""
		listNodesFunctions = [
			Make.FunctionDef(name="functionAlpha", body=[Make.Pass()]),
			Make.FunctionDef(name="functionBeta", body=[Make.Pass()]),
			Make.FunctionDef(name="functionGamma", body=[Make.Pass()]),
		]

		# Modify all function names
		actionModifyName = Grab.nameAttribute(lambda identifierOld: identifierOld + "_modified")
		listModified = [actionModifyName(node) for node in listNodesFunctions]

		listExpectedNames = ["functionAlpha_modified", "functionBeta_modified", "functionGamma_modified"]
		listActualNames = [node.name for node in listModified]
		assert listActualNames == listExpectedNames, "All function names should be modified"

	def testGrabPreservingNodeIdentityInComplexTree(self) -> None:
		"""Test that Grab preserves node identity in complex AST trees."""
		nodeModule = Make.Module(body=[
			Make.FunctionDef(name="functionAlpha", body=[
				Make.Assign(
					targets=[Make.Name("variableBeta", context=Make.Store())],
					value=Make.Constant(233)  # Fibonacci number
				)
			])
		])

		# Modify function name
		nodeFunction = nodeModule.body[0]
		identityOriginal = id(nodeFunction)

		actionModifyName = Grab.nameAttribute(lambda identifierOld: identifierOld + "_new")
		nodeModified = actionModifyName(nodeFunction)

		identityModified = id(nodeModified)
		assert identityOriginal == identityModified, "Node identity should be preserved"
		assert nodeModule.body[0] is nodeModified, "Parent reference should remain valid"

	@pytest.mark.parametrize("indexTarget,actionType,expectedLength", [
		(0, "delete", 2),
		(1, "delete", 2),
		(2, "delete", 2),
		(0, "expand", 5),  # Fibonacci number
		(1, "expand", 5),  # Fibonacci number
	])
	def testIndexWithParametrizedOperations(self, indexTarget: int, actionType: str, expectedLength: int) -> None:
		"""Test index method with parametrized operations using Fibonacci numbers."""
		listOriginal = [Make.Name("alpha"), Make.Name("beta"), Make.Name("gamma")]

		if actionType == "delete":
			actionGrab = Grab.index(indexTarget, lambda node: None)
		elif actionType == "expand":
			actionGrab = Grab.index(indexTarget, lambda node: [Make.Name("exp1"), Make.Name("exp2"), Make.Name("exp3")])
		else:
			raise ValueError(f"Unknown action type: {actionType}")

		listModified = actionGrab(listOriginal)
		assert len(listModified) == expectedLength, f"List should have {expectedLength} elements after {actionType} at index {indexTarget}"

class TestGrabEdgeCases:
	"""Test suite for edge cases in Grab usage."""

	def testAttributeModificationWithNoneValue(self) -> None:
		"""Test attribute modification when value is None."""
		nodeImportFrom = Make.ImportFrom(None, [Make.alias("itemAlpha")])

		actionModifyModule = Grab.moduleAttribute(lambda valueOld: "newModule" if valueOld is None else valueOld + "_modified")
		nodeModified = actionModifyModule(nodeImportFrom)

		assert nodeModified.module == "newModule", "None value should be handled correctly"

	def testAttributeModificationWithEmptyList(self) -> None:
		"""Test attribute modification with empty list."""
		nodeClassDef = Make.ClassDef(name="ClassAlpha", bases=[])

		actionModifyBases = Grab.basesAttribute(lambda listBases: listBases + [Make.Name("BaseClass")])
		nodeModified = actionModifyBases(nodeClassDef)

		assert len(nodeModified.bases) == 1, "Empty list should be modified correctly"
		assert nodeModified.bases[0].id == "BaseClass", "Base class should be added"

	def testIndexWithNegativeIndices(self) -> None:
		"""Test index method with negative indices."""
		listOriginal = [Make.Name("alpha"), Make.Name("beta"), Make.Name("gamma")]

		actionModifyLast = Grab.index(-1, lambda node: Make.Name(node.id.upper()))
		listModified = actionModifyLast(listOriginal)

		assert listModified[-1].id == "GAMMA", "Last element should be modified"
		assert listModified[0].id == "alpha", "First element should be unchanged"

	def testChainedIndexOperations(self) -> None:
		"""Test chained index operations."""
		listOriginal = [Make.Name("alpha"), Make.Name("beta"), Make.Name("gamma"), Make.Name("delta")]

		# Apply multiple index operations
		actionModify0 = Grab.index(0, lambda node: Make.Name(node.id.upper()))
		actionModify2 = Grab.index(2, lambda node: Make.Name(node.id.upper()))

		listAfterFirst = actionModify0(listOriginal)
		listAfterSecond = actionModify2(listAfterFirst)

		assert listAfterSecond[0].id == "ALPHA", "First element should be modified"
		assert listAfterSecond[1].id == "beta", "Second element should be unchanged"
		assert listAfterSecond[2].id == "GAMMA", "Third element should be modified"
		assert listAfterSecond[3].id == "delta", "Fourth element should be unchanged"
