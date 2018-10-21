data = []
global data
class DatabaseHelper(object):
    def __init__(self, table):
        pass

    def insert(self, new_data):
        data.append(new_data)

    def find_one(self, query):
        if (len(data) >= 1):
            return data[0]

        return None

    @staticmethod
    def clean_db():
        global data
        data = []
