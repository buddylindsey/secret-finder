"""Module setup."""

import runpy
from setuptools import setup, find_packages

PACKAGE_NAME = "secretfinder"
version_meta = runpy.run_path("./version.py")
VERSION = version_meta["__version__"]


with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author='Buddy Lindsey',
        url='https://github.com/buddylindsey/secret-finder',
        packages=find_packages(),
        install_requires=parse_requirements("requirements/base.txt"),
        scripts=[],
        description="Get your hard won secrets, simply",
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires=">=3.7",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        project_urls={
            'Documentation': 'https://github.com/buddylindsey/secret-finder',
            'Source': 'https://github.com/buddylindsey/secret-finder',
        },
    )
