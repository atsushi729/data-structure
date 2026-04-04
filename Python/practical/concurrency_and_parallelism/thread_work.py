import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def do_async_task(task_id: int, duration: int) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed after {duration} seconds"


def run_thread_tasks(tasks: int) -> list[str]:
    results: list[str] = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(do_async_task, i, 1) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


if __name__ == "__main__":
    start_time = time.time()
    results = run_thread_tasks(tasks=5)
    end_time = time.time()

    print("========= Results =========")
    for result in results:
        print(result)

    print(f"Total execution time: {end_time - start_time:.2f} seconds")
