#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-singletons',
    use_scm_version={'version_scheme': 'post-release'},
    description='Reusable singleton models for Django',
    author='Thomas Ashelford',
    author_email='thomas@ether.com.au',
    url='http://github.com/tttallis/django-singletons',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)