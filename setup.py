from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboBandit',
    version='1.1',
    packages=[''],
    package_dir={'': 'robobandit'},
    url='https://www.github.com/we45/RoboBandit',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for Python\'s Bandit SAST Product and PyUP Safety SCA Scanner for Python' ,
    install_requires=[
        'docker',
        'robotframework==3.0.4'
    ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)
