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

class Solution:

    def __init__(self, weights: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for w in weights:
            prefix_sum += w
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        pass


# Your Solution object will be instantiated and called as such:
w = [1, 3, 2]
obj = Solution(w)
param_1 = obj.pickIndex()