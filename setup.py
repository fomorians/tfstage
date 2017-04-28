"""
Setup module.
"""

from os import path
from setuptools import setup

REQUIRED_PACKAGES = []
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(name='tfstage',
      version='0.1.0',
      description='TensorFlow project scaffolding',
      long_description=LONG_DESCRIPTION,
      url='http://github.com/fomorians/tfstage',
      author='Jim Fleming',
      author_email='jim@fomoro.com',
      license='MIT',
      packages=['tfstage'],
      scripts=['bin/tfstage'],
      install_requires=[
          'termcolor',
          'pystache'
      ],
      zip_safe=False)
