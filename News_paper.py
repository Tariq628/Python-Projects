# from win32com.client import Dispatch
# import json
# import requests
# def speak(str):
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
# speak("News for Today ")
# url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=ba8551c420f14d84a6541f06250a6376"
# news = requests.get(url).text
# news_json = json.loads(news)
# articles = news_json["articles"]
# for article in articles:
#     print(article["title"])
#     speak(article["title"])
#     speak("Moving On to the next news")


import requests
import json
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=ba8551c420f14d84a6541f06250a6376")
arts = json.loads(r.text)["articles"]
for i in arts:
    print(i['content'])
    speak(i['content'])
    speak("Moving on the next news")