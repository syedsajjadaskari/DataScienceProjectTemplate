import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project Name:")
    if project_name != '':
        break

logging.info("creating project by name: {project_name}")
#list of files
list_of_files = [
    ".github/workflows/.gitkeep",#to perform github actions/workflows/empty file gitkeeps
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",#to perform tests init file
    f"tests/unit/__init__.py",#to perform unit tests
    f"tests/integration/__init_.py",#to perform integration test
    "init_setup.sh",#manage envirnment
    "requirements.txt",#user requirements
    "requirements_dev.txt",#developer requirements
    #"pyproject.toml",# pyproject.toml is the specified file format of PEP 518 which contains the build system requirements of Python projects.
    "setup.py",#to setup files
    "setup.cfg",#setup. cfg is an ini file, containing option defaults for setup.py commands
    "tox.ini",#helps to testing on various envirnments

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a directory as:{filedir} for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating a new file :{filename} ")
    else:
        logging.info(f"file is already present")

