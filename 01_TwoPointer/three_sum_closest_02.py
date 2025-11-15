# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_diff = inf
        closest_sum = 0

        nums.sort()
        for current in range(n - 2):
            low = current + 1
            high = n - 1

            while low < high:
                three_sum = nums[current] + nums[low] + nums[high]
                diff = target - three_sum
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closest_sum = three_sum

                if diff == 0:
                    return three_sum
                elif diff > 0:
                    low += 1
                else:
                    high -= 1

        return closest_sum


def main() -> None:
    solution = Solution()
    examples = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], -100),
        ([1, 2, 4, 8, 16, 32, 64, 128], 82),
    ]

    for idx, (nums, target) in enumerate(examples, start=1):
        print(f"Example {idx}:")
        print("nums=", nums)
        print("target=", target)
        result = solution.threeSumClosest(nums, target)
        print("closest sum =", result)
        print("-" * 40)


if __name__ == "__main__":
    main()
