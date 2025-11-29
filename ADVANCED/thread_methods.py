# thread methods in PYTHON: 

# order of thread excution depends on resources and time took
# which is scheduled by operating system (OS)

# # MEHTOD - 1: MULTIPLE THREADS EXECUTION
# import threading
# import time

# def task1():
#     print("Task-1 started...")
#     time.sleep(5)
#     print("Task-1 completed...")

# def task2():
#     print("Task-2 started...")
#     time.sleep(3)
#     print("Task-2 completed...")


# # creating the multiple threads:
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# # start the thread executions
# t1.start()
# t2.start()

# # wait for threads to complete execution:
# t1.join()
# t2.join()

# print("Main Thread Execution Completed...")


# MEHTOD - 2: THREAD POOL EXECUTIONS
from concurrent.futures import ThreadPoolExecutor
import time

def task1():
    print("Task-1 started...")
    time.sleep(5)
    print("Task-1 completed...")
    return 'task-1'

def task2():
    print("Task-2 started...")
    time.sleep(3)
    print("Task-2 completed...")
    return 'task-2'


# creating the multiple threads:
with ThreadPoolExecutor(max_workers=2) as executor:
    # manage the thread executions to start
    task1_future = executor.submit(task1)
    task2_future = executor.submit(task2)

# wait for threads to complete execution:
task1_result = task1_future.result()
task2_result = task2_future.result()

print("Main Thread Execution Completed...")