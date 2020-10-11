from time import sleep

import requests
import domen
import json

token = domen.token
URL = 'https://api.telegram.org/bot' + token + '/'


def get_news(country):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country={}&'
           'apiKey={}'.format(country, token))
    response = requests.get(url)
    result = response.json()
    titles = []
    for article in result['articles']:
        titl = article['title']
        titles.append(titl)
    return titles




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'text': message_text}

    return message


def send_message(chat_id, text='вайт о момент'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)



def main():
    #d = get_updates()

    #with open('updates.json', 'w') as file:
    # #json.dump(d, file, indent=2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']


    if text == 'ru':
        news = get_news(text)
        send_message(chat_id, "\n\n".join(news))


    elif text == "гавеную":
        send_message(chat_id, 'Хороший выбор!')
    else:
        send_message(chat_id, 'че хочешь?')


if __name__ == '__main__':
        main()
from pprint import pprint


