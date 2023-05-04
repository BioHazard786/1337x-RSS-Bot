from os import getenv
from time import time
from dotenv import load_dotenv
try:
    load_dotenv("config.env")
except:
    pass

botStartTime = time()
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
CHANNEL = -1001922471186
DETA = getenv("DETA")
OWNER_ID = 798171690
RSS_MESSAGE = '''
<b>{title}</b>

<b>‣ Category : <code>{category}</code></b>
<b>‣ Type : <code>{type}</code></b>
<b>‣ Language : <code>{language}</code></b>
<b>‣ Size : <code>{size}</code></b>
<b>‣ Uploaded By : <code>{uploader}</code></b>

<b>🧲 Magnet :</b>
<code>{magnet_link}</code>
'''


class Torrent_User:
    users = {}

    @classmethod
    def Set(cls, torrent_users):
        cls.users.update(torrent_users)

    @classmethod
    def Get(cls):
        return cls.users

    @classmethod
    def Remove(cls, user):
        cls.users.pop(user)

    @classmethod
    def GetLink(cls, user):
        return cls.users[user]
