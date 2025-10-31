"""Comprehensive tests for the containers module."""
# pyright: standard
from astToolkit import Make
from astToolkit.containers import (
	IngredientsFunction,
	IngredientsModule,
	LedgerOfImports,
	astModuleToIngredientsFunction,
)
from collections.abc import Callable
from pathlib import Path
from typing import Any
import ast
import pytest
import tempfile


class TestLedgerOfImports:
	"""Test suite for LedgerOfImports class."""

	@pytest.mark.parametrize("startWithParameter,expectedListModules,expectedCountTypeIgnores", [
		(None, [], 0),  # Initialize with None
		(Make.Module([Make.Import('ast'), Make.ImportFrom('collections', [Make.alias('defaultdict')])]), ['ast', 'collections'], 0),  # Initialize with module
	])
	def testInitialization(self, startWithParameter: ast.AST | None, expectedListModules: list[str], expectedCountTypeIgnores: int) -> None:
		"""Test LedgerOfImports initialization with various inputs."""
		ledgerImports = LedgerOfImports(startWith=startWithParameter)
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		
		for identifierModule in expectedListModules:
			assert identifierModule in listModuleIdentifiers
		assert len(ledgerImports.type_ignores) == expectedCountTypeIgnores

	@pytest.mark.parametrize("identifierModuleTest,expectedPredicateResult", [
		("ast", True),
		("collections", True),
		("os", False),
		("sys", False),
	])
	def testAddImportAsStrAddsDirectImport(self, identifierModuleTest: str, expectedPredicateResult: bool) -> None:
		"""Test addImport_asStr adds direct imports correctly."""
		ledgerImports = LedgerOfImports()
		ledgerImports.addImport_asStr('ast')
		ledgerImports.addImport_asStr('collections')
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		assert (identifierModuleTest in listModuleIdentifiers) is expectedPredicateResult

	@pytest.mark.parametrize("identifierModuleTest,nameIdentifierTest,expectedPredicateResult", [
		("collections", "defaultdict", True),
		("typing", "Any", True),
		("collections", "Counter", False),
		("os", "path", False),
	])
	def testAddImportFromAsStrAddsFromImports(self, identifierModuleTest: str, nameIdentifierTest: str, expectedPredicateResult: bool) -> None:
		"""Test addImportFrom_asStr adds from-imports correctly using semantic identifiers."""
		ledgerImports = LedgerOfImports()
		ledgerImports.addImportFrom_asStr('collections', 'defaultdict')
		ledgerImports.addImportFrom_asStr('typing', 'Any')
		listAstImports = ledgerImports.makeList_ast()

		# Check if the module and name combination exists
		predicateFoundCombination = False
		for astImportStatement in listAstImports:
			if isinstance(astImportStatement, ast.ImportFrom):
				if astImportStatement.module == identifierModuleTest:
					for aliasNode in astImportStatement.names:
						if aliasNode.name == nameIdentifierTest:
							predicateFoundCombination = True
							break
		assert predicateFoundCombination is expectedPredicateResult

	@pytest.mark.parametrize("identifierModule,nameIdentifier,asNameIdentifier,expectedPredicateFound", [
		("collections", "defaultdict", "dd", True),
		("typing", "Any", "TypeAny", True),
		("os", "path", "osPath", True),
	])
	def testAddImportFromAsStrWithAlias(self, identifierModule: str, nameIdentifier: str, asNameIdentifier: str, expectedPredicateFound: bool) -> None:
		"""Test addImportFrom_asStr with alias parameter."""
		ledgerImports = LedgerOfImports()
		ledgerImports.addImportFrom_asStr(identifierModule, nameIdentifier, asName=asNameIdentifier)
		listAstImports = ledgerImports.makeList_ast()

		predicateFoundAlias = False
		for astImportStatement in listAstImports:
			if isinstance(astImportStatement, ast.ImportFrom):
				if astImportStatement.module == identifierModule:
					for aliasNode in astImportStatement.names:
						if aliasNode.name == nameIdentifier and aliasNode.asname == asNameIdentifier:
							predicateFoundAlias = True
		assert predicateFoundAlias is expectedPredicateFound

	@pytest.mark.parametrize("identifierModule,expectedPredicateInList", [
		("pathlib", True),
		("ast", True),
		("sys", True),
	])
	def testAddAstWithImportNode(self, identifierModule: str, expectedPredicateInList: bool) -> None:
		"""Test addAst with Import AST node."""
		ledgerImports = LedgerOfImports()
		astImportNode = Make.Import(identifierModule)
		ledgerImports.addAst(astImportNode)
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		assert (identifierModule in listModuleIdentifiers) is expectedPredicateInList

	@pytest.mark.parametrize("identifierModule,nameAlias,expectedPredicateInList", [
		("os", "path", True),
		("collections", "defaultdict", True),
		("typing", "Any", True),
	])
	def testAddAstWithImportFromNode(self, identifierModule: str, nameAlias: str, expectedPredicateInList: bool) -> None:
		"""Test addAst with ImportFrom AST node."""
		ledgerImports = LedgerOfImports()
		astImportFromNode = Make.ImportFrom(identifierModule, [Make.alias(nameAlias)])
		ledgerImports.addAst(astImportFromNode)
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		assert (identifierModule in listModuleIdentifiers) is expectedPredicateInList

	@pytest.mark.parametrize("nodeInvalid,expectedExceptionMatch", [
		(Make.Assign(targets=[Make.Name('variableAlpha', context=Make.Store())], value=Make.Constant(233)), "I can only accept"),
		(Make.Pass(), "I can only accept"),
	])
	def testAddAstWithInvalidNode(self, nodeInvalid: ast.AST, expectedExceptionMatch: str) -> None:
		"""Test addAst raises ValueError with invalid node type."""
		ledgerImports = LedgerOfImports()
		with pytest.raises(ValueError, match=expectedExceptionMatch):
			ledgerImports.addAst(nodeInvalid)  # pyright: ignore[reportArgumentType]

	@pytest.mark.parametrize("listOperations,expectedCountUnique", [
		([("addImport_asStr", "ast"), ("addImport_asStr", "ast")], 1),  # Duplicate direct import
		([("addImportFrom_asStr", "collections", "defaultdict"), ("addImportFrom_asStr", "collections", "Counter")], 1),  # Same module
		([("addImport_asStr", "ast"), ("addImportFrom_asStr", "collections", "defaultdict")], 2),  # Different types
	])
	def testExportListModuleIdentifiersReturnsUniqueValues(self, listOperations: list[tuple[str, ...]], expectedCountUnique: int) -> None:
		"""Test exportListModuleIdentifiers returns unique, sorted module names."""
		ledgerImports = LedgerOfImports()
		
		for operation in listOperations:
			methodName = operation[0]
			if methodName == "addImport_asStr":
				ledgerImports.addImport_asStr(operation[1])  # type: ignore
			elif methodName == "addImportFrom_asStr":
				ledgerImports.addImportFrom_asStr(operation[1], operation[2])  # type: ignore
		
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		# Should be sorted and unique
		assert listModuleIdentifiers == sorted(set(listModuleIdentifiers))
		assert len(set(listModuleIdentifiers)) == expectedCountUnique

	@pytest.mark.parametrize("listOperations,expectedCountImportStatements,expectedCountImportFromStatements", [
		([("addImport_asStr", "ast"), ("addImportFrom_asStr", "typing", "Any")], 1, 1),
		([("addImport_asStr", "ast"), ("addImport_asStr", "sys")], 2, 0),
		([("addImportFrom_asStr", "typing", "Any"), ("addImportFrom_asStr", "collections", "defaultdict")], 0, 2),
	])
	def testMakeListAstGeneratesImportStatements(self, listOperations: list[tuple[str, ...]], expectedCountImportStatements: int, expectedCountImportFromStatements: int) -> None:
		"""Test makeList_ast generates correct import statement nodes."""
		ledgerImports = LedgerOfImports()
		
		for operation in listOperations:
			methodName = operation[0]
			if methodName == "addImport_asStr":
				ledgerImports.addImport_asStr(operation[1])  # type: ignore
			elif methodName == "addImportFrom_asStr":
				ledgerImports.addImportFrom_asStr(operation[1], operation[2])  # type: ignore
		
		listAstImports = ledgerImports.makeList_ast()
		countImport = sum(1 for astImport in listAstImports if isinstance(astImport, ast.Import))
		countImportFrom = sum(1 for astImport in listAstImports if isinstance(astImport, ast.ImportFrom))
		
		assert countImport == expectedCountImportStatements
		assert countImportFrom == expectedCountImportFromStatements

	@pytest.mark.parametrize("listOperations,expectedCountImportFrom,expectedCountNames", [
		([("addImportFrom_asStr", "collections", "defaultdict"), ("addImportFrom_asStr", "collections", "defaultdict"), ("addImportFrom_asStr", "collections", "Counter")], 1, 2),
		([("addImportFrom_asStr", "typing", "Any"), ("addImportFrom_asStr", "typing", "Any")], 1, 1),
	])
	def testMakeListAstDeduplicatesImports(self, listOperations: list[tuple[str, ...]], expectedCountImportFrom: int, expectedCountNames: int) -> None:
		"""Test makeList_ast deduplicates repeated import requests."""
		ledgerImports = LedgerOfImports()
		
		for operation in listOperations:
			ledgerImports.addImportFrom_asStr(operation[1], operation[2])  # type: ignore
		
		listAstImports = ledgerImports.makeList_ast()
		countImportFrom = sum(1 for astImport in listAstImports if isinstance(astImport, ast.ImportFrom))
		assert countImportFrom == expectedCountImportFrom
		
		importFromNode = next(astImport for astImport in listAstImports if isinstance(astImport, ast.ImportFrom))
		assert len(importFromNode.names) == expectedCountNames

	@pytest.mark.parametrize("identifierModule,listNamesToAdd,expectedPredicateModuleNotInList", [
		("collections", ["defaultdict", "Counter"], True),
		("typing", ["Any", "Dict"], True),
		("os", ["path"], True),
	])
	def testRemoveImportFromModule(self, identifierModule: str, listNamesToAdd: list[str], expectedPredicateModuleNotInList: bool) -> None:
		"""Test removeImportFromModule removes all imports from a module."""
		ledgerImports = LedgerOfImports()
		for nameToAdd in listNamesToAdd:
			ledgerImports.addImportFrom_asStr(identifierModule, nameToAdd)
		ledgerImports.removeImportFromModule(identifierModule)
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		assert (identifierModule not in listModuleIdentifiers) is expectedPredicateModuleNotInList

	@pytest.mark.parametrize("identifierModule,listNamesToAdd,nameToRemove,asNameToRemove,listNamesExpectedRemaining", [
		("typing", ["Any", "Dict"], "Any", None, ["Dict"]),
		("typing", ["Any", "Dict", "List"], "Dict", None, ["Any", "List"]),
		("collections", ["defaultdict", "Counter"], "defaultdict", None, ["Counter"]),
	])
	def testRemoveImportFromWithSpecificItem(self, identifierModule: str, listNamesToAdd: list[str], nameToRemove: str, asNameToRemove: str | None, listNamesExpectedRemaining: list[str]) -> None:
		"""Test removeImportFrom removes specific item from from-imports."""
		ledgerImports = LedgerOfImports()
		for nameToAdd in listNamesToAdd:
			ledgerImports.addImportFrom_asStr(identifierModule, nameToAdd)
		
		ledgerImports.removeImportFrom(identifierModule, nameToRemove, asNameToRemove)
		
		# Check remaining names
		listAstImports = ledgerImports.makeList_ast()
		listNamesFound: list[str] = []
		for astImportStatement in listAstImports:
			if isinstance(astImportStatement, ast.ImportFrom) and astImportStatement.module == identifierModule:
				listNamesFound = [aliasNode.name for aliasNode in astImportStatement.names]
		
		for nameExpected in listNamesExpectedRemaining:
			assert nameExpected in listNamesFound
		assert nameToRemove not in listNamesFound

	@pytest.mark.parametrize("identifierModule,listNamesToAdd,nameToRemove,asNameToRemove,listNamesExpectedRemaining", [
		("collections", [("defaultdict", "dd"), ("Counter", None)], "defaultdict", "dd", ["Counter"]),
		("typing", [("Any", "TypeAny"), ("Dict", None)], "Any", "TypeAny", ["Dict"]),
	])
	def testRemoveImportFromWithAlias(self, identifierModule: str, listNamesToAdd: list[tuple[str, str | None]], nameToRemove: str, asNameToRemove: str, listNamesExpectedRemaining: list[str]) -> None:
		"""Test removeImportFrom removes item with alias."""
		ledgerImports = LedgerOfImports()
		for nameToAdd, asNameToAdd in listNamesToAdd:
			ledgerImports.addImportFrom_asStr(identifierModule, nameToAdd, asName=asNameToAdd)
		
		ledgerImports.removeImportFrom(identifierModule, nameToRemove, asNameToRemove)
		
		# Check remaining names
		listAstImports = ledgerImports.makeList_ast()
		listNamesFound: list[str] = []
		for astImportStatement in listAstImports:
			if isinstance(astImportStatement, ast.ImportFrom) and astImportStatement.module == identifierModule:
				listNamesFound = [aliasNode.name for aliasNode in astImportStatement.names]
		
		for nameExpected in listNamesExpectedRemaining:
			assert nameExpected in listNamesFound
		assert nameToRemove not in listNamesFound

	@pytest.mark.parametrize("listLedgerOperations,expectedListModules", [
		([([("addImport_asStr", "ast")], [("addImport_asStr", "collections")])], ["ast", "collections"]),
		([([("addImportFrom_asStr", "typing", "Any")], [("addImportFrom_asStr", "typing", "Dict")])], ["typing"]),
		([([("addImport_asStr", "ast"), ("addImportFrom_asStr", "typing", "Any")], [("addImport_asStr", "collections")])], ["ast", "collections", "typing"]),
	])
	def testUpdateMergesMultipleLedgers(self, listLedgerOperations: list[list[list[tuple[str, ...]]]], expectedListModules: list[str]) -> None:
		"""Test update merges imports from multiple ledgers."""
		listLedgers: list[LedgerOfImports] = []
		
		for ledgerOperations in listLedgerOperations[0]:
			ledger = LedgerOfImports()
			for operation in ledgerOperations:
				methodName = operation[0]
				if methodName == "addImport_asStr":
					ledger.addImport_asStr(operation[1])  # type: ignore
				elif methodName == "addImportFrom_asStr":
					ledger.addImportFrom_asStr(operation[1], operation[2])  # type: ignore
			listLedgers.append(ledger)
		
		ledgerTarget = LedgerOfImports()
		ledgerTarget.update(*listLedgers)
		
		listModuleIdentifiers = ledgerTarget.exportListModuleIdentifiers()
		for identifierModule in expectedListModules:
			assert identifierModule in listModuleIdentifiers

	@pytest.mark.parametrize("listStatementsInModule,expectedListModules", [
		([Make.Import('pathlib'), Make.ImportFrom('os', [Make.alias('path')])], ['pathlib', 'os']),
		([Make.Import('ast'), Make.Import('sys')], ['ast', 'sys']),
		([Make.ImportFrom('collections', [Make.alias('defaultdict')]), Make.ImportFrom('typing', [Make.alias('Any')])], ['collections', 'typing']),
	])
	def testWalkThisDiscoversImports(self, listStatementsInModule: list[ast.stmt], expectedListModules: list[str]) -> None:
		"""Test walkThis automatically discovers imports in AST."""
		# Add a non-import statement to ensure walkThis filters correctly
		listStatementsInModule.append(Make.Assign(
			targets=[Make.Name('variableAlpha', context=Make.Store())],
			value=Make.Constant(233)
		))
		moduleWithImports = Make.Module(listStatementsInModule)
		
		ledgerImports = LedgerOfImports()
		ledgerImports.walkThis(moduleWithImports)
		
		listModuleIdentifiers = ledgerImports.exportListModuleIdentifiers()
		for identifierModule in expectedListModules:
			assert identifierModule in listModuleIdentifiers


class TestIngredientsFunction:
	"""Test suite for IngredientsFunction dataclass."""

	@pytest.mark.parametrize("nameFunctionTest,expectedNameFunction,expectedPredicateHasImports,expectedCountTypeIgnores", [
		("functionAlpha", "functionAlpha", False, 0),
		("functionBeta", "functionBeta", False, 0),
		("functionGamma", "functionGamma", False, 0),
	])
	def testInitializationWithDefaults(self, nameFunctionTest: str, expectedNameFunction: str, expectedPredicateHasImports: bool, expectedCountTypeIgnores: int) -> None:
		"""Test IngredientsFunction initialization with default values."""
		astFunctionDefTest = Make.FunctionDef(name=nameFunctionTest, body=[Make.Pass()])
		ingredientsFunction = IngredientsFunction(astFunctionDef=astFunctionDefTest)

		assert ingredientsFunction.astFunctionDef.name == expectedNameFunction
		assert isinstance(ingredientsFunction.imports, LedgerOfImports)
		assert (len(ingredientsFunction.imports.exportListModuleIdentifiers()) > 0) is expectedPredicateHasImports
		assert len(ingredientsFunction.type_ignores) == expectedCountTypeIgnores

	@pytest.mark.parametrize("nameFunctionTest,identifierModuleToAdd,expectedPredicateModuleInList", [
		("functionDelta", "ast", True),
		("functionEpsilon", "typing", True),
		("functionZeta", "collections", True),
	])
	def testInitializationWithImports(self, nameFunctionTest: str, identifierModuleToAdd: str, expectedPredicateModuleInList: bool) -> None:
		"""Test IngredientsFunction initialization with imports."""
		astFunctionDefTest = Make.FunctionDef(name=nameFunctionTest, body=[Make.Pass()])
		ledgerImportsTest = LedgerOfImports()
		ledgerImportsTest.addImport_asStr(identifierModuleToAdd)

		ingredientsFunction = IngredientsFunction(
			astFunctionDef=astFunctionDefTest,
			imports=ledgerImportsTest
		)

		assert ingredientsFunction.astFunctionDef.name == nameFunctionTest
		assert (identifierModuleToAdd in ingredientsFunction.imports.exportListModuleIdentifiers()) is expectedPredicateModuleInList


class TestIngredientsModule:
	"""Test suite for IngredientsModule dataclass."""

	@pytest.mark.parametrize("initializationParameter,expectedCountFunctions", [
		(None, 0),
	])
	def testInitializationWithDefaults(self, initializationParameter: None, expectedCountFunctions: int) -> None:
		"""Test IngredientsModule initialization with default values."""
		ingredientsModule = IngredientsModule()

		assert isinstance(ingredientsModule.imports, LedgerOfImports)
		assert isinstance(ingredientsModule.prologue, ast.Module)
		assert isinstance(ingredientsModule.epilogue, ast.Module)
		assert isinstance(ingredientsModule.launcher, ast.Module)
		assert len(ingredientsModule.listIngredientsFunctions) == expectedCountFunctions

	@pytest.mark.parametrize("nameFunctionTest,expectedCountFunctions,expectedNameFunction", [
		("functionEta", 1, "functionEta"),
		("functionTheta", 1, "functionTheta"),
		("functionIota", 1, "functionIota"),
	])
	def testInitializationWithSingleFunction(self, nameFunctionTest: str, expectedCountFunctions: int, expectedNameFunction: str) -> None:
		"""Test IngredientsModule initialization with single function."""
		astFunctionDefTest = Make.FunctionDef(name=nameFunctionTest, body=[Make.Pass()])
		ingredientsFunctionTest = IngredientsFunction(astFunctionDef=astFunctionDefTest)

		ingredientsModule = IngredientsModule(ingredientsFunction=ingredientsFunctionTest)

		assert len(ingredientsModule.listIngredientsFunctions) == expectedCountFunctions
		assert ingredientsModule.listIngredientsFunctions[0].astFunctionDef.name == expectedNameFunction

	@pytest.mark.parametrize("listNamesFunctions,expectedCountFunctions", [
		(["functionKappa", "functionLambda"], 2),
		(["functionMu", "functionNu", "functionXi"], 3),
		(["functionOmicron"], 1),
	])
	def testInitializationWithMultipleFunctions(self, listNamesFunctions: list[str], expectedCountFunctions: int) -> None:
		"""Test IngredientsModule initialization with sequence of functions."""
		listIngredientsFunctions: list[IngredientsFunction] = []
		for nameFunction in listNamesFunctions:
			astFunctionDef = Make.FunctionDef(name=nameFunction, body=[Make.Pass()])
			listIngredientsFunctions.append(IngredientsFunction(astFunctionDef=astFunctionDef))

		ingredientsModule = IngredientsModule(ingredientsFunction=listIngredientsFunctions)

		assert len(ingredientsModule.listIngredientsFunctions) == expectedCountFunctions
		for indexFunction, nameFunction in enumerate(listNamesFunctions):
			assert ingredientsModule.listIngredientsFunctions[indexFunction].astFunctionDef.name == nameFunction

	@pytest.mark.parametrize("nameVariable,valueFibonacci", [
		("variablePi", 13),
		("variableRho", 21),
		("variableSigma", 34),
	])
	def testAppendPrologueAddsStatements(self, nameVariable: str, valueFibonacci: int) -> None:
		"""Test appendPrologue adds statements to prologue section."""
		ingredientsModule = IngredientsModule()
		countBefore = len(ingredientsModule.prologue.body)
		statementAssignment = Make.Assign(
			targets=[Make.Name(nameVariable, context=Make.Store())],
			value=Make.Constant(valueFibonacci)
		)
		ingredientsModule.appendPrologue(statement=statementAssignment)

		# Should have added one statement
		assert len(ingredientsModule.prologue.body) == countBefore + 1
		# The added statement should be an Assign
		predicateFoundOurStatement = False
		for statement in ingredientsModule.prologue.body:
			if isinstance(statement, ast.Assign) and hasattr(statement.targets[0], 'id') and statement.targets[0].id == nameVariable:
				predicateFoundOurStatement = True
				break
		assert predicateFoundOurStatement

	@pytest.mark.parametrize("nameFunctionToCall,argumentConstant", [
		("print", "Completed"),
		("logMessage", "Done"),
		("reportStatus", "Finished"),
	])
	def testAppendEpilogueAddsStatements(self, nameFunctionToCall: str, argumentConstant: str) -> None:
		"""Test appendEpilogue adds statements to epilogue section."""
		ingredientsModule = IngredientsModule()
		countBefore = len(ingredientsModule.epilogue.body)
		statementExpression = Make.Expr(Make.Call(Make.Name(nameFunctionToCall), [Make.Constant(argumentConstant)]))
		ingredientsModule.appendEpilogue(statement=statementExpression)

		# Should have added one statement
		assert len(ingredientsModule.epilogue.body) == countBefore + 1
		# The added statement should be an Expr with our specific call
		predicateFoundOurStatement = False
		for statement in ingredientsModule.epilogue.body:
			if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
				if hasattr(statement.value.func, 'id') and statement.value.func.id == nameFunctionToCall:
					predicateFoundOurStatement = True
					break
		assert predicateFoundOurStatement

	@pytest.mark.parametrize("nameFunctionToCall", [
		("main"),
		("runApplication"),
		("startProgram"),
	])
	def testAppendLauncherAddsStatements(self, nameFunctionToCall: str) -> None:
		"""Test appendLauncher adds statements to launcher section."""
		ingredientsModule = IngredientsModule()
		countBefore = len(ingredientsModule.launcher.body)
		statementExpression = Make.Expr(Make.Call(Make.Name(nameFunctionToCall), []))
		ingredientsModule.appendLauncher(statement=statementExpression)

		# Should have added one statement
		assert len(ingredientsModule.launcher.body) == countBefore + 1
		# The added statement should be an Expr with our specific call
		predicateFoundOurStatement = False
		for statement in ingredientsModule.launcher.body:
			if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
				if hasattr(statement.value.func, 'id') and statement.value.func.id == nameFunctionToCall:
					predicateFoundOurStatement = True
					break
		assert predicateFoundOurStatement

	@pytest.mark.parametrize("nameFunctionTest,expectedCountFunctions", [
		("functionTau", 1),
		("functionUpsilon", 1),
		("functionPhi", 1),
	])
	def testAppendIngredientsFunctionAddsFunction(self, nameFunctionTest: str, expectedCountFunctions: int) -> None:
		"""Test appendIngredientsFunction adds function to list."""
		ingredientsModule = IngredientsModule()
		astFunctionDefTest = Make.FunctionDef(name=nameFunctionTest, body=[Make.Pass()])
		ingredientsFunctionTest = IngredientsFunction(astFunctionDef=astFunctionDefTest)

		ingredientsModule.appendIngredientsFunction(ingredientsFunctionTest)

		assert len(ingredientsModule.listIngredientsFunctions) == expectedCountFunctions
		assert ingredientsModule.listIngredientsFunctions[0].astFunctionDef.name == nameFunctionTest

	@pytest.mark.parametrize("listNamesFunctions,expectedCountFunctions", [
		(["functionChi", "functionPsi"], 2),
		(["functionOmega", "functionAlpha", "functionBeta"], 3),
	])
	def testAppendIngredientsFunctionAddsMultipleFunctions(self, listNamesFunctions: list[str], expectedCountFunctions: int) -> None:
		"""Test appendIngredientsFunction adds multiple functions at once."""
		ingredientsModule = IngredientsModule()

		listIngredientsFunctions: list[IngredientsFunction] = []
		for nameFunction in listNamesFunctions:
			astFunctionDef = Make.FunctionDef(name=nameFunction, body=[Make.Pass()])
			listIngredientsFunctions.append(IngredientsFunction(astFunctionDef=astFunctionDef))

		ingredientsModule.appendIngredientsFunction(*listIngredientsFunctions)

		assert len(ingredientsModule.listIngredientsFunctions) == expectedCountFunctions

	@pytest.mark.parametrize("identifierModule,listNamesModuleLevel,listNamesFunctionLevel,expectedPredicateModuleNotInModuleLedger,expectedPredicateModuleNotInFunctionLedger", [
		("typing", ["Any"], ["Dict"], True, True),
		("collections", ["defaultdict"], ["Counter"], True, True),
		("os", ["path"], ["getcwd"], True, True),
	])
	def testRemoveImportFromModuleAcrossAllFunctions(self, identifierModule: str, listNamesModuleLevel: list[str], listNamesFunctionLevel: list[str], expectedPredicateModuleNotInModuleLedger: bool, expectedPredicateModuleNotInFunctionLedger: bool) -> None:
		"""Test removeImportFromModule removes from-imports from module and all functions."""
		ingredientsModule = IngredientsModule()

		# Add module-level from-imports
		for nameToAdd in listNamesModuleLevel:
			ingredientsModule.imports.addImportFrom_asStr(identifierModule, nameToAdd)

		# Add function with from-imports
		astFunctionDefTest = Make.FunctionDef(name='functionTest', body=[Make.Pass()])
		ingredientsFunctionTest = IngredientsFunction(astFunctionDef=astFunctionDefTest)
		for nameToAdd in listNamesFunctionLevel:
			ingredientsFunctionTest.imports.addImportFrom_asStr(identifierModule, nameToAdd)
		ingredientsModule.appendIngredientsFunction(ingredientsFunctionTest)

		# Remove from everywhere
		ingredientsModule.removeImportFromModule(identifierModule)

		# Verify removal
		assert (identifierModule not in ingredientsModule.imports.exportListModuleIdentifiers()) is expectedPredicateModuleNotInModuleLedger
		assert (identifierModule not in ingredientsModule.listIngredientsFunctions[0].imports.exportListModuleIdentifiers()) is expectedPredicateModuleNotInFunctionLedger

	@pytest.mark.parametrize("identifierModule,namePrologueVariable,valuePrologue,nameFunction,nameFunctionEpilogue,nameFunctionLauncher", [
		("collections", "variableStart", 55, "functionProcess", "epilogueMarker", "launcherMarker"),
		("ast", "variableInit", 89, "functionExecute", "finalize", "launch"),
	])
	def testBodyPropertyAssemblesComponentsInCorrectOrder(self, identifierModule: str, namePrologueVariable: str, valuePrologue: int, nameFunction: str, nameFunctionEpilogue: str, nameFunctionLauncher: str) -> None:
		"""Test body property assembles all components in correct order."""
		ingredientsModule = IngredientsModule()

		# Add import
		ingredientsModule.imports.addImport_asStr(identifierModule)

		# Add prologue
		statementPrologueUnique = Make.Assign(
			targets=[Make.Name(namePrologueVariable, context=Make.Store())],
			value=Make.Constant(valuePrologue)
		)
		ingredientsModule.appendPrologue(statement=statementPrologueUnique)

		# Add function
		astFunctionDefTest = Make.FunctionDef(name=nameFunction, body=[Make.Pass()])
		ingredientsModule.appendIngredientsFunction(IngredientsFunction(astFunctionDef=astFunctionDefTest))

		# Add epilogue
		statementEpilogueUnique = Make.Expr(Make.Call(Make.Name(nameFunctionEpilogue), []))
		ingredientsModule.appendEpilogue(statement=statementEpilogueUnique)

		# Add launcher
		statementLauncherUnique = Make.Expr(Make.Call(Make.Name(nameFunctionLauncher), []))
		ingredientsModule.appendLauncher(statement=statementLauncherUnique)

		listBodyStatements = ingredientsModule.body

		# Find indices of our specific statements
		indexPrologue = -1
		indexFunction = -1
		indexEpilogue = -1
		indexLauncher = -1

		for indexStatement, statement in enumerate(listBodyStatements):
			if isinstance(statement, ast.Assign) and hasattr(statement.targets[0], 'id') and statement.targets[0].id == namePrologueVariable:
				indexPrologue = indexStatement
			elif isinstance(statement, ast.FunctionDef) and statement.name == nameFunction:
				indexFunction = indexStatement
			elif isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
				if hasattr(statement.value.func, 'id'):
					if statement.value.func.id == nameFunctionEpilogue:
						indexEpilogue = indexStatement
					elif statement.value.func.id == nameFunctionLauncher:
						indexLauncher = indexStatement

		# Verify correct ordering: prologue < function < epilogue < launcher
		assert indexPrologue < indexFunction, "Prologue should come before function"
		assert indexFunction < indexEpilogue, "Function should come before epilogue"
		assert indexEpilogue < indexLauncher, "Epilogue should come before launcher"

		# Also verify imports come first
		assert isinstance(listBodyStatements[0], (ast.Import, ast.ImportFrom)), "Imports should come first"

	@pytest.mark.parametrize("lineNumberFirst,textIgnoreFirst,lineNumberSecond,textIgnoreSecond,expectedMinimumCount", [
		(5, "type: ignore", 13, "type: ignore[arg-type]", 2),
		(8, "type: ignore", 21, "type: ignore[return]", 2),
	])
	def testTypeIgnoresPropertyConsolidatesAllTypeIgnores(self, lineNumberFirst: int, textIgnoreFirst: str, lineNumberSecond: int, textIgnoreSecond: str, expectedMinimumCount: int) -> None:
		"""Test type_ignores property consolidates type ignores from all components."""
		ingredientsModule = IngredientsModule()

		# Add type ignores to various components
		typeIgnoreFirst = ast.TypeIgnore(lineNumberFirst, textIgnoreFirst)
		typeIgnoreSecond = ast.TypeIgnore(lineNumberSecond, textIgnoreSecond)

		ingredientsModule.imports.type_ignores.append(typeIgnoreFirst)
		ingredientsModule.prologue.type_ignores.append(typeIgnoreSecond)

		listTypeIgnores = ingredientsModule.type_ignores

		# Should have both type ignores
		assert len(listTypeIgnores) >= expectedMinimumCount
		assert typeIgnoreFirst in listTypeIgnores
		assert typeIgnoreSecond in listTypeIgnores

	@pytest.mark.parametrize("nameFunction,nameParameter,valueReturn,expectedTextImport,expectedTextFunction", [
		("functionSigma", "parameterValue", 233, "from typing import Any", "def functionSigma"),
		("functionTau", "inputData", 377, "from typing import Any", "def functionTau"),
	])
	def testWriteAstModuleCreatesFile(self, nameFunction: str, nameParameter: str, valueReturn: int, expectedTextImport: str, expectedTextFunction: str) -> None:
		"""Test write_astModule creates a valid Python file using extracted function."""
		# Use a real module with a function that actually uses the import
		moduleSource = f"""
from typing import Any

def {nameFunction}({nameParameter}: Any) -> int:
	return {valueReturn}
"""
		moduleAST = ast.parse(moduleSource)

		# Extract the function
		ingredientsFunctionTest = astModuleToIngredientsFunction(moduleAST, nameFunction)

		# Create module and add the function
		ingredientsModule = IngredientsModule()
		ingredientsModule.appendIngredientsFunction(ingredientsFunctionTest)

		# Write to temp file
		with tempfile.TemporaryDirectory() as pathDirectoryTemporary:
			pathFilenameOutput = Path(pathDirectoryTemporary) / 'moduleGenerated.py'
			ingredientsModule.write_astModule(pathFilenameOutput)

			# Verify file exists and is valid Python
			assert pathFilenameOutput.exists()

			# Read and parse the generated file
			textContent = pathFilenameOutput.read_text()
			assert expectedTextImport in textContent
			assert expectedTextFunction in textContent

			# Verify it's valid Python by parsing it
			ast.parse(textContent)


class TestAstModuleToIngredientsFunction:
	"""Test suite for astModuleToIngredientsFunction helper function."""

	@pytest.mark.parametrize("nameFunction,identifierModuleToImport,valueReturn,expectedNameFunction,expectedPredicateModuleInList", [
		("functionUpsilon", "ast", 89, "functionUpsilon", True),
		("functionPhi", "sys", 144, "functionPhi", True),
		("functionChi", "typing", 233, "functionChi", True),
	])
	def testExtractsNamedFunction(self, nameFunction: str, identifierModuleToImport: str, valueReturn: int, expectedNameFunction: str, expectedPredicateModuleInList: bool) -> None:
		"""Test astModuleToIngredientsFunction extracts named function correctly."""
		# Create a module with a function
		moduleWithFunction = Make.Module([
			Make.Import(identifierModuleToImport),
			Make.FunctionDef(
				name=nameFunction,
				body=[Make.Return(Make.Constant(valueReturn))]
			)
		])

		ingredientsFunction = astModuleToIngredientsFunction(moduleWithFunction, nameFunction)

		assert ingredientsFunction.astFunctionDef.name == expectedNameFunction
		assert (identifierModuleToImport in ingredientsFunction.imports.exportListModuleIdentifiers()) is expectedPredicateModuleInList

	@pytest.mark.parametrize("nameFunctionToFind,expectedExceptionType", [
		("functionNonexistent", Exception),
		("functionMissing", Exception),
	])
	def testRaisesWhenFunctionNotFound(self, nameFunctionToFind: str, expectedExceptionType: type[Exception]) -> None:
		"""Test astModuleToIngredientsFunction raises when function doesn't exist."""
		moduleEmpty = Make.Module([])

		with pytest.raises(expectedExceptionType):
			astModuleToIngredientsFunction(moduleEmpty, nameFunctionToFind)

	@pytest.mark.parametrize("nameFunction,listModulesToImport,expectedListModulesInLedger", [
		("functionPsi", ["ast", "sys"], ["ast", "sys"]),
		("functionOmega", ["typing", "collections", "os"], ["typing", "collections", "os"]),
	])
	def testCapturesAllModuleImports(self, nameFunction: str, listModulesToImport: list[str], expectedListModulesInLedger: list[str]) -> None:
		"""Test astModuleToIngredientsFunction captures all imports from module."""
		listStatements: list[ast.stmt] = [Make.Import(identifierModule) for identifierModule in listModulesToImport]
		listStatements.append(Make.FunctionDef(name=nameFunction, body=[Make.Pass()]))
		
		moduleWithMultipleImports = Make.Module(listStatements)

		ingredientsFunction = astModuleToIngredientsFunction(moduleWithMultipleImports, nameFunction)

		listModuleIdentifiers = ingredientsFunction.imports.exportListModuleIdentifiers()
		for identifierModule in expectedListModulesInLedger:
			assert identifierModule in listModuleIdentifiers
