with open('input') as f:
    lines = f.read().strip().split("\n")
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    ways = 0
    for hold in range(1, time):
        reach = (time - hold) * hold
        if reach > dist:
            ways += 1
        elif ways > 0:
            break
    print(ways)

print('Part 2:', ways)
