import math
def solve():
  n = int(input())
  f = int(input())

  if (n % 100 > 0):
    n = math.floor(n / 100) * 100
  
  while(True):
    if (n % f == 0):
      break
    n = n + 1

  if (n % 100 < 10): print('0', end='')
  print(n % 100)

solve()