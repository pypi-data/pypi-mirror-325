# setup.py
from setuptools import setup, find_packages

setup(
    name='my_test_package_XyZEFg',
    version='0.1.1',
    packages=find_packages(),
    description='A simple test package for PyPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Julia Joseph',
    classifiers=['Programming Language :: Python'],
    python_requires='>=3.6'
)