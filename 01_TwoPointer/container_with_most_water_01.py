"""
# Statement
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


# **Solution: Container With Most Water**

- **Goal:** Find the maximum area.
- **Formula:** Area is calculated as `width * height`.
- **Technique:** Use the **two-pointer** approach.
- **Pointers:**
    - Initialize `left` at the beginning of the array.
    - Initialize `right` at the end of the array.
- **Area Calculation:**
    - `width` is `right - left`.
    - `height` is the smaller value between the heights at the `left` and `right` pointers (`min(height[left], height[right])`).
- **Update Maximum:**
    - Calculate the current area.
    - Update `max_amount` if the current area is greater than the current `max_amount`.
- **Pointer Movement:**
    - To find a potentially larger area, move the pointer that is currently pointing to the smaller height.
    - Since the height of the container is limited by the shorter line, moving the shorter line's pointer might allow for a taller container. Moving the taller line's pointer would only decrease the width without the possibility of increasing the height, leading to a smaller area.
- **Iteration:** Repeat this process until the `left` and `right` pointers meet.
"""

def container_with_most_water(height):
    n = len(height)
    max_amount = 0

    left = 0
    right = n - 1
    while left < right:
        current_height = min(height[left], height[right])
        width = right - left
        amount = current_height * width
        max_amount = max(max_amount, amount)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_amount

