from sys import *
import collections
od = collections.OrderedDict()

hold_card_length = int(stdin.readline())
hold_card = map(int,stdin.readline().split())
check_card_length = int(stdin.readline())
check_card = map(int,stdin.readline().split())
for card in check_card:
    od[card] = 0
for card in hold_card:
    if card in od:
        od[card] += 1

for card in od.values():
    print(card)