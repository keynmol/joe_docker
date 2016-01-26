from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='joe_docker',
      version=version,
      description="Piss easy container infrastructure 'manager'",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='docker',
      author='Anton Sviridov',
      author_email='keynmol@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      scripts = ['bin/joe_docker']
      )
