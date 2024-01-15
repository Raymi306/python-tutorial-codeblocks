"""Testers and test helpers for QA of tutorial"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import doctest


TIMEOUT_SEC = 10


class BuildTestFailure(BaseException):
    """Custom exception to indicate a build test failure"""


@dataclass(frozen=True)
class BuildTestResult:
    """Helper class to represent a build test result"""
    passed: bool
    output: list[str] = field(default_factory=list)


# pylint: disable=too-few-public-methods
class BuildTest(ABC):
    """Abstract class to build tests upon"""
    name = ''

    @abstractmethod
    def _test(self):
        """
        Children implement me
        Perform actions to ensure quality of tutorial
        """
        raise NotImplementedError

    def test(self):
        """Universal test logic"""
        test_result = self._test()
        print(f'\nTesting {self.name or self}')

        if not test_result.passed:  # only take action on failures
            print('  - Fail!')
            if test_result.output:
                print('Output:')
                for line in test_result.output:
                    print(f'  {line}')
            raise BuildTestFailure()
        print('  - Pass')


class CodeblocksTester(BuildTest):
    """Make sure the templated codeblocks do what the tutorial claims"""
    name = 'Codeblocks'

    def _test(self):
        from app import codeblocks  # pylint: disable=import-outside-toplevel
        failure_count, _ = doctest.testmod(
                codeblocks,
                verbose=None,
                report=False
                )
        return BuildTestResult(not bool(failure_count))
# pylint: enable=too-few-public-methods
