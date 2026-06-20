def print_list_with_forward_arrow(linked_list_node):
    current = linked_list_node
    while current:
        print(current.data, end=" ")  # print node value
        
        current = current.next
        if current:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")
