
def find_longest_substring(input_str):
    n = len(input_str)
    max_length = 0
    start = 0
    seen = {}
    for end in range(n):
        if input_str[end] not in seen:
            seen[input_str[end]] = end
        else:
            max_length = max(max_length, end - start)
            start = max(start, seen[input_str[end]] + 1)
            seen[input_str[end]] = end
        
        if end >= n - 1:
            max_length = max(max_length, end - start + 1)

    return max_length



def main():
   cases_and_ans = [
       ("abcdbea", 5),
       ("bbbbb", 1),
       ("", 0)
    ]
   for (inputs, ans) in cases_and_ans:
        assert find_longest_substring(inputs) == ans


if __name__ == "__main__":
   main()
