def solve():
  testCase = int(input())
  reuslt = []

  for i in range(testCase):
    eachCase = list(map(int, input().split()))
    points = eachCase[1:]
    average = sum(points) / eachCase[0]
    count = 0
    for i in range(1, len(eachCase)):
      if (eachCase[i] > average):
        count += 1
    percentage = (count / eachCase[0]) * 100

    reuslt.append(percentage)

  for i in reuslt:
    formatted = f"{i:.3f}%"
    print(formatted)
    

solve()