import sys
from setuptools import setup

args = ' '.join(sys.argv).strip()
if not any(args.endswith(suffix) for suffix in ['setup.py sdist', 'setup.py check -r -s']):
    raise ImportError('The package you are trying to install is not supported through PyPI. These packages are only available through the AWS Glue runtime.')

setup(
    name='amzn-awsgluemlpythonlibs',
    author='awsglue',
    version='0.0.1',
    description='AWS Glue ML Python Libs',
    classifiers=[
        'Development Status :: 7 - Inactive',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ]
)
