from setuptools import find_packages,setup
from typing import List


def get_requirements()-> List[str]:
    """
        This func will return list of requirements
    
    """
    req_lst:List[str]=[]
    try:
        with open('req.txt','r') as file:
            
            #read line from the file

            lines = file.readlines()

            for line in lines:
                req = line.strip()
                if req and req !='-e .':
                    req_lst.append(req)
    except FileNotFoundError:
        print("req.txt not found")

    return req_lst

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author= "Pratham Vichare",
    author_email= "prathamvichare645@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)