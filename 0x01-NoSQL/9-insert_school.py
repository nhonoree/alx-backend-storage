def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.
    Returns the inserted document's _id.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
