import requests
import json
def instadown(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "2cd5bfb8c7mshd9728daca531f13p118fdfjsn77c84124efd2",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    print(rest)
instadown("https://www.instagram.com/p/Co6DhHvjkjh/?igshid=YmMyMTA2M2Y=")