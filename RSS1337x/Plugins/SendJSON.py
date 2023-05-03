from .__init__ import *


@bot.on_message(filters.command(['send']) & filters.private)
async def send(app, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("<code>Only for owner use</code>")

    reply = await message.reply(f"<code>Sending...</code>")
    for file in glob.glob("*.json"):
        await app.send_document(message.chat.id, file)
    await reply.edit("<code>Sent!</code>")
