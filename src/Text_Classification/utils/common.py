import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from Text_Classification.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns
    Args:
        path_to_yaml (str): path of input file
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} load successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """create directories based on given path list
    
    Args:
        path_to_directories (list): list of path for creating directories
        verbose (bool, optional): ignore logging if multiple directories have to be created. Default to True            
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"The directory created in {path}")

@ensure_annotations
def get_size(path: Path) -> str :
    """get size of the file in KB
    Args:
        path (Path): path to file
    Returns:
        str: size of file in KB
    """
    
    size_in_kb = round(os.path.getsize(path)/ 1024)
    return f"~ {size_in_kb} KB"

