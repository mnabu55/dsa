from collections import defaultdict
import heapq


def third_max(nums):
    min_heap = []
    seen = set()

    for num in nums:
        if num in seen:
            continue

        if len(min_heap) >= 3:
            if min_heap[0] < num:
                seen.remove(min_heap[0])
                heapq.heappop(min_heap)

                heapq.heappush(min_heap, num)
                seen.add(num)
        else:
            heapq.heappush(min_heap, num)
            seen.add(num)

    if len(min_heap) == 1:
        return min_heap[0]
    elif len(min_heap) == 2:
        first_num = heapq.heappop(min_heap)
        second_num = heapq.heappop(min_heap)
        return max(first_num, second_num)

    return min_heap[0]


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
