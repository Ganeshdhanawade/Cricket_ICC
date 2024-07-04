import os, sys 
from pathlib import Path
import logging

while True:
    project_name=input("Enter you project name: ")
    if project_name != "":
        break

## src/__init__.py
##src/components/__init__.py
list_of_files = [
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/predict_pipeline.py",
    f"src/pipeline/train_pipeline.py",
    "__init__.py",
    "exception.py",
    "logger.py",
    "utils.py"   
]

for filepth in list_of_files:
    filepath=Path(filepth)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    
    else:
        logging.info("file is already present at: {filepath}")