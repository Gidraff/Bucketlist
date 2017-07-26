"""modules and packages to used to test bucketlist"""

from unittest import TestCase
from app.main.bucketlist import BucketList
from app.main.data import Data

class TestBucketList(TestCase):
    """Main BucketList Test class"""
    def setUp(self):
        """this prepares test fixture"""

        self.new_bucketlist = BucketList('bucket_title','am a bucket','username','1234')
        self.bucketlist_data = Data
    def test_save_bucketlist_info(self):
        """tests whether the bucketlist has been saved"""

        result = len(self.bucketlist_data.bucketlists)
        self.new_bucketlist.save_bucketlist_info()
        self.assertNotEqual(result, len(self.bucketlist_data.bucketlists))