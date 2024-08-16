import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4)

tree = {}


def find(node, target):
    if 'val' in node.keys():
        if target < node['val']:
            if 'left' in node.keys():
                find(node['left'], target)
            else:
                node['left'] = {'val': target}
        else:
            if 'right' in node.keys():
                find(node['right'], target)
            else:
                node['right'] = {'val': target}
    else:
        node['val'] = target


def dfs(node):
    if 'left' in node.keys():
        dfs(node['left'])
        print(node['left']['val'])
    if 'right' in node.keys():
        dfs(node['right'])
        print(node['right']['val'])


while True:
    try:
        num = int(input().rstrip())
        find(tree, num)
    except:
        break

dfs(tree)
print(tree['val'])
