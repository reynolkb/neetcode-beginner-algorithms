from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


def insertBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    else:
        root.right = insertBST(root.right, val)
    return root


def levelOrderTraversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


# Main function
def main():
    # Initialize the root node
    root = TreeNode(5)

    # Insert other nodes to build the BST
    for val in [3, 6, 2, 4, None, 7]:
        if val is not None:
            insertBST(root, val)

    # Create the solution object and search for the node
    sol = Solution()
    subtree_root = sol.deleteNode(root, 3)

    # Print the subtree rooted at the found node
    result = levelOrderTraversal(subtree_root)
    print(result)  # Output should be [2, 1, 3]


if __name__ == "__main__":
    main()
