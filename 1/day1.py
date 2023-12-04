def firstlast(line, find):
    first = None
    last = None
    pos = float("inf")
    lastpos = -1

    for idx, num in enumerate(find):
        loc = line.find(num)
        if loc != -1 and loc < pos:
            pos = loc
            first = idx
        loc = line.rfind(num)
        if loc != -1 and loc > lastpos:
            last = idx
            lastpos = loc

    return first, pos, last, lastpos


with open("input") as f:
    total = 0
    chartotal = 0
    for line in f:
        charfirst, charpos, charlast, charlastpos = firstlast(line, "0123456789")
        chartotal += int(charfirst * 10 + charlast)

        first, pos, last, lastpos = firstlast(
            line, ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        )
        if charpos < pos:
            first = charfirst
        if charlastpos > lastpos:
            last = charlast

        total += int(first * 10 + last)

    print("Part 1:", chartotal)
    print("Part 2:", total)
