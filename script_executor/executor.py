import subprocess
import threading
import queue
import os
import time
from datetime import datetime

class ScriptTask:
    def __init__(self, command, mode='sequential', on_fail='continue'):
        self.command = command
        self.mode = mode
        self.on_fail = on_fail
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

class ScriptExecutor:
    def __init__(self, output_dir='script_outputs'):
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self.running = True
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.worker_thread = threading.Thread(target=self._worker)
        self.worker_thread.start()

    def submit_command(self, command, mode='sequential', on_fail='continue'):
        task = ScriptTask(command, mode, on_fail)
        if mode == 'immediate':
            threading.Thread(target=self._execute_command, args=(task,)).start()
        else:
            self.queue.put(task)

    def _worker(self):
        while self.running:
            try:
                task = self.queue.get(timeout=1)
                self._execute_command(task)
                self.queue.task_done()
            except queue.Empty:
                continue

    def _execute_command(self, task):
        output_file = os.path.join(
            self.output_dir, f"{task.timestamp}_command.log"
        )
        with open(output_file, 'w') as outfile:
            process = subprocess.Popen(
                task.command,
                stdout=outfile,
                stderr=subprocess.STDOUT,
                shell=True
            )
            process.communicate()

        if process.returncode != 0 and task.on_fail == 'stop':
            with self.lock:
                self.running = False
                print(f"Command '{task.command}' failed. Stopping further execution.")

    def stop(self):
        self.running = False
        self.worker_thread.join()
