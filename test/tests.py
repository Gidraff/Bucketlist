"""Package and modules to be imported"""

from unittest import TestCase
from app.main.activity import Activity
from app.main.bucketlist import BucketList
from app.main.user import User

class TestBucketList(TestCase):
    """Main BucketList Test class"""
    def setUp(self):
        """Sets up test fixture"""
        self.new_bucketlist = BucketList('bucket_title', 'am a bucket')
    def test_add_activity(self):
        """Test whether an activity has been saved"""
        before_add = len(self.new_bucketlist.activities)
        self.new_bucketlist.add_activity('this is awesome')
        after_add = len(self.new_bucketlist.activities)
        self.assertEqual(after_add - before_add, 1)

    def test_edit_activity(self):
        "Test whether  an activity has been edited"
        id = self.new_bucketlist.add_activity('this is cool')
        self.new_bucketlist.edit_acivity(id, 'this is awesome')
        self.assertEqual(self.new_bucketlist.activities[id].activity, 'this is awesome')

    def test_delete_activity(self):
        """Test whether an activity has been deleted"""
        id = self.new_bucketlist.add_activity('this is an activity')
        size_before = len(self.new_bucketlist.activities)
        self.new_bucketlist.delete_activity(id)
        size_after = len(self.new_bucketlist.activities)
        self.assertTrue(size_before - size_after, 1)
        
            
class TestUser(TestCase):
    """Sets up fixture for tests"""
    def setUp(self):
        """Set up test fixture"""
        self.new_user = User('mary', 'mary@mail', 'i1234')

    def test_create_bucketlist(self):
        """Test whether bucketlist has been  created"""
        result = len(self.new_user.bucketlists)
        self.new_user.create_bucketlist('this is new', 'new bucketlist')
        after_add = len(self.new_user.bucketlists)
        self.assertEqual(after_add - result, 1)

    def test_update_bucketlist(self):
        """Test whether bucketlist has been edited"""
        id = self.new_user.create_bucketlist('this is another', 'yet another')
        self.new_user.update_bucketlist(id, 'this work', 'yes it does')
        self.assertEqual(self.new_user.bucketlists[id].title, 'this work')
        self.assertEqual(self.new_user.bucketlists[id].description, 'yes it does')
        
    def test_delete_bucketlist(self):
        """Test whether  bucketlist has been deleted"""
        id = self.new_user.create_bucketlist('another one', 'bungee')
        result = len(self.new_user.bucketlists)
        self.new_user.delete_bucketlist(id)
        after_delete = len(self.new_user.bucketlists)
        self.assertTrue(result, after_delete)