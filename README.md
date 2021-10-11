# python-tutorial

## Brief summary
A tutorial with eventual content for both absolute beginners and experienced programmers.

Also note the github project board

## Libraries
[Python-Markdown](https://python-markdown.github.io/) - Converts Markdown to HTML

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Templating, used for links, codeblocks, and HTML

## Theoretical usage
After cloning the repository, create a virtual environment `python3 -m venv venv` and install all dependencies in requirements.txt `pip install -r requirements.txt`.
Then, run `python3 -m app.build` from the top level directory, and it should just work.
Theoretically.

Currently, the style sheet for pygments is being created using pygmentize cli:
`pygmentize -S solarized-light -f html -a .codehilite > dist/styles.css`
