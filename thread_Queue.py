import threading
import time
from queue import Queue

#Queue
q = Queue(maxsize=10)

def func(q):
    while True:
        start_time = time.time()
        print('Hello World')
        time.sleep(0.1)
        end_time = time.time()
        interval = end_time - start_time
        #print(interval)
        q.put(interval)

def func2(q):
    while True:
        item = q.get()
        print(item)


thread1 = threading.Thread(target=func, args=(q,))
thread1.start()

thread2 = threading.Thread(target=func2, args=(q,))
thread2.start()