
def solve():
  x = 0
  n = int(input())
  if (n == 1): return 1
  bee = 1

  while(bee  < n):
    bee = bee + 6 * x
    x += 1
  return x

result = solve()

print(result)
