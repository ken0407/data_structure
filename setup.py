# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_pth = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
	requirements = [line.rstrip() for line in f]
    return requirements 

with open('LICENSE') as f:
    license = f.read()

setup(
    name='data_structure',
    version='0.1.0',
    description='practice of data and structure.',
    author='Kentaro Ishii',
    author_email='kentaro.ishii0407@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/kentaro0407/data_structure',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

