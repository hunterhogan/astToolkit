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
    nodeClass = getattr(ast, identifierClass)
    
    # Helper to create minimal arguments node
    def makeEmptyArguments() -> ast.arguments:
        return ast.arguments(
            posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
        )
    
    # Build kwargs for node creation
    dictionaryKwargs = {nameAttribute: valueAttributeNode}
    
    # Add minimal required attributes for each node type using a mapping
    dictionaryDefaults: dict[str, dict[str, Any]] = {
        "alias": {"name": "defaultName"},
        "arg": {"arg": "defaultArg"},
        "Constant": {"value": 0},
        "Name": {"id": "defaultName", "ctx": ast.Load()},
        "ClassDef": {
            "name": "DefaultClass",
            "bases": [],
            "keywords": [],
            "body": [ast.Pass()],
            "decorator_list": [],
        },
        "FunctionDef": {
            "name": "defaultFunction",
            "args": makeEmptyArguments(),
            "body": [ast.Pass()],
            "decorator_list": [],
        },
        "keyword": {"arg": "defaultKeyword", "value": ast.Constant(value=0)},
        "Attribute": {
            "value": ast.Name(id="objectDefault", ctx=ast.Load()),
            "attr": "attrDefault",
            "ctx": ast.Load(),
        },
        "Expr": {"value": ast.Constant(value=0)},
        "Global": {"names": []},
        "Nonlocal": {"names": []},
        "Delete": {"targets": []},
        "Import": {"names": []},
        "Lambda": {"args": makeEmptyArguments(), "body": ast.Constant(value=0)},
        "YieldFrom": {"value": ast.Name(id="defaultGenerator", ctx=ast.Load())},
        "NamedExpr": {
            "target": ast.Name(id="defaultTarget", ctx=ast.Store()),
            "value": ast.Constant(value=0),
        },
        "Starred": {"value": ast.Name(id="defaultValue", ctx=ast.Load()), "ctx": ast.Load()},
        "List": {"elts": [], "ctx": ast.Load()},
        "Set": {"elts": []},
        "Tuple": {"elts": [], "ctx": ast.Load()},
        "Dict": {"keys": [], "values": []},
    }
    
    # Apply defaults for the node type
    if identifierClass in dictionaryDefaults:
        for keyDefault, valueDefault in dictionaryDefaults[identifierClass].items():
            dictionaryKwargs.setdefault(keyDefault, valueDefault)
    
    # Create the node
    try:
        nodeTest = nodeClass(**dictionaryKwargs)
    except TypeError as errorType:
        # Some nodes might need more specific setup
        raise AssertionError(
            f"Failed to create {identifierClass} node with kwargs {dictionaryKwargs}: {errorType}"
        ) from errorType
    
    # Create the predicate that checks if the attribute equals the check value
    predicateAttributeCheck = methodAttribute(lambda attributeActual: attributeActual == valueAttributeCheck)
    
    # Execute the predicate
    resultActual = predicateAttributeCheck(nodeTest)
    
    # Assert the result
    assert resultActual == expectedResult, (
        f"Be.{identifierClass}.{nameMethod} with node.{nameAttribute}={valueAttributeNode} "
        f"checking against {valueAttributeCheck} should return {expectedResult}, but got {resultActual}"
    )
