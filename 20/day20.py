# type: ignore

import itertools
from dataclasses import dataclass, field
from collections import deque, defaultdict


@dataclass
class Module:
    typ: str = ''
    dest: list[str] = field(default_factory=list)
    hi: bool = False
    mem: dict[str, bool] = field(default_factory=dict)


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


def ways(search, hi, modules):
    if search == 'broadcaster':
        if hi:
            raise RuntimeError
        return

    paths = []
    for name, mod in modules.items():
        for other in mod.dest:
            if other != search:
                continue
            # need mod to output equal to hi
            if mod.typ == '&':
                if hi is False:
                    paths.append([(into, True) for into in mod.mem])
            return

            if modules[search].typ:
                paths.append(name)

    return paths



def sim(modules, stopat=None):
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
            for dest in mod.dest:
                pending.append((name, dest, mod.hi))
        elif mod.typ == '&':
            mod.mem[src] = pulse
            new = not all(val for val in mod.mem.values())
            for dest in mod.dest:
                pending.append((name, dest, new))
        elif mod.typ == 'broadcaster':
            for dest in mod.dest:
                pending.append((name, dest, pulse))
        elif name == stopat and pulse is False:
            raise StopIteration

    return hicount, locount


def part1():
    modules = read_input()
    totalhi = 0
    totallo = 0
    for buttons in range(1, 1001):
        hi, lo = sim(modules)
        totalhi += hi
        totallo += lo

        if all(mod.hi is False for mod in modules.values()):
            break

    assert 1000 % buttons == 0
    return (totalhi * 1000 // buttons) * (totallo * 1000 // buttons)


def part2():
    modules = read_input()
    breakpoint()
    x = ways('rx', modules)
    breakpoint()
    for buttons in itertools.count():
        try:
            hi, lo = sim(modules, stopat='rx')
        except StopIteration:
            return buttons

    return buttons


if __name__ == "__main__":
    # print("Part 1:", part1())
    print("Part 2:", part2())
