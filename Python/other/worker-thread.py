class task:
    offset = 0


class TaskCompleate:

    def call_back(self):
        print("Task is completed")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_complete = TaskCompleate()

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self):
        if self.tasks:
            task = self.tasks.pop(0)
            task.call_back()

    def poll(self):
        if self.tasks:
            task = self.tasks.pop(0)
            return task
        return None


def main():
    manager = TaskManager()

    for i in range(5):
        task = task()
        manager.add_task(task)

    while True:
        task = manager.poll()
        task.call_back()
