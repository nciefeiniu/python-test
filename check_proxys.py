import threading
import requests
import queue
import telnetlib

#先准备好数据
#这只是测试，实际可以从数据库读取
q = queue.Queue(20)
# q.put({"http":" 219.244.186.30:3128"})
q.put({"http": "113.200.101.200:80"})
q.put({"http": "61.178.238.122:63000"})
q.put({"http": "110.185.170.184:8080"})
q.put({"http": "58.42.203.165:8118"})
q.put({"http": "218.6.145.11:9797"})
q.put({"http": "14.211.118.160:9797"})
q.put({"http": "61.223.95.232:3128"})
q.put({"http": "114.243.67.243:8118"})
q.put({"http": "36.67.66.115:53281"})
q.put({"http": "49.71.16.6:8118"})
q.put({"http": "125.211.202.26:53281"})
q.put({"http":"113.140.25.4:81"})

#下面是验证代理ip是否可用
class proThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("线程："+str(self.threadID)+"开始")
        while q.qsize()> 0:
            proxie = q.get()
            print(proxie)
            response = ''
            try:
                response = requests.get("http://ip.chinaz.com/getip.aspx", proxies=proxie, timeout=20)
            except Exception as err:
                print(err)
            finally:
                if response:
                    print(response.text)
                else:
                    print("error")

#这里只是简单的开启2个线程
thread1 = proThread(1)
thread2 = proThread(2)
thread1.start()
thread2.start()
thread2.join()
thread1.join()


#
# import requests
#
#
# url = "http://ip.chinaz.com/"
# proxie = {"http":"124.72.109.183:8118"}
# r = requests.get(url, proxies=proxie)
# print(r.text)

# import telnetlib
#
# try:
#     telnetlib.Telnet('124.72.109.183', port='8118', timeout=20)
# except:
#     print ('connect failed')
# else:
#     print ('success')
