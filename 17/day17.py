# type: ignore
import heapq
import time, os


def read_input():
    grid = {}
    with open("input") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                grid[x, y] = int(char)

    return grid


def moves(point, grid, dir, atleast=1, atmost=1):
    if dir is None:
        dirs = [(1, 0), (0, 1)]
    else:
        dirx, diry = dir
        assert dirx == 0 or diry == 0
        if dirx == 0:
            dirs = [(-1, 0), (1, 0)]
        elif diry == 0:
            dirs = [(0, -1), (0, 1)]

    x, y = point
    for dirx, diry in dirs:
        cost = 0
        for jump in range(1, atmost + 1):
            other = (x + dirx * jump, y + diry * jump)
            if other not in grid:
                break
            cost += grid[other]

            if jump >= atleast:
                yield (dirx, diry), other, cost


def dijkstra(grid, atleast=1, atmost=3):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)

    seen = set()
    pending = [(0, (0, 0), None)]
    pset = set(pending)  # set copy of `pending` for faster membership checks
    while pending:
        cost, node, dir = heapq.heappop(pending)
        pset.remove((cost, node, dir))

        if node == (maxx, maxy):
            return cost

        for movedir, move, movecost in moves(node, grid, dir, atleast, atmost):
            if (move, movedir) in seen:
                continue

            new = (cost + movecost, move, movedir)
            if new in pset:
                continue
            heapq.heappush(pending, new)
            pset.add(new)

        seen.add((node, dir))

    return -1


def draw(grid, pos, dir):
    maxx = max(x[0] for x in grid)
    maxy = max(x[1] for x in grid)

    pre = grid[pos]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), None]
    grid[pos] = "<>^vX"[moves.index(dir)]
    for y in range(maxy + 1):
        print("".join(str(grid[x, y]) for x in range(maxx + 1)))

    grid[pos] = pre


def part1():
    grid = read_input()
    cost = dijkstra(grid, 1, 3)

    return cost


def part2():
    grid = read_input()
    cost = dijkstra(grid, 4, 10)

    return cost


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
