from sys import *

answer = 0
string_set = set()
N,M = map(int,stdin.readline().split())

for _ in range(N):
    set_word = stdin.readline().rstrip()
    string_set.add(set_word)

for _ in range(M):
    check_word = stdin.readline().rstrip()
    if check_word in string_set:
        answer += 1
        
print(answer)

