import itertools


with open('input') as f:
    data = f.read().strip()

lines = [list(line) for line in data.split("\n")]
factor = 1000000
emptycols = []
emptyrows = []

for x in range(len(lines)):
    for y in range(len(lines)):
        if lines[y][x] != '.':
            break
    else:
        emptycols.append(x)

for y, line in enumerate(lines):
    if set(line) == {'.'}:
        emptyrows.append(y)

grid = {}
galaxies = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            galaxies.append((x, y))
        grid[x, y] = char


def distance(galaxies, factor):
    total = 0
    for (galx, galy), (otherx, othery) in itertools.combinations(galaxies, 2):
        for x in range(min(galx, otherx), max(galx, otherx)):
            total += factor if x in emptycols else 1
        for y in range(min(galy, othery), max(galy, othery)):
            total += factor if y in emptyrows else 1
    return total


print("Part 1:", distance(galaxies, 2))
print("Part 2:", distance(galaxies, 1000000))
