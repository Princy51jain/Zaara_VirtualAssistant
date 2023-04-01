# Akhbaar padhke sunaao


import requests
import json
from win32com.client import Dispatch


def speak(text):
    speaker = Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.GetDescription() == "Microsoft Zira Desktop - English (United States)":
            speaker.Voice = voice
            break
    speaker.Speak(text)


if __name__ == '__main__':
    speak("Today's top 10 headlines are...")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=54de6b5725794eb58b6dac54b394e221"
    news = requests.get(url).text
    news_dict = json.loads(news)
    artls = news_dict['articles']
    for i in range(0, 9):
        url = artls[i]['url']
        print(f"{i + 1}. {artls[i]['title']} ")
        print(f"for more , please consider this link: {url}")
        speak(artls[i]['title'])
        speak("Moving on to the next headline...")
    speak("Thank you for patiently listening to us...")
