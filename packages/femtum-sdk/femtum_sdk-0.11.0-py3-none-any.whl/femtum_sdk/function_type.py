from typing import Optional, TypedDict


class TagDict(TypedDict):
    Key: str
    Value: Optional[str]


class FunctionConfigurationDict(TypedDict):
    WaferName: Optional[str]
    ReticleName: Optional[str]
    DieName: Optional[str]
    CircuitName: Optional[str]
    ResultName: Optional[str]
    Tags: list[TagDict]


class FunctionHandleEventDict(TypedDict):
    Configuration: FunctionConfigurationDict
