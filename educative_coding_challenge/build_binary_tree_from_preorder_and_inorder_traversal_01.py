# Definition of a binary tree node
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# from ds_v1.BinaryTree.BinaryTree import TreeNode


def build_tree(p_order, i_order):
    if not p_order or not i_order:
        return None

    # The first element in preorder is the root
    root_value = p_order[0]
    root = TreeNode(root_value)

    # Find the index of the root in inorder
    root_index = i_order.index(root_value)

    # Elements to the left of root_index in inorder are part of the left subtree
    # Elements to the right of root_index in inorder are part of the right subtree
    left_i_order = i_order[:root_index]
    right_i_order = i_order[root_index + 1 :]

    # Corresponding elements in preorder for left and right subtrees
    left_p_order = p_order[1 : 1 + len(left_i_order)]
    right_p_order = p_order[1 + len(left_i_order) :]

    # Recursively build the left and right subtrees
    root.left = build_tree(left_p_order, left_i_order)
    root.right = build_tree(right_p_order, right_i_order)

    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


# Driver code
def main():
    inputs = [
        ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [3, 2, 1]),
    ]

    for i in range(len(inputs)):
        p_order = inputs[i][0]
        i_order = inputs[i][1]
        print(i + 1, ".\tpreorder:", p_order)
        print("\tinorder:", i_order)
        root = build_tree(p_order, i_order)
        print("\n\tThe inorder traversal of the constructed tree is: ", end="")
        inorder_traversal(root)
        print("\n" + "-" * 100)


if __name__ == "__main__":
    main()
