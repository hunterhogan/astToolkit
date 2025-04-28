from importlib import import_module as importlib_import_module
from inspect import getfile as inspect_getfile
from pathlib import Path
from tomli import load as tomli_load
import dataclasses

# TODO some of this can move to toolFactory because of the unusual nature of this package.
try:
	packageNamePACKAGING: str = tomli_load(Path("../pyproject.toml").open('rb'))["project"]["name"]
except Exception:
	packageNamePACKAGING = "astToolkit"

def getPathPackageINSTALLING() -> Path:
	pathPackage: Path = Path(inspect_getfile(importlib_import_module(packageNamePACKAGING)))
	if pathPackage.is_file():
		pathPackage = pathPackage.parent
	return pathPackage

@dataclasses.dataclass
class PackageSettings:

	fileExtension: str = dataclasses.field(default='.py', metadata={'evaluateWhen': 'installing'})
	"""Default file extension for generated code files."""

	packageName: str = dataclasses.field(default = packageNamePACKAGING, metadata={'evaluateWhen': 'packaging'})
	"""Name of this package, used for import paths and configuration."""

	pathPackage: Path = dataclasses.field(default_factory=getPathPackageINSTALLING, metadata={'evaluateWhen': 'installing'})
	"""Absolute path to the installed package directory."""

The = PackageSettings()

class FREAKOUT(Exception): pass
