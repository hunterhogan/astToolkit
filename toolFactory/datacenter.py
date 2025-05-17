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
	dataframe['ast_exprType'] = dataframe['ast_exprType'].apply(sorted, key=str.lower)
	dataframe['listTypesByVersion'] = dataframe[['attributeVersionMinorMinimum', 'ast_exprType']].apply(tuple, axis=1)
	return dataframe.groupby('attribute')['listTypesByVersion'].agg(list).to_dict()

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

	dataframe['classVersionMinorMinimum'] = dataframe['classVersionMinorMinimum'].where(dataframe['classVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)
	dataframe['match_argsVersionMinorMinimum'] = dataframe['match_argsVersionMinorMinimum'].where(dataframe['match_argsVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)

	dataframe = dataframe[dataframe['attribute'] != "No"]
	dataframe = dataframe[listElements].drop_duplicates()

	def compute_listFunctionDef_args(row: pandas.Series) -> pandas.Series:
		listAttributes: list[str] = cast(str, row['match_args']).replace("'","").replace(" ","").split(',')  # Split 'match_args' into a list
		className = row['ClassDefIdentifier']
		version = row['match_argsVersionMinorMinimum']
		collected_args: list[str] = []
		collected_defaultValue: list[str] = []
		collectedTupleCall_keywords: list[str | bool] = []
		for attributeTarget in listAttributes:
			tupleCall_keywords = []
			tupleCall_keywords.append(attributeTarget)
			matching_row = dataframe[
				(dataframe['attribute'] == attributeTarget) &
				(dataframe['ClassDefIdentifier'] == className) &
				(dataframe['match_argsVersionMinorMinimum'] == version)
			]
			if not matching_row.empty:
				if matching_row.iloc[0]['keywordArguments']:
					tupleCall_keywords.append(True)
					tupleCall_keywords.append(matching_row.iloc[0]['defaultValue'])
				else:
					collected_args.append(matching_row.iloc[0]['ast_arg'])
					tupleCall_keywords.append(False)
					if matching_row.iloc[0]['attributeRename'] != "No":
						tupleCall_keywords.append(matching_row.iloc[0]['attributeRename'])
					else:
						tupleCall_keywords.append(attributeTarget)
					if matching_row.iloc[0]['defaultValue'] != "No":
						collected_defaultValue.append(matching_row.iloc[0]['defaultValue'])
			collectedTupleCall_keywords.append(tuple(tupleCall_keywords))

		return pandas.Series([collected_args, collected_defaultValue, collectedTupleCall_keywords],
							index=['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords'])

	# Apply the function to create the new columns
	dataframe[['listStr4FunctionDef_args', 'listDefaults', 'listTupleCall_keywords']] = dataframe.apply(compute_listFunctionDef_args, axis=1)

	def compute_kwarg(group: pandas.Series) -> str:
		list_kwargAnnotation = sorted(value for value in group.unique() if value != "No")
		return 'OR'.join(list_kwargAnnotation) if list_kwargAnnotation else "No"
	dataframe['kwarg'] = (dataframe.groupby(['ClassDefIdentifier', 'match_argsVersionMinorMinimum'])['kwargAnnotation'].transform(compute_kwarg))

	dataframe = dataframe.drop(columns=['match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue', 'keywordArguments', 'kwargAnnotation'])

	# Convert columns to strings for drop_duplicates (since lists aren't hashable)
	dataframeHashable = dataframe.copy()
	dataframeHashable['listStr4FunctionDef_args'] = dataframeHashable['listStr4FunctionDef_args'].apply(lambda x: str(x))
	dataframeHashable['listDefaults'] = dataframeHashable['listDefaults'].apply(lambda x: str(x))
	dataframeHashable['listTupleCall_keywords'] = dataframeHashable['listTupleCall_keywords'].apply(lambda x: str(x))
	dataframeHashable = dataframeHashable.drop_duplicates()
	indicesToKeep = dataframeHashable.index

	# Filter the original dataframe to keep only the unique rows
	dataframe = dataframe.loc[indicesToKeep]

	# Create the nested dictionary structure
	# First, create a function to build the inner match_args dictionaries
	def create_match_args_dict(group: pandas.Series) -> dict[int, DictionaryMatchArgs]:
		return {
			row['match_argsVersionMinorMinimum']: {
				'kwarg': row['kwarg'],
				'listDefaults': row['listDefaults'],
				'listStr4FunctionDef_args': row['listStr4FunctionDef_args'],
				'listTupleCall_keywords': row['listTupleCall_keywords']
			}
			for _elephino, row in group.iterrows()
		}

	# Group by ClassDefIdentifier and classVersionMinorMinimum to create nested structure
	ImaAIGeneratedDictionaryWithTheStupidestIdentifier: dict[str, DictionaryClassDef] = {}
	for ClassDefIdentifier, class_group in dataframe.groupby('ClassDefIdentifier', sort=False):
		ImaAIGeneratedDictionaryWithTheStupidestIdentifier[ClassDefIdentifier] = {
			'classAs_astAttribute': class_group['classAs_astAttribute'].iloc[0],
			'classVersionMinorMinimum': {}
		}

		# Group by classVersionMinorMinimum and build the inner dictionaries
		for classVersionMinorMinimum, ver_group in class_group.groupby('classVersionMinorMinimum'):
			ImaAIGeneratedDictionaryWithTheStupidestIdentifier[ClassDefIdentifier]['classVersionMinorMinimum'][classVersionMinorMinimum] = create_match_args_dict(ver_group)

	return ImaAIGeneratedDictionaryWithTheStupidestIdentifier

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[int, list[str]]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'classAs_astAttribute']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

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
