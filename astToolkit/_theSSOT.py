from importlib import import_module as importlib_import_module
from inspect import getfile as inspect_getfile
from pathlib import Path
import dataclasses

identifierPackage = 'astToolkit'

def getPathPackageINSTALLING() -> Path:
    pathPackage: Path = Path(inspect_getfile(importlib_import_module(identifierPackage)))
    if pathPackage.is_file():
        pathPackage = pathPackage.parent
    return pathPackage

@dataclasses.dataclass
class PackageSettings:
    fileExtension: str = dataclasses.field(default='.py')
    'Default file extension for generated code files.'
    packageName: str = dataclasses.field(default=identifierPackage)
    'Name of this package, used for import paths and configuration.'
    pathPackage: Path = dataclasses.field(default_factory=getPathPackageINSTALLING, metadata={'evaluateWhen': 'installing'})
    'Absolute path to the installed package directory.'
packageSettings = PackageSettings()