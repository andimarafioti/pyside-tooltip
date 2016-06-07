# coding: utf-8
from setuptools import setup

__author__ = 'Andres'


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyside-tooltip',
      version='0.2.1',
      description='Custom tooltip extension for pyside',
      long_description=readme(),
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: Developers'
      ],

      url='https://github.com/andimarafioti/pyside-tooltip',
      author='Andres Marafioti',
      author_email='andimarafioti@gmail.com',
      license='MIT',
      packages=['pyside_tooltip', 'pyside_tooltip/positioning'],
      install_requires=[
          'PySide',
      ],
      zip_safe=False)
