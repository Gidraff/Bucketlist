"""modules and standard libraries to be used by User class"""

from datetime import datetime
from uuid import uuid4
from bucketlist import BucketList
from data import Data

class User(object):
    """User class that allows user to create, view, update and delete bucketlist"""
    def __init__(self,name, user_name, email,password, user_id=None):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.user_id = uuid4().hex

    def create_bucketlist(self, title, description, date_created=datetime.utcnow()):
        """creates and saves user's bucketlist"""

        bucketlist = BucketList(title=title,
                                description=description,
                                created_by=self.user_name,
                                date_created=date_created,
                                owner_id=self.user_id)
        bucketlist.save_bucketlist()

    @staticmethod
    def view_bucketlist(bucketlist_id):
        """returns list of user's bucketlist"""

        all_bucketlist = [bucketlist_ for bucketlist_ in Data.bucketlists\
         if bucketlist_id == bucketlist_['owner_id'] or bucketlist_id == bucketlist_['bucketlist_id']]
        return all_bucketlist

    def update_bucketlist(self, title, description):
        """Allows user to make update or edit buckelist"""

        for bucketlist in Data.bucketlists:
            if bucketlist['owner_id'] == self.user_id:
                bucketlist['title'] = title
                bucketlist['description'] = description
                return True

    @staticmethod
    def delete_bucketlist(bucketlist_id):
        """delete bucketlist with the  passed arguments"""

        for bucketlist in Data.bucketlists:
            if bucketlist_id == bucketlist['bucketlist_id']:
                del bucketlist
                return True
    @staticmethod
    def verify_user(email):
        """checks whether user exists in the Data class"""
        email_checker = [i['email'] for i in Data.user if email == i['email']]
        return "".join(email_checker) == email
    
    def user_detail_to_dict(self):
        """return user details as a dictionary"""

        return {
                'name':self.name,
                'user_name':self.user_name,
                'email':self.email,
                'password':self.password,
                'user_id':self.user_id
                }        

    def save_info(self):
        """save user's detail in Data.users"""
        Data.user.append(self.user_detail_to_dict())

    @classmethod
    def register_user(cls, name, user_name, email, password):
        does_exist = cls.verify_user(email)
        if does_exist is False:
            new_user = cls(name, user_name, email, password)
            new_user.save_info()
            return True
        else:
            return False
 

user_one = User
p = user_one.register_user('raff', 'raff','raff@mail', '54321')
print(Data.user)
print(p)
p1 = user_one.register_user('raff', 'raff','raff@mail', '54321')
print(p1)
print(Data.user)