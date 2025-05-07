#synchronous
import asyncio
import time


def task(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finishing {name}")


task("smitha")
task("rao")

#aynschronous

async def task1(name):
    print(f"starting {name}")
    await asyncio.sleep(2)
    print(f"finishing {name}")

async def main():
    await asyncio.gather(task1("ashok"),task1("bhat"))

asyncio.run(main())