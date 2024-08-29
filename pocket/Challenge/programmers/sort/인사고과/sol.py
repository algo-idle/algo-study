import time
import random
random.seed(123123)

def solution(scores):
    target = scores[0]
    scores = list(filter(lambda x: sum(x) > sum(target), scores))
    scores.sort(key=lambda x: (-x[0], x[1]))

    buf = 0
    answer = 1
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if buf > score[1]:
            continue
        answer += 1
        buf = score[1]

    return answer

print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
start_time = time.time()
print(solution([[random.randint(0, 100001), random.randint(0, 100001)] for _ in range(100000)]))
end_time = time.time()
print((end_time - start_time) * 1000, "ms")
