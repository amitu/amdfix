# -*- coding: utf-8 -*-
from setuptools import setup

try:
    long_description = open('README.md', 'rt').read()
except Exception:
    long_description = ""

setup(
    name="amdfix",
    description="amdfix fixes AMD files",
    long_description=long_description,

    version="0.0.1",
    author='Amit Upadhyay',
    author_email="upadhyay@gmail.com",

    url='https://github.com/amitu/amdfix',
    license='BSD',

    install_requires=[
    ],
    packages=["amdfix"],
    entry_points={
        'console_scripts': ['amdfix=amdfix.__main__:main']
    },

    test_suite='tests',

    zip_safe=True,
)
