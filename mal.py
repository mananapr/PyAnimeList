from definations import mal
import webbrowser
import time
import getpass
import sys
import os

def clear():
    os.system('clear')

def display_anime_info(anime):
    clear()
    user_anime = mal.get_user_list()
    in_user_list = 0
    temp = ''
    for a in user_anime:
        if a.id == anime.id:
            temp = a
            in_user_list = 1
            break

    if in_user_list == 0:
        print('%s (%s)\nScore: %s\nEpisodes: %s\nStatus: %s\nDuration: %s - %s\n\n\t\tSynopsis\n%s\n\n' %(anime.title, anime.english, anime.score, anime.episodes, anime.status, anime.start_date, anime.end_date, anime.synopsis))
        print('(a)dd anime   (s)earch   (m)ain menu (o)pen in browser')
        choice = input('> ')
        if choice == 'a':
            ## add anime
            pass
        elif choice == 's':
            search()
        elif choice == 'm':
            main()
        elif choice == 'o':
            webbrowser.open('https://myanimelist.net/anime/' + anime.id)
        else:
            clear()
            print('Invalid Option... Redirecting to Main Menu')
            time.sleep(2)
            main()
    else:
        print('%s (%s)\nMAL Score: %s\nYour Score: %s\nEpisodes: %s/%s\nStatus: %s\nDuration: %s - %s\n\n\t\tSynopsis\n%s\n\n' %(anime.title, anime.english, anime.score, temp.user_score, temp.user_episodes, anime.episodes, anime.status, anime.start_date, anime.end_date, anime.synopsis)) 
        print('(u)pdate   (d)elete   (s)earch   (m)ain   (o)pen in browser')
        choice = input('> ')
        if choice == 'u':
            ## updtae
            pass
        elif choice == 'd':
            ## delete
            pass
        elif choice == 's':
            search()
        elif choice == 'm':
            main()
        elif choice == 'o':
            webbrowser.open('https://myanimelist.net/anime/' + anime.id)
        else:
            clear()
            print('Invalid Option... Redirecting to Main Menu')
            time.sleep(2)
            main()

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
            anime_num = int(input('Enter Anime Number: '))
            chosen_anime = results[anime_num - 1]
            display_anime_info(chosen_anime)

        elif choice == 's':
            search()

        elif choice == 'm':
            main()

        else:
            clear()
            print('Unknown input! Redirecting to Main Menu')
            time.sleep(2)
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
