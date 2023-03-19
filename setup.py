from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="FinancialFraudDetection"
VERSION="0.0.1"
AUTHOR="Arun khare"
DESRCIPTION="Rajasthan IT Day Hackathon Project "
SRC_REPO = "frauddetection"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
long_description=long_description,
long_description_content="text\markdown",
url=f"https://github.com/{AUTHOR}/{SRC_REPO}",
project_urls={
   "Bug Tracker": f"https://github.com/{AUTHOR}/{SRC_REPO}/issues",
},
package_dir={"": "src"},
packages=find_packages(where="src")
)

