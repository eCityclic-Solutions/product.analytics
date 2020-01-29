# -*- coding: utf-8 -*-
"""Installer for the product.analytics package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='product.analytics',
    version='1.0a1',
    description="Integration with Google Analytics",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='csanahuja',
    author_email='csanahuja10@gmail.com',
    url='https://gitlab.com/csanahuja/product.analytics/',
    project_urls={
        # 'PyPI': 'https://pypi.python.org/pypi/product.analytics',
        # 'Documentation': 'https://product.analytics.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['product'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'z3c.jbot',
        'google-api-python-client==1.7.11',
        'uritemplate==3.0.1',
        'google-auth-httplib2==0.0.3',
        'httplib2==0.17.0',
        'google-auth==1.11.0',
        'rsa==4.0',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'cachetools==4.0.0',
        'oauth2client==4.1.3',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = product.analytics.locales.update:update_locale
    """,
)
