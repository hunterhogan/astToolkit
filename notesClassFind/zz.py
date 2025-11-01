# ruff: noqa
from astToolkit import Be, Find, Make
import ast

node = ast.Module([ast.Import([ast.alias('pathlib')])], [])
node = Make.While(test=Make.Compare(left=Make.Attribute(Make.Name('state'), 'groupsOfFolds'), ops=[Make.Gt], comparators=[Make.Constant(0)]), body=[])

print(f"{Be.While(node) = }")
print(f"{Find().While()(node) = }")
print(f"{Be.While.testIs(Be.Compare)(node) = }")
print(f"{Be.While.testIs(Be.Compare.leftIs(Be.Attribute))(node) = }")

print(f"{Be.Module(node) = }")
print(f"{Be.Module.bodyIs(lambda x: Be.Import(x[0]))(node) = }")
print(f"{Find.Module(node) = }")
print(f"{Find.Module.at(0).Import(node) = }")

Find.alias.name.equal('foo').
