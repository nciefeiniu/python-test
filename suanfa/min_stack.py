# -*- coding: utf-8 -*-


# 包含Min函数的栈
class MinStack:
    def __init__(self):
        # 数据栈
        self.m_data = []
        # 辅助栈
        self.m_min = []

    def push(self, num):
        self.m_data.append(num)
        if len(self.m_min) == 0:
            self.m_min.append(num)
        else:
            if num < self.m_min[-1]:
                self.m_min.append(num)
            else:
                self.m_min.append(self.m_min[-1])
        # print self.m_data, self.m_min

    def pop(self):
        self.m_min.pop()
        return self.m_data.pop()

    def get_min(self):
        return self.m_min[-1]


if __name__ == '__main__':
    m = MinStack()
    m.push(2)
    m.push(3)
    m.push(1)
    print m.m_min, m.m_data
    m.push(3)
    m.push(2)
    m.push(4)
    m.push(5)
    m.push(1)
    print m.m_min, m.m_data
    print m.get_min()
    print '======================='
    m.pop()
    print m.get_min()
    m.pop()
    print m.get_min()
    m.pop()
    print m.get_min()
    m.pop()
    print m.get_min()