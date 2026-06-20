"""
Statement:
For a given positive integer n, return an array of length n+1 such that
result[x] is the count of 1s in the binary representation of x, for 0 <= x <= n.
"""


def counting_bits(n: int) -> list[int]:
    result = [0] * (n + 1)
    for x in range(1, n + 1):
        # x >> 1 drops the last bit; (x & 1) adds 1 if x is odd
        result[x] = result[x >> 1] + (x & 1)
    return result


if __name__ == "__main__":
    for n in [2, 5, 8]:
        print(f"n={n}: {counting_bits(n)}")
