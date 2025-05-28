"""
AST Container Classes for Python Code Generation and Transformation

This module provides specialized container classes that organize AST nodes, imports, and program structure for code
generation and transformation. These classes form the organizational backbone of the code generation system, enabling:

1. Tracking and managing imports with LedgerOfImports.
2. Packaging function definitions with their dependencies via IngredientsFunction.
3. Structuring complete modules with IngredientsModule.

Together, these container classes implement a component-based architecture for programmatic generation of
high-performance code. They maintain a clean separation between structure and content, allowing transformations to be
applied systematically while preserving relationships between code elements.

The containers work in conjunction with transformation tools that manipulate the contained AST nodes to implement
specific optimizations and transformations.
"""

from astToolkit import identifierDotAttribute, Make
from collections import defaultdict
from collections.abc import Sequence
from Z0Z_tools import updateExtendPolishDictionaryLists
import ast
import dataclasses

# I am not claiming `LedgerOfImports` is perfect or the best, but I generally like it and I don't know of a better way.
# But, some of my opinion might be due to the Ikea-effect: this is the first and only object-oriented class I've created.
# Because I fricken hate OOP.
class LedgerOfImports:
	"""
	Manage import dependencies when building Python modules programmatically.

	Think of this as a smart notebook that keeps track of which Python libraries and modules 
	your generated code needs to import. When you're building Python code from scratch or 
	transforming existing code, you need to ensure all the necessary `import` and `from module import name` 
	statements are included in the final result.

	The Ledger stores information about import dependencies and can later generate the actual 
	import statements that should appear at the top of your Python file. It handles:

	- Recording that your code needs `import ast` or `from collections import defaultdict`
	- Consolidating multiple requests for the same imports to avoid duplicates
	- Organizing imports in a clean, standardized format
	- Removing import dependencies that are no longer needed
	- Merging import requirements from multiple code components

	This is especially useful when you're extracting functions from one module, transforming them,
	and reassembling them into a new module - you need to track which imports the original 
	functions depended on and include them in the generated code.

	Example workflow:
	1. Parse existing Python code and capture its import dependencies
	2. Transform or combine code from multiple sources
	3. Generate clean import statements for the final module
	4. Write a complete, executable Python file
	"""
	
	# 3 basic actions: add, remove, export
	# Existing syntax for adding imports:
		# ast.AST, walk. Wait, the logic in `addAst` is not necessary now that I have `walkThis`. No, no, walkThis is built on `addAst`. 
		# ast.Import | ast.ImportFrom
		# str as parameters
		# LedgerOfImports
	# New syntax for adding imports:
		# str represention, including multiline strings, of an import statement, e.g., `"from collections.abc import Sequence"`
		# Iterable[ast.AST] (includes ast.Import | ast.ImportFrom)
		# Iterable[str representation]
	# In general, the public method will, at most, convert the input in some way
	# However, it is nearly certain that I will instead use internal methods to convert the input to a standardized form.
	# Internally, I really only need one code block to add the data to the correct data structure.
	# Furthermore, I can use the conversion logic on requests to remove imports.
	# Then have one logic block for removing imports.
	# The net effect will be to increase the options for the user to add or remove imports, while keeping the internal logic simple and consistent.
	# Existing export options:
		# list of ast.Import | ast.ImportFrom
		# list of str representation of only the module names, e.g., `['collections.abc', 'ast']`: specifically for 
		# use with `autoflake.fix_code(additional_imports=)`, which now seems like an overly specific use case. BUT, 
		# I decided to not created methods for "remove all except" because existing tools like `autoflake` can remove 
		# unused imports. So, it's not really overly specific.

	# TODO Think about how to resolving (`makeList_ast`) the ledger of imports and remove self-referential imports, 
	# and I now understand why I have not yet done this: the ledger is ignorant of the package/module context in which it is used.
	# idea: an optional property of the ledger such as `dotModule: identifierDotAttribute`, so the ledger "knows" the context in which it is used.
	# Interestingly, because ast.Module does not have a `name` attribute, `IngredientsModule` does not have a `name` attribute either.
	# I have been conflicted about how to handle that. I would _not_ want to duplicate information in the ledger and in `IngredientsModule`.
	# But because `LedgerOfImports` is part of `IngredientsModule`, it might be a natural place to store the package, logical path, 
	# and module information for `IngredientsModule`. `LedgerOfImports` doesn't currently have sophisticated tools for handling logical paths,
	# but that's in part because I hadn't realized the context problem before now. And between `LedgerOfImports` and `IngredientsModule`, 
	# that logic should be in `LedgerOfImports`, because it is the one that handles the imports.
	# NOTE this feels like an issue that someone else has already solved.

	def __init__(self, startWith: ast.AST | None = None, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Create a new import dependency tracker.

		Parameters:
			startWith: Parse this AST node to automatically capture any import dependencies it contains.
				Useful when extracting code that already has imports you want to preserve.
			type_ignores: Additional type ignore directives to include in the generated module.
		"""
		self._dictionaryImportFrom: dict[identifierDotAttribute, list[tuple[str, str | None]]] = defaultdict(list)
		self._listImport: list[identifierDotAttribute] = []
		self.type_ignores: list[ast.TypeIgnore] = [] if type_ignores is None else list(type_ignores)
		if startWith:
			self.walkThis(startWith)

	def addAst(self, astImport____: ast.Import | ast.ImportFrom, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Record import dependencies from an existing import statement node.

		This method extracts import dependency information from AST nodes that represent 
		import statements in parsed Python code. Use this when you have existing import 
		statements and want to capture their dependency information for later use.

		Parameters:
			astImport____: An AST node representing either `import module` or `from module import name` 
				statements from parsed Python code.
			type_ignores: Additional type ignore directives associated with this import.
		
		Raises:
			ValueError: If the AST node is not an import statement type.
		"""
		match astImport____:
			case ast.Import():
				for alias in astImport____.names:
					self._listImport.append(alias.name)
			case ast.ImportFrom():
				# TODO fix the mess created by `None` means '.'. I need a `str_nameDOTname` to replace '.', 
				# of course this involves the same package/module context problem as above.
				if astImport____.module is None:
					astImport____.module = '.'
				for alias in astImport____.names:
					self._dictionaryImportFrom[astImport____.module].append((alias.name, alias.asname))
			case _:
				raise ValueError(f"I received {type(astImport____) = }, but I can only accept {ast.Import} and {ast.ImportFrom}.")
		if type_ignores:
			self.type_ignores.extend(type_ignores)

	def addImport_asStr(self, dotModule: identifierDotAttribute, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Record a dependency on a module that should be imported directly.
		
		This records that your generated code needs an `import module` statement.
		For example, calling `addImport_asStr("ast")` records that the final code 
		should include `import ast`.

		Parameters:
			dotModule: The module name to import (e.g., "ast", "collections.abc", "os.path").
			type_ignores: Additional type ignore directives associated with this import.
		"""
		self._listImport.append(dotModule)
		if type_ignores:
			self.type_ignores.extend(type_ignores)

	def addImportFrom_asStr(self, dotModule: identifierDotAttribute, name: str, asName: str | None = None, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Record a dependency on a specific item from a module.
		
		This records that your generated code needs a `from module import name` statement.
		For example, calling `addImportFrom_asStr("collections", "defaultdict")` records 
		that the final code should include `from collections import defaultdict`.

		Parameters:
			dotModule: The module to import from (e.g., "collections", "os.path").
			name: The specific item to import from that module (e.g., "defaultdict", "join").
			asName: Optional alias for the imported item (e.g., "dd" in `from collections import defaultdict as dd`).
			type_ignores: Additional type ignore directives associated with this import.
		"""
		self._dictionaryImportFrom[dotModule].append((name, asName))
		if type_ignores:
			self.type_ignores.extend(type_ignores)

	def exportListModuleIdentifiers(self) -> list[identifierDotAttribute]:
		"""
		Get a list of all module names that have recorded dependencies.
		
		Returns all module names that have been recorded for import, whether through 
		direct imports (`import module`) or from-imports (`from module import name`).
		This is useful for tools like autoflake that need to know which modules
		should be preserved during import optimization.

		Returns:
			listModuleIdentifiers:
			Sorted list of module names that have import dependencies recorded.
		"""
		listModuleIdentifiers: list[identifierDotAttribute] = list(self._dictionaryImportFrom.keys())
		listModuleIdentifiers.extend(self._listImport)
		return sorted(set(listModuleIdentifiers))

	def makeList_ast(self) -> list[ast.ImportFrom | ast.Import]:
		"""
		Generate the actual import statement nodes for the final Python module.
		
		This converts all recorded import dependencies into the AST nodes that represent 
		import statements in Python code. The generated statements will appear at the top 
		of your final Python file when the module is written. Import statements are 
		automatically sorted and deduplicated.

		Returns:
			listImportFrom:
			List of AST nodes representing import statements, ready to be placed in a Python module.
			These nodes can be converted to Python source code like "import ast" and 
			"from collections import defaultdict".
		"""
		listImportFrom: list[ast.ImportFrom] = []
		for dotModule, list_nameTuples in sorted(self._dictionaryImportFrom.items()):
			list_nameTuples: list[tuple[str, str | None]] = sorted(list(set(list_nameTuples)), key=lambda nameTuple: nameTuple[0])
			list_alias: list[ast.alias] = []
			for name, asName in list_nameTuples:
				list_alias.append(Make.alias(name, asName))
			if list_alias:
				listImportFrom.append(Make.ImportFrom(dotModule, list_alias))
		list_astImport: list[ast.Import] = [Make.Import(dotModule) for dotModule in sorted(set(self._listImport))]
		return listImportFrom + list_astImport
	def removeImportFromModule(self, dotModule: identifierDotAttribute) -> None:
		"""
		Remove all recorded dependencies on a specific module.
		
		This removes all import dependency records for the specified module, whether from 
		direct imports or from-imports. After calling this method, no import statements 
		related to this module will be generated in the final code.

		Parameters:
			dotModule: The module name to remove all dependencies for (e.g., "ast", "collections.abc").
		"""
		self.removeImportFrom(dotModule, None, None)
	def removeImportFrom(self, dotModule: identifierDotAttribute, name: str | None, asName: str | None = None) -> None:
		"""
		Remove specific import dependency records from a module.
		
		This provides fine-grained control over which import dependencies to remove. 
		You can remove all dependencies from a module, specific items, or items with 
		specific aliases.

		Parameters:
			dotModule: The module name containing the import dependencies to modify.
			name: The specific item name to remove. If None, removes based on asName matching.
			asName: The specific alias to remove. If None with a name, removes exact name matches.

		Removal behavior:
		- name=None, asName=None: Remove all dependency records for the module
		- name="item", asName=None: Remove records for importing "item" without an alias  
		- name="item", asName="alias": Remove records for importing "item as alias"
		- name=None, asName="alias": Remove any record that uses "alias" as the imported name
		"""
		if dotModule in self._dictionaryImportFrom:
			if name is None and asName is None:
				# Remove all entries for `dotModule`
				self._dictionaryImportFrom.pop(dotModule)
			else:
				if name is None:
					def conditionalFilter(entry_name: str, entry_asName: str | None) -> bool:
						return not (entry_asName == asName) and not (entry_asName is None and entry_name == asName)
				else:
					def conditionalFilter(entry_name: str, entry_asName: str | None) -> bool:
						return not (entry_name == name and entry_asName == asName)
				self._dictionaryImportFrom[dotModule] = [(entry_name, entry_asName) for entry_name, entry_asName in self._dictionaryImportFrom[dotModule] if conditionalFilter(entry_name, entry_asName)]
				if not self._dictionaryImportFrom[dotModule]:
					self._dictionaryImportFrom.pop(dotModule)
	def update(self, *fromLedger: 'LedgerOfImports') -> None:
		"""
		Merge import dependencies from other Ledgers into this one.
		
		This combines import dependency records from multiple sources, which is useful when 
		assembling code from different modules or functions. Duplicate dependencies are 
		automatically handled - the same import will only be recorded once.

		Parameters:
			*fromLedger: One or more other LedgerOfImports instances to merge dependencies from.
		"""
		updatedDictionary: dict[str, list[tuple[str, str | None]]] = updateExtendPolishDictionaryLists(self._dictionaryImportFrom, *(ledger._dictionaryImportFrom for ledger in fromLedger), destroyDuplicates=True, reorderLists=True)
		self._dictionaryImportFrom = defaultdict(list, updatedDictionary)
		for ledger in fromLedger:
			self._listImport.extend(ledger._listImport)
			self.type_ignores.extend(ledger.type_ignores)

	def walkThis(self, walkThis: ast.AST, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Automatically discover and record import dependencies from existing code.
		
		This method analyzes parsed Python code (AST nodes) and automatically records 
		any import statements it finds. This is the easiest way to capture import 
		dependencies when working with existing code that you want to transform or extract.

		Parameters:
			walkThis: Any AST node (like a parsed module, function, or code block) to scan for imports.
			type_ignores: Additional type ignore directives to include.
		"""
		for nodeBuffalo in ast.walk(walkThis):
			if isinstance(nodeBuffalo, (ast.Import, ast.ImportFrom)):
				self.addAst(nodeBuffalo)
		if type_ignores:
			self.type_ignores.extend(type_ignores)

# Inspiration for adding new methods to `LedgerOfImports`:
# ledgerOfImports = LedgerOfImports()
# ledgerOfImports = LedgerOfImports(ast.parse("from types import EllipsisType, NotImplementedType; from typing import Any, TypeAlias as typing_TypeAlias, TypedDict, TypeVar as typing_TypeVar; import ast; import sys"))
# ledgerOfImports.walkThis(ast.parse("from types import EllipsisType, NotImplementedType"))
# ledgerOfImports = LedgerOfImports(ast.parse("""
# from types import EllipsisType, NotImplementedType
# from typing import Any, TypeAlias as typing_TypeAlias, TypedDict, TypeVar as typing_TypeVar
# import ast
# import sys""")
# )

# I don't particularly like `IngredientsFunction`, except that it is well integrated with `LedgerOfImports` and `IngredientsModule`.
@dataclasses.dataclass
class IngredientsFunction:
	"""
	Package a function definition with its import dependencies for code generation.

	IngredientsFunction encapsulates an AST function definition along with all the imports required for that function to
	operate correctly. This creates a modular, portable unit that can be:

	1. Transformed independently (e.g., by applying Numba decorators).
	2. Transplanted between modules while maintaining dependencies.
	3. Combined with other functions to form complete modules.
	4. Analyzed for optimization opportunities.

	This class forms the primary unit of function manipulation in the code generation system, enabling targeted
	transformations while preserving function dependencies.

	Parameters:
		astFunctionDef: The AST representation of the function definition
		imports: Import statements needed by the function
		type_ignores: Type ignore comments associated with the function
	"""
	astFunctionDef: ast.FunctionDef
	imports: LedgerOfImports = dataclasses.field(default_factory=LedgerOfImports)
	type_ignores: list[ast.TypeIgnore] = dataclasses.field(default_factory=lambda: list[ast.TypeIgnore]())

# I am ambivalent about `IngredientsModule`. I've created some useful methods, but I feel like there is a better paradigm. For 
# example, I dislike OOP so much that I was completely blind to the need to treat `ast.ClassDef` the same as `ast.FunctionDef`.
# I could retrofit ClassDef, but I think it would better for me to find a better paradigm for managing various "lego blocks" of abstracted Python code.
@dataclasses.dataclass
class IngredientsModule:
	"""
	Build complete Python modules programmatically from organized components.

	When you need to generate Python code automatically - whether extracting functions from 
	existing modules, combining code from multiple sources, or building entirely new modules - 
	IngredientsModule provides the organizational structure to assemble all the pieces correctly.

	Think of this as a blueprint for a Python file that lets you systematically organize:
	- Import statements from all your code components
	- Setup code that runs when the module is loaded  
	- Function definitions with their dependencies properly tracked
	- Cleanup or configuration code 
	- Script entry point code for when the module is executed directly

	The class maintains the logical structure of a Python module while allowing you to 
	modify, transform, and reorganize the components before generating the final code.
	This is especially useful for:

	- Code optimization workflows that extract and inline functions
	- Code generation pipelines that assemble modules from templates
	- Refactoring tools that reorganize existing codebases
	- Research workflows that programmatically modify and test code variants

	When you're ready, the organized components can be converted into executable Python 
	source code and written to files. The generated modules will have clean import 
	statements, proper organization, and all necessary dependencies.
	Parameters:
		ingredientsFunction: Optional function(s) to include in the module. Can be a single 
			IngredientsFunction or a sequence of them. They will be added to listIngredientsFunctions.
	"""
	ingredientsFunction: dataclasses.InitVar[Sequence[IngredientsFunction] | IngredientsFunction | None] = None

	# init var with an existing module? method to deconstruct an existing module?

	# `body` attribute of `ast.Module`
	"""NOTE
	- Bare statements in `prologue` and `epilogue` are not 'protected' by `if __name__ == '__main__':` so they will be executed merely by loading the module.
	- The dataclass has methods for modifying `prologue`, `epilogue`, and `launcher`.
	- However, `prologue`, `epilogue`, and `launcher` are `ast.Module` (as opposed to `list[ast.stmt]`), so that you may use tools such as `ast.walk` and `ast.NodeVisitor` on the fields.
	"""
	imports: LedgerOfImports = dataclasses.field(default_factory=LedgerOfImports)
	"""
	Manages import dependencies for the entire module.
	
	This tracks all the import statements (like 'import ast' or 'from collections import defaultdict') 
	that the generated module will need. The ledger automatically consolidates imports from all 
	functions and components, eliminating duplicates and organizing them properly.
	
	Modify this using LedgerOfImports methods like addImport_asStr() and addImportFrom_asStr().
	"""
	prologue: ast.Module = Make.Module([])
	"""
	Code that runs immediately when the module is imported.
	
	This contains statements that execute right after the import statements, before any 
	function definitions. Use this for module-level setup, configuration, or initialization 
	code. Warning: This code runs whenever someone imports your module, not just when 
	they run it as a script.
	
	Add statements using appendPrologue().
	"""
	listIngredientsFunctions: list[IngredientsFunction] = dataclasses.field(default_factory=lambda: list[IngredientsFunction]())
	"""
	The function definitions that form the core of this module.
	
	Each IngredientsFunction contains a function definition along with its import dependencies 
	and other metadata. These functions will appear in the middle section of the generated 
	module, after prologue code and before epilogue code.
	
	Add functions using appendIngredientsFunction().
	"""
	epilogue: ast.Module = Make.Module([])
	"""
	Code that runs after all function definitions are loaded.
	
	This contains statements that execute after the function definitions but before any 
	script entry point code. Use this for module-level configuration that depends on 
	the functions being defined, or for setting up module-level variables.
	
	Add statements using appendEpilogue().
	"""
	launcher: ast.Module = Make.Module([])
	"""
	Script entry point code that runs when the module is executed directly.
	
	This should contain the main logic for when someone runs your module as a script 
	(e.g., 'python mymodule.py'). The code here will be automatically wrapped in 
	'if __name__ == "__main__":' when the module is generated.
	
	Add statements using appendLauncher().
	"""

	# `ast.TypeIgnore` statements to supplement those in other fields; `type_ignores` is a parameter for `ast.Module` constructor
	_supplemental_type_ignores: list[ast.TypeIgnore] = dataclasses.field(default_factory=lambda: list[ast.TypeIgnore]())
	"""Internal: Additional type ignore directives."""

	def __post_init__(self, ingredientsFunction: Sequence[IngredientsFunction] | IngredientsFunction | None = None) -> None:
		if ingredientsFunction is not None:
			if isinstance(ingredientsFunction, IngredientsFunction):
				self.appendIngredientsFunction(ingredientsFunction)
			else:
				self.appendIngredientsFunction(*ingredientsFunction)

	def _append_astModule(self, self_astModule: ast.Module, astModule: ast.Module | None, statement: Sequence[ast.stmt] | ast.stmt | None, type_ignores: list[ast.TypeIgnore] | None) -> None:
		"""
		Internal: Append statements to a module section.
		"""
		list_body: list[ast.stmt] = []
		listTypeIgnore: list[ast.TypeIgnore] = []
		if astModule is not None and isinstance(astModule, ast.Module): # pyright: ignore[reportUnnecessaryIsInstance]
			list_body.extend(astModule.body)
			listTypeIgnore.extend(astModule.type_ignores)
		if type_ignores is not None:
			listTypeIgnore.extend(type_ignores)
		if statement is not None:
			if isinstance(statement, Sequence):
				list_body.extend(statement)
			else:
				list_body.append(statement)
		self_astModule.body.extend(list_body)
		self_astModule.type_ignores.extend(listTypeIgnore)
		ast.fix_missing_locations(self_astModule)

	def appendPrologue(self, astModule: ast.Module | None = None, statement: Sequence[ast.stmt] | ast.stmt | None = None, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Add setup code that runs when the module is imported.
		
		Use this to add statements that should execute immediately after the import statements,
		before any function definitions. This is useful for module-level initialization,
		configuration setup, or global variable definitions that your functions will need.
		
		Warning: Code added here runs every time someone imports your module, not just when
		they run it as a script. For script-only code, use appendLauncher() instead.

		Parameters:
			astModule: An existing parsed module to append all statements from.
			statement: Individual statement(s) to append. Can be a single statement or sequence.
			type_ignores: Additional type ignore directives associated with the added code.
		"""
		self._append_astModule(self.prologue, astModule, statement, type_ignores)

	def appendEpilogue(self, astModule: ast.Module | None = None, statement: Sequence[ast.stmt] | ast.stmt | None = None, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Add cleanup code that runs after all functions are defined.
		
		Use this to add statements that should execute after all function definitions have
		been processed, but before any script entry point code. This is useful for
		module-level configuration that depends on the functions being available, or for
		setting up module-level objects that use the defined functions.

		Parameters:
			astModule: An existing parsed module to append all statements from.
			statement: Individual statement(s) to append. Can be a single statement or sequence.
			type_ignores: Additional type ignore directives associated with the added code.
		"""
		self._append_astModule(self.epilogue, astModule, statement, type_ignores)

	def appendLauncher(self, astModule: ast.Module | None = None, statement: Sequence[ast.stmt] | ast.stmt | None = None, type_ignores: list[ast.TypeIgnore] | None = None) -> None:
		"""
		Add script entry point code that runs only when the module is executed directly.
		
		Use this to add the main logic for when someone runs your generated module as a script
		(e.g., 'python mymodule.py'). The code you add here will be automatically wrapped in
		'if __name__ == "__main__":' in the final generated module, so it only runs when the
		module is executed directly, not when it's imported by other code.

		Parameters:
			astModule: An existing parsed module to append all statements from.
			statement: Individual statement(s) to append. Can be a single statement or sequence.
			type_ignores: Additional type ignore directives associated with the added code.
		"""
		self._append_astModule(self.launcher, astModule, statement, type_ignores)

	def appendIngredientsFunction(self, *ingredientsFunction: IngredientsFunction) -> None:
		"""
		Add function definitions to this module.
		
		Each IngredientsFunction contains a complete function definition along with its 
		import dependencies and metadata. The functions will be placed in the generated 
		module after any prologue code and before any epilogue code.
		
		When multiple functions are added, they maintain the order in which they were added.
		Import dependencies from all functions are automatically consolidated at the module level.

		Parameters:
			*ingredientsFunction: One or more IngredientsFunction objects containing the 
				function definitions to add to this module.
		"""
		for allegedIngredientsFunction in ingredientsFunction:
			self.listIngredientsFunctions.append(allegedIngredientsFunction)

	def removeImportFromModule(self, dotModule: identifierDotAttribute) -> None:
		"""
		Remove all import dependencies for a specific module across this entire module.
		
		This removes all recorded import dependencies for the specified module from both
		the module-level imports and from all individual functions. Use this when you know
		a particular module is no longer needed anywhere in the generated code.

		Parameters:
			dotModule: The module name to remove all dependencies for (e.g., "ast", "collections.abc").
		"""
		self.removeImportFrom(dotModule, None, None)

	def removeImportFrom(self, dotModule: identifierDotAttribute, name: str | None, asName: str | None = None) -> None:
		"""
		Remove specific import dependencies across this module and all its functions.
		
		This method provides fine-grained control over which import dependencies to remove
		from both the module-level imports and all individual function imports. This ensures 
		consistent import management across the entire generated module. You can remove all 
		dependencies from a module, specific items, or items with specific aliases.
		
		Note: This removal is not permanent - import dependencies can be added again later 
		if needed.

		Parameters:
			dotModule: The module name containing the import dependencies to modify.
			name: The specific item name to remove. If None, removes based on asName matching.
			asName: The specific alias to remove. If None with a name, removes exact name matches.

		Removal behavior:
		- name=None, asName=None: Remove all dependency records for the module
		- name="item", asName=None: Remove records for importing "item" without an alias  
		- name="item", asName="alias": Remove records for importing "item as alias"		
		- name=None, asName="alias": Remove any record that uses "alias" as the imported name
		"""
		self.imports.removeImportFrom(dotModule, name, asName)
		for ingredientsFunction in self.listIngredientsFunctions:
			ingredientsFunction.imports.removeImportFrom(dotModule, name, asName)

	def _consolidatedLedger(self) -> LedgerOfImports:
		"""
		Internal: Merge all import dependencies from module and functions into a single ledger.
		"""
		sherpaLedger = LedgerOfImports()
		listLedgers: list[LedgerOfImports] = [self.imports]
		for ingredientsFunction in self.listIngredientsFunctions:
			listLedgers.append(ingredientsFunction.imports)
		sherpaLedger.update(*listLedgers)
		return sherpaLedger

	@property
	def _list_astImportImportFrom(self) -> list[ast.Import | ast.ImportFrom]:
		"""Internal: Generate consolidated import statements."""
		return self._consolidatedLedger().makeList_ast()

	@property
	def body(self) -> list[ast.stmt]:
		"""
		Get the complete sequence of statements that will form the generated Python module.
		
		This property assembles all the components of your module in the correct order:
		1. Import statements (consolidated from all functions and module-level imports)
		2. Prologue code (module-level setup that runs on import)
		3. Function definitions (all the functions you've added)
		4. Epilogue code (module-level code that runs after functions are defined)
		5. Launcher code (script entry point, automatically wrapped in if __name__ == "__main__")
		
		The returned list represents the complete body of statements for an executable Python module.
		This is typically used internally when converting the IngredientsModule to actual Python source code.

		Returns:
			Complete list of statements that will appear in the generated Python module, in execution order.
		"""
		list_stmt: list[ast.stmt] = []
		list_stmt.extend(self._list_astImportImportFrom)
		list_stmt.extend(self.prologue.body)
		for ingredientsFunction in self.listIngredientsFunctions:
			list_stmt.append(ingredientsFunction.astFunctionDef)
		list_stmt.extend(self.epilogue.body)
		list_stmt.extend(self.launcher.body)
		# TODO `launcher`, if it exists, must start with `if __name__ == '__main__':` and be indented
		return list_stmt

	@property
	def type_ignores(self) -> list[ast.TypeIgnore]:
		"""
		Get all type ignore directives that should be included in the generated module.
		
		This consolidates type ignore directives from all components (module-level, individual 
		functions, prologue, epilogue, and launcher code) into a single list. Type ignores are 
		used to suppress specific type checking warnings in the generated code.
		
		This is typically used internally when creating the final Python module structure.

		Returns:
			Complete list of type ignore directives for the generated module.
		"""
		listTypeIgnore: list[ast.TypeIgnore] = self._supplemental_type_ignores
		listTypeIgnore.extend(self._consolidatedLedger().type_ignores)
		listTypeIgnore.extend(self.prologue.type_ignores)
		for ingredientsFunction in self.listIngredientsFunctions:
			listTypeIgnore.extend(ingredientsFunction.type_ignores)
		listTypeIgnore.extend(self.epilogue.type_ignores)
		listTypeIgnore.extend(self.launcher.type_ignores)
		return listTypeIgnore
