import os,sys
import yaml
import numpy as np
import pandas as pd
from visa.constant import *
from visa.exception import CustomException

def read_yaml_file(filr_path:str)->dict:
    try:
        with open(file_path,'rb') as yaml_file: #rb for reading data
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys) from e