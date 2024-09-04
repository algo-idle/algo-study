def solution(scores):
    wanhoX, wanhoY = scores.pop(0)
    scores.sort(key=lambda x: (-x[0], x[1]))
    ranking = 1
    maxY = 0
    for x, y in scores:
        if wanhoX < x and wanhoY < y:
            return -1
        if y >= maxY:
            maxY = y
            if wanhoX + wanhoY < x + y:
                ranking += 1
    return ranking

scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
print(solution(scores))