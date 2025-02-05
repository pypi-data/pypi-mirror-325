#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='grip-nulling',
	 version='1.5.1',
    author='M.-A. Martinod',
    description='Self-calibration data reduction tools for nulling interferometry',
	 long_description='GRIP is a novel data reduction methods providing self-calibrated methods for nulling interferometry. Check https://github.com/mamartinod/grip for more information',
    packages=find_packages(),
    install_requires=[
		'numpy>=1.26.2',
		'scipy>=1.11.4',
		'matplotlib>=3.6.3',
		'h5py>=3.8.0',
		'emcee>=3.1.4',
		'numdifftools>=0.9.41',
		'astropy>=5.2.1'
    ],


)