# Definition for singly-linked list.
from ListNode import ListNode
from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow


def twin_sum(head: ListNode) -> int:
    # --- 1. 中間を探す（fast/slow ポインタ）---
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # --- 2. 後半を反転する ---
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # prev が反転後の後半の先頭

    # --- 3. 前半と後半を走査して最大ツイン和を求める ---
    first = head
    second = prev
    max_sum = 0
    while second:  # second の方が短い（半分）
        twin_sum = first.val + second.val
        max_sum = max(max_sum, twin_sum)
        first = first.next
        second = second.next

    return max_sum


def main():

    lists = [
        [2, 3, 5, 7],
        [81, 144, 64, 121, 25, 49],
        [4, 5, 6, 7],
        [1, 1000],
        [11, 77, 44, 99, 22, 66, 55, 88],
    ]

    for i in range(len(lists)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i + 1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMaximum twin sum: ", twin_sum(input_linked_list.head))
        print("-" * 100)


if __name__ == "__main__":
    main()
