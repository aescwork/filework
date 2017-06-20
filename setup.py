# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='filework',
    version='1.1.0',
    description='A simple class to make working with files easier.',
    long_description=long_description,
    url='https://github.com/aescwork/filework',
    author='Vollund Leysing',
    author_email='aescwork@protonmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='filework setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peppercorn'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
        'filework': ['package_data.dat'],
    },
    data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'filework=filework:main',
        ],
    },
)
