"""
module and standard libraries imported for use in test activity class
"""

from unittest import TestCase
from app.main.activity import Activity
from app.main.data import Data

class TestActivity(TestCase):
    """Activity class Tests"""

    def setUp(self):
        self.activity = Activity('surfing', 'username', '1234')
        self.activity_data = Data.activities
        
    def test_save_activity_info(self):
        result = len(self.activity_data)
        self.activity.save_activity_info()
        self.assertNotEqual(result, len(self.activity_data.activities))
