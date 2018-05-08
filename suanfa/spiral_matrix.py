#!/usr/bin/python3

'''
输出以下格式的数据：
如：
when i=0
1

when i=1
7 8 9
6 1 2
5 4 3

when i=2
21 22 23 24 25
20 7  8  9  10
19 6  1  2  11
18 5  4  3  12
17 16 15 14 13
'''

def out_print(num:int):
    # 几行几列，对等二维列表
    rows = cols = 2 * num + 1
    # print('行列'+str(rows), str(cols))
    num_list = [[0 for col in range(cols)] for row in range(rows)]
    print('初始列表'+str(num_list))
    # 初始位置以及初始值
    s_x = num
    s_y = num
    start_num = 2
    num_list[s_x][s_y] = 1
    # 结束位置
    e_x = 0
    e_y = cols - 1
    # 坐标操作
    op = [(0,1), (1,0), (0,-1), (-1,0)]
    for i in range(1,rows+1):
        if i % 2 == 1:
            direction = op[:2]
        else:
            direction = op[2:]
        for m in range(0,i):
            s_x += direction[0][0]
            s_y += direction[0][1]
            # print(str(m)+'坐标m:'+str(s_x),str(s_y)+ ',i:'+str(i))
            num_list[s_x][s_y] = start_num
            start_num += 1
            if s_x == 0 and s_y == cols - 1:
                break
        if s_x == 0 and s_y == cols - 1:
            break
        for n in range(i):
            s_x += direction[1][0]
            s_y += direction[1][1]
            # print(str(n) + '坐标n:' + str(s_x), str(s_y)+ ',i:'+str(i))
            num_list[s_x][s_y] = start_num
            start_num += 1
    return num_list

test = out_print(1)
print(test)