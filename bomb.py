#!/usr/bin/env python

"""
Defuse the bomb with python!

Intended as a training program for debugging python.
"""
import getpass

GLOBAL_BOMB_PASSWORD = 1

def detonate():
    print('The bomb blew up!!1!')
    import sys
    sys.stdout.flush()
    import os
    os._exit(1)


def main():
    global GLOBAL_BOMB_PASSWORD
    try:
        local_password = 10
        user_password = getpass.getpass('User Password: ')

        if long(user_password) + GLOBAL_BOMB_PASSWORD != 5:
            detonate()

        print('Checking global password:')
        if GLOBAL_BOMB_PASSWORD == 1:
            detonate()

        print('Checking local password')
        if local_password != 40:
            detonate()

        print('Uhoh, it\'s about to explode!')
        detonate()
        print('Congratulations, you have defused the bomb!')
    except:
        detonate()


if __name__ == '__main__':
    main()
