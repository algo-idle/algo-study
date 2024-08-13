from sys import *
import collections
arr = stdin.readline().rstrip()
result = []
arr_list = arr.upper()
arr_dict = collections.Counter(arr_list)
check = max(arr_dict.values())
for i in arr_dict.keys():
    if arr_dict[i] == check:
        result.append(i)
if len(result) == 1:
    print(*result)
else:
    print("?")
