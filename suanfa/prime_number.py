#!/bin/python3

'''
判断两数之间有多少个素数
'''
def prime_number(start_num, end_num):
    prime_numbers = [x for x in range(start_num, end_num+1) if 0 not in [x % m for m in range(2,x-1)]]
    return prime_numbers,len(prime_numbers)

test,numbers = prime_number(101,200)
print(test,numbers)