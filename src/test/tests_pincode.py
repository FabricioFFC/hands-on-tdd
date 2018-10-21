import unittest
from models.pincode import Pincode
from helpers.database import DatabaseHelper

from test_helpers.database import DatabaseTestHelper

from exception.invalid_pincode_exception import InvalidPincodeException

class TestPincode (unittest.TestCase):
    global_pincode = '1a2s4d5678'
    def setUp(self):
        DatabaseTestHelper.clean_table('pincodes')

    def test_save_pincode_in_database(self):
        # given
        pincode = Pincode(self.global_pincode, DatabaseHelper)
        # when
        pincode.save()

        # then
        statement = 'SELECT * FROM pincodes'
        rows = DatabaseTestHelper.query(statement)

        self.assertEqual(1, len(rows))
        self.assertEqual(self.global_pincode, rows[0].get('pincode'))

    def test_throws_exception_when_pincode_is_already_used(self):
        # given
        pincode = Pincode(self.global_pincode, DatabaseHelper)
        # when
        pincode.save()
        # then
        with self.assertRaises(InvalidPincodeException) as context:
            pincode.save()
        self.assertTrue('InvalidPincodeException' in context.exception)

if __name__ == '__main__':
    unittest.main()
