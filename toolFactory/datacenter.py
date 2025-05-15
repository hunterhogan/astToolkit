from toolFactory import pathFilenameDataframeAST, pythonVersionMinorMinimum
from typing import Any, TypedDict
import pandas
import pandera

class DictionaryAstExprType(TypedDict):
	attributeVersionMinorMinimum: int
	ast_exprType: str

panderaSchema = pandera.DataFrameSchema({
	"ClassDefIdentifier": pandera.Column(str),
	"versionMajor": pandera.Column(int),
	"versionMinor": pandera.Column(int),
	"versionMicro": pandera.Column(int),
	"base": pandera.Column(str),
	"deprecated": pandera.Column(bool),
	"base_typing_TypeAlias": pandera.Column(str),
	"attributeRename": pandera.Column(str),
	"typeC": pandera.Column(str),
	"typeStub": pandera.Column(str),
	"type_field_type": pandera.Column(str),
	"typeStub_typing_TypeAlias": pandera.Column(str),
	"list2Sequence": pandera.Column(bool),
	"defaultValue": pandera.Column(str),
	"keywordArguments": pandera.Column(bool),
	"kwargAnnotation": pandera.Column(str),
	"classAs_astAttribute": pandera.Column(str),
	"classVersionMinorMinimum": pandera.Column(int),
	"attribute": pandera.Column(str),
	"attributeKind": pandera.Column(str),
	"attributeVersionMinorMinimum": pandera.Column(int),
	"TypeAliasSubcategory": pandera.Column(str),
	"type": pandera.Column(str),
	"ast_exprType": pandera.Column(str),
	"ast_arg": pandera.Column(str),
	"match_args": pandera.Column(str),
	"match_argsVersionMinorMinimum": pandera.Column(int),
})

def getDataframe(deprecated: bool, versionMinorMaximum: int | None, *indices: str) -> pandas.DataFrame:
	dataframe = pandas.read_parquet(pathFilenameDataframeAST)
	dataframe = panderaSchema.validate(dataframe)

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	if indices:
		dataframe.set_index(keys=indices) # pyright: ignore[reportUnknownMemberType]

	return dataframe

def getElementsBe(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
	listElementsHARDCODED = ['ClassDefIdentifier', 'classAs_astAttribute', 'classVersionMinorMinimum']
	listElements = listElementsHARDCODED

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe.sort_values(by='versionMinor', inplace=False, ascending=False).drop_duplicates('ClassDefIdentifier')

	dataframe = dataframe.iloc[dataframe['ClassDefIdentifier'].astype(str).str.lower().argsort()] # pyright: ignore[reportUnknownMemberType]

	dataframe = dataframe[listElements]

	return dataframe.to_dict(orient='records') # pyright: ignore[reportReturnType, reportUnknownMemberType]

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

def getElementsGrab(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[int, list[str]]]:
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

	# Now group by attribute, then by attributeVersionMinorMinimum, collecting ast_exprType into lists
	dictionaryAttribute: dict[str, dict[int, list[str]]] = {}
	for attribute, groupAttribute in dataframe.groupby('attribute'):
		dictionaryVersionMinorMinimum: dict[int, list[str]] = {}
		groupByVersion = groupAttribute.groupby('attributeVersionMinorMinimum')
		for attributeVersionMinorMinimum, groupVersion in groupByVersion:
			listExprType = sorted(groupVersion['ast_exprType'].unique(), key=lambda x: str(x).lower()) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
			dictionaryVersionMinorMinimum[attributeVersionMinorMinimum] = listExprType # pyright: ignore[reportArgumentType]
		dictionaryAttribute[attribute] = dictionaryVersionMinorMinimum # pyright: ignore[reportArgumentType]
	return dictionaryAttribute

def getElementsMake(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
	listElementsHARDCODED = [
		'ClassDefIdentifier',
		'attribute',
		'fieldRename',
		'attributeKind',
		'ast_arg',
		'defaultValue',
		'classAs_astAttribute',
		'classVersionMinorMinimum',
		'attributeVersionMinorMinimum',
		'keywordArguments',
		'kwargAnnotation',
		'match_args',
		'match_argsVersionMinorMinimum',
	]
	listElements = listElementsHARDCODED

	"""
	Only ast class with parameters that can be set in the constructor. (__init__ method), which should mean I can filter out 'attributeKind' == 'No'.
	Approximately 40 methods in `Make` will only have the four `_attribute` attributes. Instead of treating those as `**keywordArguments`, I could make them args with default values.
	The same top-level order as getElementsBe
	"""

	"""What to return, identifiers for the return are tentative.
	ClassDefIdentifier
	list_ast_arg: list[str] if `keywordArguments` is False, add `ast_arg` in the order of 'match_args'
	kwarg: str, if `keywordArguments` is True, add `kwargAnnotation` to `list_kwargAnnotation`; later, get unique values and `'OR'.join(list_kwargAnnotation)`
	defaults: list[str] = if `keywordArguments` is False, add `defaultValue` in the order of 'match_args'

	classAs_astAttribute
	listCall_args: list[tuple(str, str)] ('attribute', if `keywordArguments` is False, 'fieldRename' | if `keywordArguments` is True and there is a 'defaultValue', then 'defaultValue' | 'attribute')
	'keywordArguments'

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

	dataframe = getDataframe(deprecated, versionMinorMaximum)

	dataframe = dataframe.sort_values(by='versionMinor', inplace=False, ascending=False).drop_duplicates('ClassDefIdentifier')

	dataframe = dataframe[listElements]

	return dataframe.to_dict(orient='records') # pyright: ignore[reportReturnType, reportUnknownMemberType]

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
	grouped = dataframe.groupby(['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum'])
	for (attribute, typeAliasSubcategory, attributeVersionMinorMinimum), group in grouped:
		listClassDefIdentifier = sorted(group['classAs_astAttribute'].unique(), key=lambda x: str(x).lower()) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
		if attribute not in dictionaryAttribute:
			dictionaryAttribute[attribute] = {}
		if typeAliasSubcategory not in dictionaryAttribute[attribute]:
			dictionaryAttribute[attribute][typeAliasSubcategory] = {}
		dictionaryAttribute[attribute][typeAliasSubcategory][int(attributeVersionMinorMinimum)] = listClassDefIdentifier
	return dictionaryAttribute
