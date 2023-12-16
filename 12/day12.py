import functools


def read_input():
    with open("input") as f:
        data = []
        for line in f:
            springs, counts = line.split()
            counts = tuple(map(int, counts.split(",")))
            data.append((springs, counts))

        return data


@functools.cache
def matches(springs, counts):
    acc = 0
    countit = iter(counts)

    search = next(countit, None)
    for idx, c in enumerate(springs):
        if c == "." and acc > 0:
            if acc != search:
                return 0
            acc = 0
            search = next(countit, None)
        elif c == "#":
            if search is None:
                return 0
            acc += 1
        elif c == "?":
            if search is None :
                if '#' in springs[idx:]:
                    return 0
                rest = ()
            else:
                if acc > search:
                    return 0
                rest = (search, *countit)

            a = matches('#' * acc + '#' + springs[idx+1:], rest)
            b = matches('#' * acc + '.' + springs[idx+1:], rest)
            return a + b

    return (search is None and acc == 0) or (search is not None and search == acc and not tuple(countit))


def part1():
    data = read_input()
    total = 0
    for springs, counts in data:
        a = matches(springs, counts)
        total += a

    return total


def scale(springs, counts, factor):
    springs = '?'.join([springs] * factor)
    counts = counts * factor
    return springs, counts


def part2():
    data = read_input()
    total = 0
    for springs, counts in data:
        total += matches(*scale(springs, counts, 5))

    return total

    

if __name__ == "__main__":
    print('part 1:', part1())
    print("part 2:", part2())
