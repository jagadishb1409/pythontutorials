import threading

class MyThread(threading.Thread):
    def run(self):
        # Code to be executed in this thread
        print("Hello from thread", self.name)

        

my_thread = MyThread()
my_thread.start()


my_thread = MyThread()
my_thread.start()
my_thread.join()


import threading

# Create a semaphore object with a maximum of 3 threads allowed to access at a time
semaphore = threading.Semaphore(3)

def worker():
    """Thread worker function"""
    semaphore.acquire()
    try:
        # Do some work...
        print(f"Thread {threading.current_thread().name} is working")
    finally:
        semaphore.release()

# Create 10 worker threads
threads = [threading.Thread(target=worker, name=f"Thread-{i}") for i in range(10)]

# Start the threads
for t in threads:
    t.start()

# Wait for the threads to finish
for t in threads:
    t.join()

print("All threads finished")
