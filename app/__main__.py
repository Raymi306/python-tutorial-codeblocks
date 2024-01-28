"""Module for building and build-time QA of the python tutorial website"""
import inspect
import json
from os import makedirs
import sys

from app.codeblocks import get_func_body
from app.pages import first_steps, first_projects, variables
from app.qa import CodeblocksTester, BuildTestFailure


PAGE_MODULES = (
     first_steps,
     first_projects,
     variables,
 )


def run_build_checks():
    """QA for build process"""
    testers = (CodeblocksTester(PAGE_MODULES),)
    fail = False
    for tester in testers:
        try:
            tester.test()
        except BuildTestFailure:
            fail = True
    if fail:
        sys.exit(1)


def main():
    """
    Perform all of the actions necessary to output the python tutorial codeblocks
    """
    run_build_checks()
    makedirs('dist', exist_ok=True)
    with open('dist/codeblocks.json', 'w', encoding='utf-8') as f:
        json.dump(get_func_body, f)
        for module in PAGE_MODULES:
            for fn_name, fn in inspect.getmembers(module):
                print(fn_name, fn)


if __name__ == '__main__':
    main()
