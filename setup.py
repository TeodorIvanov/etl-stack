import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='etl_stack',
    url='https://gitlab.aiidatapro.net/teodor/etl-stack',
    version='0.0.1',
    # namespace_packages=['adp', 'adp.elastic_doctypes'],
    packages=[p for p in find_packages() if p.partition('.')[0] == 'adp'],
    include_package_data=True,
    license='MIT',
    install_requires=[
        'joblib',
        'tqdm',
    ],
    description='Flexible class-based ETL pipelines',
    author='Teodor Ivanov',
    author_email='teodor.ivanov@adata.pro',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
    ],
)
