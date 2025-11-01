import ast

def generateStubFile_prototypeFind(pathFilenameStub: str, astNodeNames: list[str], attributeNames: list[str]) -> None:
    stubContent = _generateStubHeader()
    stubContent += _generateFindClass(astNodeNames, attributeNames)

    with open(pathFilenameStub, 'w', encoding='utf-8') as writeStream:
        writeStream.write(stubContent)

def _generateStubHeader() -> str:
    return '''import ast
from typing import Any, overload

class Find:
    def __init__(self, listPathSteps: list[tuple[str, Any]] | None = None) -> None: ...
    def matches(self, nodeTarget: ast.AST) -> bool: ...
    def __call__(self, nodeTarget: ast.AST) -> bool: ...

    def equal(self, valueTarget: Any) -> 'Find': ...
    def at(self, indexTarget: int) -> 'Find': ...

'''

def _generateFindClass(astNodeNames: list[str], attributeNames: list[str]) -> str:
    stubMethods = []

    for nodeName in astNodeNames:
        stubMethods.append(f"    def {nodeName}(self) -> 'Find': ...")

    for attributeName in attributeNames:
        stubMethods.append(f"    def {attributeName}(self) -> 'Find': ...")

    uniqueMethods = sorted(set(stubMethods))

    methodsString = '\n'.join(uniqueMethods)
    methodsString += '\n    \n    def __getattr__(self, attributeName: str) -> \'Find\': ...\n'

    return methodsString

def getAstNodeNames() -> list[str]:
    astNodeNames = []
    for attributeName in dir(ast):
        astAttribute = getattr(ast, attributeName)
        if isinstance(astAttribute, type) and issubclass(astAttribute, ast.AST):
            astNodeNames.append(attributeName)
    return astNodeNames

def getAstAttributeNames() -> list[str]:
    attributeNames = set()

    for attributeName in dir(ast):
        astAttribute = getattr(ast, attributeName)
        if isinstance(astAttribute, type) and issubclass(astAttribute, ast.AST):
            for fieldName in astAttribute._fields:
                attributeNames.add(fieldName)

    return sorted(attributeNames)

def updateStubFile_prototypeFind() -> None:
    from pathlib import Path
    pathRoot = Path(__file__).parent
    pathFilenameStub = pathRoot / '_prototypeFind.pyi'

    astNodeNames = getAstNodeNames()
    attributeNames = getAstAttributeNames()

    generateStubFile_prototypeFind(str(pathFilenameStub), astNodeNames, attributeNames)

if __name__ == "__main__":
    updateStubFile_prototypeFind()
