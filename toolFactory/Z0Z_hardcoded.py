from pathlib import Path
from typing import TypeAlias as typing_TypeAlias

ast_Identifier: typing_TypeAlias = str
fileExtension: str = '.py'
packageName: ast_Identifier = 'astToolkit'
pathRoot = Path('/apps') / packageName
pathPackage = pathRoot / packageName
pathTypeshed = pathRoot / 'typeshed' / 'stdlib'
str_nameDOTname: typing_TypeAlias = str
sys_version_infoMinimum: tuple[int, int] = (3, 10)
sys_version_infoTarget: tuple[int, int] = (3, 13)

listASTSubclasses: list[str] = ['_Slice', 'AST', 'binaryop', 'boolop', 'cmpop', 'excepthandler', 'expr_context', 'expr', 'mod', 'operator', 'pattern', 'stmt', 'type_ignore', 'type_param', 'unaryop',]

class FREAKOUT(Exception):
	pass
