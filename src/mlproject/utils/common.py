import os
from box.exceptions import BoxValueError
import yaml
from mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_list: list):
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = os.path.getsize(path) / 1024
    return f"~ {size_in_kb:.2f} KB"