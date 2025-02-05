# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:  # Explicit UTF-8 encoding
    long_description = fh.read()

setup(
    name="accounda",
    version="0.1.0",
    description="A Python library for interaction with the Accounda API.",
    long_description=long_description,  # Adds a long description for PyPI
    long_description_content_type="text/markdown",  # Tells PyPI to interpret as Markdown
    author="Accounda",
    author_email="service@accounda.com",
    url="https://github.com/alexander-zotter/accounda-client",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
