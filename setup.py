##############################################################################
#
# Copyright (c) Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for refline.srccheck package
"""
import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="refline.srccheck",
    version='2.0.dev0',
    url="https://github.com/zopefoundation/refline.srccheck",
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'pyflakes',
        'polib',
        'cssutils',
    ],
    extras_require=dict(
        test=(
            'zope.testing',
            'zope.testrunner',
        ),
    ),
    packages=find_packages('src'),
    package_dir={'': 'src'},

    namespace_packages=['refline'],

    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    description="Source checking/linting tool",
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
    ),
    license='ZPL 2.1',
    keywords="zope zope3",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
