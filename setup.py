__version__ = '0.4'

import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

setup(name='titlecase',
    version=__version__,
    description="Python Port of John Gruber's titlecase.pl",
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing :: Filters",
    ],
    keywords='string formatting',
    author="Stuart Colville",
    author_email="pypi@muffinresearch.co.uk",
    url="http://www.muffinresearch.co.uk/",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="titlecase.tests",
    entry_points = """\
    """
)

