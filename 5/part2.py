import sys

from part1 import read_input


def move(seedrngs, lvl):
    ranges = []
    for dest, source, rng in lvl:
        ranges.append((source, source + rng, -source + dest))
    ranges.sort(key=lambda x: x[0])

    # insert missing ranges. those not included in the input will have an applied difference of 0
    last = 0
    for start, end, diff in list(ranges):
        if start > last:
            ranges.append((last, start, 0))
        last = end
    ranges.sort(key=lambda x: x[0])
    ranges.append((ranges[-1][1], sys.maxsize, 0))

    # split our seed ranges to fit the definitions
    new = []
    for seed_start, seed_end in seedrngs:
        for start, end, diff in list(ranges):
            if seed_start < start:
                break
            if end <= seed_start:
                continue
            rngend = min(seed_end, end)
            new.append((seed_start + diff, rngend + diff))
            seed_start = rngend

    new.sort(key=lambda x: x[0])

    return new


def part2():
    seeds, mapdata = read_input()

    seedrngs = [(x, x + y) for x, y in zip(seeds[::2], seeds[1::2])]
    for lvl in mapdata:
        seedrngs = move(seedrngs, lvl)

    return min(seedrngs)[0]


if __name__ == "__main__":
    print("Part 2:", part2())
