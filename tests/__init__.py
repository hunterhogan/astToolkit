"""Test the astToolkit package.

Test package organization (in tests/):
- conftest.py: Fixtures: an isolated copy of a node for a target that mutates it, and a destination file for `write_astModule`
- conftestAnnex.py: `assertComparable`, the assertion helper for `ast` structure, re-exported here
- dataSamples/: Samples whose meaning does not depend on a test, named by content
- test_Be.py: Class identification by `Be`, and attribute predicates such as `Be.Name.idIs`
- test_Grab.py: Attribute and element transformations by `Grab`
- test_IfThis.py: Predicates built by `IfThis`
- test_Then.py: Actions built by `Then`
- test_changeDef.py: Definition indexes, inlining, and parameter removal
- test_filesystem.py: Parsing modules by logical path and writing modules
- test_transformationTools.py: Expression parsing, operand extraction, and find-and-replace by unparsed text
"""
from __future__ import annotations

import pytest

# Register assertion rewriting before importing `conftestAnnex`, so its plain `assert` statements report their operands.
# ruff: ignore[non-empty-init-module]
pytest.register_assert_rewrite('tests.conftestAnnex')

# isort: split
# ruff: ignore[module-import-not-at-top-of-file]
from hunterMakesPy.tests import assertEqualTo as assertEqualTo, messageTestFailure as messageTestFailure
# ruff: ignore[module-import-not-at-top-of-file]
from tests.conftestAnnex import assertComparable as assertComparable
