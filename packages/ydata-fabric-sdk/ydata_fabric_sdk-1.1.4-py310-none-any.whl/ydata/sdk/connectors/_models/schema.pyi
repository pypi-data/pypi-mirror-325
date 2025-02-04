from _typeshed import Incomplete
from ydata.sdk.common.model import BaseModel, Config
from ydata.sdk.common.pydantic_utils import to_camel

class BaseConfig(Config):
    alias_generator = to_camel

class TableColumn(BaseModel):
    """Class to store the information of a Column table."""
    model_config: Incomplete
    name: str
    variable_type: str
    primary_key: bool | None
    is_foreign_key: bool | None
    foreign_keys: list
    nullable: bool

class Table(BaseModel):
    """Class to store the table columns information."""
    model_config: Incomplete
    name: str
    columns: list[TableColumn]
    primary_keys: list[TableColumn]
    foreign_keys: list[TableColumn]

class Schema(BaseModel):
    """Class to store the database schema information."""
    model_config: Incomplete
    name: str
    tables: list[Table] | None
