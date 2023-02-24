import requests
import json
def instadown(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers= {
    'X-RapidAPI-Key': '7b9b9944bdmsh4cd21ef6613b941p1781bbjsn1b56afbb9fd5',
    'X-RapidAPI-Host': 'instagram-downloader-download-instagram-videos-stories.p.rapidapi.com'
  }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return "ссылка не опознан"
    else:
        dict = {}
        if rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'caarousel'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Story-Video':
            dict['type'] = 'story-video'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Story-Image':
            dict['type'] = 'story-image'
            dict['media']=rest['media']
            return dict
        else:
            return "формат не опознан"
            
   
    print(dict)
instadown("https://instagram.com/stories/mr.saidofff/3044355388045539789?utm_source=ig_story_item_share&igshid=YmMyMTA2M2Y=")