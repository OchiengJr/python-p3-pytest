#!/usr/bin/env python3

from bool_functions import return_true

class TestBoolFunctions:
    '''Test cases for bool_functions.py'''

    def test_return_true(self):
        '''Test that return_true() function returns True.'''
        assert return_true() is True
