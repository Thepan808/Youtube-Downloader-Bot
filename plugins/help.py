from pyrogram import Client, filters, idle


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Apenas suporta Youtube link, (playlist funciona! Basta por link + audio ou vídeo) =)"
    await message.reply_text(helptxt)
