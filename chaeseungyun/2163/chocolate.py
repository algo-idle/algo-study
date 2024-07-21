def solve(n, m):
  if (n == 1 and m == 1): return 0

  bigger = 0
  smaller = 0
  if (n >= m): 
    bigger = n
    smaller = m
  else:
    bigger = m
    smaller = n
  
  if (bigger % 2 ==0): return solve(bigger // 2, smaller) * 2 + 1
  else: return solve(bigger // 2, smaller) + solve(bigger // 2 + 1, smaller) + 1

def main():
  n, m = map(int, input().split())

  if (n == 1 and m == 1): return 0

  return solve(n, m)

print(main())
