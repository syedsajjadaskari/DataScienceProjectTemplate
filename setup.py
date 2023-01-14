import setuptools

with open("README.md", "r", encodeing="utf-8") as f:
    long_discription = f.read()

__version__ = "0.0.0"

REPO_NAME = "DataScienceProjectTemplate"
AUTHOR_USER_NAME = "syedsajjadaskari"
SRC_REPO = "DataScienceProjectTemplate"
AUTHOR_EMAIL = "syedsajjad62@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    authoe_email = AUTHOR_EMAIL,
    description = "Template for python data science project",
    long_discription_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)