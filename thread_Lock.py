import random
import threading
import time

val = 0
# 현재 increment함수와 decrement함수가 global variable에 동시에 접근하여서 언제 시스템이 끝날지 모름
# Lock이라는 개념을 사용!

tl = threading.Lock()

def increment(lock):
    global val
    lock.acquire() #locking
    while val < 10:
        val += 1
        print('increment의 현재 값은:',val)
        sleeptime = random.randint(0,1)
        time.sleep(sleeptime)
    lock.release() #releasing

def decrement(lock):
    global val
    lock.acquire()  # locking
    while val > -10:
        val -= 1
        print('decrement의 현재 값은:',val)
        sleeptime = random.randint(0,1)
        time.sleep(sleeptime)
    lock.release()  # releasing

t1 = threading.Thread(target=increment,args =(tl,))
t2 = threading.Thread(target=decrement,args =(tl,))
t1.start()
t2.start()