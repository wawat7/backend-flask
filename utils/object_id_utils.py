from bson import ObjectId


def is_valid_objectid(string: str):
    try:
        ObjectId(string)
        return True
    except:
        return False
