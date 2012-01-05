# encoding: utf-8
""" The fritzing parser test class """

from parser.fritzing import Fritzing
import unittest


class FritzingTests(unittest.TestCase):
    """ The tests of the fritzing parser """

    def test_create_new_fritzing_parser(self):
        """ Test creating an empty parser. """
        parser = Fritzing()
        assert parser != None
