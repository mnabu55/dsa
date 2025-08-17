def rain_water(heights):
    n = len(heights)
    drop_water = 0
    for i in range(n):
        max_left, max_right = 0, 0
        left = i - 1
        while left >= 0:
            max_left = max(max_left, heights[left])
            left -= 1
        
        right = i + 1
        while right < n:
            max_right = max(max_right, heights[right])
            right += 1
        
        height = min(max_left, max_right)
        drop_water += max(height - heights[i], 0)
    
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
