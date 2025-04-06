import os
from setuptools import setup, find_packages

# Define the package metadata
PACKAGE_NAME = "mymathlib_ismail11_shma"
VERSION = "0.1.0"
DESCRIPTION = "A simple math library for basic arithmetic operations"
AUTHOR = "Your Name"
AUTHOR_EMAIL = "your.email@example.com"
URL = "https://github.com/yourusername/mymathlib"

# Read the long description from README.md if available
LONG_DESCRIPTION = """A simple math library that provides addition, subtraction, multiplication, and division functions.

## Installation
```sh
pip install mymathlib_ismail11_shma
```

## Usage
```python
from mymathlib.arithmetic import add, subtract, multiply, divide

print(add(2, 3))  # Output: 5
print(subtract(5, 2))  # Output: 3
print(multiply(4, 3))  # Output: 12
print(divide(10, 2))  # Output: 5.0
```
"""

# Define the package structure
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
)
