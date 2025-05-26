import asyncio
import aiosqlite


async def async_fetch_users(cursor):
    """ fetch all users """
    cur = await cursor.execute("SELECT * FROM users")
    print(await cur.fetchall())

async def async_fetch_older_users(cursor):
    """ fetch all users older than 40 """
    cur = await cursor.execute("SELECT * FROM users WHERE age > 40")
    print(await cur.fetchall())

async def main():
    async with aiosqlite.connect("users.db") as db:
        await asyncio.gather(async_fetch_users(db), async_fetch_older_users(db))

asyncio.run(main())
