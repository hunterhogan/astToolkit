from ast import AST
from astToolkit import ConstantValueType

def dump(node: AST, annotate_fields: bool = True, include_attributes: bool = False, *, indent: int | str | None = None, show_empty: bool = False) -> str:
    """Return a formatted string representation of an AST node.

    Parameters:
        node: The AST node to format
        annotate_fields (True): Whether to include field names in the output
        include_attributes (False): Whether to include node attributes in addition to fields
        indent (None): String for indentation or number of spaces; `None` for single-line output
        show_empty (False): Whether to include fields with empty list or `None` values

    Returns:
        formattedString: String representation of the AST node with specified formatting
    """
    def _format(node: ConstantValueType | AST | list[AST] | list[str], level: int = 0) -> tuple[str, bool]:
        if indent_str is not None:
            level += 1
            prefix: str = '\n' + indent_str * level
            sep: str = ',\n' + indent_str * level
        else:
            prefix = ''
            sep = ', '
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
                        args.append('%s=%s' % (name, value))
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
                    args.append('%s=%s' % (name, value_formatted))
                else:
                    args.append(value_formatted)
            if include_attributes and node._attributes:
                for name_attributes in node._attributes:
                    try:
                        value_attributes = getattr(node, name_attributes)
                    except AttributeError:
                        continue
                    if value_attributes is None and getattr(cls, name_attributes, ...) is None:
                        continue
                    value_attributes_formatted, simple = _format(value_attributes, level)
                    allsimple = allsimple and simple
                    args.append('%s=%s' % (name_attributes, value_attributes_formatted))
            if allsimple and len(args) <= 3:
                return ('%s(%s)' % (f"{node.__class__.__module__}.{node.__class__.__name__}", ', '.join(args)), not args)
            return ('%s(%s%s)' % (f"{node.__class__.__module__}.{node.__class__.__name__}", prefix, sep.join(args)), False)
        elif isinstance(node, list):
            if not node:
                return ('[]', True)
            return ('[%s%s]' % (prefix, sep.join(_format(x, level)[0] for x in node)), False)
        return (repr(node), True)

    if not isinstance(node, AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    if indent is not None and not isinstance(indent, str):
        indent_str = ' ' * indent
    else:
        indent_str = indent
    return _format(node)[0]

