from collections.abc import Sequence
from toolFactory import pathFilenameDataframeAST, pythonVersionMinorMinimum
from typing import cast, TypeAlias, TypedDict
import pandas

# TODO datacenter needs to do all data manipulation, not the toolFactory
# TODO more and better pandas usage
# TODO or better, get rid of Pandas and use the original sources

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
	kwarg: str
	listDefaults: list[str]
	listStr4FunctionDef_args: list[str]
	listTupleCall_keywords: list[tuple[str, bool, str]]

class DictionaryClassDef(TypedDict):
	classAs_astAttribute: str
	classVersionMinorMinimum: dict[int, dict[int, DictionaryMatchArgs]]

def _sortCaseInsensitive(dataframe: pandas.DataFrame, columns: Sequence[str]) -> pandas.DataFrame:
    dataframeCopy = dataframe.copy()
    for columnName in columns:
        dataframeCopy[columnName] = dataframe[columnName].str.lower() # pyright: ignore[reportUnknownMemberType]

    sorted_index = dataframeCopy.sort_values(by=columns).index # pyright: ignore[reportUnknownMemberType]
    return dataframe.loc[sorted_index]

def getDataframe(deprecated: bool, versionMinorMaximum: int | None, *indices: str) -> pandas.DataFrame:
	dataframe = pandas.read_parquet(pathFilenameDataframeAST)

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	columnsVersion = ['attributeVersionMinorMinimum', 'classVersionMinorMinimum', 'match_argsVersionMinorMinimum']
	dataframe[columnsVersion] = dataframe[columnsVersion].where(dataframe[columnsVersion] > pythonVersionMinorMinimum, -1)

	if indices:
		dataframe.set_index(keys=indices) # pyright: ignore[reportUnknownMemberType]

	return dataframe

def getElementsBe(deprecated: bool = False, versionMinorMaximum: int | None = None) -> Sequence[DictionaryToolBe]:
	listElementsHARDCODED = ['ClassDefIdentifier', 'classAs_astAttribute', 'classVersionMinorMinimum']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[listElements].drop_duplicates()

	return dataframe.to_dict(orient='records') # pyright: ignore[reportReturnType]

def getElementsClassIsAndAttribute(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, DictionaryAstExprType]]:
	return getElementsDOT(deprecated, versionMinorMaximum)

def getElementsDOT(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, DictionaryAstExprType]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'ast_exprType']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe = _sortCaseInsensitive(dataframe, listElements[0:2])

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, DictionaryAstExprType]] = {}
	for _elephino, row in dataframe.iterrows(): # pyright: ignore[reportUnknownVariableType]
		attributeKey = cast(str, row['attribute'])
		typeAliasKey = cast(str, row['TypeAliasSubcategory'])
		attributeVersionMinorMinimum = cast(int, row['attributeVersionMinorMinimum'])
		astExprType = cast(str, row['ast_exprType'])
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

	dataframe = dataframe[listElements]
	dataframe = dataframe.drop_duplicates()
	dataframe = dataframe.drop_duplicates(subset=['attribute', 'ast_exprType'], keep='first')

	dataframe = dataframe.groupby(['attribute', 'attributeVersionMinorMinimum'])['ast_exprType'].aggregate(list).reset_index()
	dataframe['ast_exprType'] = dataframe['ast_exprType'].apply(sorted, key=str.lower) # pyright: ignore[reportUnknownMemberType]
	dataframe['listTypesByVersion'] = dataframe[['attributeVersionMinorMinimum', 'ast_exprType']].apply(tuple, axis=1) # pyright: ignore[reportUnknownMemberType]
	return dataframe.groupby('attribute')['listTypesByVersion'].aggregate(list).to_dict()

def getElementsMake(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, DictionaryClassDef]:
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

	dataframe = dataframe[dataframe['attribute'] != "No"]
	dataframe = dataframe[listElements].drop_duplicates()

	def compute_listFunctionDef_args(row: pandas.Series) -> pandas.Series: # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
		listAttributes: list[str] = cast(str, row['match_args']).replace("'","").replace(" ","").split(',')  # Split 'match_args' into a list
		className = cast(str, row['ClassDefIdentifier'])
		version = cast(int, row['match_argsVersionMinorMinimum'])
		listStr4FunctionDef_args: list[str] = []
		listDefaults: list[str] = []
		listTupleCall_keywords: list[tuple[str, bool, str]] = []
		for attributeTarget in listAttributes:
			tupleCall_keywords: list[str | bool] = []
			tupleCall_keywords.append(attributeTarget)
			matching_row = dataframe[
				(dataframe['attribute'] == attributeTarget) &
				(dataframe['ClassDefIdentifier'] == className) &
				(dataframe['match_argsVersionMinorMinimum'] == version)
			]
			if not matching_row.empty:
				if matching_row.iloc[0]['keywordArguments']:
					tupleCall_keywords.append(True)
					tupleCall_keywords.append(cast(str, matching_row.iloc[0]['defaultValue']))
				else:
					listStr4FunctionDef_args.append(cast(str, matching_row.iloc[0]['ast_arg']))
					tupleCall_keywords.append(False)
					if matching_row.iloc[0]['attributeRename'] != "No":
						tupleCall_keywords.append(cast(str,matching_row.iloc[0]['attributeRename']))
					else:
						tupleCall_keywords.append(attributeTarget)
					if matching_row.iloc[0]['defaultValue'] != "No":
						listDefaults.append(cast(str, matching_row.iloc[0]['defaultValue']))
			listTupleCall_keywords.append(cast(tuple[str, bool, str], tuple(tupleCall_keywords)))

		return pandas.Series([listStr4FunctionDef_args, listDefaults, listTupleCall_keywords],
							index=['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords'])

	# Apply the function to create the new columns
	dataframe[['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords']] = dataframe.apply(compute_listFunctionDef_args, axis=1) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]

	def compute_kwarg(group: pandas.Series) -> str: # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
		list_kwargAnnotation = sorted(value for value in group.unique() if value != "No")
		return 'OR'.join(list_kwargAnnotation) if list_kwargAnnotation else "No"
	dataframe['kwarg'] = (dataframe.groupby(['ClassDefIdentifier', 'match_argsVersionMinorMinimum'])['kwargAnnotation'].transform(compute_kwarg)) # pyright: ignore[reportUnknownArgumentType]

	dataframe = dataframe.drop(columns=['match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue', 'keywordArguments', 'kwargAnnotation'])

	# Convert columns to strings for drop_duplicates (since lists aren't hashable)
	dataframeHashable = dataframe.copy()
	columnsLists = ['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords']
	dataframeHashable[columnsLists] = dataframeHashable[columnsLists].astype(str)
	dataframeHashable = dataframeHashable.drop_duplicates()
	indicesToKeep = dataframeHashable.index

	# Filter the original dataframe to keep only the unique rows
	dataframe = dataframe.loc[indicesToKeep]

	# Create the nested dictionary structure
	# First, create a function to build the inner match_args dictionaries
	def idkHowToNameThingsOrFollowInstructions(groupbyClassVersion: pandas.DataFrame) -> dict[int, DictionaryMatchArgs]: # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
		return {
			row['match_argsVersionMinorMinimum']: {
				'kwarg': row['kwarg'],
				'listDefaults': row['listDefaults'],
				'listStr4FunctionDef_args': row['listStr4FunctionDef_args'],
				'listTupleCall_keywords': row['listTupleCall_keywords']
			}
			for _elephino, row in groupbyClassVersion.iterrows() # pyright: ignore[reportUnknownVariableType]
		}

	# Group by ClassDefIdentifier and classVersionMinorMinimum to create nested structure
	ImaAIGeneratedDictionaryWithTheStupidestIdentifier: dict[str, DictionaryClassDef] = {}
	for ClassDefIdentifier, class_group in dataframe.groupby('ClassDefIdentifier', sort=False):
		ImaAIGeneratedDictionaryWithTheStupidestIdentifier[cast(str, ClassDefIdentifier)] = {
			'classAs_astAttribute': class_group['classAs_astAttribute'].iloc[0], # pyright: ignore[reportUnknownMemberType]
			'classVersionMinorMinimum': {}
		}

		# Group by classVersionMinorMinimum and build the inner dictionaries
		for classVersionMinorMinimum, groupbyClassVersion in class_group.groupby('classVersionMinorMinimum'):
			ImaAIGeneratedDictionaryWithTheStupidestIdentifier[cast(str, ClassDefIdentifier)]['classVersionMinorMinimum'][cast(int, classVersionMinorMinimum)] = idkHowToNameThingsOrFollowInstructions(groupbyClassVersion)

	return ImaAIGeneratedDictionaryWithTheStupidestIdentifier

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[int, list[str]]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'classAs_astAttribute']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe = _sortCaseInsensitive(dataframe, listElements[0:2])

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
