# Function to find the minimum characters to append to string s
# to make string t a subsequence of s


def min_chars_to_append(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(t) - j


# Driver code
def main():
    inputs = [
        ("abc", "abdbc"),
        ("abc", "abcd"),
        ("abc", "abc"),
        ("abc", "def"),
        ("ace", "abcde"),
    ]

    for i in range(len(inputs)):
        s = inputs[i][0]
        t = inputs[i][1]
        print(i + 1, ".\ts:", s, "\tt:", t)
        result = min_chars_to_append(s, t)
        print("\tMinimum characters to append:", result)
        print("\n" + "-" * 100)


if __name__ == "__main__":
    main()
