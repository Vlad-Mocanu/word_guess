# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='word_guess',
    version='1.0.0',
    description='Word guess algorithm for providing help in playing Wordle ',
    long_description=long_description,
    url='https://github.com/Vlad-Mocanu/word_guess',
    author='Vlad Mocanu',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 3.7.3'
    ],
    keywords='words wordle guess',
    install_requires=[
        'numpy==1.21.0',
        'pyyaml>=6.0',
        'wolframclient>=1.1.7'
    ]
)
