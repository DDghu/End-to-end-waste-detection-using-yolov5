import os
from pathlib import Path #cause it automatically correct / or \ according to the os 
import logging #cause for every run i want to see the logs

#the logging string it tracks wwhich time you executed the code and which date you executed the code
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name='WasteDetection'

list_of_files = [
    ".github/workflows/.gitkeep", #this .github help in ci/cd deployment and the things are automatically deployed on cloud
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py", #end point
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath) #it detects the path either it is windows or mac path etc

    filedir, filename = os.path.split(filepath)
    if filedir!="": # if filedir is not empty
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    
    else:
        logging.info(f"{filename} is already created")