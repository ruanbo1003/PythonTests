
import asyncio
import time
import boto3
import jpush


async def async_sleep():
    await asyncio.sleep(1)
    return "async sleep end"


async def my_task():
    ret = await async_sleep()
    return ret


async def main(loop=None):
    if loop:
        asyncio.ensure_future(main(), loop=loop)
        asyncio.ensure_future(main(), loop=loop)

    while 1:
        ret = await async_sleep()
        print("ret:", ret)


def main_test():
    loop = asyncio.get_event_loop()
    task = main(loop)
    loop.run_until_complete(task)

    loop.close()


if __name__ == "__main__":
    main_test()
