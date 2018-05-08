#!/bin/python3

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

c = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
print(c)