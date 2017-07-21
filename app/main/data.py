"""module that contains Data class"""

class Data(object):
    """Data class """

    users = []
    bucketlists = []
    activities = []
    @staticmethod
    def save_data(args):
        """method that saves all data"""
        if 'email' in args:
            Data.users.append(args)
            return True
        elif 'title' in args:
            Data.bucketlists.append(args)
            return True
        elif 'activity' in args:
            Data.activities.append(args)
            return True

