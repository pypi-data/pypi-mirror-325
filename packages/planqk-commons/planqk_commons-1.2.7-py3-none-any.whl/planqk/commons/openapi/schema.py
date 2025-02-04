from inspect import Signature
from typing import Any, Dict, Tuple

from pydantic import BaseModel


def generate_schemas(signature: Signature) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    input_schema = {}
    output_schema = {}
    schema_definitions = {}

    # generate schema for each parameter
    parameters = signature.parameters
    for parameter in parameters.values():
        parameter_type = parameter.annotation

        if issubclass(parameter_type, BaseModel):
            schema, schema_definition = generate_pydantic_schema(parameter_type)
            input_schema = schema
            if schema_definition is not None:
                schema_definitions.update(schema_definition)

    # generate schema for the return type
    return_type = signature.return_annotation
    if issubclass(return_type, BaseModel):
        schema, schema_definition = generate_pydantic_schema(return_type)
        output_schema = schema
        if schema_definition is not None:
            schema_definitions.update(schema_definition)

    return input_schema, output_schema, schema_definitions


def generate_pydantic_schema(parameter_type) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    if not issubclass(parameter_type, BaseModel):
        raise ValueError("Only Pydantic models are supported")

    schema_definition = None
    schema = parameter_type.model_json_schema(
        ref_template="#/components/schemas/{model}",
        mode="serialization",
    )

    if "$defs" in schema:
        schema_definition = schema.pop("$defs")

    return schema, schema_definition
