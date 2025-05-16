from collections.abc import Sequence
from toolFactory import pathFilenameDataframeAST, pythonVersionMinorMinimum
from typing import TypedDict, TypeAlias
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
	listFunctionDef_args: list[str]
	kwarg: str
	defaults: list[str]
	listCall_args: list[tuple[str, str]]

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

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where( # pyright: ignore[reportUnknownMemberType]
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe.sort_values(by=listElements[0:2], key=lambda x: x.str.lower()) # pyright: ignore[reportUnknownLambdaType, reportUnknownMemberType]

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

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where( # pyright: ignore[reportUnknownMemberType]
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe[listElements]
	dataframe = dataframe.drop_duplicates()
	dataframe = dataframe.drop_duplicates(subset=['attribute', 'ast_exprType'], keep='first')

	dataframe = dataframe.groupby(['attribute', 'attributeVersionMinorMinimum'])['ast_exprType'].agg(list).reset_index() # pyright: ignore[reportUnknownMemberType]
	# Sort each list of ast_exprType case-insensitively
	dataframe['ast_exprType'] = dataframe['ast_exprType'].apply(sorted, key=str.lower) # pyright: ignore[reportUnknownMemberType]

	# Create tuples of (Version, ListTypesASTformAsStr)
	dataframe['listTypesByVersion'] = dataframe[['attributeVersionMinorMinimum', 'ast_exprType']].apply(tuple, axis=1) # pyright: ignore[reportUnknownMemberType]

	# Final grouping by attribute and convert to dictionary
	return dataframe.groupby('attribute')['listTypesByVersion'].agg(list).to_dict() # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType]

def getElementsMake(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[DictionaryToolMake]:
	listElementsHARDCODED = [
	'ClassDefIdentifier', 'classAs_astAttribute', 'match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue',
	'keywordArguments', 'kwargAnnotation', 'classVersionMinorMinimum', 'attributeVersionMinorMinimum', 'match_argsVersionMinorMinimum',
	]
	listElements = listElementsHARDCODED

	"""What to return, identifiers for the return are tentative.
	ClassDefIdentifier
	listFunctionDef_args: list[str] if `keywordArguments` is False, add `ast_arg` in the order of 'match_args'
	kwarg: str, if `keywordArguments` is True, add `kwargAnnotation` to `list_kwargAnnotation`; later, get unique values and `'OR'.join(list_kwargAnnotation)`
	defaults: list[str] = if `keywordArguments` is False, add `defaultValue` in the order of 'match_args'

	classAs_astAttribute
	listCall_args: list[tuple(str, str)] ('attribute', if `keywordArguments` is False, 'attributeRename' | if `keywordArguments` is True and there is a 'defaultValue', then 'defaultValue' | 'attribute')
	'keywordArguments'

pythonVersionMinorMinimum = 10
df = df[~df['deprecated']]
df['classVersionMinorMinimum'] = df['classVersionMinorMinimum'].where(df['classVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)
df['attributeVersionMinorMinimum'] = df['attributeVersionMinorMinimum'].where(df['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)
df['match_argsVersionMinorMinimum'] = df['match_argsVersionMinorMinimum'].where(df['match_argsVersionMinorMinimum'] > pythonVersionMinorMinimum, -1)

listElements = ['ClassDefIdentifier', 'classAs_astAttribute', 'match_args', 'attribute', 'attributeRename', 'ast_arg', 'defaultValue', 'keywordArguments', 'kwargAnnotation', 'classVersionMinorMinimum', 'attributeVersionMinorMinimum', 'match_argsVersionMinorMinimum',]
df = df[df['attribute'] != "No"]
subset = [element for element in listElements if element not in ['match_args', 'match_argsVersionMinorMinimum']]
df = df[listElements].drop_duplicates()

# Create a new column 'listFunctionDef_args' based on conditions
def compute_listFunctionDef_args(row):
	listAttributes = row['match_args'].replace("'","").replace(" ","").split(',')  # Split 'match_args' into a list
	className = row['ClassDefIdentifier']  # Get 'ClassDefIdentifier'
	version = row['match_argsVersionMinorMinimum']  # Get 'match_argsVersionMinorMinimum'
	collected_args: list[str] = []
	collected_defaultValue: list[str] = []
	for attributeTarget in listAttributes:
		# Find the row matching the conditions
		matching_row = df[
			(df['attribute'] == attributeTarget) &
			(df['ClassDefIdentifier'] == className) &
			(df['match_argsVersionMinorMinimum'] == version)
		]
		if not matching_row.empty:
			if not matching_row.iloc[0]['keywordArguments']:  # Check 'keywordArguments'
				collected_args.append(matching_row.iloc[0]['ast_arg'])  # Collect 'ast_arg'
				if matching_row.iloc[0]['defaultValue'] != "No":
					collected_defaultValue.append(matching_row.iloc[0]['defaultValue'])  # Collect 'defaultValue'
	# Format the collected arguments as a string
	listFunctionDef_args = ', '.join(f'"{arg}"' for arg in collected_args)
	defaults = 'No'
	if collected_defaultValue:
		defaults = ', '.join(f'"{defaultValue}"' for defaultValue in collected_defaultValue)
	return pd.Series([listFunctionDef_args, defaults], index=['listFunctionDef_args', 'defaults'])
# Apply the function to create the new column
# df['listFunctionDef_args'] = df.apply(compute_listFunctionDef_args, axis=1)
df[['listFunctionDef_args', 'defaults']] = df.apply(compute_listFunctionDef_args, axis=1)

# Compute 'kwarg' column based on 'kwargAnnotation'
def compute_kwarg(group):
	list_kwargAnnotation = sorted(val for val in group.unique() if val != "No")
	return 'OR'.join(list_kwargAnnotation) if list_kwargAnnotation else "No"
df['kwarg'] = (
	df.groupby(['ClassDefIdentifier', 'match_argsVersionMinorMinimum'])['kwargAnnotation']
	.transform(compute_kwarg)
)
	"""

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dd = [DictionaryToolMake(ClassDefIdentifier='', classAs_astAttribute='', versionMinimum={}, classVersionMinorMinimum=-1, attributeVersionMinorMinimum=-1, match_argsVersionMinorMinimum=-1)]
	return dd


"""Additional notes
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

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[int, list[str]]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'classAs_astAttribute']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	# Filter for _fields
	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	# Update attributeVersionMinorMinimum
	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].where( # pyright: ignore[reportUnknownMemberType]
		dataframe['attributeVersionMinorMinimum'] > pythonVersionMinorMinimum, -1
	)

	dataframe = dataframe.sort_values(by=listElements[0:2], key=lambda x: x.str.lower()) # pyright: ignore[reportUnknownLambdaType, reportUnknownMemberType]

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, dict[int, list[str]]]] = {}
	grouped = dataframe.groupby(['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum']) # pyright: ignore[reportUnknownMemberType]
	for (attribute, typeAliasSubcategory, attributeVersionMinorMinimum), group in grouped:
		listClassDefIdentifier = sorted(group['classAs_astAttribute'].unique(), key=lambda x: str(x).lower()) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
		if attribute not in dictionaryAttribute:
			dictionaryAttribute[attribute] = {}
		if typeAliasSubcategory not in dictionaryAttribute[attribute]:
			dictionaryAttribute[attribute][typeAliasSubcategory] = {}
		dictionaryAttribute[attribute][typeAliasSubcategory][int(attributeVersionMinorMinimum)] = listClassDefIdentifier
	return dictionaryAttribute
