from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.rst")
version = read_file("VERSION").strip()
requirements = read_requirements("requirements.txt")

setup(
    name = 'helpr',
    version = version,
    author = 'Clinikally',
    author_email = 'puneetsrivastava@clinikally.com',
    url = 'https://github.com/clinikally/helpr',
    description = 'A Python package to help you with your daily tasks',
    long_description_content_type = "text/x-rst",
    long_description = long_description,
    license = "MIT license",
    packages = find_packages(),  # This will find the helpr directory
    package_dir = {"": "."},    # Add this line
    install_requires = requirements,
    python_requires = ">=3.7",  # Add this line
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)