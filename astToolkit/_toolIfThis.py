from astToolkit import Be
from collections.abc import Callable
from typing import Any
from typing_extensions import TypeIs
import ast

class IfThis:
	@staticmethod
	def is_argIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.arg] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.arg]:
			return Be.arg.argIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def is_keywordIdentifier(identifier: str | None) -> Callable[[ast.AST], TypeIs[ast.keyword] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.keyword]:
			return Be.keyword.argIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isAssignAndTargets0Is(targets0Predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], TypeIs[ast.Assign] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Assign] | bool:
			return Be.Assign(node) and targets0Predicate(node.targets[0])
		return workhorse

	@staticmethod
	def isAttributeIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute]:
			return Be.Attribute.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isAttributeName(node: ast.AST) -> TypeIs[ast.Attribute]:
		return Be.Attribute.valueIs(Be.Name)(node)

	@staticmethod
	def isAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute]:
			return Be.Attribute.valueIs(Be.Name.idIs(IfThis.isIdentifier(namespace)))(node) and Be.Attribute.attrIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isCallIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
			return Be.Call.funcIs(Be.Name.idIs(IfThis.isIdentifier(identifier)))(node)
		return workhorse

	@staticmethod
	def isCallAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
			return Be.Call.funcIs(IfThis.isAttributeNamespaceIdentifier(namespace, identifier))(node)
		return workhorse

	@staticmethod
	def isCallToName(node: ast.AST) -> TypeIs[ast.Call]:
		return Be.Call.funcIs(Be.Name)(node)

	@staticmethod
	def isClassDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.ClassDef] | bool:
			return Be.ClassDef.nameIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isConstant_value(value: Any) -> Callable[[ast.AST], TypeIs[ast.Constant] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Constant] | bool:
			return Be.Constant.valueIs(lambda thisAttribute: thisAttribute == value)(node)
		return workhorse

	@staticmethod
	def isFunctionDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.FunctionDef] | bool:
			return Be.FunctionDef.nameIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isIdentifier(identifier: str | None) -> Callable[[str | None], TypeIs[str] | bool]:
		def workhorse(node: str | None) -> TypeIs[str]:
			return node == identifier
		return workhorse

	@staticmethod
	def isIfUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.If] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.If] | bool:
			return Be.If.testIs(IfThis.isUnaryNotAttributeNamespaceIdentifier(namespace, identifier))(node)
		return workhorse

	@staticmethod
	def isNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Name] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Name]:
			return Be.Name.idIs(IfThis.isIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isNestedNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute | ast.Starred | ast.Subscript] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute | ast.Starred | ast.Subscript] | bool:
			return IfThis.isNameIdentifier(identifier)(node) or IfThis.isAttributeIdentifier(identifier)(node) or IfThis.isSubscriptIdentifier(identifier)(node) or IfThis.isStarredIdentifier(identifier)(node)
		return workhorse

	@staticmethod
	def isStarredIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Starred] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Starred]:
			return Be.Starred.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isSubscriptIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Subscript] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.Subscript]:
			return Be.Subscript.valueIs(IfThis.isNestedNameIdentifier(identifier))(node)
		return workhorse

	@staticmethod
	def isUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.UnaryOp] | bool]:
		def workhorse(node: ast.AST) -> TypeIs[ast.UnaryOp]:
			return (Be.UnaryOp(node)
					and Be.Not(node.op)
					and IfThis.isAttributeNamespaceIdentifier(namespace, identifier)(node.operand))
		return workhorse

	@staticmethod
	def matchesMeButNotAnyDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		def workhorse(node: ast.AST) -> bool:
			return predicate(node) and IfThis.matchesNoDescendant(predicate)(node)
		return workhorse

	@staticmethod
	def matchesNoDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		def workhorse(node: ast.AST) -> bool:
			for descendant in ast.walk(node):
				if descendant is not node and predicate(descendant):
					return False
			return True
		return workhorse

	@staticmethod
	def unparseIs(astAST: ast.AST) -> Callable[[ast.AST], bool]:
		def workhorse(node: ast.AST) -> bool:
			return ast.unparse(node) == ast.unparse(astAST)
		return workhorse
