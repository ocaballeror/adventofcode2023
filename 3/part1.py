with open('input') as f:
    data = []
    for y, line in enumerate(f):
        data.append([])
        for x, char in enumerate(line.strip()):
            data[-1].append(char)


def adjacent(x, y):
    for movex, movey in (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ):
        move = x + movex, y + movey
        try:
            yield data[move[1]][move[0]]
        except IndexError:
            pass


total = 0
for y, line in enumerate(data):
    acc = []
    ispart = False
    for x, char in enumerate(line):
        if char.isnumeric():
            acc.append(char)
            for other in adjacent(x, y):
                if not other.isnumeric() and other != '.':
                    ispart = True
        else:
            if acc and ispart:
                num = int(''.join(acc))
                total += num
            acc = []
            ispart = False

    if acc and ispart:
        num = int(''.join(acc))
        total += num

print('total:', total)
