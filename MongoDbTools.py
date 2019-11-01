from pymongo import MongoClient

class mongoDbTools:

    def init(self)：
        self.conn = MongoClient('10.106.74.21', 26047)
        self.db = self.conn['curriculum']
    
    def connect_db(self):

	pass