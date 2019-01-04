#!/usr/bin/env python

import os
from os.path import exists, join
from setuptools import setup, find_packages
from datetime import datetime

today = datetime.now().isocalendar()

#: Generate the current version
version = "{0}.{1}.{2}".format(today[0]%100, today[1], today[2])

SCRIPTS = [join('bin', s) for s in ['datalab-demo']]
if os.name == "nt":
    SCRIPTS = [s+'.bat' for s in SCRIPTS]
elif os.name == "posix":
    SCRIPTS = [s + '.sh' for s in SCRIPTS]

setup(
    name='datalab-demo',
    version=version,
    author='David Koo',
    author_email='nuanguang.gu@intel.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=SCRIPTS,
    url='https://github.intel.com/datalab/datalab-demo',
    license=open('LICENSE').read() if exists("LICENSE") else "Intel Test Utilities Team",
    description='DataLab Demo Project',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    data_files=["LICENSE"],
    # Any requirements here
    install_requires=[
        'pyside;python_version<="2.7" and platform_system=="Windows"',
        'pyside2;python_version<="2.7" and platform_system!="Windows"',
        'pyside2;python_version>="3.6"',
        'pyqt5;python_version>="3.6"',
        'qt.py'
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)