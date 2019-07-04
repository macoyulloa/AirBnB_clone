#!/usr/bin/python3
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime
from models import storage


def setUpModule():
    pass


def tearDownModule():
    pass


class TestStringMethods(unittest.TestCase):
    def test_pep(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_model/test_base_model.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class test_class_instance(unittest.TestCase):

    def setUp(self):
        self.dupmodel = BaseModel()
        print("setUp")

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_documentation(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_number(self):
        self.dupmodel.my_number = 398
        self.assertEqual(self.dupmodel.my_number, 398)

    def test_name(self):
        self.dupmodel.name = "Hello"
        self.assertEqual(self.dupmodel.name, "Hello")

    def test_instances(self):
        self.assertTrue(hasattr(self.dupmodel, "__init__"))
        self.assertTrue(hasattr(self.dupmodel, "save"))
        self.assertTrue(hasattr(self.dupmodel, "__str__"))
        self.assertTrue(hasattr(self.dupmodel, "to_dict"))

    def test_save(self):
        self.dupmodel.name = "Hello"
        storage.reload()
        print(storage.all())
        self.assertTrue(storage.all(), "Hello")
        self.assertTrue(hasattr(self.dupmodel, 'save'))

    def test_instance2(self):
        self.assertIsInstance(self.dupmodel, BaseModel)

if __name__ == '__main__':
    unittest.main()
