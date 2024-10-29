from setuptools import find_packages,setup
from typing import List

HYPEN_E_REQ="-e."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_REQ in requirements:
            requirements.remove(HYPEN_E_REQ)

setup(
name='MLproject',
version='0.0.1',
author='Dastaan',
author_email='harsh.singh.belwal278@gmail.com',
packages=find_packages(),
install_requires=get_requirements(requirements.txt)
)