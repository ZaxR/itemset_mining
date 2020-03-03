#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import find_packages, setup

from itemset_mining


with open('itemset_mining/VERSION') as version_file:
    version = version_file.read().strip()

with open("README.md") as readme_file:
    readme = readme_file.read()

# Requirements placed here for convenient viewing
install_requires = []
tests_requires = ["pytest", "pytest-cov"]
docs_requires = ["m2r", "setuptools>=30.4", "Sphinx", "sphinx_rtd_theme"]
dev_requires = tests_requires + docs_requires + ["pre-commit", "tox"]

# Avoid setuptools as an entrypoint unless it's the only way to do it.
# In other words, only use setuptools to build dists and wheels.
# E.g.: Run tests with pytest or tox; build sphinx directly; etc.
setup(
    name=itemset_mining.__name__,
    version=version,
    description='A python package for itemset mining algorithms.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/zaxr/itemset_mining",
    author=itemset_mining.__author__,
    author_email=itemset_mining.__email__,
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                 "Natural Language :: English",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8"],
    keywords='high utility itemset mining data pattern huim apriori frequent',
    packages=find_packages(exclude=["docs", "tests"]),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={'docs': docs_requires,
                    'test': tests_requires,
                    'dev': dev_requires}
)
