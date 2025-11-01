"""Sample Python module for testing parsePathFilename2astModule."""

def functionAlpha(parameterFirst: int, parameterSecond: str) -> str:
	"""A sample function for testing extractFunctionDef."""
	resultComputed = f"{parameterFirst}: {parameterSecond}"
	return resultComputed

def functionBeta() -> None:
	"""Another sample function."""
	pass

class ClassGamma:
	"""A sample class for testing extractClassDef."""

	def methodDelta(self) -> int:
		"""A method within the class."""
		return 13

class ClassEpsilon:
	"""Another sample class."""

	attributeZeta: str = "valueTest"
