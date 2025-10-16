import heapq


def third_max(nums):
    max_heap = [-num for num in set(nums)]
    heapq.heapify(max_heap)

    if len(max_heap) < 3:
        return -max_heap[0]

    for _ in range(2):
        heapq.heappop(max_heap)

    return -heapq.heappop(max_heap)


# Driver code
def main():
    test_cases = [[3, 2, 1], [1, 2], [2, 2, 3, 1], [5, 5, 4, 3, 2], [1, 1, 1, 1]]

    i = 0
    for nums in test_cases:
        print(i + 1, ".\tnums: ", nums, sep="")
        print("\n\tThe third maximum is: ", third_max(nums), sep="")
        print("-" * 100)
        i += 1


if __name__ == "__main__":
    main()
