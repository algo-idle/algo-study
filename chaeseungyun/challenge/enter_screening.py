def solution(n, times):
    answer = 0
    
    left = min(times) # 가장 적게 걸리는 시간
    right = max(times) * n # 가장 오래 걸리는 시간
    
    while left <= right:
        mid = left + (right - left) // 2 # 중간값
        total = 0
        for time in times:
            total += mid // time # 각 심사 위원이 시간 내에 검사할 수 있는 사람 수
            if total >= n:
                break
                
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer