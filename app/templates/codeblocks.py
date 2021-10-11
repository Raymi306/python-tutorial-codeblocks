"""Exports doctested, minimal codeblocks for templating"""
import inspect
from unittest.mock import patch


def normalize_indentation(line, set_level, level):
    """Remove unnecessary indentation resulting from doctesting of code"""
    counter = 0
    length = len(line)
    while counter < length - 1 and line[counter] == ' ':
        counter += 1
    if set_level:
        level = int(counter / 4)
        result = line[4 * level:], level
    else:
        index = 4 * level
        result = line[index:], level
    return ''.join(result[0]) + '\n', result[1]


def get_func_body(name):
    """
    Remove docstrings, indentation, and testing artifacts from function
    indicated by name for use with templating as a codeblock

    Functions can be marked with # START and # END comments for special
    trimming of testing code
    """
    raw = inspect.getsource(name)
    lines = raw.split('\n')[1:]
    set_level = True
    level = None
    result = []
    if '# START' in raw and '# END' in raw:
        take = False
        for line in lines:
            if '# END' in line:
                take = False
            if take:
                line, level = normalize_indentation(line, set_level, level)
                set_level = False
                result.append(line)
            if '# START' in line:
                take = True
        return ''.join(result).strip()
    docstring_occurences = 0
    for line in lines:
        if docstring_occurences >= 2:
            line, level = normalize_indentation(line, set_level, level)
            set_level = False
            result.append(line)
        if '"""' in line:
            docstring_occurences += 1
    return ''.join(result).strip()


# pylint: disable=line-too-long
# pylint: disable=redefined-builtin
def hello_world():
    """
    >>> hello_world()
    Hello world
    """
    print('Hello world')


def input_noop():
    """
    >>> input_noop()
    """
    with patch('builtins.input') as input:
        # START
        input()
        # END


def input_and_print(mocked_input_ret):
    """
    >>> input_and_print('hello')
    You typed: hello
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_variable = input()
        print('You typed: ' + my_variable)
        # END


def input_and_print_twice(mocked_input_ret):
    """
    >>> input_and_print_twice('7')
    77
    >>> input_and_print_twice('foo')
    foofoo
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        print(my_number * 2)
        # END


def input_and_print_double_v1(mocked_input_ret):
    """
    >>> input_and_print_double_v1('7')
    14
    >>> input_and_print_double_v1('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = int(input())
        print(my_number * 2)
        # END


def input_and_print_double_v2(mocked_input_ret):
    """
    >>> input_and_print_double_v1('7')
    14
    >>> input_and_print_double_v1('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        print(int(my_number) * 2)
        # END


def input_and_print_double_v3(mocked_input_ret):
    """
    >>> input_and_print_double_v1('7')
    14
    >>> input_and_print_double_v1('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        print(int(input()) * 2)
        # END


def input_and_print_double_v4(mocked_input_ret):
    """
    >>> input_and_print_double_v1('7')
    14
    >>> input_and_print_double_v1('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        my_number = int(my_number)
        print(my_number * 2)
        # END


def futures_try_int_input(mocked_input_ret):
    """
    >>> futures_try_int_input(4)
    8
    >>> futures_try_int_input('q')
    That's not a number!
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number_as_string = input()
        try:
            my_number = int(my_number_as_string)
        except ValueError:
            # Python has several builtin error types, knowing when and how to reference the documentation is a valuable skill in its own right
            print('That\'s not a number!')
        else:
            print(my_number * 2)
        # END


def conditions_names(mocked_input_ret):
    """
    >>> conditions_names('max')
    weeb
    >>> conditions_names('jax')
    cool name!
    >>> conditions_names('foobarbaz')
    Hello, foobarbaz
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        user_input = input('What\'s your name?')
        if user_input == 'max':
            print('weeb')
        elif user_input == 'jax':
            print('cool name!')
        else:
            print('Hello, ' + user_input)
        # END


# pylint: disable=using-constant-test
def conditions_indent():
    """
    >>> conditions_indent()
    True is true...
    You'll see this get printed too!
    """
    if True:
        print('True is true...')
        print('You\'ll see this get printed too!')
# pylint: enable=using-constant-test


def loops_scream():
    """
    NO TEST
    """
    while True:
        print('hewwo???')


def loops_input_to_break(mocked_input_se):
    """
    >>> loops_input_to_break(('q',))
    >>> loops_input_to_break(('foo', 'q'))
    You said, foo
    """
    with patch('builtins.input') as input:
        input.side_effect = mocked_input_se
        # START
        while True:
            user_input = input('Type \'q\' to exit')
            if user_input == 'q':
                break
            # An alternate way to format strings, note the f before the lead quote, and the braces around the variable name
            print(f'You said, {user_input}')
        # END


def loops_2_var_counter(mocked_input_se):
    """
    >>> loops_2_var_counter(('q', 'q', 'q'))
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    >>> loops_2_var_counter(('q', 'foo', 'q', 'q'))
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    """
    with patch('builtins.input') as input:
        input.side_effect = mocked_input_se
        # START
        counter = 0
        target = 3
        while counter < target:
            val = input(f'You have typed \'q\' {counter} times. Type \'q\' and press enter {target - counter} times to exit.\n')
            if val == 'q':
                counter += 1 # equivalent to `counter = counter + 1`
            print('Loopedy loop...')
        # END


def loops_weird_continue():
    """
    >>> loops_weird_continue()
    2
    4
    6
    8
    10
    """
    num = 0
    while num <= 10:
        num += 1
        if num % 2:
            continue
        print(num)


# names of functions to be exported as codeblocks
CODEBLOCK_NAMES = (
    'hello_world',
    'input_noop',
    'input_and_print',
    'input_and_print_twice',
    'input_and_print_double_v1',
    'input_and_print_double_v2',
    'input_and_print_double_v3',
    'input_and_print_double_v4',
    'futures_try_int_input',
    'conditions_names',
    'conditions_indent',
    'loops_scream',
    'loops_input_to_break',
    'loops_2_var_counter',
    'loops_weird_continue',
    )

locals_proxy = locals()
codeblocks = {
        func_name: get_func_body(
            locals_proxy[func_name]
            ) for func_name in CODEBLOCK_NAMES
        }
