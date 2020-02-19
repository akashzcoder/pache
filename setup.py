import sys

from setuptools import find_packages, setup

if {"pytest", "test", "ptr"}.intersection(sys.argv):
    setup_requires = ["pytest-runner"]
else:
    setup_requires = []

setup(
    name="pache",
    description="Python Caching Library",
    version="0.0.1",
    author="Akash",
    author_email="akashsingh.zcoder@gmail.com",
    setup_requires=setup_requires,
    license="MIT",
    packages=find_packages(),
)
