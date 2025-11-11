# setup.py
"""
Python Learning Repository Setup
Author: David Vaupel
"""

from setuptools import setup, find_packages

setup(
    name="python-learning",
    version="1.0.0",
    author="David Vaupel",
    author_email="221494616+MCCMDave@users.noreply.github.com",
    description="Python learning projects and practical automation scripts for homelab",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MCCMDave/python-learning",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.13",
    install_requires=[
        # Wenn du später externe Packages brauchst:
        # "requests>=2.31.0",
        # "python-dotenv>=1.0.0",
    ],
)