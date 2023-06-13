import requests
import os

API_KEY = os.getenv("NewsAPIKey")


def getArticles():
    req = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}")
    content = req.json()

    articles = content['articles']
    print(articles[0]['title'])
    print(articles[0]['description'])


