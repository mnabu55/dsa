# =========================================================================
# Problem: Find Target Indeices After Sorting Array
# URL: https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

from typing import List


# Approarch: Linear search
# Time complexity: O(NlogN)
# Space complexity: O(N)
def find_target_indices(nums: List[int], target: int) -> List[int]:
    target_indeces = []
    nums.sort()

    for i, num in enumerate(nums):
        if num == target:
            target_indeces.append(i)

    return target_indeces


def main():
    nums_array = [
        [1, 2, 3, 4],
        [3, 7, 2],
        [5],
        [8, 1, 4, 2, 1, 4, 8],
        [10, 20, 30],
        [4, 3, 2, 5, 1],
    ]
    target_array = [4, 7, 5, 8, 20, 7]
    expected_array = [[3], [2], [0], [5, 6], [1], []]

    for nums, target, expected in zip(nums_array, target_array, expected_array):
        print(f"nums: {nums},\ttarget: {target}")
        actual = find_target_indices(nums, target)
        print(f"actual: {actual},\texpected: {expected}\n")
        assert actual == expected


if __name__ == "__main__":
    main()
