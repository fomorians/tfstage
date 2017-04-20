from setuptools import setup

from tfstage import __version__

setup(name='tfstage',
      version=__version__,
      description='TensorFlow experiment scaffolding.',
      url='http://github.com/fomorians/scaffold',
      author='Jim Fleming',
      author_email='jim@fomoro.com',
      license='MIT',
      packages=['tfstage'],
      scripts=['bin/tfstage'],
      install_requires=[
          'pystache',
      ],
      zip_safe=False)
