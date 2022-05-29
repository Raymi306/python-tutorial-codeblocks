"""Module for building and build-time QA of the python tutorial website"""
from os import makedirs
from pathlib import Path
import sys

from jinja2 import Environment, PackageLoader, DebugUndefined
from markdown import markdown

from app import config
from app.templates import TEMPLATES, BASE_HTML
from app.templates.codeblocks import codeblocks
from app.templates.links import links
from app.qa import LinkTester, CodeblocksTester, UnresolvedTemplateVariablesTester


def run_build_checks(env, ctx):
    """QA for build process"""
    testers = (
            LinkTester(),
            CodeblocksTester(),
            UnresolvedTemplateVariablesTester(env, ctx),
            )
    for tester in testers:
        tester.test()


def render_templates(env, ctx):
    """
    Generator
    Render templates in correct order to produce a final render
    """
    py_md_extensions = (
            'attr_list',
            'fenced_code',
            'codehilite',
            'toc',
            )
    base_html_template = env.get_template(BASE_HTML)

    for name in TEMPLATES:
        template = env.get_template(name)
        html = markdown(
                template.render(ctx),
                extensions=py_md_extensions
                )
        final_render = base_html_template.render({'body_content': html})
        path = Path(config['DIST_PATH'], Path(name).stem).with_suffix('.html')
        yield final_render, path


def write_render(render, path):
    """Write final render to appropriate path"""
    args = sys.argv[1:]
    if 'dry-run' not in args:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render)


def build():
    """
    Perform all of the actions necessary to output the python tutorial webpages
    """
    env = Environment(
            loader=PackageLoader('app'),
            autoescape=False,
            undefined=DebugUndefined,
            )
    ctx = {**codeblocks, **links}
    run_build_checks(env, ctx)
    makedirs('dist', exist_ok=True)
    for render, path in render_templates(env, ctx):
        write_render(render, path)


if __name__ == '__main__':
    build()
