import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def do_cpu_bound_work(task_id: int, iteration: int) -> str:
    """重い処理をシミュレートする関数"""
    print(f"Task {task_id} started, will perform CPU-bound work for {iteration} iterations")
    total = 0
    for i in range(iteration):
        total += i
    print(f"Task {task_id} completed")
    return f"Result of task {task_id} with total {total}"


def run_process_tasks(tasks: int) -> list[str]:
    """複数のタスクをプロセスプールで実行する関数"""
    results: list[str] = []

    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(do_cpu_bound_work, i, 10000) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


if __name__ == "__main__":
    start_time = time.time()
    results = run_process_tasks(tasks=5)
    end_time = time.time()

    print("========= Results =========")
    for result in results:
        print(result)

    print(f"Total execution time: {end_time - start_time:.2f} seconds")
