#!/usr/bin/python3
"""
Testing the Place Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testing the Place Class
    """

    @classmethod
    def setUpClass(clas):
        " Setup Class Place "
        cls.place = Place()
        cls.place.name = "Rio"
        cls.place.city_id = "ro-34"
        cls.place.description = "capital de playa"
        cls.place.user_id = " 345654 "
        cls.place.number_rooms = 234
        cls.place.number_bathrooms = 324
        cls.place.max_guest = 56789
        cls.place.price_by_night = 8754332
        cls.place.latitude = 23.678
        cls.place.longitud = 43.7

    @classmethod
    def teardown(cls):
        " Delete the instance "
        del cls.place


if __name__ == "__main__":
        unittest.main()
