import sys

read = sys.stdin.readline
N = int(read())
for _ in range(N):
    p = list(read())
    p.pop()
    n = int(read())
    try:
        nums = list(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    except:
        numㅇs = []
    isReverse = False
    isError = False
    for order in p:
        if order == "R":
            isReverse = not isReverse
        else:
            if n == 0:
                isError = True
                break
            n -= 1
            nums.pop() if isReverse else nums.pop(0)
    if isReverse:
        nums.reverse()
    result = "["
    for num in nums:
        result += str(num) + ","
    if result.strip()[-1] == ",":
        result = result[:-1]
    result += "]"
    print("error") if isError else print(result)
