from register_view import register_user
from  register_model import validate_name, validate_email, validate_password
#testing functions with unittest
import unittest
import pytest
class loadDataTest(unittest.TestCase):
    def test_load_data(self):
        assert register_user('Ana', 'girl@she.com', 'abi123') is True
        print("Test passed")

    
if "__name__" == "__main__":
    unittest.main()