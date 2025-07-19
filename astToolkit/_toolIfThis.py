"""Antecedent functions for identifying AST node patterns using the antecedent-action pattern.

(AI generated docstring)

This module provides the `IfThis` class, which contains static methods for generating predicates that match specific Python AST
node patterns. These predicates are designed for use with the antecedent-action pattern in the astToolkit package, enabling
type-safe, composable AST analysis and transformation workflows.

"""
from astToolkit import Be
from collections.abc import Callable
from typing import Any
from typing_extensions import TypeIs
import ast

class IfThis:
	"""Composable predicate generators for AST node identification in antecedent-action workflows.

	(AI generated docstring)

	The `IfThis` class provides static methods that return predicate functions for matching Python AST nodes based on type,
	identifier, structure, or value. These predicates are intended for use with the antecedent-action pattern, supporting
	type-safe AST traversal and transformation with the astToolkit package. Each method returns a callable suitable for use with
	`NodeTourist`, `NodeChanger`, or other toolkit components.

	"""

	@staticmethod
	def isAllOf[归个](*predicate: Callable[[ast.AST], TypeIs[归个] | bool]) -> Callable[[ast.AST], TypeIs[归个] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[归个] | bool:
			return all(antecedent(node) for antecedent in predicate)
		return workhorse

	@staticmethod
	def isAnyOf[归个](*predicate: Callable[[ast.AST], TypeIs[归个] | bool]) -> Callable[[ast.AST], TypeIs[归个] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[归个] | bool:
			return any(antecedent(node) for antecedent in predicate)
		return workhorse

	@staticmethod
	def is_argIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.arg]]:
		"""Return a predicate matching an `ast.arg` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The argument name to match against the `arg` (**arg**ument) field of an `ast.arg` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.arg]]
			Predicate returning `True` if the node is an `ast.arg` with the given identifier.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.arg]:
			return Be.arg.argIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def is_keywordIdentifier(identifier: str | None) -> Callable[[ast.AST], TypeIs[ast.keyword]]:
		"""Return a predicate matching an `ast.keyword` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str | None
			The keyword argument name to match against the `arg` (**arg**ument) field of an `ast.keyword` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.keyword]]
			Predicate returning `True` if the node is an `ast.keyword` with the given identifier.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.keyword]:
			return Be.keyword.argIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isAssignAndTargets0Is(targets0Predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], TypeIs[ast.Assign]]:
		"""Return a predicate matching an `ast.Assign` node whose first target matches a given predicate.

		(AI generated docstring)

		Parameters
		----------
		targets0Predicate : Callable[[ast.AST], bool]
			Predicate to apply to the first element of the `targets` field of an `ast.Assign` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Assign]]
			Predicate returning `True` if the node is an `ast.Assign` and its first target matches `targets0Predicate`.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Assign]:
			return Be.Assign(node) and targets0Predicate(node.targets[0])
		return workhorse

	@staticmethod
	def isAttributeIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute]]:
		"""Return a predicate matching an `ast.Attribute` node whose value matches a nested identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The identifier to match in the value of the `ast.Attribute` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Attribute]]
			Predicate returning `True` if the node is an `ast.Attribute` whose value matches the identifier.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute]:
			return Be.Attribute.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isAttributeName(node: ast.AST) -> TypeIs[ast.Attribute]:
		"""Return `True` if the node is an `ast.Attribute` whose value is an `ast.Name` node.

		(AI generated docstring)

		Parameters
		----------
		node : ast.AST
			The AST node to check.

		Returns
		-------
		result : TypeIs[ast.Attribute]
			`True` if the node is an `ast.Attribute` with a value of type `ast.Name`.
		"""
		return Be.Attribute.valueIs(Be.Name)(node)

	@staticmethod
	def isAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute]]:
		"""Return a predicate matching an `ast.Attribute` node with a specific namespace and identifier.

		(AI generated docstring)

		Parameters
		----------
		namespace : str
			The namespace identifier to match in the value's `id` (**id**entifier) field.
		identifier : str
			The attribute identifier to match in the `attr` (**attr**ibute) field.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Attribute]]
			Predicate returning `True` if the node is an `ast.Attribute` with the given namespace and identifier.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute]:
			return Be.Attribute.valueIs(Be.Name.idIs(IfThis.isIdentifier(namespace)))(node) and Be.Attribute.attrIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isCallIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call]]:
		"""Return a predicate matching an `ast.Call` node whose function is a `Name` with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The function name to match in the `id` (**id**entifier) field of the `Name` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Call]]
			Predicate returning `True` if the node is an `ast.Call` to the given identifier.
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Call]:
			return Be.Call.funcIs(Be.Name.idIs(IfThis.isIdentifier(identifier)))(node)
		return workhorse

	@staticmethod
	def isCallAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call]]:
		"""Return a predicate matching an `ast.Call` node whose function is an `ast.Attribute` with a specific namespace and identifier.

		(AI generated docstring)

		Parameters
		----------
		namespace : str
			The namespace identifier to match in the attribute's value.
		identifier : str
			The attribute identifier to match in the `attr` (**attr**ibute) field.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Call]]
			Predicate returning `True` if the node is an `ast.Call` whose function is an `ast.Attribute` with the given namespace and identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Call]:
			return Be.Call.funcIs(IfThis.isAttributeNamespaceIdentifier(namespace, identifier))(node)
		return workhorse

	@staticmethod
	def isCallToName(node: ast.AST) -> TypeIs[ast.Call]:
		"""Return `True` if the node is an `ast.Call` whose function is a `Name` node.

		(AI generated docstring)

		Parameters
		----------
		node : ast.AST
			The AST node to check.

		Returns
		-------
		result : TypeIs[ast.Call]
			`True` if the node is an `ast.Call` whose function is a `Name` node.

		"""
		return Be.Call.funcIs(Be.Name)(node)

	@staticmethod
	def isClassDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.ClassDef]]:
		"""Return a predicate matching an `ast.ClassDef` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The class name to match in the `name` field of the `ast.ClassDef` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.ClassDef]]
			Predicate returning `True` if the node is an `ast.ClassDef` with the given identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef]:
			return Be.ClassDef.nameIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isConstant_value(value: Any) -> Callable[[ast.AST], TypeIs[ast.Constant]]:
		"""Return a predicate matching an `ast.Constant` node with a specific value.

		(AI generated docstring)

		Parameters
		----------
		value : Any
			The value to match in the `value` field of the `ast.Constant` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Constant]]
			Predicate returning `True` if the node is an `ast.Constant` with the given value.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Constant]:
			return Be.Constant.valueIs(lambda thisAttribute: thisAttribute == value)(node)
		return workhorse

	@staticmethod
	def isFunctionDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.FunctionDef]]:
		"""Return a predicate matching an `ast.FunctionDef` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The function name to match in the `name` field of the `ast.FunctionDef` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.FunctionDef]]
			Predicate returning `True` if the node is an `ast.FunctionDef` with the given identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef]:
			return Be.FunctionDef.nameIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isIdentifier(identifier: str | None) -> Callable[[str | None], TypeIs[str]]:
		"""Return a predicate matching a string or None value to a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str | None
			The identifier to match.

		Returns
		-------
		predicate : Callable[[str | None], TypeIs[str]]
			Predicate returning `True` if the value matches the identifier.

		"""
		def workhorse(node: str | None) -> TypeIs[str]:
			return node == identifier
		return workhorse

	@staticmethod
	def isIfUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.If]]:
		"""Return a predicate matching an `ast.If` node whose test is a unary NOT of an attribute with a specific namespace and identifier.

		(AI generated docstring)

		Parameters
		----------
		namespace : str
			The namespace identifier to match in the attribute's value.
		identifier : str
			The attribute identifier to match in the `attr` (**attr**ibute) field.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.If]]
			Predicate returning `True` if the node is an `ast.If` whose test is a unary NOT of an attribute with the given namespace and identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.If]:
			return Be.If.testIs(IfThis.isUnaryNotAttributeNamespaceIdentifier(namespace, identifier))(node)
		return workhorse

	@staticmethod
	def isNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Name]]:
		"""Return a predicate matching an `ast.Name` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The identifier to match in the `id` (**id**entifier) field of the `ast.Name` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Name]]
			Predicate returning `True` if the node is an `ast.Name` with the given identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Name]:
			return Be.Name.idIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isNestedNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute | ast.Starred | ast.Subscript]]:
		"""Return a predicate matching an `ast.Name`, `ast.Attribute`, `ast.Subscript`, or `ast.Starred` node with a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The identifier to match in the node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Attribute | ast.Starred | ast.Subscript]]
			Predicate returning `True` if the node is a `Name`, `Attribute`, `Subscript`, or `Starred` with the given identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute | ast.Starred | ast.Subscript]:
			return IfThis.isNameIdentifier(identifier)(node) or IfThis.isAttributeIdentifier(identifier)(node) or IfThis.isSubscriptIdentifier(identifier)(node) or IfThis.isStarredIdentifier(identifier)(node)
		return workhorse

	@staticmethod
	def isStarredIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Starred]]:
		"""Return a predicate matching an `ast.Starred` node whose value matches a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The identifier to match in the value of the `ast.Starred` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Starred]]
			Predicate returning `True` if the node is an `ast.Starred` whose value matches the identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Starred]:
			return Be.Starred.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isSubscriptIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Subscript]]:
		"""Return a predicate matching an `ast.Subscript` node whose value matches a specific identifier.

		(AI generated docstring)

		Parameters
		----------
		identifier : str
			The identifier to match in the value of the `ast.Subscript` node.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.Subscript]]
			Predicate returning `True` if the node is a `Subscript` whose value matches the identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Subscript]:
			return Be.Subscript.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.UnaryOp]]:
		"""Return a predicate matching an `ast.UnaryOp` node representing a NOT operation on an attribute with a specific namespace and identifier.

		(AI generated docstring)

		Parameters
		----------
		namespace : str
			The namespace identifier to match in the attribute's value.
		identifier : str
			The attribute identifier to match in the `attr` (**attr**ibute) field.

		Returns
		-------
		predicate : Callable[[ast.AST], TypeIs[ast.UnaryOp]]
			Predicate returning `True` if the node is a `UnaryOp` representing NOT of an attribute with the given namespace and identifier.

		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.UnaryOp]:
			return (Be.UnaryOp(node)
					and Be.Not(node.op)
					and IfThis.isAttributeNamespaceIdentifier(namespace, identifier)(node.operand))
		return workhorse

	@staticmethod
	def matchesMeButNotAnyDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		"""Return a predicate that matches a node if it matches the given predicate, but no descendant matches it.

		(AI generated docstring)

		Parameters
		----------
		predicate : Callable[[ast.AST], bool]
			Predicate to match against the node and its descendants.

		Returns
		-------
		predicate : Callable[[ast.AST], bool]
			Predicate returning `True` if the node matches and no descendant matches.

		"""
		def workhorse(node: ast.AST) -> bool:
			return predicate(node) and IfThis.matchesNoDescendant(predicate)(node)
		return workhorse

	@staticmethod
	def matchesNoDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		"""Return a predicate that matches a node if no descendant matches the given predicate.

		(AI generated docstring)

		Parameters
		----------
		predicate : Callable[[ast.AST], bool]
			Predicate to check against all descendants of the node.

		Returns
		-------
		predicate : Callable[[ast.AST], bool]
			Predicate returning `True` if no descendant matches the predicate.

		"""
		def workhorse(node: ast.AST) -> bool:
			return all(not (descendant is not node and predicate(descendant)) for descendant in ast.walk(node))
		return workhorse

	@staticmethod
	def unparseIs(astAST: ast.AST) -> Callable[[ast.AST], bool]:
		"""Return a predicate that matches a node if its unparsed code matches the unparsed code of a given AST node.

		(AI generated docstring)

		Parameters
		----------
		astAST : ast.AST
			The AST node to compare against.

		Returns
		-------
		predicate : Callable[[ast.AST], bool]
			Predicate returning `True` if the node's unparsed code matches the given AST node's unparsed code.

		"""
		def workhorse(node: ast.AST) -> bool:
			return ast.unparse(node) == ast.unparse(astAST)
		return workhorse
