# type: ignore
import functools

def hash(label):
    return functools.reduce(lambda acc, x: ((acc + ord(x)) * 17) % 256, label, 0)

with open("input") as f:
    steps = f.read().strip().split(",")


part1 = sum(map(hash, steps))
print("Part 1:", part1)


boxes = [[] for _ in range(256)]
for instruction in steps:
    if '-' in instruction:
        label = instruction.strip('-')
        assert instruction == label + '-'

        box = boxes[hash(label)]
        exist = next((idx for idx, x in enumerate(box) if x[0] == label), None)
        if exist is None:
            continue
        box.pop(exist)
    else:
        label, lens = instruction.split('=')
        lens = int(lens)
        box = boxes[hash(label)]

        for idx, x in enumerate(box):
            if x[0] == label:
                box[idx] = (label, lens)
                break
        else:
            box.append((label, lens))

part2 = sum(
    (1 + boxidx) * (1 + lensidx) * lens[1]
    for lensidx, lens in enumerate(box)
    for boxidx, box in enumerate(boxes)
)
print("Part 2:", part2)
