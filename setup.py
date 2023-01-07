from setuptools import find_packages,setup
from typing import List

REQ_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(REQ_FILE_NAME) as req_file:
        req_list = req_file.readlines()
    req_list = [req_name.replace("\n","") for req_name in req_list]
    if HYPHEN_E_DOT in req_list:
        req_list.remove(HYPHEN_E_DOT)
    return req_list


setup(
    name="sensor",
    version="0.0.1",
    author="Atharv Kulkarni",
    author_email="atharv4study@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)