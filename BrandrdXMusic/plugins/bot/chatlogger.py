from pyrogram import filters
from BrandrdXMusic import app
from BrandrdXMusic.mongo.chats_db import add_chat

@app.on_message(filters.group)
async def chat_logger(client, message):

    await add_chat(message.chat.id)
