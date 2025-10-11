# first, remove non alphabet and number character from input string
# second, check if string is valid palindrome by two pointer

import re


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # string = ""
        # for char in s:
        #     if char.isalnum():
        #         string += char.lower()
        string = "".join([char.lower() for char in s if char.isalnum()])

        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True


def main():
    solution = Solution()

    input_strings = ["A man, a plan, a canal: Panama"]
    expecteds = [True]

    for input_string, expected in zip(input_strings, expecteds):
        print("input_string: ", input_string)
        actual = solution.validPalindrome(input_string)
        print(f"expected: {expected},\tactual: {actual}")
        assert expected == actual


if __name__ == "__main__":
    main()
