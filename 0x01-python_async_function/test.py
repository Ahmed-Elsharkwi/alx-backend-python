import asyncio
import time

async def hello():
    await asyncio.sleep(3)
    print("hello")
async def hele():
    await asyncio.sleep(3)
    print("techo")
async def main():
    st = time.time()
    
    reslut = asyncio.create_task(hello())
    reslut_1 = asyncio.create_task(hele())
    
    await hello()
    await hele()
    et = time.time()
    print(et - st)
asyncio.run(main())
