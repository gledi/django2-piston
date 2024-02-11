#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(
    name = "django2-piston",
    version = "2.2.4",
    url = 'https://github.com/wilsonchingg/django2-piston',
	download_url = 'https://github.com/wilsonchingg/django2-piston',
    license = 'BSD',
    description = "A Django Piston fork to make it compatible to Django 2 and Python 3",
    author = 'Wilson Ching',
    author_email = 'wilsonchingg96@gmail.com',
    packages = find_packages(),
    py_modules=['piston'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
