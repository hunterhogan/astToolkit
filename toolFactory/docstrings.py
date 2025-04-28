docstringWarning: str = """This file is generated automatically, so changes to this file will be lost."""

ClassDefDocstringBe: str = (
	"""
	Provide type-guard functions for safely verifying AST node types during manipulation.

	The be class contains static methods that perform runtime type verification of AST nodes, returning TypeGuard
	results that enable static type checkers to narrow node types in conditional branches. These type-guards:

	1. Improve code safety by preventing operations on incompatible node types.
	2. Enable IDE tooling to provide better autocompletion and error detection.
	3. Document expected node types in a way that is enforced by the type system.
	4. Support pattern-matching workflows where node types must be verified before access.

	When used with conditional statements, these type-guards allow for precise, type-safe manipulation of AST nodes
	while maintaining full static type checking capabilities, even in complex transformation scenarios.
	"""
	)

ClassDefDocstringDOT: str = (
	"""
	Access attributes and sub-nodes of AST elements via consistent accessor methods.

	The DOT class provides static methods to access specific attributes of different types of AST nodes in a consistent
	way. This simplifies attribute access across various node types and improves code readability by abstracting the
	underlying AST structure details.

	DOT is designed for safe, read-only access to node properties, unlike the grab class which is designed for modifying
	node attributes.
	"""
)

ClassDefDocstringGrab: str = (
	"""
	Modify specific attributes of AST nodes while preserving the node structure.

	The grab class provides static methods that create transformation functions to modify specific attributes of AST
	nodes. Unlike DOT which provides read-only access, grab allows for targeted modifications of node attributes without
	replacing the entire node.

	Each method returns a function that takes a node, applies a transformation to a specific attribute of that node, and
	returns the modified node. This enables fine-grained control when transforming AST structures.
	"""
)

ClassDefDocstringMake: str = (
	"""
	Almost all parameters described here are only accessible through a method's `**keywordArguments` parameter.

	Parameters:
		context (ast.Load()): Are you loading from, storing to, or deleting the identifier? The `context` (also, `ctx`) value is `ast.Load()`, `ast.Store()`, or `ast.Del()`.
		col_offset (0): int Position information specifying the column where an AST node begins.
		end_col_offset (None): int|None Position information specifying the column where an AST node ends.
		end_lineno (None): int|None Position information specifying the line number where an AST node ends.
		level (0): int Module import depth level that controls relative vs absolute imports. Default 0 indicates absolute import.
		lineno: int Position information manually specifying the line number where an AST node begins.
		kind (None): str|None Used for type annotations in limited cases.
		type_comment (None): str|None "type_comment is an optional string with the type annotation as a comment." or `# type: ignore`.
		type_params: list[ast.type_param] Type parameters for generic type definitions.

	The `ast._Attributes`, lineno, col_offset, end_lineno, and end_col_offset, hold position information; however, they are, importantly, _not_ `ast._fields`.
	"""
	)
