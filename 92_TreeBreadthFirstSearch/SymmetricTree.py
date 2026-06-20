from TreeNode import *
from BinaryTree import *

from collections import deque 

def is_symmetric(root):
    # queue = []
    # queue.append(root.left)
    # queue.append(root.right)

    queue = deque()
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        # left = queue.pop(0)
        # right = queue.pop(0)
        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.data != right.data:
            return False

        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True


# Driver code
def main():
    list_of_trees = [
        [
            TreeNode(1),
            TreeNode(2),
            TreeNode(2),
            TreeNode(3),
            TreeNode(4),
            TreeNode(4),
            TreeNode(3),
        ],
        [
            TreeNode(18),
            TreeNode(21),
            TreeNode(21),
            TreeNode(47),
            TreeNode(20),
            TreeNode(21),
            TreeNode(47),
        ],
        [
            TreeNode(25),
            TreeNode(4),
            TreeNode(67),
            TreeNode(2),
            TreeNode(3),
            TreeNode(3),
            TreeNode(2),
        ],
        [TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), None, None, TreeNode(3)],
        [
            TreeNode(1),
            TreeNode(2),
            TreeNode(2),
            None,
            TreeNode(3),
            TreeNode(3),
            None,
            TreeNode(4),
            TreeNode(5),
            TreeNode(5),
            TreeNode(4),
        ],
    ]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    i = 0
    for tree in input_trees:
        print(i + 1, ".\tInput Tree: ")
        #display_tree(tree.root)
        print("\n\tResult:", is_symmetric(tree.root))
        print("-" * 100)
        i += 1


if __name__ == "__main__":
    main()
