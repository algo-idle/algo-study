from sys import *

while True:
    num = int(stdin.readline())
    count = 1
    answer = [1]
    if num == -1:
        break
    for i in range(2,num):
        if num % i == 0:
            count += i
            answer.append(i)
            
    if count == num:
        print("{} = ".format(num),end='')
        print(*answer,sep=' + ')
    else:
        print("{} is NOT perfect.".format(num))