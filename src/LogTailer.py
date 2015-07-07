import Queue
import platform
import threading
import subprocess

class LogTailer:

    def __init__(self, log_location):
        self.log_location = log_location
        self.platform = platform.system()
        self.running = False

        self.input_buffer = Queue.Queue(maxsize=20)

    def tail_log(self):
        if self.platform == 'Windows':
            tail_process = subprocess.Popen(['powershell.exe', 'Get-Content', self.log_location, '-Wait'], stdout=subprocess.PIPE)
        else:
            tail_process = subprocess.Popen(['tail', '-f', self.log_location], stdout=subprocess.PIPE)

        while self.running:
            next_line = tail_process.stdout.readline()
            self.input_buffer.put(next_line)
            if not next_line:
                break

        tail_process.kill()

    def start(self):
        self.running = True
        threading.Thread(target=self.tail_log).start()

    def stop(self):
        self.running = False

    def poll(self):
        return self.input_buffer.get()

    def poll_nowait(self):
        return self.input_buffer.get_nowait()

