import sys
input = sys.stdin.readline

start, end = map(int, input().rstrip().split())
table = [0 for _ in range(57)]

for i in range(1, len(table)):
    table[i] = 2**(i - 1) + (2 * table[i - 1])


def count(num):
    global table
    cnt = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)
    for i in range(length):
        if bin_num[i] == '1':
            val = length-i-1
            cnt += table[val]
            cnt += (num - 2**val + 1)
            num = num - 2 ** val
    return cnt


print(count(end) - count(start - 1))
