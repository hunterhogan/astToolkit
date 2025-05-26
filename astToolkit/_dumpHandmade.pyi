from ast import AST
from types import EllipsisType, NotImplementedType
from typing import TypeAlias

_Constant: TypeAlias = bool | bytes | complex | EllipsisType | float | int | None | NotImplementedType | range | str

ConstantType: TypeAlias = _Constant | frozenset['ConstantType'] | tuple['ConstantType', ...]

def dump(
    node: AST,
    annotate_fields: bool = ...,
    include_attributes: bool = ...,
    *,
    indent: int | str | None = ...,
    show_empty: bool = ...,
) -> str:
    def _format(node: ConstantType | AST | list[AST] | list[str], level: int = ...) -> tuple[str, bool]:
        # Local variables in _format function
        prefix: str
        sep: str
        cls: type[AST]
        args: list[str]
        args_buffer: list[str]
        allsimple: bool
        keywords: bool
        
        name: str
        value: AST | list[AST] | list[str] | ConstantType | bool | bytes | complex | float | int | str
        value_formatted: str
        simple: bool

        name_attributes: str
        value_attributes: int | None
        value_attributes_formatted: str

        x: AST | str
        
        ...
    
    # Local variables in dump function
    indent_str: str | None
    
    ...
