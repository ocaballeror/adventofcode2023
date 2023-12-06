with open('input') as f:
    lines = f.read().strip().split("\n")
    times = map(int, lines[0].split(":")[1].split())
    distances = map(int, lines[1].split(":")[1].split())

    total = 1
    for time, dist in zip(times,distances):
        ways = 0
        for hold in range(1, time):
            reach = (time - hold) * hold
            if reach > dist:
                ways += 1
        print(ways)
        total *= ways

print('Part 1:', total)
