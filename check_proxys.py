import threading
import requests
import queue
import pymysql


#下面是验证代理ip是否可用
class proThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("线程："+str(self.threadID)+"开始")
        while q.qsize()> 0:
            proxie = q.get()
            response = ''
            try:
                response = requests.get("http://ip.chinaz.com/getip.aspx", proxies=proxie, timeout=30)
            except Exception as err:
                print(err)
            finally:
                if response:
                    print("源ip:"+str(proxie)+"   网页返回结果"+response.text+"this ip is ok")
                else:
                    print("源ip:"+str(proxie)+"         error")


if __name__ == "__main__":
    # 这是消息队列
    q = queue.Queue()
    #连接数据库
    db = pymysql.connect(host='127.0.0.1', user='root', password='820403', db='proxy', port=3306)
    cur = db.cursor()
    # 查询ip port和类型，是http还是https
    sql = "select ip, port, protocol from proxys;"
    print(sql)
    try:
        cur.execute(sql)
        results = cur.fetchall()
        # 判断代理ip类型
        for r in results:
            if r[2] == 0:
                protocol = 'http'
            elif r[2] == 1:
                protocol = 'https'
            else:
                protocol = 'http/https'
            # 加入队列
            ips = r[0] + ':' + str(r[1])
            q.put({protocol: ips})
    except Exception as e:
        print(e)
    finally:
        db.close()
    #打印下队列长度
    print(str(q.qsize()))

    #创建多线程

    #定义线程数量
    threadNum = 5

    for n in range(0, threadNum):
        name = 'thread'+str(n+1)
        name = proThread(n+1)
        name.start()

    for t in range(0, threadNum):
        name = 'thread' + str(t + 1)
        name.join()
    print("检查完毕")


