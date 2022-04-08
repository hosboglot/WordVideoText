import requests
import random
import vk_api
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from main import write_text

with open("token.txt", 'r') as tk:
    token = tk.read()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = VkUpload(vk_session)
longpoll = VkBotLongPoll(vk_session, "212535184")


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


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        write_text(event.object['message']['text'], 3.5)
        gif = upload.document_message(doc=open('output.gif', 'rb'), peer_id=event.object['message']['peer_id'])
        send_msg("", f"doc{gif['doc']['owner_id']}_{gif['doc']['id']}")
