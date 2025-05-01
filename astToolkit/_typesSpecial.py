from typing import Any, TypeAlias
import sys

yourPythonIsOld: TypeAlias = Any

if sys.version_info >= (3, 11):
	from typing import TypedDict as TypedDict
	from typing import NotRequired as NotRequired
else:
	try:
		from typing_extensions import TypedDict as TypedDict
		from typing_extensions import NotRequired as NotRequired
	except Exception:
		TypedDict = dict[yourPythonIsOld, yourPythonIsOld]
		from collections.abc import Iterable
		NotRequired: TypeAlias = Iterable
