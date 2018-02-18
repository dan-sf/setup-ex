import setup_ex
import mock
import sys
from unittest import TestCase

class TestApi(TestCase):
    @mock.patch.object(sys, 'stdout')
    def test_func(self, mock_stdout):
        custom = setup_ex.CustomApi()
        actual = custom.func(6,5)
        expected = 30
        self.assertEqual(actual, expected)

