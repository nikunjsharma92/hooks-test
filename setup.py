#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='0.0.2',
      description='This is a test hooks package.',
      author='Nikunj Sharma',
      author_email='nikunj.sharma92@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
