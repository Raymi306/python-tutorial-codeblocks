from unittest.mock import patch
# pylint: disable=line-too-long
# pylint: disable=redefined-builtin


def variables_assignments():
    """
    >>> variables_assignments()
    4
    4
    """
    # pylint: disable-all
    def foo():
        return 4
    def bar():
        return 5
    def do_something(v1, v2):
        pass
    # pylint: enable-all
    # START
    # assignment as statement
    my_var = foo()
    if my_var:
        print(my_var)
    # assignment as expression, using 'walrus' operator
    # NOTE: The walrus operator only works on Python3.8+
    if my_var := foo():
        print(my_var)

    # a more complicated example
    if (var_1 := foo()) and (var_2 := bar()):
        do_something(var_1, var_2)
    # END

