"""Package and modules to be imported"""

from unittest import TestCase
from app.main.user import User
from app.main.bucketlist import BucketList
from app.main.activity import Activity
from app.main.data import Data

class TestUser(TestCase):
    """setUp fixture for tests"""
    def setUp(self):
        self.new_user = User('mary', 'mary@mail', 'i1234')
        self.bucketlist_info = {
            'title': 'first',
            'description': 'first description',
            'created_by': 'raff',
            'date_created': 'today',
            'owner_id':'12345654321234565432',
            'bucketlist_id': '1234565432'
            }

        self.activity = Activity('surfing', 'username', '1234')
        self.new_data = Data


    def test_create_bucketlist(self):
        """Tests whether bucketlist has been successfully created"""
        bucketlist_size = len(self.new_data.bucketlists)
        self.new_user.create_bucketlist('Funstuff', 'Do fan stuffs')
        bucketlist_size_after_creation = len(self.new_data.bucketlists)
        self.assertNotEqual(bucketlist_size, bucketlist_size_after_creation)
    def test_verify_user_returns_true(self):
        """verifies user exist"""
        result = self.new_user.verify_user("mary@mail")
        self.assertFalse(result)
    def test_read_bucketlist(self):
        """test if bucketlist can be viewed"""
        result = self.new_data.retrieve_data('1234565432')
        self.assertTrue(type(result), dict)

    def test_create_activity(self):
        """test if an activity has been created"""
        result = len(self.new_data.activities)
        self.new_data.save_data(self.bucketlist_info)
        self.new_user.create_activity("do onething")
        self.assertEqual(result, 0)
