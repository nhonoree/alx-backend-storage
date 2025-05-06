def list_all(mongo_collection):
        """
            Lists all documents in a MongoDB collection.
                Returns an empty list if the collection is empty.
                    """
                        return list(mongo_collection.find())

