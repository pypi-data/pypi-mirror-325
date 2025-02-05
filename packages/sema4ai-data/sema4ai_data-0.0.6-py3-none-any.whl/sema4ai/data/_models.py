import json

from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


class SourceInfo(BaseModel):
    @staticmethod
    def parse_connection_data(v) -> dict | None:
        if isinstance(v, str):
            return json.loads(v)
        return v

    name: Annotated[str, Field(description="The name of the data source", alias="NAME")]
    type: Annotated[str, Field(description="The type of the data source", alias="TYPE")]
    engine: Annotated[
        str | None, Field(description="The engine of the data source", alias="ENGINE")
    ] = None
    connection_data: Annotated[
        dict | None,
        BeforeValidator(parse_connection_data),
        Field(
            description="The connection data of the data source",
            alias="CONNECTION_DATA",
        ),
    ] = None


class TableInfo(BaseModel, extra="allow"):
    table_schema: Annotated[
        str, Field(description="The schema of the table", alias="TABLE_SCHEMA")
    ]
    table_name: Annotated[
        str, Field(description="The name of the table", alias="TABLE_NAME")
    ]
    table_type: Annotated[
        str, Field(description="The type of the table", alias="TABLE_TYPE")
    ]
    engine: Annotated[
        str | None, Field(description="The engine of the table", alias="ENGINE")
    ] = None
    version: Annotated[
        int | None, Field(description="The version of the table", alias="VERSION")
    ] = None
    table_rows: Annotated[
        int, Field(description="The estimated number of rows", alias="TABLE_ROWS")
    ]
    create_time: Annotated[
        str, Field(description="The creation timestamp", alias="CREATE_TIME")
    ]
    update_time: Annotated[
        str, Field(description="The last update timestamp", alias="UPDATE_TIME")
    ]


class ColumInfo(BaseModel):
    column_name: Annotated[
        str, Field(description="The name of the column", alias="COLUMN_NAME")
    ]
    data_type: Annotated[
        str, Field(description="The data type of the column", alias="DATA_TYPE")
    ]
