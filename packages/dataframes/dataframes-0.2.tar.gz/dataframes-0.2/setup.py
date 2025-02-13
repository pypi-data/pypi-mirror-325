from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name="dataframes",
    version='0.2',
    packages=find_packages(),
    requires=[
        'pandas',
        'numpy'
    ],
    long_description=description,
)
