def rain_water(heights):
    n = len(heights)
    drop_water = 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    while left <= right:
        if left_max > right_max:
            drop_water += max(0, right_max - heights[right])

            right_max = max(right_max, heights[right])
            right -= 1
        else:
            drop_water += max(0, left_max - heights[left])

            left_max = max(left_max, heights[left])
            left += 1
    
    return drop_water


# Driver code
def main():
    input_list = [
        [1, 0, 1, 2, 1, 4, 0, 3, 5], 
        [2, 0, 9, 6],
        [3, 1, 2, 0, 2],
        [4, 2, 5, 3],
        [3, 0]
    ]
    index = 1
    for i in input_list:
        print(str(index)+".\tHeights: "+str(i))
        print("\tMaximum rainwater: " + str(rain_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()
