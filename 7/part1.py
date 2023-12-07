from collections import Counter


with open("input") as f:
    hands = {}
    for line in f:
        a, b = line.strip().split()
        hands[a] = int(b)


def poker(hand):
    count = Counter(hand)
    match sorted(count.values()):
        case [5]:
            return 1
        case [1, 4]:
            return 2
        case [2, 3]:
            return 3
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 5
        case [1, 1, 1, 2]:
            return 6
        case [1, 1, 1, 1, 1]:
            return 7


def compare(hand):
    return poker(hand), *("AKQJT98765432".index(card) for card in hand)


ranks = sorted(hands, key=compare, reverse=True)
winnings = sum(hands[h] * (idx + 1) for idx, h in enumerate(ranks))
print("Part 1:", winnings)
