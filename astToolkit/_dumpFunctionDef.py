from _ast import *

def dump(node, annotate_fields=True, include_attributes=False, *, indent=None, show_empty=False):
    """
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.  If annotate_fields is true (by default),
    the returned string will show the names and the values for fields.
    If annotate_fields is false, the result string will be more compact by
    omitting unambiguous field names.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    include_attributes can be set to true.  If indent is a non-negative
    integer or string, then the tree will be pretty-printed with that indent
    level. None (the default) selects the single line representation.
    If show_empty is False, then empty lists and fields that are None
    will be omitted from the output for better readability.
    """

    def _format(node, level=0):
        if indent is not None:
            level += 1
            prefix = '\n' + indent * level
            sep = ',\n' + indent * level
        else:
            prefix = ''
            sep = ', '
        if isinstance(node, AST):
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
                if value is None and getattr(cls, name, ...) is None:
                    keywords = True
                    continue
                if not show_empty and (value is None or value == []) and (not isinstance(node, (Constant, MatchSingleton))):
                    args_buffer.append(repr(value))
                    continue
                elif not keywords:
                    args.extend(args_buffer)
                    args_buffer = []
                value, simple = _format(value, level)
                allsimple = allsimple and simple
                if keywords:
                    args.append('%s=%s' % (name, value))
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
                    args.append('%s=%s' % (name, value))
            if allsimple and len(args) <= 3:
                return ('%s(%s)' % ('ast.' + node.__class__.__name__, ', '.join(args)), not args)
            return ('%s(%s%s)' % ('ast.' + node.__class__.__name__, prefix, sep.join(args)), False)
        elif isinstance(node, list):
            if not node:
                return ('[]', True)
            return ('[%s%s]' % (prefix, sep.join((_format(x, level)[0] for x in node))), False)
        return (repr(node), True)
    if not isinstance(node, AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    if indent is not None and (not isinstance(indent, str)):
        indent = ' ' * indent
    return _format(node)[0]