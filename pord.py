import requests
import random
import vk_api
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from MyLongPoll import MyVkLongPoll
from vk_api.bot_longpoll import VkBotEventType
from main import write_text

try:
    with open("token.txt", 'r') as tk:
        token = tk.read()

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    longpoll = MyVkLongPoll(vk_session, "212535184")
except Exception as e:
    print(e)


def send_msg(msg, att=''):
    try:
        return vk.messages.send(
            peer_ids=event.object['message']['peer_id'],
            random_id=random.random(),
            message=msg,
            attachment=att
        )
    except Exception as e:
        print(e)

try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            write_text(event.object['message']['text'], 3.5)
            gif = upload.document_message(doc=open('output.gif', 'rb'), peer_id=event.object['message']['peer_id'])
            send_msg("", f"doc{gif['doc']['owner_id']}_{gif['doc']['id']}")
except Exception as e:
    print(e)
