def two_sum(arr, t):
    seen = {}

    for i, num in enumerate(arr):
        lookup_number = t - num
        if lookup_number in seen:
            return [seen[lookup_number], i]
        seen[num] = i

    return []


def main():
    arrs = [
        [1, 10, 8, 4, 9],
        [5, 12, 15, 21, 6, 17],
    ]
    ts = [
        17,
        33,
    ]
    answers = [
        [2, 4],
        [1, 3],
    ]

    for arr, t, expected in zip(arrs, ts, answers):
        print(f"Input; arr: {arr},\tt: {t}")
        actual = two_sum(arr, t)
        print(f"Output; actual: {actual},\texpected: {expected}\n")
        assert actual == expected


class Test

if __name__ == "__main__":
    main()