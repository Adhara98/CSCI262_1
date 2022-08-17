from contexts import salt_reader, salt_writer, shadow_reader, shadow_writer
from password_utils import generate_hash

class UserService(object):
    salt_len = 8

    def __enter__(self):
        self.__service__ = UserService()
        return self.__service__

    def __exit__(self, *args):
        self.__service__.save()

    def __init__(self) -> None:
        self._users = dict()
        self.__populate_users__()
    
    def __populate_users__(self) -> None:
        with salt_reader() as salts, shadow_reader() as shadows:
            for salt, shadow in zip(salts, shadows):
                self._users[salt['Username']] = {
                    'Salt': salt['Salt'],
                    'PassSaltHash': shadow['PassSaltHash'],
                    'SecurityClearance': int(shadow['SecurityClearance'])
                }

    def get_users(self) -> list:
        return self._users

    def exists(self, username) -> bool:
        return username in self._users

    def add_user(self, username: str, password: str, clearance: int) -> None:
        assert not self.exists(username), 'User already exists'

        salt, hash = generate_hash(password)
        self._users[username] = {
            'Username': username,
            'Salt': salt,
            'PassSaltHash': hash,
            'SecurityClearance': clearance
        }

    def save(self) -> None:
        with salt_writer() as salts, shadow_writer() as shadows:
            salts.writeheader()
            shadows.writeheader()
            for username, data in self._users.items():
                salts.writerow({
                    'Username': username,
                    'Salt': data['Salt']
                })
                shadows.writerow({
                    'Username': username,
                    'PassSaltHash': data['PassSaltHash'],
                    'SecurityClearance': data['SecurityClearance']
                })

