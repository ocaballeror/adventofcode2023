import re


with open('input') as f:
    total = 0
    for gamenr, line in enumerate(f, start=1):
        if not line.strip():
            continue

        for match in re.findall(r'\d+ red', line):
            num = int(match.split()[0])
            if num > 12:
                break
        else:
            for match in re.findall(r'\d+ green', line):
                num = int(match.split()[0])
                if num > 13:
                    break
            else:
                for match in re.findall(r'\d+ blue', line):
                    num = int(match.split()[0])
                    if num > 14:
                        break
                else:
                    total += gamenr


print('total:', total)
