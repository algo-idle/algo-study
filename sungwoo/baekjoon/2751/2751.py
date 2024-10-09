import sys
read = sys.stdin.readline

N = int(read())
nums = [int(read()) for _ in range(N)]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    return merge(left, right)


def merge(left, right):
    li = []
    l = 0
    r = 0
    while l + r < len(left) + len(right):
        if l == len(left):
            li.append(right[r])
            r += 1
        elif r == len(right):
            li.append(left[l])
            l += 1
        else:
            if left[l] < right[r]:
                li.append(left[l])
                l += 1
            else:
                li.append(right[r])
                r += 1
    return li


for i in merge_sort(nums):
    print(i)