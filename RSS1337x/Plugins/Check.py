from .__init__ import *


@bot.on_message(filters.command(['check_status']) & filters.private)
async def check_status(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("<code>Only for owner use</code>")

    args = message.text.split(" ", 1)
    if len(args) <= 1:
        return await message.reply(f"<b>Not applicable</b>")

    url = args[-1].strip()
    response = requests.get(url)
    await message.reply(f"<b>URL : </b><code>{url}</code>\n\n<b>Status Code : </b><code>{response.status_code}</code>")
