"""Tests for the IfThis class predicates using parametrized tests and DRY principles."""
# pyright: standard
from astToolkit import Be, IfThis, Make
from collections.abc import Callable
from typing import Any
import ast
import pytest

class TestIfThisBasicPredicates:
	"""Test suite for basic IfThis methods."""

	@pytest.mark.parametrize("valueInputTest,expectedPredicateResult", [
		("identifierNorthward", True),
		("identifierSouthward", False),
		(None, False),
	])
	def testIsIdentifierWithStringPattern(self, valueInputTest: str | None, expectedPredicateResult: bool) -> None:
		"""Test isIdentifier with string identifier using cardinal directions."""
		predicateIdentifier: Callable[[str | None], bool] = IfThis.isIdentifier("identifierNorthward")
		assert predicateIdentifier(valueInputTest) is expectedPredicateResult

	@pytest.mark.parametrize("valueInputTest,expectedPredicateResult", [
		(None, True),
		("identifierNorthward", False),
	])
	def testIsIdentifierWithNonePattern(self, valueInputTest: str | None, expectedPredicateResult: bool) -> None:
		"""Test isIdentifier with None identifier."""
		predicateIdentifier: Callable[[str | None], bool] = IfThis.isIdentifier(None)
		assert predicateIdentifier(valueInputTest) is expectedPredicateResult

	@pytest.mark.parametrize("valueToTest,valueInNode,expectedPredicateResult", [
		(233, 233, True),  # Fibonacci number
		(233, 89, False),  # Different Fibonacci numbers
		("stringAlpha", "stringAlpha", True),
		("stringAlpha", "stringBeta", False),
		(None, None, True),
		(None, 233, False),
	])
	def testIsConstantValueWithVariousTypes(self, valueToTest: Any, valueInNode: Any, expectedPredicateResult: bool) -> None:
		"""Test isConstant_value with various values using Fibonacci numbers."""
		nodeConstant: ast.Constant = Make.Constant(valueInNode)
		predicateConstantValue: Callable[[ast.AST], bool] = IfThis.isConstant_value(valueToTest)
		assert predicateConstantValue(nodeConstant) is expectedPredicateResult

	def testIsConstantValueWithWrongNodeType(self) -> None:
		"""Test isConstant_value with wrong node type."""
		nodeNameIncorrect: ast.Name = Make.Name("identifierTest")
		predicateConstantValue: Callable[[ast.AST], bool] = IfThis.isConstant_value(233)
		assert predicateConstantValue(nodeNameIncorrect) is False

class TestIfThisIdentifierBasedMethods:
	"""Test suite for identifier-based IfThis methods using fixtures."""

	def testIdentifierBasedMethods(self, ifThisIdentifierTestData: tuple[str, str, Callable[[str], ast.AST], bool]) -> None:
		"""Test identifier methods using parametrized data."""
		methodNameIfThis, identifierToTest, factoryNodeAST, expectedPredicateResult = ifThisIdentifierTestData

		# Get the method from IfThis
		methodIfThis = getattr(IfThis, methodNameIfThis)

		# Create the predicate
		predicateGenerated = methodIfThis(identifierToTest)

		# Create the test node
		nodeAST = factoryNodeAST(identifierToTest)

		# Test the predicate
		assert predicateGenerated(nodeAST) is expectedPredicateResult, f"{methodNameIfThis}({identifierToTest}) should return {expectedPredicateResult}"

	@pytest.mark.parametrize("methodNameIfThis,identifierToTest", [
		("isNameIdentifier", "variableNorthward"),
		("isFunctionDefIdentifier", "functionEastward"),
		("isClassDefIdentifier", "ClassNorthEast"),
		("isCallIdentifier", "callablePrimary"),
		("is_argIdentifier", "parameterFibonacci"),
		("is_keywordIdentifier", "keywordAlpha"),
	])
	def testIdentifierMethodsWithWrongNodeType(self, methodNameIfThis: str, identifierToTest: str) -> None:
		"""Test identifier methods with wrong node types using cardinal directions."""
		methodIfThis = getattr(IfThis, methodNameIfThis)
		predicateGenerated = methodIfThis(identifierToTest)
		nodeWrongType = Make.Constant(233)  # Wrong node type for all these methods (Fibonacci number)
		assert predicateGenerated(nodeWrongType) is False

class TestIfThisSimplePredicateMethods:
	"""Test suite for simple predicate IfThis methods using fixtures."""

	def testSimplePredicateMethods(self, ifThisSimplePredicateTestData: tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]) -> None:
		"""Test simple predicate methods using parametrized data."""
		methodNameIfThis, tupleArgumentsTest, factoryNodeAST, expectedPredicateResult = ifThisSimplePredicateTestData

		# Get the method from IfThis
		methodIfThis = getattr(IfThis, methodNameIfThis)

		# Create the predicate
		predicateGenerated = methodIfThis(*tupleArgumentsTest)

		# Create the test node
		nodeAST = factoryNodeAST()

		# Test the predicate
		assert predicateGenerated(nodeAST) is expectedPredicateResult, f"{methodNameIfThis}({tupleArgumentsTest}) should return {expectedPredicateResult}"

	def testDirectPredicateMethods(self, ifThisDirectPredicateTestData: tuple[str, Callable[[], ast.AST], bool]) -> None:
		"""Test direct predicate methods that take node directly."""
		methodNameIfThis, factoryNodeAST, expectedPredicateResult = ifThisDirectPredicateTestData

		# Get the method from IfThis
		methodIfThis = getattr(IfThis, methodNameIfThis)

		# Create the test node
		nodeAST = factoryNodeAST()

		# Test the method directly
		resultPredicate = methodIfThis(nodeAST)
		assert resultPredicate is expectedPredicateResult, f"{methodNameIfThis}(node) should return {expectedPredicateResult}"

class TestIfThisComplexPredicateMethods:
	"""Test suite for complex predicate IfThis methods using fixtures."""

	def testComplexPredicateMethods(self, ifThisComplexPredicateTestData: tuple[str, tuple[Any, ...], Callable[[], ast.AST], bool]) -> None:
		"""Test complex predicate methods using parametrized data."""
		methodNameIfThis, tupleArgumentsTest, factoryNodeAST, expectedPredicateResult = ifThisComplexPredicateTestData

		# Get the method from IfThis
		methodIfThis = getattr(IfThis, methodNameIfThis)

		# Create the predicate
		predicateGenerated = methodIfThis(*tupleArgumentsTest)

		# Create the test node
		nodeAST = factoryNodeAST()

		# Test the predicate
		assert predicateGenerated(nodeAST) is expectedPredicateResult, f"{methodNameIfThis}({tupleArgumentsTest}) should return {expectedPredicateResult}"

	@pytest.mark.parametrize("namespaceObjectTest,identifierAttributeTest", [
		("objectPrimary", "methodEastward"),
		("objectSecondary", "valueNorthward"),
		("classTertiary", "nameWestward"),
	])
	def testIsAttributeNamespaceIdentifierPositiveCases(self, namespaceObjectTest: str, identifierAttributeTest: str) -> None:
		"""Test isAttributeNamespaceIdentifier with matching cases using semantic identifiers."""
		nodeAttribute = Make.Attribute(Make.Name(namespaceObjectTest), identifierAttributeTest)
		predicateGenerated = IfThis.isAttributeNamespaceIdentifier(namespaceObjectTest, identifierAttributeTest)
		assert predicateGenerated(nodeAttribute) is True

	def testIsIfUnaryNotAttributeNamespaceIdentifierPositiveCase(self) -> None:
		"""Test isIfUnaryNotAttributeNamespaceIdentifier with matching case."""
		nodeIf = Make.If(
			test=Make.UnaryOp(
				op=Make.Not(),
				operand=Make.Attribute(Make.Name("objectTarget"), "flagEnabled")
			),
			body=[Make.Pass()]
		)
		predicateGenerated = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("objectTarget", "flagEnabled")
		assert predicateGenerated(nodeIf) is True

	def testIsIfUnaryNotAttributeNamespaceIdentifierNegativeCase(self) -> None:
		"""Test isIfUnaryNotAttributeNamespaceIdentifier with non-matching case."""
		nodeIf = Make.If(test=Make.Name("conditionAlternate"), body=[Make.Pass()])
		predicateGenerated = IfThis.isIfUnaryNotAttributeNamespaceIdentifier("objectTarget", "flagEnabled")
		assert predicateGenerated(nodeIf) is False

class TestIfThisLogicalCombinationMethods:
	"""Test suite for logical combination IfThis methods."""

	@pytest.mark.parametrize("listPredicatesTest,nodeASTTest,expectedPredicateResult", [
		# All predicates match
		([Be.Name, lambda nodeTarget: hasattr(nodeTarget, 'id') and nodeTarget.id == "identifierNorthward"], Make.Name("identifierNorthward"), True),
		# Some predicates don't match
		([Be.Name, lambda nodeTarget: hasattr(nodeTarget, 'id') and nodeTarget.id == "identifierSouthward"], Make.Name("identifierNorthward"), False),
		([], Make.Name("identifierNorthward"), True), # Empty predicates list - all() returns True for empty sequence
	])
	def testIsAllOfWithVariousPredicateCombinations(self, listPredicatesTest: list[Callable[..., Any]], nodeASTTest: ast.AST, expectedPredicateResult: bool) -> None:
		"""Test isAllOf with various predicate combinations using semantic identifiers."""
		predicateCombined = IfThis.isAllOf(*listPredicatesTest)
		assert predicateCombined(nodeASTTest) is expectedPredicateResult

	@pytest.mark.parametrize("listPredicatesTest,nodeASTTest,expectedPredicateResult", [
		# At least one predicate matches
		([Be.Constant, Be.Name], Make.Name("identifierNorthward"), True),
		# No predicates match
		([Be.Constant, Be.FunctionDef], Make.Name("identifierNorthward"), False),
		([], Make.Name("identifierNorthward"), False), # Empty predicates list - any() returns False for empty sequence
	])
	def testIsAnyOfWithVariousPredicateCombinations(self, listPredicatesTest: list[Callable[..., Any]], nodeASTTest: ast.AST, expectedPredicateResult: bool) -> None:
		"""Test isAnyOf with various predicate combinations using semantic identifiers."""
		predicateCombined = IfThis.isAnyOf(*listPredicatesTest)
		assert predicateCombined(nodeASTTest) is expectedPredicateResult

class TestIfThisTreeAnalysisMethods:
	"""Test suite for tree analysis IfThis methods."""

	def testMatchesNoDescendantPositiveCase(self) -> None:
		"""Test matchesNoDescendant when no descendant matches predicate."""
		nodeAssignTarget = Make.Assign(
			targets=[Make.Name("variableAlpha", context=Make.Store())],
			value=Make.Constant(233)  # Fibonacci number
		)
		def predicateNameMatching(nodeTarget: ast.AST) -> bool:
			return Be.Name(nodeTarget) and getattr(nodeTarget, 'id', None) == "variableBeta"
		predicateGenerated = IfThis.matchesNoDescendant(predicateNameMatching)
		assert predicateGenerated(nodeAssignTarget) is True

	def testMatchesNoDescendantNegativeCase(self) -> None:
		"""Test matchesNoDescendant when a descendant matches predicate."""
		nodeAssignTarget = Make.Assign(
			targets=[Make.Name("variableAlpha", context=Make.Store())],
			value=Make.Constant(233)  # Fibonacci number
		)
		def predicateNameMatching(nodeTarget: ast.AST) -> bool:
			return Be.Name(nodeTarget) and getattr(nodeTarget, 'id', None) == "variableAlpha"
		predicateGenerated = IfThis.matchesNoDescendant(predicateNameMatching)
		assert predicateGenerated(nodeAssignTarget) is False

	def testMatchesMeButNotAnyDescendantPositiveCase(self) -> None:
		"""Test matchesMeButNotAnyDescendant when node matches but descendants don't."""
		nodeAssignTarget = Make.Assign(
			targets=[Make.Name("variableAlpha", context=Make.Store())],
			value=Make.Constant(233)  # Fibonacci number
		)
		predicateAssignmentMatching = Be.Assign
		predicateGenerated = IfThis.matchesMeButNotAnyDescendant(predicateAssignmentMatching)
		assert predicateGenerated(nodeAssignTarget) is True

	def testMatchesMeButNotAnyDescendantNegativeCase(self) -> None:
		"""Test matchesMeButNotAnyDescendant when node doesn't match."""
		nodeNameTarget = Make.Name("variableAlpha")
		predicateAssignmentMatching = Be.Assign
		predicateGenerated = IfThis.matchesMeButNotAnyDescendant(predicateAssignmentMatching)
		assert predicateGenerated(nodeNameTarget) is False

	@pytest.mark.parametrize("nodeFirst,nodeSecond,expectedPredicateResult", [
		(Make.Name("variableAlpha"), Make.Name("variableAlpha"), True),
		(Make.Name("variableAlpha"), Make.Name("variableBeta"), False),
		(Make.Constant(233), Make.Constant(233), True),  # Fibonacci numbers
		(Make.Constant(233), Make.Constant(89), False),  # Different Fibonacci numbers
	])
	def testUnparseIsWithVariousNodeCombinations(self, nodeFirst: ast.AST, nodeSecond: ast.AST, expectedPredicateResult: bool) -> None:
		"""Test unparseIs with various node combinations using semantic identifiers and Fibonacci numbers."""
		predicateGenerated = IfThis.unparseIs(nodeFirst)
		assert predicateGenerated(nodeSecond) is expectedPredicateResult

class TestIfThisAdvancedUsageScenarios:
	"""Test suite for advanced IfThis usage scenarios."""

	def testNestedIdentifierPatternsWithVariousNodeTypes(self) -> None:
		"""Test isNestedNameIdentifier with various node types."""
		identifierToTest = "variableTargetAlpha"
		predicateGenerated = IfThis.isNestedNameIdentifier(identifierToTest)

		# Should match Name
		nodeName = Make.Name(identifierToTest)
		assert predicateGenerated(nodeName) is True

		# Should match Attribute with matching value
		nodeAttributeMatching = Make.Attribute(Make.Name(identifierToTest), "methodSecondary")
		assert predicateGenerated(nodeAttributeMatching) is True

		# Should not match Attribute with non-matching value
		nodeAttributeNonMatching = Make.Attribute(Make.Name("variableTargetBeta"), "methodSecondary")
		assert predicateGenerated(nodeAttributeNonMatching) is False

	def testIsAssignAndTargets0IsWithVariousTargetPredicates(self) -> None:
		"""Test isAssignAndTargets0Is with various target predicates."""
		nodeAssignTarget = Make.Assign(
			targets=[Make.Name("variableGamma", context=Make.Store())],
			value=Make.Constant(233)  # Fibonacci number
		)

		# Matching target predicate
		def predicateTargetMatching(nodeTarget: ast.AST) -> bool:
			return Be.Name(nodeTarget) and getattr(nodeTarget, 'id', None) == "variableGamma"
		predicateGenerated = IfThis.isAssignAndTargets0Is(predicateTargetMatching)
		assert predicateGenerated(nodeAssignTarget) is True

		# Non-matching target predicate
		def predicateTargetWrong(nodeTarget: ast.AST) -> bool:
			return Be.Name(nodeTarget) and getattr(nodeTarget, 'id', None) == "variableDelta"
		predicateWrong = IfThis.isAssignAndTargets0Is(predicateTargetWrong)
		assert predicateWrong(nodeAssignTarget) is False

		# Wrong node type
		nodeNameWrongType = Make.Name("variableGamma")
		assert predicateGenerated(nodeNameWrongType) is False

	def testComplexPredicateCompositionWithRealWorldScenarios(self) -> None:
		"""Test complex predicate compositions with real-world scenarios."""
		# Create a function with assignment in body
		nodeFunctionWithAssignment = Make.FunctionDef(
			name="functionProcessor",
			body=[Make.Assign(
				targets=[Make.Name("variableResult", context=Make.Store())],
				value=Make.Constant(233)  # Fibonacci number
			)]
		)

		# Complex predicate combining multiple conditions
		predicateComplexCombination = IfThis.isAllOf(
			Be.FunctionDef,
			lambda nodeTarget: getattr(nodeTarget, 'name', None) == "functionProcessor",
			lambda nodeTarget: len(getattr(nodeTarget, 'body', [])) > 0
		)
		assert predicateComplexCombination(nodeFunctionWithAssignment) is True

		# Should fail if any condition doesn't match
		functionDifferentName = Make.FunctionDef(name="functionAlternate", body=[Make.Pass()])
		assert predicateComplexCombination(functionDifferentName) is False
