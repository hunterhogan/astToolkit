from astToolkit import astASTattributes
import ast
import sys

if sys.version_info >= (3, 13):

	def dump(node: ast.AST, *, annotate_fields: bool = True, include_attributes: bool = False, indent: int | str | None = None, show_empty: bool = False) -> str:
		"""Return a formatted string representation of an `ast.AST` node.

		Parameters
		----------
		node : ast.AST
			The `ast.AST` node to format.
		annotate_fields : bool = True
			Whether to include field names in the output.
		include_attributes : bool = False
			Whether to include node "_attributes" in addition to fields. The attributes in category `_attributes` are `lineno` (line
			_**n**umer**o**_ (_Latin_ "number")), `col_offset` (***col***umn offset), `end_lineno` (end line _**n**umer**o**_ (_Latin_
			"number")), and `end_col_offset` (end ***col***umn offset).
		indent : int | str | None = None
			String for indentation or number of spaces; `None` for single-line output.
		show_empty : bool = False
			Whether to include fields with empty list or `None` values.

		Returns
		-------
		formattedString : str
			String representation of the `ast.AST` node with specified formatting.

		"""
		def _format(node: astASTattributes, level: int = 0) -> tuple[str, bool]:
			if indentString is not None:
				level += 1
				ImaIndent: str = '\n' + indentString * level
				separator: str = ',\n' + indentString * level
			else:
				ImaIndent = ''
				separator = ', '
			if isinstance(node, ast.AST):
				astAST: type[ast.AST] = type(node)
				listAttributes: list[str] = []
				attributeStaging: list[str] = []
				simpleOutput: bool = True
				showAnnotations: bool = annotate_fields
				for name in node._fields:
					try:
						value: astASTattributes = getattr(node, name)
					except AttributeError:
						showAnnotations = True
						continue
					if value is None and getattr(astAST, name, ...) is None:
						if show_empty:
							listAttributes.append(f'{name}={value}')
						showAnnotations = True
						continue
					if not show_empty:
						if value == []:
							field_type: astASTattributes = astAST._field_types.get(name, object)  # noqa: SLF001
							if getattr(field_type, '__origin__', ...) is list:
								if not showAnnotations:
									attributeStaging.append(repr(value))
								continue
						if not showAnnotations:
							listAttributes.extend(attributeStaging)
							attributeStaging = []
					valueFormatted, simpleFormat = _format(value, level)
					simpleOutput = simpleOutput and simpleFormat
					if showAnnotations:
						listAttributes.append(f'{name}={valueFormatted}')
					else:
						listAttributes.append(valueFormatted)
				if include_attributes and node._attributes:  # noqa: SLF001
					for name_attributes in node._attributes:  # noqa: SLF001
						try:
							value_attributes = getattr(node, name_attributes)
						except AttributeError:
							continue
						if value_attributes is None and getattr(astAST, name_attributes, ...) is None:
							continue
						value_attributesFormatted, simpleFormat = _format(value_attributes, level)
						simpleOutput = simpleOutput and simpleFormat
						listAttributes.append(f'{name_attributes}={value_attributesFormatted}')
				if simpleOutput and len(listAttributes) <= 3:
					return (f"ast.{node.__class__.__name__}({', '.join(listAttributes)})", not bool(listAttributes))
				return (f"ast.{node.__class__.__name__}({ImaIndent}{separator.join(listAttributes)})", False)
			elif isinstance(node, list):
				if not node:
					return ('[]', True)
				return (f'[{ImaIndent}{separator.join(_format(x, level)[0] for x in node)}]', False)
			return (repr(node), True)

		if not isinstance(node, ast.AST):
			message = f'expected `ast.AST`, got {node.__class__.__name__!r}'
			raise TypeError(message)
		if indent is not None and not isinstance(indent, str):
			indentString = " " * indent
		else:
			indentString = indent
		return _format(node)[0]

