def is_happy_number(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        total = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total += digit * digit
        return total

    slow = n
    fast = sum_of_squares(n)

    while fast != 1 and slow != fast:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))

    return fast == 1


import unittest


class TestHappyNumber(unittest.TestCase):
    def test_happy_numbers(self):
        self.assertTrue(is_happy_number(19))
        self.assertTrue(is_happy_number(7))
        self.assertTrue(is_happy_number(1))

    def test_unhappy_numbers(self):
        self.assertFalse(is_happy_number(2))
        self.assertFalse(is_happy_number(3))
        self.assertFalse(is_happy_number(4))

    def test_large_happy_number(self):
        self.assertTrue(is_happy_number(100))

    def test_large_unhappy_number(self):
        self.assertFalse(is_happy_number(20))


if __name__ == "__main__":
    unittest.main()
