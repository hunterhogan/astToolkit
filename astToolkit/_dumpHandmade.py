from ast import AST
from astToolkit import ConstantValueType

def dump(node: AST, *, annotate_fields: bool = True, include_attributes: bool = False, indent: int | str | None = None, show_empty: bool = False) -> str:
	"""Return a formatted string representation of an AST node.

	(AI generated docstring)

	Parameters
	----------
	node : AST
		The AST node to format.
	annotate_fields : bool = True
		Whether to include field names in the output.
	include_attributes : bool = False
		Whether to include node attributes in addition to fields.
	indent : int | str | None = None
		String for indentation or number of spaces; `None` for single-line output.
	show_empty : bool = False
		Whether to include fields with empty list or `None` values.

	Returns
	-------
	formattedString : str
		String representation of the AST node with specified formatting.

	"""
	def _format(node: ConstantValueType | AST | list[AST] | list[str], level: int = 0) -> tuple[str, bool]:
		if indent_str is not None:
			level += 1
			ImaIndent: str = '\n' + indent_str * level
			separator: str = ',\n' + indent_str * level
		else:
			ImaIndent = ''
			separator = ', '
		if isinstance(node, AST):
			cls: type[AST] = type(node)
			args: list[str] = []
			args_buffer: list[str] = []
			allsimple: bool = True
			keywords: bool = annotate_fields
			for name in node._fields:
				try:
					value = getattr(node, name)
				except AttributeError:
					keywords = True
					continue
				if value is None and getattr(cls, name, ...) is None:
					if show_empty:
						args.append(f'{name}={value}')
					keywords = True
					continue
				if not show_empty:
					if value == []:
						field_type: ConstantValueType | AST | list[AST] | list[str] = cls._field_types.get(name, object)
						if getattr(field_type, '__origin__', ...) is list:
							if not keywords:
								args_buffer.append(repr(value))
							continue
					if not keywords:
						args.extend(args_buffer)
						args_buffer = []
				value_formatted, simple = _format(value, level)
				allsimple = allsimple and simple
				if keywords:
					args.append(f'{name}={value_formatted}')
				else:
					args.append(value_formatted)
			if include_attributes and node._attributes:  # noqa: SLF001
				for name_attributes in node._attributes:  # noqa: SLF001
					try:
						value_attributes = getattr(node, name_attributes)
					except AttributeError:
						continue
					if value_attributes is None and getattr(cls, name_attributes, ...) is None:
						continue
					value_attributes_formatted, simple = _format(value_attributes, level)
					allsimple = allsimple and simple
					args.append(f'{name_attributes}={value_attributes_formatted}')
			if allsimple and len(args) <= 3:  # noqa: PLR2004
				return (f"ast.{node.__class__.__name__}({', '.join(args)})", not args)
			return (f"ast.{node.__class__.__name__}({ImaIndent}{separator.join(args)})", False)
		elif isinstance(node, list):
			if not node:
				return ('[]', True)
			return (f'[{ImaIndent}{separator.join(_format(x, level)[0] for x in node)}]', False)
		return (repr(node), True)

	if not isinstance(node, AST):
		message = f'expected AST, got {node.__class__.__name__!r}'
		raise TypeError(message)
	if indent is not None and not isinstance(indent, str):
		indent_str = ' ' * indent
	else:
		indent_str = indent
	return _format(node)[0]

