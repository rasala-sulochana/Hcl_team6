'''''''''
import threading
print(threading.current_thread().getName())
'''''''''
from threading import *
import time
def demo_thread():
    time.sleep(1)
    print("hi")
t1=Thread(target=demo_thread)
t1.start()
