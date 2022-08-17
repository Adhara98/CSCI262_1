import sys, getopt
from processes import do_sign_in, do_sign_up, operate_on_filestore
from password_utils import hash_md5

def main(opts):
    print('\nMD5 ("This is a test") =', hash_md5('This is a test'), '\n')

    if '-i' in dict(opts).keys():
        do_sign_up()
    else:
        user = do_sign_in()
        input('\nPress Enter to continue... ')
        operate_on_filestore(user)
        

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'i')
    try:
        main(opts)
    except KeyboardInterrupt as e:
        print('\n\n Terminated!')

