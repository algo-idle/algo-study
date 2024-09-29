from collections import deque


def solution(n, results):
    answer = 0
    wl = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    for w, l in results:
        wl[w - 1][l - 1] = 1
        wl[l - 1][w - 1] = -1

    for k in range(n):
        for start in range(n):
            for end in range(n):
                if wl[start][k] == 1 and wl[k][end] == 1:
                    wl[start][end] = 1
                    wl[end][start] = -1

    for i in range(n):
        if 0 not in wl[i]:
            answer += 1

    return answer
