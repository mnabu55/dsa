from linked_list_node import *
from linked_list import *

def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = head
    cur1 = head
    cur2 = cur1.next
    next = cur2.next
    head = cur2
    while cur1 and cur1.next:
        cur2 = cur1.next
        next = cur2.next
        prev.next = cur2
        cur1.next = next
        cur2.next = cur1
        prev = cur1
        cur1 = next
    return head


def main():
    lst = [1,2,3,4,5]
    linkedlist = LinkedList()
    linkedlist.create_linked_list(lst)
    print(linkedlist)
    ans = LinkedList()
    ans.head = swap_pairs(linkedlist.head)
    print(ans)


if __name__ == '__main__':
    main()
