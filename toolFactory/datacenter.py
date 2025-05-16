# pyright: reportArgumentType = false
# pyright: reportUnknownParameterType = false
# pyright: reportUnknownLambdaType = false
# pyright: reportMissingTypeArgument = false
# pyright: reportUnknownArgumentType = false
# pyright: reportReturnType = false
# pyright: reportUnknownMemberType = false
# pyright: reportUnknownVariableType = false

from collections.abc import Sequence
from toolFactory import pathFilenameDataframeAST, pythonVersionMinorMinimum
from typing import TypedDict, TypeAlias, cast
import pandas

Attribute: TypeAlias = str
Version: TypeAlias = int
ListTypesASTformAsStr: TypeAlias = list[str]
TupleTypesForVersion: TypeAlias = tuple[Version, ListTypesASTformAsStr]
ListTypesByVersion: TypeAlias = list[TupleTypesForVersion]

class DictionaryAstExprType(TypedDict):
	attributeVersionMinorMinimum: int
	ast_exprType: str

class DictionaryToolBe(TypedDict):
	ClassDefIdentifier: str
	classAs_astAttribute: str
	classVersionMinorMinimum: int

class DictionaryMatchArgs(TypedDict):
	listStr4FunctionDef_args: list[str]
	kwarg: str
	listDefaults: list[str]
	listTuplesCall_keywords: list[tuple[str, bool, str]]

class DictionaryToolMake(TypedDict):
	ClassDefIdentifier: str
	classAs_astAttribute: str
	versionMinimum: dict[int, DictionaryMatchArgs]

	classVersionMinorMinimum: int
	attributeVersionMinorMinimum: int
	match_argsVersionMinorMinimum: int

def getDataframe(deprecated: bool, versionMinorMaximum: int | None, *indices: str) -> pandas.DataFrame:
	dataframe = pandas.read_parquet(pathFilenameDataframeAST)

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	if indices:
		dataframe.set_index(keys=indices)

	return dataframe

def getElementsBe(deprecated: bool = False, versionMinorMaximum: int | None = None) -> Sequence[DictionaryToolBe]:
	listElementsHARDCODED = ['ClassDefIdentifier', 'classAs_astAttribute', 'classVersionMinorMinimum']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe['classVersionMinorMinimum'] = dataframe['classVersionMinorMinimum'].where(
		dataframe['classVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe[listElements].drop_duplicates()

	return dataframe.to_dict(orient='records')

def getElementsClassIsAndAttribute(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, DictionaryAstExprType]]:
	return getElementsDOT(deprecated, versionMinorMaximum)

def getElementsDOT(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, DictionaryAstExprType]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'ast_exprType']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where(
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe.sort_values(by=listElements[0:2], key=lambda x: x.str.lower())

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, DictionaryAstExprType]] = {}
	for _elephino, row in dataframe.iterrows():
		attributeKey = row['attribute']
		typeAliasKey = row['TypeAliasSubcategory']
		attributeVersionMinorMinimum = row['attributeVersionMinorMinimum']
		astExprType = row['ast_exprType']
		if attributeKey not in dictionaryAttribute:
			dictionaryAttribute[attributeKey] = {}
		if typeAliasKey not in dictionaryAttribute[attributeKey]:
			dictionaryAttribute[attributeKey][typeAliasKey] = {
				'attributeVersionMinorMinimum': attributeVersionMinorMinimum,
				'ast_exprType': astExprType
			}
		else:
			if attributeVersionMinorMinimum < dictionaryAttribute[attributeKey][typeAliasKey]['attributeVersionMinorMinimum']:
				dictionaryAttribute[attributeKey][typeAliasKey] = DictionaryAstExprType(
					attributeVersionMinorMinimum=attributeVersionMinorMinimum,
					ast_exprType=astExprType
				)
	return dictionaryAttribute

def getElementsGrab(deprecated: bool = False, versionMinorMaximum: Version | None = None) -> dict[Attribute, ListTypesByVersion]:
	listElementsHARDCODED = ['attribute', 'attributeVersionMinorMinimum', 'ast_exprType']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where(
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe[listElements]
	dataframe = dataframe.drop_duplicates()
	dataframe = dataframe.drop_duplicates(subset=['attribute', 'ast_exprType'], keep='first')

	dataframe = dataframe.groupby(['attribute', 'attributeVersionMinorMinimum'])['ast_exprType'].agg(list).reset_index()
	# Sort each list of ast_exprType case-insensitively
	dataframe['ast_exprType'] = dataframe['ast_exprType'].apply(sorted, key=str.lower)

	# Create tuples of (Version, ListTypesASTformAsStr)
	dataframe['listTypesByVersion'] = dataframe[['attributeVersionMinorMinimum', 'ast_exprType']].apply(tuple, axis=1)

	# Final grouping by attribute and convert to dictionary
	return dataframe.groupby('attribute')['listTypesByVersion'].agg(list).to_dict()

def getElementsMake(deprecated: bool = False, versionMinorMaximum: int | None = None):
	listElementsHARDCODED = [
	'ClassDefIdentifier',
	'classAs_astAttribute',
	'match_args',
	'attribute',
	'attributeRename',
	'ast_arg',
	'defaultValue',
	'keywordArguments',
	'kwargAnnotation',
	'classVersionMinorMinimum',
	'match_argsVersionMinorMinimum',
	]
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe['classVersionMinorMinimum'] = dataframe['classVersionMinorMinimum'].where(dataframe['classVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)
	dataframe['match_argsVersionMinorMinimum'] = dataframe['match_argsVersionMinorMinimum'].where(dataframe['match_argsVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)

	dataframe = dataframe[dataframe['attribute'] != "No"]
	dataframe = dataframe[listElements].drop_duplicates()

	# Create a new column 'listStr4FunctionDef_args' based on conditions
	def compute_listFunctionDef_args(row: pandas.Series) -> pandas.Series:
		listAttributes = cast(str, row['match_args']).replace("'","").replace(" ","").split(',')  # Split 'match_args' into a list
		className = row['ClassDefIdentifier']   # Get 'ClassDefIdentifier'
		version = row['match_argsVersionMinorMinimum']   # Get 'match_argsVersionMinorMinimum'
		collected_args: list[str] = []
		collected_defaultValue: list[str] = []
		collectedTupleCall_keywords: list[str | bool] = []
		for attributeTarget in listAttributes:
			tupleCall_keywords = []
			# Find the row matching the conditions
			tupleCall_keywords.append(attributeTarget)
			matching_row = dataframe[
				(dataframe['attribute'] == attributeTarget) &
				(dataframe['ClassDefIdentifier'] == className) &
				(dataframe['match_argsVersionMinorMinimum'] == version)
			]
			if not matching_row.empty:
				if matching_row.iloc[0]['keywordArguments']:   # Check 'keywordArguments'
					tupleCall_keywords.append(True)
					tupleCall_keywords.append(matching_row.iloc[0]['defaultValue'])
				else:
					collected_args.append(matching_row.iloc[0]['ast_arg'])   # Collect 'ast_arg'
					tupleCall_keywords.append(False)
					if matching_row.iloc[0]['attributeRename'] != "No":
						tupleCall_keywords.append(matching_row.iloc[0]['attributeRename'])
					else:
						tupleCall_keywords.append(attributeTarget)
					if matching_row.iloc[0]['defaultValue'] != "No":
						collected_defaultValue.append(matching_row.iloc[0]['defaultValue'])   # Collect 'defaultValue'
			collectedTupleCall_keywords.append(tuple(tupleCall_keywords))

		# Store the actual lists/tuples instead of formatting as strings
		return pandas.Series([collected_args, collected_defaultValue, collectedTupleCall_keywords],
							index=['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords'])

	# Apply the function to create the new columns
	dataframe[['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords']] = dataframe.apply(compute_listFunctionDef_args, axis=1)

	# Compute 'kwarg' column based on 'kwargAnnotation'
	def compute_kwarg(group: pandas.Series) -> str:
		list_kwargAnnotation = sorted(value for value in group.unique() if value != "No")
		return 'OR'.join(list_kwargAnnotation) if list_kwargAnnotation else "No"
	dataframe['kwarg'] = (
		dataframe.groupby(['ClassDefIdentifier', 'match_argsVersionMinorMinimum'])['kwargAnnotation']
		.transform(compute_kwarg)
	)

	dataframe = dataframe.drop(columns=['match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue', 'keywordArguments', 'kwargAnnotation'])

	# Convert columns to strings for drop_duplicates (since lists aren't hashable)
	temp_dataframe = dataframe.copy()
	temp_dataframe['listStr4FunctionDef_args'] = temp_dataframe['listStr4FunctionDef_args'].apply(lambda x: str(x))
	temp_dataframe['listDefaults'] = temp_dataframe['listDefaults'].apply(lambda x: str(x))
	temp_dataframe['listTupleCall_keywords'] = temp_dataframe['listTupleCall_keywords'].apply(lambda x: str(x))

	# Drop duplicates on the string representation
	temp_dataframe = temp_dataframe.drop_duplicates()

	# Get the indices of the unique rows
	unique_indices = temp_dataframe.index

	# Filter the original dataframe to keep only the unique rows
	dataframe = dataframe.loc[unique_indices]

	# newColumns = ['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords', 'kwarg']
	return dataframe.to_dict(orient='records')

	"""Additional notes
	What to return, identifiers for the return are tentative.
	ClassDefIdentifier
	listStr4FunctionDef_args: list[str] if `keywordArguments` is False, add `ast_arg` in the order of 'match_args'
	kwarg: str, if `keywordArguments` is True, add `kwargAnnotation` to `list_kwargAnnotation`; later, get unique values and `'OR'.join(list_kwargAnnotation)`
	listDefaults: list[str] = if `keywordArguments` is False, add `defaultValue` in the order of 'match_args'

	classAs_astAttribute
	listTupleCall_keywords: list[tuple(str, bool, str)]
		attributes in match_args:
			attribute, if `keywordArguments` is False, False, 'attributeRename' if 'attributeRename' is not "No", else 'attribute'
						if `keywordArguments` is True, True, then 'defaultValue'

							classVersionMinorMinimum: more than one if applicable, and with different values for some of the above returns; we should create the code to handle:
		class,classVersionMinorMinimum,match_argsVersionMinorMinimum
		AsyncFunctionDef,-1,-1
		AsyncFunctionDef,-1,12
		ClassDef,-1,-1
		ClassDef,-1,12
		FunctionDef,-1,-1
		FunctionDef,-1,12

	match_argsVersionMinorMinimum: more than one if applicable, and with different values for some of the above returns; certainly applies to:
		class,classVersionMinorMinimum,match_argsVersionMinorMinimum
		ParamSpec,12,12
		ParamSpec,12,13
		TypeVar,12,12
		TypeVar,12,13
		TypeVarTuple,12,12
		TypeVarTuple,12,13
	"""

	"""
pythonVersionMinorMinimum = 10
listElements = ['ClassDefIdentifier', 'classAs_astAttribute', 'match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue', 'keywordArguments', 'kwargAnnotation', 'classVersionMinorMinimum', 'match_argsVersionMinorMinimum',]
df = df[~df['deprecated']]
	"""

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[int, list[str]]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'classAs_astAttribute']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	# Filter for _fields
	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	# Update attributeVersionMinorMinimum
	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where(
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe.sort_values(by=listElements[0:2], key=lambda x: x.str.lower())

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, dict[int, list[str]]]] = {}
	grouped = dataframe.groupby(['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum'])
	for (attribute, typeAliasSubcategory, attributeVersionMinorMinimum), group in grouped:
		listClassDefIdentifier = sorted(group['classAs_astAttribute'].unique(), key=lambda x: str(x).lower()) 
		if attribute not in dictionaryAttribute:
			dictionaryAttribute[attribute] = {}
		if typeAliasSubcategory not in dictionaryAttribute[attribute]:
			dictionaryAttribute[attribute][typeAliasSubcategory] = {}
		dictionaryAttribute[attribute][typeAliasSubcategory][int(attributeVersionMinorMinimum)] = listClassDefIdentifier
	return dictionaryAttribute
