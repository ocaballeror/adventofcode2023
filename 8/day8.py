import functools
import itertools
import math


with open('input') as f:
    lines = f.read().split('\n')

    dirs = lines[0]
    graph = {}
    for line in lines[2:]:
        if not line.strip():
            continue
        line = (
            line.strip()
            .replace(' = ', ' ')
            .replace('(', '')
            .replace(',', '')
            .replace(')', '')
        )
        node, l, r = line.split()
        graph[node] = (l, r)

head = 'AAA'
pattern = itertools.cycle(dirs)

count = 0
while head != 'ZZZ':
    where = next(pattern)
    head = graph[head][int(where == 'R')]
    count += 1

print("Part 1:", count)

heads = [h for h in graph if h.endswith('A')]


def findcycle(head):
    pattern = itertools.cycle(dirs)
    while not head.endswith('Z'):
        where = next(pattern)
        head = graph[head][int(where == 'R')]
    cycle = 0
    while True:
        where = next(pattern)
        head = graph[head][int(where == 'R')]
        cycle += 1
        if head.endswith('Z'):
            break

    return cycle


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


res = functools.reduce(lcm, map(findcycle, heads))
print("Part 2:", res)
