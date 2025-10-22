from collections import Counter
import unittest


def removeDuplicateLetters(s: str) -> str:
    count = Counter(s)
    stack = []
    seen = set()

    for char in s:
        count[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and count[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return "".join(stack)


class TestRemoveDuplicateLetters(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(removeDuplicateLetters("bcabc"), "abc")
        self.assertEqual(removeDuplicateLetters("cbacdcbc"), "acdb")

    def test_single_letter(self):
        self.assertEqual(removeDuplicateLetters("a"), "a")

    def test_all_same_letters(self):
        self.assertEqual(removeDuplicateLetters("aaaaa"), "a")

    def test_already_unique(self):
        self.assertEqual(removeDuplicateLetters("abc"), "abc")

    def test_reverse_order(self):
        self.assertEqual(removeDuplicateLetters("zyx"), "zyx")

    def test_complex_case(self):
        self.assertEqual(removeDuplicateLetters("bbcaac"), "bac")

    def test_mixed(self):
        self.assertEqual(removeDuplicateLetters("abacb"), "abc")


if __name__ == "__main__":
    unittest.main()
