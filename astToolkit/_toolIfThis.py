from astToolkit import Be, DOT
from collections.abc import Callable
from typing import Any, cast
from typing_extensions import TypeIs
import ast

class IfThis:
	"""Predicate functions for AST node identification in the antecedent-action pattern.
	(AI generated docstring)

	Provides static methods that return predicate functions for identifying specific
	AST node types and patterns. These predicates serve as the `findThis` parameter
	in visitor classes (`NodeTourist` and `NodeChanger`), enabling precise node
	matching based on type, identifier, structure, and value criteria.

	The class implements the antecedent component of the antecedent-action pattern
	by providing composable type-safe predicates that can be combined with action
	functions from the `Then` class for comprehensive AST analysis and transformation.
	"""

	@staticmethod
	def is_argIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.arg] | bool]:
		"""Match function argument nodes with specific identifier.
		(AI generated docstring)

		Creates a predicate that identifies `ast.arg` nodes where the argument
		name matches the specified identifier. Used for matching function
		parameters: in function definitions.

		Parameters:

			identifier: The argument name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.arg]` for
				matching nodes, enabling type-safe argument node processing
		"""
		return lambda node: Be.arg(node) and IfThis.isIdentifier(identifier)(DOT.arg(node))

	@staticmethod
	def is_keywordIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.keyword] | bool]:
		"""Match keyword argument nodes with specific identifier.
		(AI generated docstring)

		Creates a predicate that identifies `ast.keyword` nodes where the keyword
		name matches the specified identifier. Used for matching named arguments
		in function calls.

		Parameters:

			identifier: The keyword argument name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.keyword]` for
				matching nodes, enabling type-safe keyword argument processing
		"""
		return lambda node: Be.keyword(node) and node.arg is not None and IfThis.isIdentifier(identifier)(node.arg)

	@staticmethod
	def isArgumentIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.arg | ast.keyword] | bool]:
		"""Match function or keyword argument nodes with specific identifier.
		(AI generated docstring)

		Creates a predicate that identifies either `ast.arg` or `ast.keyword` nodes
		where the argument name matches the specified identifier. Provides unified
		matching for both positional and keyword arguments.

		Parameters:

			identifier: The argument name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.arg | ast.keyword]`
				for matching nodes, enabling type-safe argument processing
		"""
		return lambda node: (Be.arg(node) or Be.keyword(node)) and node.arg is not None and IfThis.isIdentifier(identifier)(node.arg)

	@staticmethod
	def isAssignAndTargets0Is(targets0Predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], TypeIs[ast.AnnAssign] | bool]:
		"""Match assignment nodes where first target satisfies predicate.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Assign` nodes where the first
		assignment target matches the provided predicate function. Used for
		filtering assignments based on the structure or properties of their targets.

		Parameters:

			targets0Predicate: Function to test the first assignment target

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.AnnAssign]` for
				matching assignment nodes with qualifying first targets
		"""
		return lambda node: Be.Assign(node) and targets0Predicate(node.targets[0])

	@staticmethod
	def isAttributeIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:
		"""Match attribute access nodes with nested identifier chains.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Attribute` nodes where the base
		expression contains a nested chain ending with the specified identifier.
		Handles complex attribute access patterns like `obj.attr`, `obj[key].attr`,
		and `*obj.attr` where `obj` matches the identifier.

		Parameters:

			identifier: The base identifier to match in the attribute chain

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Attribute]` for
				matching attribute nodes with qualifying nested identifier chains
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute]:
			return Be.Attribute(node) and IfThis.isNestedNameIdentifier(identifier)(DOT.value(node))
		return workhorse

	@staticmethod
	def isAttributeName(node: ast.AST) -> TypeIs[ast.Attribute]:
		"""Match simple attribute access on name expressions.
		(AI generated docstring)

		Identifies `ast.Attribute` nodes where the base expression is a simple
		`ast.Name` node, representing direct attribute access patterns like
		`variable.attribute` rather than complex nested expressions.

		Parameters:

			node: AST node to test

		Returns:

			typeIs: `TypeIs[ast.Attribute]` for simple name-based attribute access
		"""
		return Be.Attribute(node) and Be.Name(DOT.value(node))

	@staticmethod
	def isAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute] | bool]:
		"""Match namespaced attribute access with specific namespace and attribute.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Attribute` nodes representing
		`namespace.identifier` patterns. Used for matching module attribute access,
		method calls on specific objects, and other qualified name patterns.

		Parameters:

			namespace: The base object or module name to match
			identifier: The attribute name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Attribute]` for
				matching namespaced attribute access nodes
		"""
		return lambda node: IfThis.isAttributeName(node) and IfThis.isNameIdentifier(namespace)(DOT.value(node)) and IfThis.isIdentifier(identifier)(DOT.attr(node))

	@staticmethod
	def isCallIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:
		"""Match function call nodes with specific function name.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Call` nodes where the called
		function is a simple name matching the specified identifier. Used for
		finding calls to specific functions like `print()`, `len()`, or custom functions.

		Parameters:

			identifier: The function name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Call]` for
				matching function call nodes with the specified name
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
			return IfThis.isCallToName(node) and IfThis.isIdentifier(identifier)(DOT.id(cast(ast.Name, DOT.func(node))))
		return workhorse

	@staticmethod
	def isCallAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.Call] | bool]:
		"""Match method call nodes with specific namespace and method name.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Call` nodes representing method
		calls on specific objects, like `obj.method()` or `module.function()`.
		Combines namespace and method name matching for precise call identification.

		Parameters:

			namespace: The object or module name to match
			identifier: The method or function name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Call]` for
				matching namespaced method call nodes
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Call] | bool:
			return Be.Call(node) and IfThis.isAttributeNamespaceIdentifier(namespace, identifier)(DOT.func(node))
		return workhorse

	@staticmethod
	def isCallToName(node: ast.AST) -> TypeIs[ast.Call]:
		"""Match function call nodes with simple name expressions.
		(AI generated docstring)

		Identifies `ast.Call` nodes where the called function is a simple `ast.Name`
		node rather than a complex expression. Used for distinguishing direct
		function calls from method calls or computed function expressions.

		Parameters:

			node: AST node to test

		Returns:

			typeIs: `TypeIs[ast.Call]` for simple name-based function calls
		"""
		return Be.Call(node) and Be.Name(DOT.func(node))

	@staticmethod
	def isClassDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.ClassDef] | bool]:
		"""Match class definition nodes with specific class name.
		(AI generated docstring)

		Creates a predicate that identifies `ast.ClassDef` nodes where the class
		name matches the specified identifier. Used for finding specific class
		definitions in AST traversal and transformation operations.

		Parameters:

			identifier: The class name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.ClassDef]` for
				matching class definition nodes with the specified name
		"""
		return lambda node: Be.ClassDef(node) and IfThis.isIdentifier(identifier)(DOT.name(node))

	@staticmethod
	def isConstant_value(value: Any) -> Callable[[ast.AST], TypeIs[ast.Constant] | bool]:
		"""Match constant nodes with specific value.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Constant` nodes containing the
		specified value. Used for finding specific literals like strings, numbers,
		booleans, or None values in the AST.

		Parameters:

			value: The constant value to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Constant]` for
				matching constant nodes with the specified value
		"""
		return lambda node: Be.Constant(node) and DOT.value(node) == value

	@staticmethod
	def isFunctionDefIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.FunctionDef] | bool]:
		"""Match function definition nodes with specific function name.
		(AI generated docstring)

		Creates a predicate that identifies `ast.FunctionDef` nodes where the
		function name matches the specified identifier. Essential for finding
		specific function definitions during AST analysis and transformation.

		Parameters:

			identifier: The function name to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.FunctionDef]` for
				matching function definition nodes with the specified name
		"""
		return lambda node: Be.FunctionDef(node) and IfThis.isIdentifier(identifier)(DOT.name(node))

	@staticmethod
	def isIdentifier(identifier: str) -> Callable[[str], TypeIs[str] | bool]:
		"""Match string values with specific identifier.
		(AI generated docstring)

		Creates a predicate that tests string equality with the specified identifier.
		This is a fundamental building block used by other predicate methods for
		comparing names, attributes, and other string-based AST components.

		Parameters:

			identifier: The string identifier to match

		Returns:

			predicateFunction: Function that returns `TypeIs[str]` for
				matching string values
		"""
		return lambda node: node == identifier

	@staticmethod
	def isIfUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.If] | bool]:
		"""Match if statements testing negation of namespaced attribute.
		(AI generated docstring)

		Creates a predicate that identifies `ast.If` nodes where the test condition
		is a unary `not` operation applied to a namespaced attribute access. Used
		for finding patterns like `if not obj.attr:` in conditional logic.

		Parameters:

			namespace: The object or module name in the attribute access
			identifier: The attribute name being tested

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.If]` for
				matching if statements with negated namespaced attribute tests
		"""
		return lambda node: (Be.If(node)
					and IfThis.isUnaryNotAttributeNamespaceIdentifier(namespace, identifier)(node.test))

	@staticmethod
	def isNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Name] | bool]:
		"""Match name nodes with specific identifier.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Name` nodes where the name
		matches the specified identifier. Fundamental for finding variable
		references, function names, and other simple identifiers in the AST.

		Parameters:

			identifier: The variable or name identifier to match

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Name]` for
				matching name nodes with the specified identifier
		"""
		return lambda node: Be.Name(node) and IfThis.isIdentifier(identifier)(DOT.id(node))

	@staticmethod
	def isNestedNameIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Attribute | ast.Starred | ast.Subscript] | bool]:
		"""Match complex expressions with nested identifier chains.
		(AI generated docstring)

		Creates a predicate that identifies complex AST nodes where nested
		attribute access, subscripting, or starred expressions ultimately resolve
		to a name matching the specified identifier. Handles patterns like
		`obj.attr`, `obj[key]`, `*obj`, and their combinations.

		Parameters:

			identifier: The base identifier to find in the nested expression chain

		Returns:

			predicateFunction: Function that returns `TypeIs` for matching
				nodes with nested identifier chains ending in the specified name
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Attribute | ast.Starred | ast.Subscript] | bool:
			return IfThis.isNameIdentifier(identifier)(node) or IfThis.isAttributeIdentifier(identifier)(node) or IfThis.isSubscriptIdentifier(identifier)(node) or IfThis.isStarredIdentifier(identifier)(node)
		return workhorse

	@staticmethod
	def isStarredIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Starred] | bool]:
		"""Match starred expression nodes with nested identifier chains.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Starred` nodes where the starred
		expression contains a nested chain ending with the specified identifier.
		Used for matching patterns like `*args`, `*obj.attr`, or `*container[key]`
		where the base resolves to the target identifier.

		Parameters:

			identifier: The base identifier to find in the starred expression chain

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Starred]` for
				matching starred nodes with qualifying nested identifier chains
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Starred]:
			return Be.Starred(node) and IfThis.isNestedNameIdentifier(identifier)(DOT.value(node))
		return workhorse

	@staticmethod
	def isSubscriptIdentifier(identifier: str) -> Callable[[ast.AST], TypeIs[ast.Subscript] | bool]:
		"""Match subscript expression nodes with nested identifier chains.
		(AI generated docstring)

		Creates a predicate that identifies `ast.Subscript` nodes where the
		subscripted expression contains a nested chain ending with the specified
		identifier. Used for matching patterns like `obj[key]`, `array[index]`,
		or `container.attr[key]` where the base resolves to the target identifier.

		Parameters:

			identifier: The base identifier to find in the subscript expression chain

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.Subscript]` for
				matching subscript nodes with qualifying nested identifier chains
		"""
		def workhorse(node: ast.AST) -> TypeIs[ast.Subscript]:
			return Be.Subscript(node) and IfThis.isNestedNameIdentifier(identifier)(DOT.value(node))
		return workhorse

	@staticmethod
	def isUnaryNotAttributeNamespaceIdentifier(namespace: str, identifier: str) -> Callable[[ast.AST], TypeIs[ast.UnaryOp] | bool]:
		"""Match unary not operations on namespaced attribute access.
		(AI generated docstring)

		Creates a predicate that identifies `ast.UnaryOp` nodes with `not` operators
		applied to namespaced attribute access expressions. Used for finding
		patterns like `not obj.attr` in boolean logic and conditional expressions.

		Parameters:

			namespace: The object or module name in the attribute access
			identifier: The attribute name being negated

		Returns:

			predicateFunction: Function that returns `TypeIs[ast.UnaryOp]` for
				matching unary not operations on namespaced attributes
		"""
		return lambda node: (Be.UnaryOp(node)
					and Be.Not(node.op)
					and IfThis.isAttributeNamespaceIdentifier(namespace, identifier)(node.operand))

	@staticmethod
	def matchesMeButNotAnyDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		"""Match nodes where predicate matches the node but no descendants.
		(AI generated docstring)

		Creates a predicate that identifies nodes where the provided predicate
		matches the current node but does not match any of its descendants.
		Used for finding the outermost occurrence of a pattern in nested structures.

		Parameters:

			predicate: Function to test against the node and its descendants

		Returns:

			predicateFunction: Function that returns `True` for nodes matching
				the predicate without matching descendants
		"""
		return lambda node: predicate(node) and IfThis.matchesNoDescendant(predicate)(node)

	@staticmethod
	def matchesNoDescendant(predicate: Callable[[ast.AST], bool]) -> Callable[[ast.AST], bool]:
		"""Match nodes where predicate matches no descendants.
		(AI generated docstring)

		Creates a predicate that identifies nodes where the provided predicate
		does not match any descendant nodes. Used for ensuring that a subtree
		does not contain specific patterns or constructs.

		Parameters:

			predicate: Function to test against descendant nodes

		Returns:

			predicateFunction: Function that returns `True` for nodes with
				no descendants matching the predicate
		"""
		def workhorse(node: ast.AST) -> bool:
			for descendant in ast.walk(node):
				if descendant is not node and predicate(descendant):
					return False
			return True
		return workhorse

	@staticmethod
	def unparseIs(astAST: ast.AST) -> Callable[[ast.AST], bool]:
		"""Match nodes with identical unparsed representation.
		(AI generated docstring)

		Creates a predicate that identifies AST nodes that produce the same
		string representation when unparsed as the provided reference AST.
		Used for structural comparison based on generated code rather than
		exact node equality.

		Parameters:

			astAST: Reference AST node to compare against

		Returns:

			predicateFunction: Function that returns `True` for nodes with
				matching unparsed string representation
		"""
		def workhorse(node: ast.AST) -> bool:
			return ast.unparse(node) == ast.unparse(astAST)
		return workhorse
