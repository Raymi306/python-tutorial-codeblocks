"""Exposes Markdown and HTML templates and provides data for templating"""
import glob
import os


TEMPLATES = tuple(glob.glob('*.md', root_dir=os.path.dirname(__file__)))
BASE_HTML = 'base_html.html'
