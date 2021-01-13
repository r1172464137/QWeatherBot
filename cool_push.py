import requests

def send_msg_to_qq_group(KEY, content):
    group_api = 'https://push.xuthus.cc/group/{}'.format(KEY)

    params = {
        'c': content
    }

    return requests.get(group_api, params=params).json()

def send_msg_to_qq_user(KEY, content):
    group_api = 'https://push.xuthus.cc/send/{}'.format(KEY)

    params = {
        'c': content
    }

    return requests.get(group_api, params=params).json()
