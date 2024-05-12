#!/usr/bin/env python3

from string_functions import return_string, interpolate_string

class TestStringFunctions:
    '''Test cases for string_functions.py'''

    def test_return_string(self):
        '''Test that return_string() function returns a string.'''
        assert isinstance(return_string(), str)

    def test_interpolate_string(self):
        '''Test that interpolate_string() function inserts a string into another string.'''
        assert interpolate_string('Guido') == 'Hello, Guido!'
