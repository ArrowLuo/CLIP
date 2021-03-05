import os

import pkg_resources
from setuptools import setup, find_packages
https://github.com/ArrowLuo/CLIP/blob/main/setup.py
setup(
    name="clip",
    py_modules=["clip"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
