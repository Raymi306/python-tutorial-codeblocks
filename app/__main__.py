"""Module for building and build-time QA of the python tutorial website"""
import json
from os import makedirs
import sys

from app.codeblocks import codeblocks
from app.qa import CodeblocksTester, BuildTestFailure


def run_build_checks():
    """QA for build process"""
    testers = (
            CodeblocksTester(),
            )
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
        json.dump(codeblocks, f)


if __name__ == '__main__':
    main()
