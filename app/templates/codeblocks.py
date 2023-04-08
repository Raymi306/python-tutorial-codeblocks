"""
Exports doctested, minimal codeblocks for templating
Docstrings MUST be double quotes!
"""

import inspect
from unittest.mock import patch


def normalize_indentation(line, set_level, level):
    """Remove unnecessary indentation resulting from doctesting of code"""
    if line == '\n':
        return line, level
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
    consume_whitespace = True
    result = []
    if '# START' in raw and '# END' in raw:
        take = False
        for line in lines:
            if '# END' in line:
                take = False
            if take:
                if not line.strip() and consume_whitespace: # DRY :\
                    continue
                consume_whitespace = False
                line, level = normalize_indentation(line, set_level, level)
                set_level = False
                result.append(line)
            if '# START' in line:
                take = True
        return ''.join(result).strip() # confused myself with early return lol
    docstring_occurences = 0
    for line in lines:
        if docstring_occurences >= 2:
            if not line.strip() and consume_whitespace: # DRY :\
                continue
            consume_whitespace = False
            line, level = normalize_indentation(line, set_level, level)
            set_level = False
            result.append(line)
        docstring_occurences += line.count('"""')

    return ''.join(result).strip()


def mark(fn):  # pylint: disable=invalid-name
    """Give something for code inspection to find functions
    that we wish to include as codeblocks, and make fn static"""
    fn.__mark = None  # pylint: disable=protected-access
    return staticmethod(fn)


class Codeblocks:  # pylint: disable=too-many-public-methods
    """Container of functions needed for templating"""

    # pylint: disable=line-too-long
    # pylint: disable=redefined-builtin
    @mark
    def hello_world():
        """
        >>> Codeblocks.hello_world()
        Hello world
        """
        print('Hello world')

    @mark
    def input_noop():
        """
        >>> Codeblocks.input_noop()
        """
        with patch('builtins.input') as input:
            # START
            input()
            # END

    @mark
    def input_and_print(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print('hello')
        You typed: hello
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            my_variable = input()
            print('You typed: ' + my_variable)
            # END

    @mark
    def input_and_print_twice(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print_twice('7')
        77
        >>> Codeblocks.input_and_print_twice('foo')
        foofoo
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            my_number = input()
            print(my_number * 2)
            # END

    @mark
    def input_and_print_double_v1(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print_double_v1('7')
        14
        >>> Codeblocks.input_and_print_double_v1('foo')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: 'foo'
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            my_number = int(input())
            print(my_number * 2)
            # END

    @mark
    def input_and_print_double_v2(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print_double_v2('7')
        14
        >>> Codeblocks.input_and_print_double_v2('foo')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: 'foo'
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            my_number = input()
            print(int(my_number) * 2)
            # END

    @mark
    def input_and_print_double_v3(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print_double_v3('7')
        14
        >>> Codeblocks.input_and_print_double_v3('foo')
        Traceback (most recent call last):
        ValueError: invalid literal for int() with base 10: 'foo'
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            print(int(input()) * 2)
            # END

    @mark
    def input_and_print_double_v4(mocked_input_ret):
        """
        >>> Codeblocks.input_and_print_double_v4('7')
        14
        >>> Codeblocks.input_and_print_double_v4('foo')
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

    @mark
    def futures_try_int_input(mocked_input_ret):
        """
        >>> Codeblocks.futures_try_int_input(4)
        8
        >>> Codeblocks.futures_try_int_input('q')
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

    @mark
    def conditions_names(mocked_input_ret):
        """
        >>> Codeblocks.conditions_names('max')
        Weirdo
        >>> Codeblocks.conditions_names('jax')
        Cool name!
        >>> Codeblocks.conditions_names('foobarbaz')
        Hello, foobarbaz
        """
        with patch('builtins.input') as input:
            input.return_value = mocked_input_ret
            # START
            user_input = input('What\'s your name?')
            if user_input == 'max':
                print('Weirdo')
            elif user_input == 'jax':
                print('Cool name!')
            else:
                print('Hello, ' + user_input)
            # END

    # pylint: disable=using-constant-test
    @mark
    def conditions_indent():
        """
        >>> Codeblocks.conditions_indent()
        True is true...
        You'll see this get printed too!
        """
        if True:
            print('True is true...')
            print('You\'ll see this get printed too!')
    # pylint: enable=using-constant-test

    @mark
    def conditions_boolean_logic():
        """
        >>> Codeblocks.conditions_boolean_logic()
        At least one var is Foo!
        Same length OR combined length longer than ten!
        """

        # Experimenting with conditional logic can be more convenient in the interpreter
        var_1 = 'Foo'
        var_2 = 'Bar'

        if var_1 == 'Foo' and var_2 == 'Foo':
            print('All Foo!')

        if var_1 == 'Foo' or var_2 == 'Foo':
            print('At least one var is Foo!')

        if not var_1 or not var_2:
            print('At least one var is falsey!')

        length_var_1 = len(var_1)
        length_var_2 = len(var_2)

        if length_var_1 == length_var_2 and length_var_1 + length_var_2 > 10:
            print('Same length AND combined length longer than ten!')

        if length_var_1 == length_var_2 or length_var_1 + length_var_2 > 10:
            print('Same length OR combined length longer than ten!')

    @mark
    def loops_scream():
        """
        NO TEST
        """
        while True:
            print('hello...', end='')

    @mark
    def loops_input_to_break(mocked_input_se):
        """
        >>> Codeblocks.loops_input_to_break(('q',))
        >>> Codeblocks.loops_input_to_break(('foo', 'q'))
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

    @mark
    def loops_2_var_counter(mocked_input_se):
        """
        >>> Codeblocks.loops_2_var_counter(('q', 'q', 'q'))
        Loopedy loop...
        Loopedy loop...
        Loopedy loop...
        >>> Codeblocks.loops_2_var_counter(('q', 'foo', 'q', 'q'))
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
                    counter += 1  # equivalent to `counter = counter + 1`
                print('Loopedy loop...')
            # END

    @mark
    def loops_simple_continue():
        """
        Skip iteration 3 and 7
        >>> Codeblocks.loops_simple_continue()
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
    @mark
    def futures_sock_continue():
        """
        An alternate continue example, with working networking code
        Can play with this by using netcat: nc -l 12345, run program, type into nc stdin
        >>> with patch('time.sleep') as mock_sleep:
        ...     mock_socket_se = ('h', 'i', None)
        ...     mock_sleep.side_effect = RuntimeError('STOP ITERATION FOR TESTING')
        ...     with patch('socket.socket') as mock_socket:
        ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
        ...         try:
        ...             Codeblocks.futures_sock_continue()
        ...         except RuntimeError:
        ...             pass
        received h
        received i
        >>> with patch('time.sleep') as mock_sleep:
        ...     mock_socket_se = (None, 'f', None, 'x', None)
        ...     mock_sleep.side_effect = (None, None, RuntimeError('STOP ITERATION FOR TESTING'))
        ...     with patch('socket.socket') as mock_socket:
        ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
        ...         try:
        ...             Codeblocks.futures_sock_continue()
        ...         except RuntimeError:
        ...             pass
        received f
        received x
        """
        from time import sleep
        import socket

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(('127.0.0.1', 12345))  # host, port
            sock.setblocking(False)
            while True:
                try:
                    data = sock.recv(1)  # unordinarily small receive size for demonstration purposes
                except TimeoutError:
                    pass
                if data:
                    print(f'received {data}')
                    continue
                sleep(0.5)
    # pylint: enable=import-outside-toplevel

    @mark
    def collections_item_access():
        """
        >>> Codeblocks.collections_item_access()
        3
        foo
        bar
        baz
        ['foo', 'bar']
        ['bar', 'baz']
        foo
        bar
        baz
        2
        value
        42
        key
        13
        value
        42
        key value
        13 42
        """
        # lists
        our_list = ['foo', 'bar', 'baz']
        print(len(our_list)) # 3
        print(our_list[0]) # foo
        print(our_list[1]) # bar
        print(our_list[-1]) # baz
        print(our_list[:2]) # foo, bar - beginning to second element
        print(our_list[1:]) # bar, baz - index 1 to end
        for item in our_list:
            print(item)
        # dictionaries
        our_dict = {'key': 'value', 13: 42}
        print(len(our_dict))
        print(our_dict['key']) # 'value'
        print(our_dict[13]) # 42
        for key in our_dict:
            print(key)
        for value in our_dict.values():
            print(value)
        for key, value in our_dict.items():
            print(key, value)

    @mark
    def collections_instantiations():
        """
        >>> Codeblocks.collections_instantiations()
        [1, 2, 3, 4] (1, 2, 3) (1,)
        {1, 2} {'key': 'value', 1: 2}
        ['lorem ipsum', 123456, 'foo bar baz', 7890]
        """
        my_list = [1, 2, 3, 4]
        my_tuple = (1, 2, 3)
        my_tuple_single_item = (1,)
        my_dictionary = {'key': 'value', 1: 2}
        my_set = {1, 2}
        my_big_list = [
                'lorem ipsum',
                123456,
                'foo bar baz',
                7890
                ]
        print(my_list, my_tuple, my_tuple_single_item)
        print(my_set, my_dictionary)
        print(my_big_list)

    @mark
    def functions_define():
        """
        >>> Codeblocks.functions_define()
        30
        9
        1
        1
        2
        3
        5
        8
        13
        """
        def add_2(num_1, num_2):
            return num_1 + num_2

        def print_collection(collection):
            for item in collection:
                print(item)

        value_1 = 10
        value_2 = 20
        print(add_2(value_1, value_2)) # 30
        print(add_2(3, 6)) # 9
        list_1 = [1, 1, 2, 3, 5, 8, 13]
        print_collection(list_1)

    @mark
    def functions_splat():
        """
        >>> Codeblocks.functions_splat()
        Both methods agree; sum of 1, 2, 3, 4 is 10
        """
        def sum_4_long_signature(num_1, num_2, num_3, num_4):
            return num_1 + num_2 + num_3 + num_4

        def sum_many(list_nums):
            accumulator = 0
            for num in list_nums:
                accumulator += num
            return accumulator

        my_list = [1, 2, 3, 4]
        result_1 = sum_4_long_signature(*my_list) # splat operator unpacks a list or tuple, double splat (**) unpacks a dictionary
        result_2 = sum_many(my_list)
        if result_1 == result_2:
            print(f'Both methods agree; sum of 1, 2, 3, 4 is {result_1}')

    # pylint: disable=import-outside-toplevel
    @mark
    def random_numbers():
        """
        >>> import random
        >>> random.seed(1)
        >>> Codeblocks.random_numbers()
        18
        73
        98
        9
        33
        16
        64
        98
        58
        61
        """
        import random

        for _ in range(10):
            print(random.randint(1, 100))
    # pylint: enable=import-outside-toplevel

    # pylint: disable=import-outside-toplevel
    @mark
    def guessing_game(mocked_input_se):
        """
        >>> import random
        >>> random.seed(1)
        >>> Codeblocks.guessing_game(('y', '18', 'y', '1', 'n'))
        You win!
        You lose!
        Game over!
        """
        with patch('builtins.input') as input:
            input.side_effect = mocked_input_se
            # START
            from random import randint

            while input('Play game? y/n: ') == 'y':
                answer = randint(1, 100)
                guess = int(input('Guess a number between 1 and 100: ').strip())
                if guess == answer:
                    print('You win!')
                else:
                    print('You lose!')
            print('Game over!')
            # END
    # pylint: enable=import-outside-toplevel

    # pylint: disable=import-outside-toplevel,redefined-outer-name
    @mark
    def argv():
        """
        >>> import sys
        >>> sys.argv = 'codeblocks.py', 'foo', 'bar'
        >>> Codeblocks.argv()
        ('codeblocks.py', 'foo', 'bar')
        codeblocks.py
        foo bar
        """
        from sys import argv
        print(argv) # prints all args
        print(argv[0]) # is always the name of the program
        # caution!
        # the below line will fail if at least 2 arguments aren't passed in to the program!
        print(argv[1], argv[2])
    # pylint: enable=import-outside-toplevel,redefined-outer-name

    @mark
    def file_io():
        """no tests, was run manually"""
        with open('my_file.txt', 'w', encoding='ascii') as f: # second argument is the mode to open the file in, w is for write
            # encoding above refers to how bytes translates to characters.
            # ascii is very common for simple english text and special characters.
            # utf-8 covers characters from many languages, and even emojis
            # character encodings are an interesting topic for further reading if you're curious
            f.write('This is both the beginning\nand the end\n')

        with open('my_file.txt', 'a', encoding='ascii') as f: # a is for append
            f.write('This is the new end\n')

        with open('my_file.txt', 'r', encoding='ascii') as f: # r for read
            for i, line in enumerate(f):
                print(f'line {i}: {line}', end='') # we can tell print not to add a new line at the end
                # we already have new lines on the lines we are reading

        with open('my_file.txt', 'r+', encoding='ascii') as f: # r+ for read and write
            f.seek(17) # advance forward in the file 17 characters
            f.write('foobarbaz')
            f.seek(0) # back to the beginning!
            print(f.readline()) # let's see the result

    # pylint: disable=import-outside-toplevel, import-error
    @mark
    def imports_1():
        """no tests"""
        import example_b
        example_b.some_function() # variables and functions defined inside of example_b can be accessed like so
    # pylint: enable=import-outside-toplevel, import-error

    # pylint: disable=import-outside-toplevel, import-error
    @mark
    def requests_demo():
        """no tests"""
        import requests
        response = requests.get('http://example.com')
        print(response.text)
    # pylint: enable=import-outside-toplevel, import-error

    # pylint: disable=import-outside-toplevel, import-error
    @mark
    def soup_demo():
        """no tests"""
        from bs4 import BeautifulSoup
        import requests
        response = requests.get('http://example.com')
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        headers = soup.find_all('h1')
        print(headers[0].text)
    # pylint: enable=import-outside-toplevel, import-error

    @mark
    def variables_assignments():
        """
        >>> Codeblocks.variables_assignments()
        4
        4
        """
        def foo():
            return 4
        def bar():
            return 5
        def do_something(v1, v2):
            pass
        # START
        # assignment as statement
        my_var = foo()
        if my_var:
            print(my_var)
        # assignment as expression, using 'walrus' operator
        if my_var := foo():
            print(my_var)

        # a more complicated example
        if (var_1 := foo()) and (var_2 := bar()):
            do_something(var_1, var_2)
        # END



codeblocks = {
    fn_name: get_func_body(
        fn
    ) for fn_name, fn in inspect.getmembers(Codeblocks, lambda pred: hasattr(pred, '__mark'))
}
