from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


def two_sum_binary_search(nums: List[int], target: int) -> List[int]:
    """
    constraints: nums should be sorted.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return []


def main():
    nums_list = [
        [2, 7, 11, 15],
        [2, 3, 4],
        [3, 3],
        [],             # 配列が空
        [2, 7, 11, 15], # ターゲット値が存在しない
        [2, 7, 2, 15]   # 配列に重複した数値が含まれる場合
    ]
    targets = [
        9,
        6,
        6,
        9,
        10,
        4
    ]
    expects = [
        [0, 1],
        [0, 2],
        [0, 1],
        [],
        [],
        [0, 2]
    ]

    for i in range(len(nums_list)):
        nums = nums_list[i]
        target = targets[i]
        expect = expects[i]
        print(f"Test case: {i + 1}")
        print(f"\tnums: {nums}")
        print(f"\texpect: {expect}")
        actual = two_sum(nums, target)
        print(f"\tactual: {actual}")
        print()
        assert actual == expect


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([], 9) == []  # 空の配列
    assert two_sum([2, 7, 11, 15], 10) == []  # ターゲット値が存在しない
    assert two_sum([2, 7, 2, 15], 4) == [0, 2] #配列に重複した数値が含まれる場合


if __name__ == '__main__':
    main()
