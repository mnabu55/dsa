import heapq


def find_kth_largest(nums, k):
    n = len(nums)
    min_heap = []

    for i in range(k):
        min_heap.append(nums[i])
    
    heapq.heapify(min_heap)

    for i in range(k, n):
        num = nums[i]
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return min_heap[0]


def main():
    test_cases = [
        ([5, 12, 9, 0, 6, 7, 1, 8, 4, 9], 4),
        ([122, 67, 89, 34, 23, 156, 132, 99, 94, 67, 72, 107, 103, 83, 125, 54, 48, 58], 6),
    ]
    expecteds = [
        8,
        103,
    ]

    for (nums, k), expected in zip(test_cases, expecteds):
        actual = find_kth_largest(nums, k)
        assert actual == expected


if __name__ == "__main__":
    main()
