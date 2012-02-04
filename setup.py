#!/usr/bin/env python

from distutils.core import setup
setup (
        name = 'markdown.extensions.superscript',
        py_modules = ['markdown.extensions.superscript'],
        package_dir = {'markdown.extensions': '.'},
        version = '0.9.0',
        description = 'A Superscript Extension for Markdown',
        author = 'Shane Graber',
        author_email = 'sgraber@gmail.com',
        url = 'https://github.com/sgraber/markdown.superscript',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        requires = [
            'markdown',
            'markdown.extensions'
        ],

)
