import math

num= int(input())
arr = []
for _ in range(num):
    tmp = int(input())
    arr.append(tmp)
    
interval = []
for i in range(len(arr)-1):
    dif = arr[i+1] - arr[i]
    interval.append(dif)

gcd = 1
min_dist = min(interval)
gcd = math.gcd(*interval)

tree = 0
for dif in interval:
    if dif == min_dist:
        pass
    tree += (dif//gcd)-1
    
print(tree)
