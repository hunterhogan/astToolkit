from ast import AST, Constant
from itertools import chain
from pathlib import Path
from types import GenericAlias
from typing import Any, cast
import ast
import pandas
import sys

"""
astClass == Slice, then base_typing_TypeAlias = _Slice
field == keywords, then fieldRename = list_keyword
astClass == 'ImportFrom' and field == 'names', then fieldRename = 'list_alias'
_Identifier in typeStub then typeStub_typing_TypeAlias = _Identifier
_Pattern in typeStub then typeStub_typing_TypeAlias = _Pattern
_Slice in typeStub then typeStub_typing_TypeAlias = _Slice
'list' in typeStub and any of ['cmpop', 'comprehension', 'expr', 'keyword', 'match_case', 'pattern', 'stmt', 'type_param', 'withitem', ] in typeStub, then list2Sequence = True
"""

pathFilenameDatabaseAST = Path('/apps/astToolkit/toolFactory/databaseAST.csv')
pathFilenameStubFile = Path('/apps/astToolkit/typeshed/stdlib/ast.pyi')

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
	Def=ast.ClassDef('j')
	c = astClass.__name__
	for node in ast.walk(ast.parse(pathFilenameStubFile.read_text())):
		if isinstance(node, ast.ClassDef) and node.name==c:
			Def=node
			del node
			break
	if not Def: raise Exception
	b = cast(Any, astClass.__base__).__name__
	ff = astClass._fields
	aa = astClass._attributes
	doc=astClass.__doc__
	d = 'deprecated' if bool(astClass.__doc__ and 'Deprecated' in astClass.__doc__) else None

	base_typing_TypeAlias = None
	typeStub_typing_TypeAlias=None
	isList2Sequence=False
	keywordArguments=None
	kwargAnnotation=None
	keywordArgumentsDefaultValue=None

	dictCtype:dict[str,str]={}
	if ff and doc and not d:
		listCstr=doc[len(c)+1:-1].split(',')
		for cstr in listCstr:
			t = cstr.split()[0]
			if '?' in t:
				t = t[0:-1] + ' | None'
			elif '*' in t:
				t = 'list(' + t[0:-1] + ')'
			dictCtype[cstr.split()[-1]] = t

	for f in ff:
		defaultValue__dict__=None
		if f in astClass.__dict__:
			defaultValue__dict__ = str(astClass.__dict__[f])
		fieldRename = fieldRenames.get(f, None)
		defaultValue = defaultValues.get(f, None)

		typeC = dictCtype.get(f)

		type_field_type=None
		if sys.version_info >= (3, 13) and f in astClass._field_types:
			t = astClass._field_types[f]
			if not isinstance(t,GenericAlias):
				try:
					type_field_type=t.__name__
				except Exception:
					pass
			if not type_field_type:
				type_field_type = str(t)
			del t

		typeStub=None
		for node in ast.walk(Def):
			if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id==f:
				typeStub=ast.unparse(node.annotation)
				break

		_attribute=None
		listRecords.append({
			'astClass': c, 'versionMajor': versionMajor, 'versionMinor': versionMinor, 'versionMicro': versionMicro, 'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias, 'field': f,
			'fieldRename': fieldRename, '_attribute': _attribute, 'typeC': typeC, 'typeStub': typeStub,
			'type_field_type': type_field_type, 'typeStub_typing_TypeAlias': typeStub_typing_TypeAlias,
			'list2Sequence': isList2Sequence, 'defaultValue__dict__': defaultValue__dict__, 'defaultValue': defaultValue,
			'keywordArguments': keywordArguments, 'kwargAnnotation': kwargAnnotation, 'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue, 'deprecated': d,
		})

	f=None
	fieldRename=None
	typeC=None
	typeStub=None
	type_field_type=None
	defaultValue=None
	for _attribute in aa:
		typeStub=int.__name__
		if 'end_' in _attribute:
			# end_lineno
			# end_col_offset
			typeStub=typeStub + ' | None'
		defaultValue__dict__=None
		if _attribute in astClass.__dict__:
			defaultValue__dict__ = str(astClass.__dict__[_attribute])

		listRecords.append({
			'astClass': c, 'versionMajor': versionMajor, 'versionMinor': versionMinor, 'versionMicro': versionMicro, 'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias, 'field': f,
			'fieldRename': fieldRename, '_attribute': _attribute, 'typeC': typeC, 'typeStub': typeStub,
			'type_field_type': type_field_type, 'typeStub_typing_TypeAlias': typeStub_typing_TypeAlias,
			'list2Sequence': isList2Sequence, 'defaultValue__dict__': defaultValue__dict__, 'defaultValue': defaultValue,
			'keywordArguments': keywordArguments, 'kwargAnnotation': kwargAnnotation, 'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue, 'deprecated': d,
		})

	_attribute=None
	typeStub=None
	defaultValue__dict__=None
	if not ff and not aa:
		listRecords.append({
			'astClass': c, 'versionMajor': versionMajor, 'versionMinor': versionMinor, 'versionMicro': versionMicro, 'base': b,
			'base_typing_TypeAlias': base_typing_TypeAlias, 'field': f,
			'fieldRename': fieldRename, '_attribute': _attribute, 'typeC': typeC, 'typeStub': typeStub,
			'type_field_type': type_field_type, 'typeStub_typing_TypeAlias': typeStub_typing_TypeAlias,
			'list2Sequence': isList2Sequence, 'defaultValue__dict__': defaultValue__dict__, 'defaultValue': defaultValue,
			'keywordArguments': keywordArguments, 'kwargAnnotation': kwargAnnotation, 'keywordArgumentsDefaultValue': keywordArgumentsDefaultValue, 'deprecated': d,
		})

def oneShotMakeDataframe(listData: list[dict[str, Any]]):
	global pathFilenameDatabaseAST
	dataframeTarget = pandas.DataFrame(listData, columns=list(listData[0].keys()))
	indexColumns = ['astClass', 'versionMajor', 'versionMinor', 'versionMicro', 'base', 'field', '_attribute', 'deprecated']
	dataframeTarget = dataframeTarget.set_index(indexColumns)  # pyright: ignore[reportUnknownMemberType]
	pathFilenameDatabaseAST = pathFilenameDatabaseAST.with_stem(pathFilenameDatabaseAST.stem + str(versionMinor))
	dataframeTarget.to_csv(pathFilenameDatabaseAST)

# oneShotMakeDataframe(listRecords)
