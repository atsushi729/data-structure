import asyncio


async def single_request(i: int) -> int:
    print("start", i)
    await asyncio.sleep(i)
    print("end", i)
    return i


async def main():
    semaphore = asyncio.Semaphore(5)

    async def coroutine(i: int) -> int:
        async with semaphore:
            return await single_request(i)

    return await asyncio.gather(*[coroutine(i) for i in range(5, 0, -1)])


if __name__ == "__main__":
    print(asyncio.run(main()))
