from dataclasses import dataclass, field
from enum import Enum
from typing import Union

from dataclass_wizard import JSONWizard


class VariableType(Enum):
    STRING = 1
    NUMBER = 2
    TIMESTAMP = 3
    SET = 4


class Operator(Enum):
    EQUAL = 1
    LESS_THAN = 2
    LESS_OR_EQUAL = 3
    GREATER_THAN = 4
    GREATER_OR_EQUAL = 5
    CONTAINS = 6
    PERCENT = 7
    REGEXP = 8
    WILDCARD = 9
    SUBSET = 10
    SUPERSET = 11


@dataclass
class CheckVariable:
    name: str
    type: VariableType


@dataclass
class Check:
    operator: Operator
    variable: CheckVariable
    value: Union[str, float, list[str], None] = None


@dataclass
class Condition:
    checks: list[Check]


@dataclass
class ValueCondition:
    checks: list[Check]
    value_override: Union[int, str]


@dataclass
class Flag:
    name: str
    enabled: bool
    overridden: bool
    conditions: list[Condition]


@dataclass
class Value:
    name: str
    enabled: bool
    overridden: bool
    value_default: Union[int, str]
    value_override: Union[int, str]
    conditions: list[ValueCondition]


@dataclass
class RequestData:
    project_name: str
    flags: list[Flag]
    values: list[Value]


@dataclass
class Variable:
    name: str
    type: VariableType


@dataclass
class PreloadFlagsRequest:
    project: str
    version: int
    variables: list[Variable] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    values: list[tuple[str, Union[str, int]]] = field(default_factory=list)


@dataclass
class PreloadFlagsResponse(JSONWizard):
    version: int
    flags: list[Flag] = field(default_factory=list)
    values: list[Value] = field(default_factory=list)


@dataclass
class SyncFlagsRequest:
    project: str
    version: int
    flags: list[str] = field(default_factory=list)
    values: list[str] = field(default_factory=list)


@dataclass
class SyncFlagsResponse(JSONWizard):
    version: int
    flags: list[Flag] = field(default_factory=list)
    values: list[Value] = field(default_factory=list)
