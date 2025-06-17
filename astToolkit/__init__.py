import sys

from astToolkit._astTypes import (
	ast_attributes as ast_attributes, ast_attributes_int as ast_attributes_int,
	ast_attributes_type_comment as ast_attributes_type_comment, ConstantValueType as ConstantValueType,
	hasDOTannotation as hasDOTannotation, hasDOTannotation_expr as hasDOTannotation_expr,
	hasDOTannotation_exprOrNone as hasDOTannotation_exprOrNone, hasDOTarg as hasDOTarg,
	hasDOTarg_str as hasDOTarg_str, hasDOTarg_strOrNone as hasDOTarg_strOrNone,
	hasDOTargs as hasDOTargs, hasDOTargs_arguments as hasDOTargs_arguments,
	hasDOTargs_list_arg as hasDOTargs_list_arg, hasDOTargs_list_expr as hasDOTargs_list_expr,
	hasDOTargtypes as hasDOTargtypes, hasDOTasname as hasDOTasname, hasDOTattr as hasDOTattr,
	hasDOTbases as hasDOTbases, hasDOTbody as hasDOTbody, hasDOTbody_expr as hasDOTbody_expr,
	hasDOTbody_list_stmt as hasDOTbody_list_stmt, hasDOTbound as hasDOTbound,
	hasDOTcases as hasDOTcases, hasDOTcause as hasDOTcause, hasDOTcls as hasDOTcls,
	hasDOTcomparators as hasDOTcomparators, hasDOTcontext_expr as hasDOTcontext_expr,
	hasDOTconversion as hasDOTconversion, hasDOTctx as hasDOTctx,
	hasDOTdecorator_list as hasDOTdecorator_list, hasDOTdefaults as hasDOTdefaults,
	hasDOTelt as hasDOTelt, hasDOTelts as hasDOTelts, hasDOTexc as hasDOTexc,
	hasDOTfinalbody as hasDOTfinalbody, hasDOTformat_spec as hasDOTformat_spec,
	hasDOTfunc as hasDOTfunc, hasDOTgenerators as hasDOTgenerators, hasDOTguard as hasDOTguard,
	hasDOThandlers as hasDOThandlers, hasDOTid as hasDOTid, hasDOTifs as hasDOTifs,
	hasDOTis_async as hasDOTis_async, hasDOTitems as hasDOTitems, hasDOTiter as hasDOTiter,
	hasDOTkey as hasDOTkey, hasDOTkeys as hasDOTkeys, hasDOTkeys_list_expr as hasDOTkeys_list_expr,
	hasDOTkeys_list_exprOrNone as hasDOTkeys_list_exprOrNone, hasDOTkeywords as hasDOTkeywords,
	hasDOTkind as hasDOTkind, hasDOTkw_defaults as hasDOTkw_defaults, hasDOTkwarg as hasDOTkwarg,
	hasDOTkwd_attrs as hasDOTkwd_attrs, hasDOTkwd_patterns as hasDOTkwd_patterns,
	hasDOTkwonlyargs as hasDOTkwonlyargs, hasDOTleft as hasDOTleft, hasDOTlevel as hasDOTlevel,
	hasDOTlineno as hasDOTlineno, hasDOTlower as hasDOTlower, hasDOTmodule as hasDOTmodule,
	hasDOTmsg as hasDOTmsg, hasDOTname as hasDOTname, hasDOTname_Name as hasDOTname_Name,
	hasDOTname_str as hasDOTname_str, hasDOTname_strOrNone as hasDOTname_strOrNone,
	hasDOTnames as hasDOTnames, hasDOTnames_list_alias as hasDOTnames_list_alias,
	hasDOTnames_list_str as hasDOTnames_list_str, hasDOTop as hasDOTop,
	hasDOTop_boolop as hasDOTop_boolop, hasDOTop_operator as hasDOTop_operator,
	hasDOTop_unaryop as hasDOTop_unaryop, hasDOToperand as hasDOToperand, hasDOTops as hasDOTops,
	hasDOToptional_vars as hasDOToptional_vars, hasDOTorelse as hasDOTorelse,
	hasDOTorelse_expr as hasDOTorelse_expr, hasDOTorelse_list_stmt as hasDOTorelse_list_stmt,
	hasDOTpattern as hasDOTpattern, hasDOTpattern_pattern as hasDOTpattern_pattern,
	hasDOTpattern_patternOrNone as hasDOTpattern_patternOrNone, hasDOTpatterns as hasDOTpatterns,
	hasDOTposonlyargs as hasDOTposonlyargs, hasDOTrest as hasDOTrest, hasDOTreturns as hasDOTreturns,
	hasDOTreturns_expr as hasDOTreturns_expr, hasDOTreturns_exprOrNone as hasDOTreturns_exprOrNone,
	hasDOTright as hasDOTright, hasDOTsimple as hasDOTsimple, hasDOTslice as hasDOTslice,
	hasDOTstep as hasDOTstep, hasDOTsubject as hasDOTsubject, hasDOTtag as hasDOTtag,
	hasDOTtarget as hasDOTtarget, hasDOTtarget_expr as hasDOTtarget_expr,
	hasDOTtarget_Name as hasDOTtarget_Name,
	hasDOTtarget_NameOrAttributeOrSubscript as hasDOTtarget_NameOrAttributeOrSubscript,
	hasDOTtargets as hasDOTtargets, hasDOTtest as hasDOTtest, hasDOTtype as hasDOTtype,
	hasDOTtype_comment as hasDOTtype_comment, hasDOTtype_ignores as hasDOTtype_ignores,
	hasDOTtype_params as hasDOTtype_params, hasDOTupper as hasDOTupper, hasDOTvalue as hasDOTvalue,
	hasDOTvalue_boolOrNone as hasDOTvalue_boolOrNone,
	hasDOTvalue_ConstantValueType as hasDOTvalue_ConstantValueType,
	hasDOTvalue_expr as hasDOTvalue_expr, hasDOTvalue_exprOrNone as hasDOTvalue_exprOrNone,
	hasDOTvalues as hasDOTvalues, hasDOTvararg as hasDOTvararg,
	identifierDotAttribute as identifierDotAttribute, 一符 as 一符, 个 as 个, 归个 as 归个, 二符 as 二符,
	俪 as 俪, 口 as 口, 工 as 工, 工位 as 工位, 布尔符 as 布尔符, 常 as 常, 形 as 形, 忽 as 忽, 拦 as 拦, 木 as 木, 本 as 本,
	比符 as 比符,
)

if sys.version_info >= (3, 13):
	from astToolkit._astTypes import hasDOTdefault_value as hasDOTdefault_value

# from astToolkit._dumpFunctionDef import dump as dump
from astToolkit._dumpHandmade import dump as dump

from astToolkit._toolkitNodeVisitor import (
	NodeChanger as NodeChanger,
	NodeTourist as NodeTourist,
)

from astToolkit._toolBe import Be as Be
from astToolkit._toolClassIsAndAttribute import ClassIsAndAttribute as ClassIsAndAttribute
from astToolkit._toolDOT import DOT as DOT
from astToolkit._toolGrab import Grab as Grab
from astToolkit._toolMake import Make as Make

from astToolkit._toolIfThis import IfThis as IfThis
from astToolkit._toolThen import Then as Then

from astToolkit._toolkitContainers import (
	IngredientsFunction as IngredientsFunction,
	IngredientsModule as IngredientsModule,
	LedgerOfImports as LedgerOfImports,
)

from astToolkit._toolkitAST import (
	astModuleToIngredientsFunction as astModuleToIngredientsFunction,
	extractClassDef as extractClassDef,
	extractFunctionDef as extractFunctionDef,
	parseLogicalPath2astModule as parseLogicalPath2astModule,
	parsePathFilename2astModule as parsePathFilename2astModule,
)
