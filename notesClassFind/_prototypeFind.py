# ruff: noqa
from collections.abc import Callable
from typing import Any
import ast

class Find:
	def __init__(self, queueOfGotten_attr: list[Callable[[Any], bool]] | None = None):
		self.queueOfGotten_attr = queueOfGotten_attr or []

	def __getattribute__(self, gotten_attrIdentifier: str):
		try:
			return object.__getattribute__(self, gotten_attrIdentifier)
		except AttributeError:
			pass

		if hasattr(ast, gotten_attrIdentifier):
			astClass = getattr(ast, gotten_attrIdentifier)
			if isinstance(astClass, type) and issubclass(astClass, ast.AST):
				Z0Z_Current = object.__getattribute__(self, 'queueOfGotten_attr')
				dontMutateMyQueue = Z0Z_Current + [lambda attrCurrent: isinstance(attrCurrent, astClass)]
				return Find(dontMutateMyQueue)

		def attribute_checker(attrCurrent: Any) -> bool:
			if hasattr(attrCurrent, gotten_attrIdentifier):
				return True
			return False

		Z0Z_Current = object.__getattribute__(self, 'queueOfGotten_attr')
		dontMutateMyQueue = Z0Z_Current + [attribute_checker]
		return Find(dontMutateMyQueue)

	def equal(self, valueTarget: Any):
		dontMutateMyQueue = self.queueOfGotten_attr + [lambda attrCurrent: attrCurrent == valueTarget]
		return Find(dontMutateMyQueue)

	def at(self, indexTarget: int):
		def index_checker(attrCurrent: Any) -> bool:
			try:
				attrCurrent[indexTarget]
				return True
			except (IndexError, TypeError, KeyError):
				return False

		dontMutateMyQueue = self.queueOfGotten_attr + [index_checker]
		return Find(dontMutateMyQueue)

	def __call__(self, node: ast.AST) -> bool:
		attrCurrent: Any = node

		for trueFalseCallable in self.queueOfGotten_attr:
			if not trueFalseCallable(attrCurrent):
				return False

		return True
