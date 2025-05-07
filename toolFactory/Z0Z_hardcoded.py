from pathlib import Path
from typing import TypeAlias as typing_TypeAlias
import ast

ast_Identifier: typing_TypeAlias = str
str_nameDOTname: typing_TypeAlias = str

pythonVersionMinorMinimum: int = 10
sys_version_infoMinimum: tuple[int, int] = (3, 10)
sys_version_infoTarget: tuple[int, int] = (3, 13)

class FREAKOUT(Exception): pass

# filesystem and namespace ===============================================
packageName: ast_Identifier = 'astToolkit'
moduleIdentifierPrefix: str = '_tool'
keywordArgumentsIdentifier: ast_Identifier = 'keywordArguments'

pathRoot = Path('/apps') / packageName
pathPackage = pathRoot / packageName
pathToolFactory = pathRoot / 'toolFactory'
pathTypeshed = pathRoot / 'typeshed' / 'stdlib'

pathFilenameDatabaseAST = pathToolFactory / 'databaseAST.csv'

fileExtension: str = '.py'
