from _typeshed import Incomplete
from pydantic import BaseModel as PydanticBaseModel, ConfigDict

class Config(ConfigDict):
    populate_by_name: bool
    extra: str
    use_enum_values: bool

class BaseModel(PydanticBaseModel):
    """BaseModel replacement from pydantic.

    All datamodel from YData SDK inherits from this class.
    """
    model_config: Incomplete
