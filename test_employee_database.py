##########################
# DO NOT TOUCH THIS FILE #
##########################
from sys import platform
import unittest

from pexpect import replwrap

import employee_database as emp

class TestEmployeeDatabase(unittest.TestCase):
    def assert_interactions(self, tests):
        """Helper function to send input and compare output to given expected.

        Arguments:
        tests -- Lists of 2-value tuples in the format: (INPUT, EXPECTED OUTPUT)"""
        for interaction in tests:
            output = self.child.run_command(interaction[0])
            self.assertEqual(interaction[1], output)

    def setUp(self):
        """Sets up tests by executing main program programmatically."""
        command = 'python'
        if platform == 'linux' or platform == 'darwin':
            command += '3'
        self.child = replwrap.REPLWrapper(f'{command} employee_database.py', '<< ', None)

    def test_add_valid(self):
        """Tests scenario: adds a user"""
        tests = [
            ('add 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Record added\r\n')
        ]
        self.assert_interactions(tests)

    def test_view_valid(self):
        """Tests scenario: adds then views a user"""
        tests = [
            ('add 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Record added\r\n'),
            ('view 1', '>> 1 Michael Denver\r\n')
        ]
        self.assert_interactions(tests)

    def test_edit_valid(self):
        """Tests scenario: adds then edits a user's name, then views user"""
        tests = [
            ('add 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Record added\r\n'),
            ('edit 1', 'Name '),
            ('Jacob', 'City '),
            ('\r', '>> Record edited\r\n'),
            ('view 1', '>> 1 Jacob Denver\r\n')
        ]
        self.assert_interactions(tests)

    def test_remove_valid(self):
        """Tests scenario: adds, views, then removes user"""
        tests = [
            ('add 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Record added\r\n'),
            ('view 1', '>> 1 Michael Denver\r\n'),
            ('remove 1', '>> Record removed\r\n'),
            ('view 1', '>> Error viewing record\r\n')
        ]
        self.assert_interactions(tests)

    def test_invalid_id(self):
        """Tests scenario: tries to add invalid ID"""
        tests = [
            ('add blah', '>> Invalid ID\r\n')
        ]
        self.assert_interactions(tests)

    def test_invalid_add(self):
        """Tests scenario: adds, then tries to add same ID again"""
        tests = [
            ('add 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Record added\r\n'),
            ('add 1', 'Name '),
            ('Jacob', 'City '),
            ('Denver', '>> Error adding record\r\n')
        ]
        self.assert_interactions(tests)

    def test_invalid_edit(self):
        """Tests scenario: tries to edit non-existent ID"""
        tests = [
            ('edit 1', 'Name '),
            ('Michael', 'City '),
            ('Denver', '>> Error editing record\r\n')
        ]
        self.assert_interactions(tests)

    def test_invalid_view(self):
        """Tests scenario: tries to view non-existent ID"""
        tests = [
            ('view 1', '>> Error viewing record\r\n')
        ]
        self.assert_interactions(tests)

    def test_invalid_remove(self):
        """Tests scenario: tries to remove non-existent ID"""
        tests = [
            ('remove 1', '>> Error removing record\r\n')
        ]
        self.assert_interactions(tests)

if __name__ == '__main__':
    unittest.main()
