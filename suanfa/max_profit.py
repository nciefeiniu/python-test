#!/usr/bin/python3

'''
列表代表股票的价格，只能买卖一次，计算哪天买哪天卖收益最大
如
[5,2,1,4,5,3]
输出
1，3
'''

def max_profit(nums: list):
    max_money = 0
    # 买卖天用列表表示
    bs = [0, 0]
    for b in range(len(nums)):
        for s in range(b+1, len(nums)):
            print(b,s)
            if nums[s] - nums[b] >= max_money:
                max_money = nums[s] - nums[b]
                print(max_money)
                bs[0] = b
                bs[1] = s

    if max_money > 0:
        return bs,max_money
    else:
        return [-1, -1]


nums = [5,2,1,4,5,3]
bs,max_money = max_profit(nums)
print("最高收入")
print(max_money)
print(bs)

