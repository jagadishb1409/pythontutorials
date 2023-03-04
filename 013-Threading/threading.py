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

