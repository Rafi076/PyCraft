# 4578556644c44a068015bf1fd7d026d8 --> news api key
import requests
import json
query = input("What type of news are you interested in ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-04&sortBy=publishedAt&apiKey=4578556644c44a068015bf1fd7d026d8"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------")