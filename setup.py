#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='sudo-lecturer',
      version='0.1',
      description='Rotate lectures given to user whenever a lecture file has been used',
      url='http://github.com/yunchih/lecturer',
      author='Yunchih Chen',
      author_email='yunchih@csie.ntu.edu.tw',
      license='MIT',
      packages = ['lecturer'],
      install_requires=['pyinotify'],
      scripts=['bin/daemon'],
      zip_safe=True)
