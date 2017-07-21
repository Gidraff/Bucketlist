"""modules and packages to used to test bucketlist"""

from unittest import TestCase
from app.main.bucketlist import BucketList
from app.main.data import Data

class TestBucketList(TestCase):
    """Main BucketList Test class"""
    def setUp(self):
        """this prepares test fixture"""

        self.bucketlist_data = Data

        self.bucketlist_one = {
            'title':'jam view',
            'description':'view city jam',
            'created_by':'username',
            'owner_id':'123456'
        }
        