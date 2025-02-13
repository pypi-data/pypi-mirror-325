from setuptools import setup, find_packages

setup(
    name="dataframes",
    version='0.1',
    packages=find_packages(),
    requires=[
        'pandas',
        'numpy'
    ],
)
