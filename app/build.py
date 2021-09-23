import doctest
from pathlib import Path
import sys

from jinja2 import Environment, PackageLoader
from markdown import markdown

from app import config
from app.links_test import run as run_link_test
from app.templates import TEMPLATES, base_html
import app.templates.codeblocks as codeblocks
from app.templates.links import links

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
    length = len(sys.argv)
    arg = None if not length > 1 else sys.argv[1]
    if arg != 'dev':
        test_codeblocks()
        test_links()
    env = Environment(
            loader=PackageLoader('app'),
            autoescape=False,
            )
    variables = {**codeblocks.codeblocks, **links}
    py_md_extensions = (
            'fenced_code',
            'codehilite',
            )
    base_html_template = env.get_template(base_html)
    for name in TEMPLATES:
        template = env.get_template(name)
        html = markdown(template.render(variables), extensions=py_md_extensions)
        final_render = base_html_template.render({'body_content': html})
        path = Path(config['DIST_PATH'], Path(name).stem).with_suffix('.html')
        with open(path, 'w') as f:
            f.write(final_render)

if __name__ == '__main__':
    build()
