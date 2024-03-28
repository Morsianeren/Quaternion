import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Find requirements.txt
with open('requirements.txt', encoding='UTF-8') as f:
    requirements = f.read().splitlines()

setup(
    name = "Quaternion",
    version = "1.0.0",
    author = "Magnus B. Klokker",
    author_email = "magnusklokker@hotmail.com",
    description = ("A package to handle quaternions"),
    license = "MIT",
    keywords = "quaternion",
    url = "https://github.com/Morsianeren/Quaternion",
    packages=['Quaternion'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires = requirements,
)