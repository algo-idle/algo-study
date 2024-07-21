a,b = map(int,input().split())
gcm = 1
lcm = 1

min_num = min(a,b)
max_num = max(a,b)
for i in range(min_num,0,-1):
    if max_num % i == 0 and min_num%i == 0:
        gcd = i
        break
print(gcd)

if gcd == 1:
    print(a*b)
else:
    print(int(gcd*(a/gcd)*(b/gcd)))

