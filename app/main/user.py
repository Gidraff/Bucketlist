"""modules and standard libraries to be used by User class"""

from uuid import uuid4
from app.main.bucketlist import BucketList
from app.main.data import Data


class User(object):
    """User class that allows user to create, view, update and delete bucketlist"""
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password
        self._id = uuid4().hex

    def create_bucketlist(self, title, description):
        """creates and saves user's bucketlist"""
        bucketlist = BucketList(title=title,
                                description=description,
                                created_by=self.user_name,
                                bucketlist_user_id=self._id)
        bucketlist.save_bucketlist_info()

    @staticmethod
    def view_bucketlist(bucketlist_id):
        """returns list of user's bucketlist"""

        all_bucketlist = [bucketlist_ for bucketlist_ in Data.bucketlists\
         if bucketlist_id == bucketlist_['owner_id']\
          or bucketlist_id == bucketlist_['bucketlist_id']]
        return all_bucketlist

    def update_bucketlist(self, title, description):
        """Allows user to make update or edit buckelist"""

        for bucketlist in Data.bucketlists:
            if bucketlist['owner_id'] == self._id:
                bucketlist['title'] = title
                bucketlist['description'] = description
                return True

    @staticmethod
    def verify_user(email):
        """checks whether user exists in the Data class"""
        email_checker = [mail['email'] for mail in Data.users if email == mail['email']]
        return "".join(email_checker) == email

    @classmethod
    def register_user(cls, user_name, email, password):
        """register user to Data.user"""
        does_exist = cls.verify_user(email)
        if does_exist is False:
            new_user = cls(user_name, email, password)
            new_user.save_users_info()
            return True
    def save_users_info(self):
        """save user's formation in Data.users as dictionary"""
        new_user = {
            'username':self.user_name,
            'email':self.email,
            'password':self.password,
            'id':self._id
        }
        Data.users.append(new_user)
    @staticmethod
    def create_activity(_id, activity):
        """creates and saves user's activity"""
        bucketlist_data = Data.retrieve_data(_id, Data.bucketlists)
        for data  in bucketlist_data:
            new_bucketlist = BucketList(
                data['title'],
                data['description'],
                data['created_by'],
                data['bucketlist_user_id']
            )
            new_bucketlist.create_activity(activity=activity)
            