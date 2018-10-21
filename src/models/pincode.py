from exception.invalid_pincode_exception import InvalidPincodeException

class Pincode(object):
    def __init__(self, pincode, Database):
        self.pincode = pincode
        self.db = Database('pincodes')

    def save(self):
        pincode_from_database = self.db.find_one("pincode = '%s'" % self.pincode)

        if pincode_from_database:
            raise InvalidPincodeException('InvalidPincodeException')

        self.db.insert(dict(pincode=self.pincode))
