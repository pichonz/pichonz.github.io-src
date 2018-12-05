#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.hedaro.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# The default metadata you want to use for all articles and pages.
DEFAULT_METADATA = {
  'description': 'Email Courses and Tutorials for Data Scientists'
}

# prevent tag pages from populating
TAGS_SAVE_AS = False
TAG_SAVE_AS = False
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

# Following items are often useful when publishing

DISQUS_SITENAME = 'hedaro'
GOOGLE_UNIVERSAL_ANALYTICS = "UA-72322029-1"
