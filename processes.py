import os
from sys import exit
from user_service import UserService
from file_manager import FileManager
from password_utils import is_strong, hash_md5


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def error(message):
    print('\nError: {}'.format(message))
    input('\nPress Enter to try again...')
    cls()

def do_sign_up() -> None:
    with UserService() as user_service:
        username = input('Username: ').strip()
        if user_service.exists(username):
            exit('\nError: User already exists')
        
        password = input('Password: ')
        while not is_strong(password):
            error(is_strong.__doc__)
            print('Username:', username)
            password = input('Password: ')
        
        while input('Confirm Password: ') != password :
            error('Passwords did not match')
            print('Username:', username)
            print('Password:', password)

        clearance = None
        while True:
            try:
                clearance = int(input('User clearance (0 or 1 or 2 or 3): ').strip())
                if clearance > 3 or clearance < 0:
                    raise Exception()
                break
            except:
                error('Clearance belongs to {0, 1, 2, 3}')
                print('Username:', username)
                print('Password:', password)
                print('Confirm Password:', password)

        user_service.add_user(username, password, clearance)
        print('\n User added!\n')

def do_sign_in() -> dict:
    with UserService() as user_service:
        username = input('Username: ').strip()
        password = input('Password: ')
        if not user_service.exists(username):
            exit('Error: User does not exist')
        else:
            print(username, 'found in salt.txt')
        
        user = user_service.get_users()[username]
        salt = user['Salt']
        print('salt retrieved:', salt)
        print('hashing ...')
        pass_salt_hash = hash_md5(salt + password)
        if pass_salt_hash == user['PassSaltHash']:
            print('Authentication for user {} complete.'.format(username))
            print('The clearance for {} is {}.'.format(username, user['SecurityClearance']))
            return {
                'Username': username,
                **user
            }
        else:
            exit('Error: Password did not match')

def operate_on_filestore(user: dict):
    def get_option():
        cls()
        option = input('Options: (C)reate, (A)ppend, (R)ead, (W)rite, (L)ist, (S)ave or (E)xit.\n').strip().capitalize()
        if len(option) == 1 and option in 'CARWLSE':
            return option

        error('Invalid Option')
        return get_option()

    username = user['Username']
    user_clearance = user['SecurityClearance']

    with FileManager() as file_manager:
        while True:
            opt = get_option()
            if opt == 'C':
                filename = input('Filename: ').strip()
                if file_manager.exists(filename):
                    error('File already exists')
                else:
                    file_manager.add_file(filename, username, user_clearance)
                    print('\nFile added!')
                    input('\nPress Enter to continue... ')
            elif opt in 'ARW':
                filename = input('Filename: ').strip()
                if not file_manager.exists(filename):
                    error('File does not exist')
                else:
                    file = file_manager.get_files()[filename]
                    if file['Classification'] > user_clearance:
                        error('You do not have the permission')
                    else:
                        print('Success!!!')
                        input('\nPress Enter to continue... ')
            elif opt == 'L':
                files = file_manager.get_files()
                print('Number of files in the system: ', len(files))
                i = 1
                for name, data in files.items():
                    print('{}.'.format(i))
                    print('\tFile Name       :', name)
                    print('\tOwner           :', data['Owner'])
                    print('\tClassification  :', data['Classification'])
                    i += 1
                input('\nPress Enter to continue... ')
            elif opt == 'S':
                file_manager.save()
                print('Files saved')
                input('\nPress Enter to continue... ')
            elif opt == 'E':
                exit('Logged out')

            

