from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("how are you",end=" ")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=('jose',))
t2=Thread(target=wish,args=('mich',))
t3=Thread(target=wish,args=('mart',))
t1.start()
t2.start()
t3.start()