from collections import Counter
import heapq


def reorganize_string(str):
    # Calculate the frequency of characters in string and store counts
    # of each character along with the character itself in hash map.
    char_counter = Counter(str)

    # initializing heap
    most_freq_chars = []

    # Store character and its negative frequency in the array
    for char, count in char_counter.items():
        most_freq_chars.append([-count, char])

    # Construct heap from the array
    heapq.heapify(most_freq_chars)

    # initializing variables
    previous = None
    result = ""

    while len(most_freq_chars) > 0 or previous:
        count, char = heapq.heappop(most_freq_chars)
        result = result + char
        # decrement the character count, as we've now used one occurrence of it
        count = (
            count + 1
        )  # as we store negative character counts, adding 1 is actually a decrement operation

        # pushing the char back to heap
        if previous:
            heapq.heappush(most_freq_chars, previous)
            previous = None

        # setting previous to the most recent used char
        if count != 0:
            previous = [count, char]

    return result


def main():
    test_cases = [
        ("aaabc", "abaca"),
    ]

    for test_case in test_cases:
        s, expected = test_case
        actual = reorganize_string(s)
        print(f"s: {s}")
        print(f"actual: {actual},\texpected: {expected}")
        assert actual == expected


if __name__ == "__main__":
    main()
