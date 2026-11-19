from __future__ import annotations

from copy import copy, deepcopy, replace
from hunterMakesPy.kitFilesystem import settings_autoflakeDEFAULT
from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
	from pathlib import Path
	import ast

@pytest.fixture
def node(request: pytest.FixtureRequest) -> ast.AST:
	"""A copy of the parametrized node, for a target that reassigns the fields of the node it receives.

	The copy is shallow: `deepcopy` fails on Python 3.15.2 for a sample such as `ast.keyword(arg=None, value=...)`.
	"""
	return replace(request.param)

@pytest.fixture
def astModule(request: pytest.FixtureRequest) -> ast.Module:
	"""An isolated copy of the parametrized module, for a target that mutates the module it receives."""
	return deepcopy(request.param)

@pytest.fixture
def FunctionDef(request: pytest.FixtureRequest) -> ast.FunctionDef:
	"""An isolated copy of the parametrized function definition, for a target that mutates the definition it receives."""
	return deepcopy(request.param)

@pytest.fixture
def pathFilename(tmp_path: Path) -> Path:
	"""An absolute path to a Python file that does not yet exist, in a directory that this fixture owns."""
	return tmp_path / 'module.py'

@pytest.fixture
def additional_importsDEFAULT(monkeypatch: pytest.MonkeyPatch) -> list[str]:
	"""A copy of `settings_autoflakeDEFAULT['additional_imports']` that replaces the original until the test ends."""
	monkeypatch.setitem(settings_autoflakeDEFAULT, 'additional_imports', copy(settings_autoflakeDEFAULT['additional_imports']))
	return settings_autoflakeDEFAULT['additional_imports']  # pyright: ignore[reportReturnType] # ty: ignore[invalid-explicit-return]
