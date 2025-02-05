from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
working_directory = path.abspath(path.dirname(__file__))
with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Setup the package
setup(
    name='aesFileEncryptionManager',
    version='1.0.1',
    author='Zorba1973',
    author_email='zorba1973@gmail.com',
    description='A simple encryption manager to encrypt and decrypt files using AES encryption.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zorba1973/aesFileEncryptionManager',
    packages=find_packages(),
    install_requires=[
        'pycryptodome>=3.21.0'
    ],
    entry_points={
        'console_scripts': [
            'aesFileEncryptionManager=aesFileEncryptionManager.encryptionManager:main',
        ],
    },

)


