import os

import cool_push
from QWeather import QWeather


def get_now_weather_info(result):
        result = result['now']

        keys = {'obsTime', 'temp', 'feelsLike', 'text', 'cloud'}
        result_dict = {}

        for key, item in result.items():
            if key in keys:
                result_dict.update({key: item})

        obs_time = '更新时间: ' + result['obsTime']
        temp = '当前温度: ' + result['temp'] + ' ℃'
        feels_like = '体感温度: ' + result['feelsLike'] + ' ℃'
        text = '天气状况: ' + result['text']
        cloud = '云量: ' + result['cloud'] + '%'

        content = '\n'.join([obs_time, temp, feels_like, text, cloud])

        return content, result_dict

def main():
    QW_KEY = os.getenv('QW_KEY')
    LOCATION = os.getenv('LOCATION')
    COOL_PUSH = os.getenv('COOL_PUSH')

    weather = QWeather(QW_KEY)

    now_info, result_dict = get_now_weather_info(weather.get_now_weather(LOCATION))

    daily = weather.get_3d_weather(LOCATION)['daily']
    tomorrow_info = daily[1]

    content = now_info + '\n\n\n'

    tomorrow_info = '明日温度: {} ~ {} ℃\n'.format(tomorrow['tempMin'], tomorrow['tempMax'])
    tomorrow_info += '早晚天气: {}, {}\n'.format(tomorrow['textDay'], tomorrow['textNight'])
    tomorrow_info += '日落时间: {}'.format(tomorrow['sunset'])

    content += tomorrow_info

    cool_push.send_msg_to_qq_group(COOL_PUSH, LOCATION + '天气\n' + content)


if __name__ == '__main__':
    main()
