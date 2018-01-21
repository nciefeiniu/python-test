import threading
import queue

q = queue.Queue()
nums = 10000
while nums>0:
    q.put(nums)
    nums = nums - 1

def quelist():
    num = q.get()
    return num


class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("线程："+str(self.threadID)+"开始")
        while q.qsize() > 0:
            print("线程"+str(self.threadID)+"卖出第"+str(q.get())+"张票")
        print("线程"+str(self.threadID)+"退出")

thread1 = myThread(1)
thread2 = myThread(2)
thread3 = myThread(3)
thread4 = myThread(4)
thread5 = myThread(5)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
print("退出主线程")