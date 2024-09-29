import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    team = [0] + list(map(int, input().rstrip().split()))
    visited = [0 for _ in range(N + 1)]
    res = 0

    for i in range(1, N + 1):
        if not visited[i]:
            stack = [i]

            while True:
                visited[stack[-1]] = True
                next = team[stack[-1]]
                if visited[next] == True:
                    if next in stack:
                        res += len(stack[stack.index(next):])
                    break
                else:
                    stack.append(next)

    print(N - res)
