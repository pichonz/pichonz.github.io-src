#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Rojas'
SITENAME = 'Hedaro Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'
LOCALE = ('usa', 'en_US')

DEFAULT_LANG = 'English'

MARKUP = ('md', 'ipynb')

# plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# theme
THEME = "./pelican-themes/pelican-octopress-theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = 'brutalistpelican'
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
