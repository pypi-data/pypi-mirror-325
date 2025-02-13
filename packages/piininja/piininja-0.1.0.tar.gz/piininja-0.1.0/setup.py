from setuptools import setup, find_packages

setup(
    name='piininja',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl'
    ],
    description='Ninja-like data anonymization library',
    long_description=open('README.md').read(),
    author='Abdullah Md. Shamim',
    author_email='abdullahshamim7584@gmail.com',
    url='https://github.com/abdullahshamim007/piininja',
)