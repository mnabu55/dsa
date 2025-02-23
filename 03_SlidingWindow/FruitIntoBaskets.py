'''
Problem: Fruits into Baskets
- Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket.
- The only restriction is that each basket can have only one type of fruit.
- You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
- Write a function to return the maximum number of fruits in both the baskets.

'''
from typing import List


def total_fruit(fruits: List[int]) -> int:
    baskets = {}
    max_fruits = 0
    left = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        baskets[fruit] = baskets.get(fruit, 0) + 1

        while len(baskets) > 2:
            left_fruit = fruits[left]
            baskets[left_fruit] -= 1

            if baskets[left_fruit] == 0:
                del baskets[left_fruit]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits


def main():
    fruits_list = [
        [1,2,3,4],
        [3,2,1,1,2,3],
        [2,3,2,1,3,2,1]
    ]
    for fruits in fruits_list:
        print("Input: ", fruits)
        print("Output: ", total_fruit(fruits))
        print("-"*50)


if __name__ == '__main__':
    main()
