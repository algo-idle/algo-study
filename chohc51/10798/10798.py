from sys import *

arr = [['*'] * 15 for _ in range(5)]
result = ''
for i in range(5):
    tmp = stdin.readline().rstrip()
    for j in range(len(tmp)):
        arr[i][j] = tmp[j]



for i in range(15):
    for j in range(5):
        if arr[j][i] != '*':
            result += arr[j][i]
print(result)
    