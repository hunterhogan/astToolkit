import pandas
from toolFactory import pathFilenameDatabaseAST, pythonVersionMinorMinimum
from typing import Any, cast

"""

"""

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
'defaultValue__dict__',
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
	dataframeTarget = pandas.read_csv(pathFilenameDatabaseAST, index_col=indexColumns)
	return dataframeTarget

def Z0Z_getToolElements(elementIndex: str, *elements: str, sortOn: str | None = None, deprecated: bool = False, versionMinorMaximum: int | None = None):
	"""Get elements of class `AST` and its subclasses for tool manufacturing.

	This is a prototype function that would work for all tool manufacturing.

	Parameters
	----------
	elementIndex
		The column name to use as a primary identifier for each element.
	elements
		The data elements used to create the tool.
	sortOn (None)
		The element to sort on.
	deprecated (False)
		If True, include deprecated classes.
	versionMinorMaximum (None)
		The maximum version minor to get. If None, get the latest version.

	Returns
	-------
		dictionaryToolElements
			A list of tuples, The elements of the class, in the order requested.
	"""
	pass

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None):
	listElementsHARDCODED = ['attribute', 'attributeVersionMinorMinimum', 'TypeAliasSubcategory', 'classAs_astAttribute']
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
	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].apply(
		lambda version: -1 if version <= pythonVersionMinorMinimum else version
	)

	dataframe = dataframe.sort_values(
		by=listElements,
		ascending=[True, False, True, True],
		key=lambda x: x.str.lower() if x.dtype == 'object' else x
	)

	dataframe = dataframe[listElements].drop_duplicates()

	# Aggregate the last column ('classAs_astAttribute') into lists
	dataframe = dataframe.groupby(listElements[0:-1])[listElements[-1]].apply(list).reset_index()

	"""
	attributeVersionMinorMinimum: {TypeAliasSubcategory: list['classAs_astAttribute] + list['classAs_astAttribute] of smaller attributeVersionMinorMinimum},
	"""


def getElementsBe(sortOn: str | None = None, deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
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
	dataframe = dataframe.sort_values(by='versionMinor', inplace=False, ascending=False).drop_duplicates('ClassDefIdentifier') # type: ignore

	if sortOn is not None:
		# TODO after changing the dataframe storage from csv to something smart, make this check smarter
		# match str(dataframe[sortOn].dtype):
		dataframe = dataframe.iloc[dataframe[sortOn].astype(str).str.lower().argsort()]

	# Select the requested columns, in the specified order
	dataframe = dataframe[listElements]

	return dataframe.to_dict(orient='records') # type: ignore
