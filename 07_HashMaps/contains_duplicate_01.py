def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = 1

    return False


def main():
    nums_array = [
        [2,2,3,1,2],
        [5,4,2,1,9,6,3],
        [10,4,12,4,7,1,4],
    ]
    expecteds = [
        True,
        False,
        True,
    ]

    for nums, expected in zip(nums_array, expecteds):
        print(f"input: {nums}")
        actual = contains_duplicate(nums)
        print(f"actual: {actual},\texpected: {expected}")


if __name__ == "__main__":
    main()
