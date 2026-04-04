import time


def do_work(task_id: int, duration: int) -> str:
    """重い処理をシミュレートする関数"""
    print(f"Task {task_id} started, will take {duration} seconds")
    time.sleep(duration)
    print(f"Task {task_id} completed")
    return f"Result of task {task_id}"


def run_sync_tasks(tasks: int) -> list[str]:
    """複数のタスクを順番に実行する関数"""
    results = []
    for i in range(tasks):
        result = do_work(i, 1)  # 各タスクは1秒かかると仮定
        results.append(result)
    return results


if __name__ == "__main__":
    start_time = time.time()
    results = run_sync_tasks(tasks=5)
    end_time = time.time()

    print("========= Results =========")
    for result in results:
        print(result)

    print(f"Total execution time: {end_time - start_time:.2f} seconds")
