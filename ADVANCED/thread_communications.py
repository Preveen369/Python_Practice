# thread communications in PYTHON: 
# [to transfer datas and events btw threads]

# key factors: shared memory, locks, semaphores, queues, signals & events, pipes

# thread communication using wait() and notify() functions:
# import threading

# condition = threading.Condition()

# def task1():
#     with condition:
#         print("Thread waiting for signal...")
#         condition.wait()
#         print("Thread recieved signal...")

# t = threading.Thread(target=task1)
# t.start()

# with condition:
#     print("Sending signal...")
#     condition.notify()

# t.join()


# thread communication using queues:
# to share datas safely between one or more threads:
# import threading
# import queue

# q = queue.Queue()

# def task1():
#     while True:
#         data = q.get()
#         print(f"Thread recieved data: {data}")
#         q.task_done()

# t = threading.Thread(target=task1)
# t.start()
# q.put("World")
# q.put("Hello")


# thread communication using daemon threads:
# The Daemon Thread does not block the main thread from exiting 
# and continues to run in the background.
# This thread automatically stops execution when main thread stops.

import threading

def my_function(arg1, arg2):
    print(f"Executing my_function thread... with {arg1} {arg2}")

t = threading.Thread(target=my_function, args=(1,5))
t.daemon = True 
t.start()   
t.join()    

# after thread finished excution
print("Main thread executed")
