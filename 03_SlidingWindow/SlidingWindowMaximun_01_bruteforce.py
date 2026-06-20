


def find_max_sliding_window(nums, w):
    n = len(nums)
    max_vals = []
    for i in range(n - w + 1):
        max_val = nums[i]
        for j in range(i + 1, i + w):
            max_val = max(max_val, nums[j])
        max_vals.append(max_val)
    return max_vals


def main():
    nums_array = [
        [-4, 2, -5, 3, 6], 
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    w_array = [
        3,
        6,
        4
    ]
    ans_array = [
        [2, 3, 6],
        [6],
        [4, 5, 6, 7, 8, 9, 10]
    ]

    for nums, w, ans in zip(nums_array, w_array, ans_array):
        assert find_max_sliding_window(nums, w) == ans


if __name__=='__main__':
    main()
