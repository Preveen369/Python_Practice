# importantant key concepts of multi-threading in PYTHON:
# multithreading, concurrent programming, threads, process, unit of work
# GIL (global interpreter lock), race condition, multi-core process
# Inter Process Communication (IPC)

# some modules don't have GIL: numpy, pandas, concurrent.features
# multithreading improves performance, efficiency of the program execution
# but may sometimes cause memory bottle-neck issues if occurred

import threading

def my_function(arg1, arg2):
    print(f"Executing my_function thread... with {arg1} {arg2}")

t = threading.Thread(target=my_function, args=(1,5))
# t.daemon = True -> automatically stops when main thread stops
t.start()   # start thread to excute (target function)
t.join()    # wait for thread to finish excution

# after thread finished excution
print("Main thread executed")
