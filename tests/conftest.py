"""SSOT for all tests."""
from __future__ import annotations

from astToolkit import packageSettings
from typing import TYPE_CHECKING
import datetime

if TYPE_CHECKING:
	from pathlib import Path

negativeTestsPerClass: int = 3
pathDataSamples: Path = packageSettings.pathPackage.parent / 'tests' / 'dataSamples'
stepSize: int = (32 - datetime.date.today().weekday()) * (datetime.date.today().day + 1)
