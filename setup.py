import os
import sys
from distutils.core import setup

version = __import__('dynamicsiteslite').get_version()

setup(
    name='django-dynamicsites-lite',
    version=version,
    description="Host multiple sites from a single django project",
    long_description="""Expands the standard django.contrib.sites package to allow for:
    Sites identified dynamically from the request via middleware
    No need for multiple virtual hosts at the webserver level
    301 Redirects to canonical hostnames
    A site may have its own urls.py and templates
    A single site may accept requests from multiple hostnames
    Allows for environment hostname mappings to use non-production hostnames (for use in dev, staging, test, etc. environments)""",
    author='Ville Määttä',
    author_email='ville.maatta@ruriat.com',
    url='https://bitbucket.org/vmaatta/django-dynamicsites-lite',
    platforms=['any'],
    packages=['dynamicsiteslite'],
)
