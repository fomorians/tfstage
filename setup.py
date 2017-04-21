from setuptools import setup

setup(name='tfstage',
      version='0.1.0',
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
