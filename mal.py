from definations import mal
import time
import getpass
import sys
import os

def clear():
    os.system('clear')

def search():
    clear()
    query = input("Enter Search Query: ")
    results = mal.search_anime(query)

    if results == 0:
        clear()
        time.sleep(2)
        print('Nothing Found!')
        main()

    else:
        clear()
        i = 1
        print('\t\tSearch Results for "%s"' %(query))
        for result in results:
            print('%d.) %s' %(i,result.title))
            i = i + 1
        print('\n(v)iew anime   (s)earch again   (m)ain menu')
        choice = input('> ')

        if choice == 'v':
            input('Enter Anime Number: ')
            pass ## for now

        elif choice == 's':
            search()

        elif choice == 'm':
            main()

        else:
            clear()
            time.sleep(2)
            print('Unknown input! Redirecting to Main Menu')
            main()
        

def login():
    clear()
    print('\t\tLogin')
    user = input('Enter Username: ')
    pwd = getpass.getpass('Enter Password for "%s": ' %(user))
    status = mal.authenticate_user(user, pwd)
    if status == -1:
        clear()
        print('Invalid Credentials!\nTry Again')
        time.sleep(2)
        login()
    elif status == 0:
        clear()
        print('Got Empty Reply From Server\nTry Again')
        time.sleep(2)
        login()
    else:
        main()

def main():
    clear()
    print('Welcome!')
    print('1.)Search Anime\n2.)Exit\n')
    choice = int(input('Enter Choice: '))
    if choice == 1:
        search()
    elif choice == 2:
        sys.exit(0)
    else:
        main()

login()
