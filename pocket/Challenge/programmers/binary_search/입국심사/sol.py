def solution(n, times):
    ans = 0

    # 주어진 t안에 처리할 수 있는 사람의 수를 반환함
    def is_possible(t):
        return sum([t // time for time in times])

    start, end = 0, times[0] * n
    while start <= end:
        mid = (start + end) // 2
        possible = is_possible(mid)
        # mid안에 처리할 수 있는 사람의 수가 n보다 크거나 같은 경우 == mid안에 처리 가능하다!
        if possible >= n:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    return ans