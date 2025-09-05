from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]



def main():
    nums_array = [
        [3,2,1,5,6,4],
        [3,2,3,1,2,4,5,5,6],
    ]
    ks = [2, 4]
    expecteds = [5, 4]

    solution = Solution()
    for nums, k, expected in zip(nums_array, ks, expecteds):
        print(f"nums: {nums},\tk: {k}")
        actual = solution.findKthLargest(nums, k)
        print(f"actual: {actual},\texpected: {expected}")
        assert actual == expected


if __name__ == "__main__":
    main()