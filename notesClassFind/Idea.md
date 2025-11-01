# Idea

Instantiate an object for use with `ast.NodeVisitor` to match against `node` and/or descendants of `node`.

Call the object by passing `node`.

## IDE autocomplete

Type `Find.`, and the following should be available for autocomplete.

1. `ast.AST` subclasses, initially and when applicable;
2. after a subclass, each attribute of the subclass until the attribute is called or until a method with the same identifier as the attribute is called;
3. after a subclass.attribute, must select a method appropriate for that subclass.attribute:
  A. methods connected to that subclass.attribute, if any,
  B. methods connected to the type of the subclass.attribute (e.g., `str` or `ast.expr`), if any,
  C. `ast.AST` subclasses that match the type of the subclass.attribute, if any.

## Notes

Every call to an attribute of `Find` starts with something like

```python
    class Class:
        def __call__(cls, node: ast.AST) -> TypeIs[ast.Class]:
            return isinstance(node, ast.Class)
```

Then, get the next attribute and apply it. If the attribute of `Find` is an `ast.AST` subclass,
then call the corresponding `isinstance(node, ast.Class)`. If it is a method, then call the method.

Centralized state-management: chaining.

## Type information

I want the types to be preserved, including the attributes of a node, such as how the information from `isinstance`
is preserved for `node.target`.

```python
def staticFunction(astClassDef: ast.ClassDef, dictionary_Attributes: dict[str, ast.expr]):
    for node in ast.walk(astClassDef):
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            dictionary_Attributes[node.target.id] = node.annotation
```

## Syntax

In general, try to make the syntax the same as "dot notation" and use (parentheses) for additional parameters.

- The system should seamlessly mix with Python `ast`.
- The syntax should naturally integrate with Python.
- Don't reinvent the wheel, and don't invent a new programming language for the user to learn.
- If an attribute is type `list`, use `.any`, `.all`, or `.at(n)`.
