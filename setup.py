#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy',
                'scipy',
                'matplotlib',
                'astropy',
                ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'healpy', 'jupyter', 'nbconvert']

setup(
    author="Jeffrey Shafiq Hazboun",
    author_email='jeffrey.hazboun@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python package for making visuals of gravitational wave signals, specifically pulsar timing array signals. ",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    package_data={'gw_sky': ['data/*.npy','data/*.npz']},
    keywords='gw_sky',
    name='gw_sky',
    packages=find_packages(include=['gw_sky']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Hazboun6/gw_sky',
    version='0.1.0',
    zip_safe=False,
)
