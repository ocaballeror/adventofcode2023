import itertools


def parse(data):
    return {
        (x, y): char
        for y, line in enumerate(data.strip().split("\n"))
        for x, char in enumerate(line.strip())
    }


def read_input():
    with open("input") as f:
        return parse(f.read())


def draw(grid):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)
    return "\n".join(("".join(grid[x, y] for x in range(maxx + 1))) for y in range(maxy + 1))


def itercols(grid):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)
    for x in range(0, maxx + 1):
        new = yield [grid[x, y] for y in range(0, maxy + 1)]
        if not new:
            continue
        for y, char in enumerate(new):
            grid[x, y] = char


def iterlines(grid):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)
    for y in range(0, maxy + 1):
        new = yield [grid[x, y] for x in range(0, maxx + 1)]
        if not new:
            continue
        for x, char in enumerate(new):
            grid[x, y] = char


def roll(grid, move="^"):
    if move == "^":
        itfunc = itercols
        rev = False
    elif move == ">":
        itfunc = iterlines
        rev = True
    elif move == "v":
        itfunc = itercols
        rev = True
    elif move == "<":
        itfunc = iterlines
        rev = False
    else:
        raise ValueError(move)

    it = itfunc(grid)
    line = next(it)
    while True:
        if rev:
            line.reverse()

        idx = 0
        while idx < len(line):
            if line[idx] != ".":
                idx = idx + 1
                continue
            nextidx = next(
                (idx for idx, char in enumerate(line[idx + 1 :], idx + 1) if char != "."),
                None,
            )
            if nextidx is None:
                break
            assert nextidx > idx
            assert nextidx < len(line)
            assert line[nextidx] in "#O"

            if line[nextidx] == "#":
                idx = nextidx
            elif line[nextidx] == "O":
                line[nextidx] = "."
                line[idx] = "O"
                idx = idx + 1

        try:
            if rev:
                line.reverse()
            line = it.send(line)
        except StopIteration:
            break


def score(grid):
    maxy = max(x[1] for x in grid)
    return sum(maxy + 1 - y for (x, y), char in grid.items() if char == "O")


def part1():
    grid = read_input()
    roll(grid, "^")

    return score(grid)


def part2():
    grid = read_input()

    seen = []
    for it in itertools.count():
        for move in "^<v>":
            roll(grid, move)
        graph = draw(grid)
        if graph in seen:
            base = seen.index(graph) + 1
            cycle = it - base + 1
            break
        seen.append(graph)

    same = seen[int((1e9 - base) % cycle + base) - 1]
    return score(parse(same))


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
