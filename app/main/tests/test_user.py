from unittest import TestCase
from app.main.user import User
from app.main.bucketlist import BucketList
from app.main.data import Data

class TestUser(TestCase):
    def setUp(self):
        self.new_user= User('mary','mary','mary@mail','i1234')
        self.bucketlist_data = {
                                'title': 'first',
                                'description': 'first description',
                                'created_by': 'raff',
                                'date_created': 'today',
                                'owner_id':'12345654321234565432',
                                'bucketlist_id': '1234565432'
                                }
        self.another_bucketlist  = {
                                'title': 'second',
                                'description': 'another description',
                                'created_by': 'james',
                                'date_created': 'today',
                                'owner_id':'7654321',
                                'bucketlist_id': '123456765432'
                                }

    def test_create_bucketlist(self):
        bucketlist_size = len(Data.bucketlists)
        self.new_user.create_bucketlist('Funstuff','Do fan stuffs')
        bucketlist_size_after_creation = len(Data.bucketlists)
        self.assertNotEqual(bucketlist_size, bucketlist_size_after_creation)


    def test_view_bucketlist(self):
        Data.bucketlists.append(self.bucketlist_data)
        result = self.new_user.view_bucketlist('1234565432')
        self.assertIsInstance(result, list)

    def test_update_bucketlist_returns_true_or_false(self):
        result = self.new_user.update_bucketlist("Bamuda","visit bamuda")
        self.assertEqual(type(result), bool)


    def test_delete_bucketlist(self):
        size_before_delete = len(Data.bucketlists.append(self.another_bucketlist))
        self.new_user.delete_bucketlist('123456765432') 
        size_after_delete = len(Data.bucketlists)
        self.assertNotEqual(size_before_delete, size_after_delete)

    def test_verify_user_returns_true(self):
        result = self.new_user.verify_user("mary@mail")
        self.assertFalse(result)