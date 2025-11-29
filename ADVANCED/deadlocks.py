# Deadlock of threads in PYTHON

# Deadlock of Threads: A deadlock is a concurrency failure mode where a thread or threads wait for a 
# condition that never occurs. The result is that the deadlock threads are unable to progress and the 
# program is stuck or frozen and must be forcefully terminated.

# Deadlock situation occuring in threads: [handling using timeouts and consistent orders]
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    lock1.acquire()
    print("Task-1 acquired lock-1")
    lock2.acquire()
    print("Task-1 acquired lock-2")

    print("Task-1 started...")
    time.sleep(5)
    print("Task-1 completed...")

    lock2.release()
    lock1.release()

def task2():
    lock2.acquire()
    print("Task-1 acquired lock-2")
    lock1.acquire()
    print("Task-1 acquired lock-1")

    print("Task-2 started...")
    time.sleep(3)
    print("Task-2 completed...")

    lock1.release()
    lock2.release()

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

print("Main Thread is executed...")