import sys
read = sys.stdin.readline

problem = str(read())
parenthesis = problem.split("-")
result = []
for numbers in parenthesis:
    total = 0
    number_list = numbers.split("+")
    for number in number_list:
        total += int(number)
    result.append(total)

if len(result) == 1:
    print(result[0])
else:
    for i in range(1, len(result)):
        result[0] -= result[i]
    print(result[0])