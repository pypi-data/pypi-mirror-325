# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# README.md 파일을 UTF-8로 명시적으로 읽기
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="openFourier",
    version="0.1.2",
    author="WonwooPark",
    author_email="bemore.one@gmail.com",
    description="A package for computing 2D Fourier transform amplitude spectrum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bemoregt/openFourier",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
    ],
)