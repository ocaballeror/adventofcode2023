with open('input') as f:
    seqs = []
    for line in f:
        seqs.append(list(map(int, line.strip().split())))


def solve(seq):
    last = seq[0]
    diffs = []
    for num in seq[1:]:
        diffs.append(num - last)
        last = num
    if set(diffs) != {0}:
        re, so = solve(diffs)
        return seq[0] - re, seq[-1] + so
    return seq[0], seq[-1]


p1 = 0
p2 = 0
for sq in seqs:
    prev, nxt = solve(sq)
    p1 += nxt
    p2 += prev

print("Part 1:", p1)
print("Part 2:", p2)
