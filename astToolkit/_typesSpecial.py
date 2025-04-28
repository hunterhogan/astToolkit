import sys
from typing import Any, TypeAlias

yourPythonIsOld: TypeAlias = Any

if sys.version_info >= (3, 12):
	from ast import (
		ParamSpec as astDOTParamSpec,
		type_param as astDOTtype_param,
		TypeAlias as astDOTTypeAlias,
		TypeVar as astDOTTypeVar,
		TypeVarTuple as astDOTTypeVarTuple,
	)
else:
	astDOTParamSpec: TypeAlias = yourPythonIsOld
	astDOTtype_param: TypeAlias = yourPythonIsOld
	astDOTTypeAlias: TypeAlias = yourPythonIsOld
	astDOTTypeVar: TypeAlias = yourPythonIsOld
	astDOTTypeVarTuple: TypeAlias = yourPythonIsOld

if sys.version_info >= (3, 11):
	from ast import TryStar as astDOTTryStar
	from typing import TypedDict as TypedDict
	from typing import NotRequired as NotRequired
else:
	astDOTTryStar: TypeAlias = yourPythonIsOld
	try:
		from typing_extensions import TypedDict as TypedDict
		from typing_extensions import NotRequired as NotRequired
	except Exception:
		TypedDict = dict[yourPythonIsOld, yourPythonIsOld]
		from collections.abc import Iterable
		NotRequired: TypeAlias = Iterable
