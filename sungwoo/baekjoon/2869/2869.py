import sys
read = sys.stdin.readline
import math

A, B, V = map(int, read().split())
print(math.ceil((V-B) / (A-B)))