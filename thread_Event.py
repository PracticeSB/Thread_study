import threading
import time

#thread 사이 통신을 위해서 사용하는 event 객체

def tf(event_obj):
    print('tf function')
    time.sleep(3)
    event_obj.set()

def tf2(event_obj):
    event_obj.wait()
    print('tf2 function')

event_lock = threading.Event()

t1 = threading.Thread(target=tf,args =(event_lock,))
t2 = threading.Thread(target=tf2,args =(event_lock,))
t1.start()
t2.start()