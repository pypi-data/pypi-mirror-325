# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:40:26 2024

@author: HOME
"""

from setuptools import setup, find_packages

setup(
    name='pushover_ml',
    version='1.4.2',
    author='Carlos Angarita',
    author_email='carlosantr@unisabana.edu.co',
    packages=find_packages(),
    include_package_data=True,  # Permite incluir datos adicionales (pkl, etc.)
    description='User-friendly Graphical User Interface (GUI) to efficiently predict a trilinear approximation of pushover curves for low-rise reinforced concrete (RC) frame buildings, using a Machine Learning (ML) based approach.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'matplotlib>=3.9.1',  # Any version of matplotlib
        'numpy>=1.26.4',  # Any version of numpy
        'joblib>=1.4.2',
        'scikit-learn==1.2.1',
        'tensorflow==2.17.0',
        'keras>=3.4.1',
        'openpyxl>=3.1.5',
        'Xlsxwriter>=3.2.0',
        'pandas>=2.2.2'
    ],
    entry_points={
        'console_scripts': [
            'pushover-ml=pushover_ml.GUI:open_gui',  # Permite usar "pushover-ml" en terminal
        ],
    },
    python_requires='>=3.9', # Adjust based on your compatibility
    url='https://github.com/carlosantr/Pushover-ML_repository',
    license='Apache-2.0', # If you have a license file
)