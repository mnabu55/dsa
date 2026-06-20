from TreeNode import *
from BinaryTree import *



def diameter_of_binaryTree(root):
    # function to recursively calculate the height of the tree
    # and update the diameter
    def dfs(node, diameter):
        if not node:
            return 0, diameter

        left_height, diameter = dfs(node.left, diameter)
        right_height, diameter = dfs(node.right, diameter)

        diameter = max(diameter, left_height + right_height)

        return max(left_height, right_height) + 1, diameter

    if not root:
        return 0

    diameter = 0
    _, diameter = dfs(root, diameter)

    return diameter

# Driver code
def main():
    list_of_trees = [ [TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6), TreeNode(7)],
                    [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(45), TreeNode(32), TreeNode(23), TreeNode(21), TreeNode(18), TreeNode(1)],
                    [TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(2), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(-1), TreeNode(-5), TreeNode(-8), TreeNode(-3), TreeNode(1), TreeNode(5), TreeNode(3)],
                    [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
    ]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    y = 1
    for tree in input_trees:
        print(y, ".\tInput Tree:", sep = "")
        #display_tree(tree.root)
        print("\tDiameter of the tree: ", diameter_of_binaryTree(tree.root), sep="")
        print("-"*100)
        y += 1

if __name__ == '__main__':
    main()
