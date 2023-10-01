from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        # Create an empty dictionary
        inorder_dict = {}

        # Loop through the list with index and value
        for idx, num in enumerate(inorder):
            # Assign the index to the corresponding number in the dictionary
            inorder_dict[num] = idx

        # Pointer for preorder list
        pre_idx = [0]

        # Recursive function to build the tree
        def build_tree(left, right):
            if left > right:
                return None

            # Get the current root from preorder
            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)

            # Move the pointer for preorder list
            pre_idx[0] += 1

            # Split the inorder list and build left and right subtrees
            root.left = build_tree(left, inorder_dict[root_val] - 1)
            root.right = build_tree(inorder_dict[root_val] + 1, right)

            return root

        return build_tree(0, len(inorder) - 1)


def level_order_traversal(root):
    if not root:
        return []

    output = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            output.append(None)

    # Remove trailing 'None' values
    while output[-1] is None:
        output.pop()

    return output


# Main function
def main():
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)

    print(level_order_traversal(root))


if __name__ == "__main__":
    main()
