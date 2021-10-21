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

        # preview of the future
        # if we begin a line with a '#', Python will ignore it
        # these lines are called comments
        # they can be useful for documenting important things in your code
        # leaving notes for yourself and others can be very important as you write more code
        # its not uncommon to return to code after just a week away and have no idea where you left off or why...

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

def conditions_boolean_logic():
    """
    >>> conditions_boolean_logic()
    One is Foo!
    Same length OR combined length longer than ten!
    """

    # Experimenting with conditional logic can be more convenient in the interpreter
    var_1 = 'Foo'
    var_2 = 'Bar'

    if var_1 == 'Foo' and var_2 == 'Foo':
        print('All Foo!')

    if var_1 == 'Foo' or var_2 == 'Foo':
        print('One is Foo!')

    if not var_1 or not var_2:
        print('One is falsey!')

    length_var_1 = len(var_1)
    length_var_2 = len(var_2)

    if length_var_1 == length_var_2 and length_var_1 + length_var_2 > 10:
        print('Same length AND combined length longer than ten!')

    if length_var_1 == length_var_2 or length_var_1 + length_var_2 > 10:
        print('Same length OR combined length longer than ten!')


def loops_scream():
    """
    NO TEST
    """
    while True:
        print('hello...', end='')


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

def loops_simple_continue():
    """
    Skip iteration 3 and 7
    >>> loops_simple_continue()
    1
    2
    4
    5
    6
    8
    9
    10
    """
    i = 0
    while i < 10:
        i += 1
        if i in {3, 7}:
            continue
        print(i)

# pylint: disable=import-outside-toplevel
def futures_sock_continue():
    """
    An alternate continue example, with working networking code
    Can play with this by using netcat: nc -l 12345, run program, type into nc stdin
    >>> with patch('time.sleep') as mock_sleep:
    ...     mock_socket_se = ('h', 'i', None)
    ...     mock_sleep.side_effect =  RuntimeError('STOP ITERATION FOR TESTING')
    ...     with patch('socket.socket') as mock_socket:
    ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
    ...         try:
    ...             futures_sock_continue()
    ...         except RuntimeError:
    ...             pass
    received h
    received i
    >>> with patch('time.sleep') as mock_sleep:
    ...     mock_socket_se = (None, 'f', None, 'x', None)
    ...     mock_sleep.side_effect =  (None, None, RuntimeError('STOP ITERATION FOR TESTING'))
    ...     with patch('socket.socket') as mock_socket:
    ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
    ...         try:
    ...             futures_sock_continue()
    ...         except RuntimeError:
    ...             pass
    received f
    received x
    """
    from time import sleep
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('127.0.0.1', 12345)) # host, port
        sock.setblocking(False)
        while True:
            try:
                data = sock.recv(1) # unordinarily small receive size for demonstration purposes
            except TimeoutError:
                pass
            if data:
                print(f'received {data}')
                continue
            sleep(0.5)
# pylint: enable=import-outside-toplevel

def loops_for_in():
    """
    >>> loops_for_in()
    3
    foo
    bar
    baz
    ['foo', 'bar']
    ['bar', 'baz']
    for loop:
    foo
    bar
    baz
    """
    our_list = ['foo', 'bar', 'baz']
    print(len(our_list))
    print(our_list[0])
    print(our_list[1])
    print(our_list[-1])
    print(our_list[:2])
    print(our_list[1:])
    print('for loop:')
    for item in our_list:
        print(item)


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
    'conditions_boolean_logic',
    'loops_scream',
    'loops_input_to_break',
    'loops_2_var_counter',
    'loops_simple_continue',
    'futures_sock_continue',
    'loops_for_in',
    )

locals_proxy = locals()
codeblocks = {
        func_name: get_func_body(
            locals_proxy[func_name]
            ) for func_name in CODEBLOCK_NAMES
        }
