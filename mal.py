from definations import MyAnimeList
import getpass
import sys
import os

def clear():
    os.system('clear')

def search():
    query = input("Query: ")
    results = mal.search_anime(query)
    if results == 0:
        print('Nothing Found!')
    else:
        for result in results:
            print(result.title)

def login():
    user = input('Enter Username: ')
    pwd = getpass.getpass('Enter Password for "%s": ' %(user))
    mal = MyAnimeList()
    status = mal.authenticate_user(user, pwd)
    if status == -1:
        print('Invalid Credentials!\nTry Again')
        login()
    elif status == 0:
        print('Got Empty Reply From Server\nTry Again')
        login()
    else:
        main()

def main():
    print('Welcome!')
    print('1.)Search Anime\n2.)Exit\n')
    choice = int(input('Enter Choice: '))
    if choice == 1:
        search()
    elif choice == 2:
        sys.exit(0)
    else:
        main()

clear()
print('\t\tLogin')
login()
