# =========================================================================
# Problem: Random Pick with Weight
# URL: https://leetcode.com/problems/random-pick-with-weight/description/
# =========================================================================

# Approach:
# This problem is solved using a combination of Prefix Sums and Binary Search.

# Core Logic:
# 1. Prefix Sums (Initialization):
#    We pre-calculate the cumulative sums of the weights (w).
#    This converts the discrete weights into continuous ranges.
#    For example, w = [1, 3, 2] becomes prefix_sums = [1, 4, 6].
#    This means: index 0 is in range [0, 1), index 1 is in [1, 4), and index 2 is in [4, 6).
#
# 2. Random Target Generation:
#    In the pickIndex() method, we generate a random integer 'target' between 1 and the total sum of weights.
#
# 3. Binary Search:
#    We then perform a binary search on the prefix_sums array to find the first element
#    that is greater than or equal to our 'target'. The index of this element corresponds
#    to the correct weighted pick.

# Time Complexity:
# - __init__: O(N) to build the prefix sum array, where N is the number of weights.
# - pickIndex: O(log N) due to the binary search on the prefix sum array.

# Space Complexity:
# - O(N) to store the prefix sum array.

from typing import List
import random
import math


class Solution:

    def __init__(self, weights: List[int]):
        self.running_sums = []
        running_sum = 0

        for w in weights:
            running_sum += w
            self.running_sums.append(running_sum)
        
        self.total_sum = running_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        low = 0
        high = len(self.running_sums)

        while low < high:
            mid = low + (high - low) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low


# Your Solution object will be instantiated and called as such:
w = [1, 3, 2]
obj = Solution(w)
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
