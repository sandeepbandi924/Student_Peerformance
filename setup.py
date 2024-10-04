from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This FUnction Return list of Requirements'''
    requiremets=[]
    with open(file_path) as file_obj:
        requiremets=file_obj.readlines()
        requiremets=[req.replace('\n','') for req in requiremets]
        
        if HYPHEN_E_DOT in requiremets:
            requiremets.remove(HYPHEN_E_DOT)
    return requiremets

setup(
    name='Student Performance Prediction',
    version='1.0',
    author='Sandeep Bandi',
    author_email='bandisandeep1374@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)