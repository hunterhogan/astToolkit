from pathlib import Path
from typing import TypeAlias as typing_TypeAlias

ast_Identifier: typing_TypeAlias = str
packageName: ast_Identifier = 'astToolkit'
pathPackage = Path('/apps') / packageName
pathTypeshed = pathPackage / 'typeshed/stdlib'
sys_version_infoMinimum: tuple[int, int] = (3, 10)
sys_version_infoTarget: tuple[int, int] = (3, 13)

class FREAKOUT(Exception):
	pass
