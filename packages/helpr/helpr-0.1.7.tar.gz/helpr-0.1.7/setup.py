import os
from setuptools import setup, find_packages

def read_requirements(file):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path) as f:
        return f.read().splitlines()

def read_file(file):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path) as f:
        return f.read().strip()

long_description = read_file("README.rst")
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name="helpr",
    version=version,
    author="Clinikally",
    author_email="puneetsrivastava@clinikally.com",
    url="https://github.com/clinikally/helpr",
    description="A Python package to help you with your daily tasks",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires=">=3.6",
)
