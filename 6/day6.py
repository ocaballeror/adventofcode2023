import math


def race(time, distance):
    ways = 0
    for hold in range(1, time):
        reach = (time - hold) * hold
        if reach > distance:
            ways += 1
        elif ways > 0:
            break

    return ways

with open('input') as f:
    lines = f.read().strip().split("\n")
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))

total = 1
for time, dist in zip(times, distances):
    total *= race(time, dist)

print('Part 1:', total)

megatime = 0
megadist = 0
for time, dist in zip(times, distances):
    megatime = megatime * (10 ** math.ceil(math.log10(time))) + time
    megadist = megadist * (10 ** math.ceil(math.log10(dist))) + dist

print('Part 2:', race(megatime, megadist))
