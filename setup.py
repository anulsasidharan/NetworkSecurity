'''
The setup.py file is an essential part of packaging and distribution of the pythn projects. 
IT is used by setuptools(od distutils in older versions of python) to define the configuration of your project,
such as its metadata, dependencies and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will retuen list of requirements.

    """
    requirement_list:List[str] = [] 
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines form the file
            lines = file.readlines()
            # Process each lines
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement) 
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

# print(get_requirements())

setup(

    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Anu L Sasidharan",
    author_email= "anulsasidharan@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)