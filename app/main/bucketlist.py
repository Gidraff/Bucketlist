"""modules and standard libraries to be used by Bucketlist classs """
import datetime
from uuid import uuid4
from app.main.activity import Activity
from app.main.data import Data


class BucketList(object):
    """Bucketlist class"""
    def __init__(self, title, description, created_by,  bucketlist_user_id):    
        self.title = title
        self.description = description
        self.created_by = created_by 
        self.date_created = datetime.datetime.utcnow()
        self.bucketlist_user_id =  bucketlist_user_id 
        self._id = uuid4()
        
        
    def create_activity(self, activity):
        """create new activities"""
        activity = Activity(
                            activity=activity,
                            created_by=self.created_by,
                            activity_owner_id=self.bucketlist_user_id
        )
        activity.save_activity_info()
    
    def save_bucketlist_info(self):
        """save bucketlist as a dictionary"""

        new_bucketlist = {
            'title': self.title,
            'description': self.description,
            'created_by': self.created_by,
            'date_created': self.date_created,
            'owner_id': self.bucketlist_user_id
        }
        Data.save_data(new_bucketlist)

