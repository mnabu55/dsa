def find_duplicate(nums):
    n = len(nums)
    slow = fast = 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return nums[nums[slow]]


nums_array = [[3,4,4,4,2], [1,1,2,3,4,5], [1,2,3,3]]
for nums in nums_array:
    print(find_duplicate(nums))
