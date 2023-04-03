from setuptools import find_packages,setup
from typing import List

def get_requirements():
    """
    This function will return list of requirements
    """
    requirement_list=[]
    """
        write a code to read requirements.txt file and append each requirement in requirements_list variable
    """

    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="poonam",
    author_email="poonamgaba@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

