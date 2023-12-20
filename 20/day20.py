# type: ignore

import itertools
import math
from dataclasses import dataclass, field
from collections import deque, defaultdict


@dataclass
class Module:
    typ: str = ''
    dest: list[str] = field(default_factory=list)
    hi: bool = False
    mem: dict[str, bool] = field(default_factory=dict)
    hist: list[bool] = field(default_factory=list)


def read_input():
    modules = defaultdict(Module)
    with open("input") as f:
        for line in f:
            source, dest = line.strip().split(' -> ')
            dest = dest.split(', ')
            if source.startswith('%') or source.startswith('&'):
                typ = source[0]
                source = source[1:]
            elif source == 'broadcaster':
                typ = source
            else:
                raise RuntimeError
            modules[source] = Module(typ, dest, False)

        for name, module in list(modules.items()):
            for other in module.dest:
                if modules[other].typ == '&':
                    modules[other].mem[name] = False

        return modules


def sim(modules):
    pending = deque([('button', 'broadcaster', False)])
    hicount = 0
    locount = 0
    while pending:
        src, name, pulse = pending.popleft()
        # print(src, f'-{"high" if pulse else "low"}->', name)
        if pulse:
            hicount += 1
        else:
            locount += 1
        mod = modules[name]
        if mod.typ == '%':
            if pulse:
                continue
            mod.hi = not mod.hi
            mod.hist.append(mod.hi)
            for dest in mod.dest:
                pending.append((name, dest, mod.hi))
        elif mod.typ == '&':
            mod.mem[src] = pulse
            new = not all(mod.mem.values())
            mod.hist.append(new)
            for dest in mod.dest:
                pending.append((name, dest, new))
        elif mod.typ == 'broadcaster':
            for dest in mod.dest:
                pending.append((name, dest, pulse))

    return hicount, locount


def part1():
    modules = read_input()
    totalhi = 0
    totallo = 0
    for buttons in range(1, 1001):
        hi, lo = sim(modules)
        totalhi += hi
        totallo += lo

    return (totalhi * 1000 // buttons) * (totallo * 1000 // buttons)


def part2():
    modules = read_input()
    # copied from input. these four modules will be conjuncted to determine rx, so just search for
    # the pattern of them sending a high
    search = dict.fromkeys(['qs', 'km', 'kz', 'xj'])
    for buttons in itertools.count(1):
        sim(modules)

        for mod in search:
            if not search[mod] and True in modules[mod].hist:
                search[mod] = buttons

        if all(search.values()):
            return math.lcm(*search.values())


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
