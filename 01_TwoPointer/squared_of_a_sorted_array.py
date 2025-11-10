# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List


class Solution:
    def squaresOfASortedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 0:
            return []

        res = [0] * n
        insert_pos = n - 1

        left, right = 0, n - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res[insert_pos] = nums[left] * nums[left]
                left += 1
            else:
                res[insert_pos] = nums[right] * nums[right]
                right -= 1

            insert_pos -= 1

        return res


def run_examples() -> None:
    solution = Solution()
    examples = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [],
        [0, 0, 1],
    ]

    for nums in examples:
        result = solution.squaresOfASortedArray(nums)
        print("input=", nums)
        print("output=", result)
        print("-" * 40)


if __name__ == "__main__":
    run_examples()
