from ast import AST, Constant
from itertools import chain
from pathlib import Path
from types import GenericAlias
from typing import Any, cast
import ast
import pandas
import sys

pathFilenameDatabaseAST = Path('/apps/astToolkit/toolFactory/databaseAST.csv')

listASTClasses: list[type[AST]] = []
for astClass in sorted([AST, *chain(*map(lambda c: c.__subclasses__(), [AST, Constant, *AST.__subclasses__()]))], key=lambda c: c.__name__):
	if not issubclass(astClass, AST): continue
	listASTClasses.append(astClass)

versionMajor: int = sys.version_info.major
versionMinor: int = sys.version_info.minor
versionMicro: int = sys.version_info.micro

listRecords: list[dict[str, Any]] = []

fieldRenames = { "asname": "asName", "ctx": "context", "func": "callee", "orelse": "orElse", }

defaultValues = { "context": "ast.Load()", "level": "0", "type_ignores": "[]", "posonlyargs": "[]", "kwonlyargs": "[]", "defaults": "[]", "kw_defaults": "[None]", "decorator_list": "[]", "finalbody": "[]", }

for astClass in listASTClasses:
	c = astClass.__name__
	b = cast(Any, astClass.__base__).__name__
	ff = astClass._fields
	aa = astClass._attributes
	d = 'deprecated' if bool(astClass.__doc__ and 'Deprecated' in astClass.__doc__) else None

	base_typing_TypeAlias = None
	typeString_typing_TypeAlias=None
	isList2Sequence=False
	keywordArguments=None
	kwargAnnotation=None
	keywordArgumentsDefaultValue=None

	if sys.version_info >= (3, 13):
		try:
			field_types_dict: dict[str, Any] = astClass._field_types
		except Exception:
			field_types_dict = {}

	for field, fieldType in field_types_dict.items():
		typeString: str | None = None
		if not isinstance(fieldType, GenericAlias):
			try:
				typeString = fieldType.__name__
			except Exception as ERRORmessage:
				typeString = str(fieldType)
		else:
			typeString = str(fieldType)

		fieldRename = fieldRenames.get(field, None)

		defaultValue = defaultValues.get(field, None)

		_attribute=None

		listRecords.append({
			'astClass': c,
			'versionMajor': versionMajor,
			'versionMinor': versionMinor,
			'versionMicro': versionMicro,
			'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias,
			'field': field,
			'fieldRename': fieldRename,
			'_attribute': _attribute,
			'typeString': typeString,
			'typeString_typing_TypeAlias': typeString_typing_TypeAlias,
			'list2Sequence': isList2Sequence,
			'defaultValue': defaultValue,
			'keywordArguments': keywordArguments,
			'kwargAnnotation': kwargAnnotation,
			'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue,
			'deprecated': d,
		})

	field=None
	fieldRename=None
	typeString=int.__name__
	defaultValue=None
	for _attribute in aa:
		listRecords.append({
			'astClass': c,
			'versionMajor': versionMajor,
			'versionMinor': versionMinor,
			'versionMicro': versionMicro,
			'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias,
			'field': field,
			'fieldRename': fieldRename,
			'_attribute': _attribute,
			'typeString': typeString,
			'typeString_typing_TypeAlias': typeString_typing_TypeAlias,
			'list2Sequence': isList2Sequence,
			'defaultValue': defaultValue,
			'keywordArguments': keywordArguments,
			'kwargAnnotation': kwargAnnotation,
			'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue,
			'deprecated': d,
		})

	_attribute=None

	if not field_types_dict and not aa:
		listRecords.append({
			'astClass': c,
			'versionMajor': versionMajor,
			'versionMinor': versionMinor,
			'versionMicro': versionMicro,
			'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias,
			'field': field,
			'fieldRename': fieldRename,
			'_attribute': _attribute,
			'typeString': typeString,
			'typeString_typing_TypeAlias': typeString_typing_TypeAlias,
			'list2Sequence': isList2Sequence,
			'defaultValue': defaultValue,
			'keywordArguments': keywordArguments,
			'kwargAnnotation': kwargAnnotation,
			'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue,
			'deprecated': d,
		})

def oneShotMakeDataframe(listData: list[dict[str, Any]]):
	global pathFilenameDatabaseAST
	dataframeTarget = pandas.DataFrame(listData, columns=list(listData[0].keys()))
	pathFilenameDatabaseAST = pathFilenameDatabaseAST.with_stem(pathFilenameDatabaseAST.stem + str(versionMinor))
	dataframeTarget.to_csv(pathFilenameDatabaseAST) # type: ignore

oneShotMakeDataframe(listRecords)

def getDataframe():
	pass

"""
See /apps/astToolkit/typeshed/stdlib/ast.pyi for information about the following.
column: 'base_typing_TypeAlias'
I think _Slice is the only one.

column: typeString_typing_TypeAlias
_Identifier, _Pattern, _Slice, _SliceAttributes
The typeString reports the primitive name or the non-alias name no matter what is written in the stub file.
This column tracks how the TypeAlias is used in typeshed, so, for example, only record "_Pattern" if it is used for that field in that class.
Furthermore, this is not the same as my TypeAlias, such as `ast_Identifier`.
"""
"""
Use apps/astToolkit/toolFactory/astFactory.py, especially the `match attributeIdentifier` code block as the source of the following
column: list2Sequence
bool
False

column: fieldRename
string
If I renamed the field, such as `attributeIdentifier = 'callee'`

column: defaultValue
string representations of various types
if I set a default value

column: keywordArguments
bool
If I treat the field as a `**keywordArguments` in `Make`. Look for `continue` in the case of `match attributeIdentifier`.
Also, all _attribute should have this column set to True.

column: kwargAnnotation
string
If I treated the field as a `**keywordArguments` in `Make`, I might have changed the `**keywordArguments` annotation, such as `ast.Name('intORstr')`.
All _attribute should have this column set to "int".
The normal annotation is `int`, so for this example, store "str" in this column.

column: keywordArgumentsDefaultValue
string or int
For example, `cast(ast.Call, cast(ast.Return, cast(ast.FunctionDef, ClassDefMake.body[-1]).body[0]).value).keywords.append(ast.keyword(attributeIdentifier, ast.Constant(0)))`
"""
