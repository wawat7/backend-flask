import bcrypt

def hash_string(s: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(s.encode('utf-8'), salt)

def check_hash_string(s: str, hash):
    if bcrypt.checkpw(s.encode('utf-8'), hash):
        return True
    else:
        return False
    