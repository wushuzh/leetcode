def num_jewels_in_stones_v1(J: str, S: str) -> int:
    count = 0
    for c in S:
        if c in J:
            count += 1
    return count


def num_jewels_in_stones_v2(J, S):
    return sum(s in J for s in S)


def num_jewels_in_stones_v3(J, S):
    return sum(map(J.count, S))


def num_jewels_in_stones_v4(J, S):
    return sum(map(S.count, J))
