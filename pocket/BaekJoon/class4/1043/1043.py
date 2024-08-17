from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
know = list(map(int, input().rstrip().split()))

if know == [0]:
    print(M)
    exit(0)

know.pop(0)
user_visit = [False for _ in range(N + 1)]
party_visit = [False for _ in range(M)]

for k in know:
    user_visit[k] = True

user_party = {u: [] for u in range(1, N + 1)}
party_user = {p: [] for p in range(M)}

for i in range(M):
    user_ids = list(map(int, input().rstrip().split()))[1:]
    party_user[i] = user_ids
    for user_id in user_ids:
        user_party[user_id].append(i)

q = deque([k for k in know])
while q:
    u = q.popleft()

    for party in user_party[u]:
        if not party_visit[party]:
            party_visit[party] = True
            for user in party_user[party]:
                if not user_visit[user]:
                    user_visit[user] = True
                    q.append(user)

print(party_visit.count(False))
