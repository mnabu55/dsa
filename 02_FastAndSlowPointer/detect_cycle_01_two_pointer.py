from linked_list import LinkedList

def detect_cycle(head):
    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

