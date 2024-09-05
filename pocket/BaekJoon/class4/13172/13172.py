mod = 10 ** 9 + 7
ans = 0
m = int(input())


def custom_pow(x, y):
    res = 1
    piv = x

    while y >= 1:
        if y % 2 == 1:
            res = (res * piv) % mod
        y //= 2
        piv = (piv * piv) % mod

    return res


for i in range(m):
    p, q = map(int, input().split())
    ans = (ans + (q * custom_pow(p, mod - 2))) % mod
print(ans % mod)
