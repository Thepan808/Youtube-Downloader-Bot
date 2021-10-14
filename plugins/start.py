from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤺°Canal°", url="https://t.me/GR4V3_S4D_CRAZZY")],
        [InlineKeyboardButton(
            "🙃 Criador 💬", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")]
    ])
    welcomed = f"Olá <b>{message.from_user.first_name}</b>\nUse /help para mais informações"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
