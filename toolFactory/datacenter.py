from toolFactory import pathFilenameDatabaseAST, pythonVersionMinorMinimum
from typing import Any
import pandas

cc=[
'ClassDefIdentifier',
'versionMajor',
'versionMinor',
'versionMicro',
'base',
'deprecated',
'base_typing_TypeAlias',
'fieldRename',
'typeC',
'typeStub',
'type_field_type',
'typeStub_typing_TypeAlias',
'list2Sequence',
'defaultValue',
'keywordArguments',
'kwargAnnotation',
'keywordArgumentsDefaultValue',
'classAs_astAttribute',
'classVersionMinorMinimum',
'attribute',
'attributeKind',
'attributeVersionMinorMinimum',
'TypeAliasSubcategory',
'type',
'ast_exprType',
'ast_arg',
]

def getDataframe() -> pandas.DataFrame:
	"""Get the dataframe from the database file.

	This is the only function that should access the data on disk.

	Returns
	-------
	pandas.DataFrame
		The dataframe containing the AST data.
	"""
	indexColumns = cc
	dataframeTarget = pandas.read_csv(pathFilenameDatabaseAST, index_col=indexColumns) # pyright: ignore[reportUnknownMemberType]
	return dataframeTarget

def getElementsBe(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
	"""Get elements of class `AST` and its subclasses for tool manufacturing.

	Parameters
	----------
	sortOn (None)
		The element to sort on; if a string, case-insensitive.
	deprecated (False)
		Whether to include deprecated classes.
	versionMinorMaximum (None)
		The maximum version minor to get. If None, get the latest version.

	Returns
		listDictionaryToolElements
	-------
			A list of dictionaries with element:value pairs.
	"""

	listElementsHARDCODED = ['ClassDefIdentifier', 'classAs_astAttribute', 'classVersionMinorMinimum']
	listElements = listElementsHARDCODED

	dataframe = getDataframe()

	# Reset index to make the index columns regular columns
	dataframe = dataframe.reset_index()

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	dataframe['versionMinor'] = dataframe['versionMinor'].astype(int)

	# Remove versions above maximum version
	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	# Remove duplicate ClassDefIdentifier
	# TODO think about how the function knows to remove _these_ duplicates
	dataframe = dataframe.sort_values(by='versionMinor', inplace=False, ascending=False).drop_duplicates('ClassDefIdentifier') # pyright: ignore[reportUnknownMemberType]

	# TODO after changing the dataframe storage from csv to something smart, make this check smarter
	# match str(dataframe[sortOn].dtype):
	dataframe = dataframe.iloc[dataframe['ClassDefIdentifier'].astype(str).str.lower().argsort()] # pyright: ignore[reportUnknownMemberType]

	# Select the requested columns, in the specified order
	dataframe = dataframe[listElements]

	return dataframe.to_dict(orient='records') # pyright: ignore[reportReturnType, reportUnknownMemberType]

def getElementsClassIsAndAttribute(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[str, int | str]]]:
	return getElementsDOT(deprecated, versionMinorMaximum)

def getElementsDOT(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[str, int | str]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'ast_exprType']
	listElements = listElementsHARDCODED

	dataframe = getDataframe()
	dataframe = dataframe.reset_index()

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	dataframe['versionMinor'] = dataframe['versionMinor'].astype(int)

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].apply( # pyright: ignore[reportUnknownMemberType]
		lambda version: -1 if version <= pythonVersionMinorMinimum else version # pyright: ignore[reportUnknownLambdaType]
	)

	dataframe = dataframe.sort_values( # pyright: ignore[reportUnknownMemberType]
		by=listElements,
		ascending=[True, True, True, True],
		key=lambda x: x.str.lower() if x.dtype == 'object' else x # pyright: ignore[reportUnknownMemberType,reportUnknownLambdaType]
	)

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, dict[str, int | str]]] = {}
	for _elephino, row in dataframe.iterrows(): # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
		attributeKey = str(row['attribute']) # pyright: ignore[reportUnknownArgumentType]
		typeAliasKey = str(row['TypeAliasSubcategory']) # pyright: ignore[reportUnknownArgumentType]
		attributeVersionMinorMinimum = row['attributeVersionMinorMinimum'] # pyright: ignore[reportUnknownVariableType]
		astExprType = row['ast_exprType'] # pyright: ignore[reportUnknownVariableType]
		if attributeKey not in dictionaryAttribute:
			dictionaryAttribute[attributeKey] = {}
		if typeAliasKey not in dictionaryAttribute[attributeKey]:
			dictionaryAttribute[attributeKey][typeAliasKey] = {
				'attributeVersionMinorMinimum': attributeVersionMinorMinimum,
				'ast_exprType': astExprType
			}
		else:
			if attributeVersionMinorMinimum < dictionaryAttribute[attributeKey][typeAliasKey]['attributeVersionMinorMinimum']:
				dictionaryAttribute[attributeKey][typeAliasKey] = {
					'attributeVersionMinorMinimum': attributeVersionMinorMinimum,
					'ast_exprType': astExprType
				}
	return dictionaryAttribute

def getElementsGrab(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[int, list[str]]]:
	listElementsHARDCODED = ['attribute', 'attributeVersionMinorMinimum', 'ast_exprType']
	listElements = listElementsHARDCODED

	dataframe = getDataframe()
	dataframe = dataframe.reset_index()

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	dataframe['versionMinor'] = dataframe['versionMinor'].astype(int)

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].apply( # pyright: ignore[reportUnknownMemberType]
		lambda version: -1 if version <= pythonVersionMinorMinimum else version # pyright: ignore[reportUnknownLambdaType]
	)

	dataframe = dataframe[listElements]
	dataframe = dataframe.drop_duplicates()

	# For each (attribute, ast_exprType), select the row with the smallest attributeVersionMinorMinimum
	dataframe = dataframe.sort_values(by=listElements, ascending=[True, True, True], key=lambda x: x.str.lower() if x.dtype == 'object' else x) # pyright: ignore[reportUnknownLambdaType, reportUnknownMemberType]
	dataframe = dataframe.drop_duplicates(subset=['attribute', 'ast_exprType'], keep='first')

	# Now group by attribute, then by attributeVersionMinorMinimum, collecting ast_exprType into lists
	dictionaryAttribute: dict[str, dict[int, list[str]]] = {}
	for attribute, groupAttribute in dataframe.groupby('attribute'): # pyright: ignore[reportUnknownMemberType]
		dictionaryVersionMinorMinimum: dict[int, list[str]] = {}
		groupByVersion = groupAttribute.groupby('attributeVersionMinorMinimum') # pyright: ignore[reportUnknownMemberType]
		for attributeVersionMinorMinimum, groupVersion in groupByVersion:
			listExprType = sorted(groupVersion['ast_exprType'].unique(), key=lambda x: str(x).lower()) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
			dictionaryVersionMinorMinimum[attributeVersionMinorMinimum] = listExprType # pyright: ignore[reportArgumentType]
		dictionaryAttribute[attribute] = dictionaryVersionMinorMinimum # pyright: ignore[reportArgumentType]
	return dictionaryAttribute

def getElementsMake(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
	"""Get elements of class `AST` and its subclasses for tool manufacturing.

	Parameters
	----------
	sortOn (None)
		The element to sort on; if a string, case-insensitive.
	deprecated (False)
		Whether to include deprecated classes.
	versionMinorMaximum (None)
		The maximum version minor to get. If None, get the latest version.

	Returns
		listDictionaryToolElements
	-------
			A list of dictionaries with element:value pairs.
	"""

	listElementsHARDCODED = ['ClassDefIdentifier', 'classAs_astAttribute', 'classVersionMinorMinimum']
	mm=['attributeVersionMinorMinimum', 'ast_arg']
	listElements = listElementsHARDCODED

	dataframe = getDataframe()

	# Reset index to make the index columns regular columns
	dataframe = dataframe.reset_index()

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	dataframe['versionMinor'] = dataframe['versionMinor'].astype(int)

	# Remove versions above maximum version
	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	# Remove duplicate ClassDefIdentifier
	# TODO think about how the function knows to remove _these_ duplicates
	dataframe = dataframe.sort_values(by='versionMinor', inplace=False, ascending=False).drop_duplicates('ClassDefIdentifier') # pyright: ignore[reportUnknownMemberType]

	# TODO after changing the dataframe storage from csv to something smart, make this check smarter
	# match str(dataframe[sortOn].dtype):
	# dataframe = dataframe.iloc[dataframe[sortOn].astype(str).str.lower().argsort()]

	# Select the requested columns, in the specified order
	dataframe = dataframe[listElements]

	return dataframe.to_dict(orient='records') # pyright: ignore[reportReturnType, reportUnknownMemberType]

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> dict[str, dict[str, dict[int, list[str]]]]:
	listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'classAs_astAttribute']
	listElements = listElementsHARDCODED

	dataframe = getDataframe()
	dataframe = dataframe.reset_index()

	if not deprecated:
		dataframe = dataframe[~dataframe['deprecated']]

	if versionMinorMaximum is not None:
		dataframe = dataframe[dataframe['versionMinor'] <= versionMinorMaximum]

	# Filter for _fields
	dataframe = dataframe[dataframe['attributeKind'] == '_field']

	# Update attributeVersionMinorMinimum
	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].apply( # pyright: ignore[reportUnknownMemberType]
		lambda version: -1 if version <= pythonVersionMinorMinimum else version # pyright: ignore[reportUnknownLambdaType]
	)

	dataframe = dataframe.sort_values( # pyright: ignore[reportUnknownMemberType]
		by=listElements,
		ascending=[True, True, True, True],
		key=lambda x: x.str.lower() if x.dtype == 'object' else x # pyright: ignore[reportUnknownLambdaType, reportUnknownMemberType]
	)

	dataframe = dataframe[listElements].drop_duplicates()

	dictionaryAttribute: dict[str, dict[str, dict[int, list[str]]]] = {}
	grouped = dataframe.groupby(['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum']) # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
	for (attribute, typeAliasSubcategory, attributeVersionMinorMinimum), group in grouped: # pyright: ignore[reportUnknownVariableType]
		listClassDefIdentifier = sorted(group['classAs_astAttribute'].unique(), key=lambda x: str(x).lower()) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
		if attribute not in dictionaryAttribute:
			dictionaryAttribute[attribute] = {}
		if typeAliasSubcategory not in dictionaryAttribute[attribute]:
			dictionaryAttribute[attribute][typeAliasSubcategory] = {}
		dictionaryAttribute[attribute][typeAliasSubcategory][attributeVersionMinorMinimum] = listClassDefIdentifier
	return dictionaryAttribute
