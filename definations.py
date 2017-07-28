import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

class Anime:
    
    def __init__(self, id, title, english, episodes, score, type, status, start_date, end_date, synopsis):
        self.id = id
        self.title = title
        self.english = english
        self.episodes = episodes
        self.score = score
        self.type = type
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.synopsis = synopsis

class MyAnimeList:
   
    def authenticate_user(self, user, pwd):
        response = requests.get('https://myanimelist.net/api/account/verify_credentials.xml', auth = HTTPBasicAuth(user,pwd))
        if response.text == 'Invalid credentials':
            return -1
        if response.text == '':
            return 0
        else:
            self.user = user
            self.pwd = pwd
            return 1

    def search_anime(self,query):
        response = requests.get('https://myanimelist.net/api/anime/search.xml?q='+query, auth = HTTPBasicAuth(self.user,self.pwd))
        if response == '':
            return 0
        soup = BeautifulSoup(response.text, 'lxml')    
        entries = soup.find_all('entry')
        search_list = []
        for en in entries:
            anime = en.contents
            while True:
                if '\n' in anime:
                    anime.remove('\n')
                else:
                    break
            
            id = anime[0].text
            title = anime[1].text
            english = anime[2].text
            episodes = anime[4].text
            score = anime[5].text
            type = anime[6].text
            status = anime[7].text
            start_date = anime[8].text
            end_date = anime[9].text
            synopsis = anime[10].text

            entry = Anime(id,title,english,episodes,score,type,status, start_date, end_date, synopsis)
            search_list.append(entry)
        
        return search_list

mal = MyAnimeList()
