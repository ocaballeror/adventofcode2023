# type: ignore


def read_input():
    grid = []
    with open("input") as f:
        for line in f:
            grid.append(list(line.strip()))

    assert len(set(len(line) for line in grid)) == 1
    return grid


def move(x, y, dir):
    assert 0 <= dir <= 3

    if dir == 0:
        return x, y - 1
    if dir == 1:
        return x + 1, y
    if dir == 2:
        return x, y + 1
    return x - 1, y


def rotate(dir, mirror):
    assert mirror in "/\\"

    if mirror == "/":
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2
    elif mirror == "\\":
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0

    return dir


def draw(grid, x, y, dir):
    pre = grid[y][x]
    grid[y][x] = "^>v<"[dir]
    for line in grid:
        print("".join(line))
    grid[y][x] = pre


def sim(grid, start=(0, 0, 1)):
    maxy = len(grid)
    maxx = len(grid[0])
    seen = set()
    energized = set()
    heads = {start}
    while heads:
        x, y, dir = heads.pop()
        while 0 <= x < maxx and 0 <= y < maxy:
            if (x, y, dir) in seen:
                break

            energized.add((x, y))
            seen.add((x, y, dir))
            char = grid[y][x]
            if char in "/\\":
                dir = rotate(dir, char)
            elif char in "-|":
                if char == "-" and dir in (0, 2):
                    heads.add((x, y, 1))
                    heads.add((x, y, 3))
                    break
                elif char == "|" and dir in (1, 3):
                    heads.add((x, y, 0))
                    heads.add((x, y, 2))
                    break
            x, y = move(x, y, dir)

    return len(energized)


def part1():
    return sim(read_input())


def part2():
    grid = read_input()

    best = 0
    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            if x == 0:
                best = max(best, sim(grid, (x, y, 1)))
            elif x == len(line) - 1:
                best = max(best, sim(grid, (x, y, 3)))
            if y == 0:
                best = max(best, sim(grid, (x, y, 2)))
            elif y == len(grid) - 1:
                best = max(best, sim(grid, (x, y, 0)))

    return best


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
