num = int(input())
if num == 1:
    print()

count = 2
while num >= count:

    if num % count == 0:
        print(count)
        num //= count
    else:
        count+=1
        
