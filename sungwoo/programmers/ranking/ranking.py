

def solution(n, results):
    result_table = list([0] * n for _ in range(n))
    for x, y in results:
        result_table[x-1][y-1] = 1
    for z in range(n):
        for x in range(n):
            for y in range(n):
                if result_table[x][y] == 0 and result_table[x][z] and result_table[z][y]:
                    result_table[x][y] = 1
    answer = 0
    for i in range(n):
        if sum(result_table[i]) + sum(list(zip(*result_table))[i]) == n-1:
            answer += 1
    print(result_table)
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
