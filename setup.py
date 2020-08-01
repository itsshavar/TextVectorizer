#!/usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.install import install
import os

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class CustomInstall(install):
    def run(self):
        install.run(self)
        os.system("python -m spacy download en_core_web_sm")


setup(name='TextVectorizer',
      version='0.1.0',
      description='Feature Engineering for Textual Data',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Shashi Tripathi, Rahul Kumar Yadav',
      author_email='shashi.123.prakash@gmail.com,rahulkryadav93@gmail.com',
      url='https://github.com/itsshavar/TextVectorizer',
      packages=find_packages(exclude='test'),
      install_requires=['spacy', 'spacy-transformers'],
      cmdclass={'install': CustomInstall}
      )
