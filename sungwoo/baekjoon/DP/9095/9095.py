import sys
read = sys.stdin.readline

T = int(read())
sumList = [1, 2, 4]
for _ in range(T):
    n = int(read())
    done = len(sumList)
    if n <= done:
        print(sumList[n-1])
    else:
        for i in range(done, n):
            sumList.append(sumList[i-3] + sumList[i-2] + sumList[i-1])
        print(sumList[n-1])