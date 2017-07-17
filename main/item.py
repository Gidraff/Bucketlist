from main.data import Data
class Item(object):
    def __init__(self, item_value, item_id):
        self.item_value = item_value
        self.item_id = item_id

    def convert_item_to_dict(self):
        """returns item in dictionary form"""
        return {
        'item_value': self.item_value,
        'item_id': self.item_id
    }

    def save_item(self):
        Data.items.append(convert_item_to_dict())
