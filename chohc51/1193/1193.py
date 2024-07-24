num = int(input())
i = 1
flag = False
while num-i>0:
    num -= i
    i+=1
    flag = not flag
if flag:
    y = 1 + (num-1)
    x = i - (num - 1)
else:
    y = i - (num - 1)
    x = 1 + (num-1)
print("{}/{}".format(y,x))


    


