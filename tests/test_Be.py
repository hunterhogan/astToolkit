from astToolkit import Be
from typing import Any

def test_BeIdentifierClassPositive(beTestData: tuple[str, str, dict[str, Any]]) -> None:
    identifierClass, subtestName, dictTest = beTestData
    node = dictTest['expression']
    beMethod = getattr(Be, identifierClass)
    assert beMethod(node), f"Be.{identifierClass} should return True for {subtestName}"

# def test_BeIdentifierClassNegative(beNegativeTestData: tuple[str, str, str, dict[str, Any]]) -> None:
#     identifierClass, identifierClassFalse, subtestName, dictTest = beNegativeTestData
#     node = dictTest['expression']
#     beMethod = getattr(Be, identifierClass)
#     assert not beMethod(node), f"Be.{identifierClass} should return False for {identifierClassFalse} node in {subtestName}"

