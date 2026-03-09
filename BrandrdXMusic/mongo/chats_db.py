from BrandrdXMusic.utils.mongo import db 

chatsdb = db.network_chats

async def add_chat(chat_id: int):
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        await chatsdb.insert_one({"chat_id": chat_id})

async def get_chats():
    chats = []
    async for chat in chatsdb.find():
        chats.append(chat["chat_id"])
    return chats
