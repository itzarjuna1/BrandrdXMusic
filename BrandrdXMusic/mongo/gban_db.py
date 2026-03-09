from BrandrdXMusic import mongodb
import time

gbans = mongodb["global_bans"]

async def add_gban(user_id: int, banned_by: int):

    if not await gbans.find_one({"user_id": user_id}):
        await gbans.insert_one(
            {
                "user_id": user_id,
                "banned_by": banned_by,
                "time": int(time.time())
            }
        )

async def is_gbanned(user_id: int):

    user = await gbans.find_one({"user_id": user_id})
    return bool(user)
