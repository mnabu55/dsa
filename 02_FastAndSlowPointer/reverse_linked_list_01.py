from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
from print_list import print_list_with_forward_arrow

def reverse(head):
    prev = None
    current = head
    next = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev


# Driver code
def main():
    input = (
                [1,2,3,4,5],
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:  ", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tAfter reverse:", end=" ", sep="")
        head = reverse(head)
        print_list_with_forward_arrow(head)
        print("\n")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
	