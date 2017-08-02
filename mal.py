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
        print('(a)dd anime   (s)earch   (m)ain menu   (o)pen in browser')
        choice = input('> ')
        if choice == 'a':
            mal.add_anime(anime)
            clear()
            print('Added in Your Plan to Watch List')
            time.sleep(1)
            main()
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
        print('Please Wait... Fetching Info...')
        res = mal.search_anime(anime.title)
        res = res[0]
        clear()
        print('%s (%s)\nMAL Score: %s\nYour Score: %s\nEpisodes: %s/%s\nStatus: %s\nDuration: %s - %s\n\n\t\tSynopsis\n%s\n\n' %(anime.title, anime.english, res.score, temp.user_score, temp.user_episodes, res.episodes, res.status, anime.start_date, anime.end_date, res.synopsis)) 
        print('(u)pdate   (d)elete   (s)earch   (m)ain   (o)pen in browser')
        choice = input('> ')
        if choice == 'u':
            mal.update_anime(anime)
            clear()
            print('Updated!')
            time.sleep(1)
            main()
        elif choice == 'd':
            mal.delete_anime(anime)
            clear()
            print('Deleted!')
            time.sleep(1)
            main()
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

def view_user_list(user_list, status):
    
    temp = []
    counter = 1
    
    for anime in user_list:
        if anime.user_status == status:
            temp.append(anime)

    for anime in temp:
        print('%d.) %s' %(counter, anime.title))
        counter = counter + 1

    print('\n(v)iew   (b)ack   (m)ain')
    choice = input('> ')

    if choice == 'v':
        num = int(input('Enter Anime Number: '))
        display_anime_info(temp[num-1])
    elif choice == 'b':
        view_user_list_main()
    else:
        main()

def view_user_list_main():
    
    clear()
    print('(w)atching   (c)ompleted   (p)lan to watch   (o)n hold   (d)ropped   (m)ain menu')
    choice = input('> ')
    user_list = mal.get_user_list()
    
    if choice == 'w':
        view_user_list(user_list, '1')
    elif choice == 'c':
        view_user_list(user_list, '2')
    elif choice == 'p':
        view_user_list(user_list, '6')
    elif choice == 'o':
        view_user_list(user_list, '3')
    elif choice == 'd':
        view_user_list(user_list, '4')
    elif choice == 'm':
        main()
    else:
        clear()
        print('Invalid Option')
        time.sleep(2)
        view_user_list_main()

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
    print('1.)Search Anime\n2.)View Anime List\n3.)Exit\n')
    choice = int(input('Enter Choice: '))
    if choice == 1:
        search()
    elif choice == 2:
        view_user_list_main()
    elif choice == 3:
        clear()
        sys.exit(0)
    else:
        main()

login()
