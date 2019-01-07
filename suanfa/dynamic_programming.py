# -*- coding: utf-8 -*-


# 动态规划，长度为n的绳子，剪成m段，最大乘积
def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    products = [0, 1, 2, 3]
    for i in xrange(4, length + 1):
        max_l = 0
        for j in xrange(1, i / 2 + 1):
            product = products[j] * products[i - j]
            if max_l < product:
                max_l = product
            if len(products) > i + 1:
                products[i] = max_l
            else:
                products.append(max_l)
    print products
    return products[length]


if __name__ == '__main__':
    print cut_rope(9)