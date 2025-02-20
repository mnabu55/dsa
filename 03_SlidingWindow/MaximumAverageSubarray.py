from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    if len(nums) < k:
        return 0
    
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k


def main():
    nums = [[1, 12, -5, -6, 50, 3], [5], [0], [1, 2], [1, 2, 3, 4, 5]]
    k = [4, 1, 100, 2, 2]

    for i in range(len(nums)):
        print(i + 1, ". \tInput: (", nums[i], ", ", k[i], ")", sep="")
        actual = find_max_average(nums[i], k[i])
        print("\tOutput: ", actual)
        print("-" * 50)


if __name__ == '__main__':
    main()
