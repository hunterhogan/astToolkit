import pandas
from toolFactory import pathFilenameDatabaseAST

"""
rename 'astClass' to 'ClassDefIdentifier'

new column
classAs_astAttribute
value
ast.Attribute(ast.Name('ast'), ClassDefIdentifier)
put the actual ClassDefIdentifier in the string in the column.

new column
classVersionMinorMinimum
for each ClassDefIdentifier,
get unique values of 'versionMinor' and sort them,
validate the data: if the values are not contiguous from smallest to largest, give an error,
validate the data: if the largest value is not 13, give an error,
validate the data: if the smallest value is less than 9, give an error,
if the smallest value is 9, record -1 in the column,
else, record the smallest value in the column.

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
'astClass',
'versionMajor',
'versionMinor',
'versionMicro',
'base',
'base_typing_TypeAlias',
'field',
'fieldRename',
'_attribute',
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
'deprecated',
]

def getDataframe() -> pandas.DataFrame:
	indexColumns = ['astClass', 'versionMajor', 'versionMinor', 'versionMicro', 'base', 'field', '_attributes', 'typeString']
	dataframeTarget = pandas.read_csv(pathFilenameDatabaseAST, index_col=indexColumns) # pyright: ignore[reportUnknownMemberType]
	return dataframeTarget
