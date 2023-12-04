with open('input') as f:
    data = {}
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            data[(x, y)] = char


def adjacent(x, y):
    for movex, movey in (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ):
        move = x + movex, y + movey
        if move in data:
            yield move

def readnum(x, y):
    movex = x
    while movex > 0 and data[(movex, y)].isnumeric():
        movex -= 1
    if not data[(movex, y)].isnumeric():
        movex += 1
    acc = []
    while (movex, y) in data and data[(movex, y)].isnumeric():
        acc.append(data[(movex, y)])
        movex += 1

    return int(''.join(acc))


total = 0
for (x, y), char in data.items():
    nums = set()
    if char == '*':
        for other in adjacent(x, y):
            if data[other].isnumeric():
                nums.add(readnum(*other))

        if len(nums) == 2:
            total += nums.pop() * nums.pop()

print('total:', total)
