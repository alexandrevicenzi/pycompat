#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    description = f.read()

setup(
    name='pycompat',
    version='0.3.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    packages=['pycompat'],
    url='https://github.com/alexandrevicenzi/pycompat',
    bugtrack_url='https://github.com/alexandrevicenzi/pycompat/issues',
    license=license,
    description='Library to check Python and System version in a easy way',
    long_description=description,
    keywords='python, system, sys, info, compatibility, py2to3',
    platforms='',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Topic :: System',
          'Topic :: Utilities',
          ],
)
