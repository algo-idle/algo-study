from sys import *

background = [[0 for i in range(100)] for j in range(100)]

count = int(stdin.readline())
answer = 0
for _ in range(count):
    width,length = map(int,stdin.readline().split())
    for i in range(10):
        for j in range(10):
            background[length+i][width+j] = 1

    
for i in range(100):
    for j in range(100):
        answer += background[i][j]
    
print(answer)
        
    
