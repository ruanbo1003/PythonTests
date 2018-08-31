
import asyncio
import time


async def async_sleep(n):
    await asyncio.sleep(n)

    return f"after sleeped {n}"


async def async_main():
    i = 0
    while i < 10:
        ret = await async_sleep(i)
        print(ret)
        i = i + 1

    print("end of async_main")


def time_sleep():
    time.sleep(10)

    print("time sleep end")
    return None


def main_test():
    # async_sleep()

    # time_sleep()

    print(type(async_sleep))  # <class 'function'>
    print(type(time_sleep))   # <class 'function'>

    async_fun = async_sleep(5)  # <coroutine object async_sleep at 0x10443d468>
    print(async_fun)

    # 这个是函数调用
    # sync_fun = time_sleep()
    # print(sync_fun)


def async_test():
    loop = asyncio.get_event_loop()
    task = async_main()
    loop.run_until_complete(task)

    loop.stop()



def loop_test():
    loop = asyncio.get_event_loop()

    if False:
        my_task = async_sleep()
        loop.run_until_complete(my_task)

    if True:
        tasks = [
            async_sleep(5),
            async_sleep(5),
            async_sleep(5),
            async_sleep(5)
        ]
        loop.run_until_complete(
            asyncio.wait(tasks)
        )

    print("loop test end")


if __name__ == "__main__":
    # main_test()

    # loop_test()

    async_test()
