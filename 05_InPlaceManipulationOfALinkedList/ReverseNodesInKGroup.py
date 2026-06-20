from __future__ import print_function
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_reversal import reverse_linked_list
from print_list import print_list_with_forward_arrow

def reverse_k_groups(head, k):

    dummy = LinkedListNode(-1)
    dummy.next = head
    ptr = dummy
 

    while(ptr != None):

        tracker = ptr

        for i in range(k):
            if not tracker:
                break
            tracker = tracker.next
        if not tracker:
            break
    
        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next
        
# Driver code
def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 2, 8, 7, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], [1]]
    k = [3, 2, 1, 7, 1]

    for i in range(len(input_list)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tLinked list: ", end=" ")
        print_list_with_forward_arrow(input_linked_list.head)
        print('\n\tk = ', k[i])
        print("\tReversed linked list: ", end=" ")
        result = reverse_k_groups(input_linked_list.head, k[i])
        print_list_with_forward_arrow(result)
        print("\n")
        print('-' * 50)


if __name__ == '__main__':
    main()
