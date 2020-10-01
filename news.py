import json
import requests
import os
import time
import bcolors

newsapi = "https://newsapi.org/v2/"
APIKey = "[KEY HERE]"

os.system('clear')
def updateAPI():
    global x
    news = requests.get(newsapi + "top-headlines?category=health&apiKey=" + APIKey)
    x = news.json()['articles']
updateAPI()

while True:
    for p in x:
        updateAPI()
        print(bcolors.HEADER + p['title'] + bcolors.ENDC)
        if(p['description'] != None):
            print(bcolors.WARN + p['description'] + bcolors.ENDC)
        print(bcolors.UNDERLINE + p['url'] + bcolors.ENDC)
        print("\n")
        time.sleep(3)
