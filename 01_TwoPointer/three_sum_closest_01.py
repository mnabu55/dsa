# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            raise ValueError("Need at least three numbers")

        nums.sort()
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(best_sum - target):
                    best_sum = current

                if current == target:
                    return target
                if current < target:
                    left += 1
                else:
                    right -= 1

        return best_sum


def run_examples() -> None:
    solution = Solution()
    examples = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], -100),
        ([1, 2, 4, 8, 16, 32, 64, 128], 82),
    ]

    for nums, target in examples:
        print("input nums =", nums, "target =", target)
        result = solution.threeSumClosest(nums, target)
        print("closest sum =", result)
        print("-" * 40)


if __name__ == "__main__":
    run_examples()
