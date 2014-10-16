#!/usr/bin/env python

from distutils.core import setup

setup(name='tubestatus',
      version='0.1.0',
      install_requires=[
          "requests >= 2.3.0",
      ],
      description='Python interface to TFL\'s tube line status API',
      long_description='',
      author='Jacob Tomlinson',
      author_email='jacob@jacobtomlinson.co.uk',
      maintainer='Jacob Tomlinson',
      maintainer_email='jacob@jacobtomlinson.co.uk',
      url='https://github.com/jacobtomlinson/tube-status',
      license='TBC',
      packages=['tubestatus'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ]
     )
