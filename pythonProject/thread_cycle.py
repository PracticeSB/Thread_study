import threading
import time

def thread_run():
    time.sleep(10)
    print('Hello World')

if __name__ == '__main__':
    #damen은 기본적으로 False가 제공되며 daemon이 True일 경우에는 main_thread가 끝날때 같이 sub_thread도 끝나는 명령
    thread1 = threading.Thread(target=thread_run, daemon=True)
    #thread1.daemon
    thread1.start()
    #thread1.join() #Join함수는 main thread와 sub_thread와의 시간을 맞춰줄 수 있는 함수
    print('프린팅 해보자')

