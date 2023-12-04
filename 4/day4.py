from functools import cache

matches = []
with open("input") as f:
    total = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        card, allnums = line.split(":")
        got, wins = map(lambda x: set(map(int, x.split())), allnums.split("|"))
        matches.append(len(wins & got))


print("part 1:", sum(1 << ms - 1 for ms in matches if ms))


@cache
def dups(num):
    ms = matches[num - 1]
    if ms == 0:
        return 1
    return 1 + sum(dups(num + i + 1) for i in range(ms))


print("part 2:", sum(dups(i + 1) for i in range(len(matches))))
