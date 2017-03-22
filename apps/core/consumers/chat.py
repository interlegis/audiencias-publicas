import json
import logging
import re
from channels import Group
from apps.core.models import Room, Message
from apps.core.utils import decrypt
from apps.core.consumers.utils import get_room, get_data
from django.contrib.auth.models import User
from django.conf import settings

log = logging.getLogger("chat")


def on_connect(message, pk):
    room = get_room(pk)
    if room is not None:
        message.reply_channel.send({"text": json.dumps({"accept": True})})
        room.online_users += 1
        if room.online_users > room.max_online_users:
            room.max_online_users = room.online_users
        room.save()
        Group(room.group_chat_name).add(message.reply_channel)
        log.debug('Chat websocket connected.')


def on_receive(message, pk):
    room = get_room(pk)
    data = get_data(message)

    if set(data.keys()) != set(('handler', 'message')):
        log.debug("Message unexpected format data")
        return
    else:
        log.debug('Chat message is ok.')

    blackList = settings.WORDS_BLACK_LIST
    wordList = re.sub("[^\w]", " ", data['message'].lower()).split()
    censured_words = list(set(blackList) & set(wordList))
    message = data['message']

    if censured_words:
        for word in censured_words:
            message = re.sub(word, '♥', message, flags=re.IGNORECASE)

    user = User.objects.get(id=decrypt(data['handler']))
    message = Message.objects.create(room=room, user=user,
                                     message=message)
    Group(room.group_chat_name).send(
        {'text': json.dumps({"hmtl": message.html_body()})}
    )


def on_disconnect(message, pk):
    try:
        room = Room.objects.get(pk=pk)
        room.online_users -= 1
        room.save()
        Group(room.group_chat_name).discard(message.reply_channel)
        log.debug('Chat websocket disconnected.')
    except (KeyError, Room.DoesNotExist):
        pass
