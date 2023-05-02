from RSS1337x import bot, loop
from RSS1337x.config import *
from RSS1337x.Database.Deta import *
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)


async def fetch_torrent_users():
    torrent_users = await loop.run_in_executor(executor, lambda: fetch_users())
    for torrent_user in torrent_users:
        Torrent_User.Set({torrent_user["user"]: torrent_user["key"]})

bot.loop.run_until_complete(fetch_torrent_users())
bot.loop.run_forever()
