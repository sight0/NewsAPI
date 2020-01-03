import json
import requests
import os
import time
import bcolors

newsapi = "https://newsapi.org/v2/"
APIKey = "{GET API FROM https://newsapi.org/register}"

os.system('clear')
def updateAPI():
    global x
    news_us = requests.get(newsapi + "top-headlines?sources=google-news&apiKey=" + APIKey)
    x = news_us.json()['articles']
updateAPI()

while True:
    for p in x:
        updateAPI()
        print(bcolors.HEADER + p['title'] + bcolors.ENDC)
        print(p['description'])
        print("\n")
        time.sleep(5)
