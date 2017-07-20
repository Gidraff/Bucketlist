from uuid import uuid4
import datetime
from app.main.data import Data
class Activity(object):
    
    def __init__(self, activity, created_by ,activity_owner_id):
        self.activity = activity
        self.created_by = created_by
        self.date_created = datetime.datetime.utcnow
        self.activity_owner_id = activity_owner_id
        self._activity_id = uuid4()


    def save_activity_info(self):
        new_activity = {
                        'activity':self.activity,
                        'created_by':self.created_by,
                        'date_created':self.date_created,
                        'activity_owner':self.activity_owner_id,
                        'id':self._activity_id
                        }
        Data.activities.append(new_activity)
