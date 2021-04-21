import os
import sys

from setuptools import setup, find_packages

def read_file(rel_path):
    abs_dir_path = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(abs_dir_path, rel_path)
    with open(abs_path, encoding='UTF-8') as f:
        return f.read()

def read_version(rel_path):
    for line in read_file(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError('No version string found')

setup(name='titlecase',
    version=read_version('titlecase/__init__.py'),
    description="Python Port of John Gruber's titlecase.pl",
    long_description=read_file('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
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
    tests_require=['nose>=1.0', 'regex>=2020.4.4'],
    extras_requires=['regex>=2020.4.4'],
    test_suite="titlecase.tests",
    entry_points = {
        'console_scripts': [
            'titlecase = titlecase.__init__:cmd',
            ],
        },
)
