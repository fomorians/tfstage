"""
Setup module.
"""

import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(name='tfstage',
      version='0.1.3',
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
      packages=find_packages(),
      package_data={'tfstage': ['*']},
      scripts=['bin/tfstage'],
      install_requires=[
          'termcolor',
          'pystache'
      ],
      include_package_data=True,
      zip_safe=False)
