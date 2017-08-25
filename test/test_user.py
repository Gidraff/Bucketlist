"""Package and modules to be imported"""

from unittest import TestCase
from app.main.activity import Activity
from app.main.bucketlist import BucketList
from app.main.user import User

class TestActivity(TestCase):
    """Activity class Tests"""

    def setUp(self):
        self.activity = Activity('surfing')
        
    def test_is_instance_of_class_activity(self):
        self.assertTrue(isinstance(self.activity, Activity))

    def test_argument_given_returned(self):
        self.assertEqual(self.activity.activity, 'surfing', msg='There is match')


class TestBucketList(TestCase):
    """Main BucketList Test class"""
    def setUp(self):
        """this prepares test fixture"""

        self.new_bucketlist = BucketList('bucket_title', 'am a bucket')
    def test_add_activity(self):
        """tests whether the activity has been saved"""
        self.new_bucketlist.add_activity('this is awesome')
        self.assertEqual(len(self.new_bucketlist.activities), 1)

    def test_edit_activity(self):
        "tests wether existing activity has been edited"
        id = self.new_bucketlist.add_activity('this is cool')
        self.new_bucketlist.edit_acivity(id, 'this is awesome')
        self.assertEqual(self.new_bucketlist.activities[id].activity, 'this is awesome')
            


class TestUser(TestCase):
    """setUp fixture for tests"""
    def setUp(self):
        self.new_user = User('mary', 'mary@mail', 'i1234')

    def test_create_bucketlist(self):
        """Tests whether bucketlist has been  created"""
        result = len(self.new_user.bucketlists)
        self.new_user.create_bucketlist('this is new', 'new bucketlist')
        after_add = len(self.new_user.bucketlists)
        self.assertTrue(after_add > result)

    def test_update_bucketlist(self):
        """test wether a bucketlist has been edited"""
        id = self.new_user.create_bucketlist('this is another', 'yet another')
        self.new_user.update_bucketlist(id, 'this work', 'yes it does')
        self.assertEqual(self.new_user.bucketlists[id].title, 'this work')
        self.assertEqual(self.new_user.bucketlists[id].description, 'yes it does')
        
    def test_delete_bucketlist(self):
        """test wether a bucketlist has been deleted"""
        id = self.new_user.create_bucketlist('another one', 'bungee')
        result = len(self.new_user.bucketlists)
        self.new_user.delete_bucketlist(id)
        self.assertNotEqual(len(self.new_user.bucketlists), result)


        



    
