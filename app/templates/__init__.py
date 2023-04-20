"""Exposes Markdown and HTML templates and provides data for templating"""
import glob
import os
import sys


if sys.version_info >= (3, 10):
    TEMPLATES = tuple(glob.glob('*.md', root_dir=os.path.dirname(__file__)))  # pylint: disable=unexpected-keyword-arg
else:
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    TEMPLATES = tuple(glob.glob('*.md'))
    os.chdir(cwd)
BASE_HTML = 'base.html'
