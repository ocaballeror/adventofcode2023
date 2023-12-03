with open('input') as f:
    total = 0
    for gamenr, line in enumerate(f, start=1):
        if not line.strip():
            continue

        game, sets = line.strip().split(": ")
        sets = sets.split(";")
        r = 0
        g = 0
        b = 0
        for st in sets:
            subsets = st.strip().split(",")
            for sub in subsets:
                num, color = sub.strip().split()
                num = int(num)
                if color == 'red' and num > r:
                    r = num
                if color == 'green' and num > g:
                    g = num
                if color == 'blue' and num > b:
                    b = num
        total += r * g * b

print('total:', total)
