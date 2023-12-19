# type: ignore
from collections import defaultdict

def read_input():
    with open("input") as f:
        data = f.read().strip()

    flows, parts = data.split("\n\n")
    newflows = defaultdict(list)
    for line in flows.split("\n"):
        name, rules = line.strip().rstrip('}').split('{')
        for rule in rules.split(","):
            if ':' in rule:
                condition, res = rule.split(":")
            else:
                condition = 'True'
                res = rule
            newflows[name].append((condition, res))

    newparts = []
    for part in parts.split("\n"):
        part = eval(part.replace('}', ')').replace('{', 'dict('))
        newparts.append(part)

    return newflows, newparts


def proc(part, flows):
    at = 'in'
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']
    while True:
        for cond, dest in flows[at]:
            if not eval(cond):
                continue

            if dest == 'A':
                return True
            if dest == 'R':
                return False
            at = dest
            break
        else:
            raise RuntimeError()


def part1():
    flows, parts = read_input()
    total = 0
    for part in parts:
        if proc(part, flows):
            total += sum(part.values())

    return total


MEM = {}


def ways(search, flows):
    if search == 'in':
        return [[]]

    if search in MEM:
        return MEM[search]

    paths = []
    for name, rules in flows.items():
        acc = []
        for cond, dest in rules:
            if dest == search:
                assert 'True' not in acc
                for way in ways(name, flows):
                    if cond != 'True':
                        paths.append(acc + [cond] + way)
                    else:
                        paths.append(acc + way)

            if '<' in cond:
                cond = cond.replace('<', '>=')
            elif '>' in cond:
                cond = cond.replace('>', '<=')
            acc.append(cond)

    MEM[search] = paths
    return paths



def part2():
    flows, _ = read_input()
    paths = ways('A', flows)
    total = 0
    for path in paths:
        boundaries = {k: (1, 4000) for k in 'xmas'}
        for cond in path:
            if '>=' in cond:
                bigger = True
                param, value = cond.split('>=')
                value = int(value)
            elif '>' in cond:
                bigger = True
                param, value = cond.split('>')
                value = int(value) + 1
            elif '<=' in cond:
                bigger = False
                param, value = cond.split('<=')
                value = int(value)
            elif '<' in cond:
                bigger = False
                param, value = cond.split('<')
                value = int(value) - 1

            low, hi = boundaries[param]
            if bigger and value > low:
                boundaries[param] = (value, hi)
            elif not bigger and value < hi:
                boundaries[param] = (low, value)

        space = 1
        for low, hi in boundaries.values():
            space *= hi - low + 1
        total += space

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
