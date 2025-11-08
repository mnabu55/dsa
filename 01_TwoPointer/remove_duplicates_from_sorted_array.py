from typing import List


class Solution:
    def removeDuplicatesFromSortedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        insert_pos = 1
        prev = nums[0]
        for i in range(1, n):
            if nums[i] != prev:
                nums[insert_pos] = nums[i]
                insert_pos += 1
            prev = nums[i]

        return insert_pos
