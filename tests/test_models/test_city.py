#!/usr/bin/python3
"""
Testing the City Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Testing the City Class
    """

    @classmethod
    def setUpClass(cls):
        " Setup City Class "
        cls.city = City()
        cls.city.state_id = "gfrf5466"
        cls.city.name = "Barbosa"

    @classmethod
    def teardown(cls):
        " Delete the City instancE "
        del cls.city


if __name__ == "__main__":
        unittest.main()
