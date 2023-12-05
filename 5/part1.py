def read_input():
    with open('input') as f:
        content = f.read().split('\n\n')

    seeds = list(map(int, content[0].split(':')[1].split()))
    mapdata = []
    for mp in content[1:]:
        mapdata.append([])
        for part in mp.split('\n')[1:]:
            if not part.strip():
                continue
            dest, source, rng = map(int, part.split())
            mapdata[-1].append((dest, source, rng))

    return seeds, mapdata


def move(seed, lvl):
    for dest, source, rng in lvl:
        if seed in range(source, source + rng):
            return seed - source + dest
    return seed


def part1():
    seeds, mapdata = read_input()

    final = []
    for seed in seeds:
        for lvl in mapdata:
            seed = move(seed, lvl)
        final.append(seed)

    return min(final)

if __name__ == "__main__":
    print("Part 1:", part1())
