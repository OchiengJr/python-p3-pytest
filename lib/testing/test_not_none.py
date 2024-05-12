#!/usr/bin/env python3

from not_none_functions import return_not_none

class TestNotNullFunctions:
    '''Test cases for not_none_functions.py'''

    def test_return_not_none(self):
        '''Test that return_not_none() function returns a value that is not None.'''
        assert return_not_none() is not None
