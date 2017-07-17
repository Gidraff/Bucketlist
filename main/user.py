from main.bucketlist import BucketList
from main.data import Data
from datetime import datetime
from uuid import uuid4
class User(object):
    
    def __init__(self,user_id, user_name, password, email):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.email = email

    def create_bucketlist(self, title, description, created_by, date_created, bucketlist_id):
        bucketlist = BucketList(title=title,
                                description=description,
                                created_by = self.user_name,
                                date_created= datetime.utcnow(),
                                bucketlist_id=self.user_id
        )

    def bucketlist_to_dict(self):
        """returns a bucketlist as a dictionary"""

        return {
        'title': self.title,
        'description': self.description,
        'created_by': self.created_by,
        'date_created': self.date_created,
        'bucketlist_id': self.bucketlist_id
    }

    def save_bucketlist(self):
        """saves created bucketlist to buckelists"""

        Data.bucketlists.append(bucketlist_to_dict())




    def view_bucketlist(self):
        pass

    def edit_bucketlist(self):
        pass

    def delete_bucketlist(self):
        pass