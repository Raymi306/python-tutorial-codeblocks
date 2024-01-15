"""Module for building and build-time QA of the python tutorial website"""
import argparse
from os import makedirs
from pathlib import Path
import sys

from jinja2 import Environment, PackageLoader, DebugUndefined
from markdown import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension

from app import config
from app.templates import TEMPLATES, BASE_HTML
from app.templates.codeblocks import codeblocks
from app.templates.links import links
from app.qa import (
    LinkTester, CodeblocksTester, UnresolvedTemplateVariablesTester, BuildTestFailure
)

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dry-run',
    action="store_true",
    help="""
    Do not write any files or directories.
    Still perform network requests for link checks
    """
)
parser.add_argument(
    '--warn-links',
    action="store_true",
    help="Do not error on link checker failures",
)

def run_build_checks(env, ctx, args):
    """QA for build process"""
    testers = (
            LinkTester(warn=args.warn_links),
            CodeblocksTester(),
            UnresolvedTemplateVariablesTester(env, ctx),
            )
    fail = False
    for tester in testers:
        try:
            tester.test()
        except BuildTestFailure:
            fail = True
    if fail:
        sys.exit(1)


def render_templates(env, ctx):
    """
    Generator
    Render templates in correct order to produce a final render
    """
    py_md_extensions = (
            'attr_list',
            'fenced_code',
            CodeHiliteExtension(guess_lang=False),
            TocExtension(toc_depth='2-6', anchorlink=True),
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
    with open(path, 'w', encoding='utf-8') as f:
        f.write(render)


def main(args):
    """
    Perform all of the actions necessary to output the python tutorial webpages
    """
    env = Environment(
            loader=PackageLoader('app'),
            autoescape=False,
            undefined=DebugUndefined,
            )
    ctx = {**codeblocks, **links}
    run_build_checks(env, ctx, args)
    if not args.dry_run:
        makedirs('dist', exist_ok=True)
        for render, path in render_templates(env, ctx):
            write_render(render, path)


if __name__ == '__main__':
    args_ = parser.parse_args()
    main(args_)
