import threading
from queue import Queue

#Queue
q = Queue(maxsize=10)

def func(queue):
    print('Hello World')
    for i in range(10):
        queue.put(i)

def func2(queue):
    print('Hello world')
    while not queue.empty():
        item = queue.get()
        print(item)
        queue.task_done()

thread1 = threading.Thread(target=func, args=(q,))
thread1.start()

thread2 = threading.Thread(target=func2, args=(q,))
thread2.start()