from astToolkit import Be
from typing import Any
import ast

def test_BeIdentifierClassPositive(beTestData: tuple[str, str, dict[str, Any]]) -> None:
    identifierClass, subtestName, dictTest = beTestData
    node = dictTest['expression']
    beMethod = getattr(Be, identifierClass)
    assert beMethod(node), f"Be.{identifierClass} should return True for {subtestName}"

def test_BeIdentifierClassNegative(beNegativeTestData: tuple[str, str, str, dict[str, Any]]) -> None:
    identifierClass, identifier_vsClass, subtestName, dictionaryTestData = beNegativeTestData
    node = dictionaryTestData['expression']
    beMethod = getattr(Be, identifierClass)
    assert not beMethod(node), f"Be.{identifierClass} should return False for {identifier_vsClass} node in {subtestName}"

def test_BeAttributeMethod(beAttributeMethodTestData: tuple[str, str, str, Any, Any, bool]) -> None:
    identifierClass, nameMethod, nameAttribute, valueAttributeNode, valueAttributeCheck, expectedResult = beAttributeMethodTestData
    
    # Get the Be class (e.g., Be.alias, Be.FunctionDef)
    classAttribute = getattr(Be, identifierClass)
    
    # Get the attribute method (e.g., Be.alias.nameIs, Be.FunctionDef.nameIs)
    methodAttribute = getattr(classAttribute, nameMethod)
    
    # Create a node with the test attribute value
    # We need to construct a node of the correct type with the attribute set
    nodeClass = getattr(ast, identifierClass)
    
    # Build kwargs for node creation
    dictionaryKwargs = {nameAttribute: valueAttributeNode}
    
    # Add minimal required attributes for each node type
    if identifierClass == "alias":
        dictionaryKwargs.setdefault("name", "defaultName")
    elif identifierClass == "arg":
        dictionaryKwargs.setdefault("arg", "defaultArg")
    elif identifierClass == "Constant":
        dictionaryKwargs.setdefault("value", 0)
    elif identifierClass == "Name":
        dictionaryKwargs.setdefault("id", "defaultName")
        dictionaryKwargs.setdefault("ctx", ast.Load())
    elif identifierClass == "ClassDef":
        dictionaryKwargs.setdefault("name", "DefaultClass")
        dictionaryKwargs.setdefault("bases", [])
        dictionaryKwargs.setdefault("keywords", [])
        dictionaryKwargs.setdefault("body", [ast.Pass()])
        dictionaryKwargs.setdefault("decorator_list", [])
    elif identifierClass == "FunctionDef":
        dictionaryKwargs.setdefault("name", "defaultFunction")
        dictionaryKwargs.setdefault("args", ast.arguments(
            posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
        ))
        dictionaryKwargs.setdefault("body", [ast.Pass()])
        dictionaryKwargs.setdefault("decorator_list", [])
    elif identifierClass == "keyword":
        dictionaryKwargs.setdefault("arg", "defaultKeyword")
        dictionaryKwargs.setdefault("value", ast.Constant(value=0))
    elif identifierClass == "Attribute":
        dictionaryKwargs.setdefault("value", ast.Name(id="objectDefault", ctx=ast.Load()))
        dictionaryKwargs.setdefault("attr", "attrDefault")
        dictionaryKwargs.setdefault("ctx", ast.Load())
    elif identifierClass == "Return":
        # Return can have None as value - already set in dictionaryKwargs
        pass
    elif identifierClass == "Expr":
        dictionaryKwargs.setdefault("value", ast.Constant(value=0))
    elif identifierClass == "Global":
        dictionaryKwargs.setdefault("names", [])
    elif identifierClass == "Nonlocal":
        dictionaryKwargs.setdefault("names", [])
    elif identifierClass == "Delete":
        dictionaryKwargs.setdefault("targets", [])
    elif identifierClass == "Import":
        dictionaryKwargs.setdefault("names", [])
    elif identifierClass == "Lambda":
        dictionaryKwargs.setdefault("args", ast.arguments(
            posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
        ))
        dictionaryKwargs.setdefault("body", ast.Constant(value=0))
    elif identifierClass == "Yield":
        # Yield can have None as value
        pass
    elif identifierClass == "YieldFrom":
        dictionaryKwargs.setdefault("value", ast.Name(id="defaultGenerator", ctx=ast.Load()))
    elif identifierClass == "NamedExpr":
        dictionaryKwargs.setdefault("target", ast.Name(id="defaultTarget", ctx=ast.Store()))
        dictionaryKwargs.setdefault("value", ast.Constant(value=0))
    elif identifierClass == "Starred":
        dictionaryKwargs.setdefault("value", ast.Name(id="defaultValue", ctx=ast.Load()))
        dictionaryKwargs.setdefault("ctx", ast.Load())
    elif identifierClass == "List":
        dictionaryKwargs.setdefault("elts", [])
        dictionaryKwargs.setdefault("ctx", ast.Load())
    elif identifierClass == "Set":
        dictionaryKwargs.setdefault("elts", [])
    elif identifierClass == "Tuple":
        dictionaryKwargs.setdefault("elts", [])
        dictionaryKwargs.setdefault("ctx", ast.Load())
    elif identifierClass == "Dict":
        dictionaryKwargs.setdefault("keys", [])
        dictionaryKwargs.setdefault("values", [])
    
    # Create the node
    try:
        nodeTest = nodeClass(**dictionaryKwargs)
    except TypeError as errorType:
        # Some nodes might need more specific setup
        raise AssertionError(f"Failed to create {identifierClass} node with kwargs {dictionaryKwargs}: {errorType}") from errorType
    
    # Create the predicate that checks if the attribute equals the check value
    predicateAttributeCheck = methodAttribute(lambda attributeActual: attributeActual == valueAttributeCheck)
    
    # Execute the predicate
    resultActual = predicateAttributeCheck(nodeTest)
    
    # Assert the result
    assert resultActual == expectedResult, (
        f"Be.{identifierClass}.{nameMethod} with node.{nameAttribute}={valueAttributeNode} "
        f"checking against {valueAttributeCheck} should return {expectedResult}, but got {resultActual}"
    )
