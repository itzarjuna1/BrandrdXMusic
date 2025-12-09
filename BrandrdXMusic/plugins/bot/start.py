import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from BrandrdXMusic import app
from BrandrdXMusic.misc import _boot_
from BrandrdXMusic.utils.decorators.language import LanguageStart
from BrandrdXMusic.utils.database import add_served_user, is_on_off
import config

# ---- Private panel buttons ----
def private_panel(_):
    return [
        [InlineKeyboardButton(text="❓ Help", callback_data="help")],
        [InlineKeyboardButton(text="💬 Support", url="https://t.me/dark_musicsupport")],
        [InlineKeyboardButton(text="📢 Channel", url="https://t.me/dark_musictm")],
        [InlineKeyboardButton(text="👤 Owner", url="https://t.me/onigirisannn")],  # replace with your ID
    ]

@app.on_message(filters.command(["start"]) & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    # Record the user
    await add_served_user(message.from_user.id)
    await message.react("❤")

    # Handle start with parameters (help/sudo/info)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        # your old logic here
        return

    # Normal start
    try:
        keyboard = private_panel(_)
    except Exception:
        keyboard = None

    # Animated welcome message
    try:
        lol = await message.reply_text(f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ︎ {message.from_user.mention}.. ❣️")
        frames = [
            f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {message.from_user.mention}.. 🥳",
            f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {message.from_user.mention}.. 💥",
            f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {message.from_user.mention}.. 🤩",
            f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {message.from_user.mention}.. 💌",
            f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {message.from_user.mention}.. 💞",
        ]
        for frame in frames:
            await asyncio.sleep(0.3)
            await lol.edit_text(frame)
        await lol.delete()
    except Exception:
        pass  # ignore animation errors

    # "**⚡ѕтαятιиg**" animation
    try:
        lols = await message.reply_text("**⚡️ѕ**")
        animation_frames = [
            "⚡ѕт", "**⚡ѕтα**", "**⚡ѕтαя**", "**⚡ѕтαят**",
            "**⚡ѕтαятι**", "**⚡ѕтαятιи**", "**⚡ѕтαятιиg**",
            "**⚡ѕтαятιиg.**", "**⚡ѕтαятιиg....**",
        ]
        for frame in animation_frames:
            await asyncio.sleep(0.1)
            await lols.edit_text(frame)
        await lols.delete()
    except Exception:
        pass  # ignore animation errors

    # Send start photo with buttons safely
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None,
    )

    # Optional logging
    if await is_on_off(config.LOG):
        await app.send_message(
            config.LOG_GROUP_ID,
            f"{message.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ."
            f"\n\n**ᴜsᴇʀ ɪᴅ : {message.from_user.id}\n**ᴜsᴇʀ ɴᴀᴍᴇ: {message.from_user.first_name}",
        )
        
