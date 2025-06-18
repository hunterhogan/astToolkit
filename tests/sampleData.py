from astToolkit import Make
import ast

testValue = ast.Import()
ast_dump_show_emptyTrue = "Import(names=[])"
astToolkit_dump_show_emptyTrue = "ast.Import(names=[])"
ast_dump_show_emptyFalse = "Import()"
astToolkit_dump_show_emptyFalse = "ast.Import()"

testValue = ast.ImportFrom()
ast_dump_show_emptyTrue = "ImportFrom(names=[])"
astToolkit_dump_show_emptyTrue = "ast.ImportFrom(module=None, names=[], level=None)"
ast_dump_show_emptyFalse = "ImportFrom()"
astToolkit_dump_show_emptyFalse = "ast.ImportFrom()"

testValue = ast.In()
ast_dump_show_emptyTrue = "In()"
astToolkit_dump_show_emptyTrue = "ast.In()"
ast_dump_show_emptyFalse = "In()"
astToolkit_dump_show_emptyFalse = "ast.In()"

testValue = ast.Import(names=[])
ast_dump_show_emptyTrue = "Import(names=[])"
astToolkit_dump_show_emptyTrue = "ast.Import(names=[])"

testValue = ast.ImportFrom(module=None, names=[], level=0)
ast_dump_show_emptyTrue = "ImportFrom(names=[], level=0)"
astToolkit_dump_show_emptyTrue = "ast.ImportFrom(module=None, names=[], level=0)"

testValue = Make.Import(dotModule='Make.Import')
ast_dump_show_emptyTrue = "Import(names=[alias(name='Make.Import')])"
astToolkit_dump_show_emptyTrue = "ast.Import(names=[ast.alias(name='Make.Import', asname=None)])"

testValue = Make.ImportFrom(dotModule='Make.ImportFrom', list_alias=[Make.alias(name='Make_ImportFrom_alias')])
ast_dump_show_emptyTrue	= "ImportFrom(module='Make.ImportFrom', names=[alias(name='Make_ImportFrom_alias')], level=0)"
astToolkit_dump_show_emptyTrue = "ast.ImportFrom(module='Make.ImportFrom', names=[ast.alias(name='Make_ImportFrom_alias', asname=None)], level=0)"

testValue = Make.In()
ast_dump_show_emptyTrue = "In()"
astToolkit_dump_show_emptyTrue = "ast.In()"
