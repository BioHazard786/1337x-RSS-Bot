from .__init__ import *


@bot.on_message(filters.command(['add']) & filters.private)
async def add(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("<code>Only for owner use</code>")

    args = message.text.split(" ", 1)
    if len(args) <= 1:
        return await message.reply(f"<b>Not applicable</b>")

    torrent_user = get_user_by_link(args[-1])
    if not torrent_user:
        return await message.reply(f"<b>Invalid link format</b>")

    Torrent_User.Set({torrent_user: args[-1]})
    await loop.run_in_executor(executor, lambda: add_users(link=str(args[-1]), user=torrent_user))
    return await message.reply(f"<b>Added User to the feed!</b>")


@bot.on_message(filters.command(['remove']) & filters.private)
async def remove(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("<code>Only for owner use</code>")

    args = message.text.split(" ", 1).strip()
    if len(args) <= 1:
        return await message.reply(f"<b>Not applicable</b>")

    torrent_user = get_user_by_link(args[-1])
    if not torrent_user:
        return await message.reply(f"<b>Invalid link format</b>")

    try:
        Torrent_User.Remove(torrent_user)
        await loop.run_in_executor(executor, lambda: remove_users(link=str(args[-1])))
        return await message.reply(f"<b>Removed User from the feed!</b>")
    except:
        return await message.reply(f"<b>User not found!</b>")


@bot.on_message(filters.command(['check']) & filters.private)
async def check(_, message):
    subscribed_feed = Torrent_User.Get()
    counter = 1
    msg = ''
    for user, link in subscribed_feed.items():
        msg += f'<b>{counter}. <a href="{link}">{user}</a></b>\n'
        counter += 1
    await message.reply(msg, disable_web_page_preview=True)


def get_user_by_link(link):
    regex = r'https://1337xx.to\/(.*)\/'
    if torrent_user := re.search(regex, link):
        return str(torrent_user[1])
    else:
        return None
