import os
import sys

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

from titlecase import __version__

setup(name='titlecase',
    version=__version__,
    description="Python Port of John Gruber's titlecase.pl",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing :: Filters",
    ],
    keywords='string formatting',
    author="Pat Pannuto, Stuart Colville, John Gruber",
    author_email="pat.pannuto+titlecase@gmail.com",
    url="https://github.com/ppannuto/python-titlecase",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=['nose'],
    setup_requires=['nose>=1.0'],
    test_suite="titlecase.tests",
    entry_points = {
        'console_scripts': [
            'titlecase = titlecase.__init__:cmd',
            ],
        },
)

