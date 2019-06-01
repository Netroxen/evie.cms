# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

long_description = '\n\n'.join([
    open('CHANGES.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('README.rst').read(),
])

long_license = open('LICENSE.rst').read()

setup(
    name='Evie',
    version='0.0.1.dev0',
    packages=find_packages('evie'),
    description='A Python based CMS system.',
    long_description=open('README.rst').read(),
    author='Jesse Stippel',
    author_email='jesse.stippel@operun.de',
    include_package_data=True,
    install_requires=['quart'],
    license='MIT',
    long_license=long_license,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords='Python Evie CMS',
)
