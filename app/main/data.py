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
    @staticmethod
    def retrieve_data(_id):
        """method that retrieves data"""
        buckelists = []
        for bucketlist in Data.bucketlists:
            if _id == bucketlist['owner_id']:
                buckelists.append(bucketlist)
                return buckelists
