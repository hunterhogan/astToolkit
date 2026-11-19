"""`parseLogicalPath2astModule` must parse the source that the import system finds for the logical path, so the expected value
parses the file at the module's spec origin with `ast.parse`, the parser that its docstring names through `Parameters_astParse`.

Expected text from `write_astModule` is hand-derived from its docstring and the `hunterMakesPy` defaults it names: `ast.unparse`
writes the module, `autoflake` removes every unused import, and `isort` sorts imports alphabetically with one line after them."""
from __future__ import annotations

from astToolkit import Make
from astToolkit.filesystem import parseLogicalPath2astModule, write_astModule
from importlib.util import find_spec
from io import StringIO
from pathlib import Path
from tests import assertComparable, assertEqualTo, messageTestFailure
from typing import Any, TYPE_CHECKING
import ast
import pytest

if TYPE_CHECKING:
	from hunterMakesPy import identifierDotAttribute

@pytest.mark.parametrize('type_comments', [False, True])
@pytest.mark.parametrize('logicalPath, package', [
	pytest.param('ast', None, id='ast')
	, pytest.param('pathlib', None, id='pathlib')
	, pytest.param('tests.dataSamples.sampleModuleForParsing', None, id='sampleModuleForParsing')
	, pytest.param('.sampleModuleForParsing', 'tests.dataSamples', id='sampleModuleForParsingRelative')
])
def test_parseLogicalPath2astModule(logicalPath: identifierDotAttribute, package: str | None, type_comments: bool) -> None:
	expected: ast.Module = ast.parse(
		Path(find_spec(logicalPath, package).origin).read_text(encoding='utf-8'), type_comments=type_comments)  # pyright: ignore[reportArgumentType, reportOptionalMemberAccess] # ty: ignore[invalid-argument-type, missing-union-attribute]
	assertComparable(parseLogicalPath2astModule(logicalPath, package, type_comments=type_comments), expected
		, parseLogicalPath2astModule.__name__, logicalPath, package, type_comments=type_comments)

parametersWrite_astModule: tuple[Any, ...] = (
	pytest.param(Make.Module([Make.FunctionDef(name='north', body=[Make.Return(Make.Constant(610))])]), None
		, 'def north():\n    return 610\n', id='importsNone')
	, pytest.param(ast.parse('import sys\nimport ast\n\ndef north():\n    return (ast, sys)'), None
		, 'import ast\nimport sys\n\ndef north():\n    return (ast, sys)\n', id='importsUnsorted')
	# `autoflake` removes each unused import line and keeps the blank line after it.
	, pytest.param(ast.parse('import os\nimport north\n\ndef south():\n    return 610'), None
		, '\ndef south():\n    return 610\n', id='importsUnused')
	# `autoflake` removes an unused standard-library import even when `remove_all_unused_imports` is `False`.
	, pytest.param(ast.parse('import os\nimport north\n\ndef south():\n    return 610'), {'autoflake': {'remove_all_unused_imports': False}}
		, 'import north\n\ndef south():\n    return 610\n', id='importsUnusedKeepThirdParty')
)

@pytest.mark.parametrize('astModule, settings, expected', parametersWrite_astModule, indirect=['astModule'])
def test_write_astModule(pathFilename: Path, astModule: ast.Module, settings: dict[str, dict[str, Any]] | None, expected: str) -> None:
	destination: Path | object = write_astModule(astModule, pathFilename, settings)
	assertEqualTo((destination, type(destination)), (pathFilename, type(pathFilename)), write_astModule.__name__, pathFilename, settings)
	assertEqualTo(pathFilename.read_text(encoding='utf-8'), expected, write_astModule.__name__, pathFilename, settings)

@pytest.mark.parametrize('astModule, settings, expected', parametersWrite_astModule, indirect=['astModule'])
def test_write_astModuleStream(astModule: ast.Module, settings: dict[str, dict[str, Any]] | None, expected: str) -> None:
	pathFilename: StringIO = StringIO()
	destination: object = write_astModule(astModule, pathFilename, settings)
	assert destination is pathFilename, messageTestFailure(destination, pathFilename, write_astModule.__name__, pathFilename, settings)
	assertEqualTo(pathFilename.getvalue(), expected, write_astModule.__name__, pathFilename, settings)

@pytest.mark.parametrize('astModule, identifierPackage', [
	pytest.param(Make.Module([Make.FunctionDef(name='north', body=[Make.Return(Make.Constant(610))])]), 'north', id='identifierPackageNorth'
		, marks=pytest.mark.xfail(strict=True, reason='`write_astModule` appends `identifierPackage` to the list in `settings_autoflakeDEFAULT`.'))
], indirect=['astModule'])
def test_write_astModuleDefaultsUnchanged(additional_importsDEFAULT: list[str], astModule: ast.Module, identifierPackage: str) -> None:
	additional_importsBefore: list[str] = [*additional_importsDEFAULT]
	write_astModule(astModule, StringIO(), identifierPackage=identifierPackage)
	assertEqualTo(additional_importsDEFAULT, additional_importsBefore, write_astModule.__name__, identifierPackage=identifierPackage)
