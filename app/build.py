from markdown import markdown
from jinja2 import Environment, PackageLoader

from app.templates import codeblocks, links
# TODO need a config file

def build():
    """Render jinja templates and pass result into markdown, writing generated html to package dist"""
    env = Environment(
            loader=PackageLoader('app'),
            autoescape=False,
            )

    variables = codeblocks
    variables.update(links)
    templates = ( # TODO load this from directory
            'misc.md',
            '00_installation.md',
            '01_how_to_run_code.md',
            '10_first_steps.md',
            )

    for name in templates:
        template = env.get_template(name)
        convert_to_md(template.render(variables), name)

def convert_to_md(render, filename):
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
