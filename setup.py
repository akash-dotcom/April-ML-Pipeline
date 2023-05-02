from setuptools import setup,find_packages
# from distutils.core import setup
from typing import List

PROJECT_NAME="ML project"
VERSION="0.0.1"
AUTHOR="Akash Saini"
DESCRIPTION="This is our project"
HYPHEN_E_DOT="-e ."
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirement_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
      name=PROJECT_NAME,
      version=VERSION,
      author=AUTHOR,
      description=DESCRIPTION,
      packages=find_packages(),
      install_requires=get_requirement_list()
      )
