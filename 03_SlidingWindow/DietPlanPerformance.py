'''
Problem Statement: https://leetcode.com/problems/diet-plan-performance/

'''


def diet_plan_performance(calories, k, lower, upper):
    def calculate_points(calory, lower, upper):
        if calory > upper:
            return 1
        elif calory < lower:
            return -1
        else:
            return 0

    points = 0
    current_sum = sum(calories[:k])
    points += calculate_points(current_sum, lower, upper)

    for i in range(k, len(calories)):
        current_sum += calories[i] - calories[i - k]
        points += calculate_points(current_sum, lower, upper)
    
    return points

# Driver code
def main():
    test_cases = [
        ([3, 5, 8, 2, 6], 2, 7, 10),       # Test Case 1: Mixed performance
        ([1, 1, 1, 1, 1], 2, 5, 10),      # Test Case 2: All sums below the lower limit
        ([10, 12, 15, 20, 25], 3, 10, 30), # Test Case 3: All sums above the upper limit
        ([5, 10, 15, 20, 25, 30], 3, 20, 40), # Test Case 4: Mix of poor, normal, and good performances
        ([3, 8, 7, 4, 5, 6], 2, 7, 10)     # Test Case 5: Sliding window with variable performance
    ]

    
    for i, (calories, k, lower, upper) in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"\tcalories = {calories}")
        print(f"\tk = {k}")
        print(f"\tlower = {lower}")
        print(f"\tupper = {upper}")
        result = diet_plan_performance(calories, k, lower, upper)
        print(f"\n\tpoints = {result}")
        print("-" * 50)


if __name__ == '__main__':
    main()
