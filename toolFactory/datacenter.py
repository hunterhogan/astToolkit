import pandas
from toolFactory import pathFilenameDatabaseAST
from typing import Any, cast

"""
new column
fieldVersionMinorMinimum
for each ClassDefIdentifier,
for each field of the ClassDefIdentifier,
get unique values of 'versionMinor' and sort them,
validate the data: if the values are not contiguous from smallest to largest, give an error,
validate the data: if the largest value is not 13, give an error,
validate the data: if the smallest value is less than 9, give an error,
if the smallest value is 9, record -1 in the column,
else, record the smallest value in the column.

"""

cc=[
'ClassDefIdentifier',
'versionMajor',
'versionMinor',
'versionMicro',
'base',
'field',
'_attribute',
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
		dataframe = cast(pandas.DataFrame, dataframe[~dataframe['deprecated']])

	# Remove versions above maximum version
	if versionMinorMaximum is not None:
		dataframe = cast(pandas.DataFrame, dataframe[dataframe['versionMinor'] <= versionMinorMaximum])

	# Remove duplicate ClassDefIdentifier
	# TODO think about how the function knows to remove _these_ duplicates
	dataframe = dataframe.sort_values('versionMinor', ascending=False).drop_duplicates('ClassDefIdentifier')

	if sortOn is not None:
		# TODO after changing the dataframe storage from csv to something smart, make this check smarter
		match str(dataframe[sortOn].dtype):
			case 'object':
				dataframe = dataframe.iloc[dataframe[sortOn].str.lower().argsort()]
			case _:
				dataframe = dataframe.sort_values(by=sortOn)

	# Select the requested columns, in the specified order
	dataframe = cast(pandas.DataFrame, dataframe[listElements])

	return dataframe.to_dict(orient='records')
