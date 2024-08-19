import sys
read = sys.stdin.readline

N = int(read())
M = int(read())
S = str(read())
P = 'IOI'

cursor = count = answer = 0
while cursor < M - 1:
    if S[cursor : cursor + 3] == P:
        cursor += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(answer)