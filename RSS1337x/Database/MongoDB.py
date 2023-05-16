import re
from motor.motor_asyncio import AsyncIOMotorClient
from RSS1337x.config import MONGODB


class MongoDB:
    def __init__(self, coll):
        self.coll = coll
        self.get = coll.find_one
        self.insert = coll.insert_one

    async def get(self, doc):
        return await self.get(doc)

    async def insert(self, doc):
        await self.insert(doc)


mongo = AsyncIOMotorClient(MONGODB)
DB = mongo["RSS"]
INDEX = MongoDB(DB['TORRENT_IDS'])


def get_id_by_link(link):
    regex = r'https://1337xx.to\/.*?\/(\d+)\/.*?'
    if torrent_id := re.search(regex, link):
        return str(torrent_id[1])
    else:
        return str(link)


async def save(link, msg_id):
    _id = get_id_by_link(link)
    doc = {
        '_id': _id,
        'message_id': msg_id
    }
    await INDEX.insert(doc)


async def check(link):
    _id = get_id_by_link(link)
    item = {"_id": _id}
    result = await INDEX.get(item)
    if not result:
        return True
    else:
        return False
