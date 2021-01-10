import requests

def send_msg_to_qq_group(KEY, content):
    group_api = 'https://push.xuthus.cc/group/{}'.format(KEY)

    data = {
        'c': content
    }

    return requests.post(group_api, data=data).json()

def send_msg_to_qq_user(KEY, content):
    group_api = 'https://push.xuthus.cc/send/{}'.format(KEY)

    data = {
        'c': content
    }

    return requests.post(group_api, data=data).json()
