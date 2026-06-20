from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
from print_list import print_list_with_forward_arrow

def palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revert_data = reverse_linked_list(slow)
    check_status = compare_two_halves(head, revert_data)

    reverse_linked_list(revert_data)

    if check_status:
        return True
    return False


def compare_two_halves(first_half, second_half):
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True

# Driver code
def main():
    input = (
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
        print(j, ".\tLinked List:", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
	