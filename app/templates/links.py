"""Exports links for templating"""
from app import config

BASE_URL = config['TUTORIAL_BASE_URL']

links = {
        'ext_github_repo': 'https://github.com/Raymi306/python-tutorial',
        'ext_python_dl_page': 'https://www.python.org/downloads/windows/',
        'int_home': config['HOMEPAGE_URL'],
        'int_index': f'{BASE_URL}/index.html',
        'int_misc': f'{BASE_URL}/misc.html',
        'int_misc_paths': f'{BASE_URL}/misc.html#path-variables',
        'int_misc_shells': f'{BASE_URL}/misc.html#command-prompts-shells-terminals',
        'int_misc_text_editors': f'{BASE_URL}/misc.html#common-text-editors',
        'int_misc_file_paths': f'{BASE_URL}/misc.html#file-paths',
        'int_installation': f'{BASE_URL}/00_installation.html',
        'int_running_code': f'{BASE_URL}/01_how_to_run_code.html',
        'int_programming_overview': f'{BASE_URL}/02_programming_overview.html',
        'int_first_steps': f'{BASE_URL}/10_first_steps.html',
        }
