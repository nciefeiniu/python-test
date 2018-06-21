#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
IO多路复用-select，实现socket的多并发。
当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度，不管哪个Socket是活跃的，都遍历一遍。这会浪费很多CPU时间
效率不高，浪费资源
'''
import socket
import select
import queue

def servers(host, port):
    server = socket.socket()
    server.bind((host, port))
    server.listen(1000)
    # 把server设置为不阻塞
    server.setblocking(False)

    msg_dic = {}
    inputs = [server,]
    outputs = []

    while True:
        # readable是socket链接的集合， output是需要返回数据的socket的集合，  exceptional是发生错误的socket集合
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)
        print(readable,writeable,exceptional)
        # 每次检测到有活跃的时候，就循环遍历整个socket,浪费资源
        for r in readable:
            if r is server:
                # 如果是server，那就把连接加入inputs，让kernel帮我们监控
                conn, addr = r.accept()
                print('有新的连接来自：%s' % str(addr))
                inputs.append(conn)
                msg_dic[conn] = queue.Queue()
            else:
                # 如果不是server， 那肯定就是conn了
                data = r.recv(1024)
                print(data)
                # r.send(data)
                # 把接受数据和发送数据分开,把数据放在msg_dic中
                msg_dic[r].put(data)
                # 并给outputs中增加一个r，也就是告诉select这里有outputs操作
                outputs.append(r)

        #  向客户端发送数据
        for w in writeable:
            send_client_data = msg_dic[w].get()
            w.send(send_client_data)
            # 发送完成，需要清理outputs，避免下次又发送
            outputs.remove(w)

        # 处理异常
        for e in exceptional:
            print(e)


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    servers(HOST, PORT)