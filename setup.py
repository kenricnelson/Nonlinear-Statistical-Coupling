import os
from setuptools import setup, find_packages

PACKAGE_NAME = "nsc_test"

here = os.path.abspath(os.path.dirname(__file__))
info = {}
with open(os.path.join(here, PACKAGE_NAME, '__version__.py'), 'r') as f:
    exec(f.read(), info)


setup(
    name=info['__title__'],
    author=info['__author__'],
    description=info['__description__'],
    url=info['__url__'],
    version=info['__version__'],
    license=info['__license__'],
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    python_requires='>= 3.6',
    install_requires=[
        'numpy',
        'scipy'
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Operating System :: OS Independent",
    ],
)
