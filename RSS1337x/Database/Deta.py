from deta import Deta
from RSS1337x.config import DETA
import re

deta = Deta(DETA)
TORRENT_IDS = deta.Base("TORRENT_IDS")
TORRENT_USERS = deta.Base("TORRENT_USERS")


def get_id_by_link(link):
    regex = r'https://1337x.unblockit.click\/.*?\/(\d+)\/.*?'
    if torrent_id := re.search(regex, link):
        return str(torrent_id[1])
    else:
        return link


def check(link):
    key = get_id_by_link(link)
    result = TORRENT_IDS.get(key)
    if not result:
        return True
    else:
        return False


def save(link, msg_id):
    key = get_id_by_link(link)
    doc = {
        'key': key,
        'message_id': msg_id
    }
    TORRENT_IDS.put(doc)


def add_users(link, user):
    doc = {
        'key': link,
        'user': user
    }
    TORRENT_USERS.put(doc)


def remove_users(link):
    TORRENT_USERS.delete(link)


def fetch_users():
    result = TORRENT_USERS.fetch()
    all_items = result.items
    while result.last:
        result = TORRENT_USERS.fetch(last=result.last)
        all_items += result.items
    return all_items
