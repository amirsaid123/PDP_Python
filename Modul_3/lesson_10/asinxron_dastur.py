import asyncio
#
# async def async_task():
#     print("Task started")
#     await asyncio.sleep(2)
#     print("Task completed")
#
# async def main():
#     await asyncio.gather(async_task(), async_task(), async_task())
#
# asyncio.run(main())



async def task_one():
    print("Task one starts")
    await asyncio.sleep(3)
    print("Task one ends")

async def task_two():
    print("Task two starts")
    await asyncio.sleep(1)
    print("Task two ends")

async def main():
    await asyncio.gather(task_one(), task_two())  # Runs both tasks concurrently

asyncio.run(main())
