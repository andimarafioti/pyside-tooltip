# coding: utf-8
from setuptools import setup

__author__ = 'Andres'


setup(name='pyside-tooltip',
      version='0.1.1',
      description='Custom tooltip extension for pyside',
      url='https://github.com/andimarafioti/pyside-tooltip',
      author='Andres Marafioti',
      author_email='andimarafioti@gmail.com',
      license='MIT',
      packages=['pyside_tooltip'],
      install_requires=[
          'PySide',
      ],
      zip_safe=False)
