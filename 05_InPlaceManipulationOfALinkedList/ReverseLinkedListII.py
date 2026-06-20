# Definition for a Linked List node
# class LinkedListNode:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list
from print_list import print_list_with_forward_arrow


def reverse_between(head, left, right):
    # Replace this placeholder return statement with your code
    current, prev = head, None
    i = 1
    while current and i < left:
        prev = current
        current = current.next
        i += 1

    
    return head


def main():
    input = (
        [6, 8, 7],
        [9, 0, 8, 2]
    )
    left = [1, 2]
    right = [2, 4]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tReversed linked list: ", end="")
        print_list_with_forward_arrow(reverse_between(input_linked_list.head, left[i], right[i]))
        print("\n", "-" * 50)


if __name__ == "__main__":
    main()
