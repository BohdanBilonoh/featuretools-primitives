from os import path

from setuptools import find_packages, setup

import pathlib
import pkg_resources
import tarfile

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='featuretools_primitives',
    version='0.0.1',
    author='Bohdan Bilonoh',
    author_email='bbilonog@gmail.com',
    classifiers=[
         'Development Status :: 2 - Pre-Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8'
    ],
    license='Apache License 2.0',
    url='https://github.com/BohdanBilonoh/featuretools_primitives',
    install_requires=open('requirements.txt').readlines(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7, <4',
    entry_points={
        'featuretools_plugin': [
            'custom_primitives = featuretools_primitives',
        ],
    },
)
