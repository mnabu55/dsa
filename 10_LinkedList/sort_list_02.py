# LeetCode 148: Sort List - Bottom-up Merge Sort (Iterative)

from typing import Optional, Tuple


class LinkedList:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def sort_list(head):
    if head is None or head.next is None:
        return head

    mid = find_mid(head)
    left = sort_list(head)
    right = sort_list(mid)

    return merge(left, right)


def find_mid(head):
    if not head:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow

        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None

    return slow


def merge(left, right):
    dummy = curr = ListNode(0)
    while left and right:
        if left.val <= right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    if left:
        curr.next = left
    elif right:
        curr.next = right

    return dummy.next


# Driver code
def main():
    input = (
        [5, 1, 4, 2, 3],
        [10, 2, 18, 3, 25, 4, 13, 11],
        [3, 2, 1, 0, -1, -2, -3],
        [12, 2, 17, 26, 72, 9, 88, 16, 11],
        [5],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i + 1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tSorted linked list: ", end="")
        print_list_with_forward_arrow(sort_list(input_linked_list.head))
        print("\n", "-" * 100, "\n")


if __name__ == "__main__":
    main()
