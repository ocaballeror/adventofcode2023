def read_input():
    instructions = []
    with open("input") as f:
        for line in f:
            dir, count, color = line.split()
            count = int(count)
            color = color.replace("(", "").replace(")", "")
            instructions.append((dir, count, color))
        return instructions


def area(instructions):
    x, y = (0, 0)
    lastx, lasty = x, y
    shoelace = 0
    perim = 0
    for dir, count in instructions:
        perim += count
        if dir == "R":
            x += count
        elif dir == "L":
            x -= count
        elif dir == "D":
            y += count
        elif dir == "U":
            y -= count

        shoelace += (lastx * y) - (x * lasty)
        lastx, lasty = x, y

    # pick's theorem
    return shoelace // 2 + (perim // 2) + 1


def part1():
    instructions = read_input()
    return area([(inst[0], inst[1]) for inst in instructions])


def part2():
    instructions = read_input()
    return area(
        [("RDLU"[int(color[6])], int(color[1:6], base=16)) for _, _, color in instructions]
    )

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
