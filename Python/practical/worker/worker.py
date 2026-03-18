import multiprocessing
import time
import os


# 1. ワーカー（作業者）の定義
def worker_process(task_queue, result_queue):
    """タスクキューから仕事を取り出し、結果をリザルトキューに入れる"""
    print(f"  [Worker {os.getpid()}] 起動しました")

    while True:
        # タスクを取り出す（タスクがない場合は待機）
        task = task_queue.get()

        # 終了信号（None）を受け取ったらループを抜ける
        if task is None:
            print(f"  [Worker {os.getpid()}] 終了します")
            task_queue.task_done()
            break

        # 実際の処理（ここでは数値の2乗を計算）
        name, num = task
        print(f"  [Worker {os.getpid()}] 処理中: {name}({num})")
        time.sleep(1)  # 重い処理をシミュレート

        result = {name: num * num}
        result_queue.put(result)
        task_queue.task_done()


# 2. マネージャーの定義
class WorkerManager:
    def __init__(self, worker_count=multiprocessing.cpu_count()):
        self.worker_count = worker_count
        self.task_queue = multiprocessing.JoinableQueue()
        self.result_queue = multiprocessing.Queue()
        self.workers = []

    def start(self):
        """指定された数のワーカープロセスを起動"""
        for _ in range(self.worker_count):
            p = multiprocessing.Process(
                target=worker_process,
                args=(self.task_queue, self.result_queue)
            )
            p.daemon = True  # メインプロセス終了時に一緒に終了
            p.start()
            self.workers.append(p)

    def add_task(self, name, data):
        """タスクをキューに追加"""
        self.task_queue.put((name, data))

    def stop(self):
        """全ワーカーに終了信号を送り、停止を待つ"""
        for _ in range(self.worker_count):
            self.task_queue.put(None)
        for p in self.workers:
            p.join()


# 3. メイン処理
if __name__ == "__main__":
    manager = WorkerManager(worker_count=3)
    manager.start()

    # タスクを投入
    tasks = [("Task-A", 10), ("Task-B", 20), ("Task-C", 30), ("Task-D", 40)]
    for name, val in tasks:
        manager.add_task(name, val)

    print("メイン: 全タスクを投入しました。")

    # 結果を回収
    for _ in range(len(tasks)):
        print(f"メイン: 結果受信 -> {manager.result_queue.get()}")

    manager.stop()
    print("メイン: マネージャーを停止しました。")
