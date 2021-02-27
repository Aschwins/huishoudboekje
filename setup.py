import os

from setuptools import setup, find_packages

setup(
    name='huishoudboekje',
    version="0.0.1",
    packages=find_packages(where='src'),
    install_requires='',
    package_dir={
        '': 'src'
    },
    description='A python package to track expenses.',
    long_description_content_type='text/markdown',
)
