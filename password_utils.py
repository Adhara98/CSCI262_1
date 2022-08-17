import hashlib, secrets
import string

salt_len = 8

def hash_md5(salted_pass: str) -> str:
    return hashlib.md5(salted_pass.encode()).hexdigest()

def generate_hash(password: str) -> tuple:
    salt_int = secrets.randbelow(10 ** (salt_len+1))
    salt = str(salt_int).zfill(salt_len)
    return salt, hash_md5(salt + password)

def is_matched(password: str, salt: str, hash: str) -> bool:
    return hash == hash_md5(salt + password)

def is_strong(password: str) -> bool:
    '''Password length must be atleast 8 letters and contain atleast 1 lowercase, 1 uppercase, 1 digit and 1 special character.'''
    st = set(password)
    is_weak = len(password) < 8 or \
        st & set(string.ascii_lowercase) == set() or \
        st & set(string.ascii_uppercase) == set() or \
        st & set(string.digits) == set() or \
        st & set(string.punctuation) == set()

    return not is_weak


        