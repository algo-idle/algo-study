import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    sequence = []
    for i in range(N):
        if i < 3:
            sequence.append(1)
        else:
            sequence.append(sequence[i-3] + sequence[i-2])
    print(sequence[-1])