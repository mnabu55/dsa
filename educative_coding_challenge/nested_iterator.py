from nested_integers import NestedIntegers


class NestedIterator:
    """
    Iterator for flattening nested NestedIntegers objects.
    """

    def __init__(self, nested_list):
        """
        Initialize iterator with a list of NestedIntegers objects.

        Args:
            nested_list: A list containing NestedIntegers objects or regular lists
        """
        self.stack = [iter(nested_list)]
        self.current = None

    def has_next(self):
        """
        Check if there are more integers in the nested structure.

        Returns:
            bool: True if there are more integers, False otherwise
        """
        while self.stack:
            try:
                element = next(self.stack[-1])
                if element.is_integer():
                    self.current = element.get_integer()
                    return True
                else:
                    nested_list = element.get_list()
                    if nested_list:
                        self.stack.append(iter(nested_list))
            except StopIteration:
                self.stack.pop()
        return False

    def next(self):
        """
        Get the next integer in the nested structure.

        Returns:
            int: The next integer
        """
        return self.current


# Test cases
if __name__ == "__main__":
    # Test 1: Simple nested structure [1, [2, 3], 4]
    ni1 = NestedIntegers(1)
    ni2 = NestedIntegers()
    ni2.add(NestedIntegers(2))
    ni2.add(NestedIntegers(3))
    ni_root1 = NestedIntegers()
    ni_root1.add(ni1)
    ni_root1.add(ni2)
    ni_root1.add(NestedIntegers(4))

    iterator1 = NestedIterator(ni_root1.get_list())
    result1 = []
    while iterator1.has_next():
        result1.append(iterator1.next())
    print(f"Test 1: [1, [2, 3], 4]")
    print(f"Result: {result1}")
    print(f"Expected: [1, 2, 3, 4]\n")

    # Test 2: Deeply nested [1, [2, [3, 4]], [5, [6, 7]]]
    ni_3_4 = NestedIntegers()
    ni_3_4.add(NestedIntegers(3))
    ni_3_4.add(NestedIntegers(4))

    ni_2_nested = NestedIntegers()
    ni_2_nested.add(NestedIntegers(2))
    ni_2_nested.add(ni_3_4)

    ni_6_7 = NestedIntegers()
    ni_6_7.add(NestedIntegers(6))
    ni_6_7.add(NestedIntegers(7))

    ni_5_nested = NestedIntegers()
    ni_5_nested.add(NestedIntegers(5))
    ni_5_nested.add(ni_6_7)

    ni_root2 = NestedIntegers()
    ni_root2.add(NestedIntegers(1))
    ni_root2.add(ni_2_nested)
    ni_root2.add(ni_5_nested)

    iterator2 = NestedIterator(ni_root2.get_list())
    result2 = []
    while iterator2.has_next():
        result2.append(iterator2.next())
    print(f"Test 2: [1, [2, [3, 4]], [5, [6, 7]]]")
    print(f"Result: {result2}")
    print(f"Expected: [1, 2, 3, 4, 5, 6, 7]\n")

    # Test 3: Single integer [5]
    ni_root3 = NestedIntegers()
    ni_root3.add(NestedIntegers(5))

    iterator3 = NestedIterator(ni_root3.get_list())
    result3 = []
    while iterator3.has_next():
        result3.append(iterator3.next())
    print(f"Test 3: [5]")
    print(f"Result: {result3}")
    print(f"Expected: [5]\n")

    # Test 4: Complex nested [1,2,[3,[4,5,6],[7,8],9],10]
    ni_4_5_6 = NestedIntegers()
    ni_4_5_6.add(NestedIntegers(4))
    ni_4_5_6.add(NestedIntegers(5))
    ni_4_5_6.add(NestedIntegers(6))

    ni_7_8 = NestedIntegers()
    ni_7_8.add(NestedIntegers(7))
    ni_7_8.add(NestedIntegers(8))

    ni_3_nested = NestedIntegers()
    ni_3_nested.add(NestedIntegers(3))
    ni_3_nested.add(ni_4_5_6)
    ni_3_nested.add(ni_7_8)
    ni_3_nested.add(NestedIntegers(9))

    ni_root4 = NestedIntegers()
    ni_root4.add(NestedIntegers(1))
    ni_root4.add(NestedIntegers(2))
    ni_root4.add(ni_3_nested)
    ni_root4.add(NestedIntegers(10))

    iterator4 = NestedIterator(ni_root4.get_list())
    result4 = []
    while iterator4.has_next():
        result4.append(iterator4.next())
    print(f"Test 4: [1,2,[3,[4,5,6],[7,8],9],10]")
    print(f"Result: {result4}")
    print(f"Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n")
