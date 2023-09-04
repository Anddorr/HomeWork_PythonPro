import time
import asyncio
from threading import Thread


def red():
    time.sleep(1)
    print('red')


async def yellow():
    await asyncio.sleep(1)
    print('yellow')


def green():
    time.sleep(1)
    print('green\n')


async def main():
    red()
    await asyncio.create_task(yellow())
    th = Thread(target=green)
    th.start()
    await asyncio.sleep(1)
    await asyncio.create_task(main())


asyncio.run(main())

# Я не понял что имеено нужно сделать и сделал это использую все модели python



