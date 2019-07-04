#!/usr/bin/python3
import unittest
import pep8
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage


def setUpModule():
        print("setup module")


def tearDownModule():
        print("teardown module")


class TestStringMethods(unittest.TestCase):
    def pep(self):
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
    def setUpClass():
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        pass

    def documentation(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def number(self):
        self.dupmodel.my_number = 398
        self.assertEqual(self.dupmodel.my_number, 398)

    def name(self):
        self.dupmodel.name = "Hello"
        self.assertEqual(self.dupmodel.name, "Hello")

    def instances(self):
        self.assertTrue(hasattr(self.dupmodel, "__init__"))
        self.assertTrue(hasattr(self.dupmodel, "save"))
        self.assertTrue(hasattr(self.dupmodel, "__str__"))
        self.assertTrue(hasattr(self.dupmodel, "to_dict"))

    def save(self):
        self.dupmodel.name = "Hello"
        self.dupmodel.save()
        storage.reload()
        self.assertTrue(storage.all(), "Hello")
        self.assertTrue(hasattr(self.dupmodel, 'save'))
        self.assertTrue(hasattr(self.dupmodel.created_at,
                                self.dupmodel.updated_at))

if __name__ == '__main__':
    unittest.main()
