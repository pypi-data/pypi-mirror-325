import os
from typing import Dict, Any

import yaml


def resolve_package_path() -> str:
    return os.path.dirname(__file__)


def load_yaml_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        openapi = yaml.safe_load(file)

    return openapi
