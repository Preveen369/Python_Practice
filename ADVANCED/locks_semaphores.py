# Threads Synchronization in PYTHON [locks and semaphore]

# Lock -> Synchronizes/controls only one thread to execute task at same time
# Semaphore -> Synchronizes/controls counter(number) of threads to execute tasks at same time

# # Locking on execution of threads:
# import threading
# import time

# lock = threading.Lock()

# def task1():
#     lock.acquire()
#     print("Task-1 started...")
#     time.sleep(5)
#     print("Task-1 completed...")
#     lock.release()

# def task2():
#     lock.acquire()
#     print("Task-2 started...")
#     time.sleep(3)
#     print("Task-2 completed...")
#     lock.release()

# thread1 = threading.Thread(target=task1)
# thread2 = threading.Thread(target=task2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Main Thread is executed...")


# Semaphores on execution of threads:
import threading
import time

semaphore = threading.Semaphore(2)

def task1():
    semaphore.acquire()
    print("Task-1 started...")
    time.sleep(5)
    print("Task-1 completed...")
    semaphore.release()

def task2():
    semaphore.acquire()
    print("Task-2 started...")
    time.sleep(3)
    print("Task-2 completed...")
    semaphore.release()

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main Thread is executed...")