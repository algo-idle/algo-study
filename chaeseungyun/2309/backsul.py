def solve():
  nanjang = []

  for _ in range(9):
    nanjang.append(int(input()))

  total = sum(nanjang)
  first = 0
  second = 0

  for i in range(9):
    for j in range(i+1, 9):
      if (total - nanjang[i] - nanjang[j] == 100):
        first = nanjang[i]
        second = nanjang[j]
        break
  
  nanjang.remove(first)
  nanjang.remove(second)
  nanjang.sort()

  for i in range(7):
    print(nanjang[i])

solve()