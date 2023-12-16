# type: ignore

def read_input():
    with open("input") as f:
        blocks = f.read().split("\n\n")
    patterns = []
    for bl in blocks:
        grid = {}
        patterns.append(grid)

        for y, line in enumerate(bl.split("\n")):
            for x, char in enumerate(line.strip()):
                grid[x, y] = char
    return patterns

def itercols(grid):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)
    for x in range(0, maxx + 1):
        yield [grid[x, y] for y in range(0, maxy + 1)]

def iterlines(grid):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)
    for y in range(0, maxy + 1):
        yield [grid[x, y] for x in range(0, maxx + 1)]

def find(grid, ignore=None, horizontal=False):
    pre = []
    found = 0
    move = iterlines if horizontal else itercols
    for idx, line in enumerate(move(grid)):
        if found:
            other = idx - 1 - 2 * found
            if other < 0:
                return found - 1
            if line == pre[other]:
                found += 1
            else:
                found = 0
        if not found:
            if pre and line == pre[-1] and ignore != idx - 1:
                found = 1

        pre.append(line)

    if found:
        return idx - found

def vertical(grid, ignore=None):
    return find(grid, horizontal=False)

def horizontal(grid, ignore=None):
    return find(grid, horizontal=True)


def score(grid):
    mirror = vertical(grid)
    if mirror is not None:
        return mirror, "v", mirror + 1

    mirror = horizontal(grid)
    if mirror is not None:
        return mirror, "h", (mirror + 1) * 100

    return None


def part1():
    patterns = read_input()
    total = 0
    for idx, grid in enumerate(patterns):
        _, _, value = score(grid)
        total += value

    return total


def part2():
    patterns = read_input()
    total = 0
    for idx, grid in enumerate(patterns):
        exp, side, scoreexp = score(grid)

        for (x, y), char in grid.items():
            grid[x, y] = "#" if char == "." else "."
            mirror = vertical(grid, ignore=exp if side == "v" else None)
            if mirror is not None:
                total += mirror + 1
                break
            else:
                mirror = horizontal(grid, ignore=exp if side == "h" else None)
                if mirror is not None:
                    total += (mirror + 1) * 100
                    break

            grid[x, y] = char
        else:
            raise RuntimeError("No mirrors")

    return total

if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())
