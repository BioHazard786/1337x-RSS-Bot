from .__init__ import *
from ..Helpers.FetchTorrentInfo import fetch_torrent_info
from ..Helpers.FetchTorrents import fetch_torrents


def jsload(file):
    with open(file, 'r') as js:
        return json.load(js)


def jsdump(obj, file):
    with open(file, 'w') as js:
        json.dump(obj, js, indent=4)


async def save_torrents():
    for user in Torrent_User.Get():
        torrents = await loop.run_in_executor(executor, lambda: fetch_torrents(user))
        if torrents:
            jsdump(torrents, f"{user}.json")


async def upload_torrents():
    for user in Torrent_User.Get():
        try:
            torrent_links = jsload(f"{user}.json")
        except:
            continue
        for link in reversed(torrent_links):
            if await check(link):
                torrent_info = await loop.run_in_executor(executor, lambda: fetch_torrent_info(link))
                if torrent_info:
                    try:
                        post = await bot.send_message(chat_id=CHANNEL,
                                                      text=RSS_MESSAGE.format(
                                                          title=torrent_info['title'],
                                                          category=torrent_info['Category'],
                                                          type=torrent_info['Type'],
                                                          language=torrent_info['Language'],
                                                          size=torrent_info['Total size'],
                                                          uploader=torrent_info['Uploaded By'],
                                                          magnet_link=torrent_info['magnet_link']
                                                      ),
                                                      disable_web_page_preview=True
                                                      )
                    except FloodWait as e:
                        await asyncio.sleep(e.value)
                    except:
                        continue
                    await save(link, str(post.id))
                await asyncio.sleep(3)

save_post = AsyncIOScheduler()
save_post.add_job(save_torrents, 'interval', minutes=1)
save_post.start()

upload_post = AsyncIOScheduler()
upload_post.add_job(upload_torrents, 'interval', minutes=1)
upload_post.start()
