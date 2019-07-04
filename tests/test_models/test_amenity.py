#!/usr/bin/python3
"""
Testing the Amenity Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.amenity import


class TestAmenity(unittest.TestCase):
    " Testing the Amenity Class "

    @classmethod
    def setUpClass(cls):
        " Setup the amenity "
        cls.amt = Amenity()
        cls.amt.name = "hola"

    @classmethod
    def teardown(cls):
        " deleting the class "
        del cls.amt

if __name__ == "__main__":
        unittest.main()
