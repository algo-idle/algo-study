import sys
input = sys.stdin.readline

N = int(input().rstrip())


def get_primes(n):
    nums = [i for i in range(n + 1)]
    nums[1] = 0
    for i in range(2, n + 1):
        for j in range(i * i, n + 1, i):
            nums[j] = 0

    return list(filter(lambda x: x != 0, nums))


def get_prefix_sum(nums):
    prefix_sum = [0 for _ in range(len(nums) + 1)]
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def sol(n):
    if n == 1:
        return 0
    primes = get_primes(n)
    prefix_sum = get_prefix_sum(primes)

    m = len(prefix_sum)
    ans = 0
    front, rear = 0, 1

    while True:
        _sum = prefix_sum[rear] - prefix_sum[front]
        if _sum == n:
            ans += 1
            rear += 1
            if rear == m:
                break
        elif _sum < n:
            rear += 1
            if rear == m:
                break
        else:
            front += 1

    return ans


print(sol(N))
