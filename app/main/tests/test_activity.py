"""
module and standard libraries imported for use in test activity class
"""

from unittest import TestCase
from app.main.activity import Activity

class TestActivity(TestCase):
    """Activity class Tests"""

    def setUp(self):
        activity = {
            'activity':'surfing',
            'created_by':'username',
            'date_created':'12-12-2012',
            'activity_owner':'1234',
            'id':'4321'
        }
    