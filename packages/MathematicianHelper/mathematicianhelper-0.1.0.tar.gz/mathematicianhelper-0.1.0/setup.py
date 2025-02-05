from setuptools import setup, find_packages

with open("README.md",'r') as f:
    description= f.read()

setup(
    name="MathematicianHelper",
    version="0.1.0",
    description="A Python package for solving mathematical problems.",
    author="Lakshay",
    author_email="lakshaygoyal201@gmail.com",
    url="https://github.com/lakshay-goyal/MathematicianHelper",
    packages=find_packages(),
    install_requires=["numpy", "sympy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    long_description=description,
    long_description_content_type="text/markdown",
)