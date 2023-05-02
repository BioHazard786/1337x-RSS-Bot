from .__init__ import *


@bot.on_message(filters.command(['start']) & filters.private)
async def start(_, message):
    args = message.text.split(" ")
    if len(args) <= 1:
        try:
            await message.reply_text("<code>I am Alive :)</code>")
        except:
            pass
        return

    torrent_link = await bot.get_messages(chat_id=CHANNEL, message_ids=int(args[-1]))
    torrent_link = torrent_link.entities[-2].url
    reply = await message.reply("<code>Fetching Magnet Link, Please wait...</code>")
    if magnet_link := await loop.run_in_executor(executor, lambda: fetch_magnet_link(torrent_link)):
        msg = f'''
        <b>Magnet Link for :- <u><i>{magnet_link["title"]}</u></i></b>\n\n<code>🧲 {magnet_link["link"]}</code>
        '''

        await reply.edit_text(msg)
    else:
        await reply.edit_text("<code>Couldn't fetch magnet link</code>")
