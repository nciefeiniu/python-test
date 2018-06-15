#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def getxin(x_num:int, x_lists:list, q_num:int, x_site:list):
    result = []
    for i in x_site:
        num = 0
        r_min = i[0]
        r_max = i[2]
        c_min = i[1]
        c_max = i[3]
        print(r_min,r_max,c_min,c_max)
        for j in x_lists:
            if j[0] >= r_min and j[0] <= r_max:
                if j[1] >= c_min and j[1] <= c_max:
                    print(j)
                    num += 1
        print('==============')
        result.append(num)
    return result


if __name__ == '__main__':
    # x_num = input('输入星星个数：').strip()
    # x_lists = []
    # for i in range(int(x_num)):
    #     site = input('请输入星星第%s个坐标(如：1 1)' % str(i + 1)).strip()
    #     x_lists.append(site.split())
    # q_num = input('请输入问题个数：').strip()
    # x_site = []
    # for i in range(int(q_num)):
    #     site = input('请输入第%s个问题(如：1 1 2 2)' % str(i + 1)).strip()
    #     x_site.append(site.split())

    x_num = 4
    x_lists = [[1,1], [2,2],[3,3],[1,3]]
    q_num = 5
    x_site = [[1,1,2,2],[1,1,3,3],[2,2,3,3],[1,2,2,3],[1,1,5,5]]
    test = getxin(x_num,x_lists,q_num,x_site)
    print(test)