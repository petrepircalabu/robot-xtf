#!/usr/bin/env python

from sys import platform

requires = {}

try:
    from setuptools import setup

    if not platform.startswith('java'):
        requires = {
            'install_requires': ['robotframework'],
        }
except ImportError:
    from distutils.core import setup

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: BSD 2-Clause
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-xtflibrary',
    version='0.1', 
    description='Robot Framework library for XEN Test Framework',
    long_description='Robot Framework library for XEN Test Framework',
    author='Petre Pircalabu',
    author_email='ppircalabu@bitdefender.com',
    url='https://github.com/petrepircalabu/robot-xtf',
    license='BSD 2-Clause',
    keywords='robotframework testing testautomation xen xtf',
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    packages=['XTFLibrary'],
    **requires
)
