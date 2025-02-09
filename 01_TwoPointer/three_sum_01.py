def three_sum(nums):
    nums.sort()

    n = len(nums)
    result = []

    for pivot in range(n):
        if nums[pivot] > 0:
            break
        if pivot > 0 and nums[pivot] == nums[pivot - 1]:
            continue
        
        low, high = pivot + 1, n - 1
        while low < high:
            total = nums[pivot] + nums[low] + nums[high]
            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:
                result.append([nums[pivot], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
    return result

# Driver code
def main():
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [-4, -1, -1, 0, 1, 2, 2],
        [-10, -7, -3, -1, 0, 3, 7, 10],
        [-3, -5, -7, -9]
    ]

    for idx, nums in enumerate(test_cases, 1):
        print(f"\nTest Case {idx}:\n\t Input:  {nums}")
        result = three_sum(nums)
        print(f"\t Output: {result}")
        print("-" * 100)


if __name__ == "__main__":
    main()
