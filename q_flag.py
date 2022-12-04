import threading
import time
from queue import Queue

q = Queue(maxsize=0)

flag = True
#thread 사이 통신을 위해서 사용하는 event 객체

def tf(q):
    global flag
    while True:
        if flag == True:
            print('tf function')
            flag = False
            q.put(flag)

def tf2(q):
    global flag
    while True:
        flag = q.get()
        if flag == False:
            print('tf2 function')
            flag = True

t1 = threading.Thread(target=tf,args =(q,))
t2 = threading.Thread(target=tf2,args =(q,))
t1.start()
t2.start()