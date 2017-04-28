"""
Setup module.
"""

from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.rst')) as f:
    LONG_DESCRIPTION = f.read()

setup(name='tfstage',
      version='0.1.1',
      description='TensorFlow project scaffolding',
      long_description=LONG_DESCRIPTION,
      url='http://github.com/fomorians/tfstage',
      author='Jim Fleming',
      author_email='jim@fomoro.com',
      license='MIT',
      keywords='tensorflow scaffold scaffolding',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Code Generators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
      packages=['tfstage'],
      scripts=['bin/tfstage'],
      install_requires=[
          'termcolor',
          'pystache'
      ],
      zip_safe=False)
