from collections import deque

class RoundRobinScheduler:
    def __init__(self, tasks):
        self.tasks = deque(tasks)

    def run(self, time_quantum):
        while self.tasks:
            current_task = self.tasks.popleft()
            print(f"Running task: {current_task}")
            remaining_time = current_task - time_quantum

            if remaining_time > 0:
                print(f"Task {current_task} still has {remaining_time} units remaining.")
                self.tasks.append(remaining_time)
            else:
                print(f"Task {current_task} completed.")

# Example usage
tasks = [10, 20, 30]
time_quantum = 5

scheduler = RoundRobinScheduler(tasks)
scheduler.run(time_quantum)
