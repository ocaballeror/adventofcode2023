import heapq
from collections import defaultdict

grid = {}
# find manually because reasons
head = (65, 57)
headchar = '|'


def read_input():
    data = open('input').read().strip()
    lines = data.replace('S', headchar).split("\n")

    newdata = []
    for idx, line in enumerate(lines):
        newline = []
        for chari, ch in enumerate(line):
            newline.append(ch)
            if chari + 1 >= len(line):
                continue
            if ch in 'FL-' and line[chari + 1] in '-7J':
                newline.append('-')
            else:
                newline.append('#')
        newdata.append(''.join(newline))

    newnewdata = []
    for idx, line in enumerate(newdata):
        newnewdata.append(line)
        if idx + 1 >= len(newdata):
            continue

        newline = []
        for chari, ch in enumerate(line):
            other = newdata[idx + 1][chari]
            if ch in 'F7|' and other in '|LJ':
                newline.append("|")
            else:
                newline.append("#")
        newnewdata.append("".join(newline))

    grid = {}
    for y, line in enumerate(newnewdata):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char

    return grid


def adjacent(pos):
    x, y = pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for movex, movey in moves:
        move = x + movex, y + movey
        yield move


def findpaths(grid):
    wait = defaultdict(list)
    got = defaultdict(bool)
    to_visit = set()

    for pos, val in grid.items():
        if val in '.#':
            to_visit.add(pos)

    for node in to_visit:
        found = False
        if node in got:
            found = got[node]
        else:
            for move in adjacent(node):
                if move not in grid:
                    found = True
                    break

                if move in got:
                    if got[move]:
                        found = True
                        break
                    else:
                        continue

                if grid[move] in '.#':
                    wait[move].append(node)

        if found:
            got[node] = found
            notify(node, found, wait, got, to_visit)

    return got


def notify(node, found, wait, got, pending):
    if node not in wait:
        return
    waiters = wait.pop(node)
    for wt in waiters:
        got[wt] = found
        pending.difference_update(wt)
        notify(wt, found, wait, got, pending)


def moves(pos, grid):
    x, y = pos
    moves = [(-1, 0, '-LFS'), (1, 0, '-J7S'), (0, -1, '|7FS'), (0, 1, '|LJS')]
    for movex, movey, opts in moves:
        move = x + movex, y + movey
        if move not in grid:
            continue
        other = grid[move]
        if grid[move] in opts and not (
            grid[pos] in 'LJF7' and grid[pos] == other
        ):
            yield move


def dijkstra(grid, head):
    to_visit = [(0, head, [])]
    paths = defaultdict(list)
    seen = set()
    while to_visit:
        _, pos, path = heapq.heappop(to_visit)
        for move in moves(pos, grid):
            paths[move] = (
                min(paths[move], path + [move], key=len)
                if move in paths
                else path + [move]
            )
            if move not in seen:
                heapq.heappush(to_visit, (len(path) + 1, move, path + [move]))
        seen.add(pos)

    return paths


def loop(grid, head):
    head = (head[0] * 2, head[1] * 2)
    paths = dijkstra(grid, head)
    for dest, path in sorted(
        paths.items(), key=lambda x: len(x[1]), reverse=True
    ):
        endmoves = list(moves(dest, grid))
        if len(endmoves) != 2:
            continue
        endmoves.remove(path[-2])

        if endmoves[0] in paths:
            return set(path + paths[endmoves[0]][::-1] + [head])


def part1(loop):
    return len(loop) // 4


def part2(grid, loop):
    for pos, val in grid.items():
        if pos not in mainloop:
            grid[pos] = '.'

    paths = findpaths(grid)
    for pos, val in grid.items():
        if pos in mainloop or pos[0] % 2 == 1 or pos[1] % 2 == 1:
            continue

        if pos in paths:
            grid[pos] = 'O'
        else:
            grid[pos] = 'I'

    return len([k for k, v in grid.items() if v == 'I'])


grid = read_input()
mainloop = loop(grid, head)


print("Part 1:", part1(mainloop))
print("Part 2:", part2(grid, mainloop))
