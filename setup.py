from setuptools import find_packages, setup
from typing import List

PROJECT_NAME="Machine Learning Project"
VERSION = '0.0.1'
DESCRIPTION = "This is ML project for end-to-end emplementation"
AUTHOR_NAME = "Ganesh Dhanawade"
AUTHOR_EMAIL = "dhanawadeganesh386@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHON_E_DOT = "-e ."
# Requriments.txt file open
# read
# \n ""

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [requriment_name.replace('\n', '') for requriment_name in requriment_list]

        if HYPHON_E_DOT in requriment_list:
            requriment_list.remove(HYPHON_E_DOT)

        return requriment_list
    
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list(),
      )
    