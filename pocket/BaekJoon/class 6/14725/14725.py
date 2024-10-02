import sys
input = sys.stdin.readline

N = int(input().rstrip())
robot = [input().rstrip().split()[1:] for _ in range(N)]

house = {}

def make_house(current, route):
    if not route:
        return
    if route[0] not in current:
        current[route[0]] = {}
    make_house(current[route[0]], route[1:])

for route in robot:
    make_house(house, route)

def print_house(current, depth):
    for key in sorted(current.keys()):
        print(f"{'--' * depth}{key}")
        print_house(current[key], depth + 1)

print_house(house, 0)
