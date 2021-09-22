import doctest
import sys

from jinja2 import Environment, PackageLoader
from markdown import markdown

from app.links_test import run as run_link_test
from app.templates import TEMPLATES
from app.templates.links import links
import app.templates.codeblocks as codeblocks
# TODO need a config file

def test_codeblocks():
    """Make sure the templated codeblocks do what I say they do"""
    failure_count, _ = doctest.testmod(codeblocks)
    if failure_count:
        print('CODEBLOCK DOCTESTS MUST PASS')
        sys.exit(1)

def test_links():
    """Make sure all templated links are good"""
    fails = run_link_test(links.values())
    if fails:
        print('LINK TESTS MUST PASS')
        for f in fails:
            print(f.url, f.status)
        sys.exit(1)

def build():
    """Render jinja templates and pass result into markdown, writing generated html to package dist"""
    test_codeblocks()
    test_links()
    env = Environment(
            loader=PackageLoader('app'),
            autoescape=False,
            )
    variables = {**codeblocks.codeblocks, **links}

    for name in TEMPLATES:
        template = env.get_template(name)
        convert_to_md(template.render(variables), name)

def convert_to_md(render, filename):
    """Using python-markdown, convert the rendered markdown into html"""
    extensions = (
            'fenced_code',
            'codehilite',
            )
    name = ''.join(filename.split('.')[0:-1]) # TODO use pathtools
    with open(f'dist/{name}.html', 'w') as f:
        html = markdown(render, extensions=extensions)
        f.write(html)

if __name__ == '__main__':
    build()
