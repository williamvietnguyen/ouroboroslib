from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A Graph Abstract Data Type'

# Setting up
setup(
    name="ouroboroslib",
    version=VERSION,
    author="William Nguyen",
    author_email="williamvnguyen2@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    url="https://github.com/williamvietnguyen/ouroboroslib",
    keywords=['python', "graph", "data", "structure", "data-structure"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3.9',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
