# we use utils frequently so we write in one file instead of separate components
import os.path
import sys
import yaml
import base64

from WasteDetection.exception import AppException
from WasteDetection.logger import logging

#we have to read the yaml file
def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successsfully"
                         )
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e

def write_yaml_file(file_path:str,content:object,replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content,file)
            logging.info("write yaml file successsfully")
    except Exception as e:
        raise AppException(e,sys) 

# decoding and encoding of image is needed to pass this image in backend
def decodeImage(imgstring, fileName):
    imgdata= base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())
