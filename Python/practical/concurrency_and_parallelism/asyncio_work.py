import asyncio
import time


async def do_async_task(task_id: int, duration: int) -> str:
    await asyncio.sleep(duration)
    return f"Task {task_id} completed after {duration} seconds"


async def run_async_tasks(tasks: int) -> list[str]:
    task_list = [do_async_task(i, 1) for i in range(tasks)]
    results = await asyncio.gather(*task_list)
    return results


if __name__ == "__main__":
    start_time = time.time()
    results = asyncio.run(run_async_tasks(tasks=5))
    end_time = time.time()

    print("========= Results =========")
    for result in results:
        print(result)

    print(f"Total execution time: {end_time - start_time:.2f} seconds")
