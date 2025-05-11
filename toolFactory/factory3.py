from collections import defaultdict
from itertools import chain
from pathlib import PurePosixPath
from toolFactory import (
	astName_overload,
	astName_staticmethod,
	astName_typing_TypeAlias,
	fileExtension,
	getElementsBe,
	getElementsTypeAlias,
	keywordArgumentsIdentifier,
	moduleIdentifierPrefix,
	pathPackage,
	pythonVersionMinorMinimum,
	getElementsMake,
	)
from toolFactory.factory_annex import (
	FunctionDefMake_Attribute,
	FunctionDefMake_Import,
	listHandmadeTypeAlias_astTypes,
)
from toolFactory.docstrings import ClassDefDocstringBe, ClassDefDocstringMake, docstringWarning
from typing import cast, TypedDict
from Z0Z_tools import writeStringToHere
import ast
# NOTE you need these because of `eval()`
from ast import Name, Store

"""
class Name(expr):
...
	ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`

TODO protect against AttributeError (I guess) in DOT, Grab, and ClassIsAndAttribute
	add docstrings to warn of problem, including in Make

"""
def writeModule(astModule: ast.Module, moduleIdentifier: str) -> None:
	ast.fix_missing_locations(astModule)
	pythonSource: str = ast.unparse(astModule)
	if moduleIdentifier in {'ClassIsAndAttribute', 'DOT', 'Grab'}:
		pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	# if 'ClassIsAndAttribute' in moduleIdentifier:
	# 	listTypeIgnore: list[ast.TypeIgnore] = []
	# 	tag = '[reportInconsistentOverload]'
	# 	for attribute in listPylanceErrors:
	# 		lineno = 0
	# 		for splitlinesNumber, line in enumerate(pythonSource.splitlines()):
	# 			# Cycle through the overloads and definitions: effectively keeping the last one, which is the definition.
	# 			if f"def {attribute}Is" in line:
	# 				lineno = splitlinesNumber + 1
	# 		listTypeIgnore.append(ast.TypeIgnore(lineno, tag))
	# 	astModule = ast.parse(pythonSource)
	# 	astModule.type_ignores.extend(listTypeIgnore)
	# 	pythonSource = ast.unparse(astModule)
	# 	pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	# if 'Grab' in moduleIdentifier:
	# 	listTypeIgnore: list[ast.TypeIgnore] = []
	# 	tag = '[reportAttributeAccessIssue]'
	# 	for attribute in listPylanceErrors:
	# 		for splitlinesNumber, line in enumerate(pythonSource.splitlines()):
	# 			if 'node.'+attribute in line:
	# 				listTypeIgnore.append(ast.TypeIgnore(splitlinesNumber+1, tag))
	# 				break
	# 	astModule = ast.parse(pythonSource)
	# 	astModule.type_ignores.extend(listTypeIgnore)
	# 	pythonSource = ast.unparse(astModule)
	# 	pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	pathFilenameModule = PurePosixPath(pathPackage, moduleIdentifier + fileExtension)
	writeStringToHere(pythonSource, pathFilenameModule)

def makeTypeAlias():
	def Z0Z_getTypeAliasSubcategory():
		if len(dictionaryVersions) == 1:
			for versionMinor, listClassAs_astAttribute in dictionaryVersions.items():
				ast_stmt = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in listClassAs_astAttribute]), 1) # pyright: ignore[reportAttributeAccessIssue]
				if versionMinor > pythonVersionMinorMinimum:
					ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3),
										ast.Constant(versionMinor)])])
								, body=[ast_stmt])
				# This branch is the simplest case: one TypeAlias for the attribute for all Python versions
				astTypesModule.body.append(ast_stmt)
		else:
			# There is a smart way to do the following, but I don't see it right now. NOTE datacenter has the responsibility to aggregate all values <= pythonVersionMinorMinimum.
			listVersionsMinor = sorted(dictionaryVersions.keys(), reverse=False)
			if len(listVersionsMinor) > 2:
				raise NotImplementedError("Hunter's code can't handle this.")
			ast_stmtAtPythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in dictionaryVersions[min(listVersionsMinor)]]), 1) # pyright: ignore[reportAttributeAccessIssue]
			ast_stmtAbovePythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in sorted(chain(*dictionaryVersions.values()), key=str.lower)]), 1) # pyright: ignore[reportAttributeAccessIssue]

			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3),
								ast.Constant(max(listVersionsMinor))])])
						, body=[ast_stmtAbovePythonMinimum]
						, orelse=[ast_stmtAtPythonMinimum])
			astTypesModule.body.append(ast_stmt)

	astTypesModule = ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, *listHandmadeTypeAlias_astTypes
			]
		, type_ignores=[]
		)

	typeAliasData: dict[str, dict[str, dict[int, list[str]]]] = getElementsTypeAlias()

	for attribute, dictionaryAttribute in typeAliasData.items():
		hasDOTIdentifier: str = 'hasDOT' + attribute
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		hasDOTTypeAliasName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())

		if len(dictionaryAttribute) == 1:
			astNameTypeAlias = hasDOTTypeAliasName_Store
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				Z0Z_getTypeAliasSubcategory()
		else:
			# See?! Sometimes, I can see a smart way to do things. This defaultdict builds a dictionary to mimic the
			# process I'm already using to build the TypeAlias.
			attributeDictionaryVersions: dict[int, list[str]] = defaultdict(list)
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				astNameTypeAlias: ast.Name = ast.Name(hasDOTIdentifier + '_' + TypeAliasSubcategory, ast.Store())
				if any(dictionaryVersions.keys()) <= pythonVersionMinorMinimum:
					attributeDictionaryVersions[min(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
				else:
					attributeDictionaryVersions[min(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
					attributeDictionaryVersions[max(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
				Z0Z_getTypeAliasSubcategory()
			astNameTypeAlias = hasDOTTypeAliasName_Store
			dictionaryVersions: dict[int, list[str]] = attributeDictionaryVersions
			Z0Z_getTypeAliasSubcategory()

	writeModule(astTypesModule, '_astTypes')

def makeToolBe():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringBe]

	listDictionaryToolElements = getElementsBe()

	for dictionaryToolElements in listDictionaryToolElements:
		ClassDefIdentifier = cast(str, dictionaryToolElements['ClassDefIdentifier'])
		classAs_astAttribute = cast(ast.Attribute, eval(dictionaryToolElements['classAs_astAttribute']))
		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']

		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name('ast.AST'))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.Return(value=ast.Call(func=ast.Name('isinstance'), args=[ast.Name('node'), classAs_astAttribute], keywords=[]))]
			, decorator_list=[astName_staticmethod]
			, returns=ast.Subscript(value=ast.Name('TypeGuard'), slice=classAs_astAttribute))

		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info'),
				ops=[ast.GtE()],
				comparators=[ast.Tuple([ast.Constant(3),
							ast.Constant(classVersionMinorMinimum)])]),
				body=[ast_stmt])

		list4ClassDefBody.append(ast_stmt)

	ClassDefBe = ast.ClassDef(name='Be', bases=[], keywords=[], body=list4ClassDefBody, decorator_list=[])

	ClassDef = ClassDefBe
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

def makeToolDOT():
	pass

def makeToolMake():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringMake]

	listDictionaryToolElements = getElementsMake()

	for dictionaryToolElements in listDictionaryToolElements:
		ClassDefIdentifier = cast(str, dictionaryToolElements['ClassDefIdentifier'])
		classAs_astAttribute = cast(ast.Attribute, eval(dictionaryToolElements['classAs_astAttribute']))
		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']

		list4FunctionDef_args_args: list[ast.arg] = []

		keywordArguments_ast_arg=None
		keywordArguments_ast_keyword = None
		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=list4FunctionDef_args_args, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=keywordArguments_ast_arg, defaults=[])
			, body=[ast.Return(value=ast.Call(classAs_astAttribute, args=[], keywords=[keywordArguments_ast_keyword] if keywordArguments_ast_keyword else []))]
			, decorator_list=[astName_staticmethod]
			, returns=classAs_astAttribute)

		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info'),
				ops=[ast.GtE()],
				comparators=[ast.Tuple([ast.Constant(3),
							ast.Constant(classVersionMinorMinimum)])]),
				body=[ast_stmt])

		list4ClassDefBody.append(ast_stmt)

	ClassDefMake = ast.ClassDef(name='Make', bases=[], keywords=[], body=list4ClassDefBody, decorator_list=[])

	ClassDef = ClassDefMake
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

if __name__ == "__main__":
	makeTypeAlias()
	makeToolBe()
