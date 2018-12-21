#! /usr/bin/env python

from setuptools import setup, find_packages
from flask_error_handling import __version__


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='flask_error_handling',
      version=__version__,
      license='PSF',
      description='Flask Error Handling provides bindings to register Exceptions with HTTP status codes.',
      long_description=readme(),
      author='Andrew Droffner',
      author_email='ad718x@us.att.com',
      url='https://codecloud.web.att.com/projects/ST_TITAN/repos/flask-error-handling/browse',
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=[
      ],
      scripts=[],
      # NO nosetests: junitparser.TestSuite confuses nose, testing ERRORs
      test_suite='nose.collector',
      # tests_require=['nose>=1.3.7', 'coverage>=4.4.1'],
      # NOTE: ./setup.py nosetests <= needs "setup_requires"
      setup_requires=[
          'coverage>=4.5.2',
          'flake8>=3.6.0',
          'Flask>=1.0.2',
          'nose>=1.3.7',
          'parameterized>=0.6.1',
      ],
      keywords=[
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ])
