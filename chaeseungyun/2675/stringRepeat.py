def solve(R, S):
    splited = list(S)
    result = ''
    for item in splited:
        for i in range(int(R)):
            result += item
    return result

def main():
    T = int(input())
    resultList = []

    for i in range(T):
        R = input().split()
        resultList.append(solve(R[0], R[1]))

    for i in resultList:
        print(i)

main()