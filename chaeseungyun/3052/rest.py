def main(): 
  result = 0
  counts = {}

  for _ in range(10):
    nature = int(input())
    if (nature % 42 in counts):
      counts[nature % 42] += 1
    else:
      counts[nature % 42] = 1

  for _ in counts.values():
    result += 1

  print(result)

main()