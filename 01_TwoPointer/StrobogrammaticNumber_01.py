'''
Given a string num representing an integer, determine whether it is a strobogrammatic number. Return TRUE if the number is strobogrammatic or FALSE if it is not.

Note:A strobogrammatic numberappears the same when rotated 180180degrees (viewed upside down). For example, “69” is strobogrammatic because it looks the same when flipped upside down, while “962” is not.
Constraints:

- 1<=1<=num.length<=50<=50
- num contains only digits.
- num has no leading zeros except when the number itself is zero.
'''

def is_strobogrammatic(num):
    digit_map = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }
    
    n = len(num)
    left, right = 0, n - 1
    
    while left <= right:
        if num[left] not in digit_map or num[right] not in digit_map:
            return False
        if digit_map[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    nums = ["69", "818", "962"]
    expecteds = [True, True, False]

    for i in range(len(nums)):
        num = nums[i]
        expected = expecteds[i]
        actual = is_strobogrammatic(num)
        assert actual == expected, f"case [{i}], failed."


if __name__ == '__main__':
    main()
