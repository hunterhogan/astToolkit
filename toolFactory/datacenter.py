import pandas
from toolFactory import pathFilenameDatabaseAST, pythonVersionMinorMinimum
from typing import Any, cast

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

def getElementsTypeAlias(deprecated: bool = False, versionMinorMaximum: int | None = None) -> list[dict[str, Any]]:
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
	dataframe['attributeVersionMinorMinimum'] = dataframe['attributeVersionMinorMinimum'].apply(
		lambda version: -1 if version <= pythonVersionMinorMinimum else version
	)

	dataframe = dataframe.sort_values(
		by=listElements,
		ascending=[True, False, True, True],
		key=lambda x: x.str.lower() if x.dtype == 'object' else x
	)

	dataframe = dataframe[listElements].drop_duplicates()

	grouped = dataframe.groupby(listElements[0:-1])['classAs_astAttribute'].apply(lambda x: ', '.join(map(str, x))).reset_index()
	valid_groups = grouped[grouped['attributeVersionMinorMinimum'].notnull()]
	dataframe = pandas.merge(dataframe, valid_groups, on=listElements[0:-1], how='outer', suffixes=('', '_updated'))
	dataframe['classAs_astAttribute'] = dataframe['classAs_astAttribute_updated'].combine_first(dataframe['classAs_astAttribute'])
	dataframe = dataframe.drop(columns=['classAs_astAttribute_updated'])
	dataframe = dataframe.drop_duplicates(subset=listElements)

	listDataframeRows = []
	for (_attribute, _TypeAliasSubcategory), subgroup in dataframe.groupby(['attribute', 'TypeAliasSubcategory']):
		listUniqueVersionMinor = subgroup['attributeVersionMinorMinimum'].unique()
		if len(listUniqueVersionMinor) == 1:
			listDataframeRows.append(subgroup)
		elif len(listUniqueVersionMinor) == 2:
			dataframeSubgroupLesserVersion = subgroup[subgroup['attributeVersionMinorMinimum'] == listUniqueVersionMinor.min()]
			dataframeSubgroupGreaterVersion = subgroup[subgroup['attributeVersionMinorMinimum'] == listUniqueVersionMinor.max()]
			# Process the lesser subgroup
			dataframeSubgroupLesserVersion = dataframeSubgroupLesserVersion.copy()
			dataframeSubgroupLesserVersion['classAs_astAttribute'] = dataframeSubgroupLesserVersion['classAs_astAttribute'].apply(lambda x: [x])
			# Process the greater subgroup
			combined = pandas.concat([dataframeSubgroupLesserVersion, dataframeSubgroupGreaterVersion])
			combined = combined.sort_values(by='classAs_astAttribute', key=lambda col: col.str.lower())
			combined_list = combined['classAs_astAttribute'].tolist()
			dataframeSubgroupGreaterVersion = dataframeSubgroupGreaterVersion.copy()
			dataframeSubgroupGreaterVersion['classAs_astAttribute'] = [combined_list]
			# Append processed subgroups
			listDataframeRows.append(dataframeSubgroupLesserVersion)
			listDataframeRows.append(dataframeSubgroupGreaterVersion)
		else:
			# Keep other groups unchanged
			listDataframeRows.append(subgroup)
	# Combine all processed groups and remove duplicates
	dataframe = pandas.concat(listDataframeRows).reset_index(drop=True)

	return dataframe.to_dict(orient='records') # type: ignore

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
