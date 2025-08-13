'''
# LeetCode Problem: 15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Approach: Two-Pointer Technique
This approach combines sorting and pointers. It has a time complexity of O(n log n).

Utilizing Pointers
After sorting the array, we'll loop through it, fixing each element nums[i] as the first element of a potential triplet. Then, use two pointers "left" and "fright" for the rest of the array.

The left pointer starts at i + 1.
The right pointer starts at the end of the array.

Using these two pointers, we'll search for combinations where the sum of nums[i] + nums[left] + nums[right] equals zero.


# approach: Two Pointer Technique
ソートとポインタを組み合わせる
O(n log n) の計算量がかかります。

ポインタの活用
ソートされた配列をループし、各要素 nums[i] を最初の要素として固定します。次に、残りの配列に対して、2つのポインタ（left と right）を使用します。
left ポインタは i + 1 から開始します。
right ポインタは配列の末尾から開始します。
この2つのポインタを使い、nums[i] + nums[left] + nums[right] の合計がゼロになる組み合わせを探します。
'''
def three_sum(nums):
    # Replace this placeholder return statement with your code
    n = len(nums)
    triplets = []
    nums.sort()
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            sum_3 = nums[i] + nums[left] + nums[right]
            if sum_3 < 0:
                left += 1
            elif sum_3 > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    
    return triplets


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
