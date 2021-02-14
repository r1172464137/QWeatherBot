import requests

def send_msg_to_qq_group(content):
    group_api = 'https://push.godever.xyz/'
    title = "天气情况"
    url= 'https://www.qweather.com/'
    params={
        'title':title,
        'description':content,
        'url':url
    }

    return requests.get(group_api, params=params).json()
    print(response)

