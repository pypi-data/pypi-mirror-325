from setuptools import setup, find_packages

setup(
    name='hawk-sdk',
    version='0.0.7',
    packages=find_packages(),
    install_requires=[
        'google-cloud-bigquery',
        'pandas'
    ],
)
