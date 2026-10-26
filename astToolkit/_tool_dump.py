import ast

def dump(node: ast.AST, annotate_fields: bool=True, include_attributes: bool=False, *, color: bool=False, indent: int | str | None=None, show_empty: bool=False) -> str:
    """
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.

    If annotate_fields is true (by default), the returned string will show the
    names and the values for fields. If annotate_fields is false, the result
    string will be more compact by omitting unambiguous field names.

    Attributes such as line numbers and column offsets are not dumped by default.
    If this is wanted, include_attributes can be set to true.

    If color is true, the returned string is syntax highlighted using ANSI
    escape sequences. If color is false (the default), colored output is always
    disabled.

    If indent is a non-negative integer or string, then the tree will be
    pretty-printed with that indent level. If indent is None (the default),
    the tree is dumped on a single line.

    If show_empty is False, then empty lists and fields that are None
    will be omitted from the output for better readability.
    """
    from _colorize import get_theme
    t = get_theme(force_color=color, force_no_color=not color).ast

    def _format(node, level=0):
        if indent is not None:
            level += 1
            prefix = '\n' + indent * level
            sep = ',\n' + indent * level
        else:
            prefix = ''
            sep = ', '
        if isinstance(node, ast.AST):
            cls = type(node)
            args = []
            args_buffer = []
            allsimple = True
            keywords = annotate_fields
            for name in node._fields:
                try:
                    value = getattr(node, name)
                except AttributeError:
                    keywords = True
                    continue
                if not show_empty and value is None and (getattr(cls, name, ...) is None):
                    keywords = True
                    continue
                if not show_empty:
                    if value == []:
                        field_type = cls._field_types.get(name, object)
                        if getattr(field_type, '__origin__', ...) is list:
                            if not keywords:
                                args_buffer.append(repr(value))
                            continue
                    if not keywords:
                        args.extend(args_buffer)
                        args_buffer = []
                value, simple = _format(value, level)
                allsimple = allsimple and simple
                if keywords:
                    args.append(f'{t.field}{name}{t.reset}={value}')
                else:
                    args.append(value)
            if include_attributes and node._attributes:
                for name in node._attributes:
                    try:
                        value = getattr(node, name)
                    except AttributeError:
                        continue
                    if value is None and getattr(cls, name, ...) is None:
                        continue
                    value, simple = _format(value, level)
                    allsimple = allsimple and simple
                    args.append(f'{t.attribute}{name}{t.reset}={value}')
            cls_name = f'{t.node}ast.{cls.__name__}{t.reset}'
            if allsimple and len(args) <= 3:
                return (f"{cls_name}({', '.join(args)})", not args)
            return (f'{cls_name}({prefix}{sep.join(args)})', False)
        elif isinstance(node, list):
            if not node:
                return ('[]', True)
            return ('[%s%s]' % (prefix, sep.join((_format(x, level)[0] for x in node))), False)
        if isinstance(node, bool) or node is None or node is Ellipsis:
            return (f'{t.keyword}{node!r}{t.reset}', True)
        if isinstance(node, (int, float, complex)):
            return (f'{t.number}{node!r}{t.reset}', True)
        if isinstance(node, (str, bytes)):
            return (f'{t.string}{node!r}{t.reset}', True)
        return (repr(node), True)
    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    if indent is not None and (not isinstance(indent, str)):
        indent = ' ' * indent
    return _format(node)[0]
