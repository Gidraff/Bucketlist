from datetime import datetime
from main.item import Item
from main.user import User
from uuid import uuid4


class BucketList(object):
    
    def __init__(self, title,description, created_by, date_created=datetime.utcnow()):
        
        self.title = title
        self.description = description
        self.created_by = created_by
        self.date_created = date_created
        self.bucketlist_id = uuid4()

        def add_items(self, item_value):
            item = Item(item_value=item_value,
                        item_id=self.bucketlist_id)
            item.save_item()
        def view_items(self):
            pass
        def edit_item(self):
            pass
        def remove_items(self):
            pass

