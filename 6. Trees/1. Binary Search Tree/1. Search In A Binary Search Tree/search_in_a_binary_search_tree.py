from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root


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

    return result


# Main function
def main():
    # Initialize the root node
    root = TreeNode(4)

    # Insert other nodes to build the BST
    for val in [2, 7, 1, 3]:
        insertBST(root, val)

    # Create the solution object and search for the node
    sol = Solution()
    subtree_root = sol.searchBST(root, 2)

    # Print the subtree rooted at the found node
    result = levelOrderTraversal(subtree_root)
    print(result)  # Output should be [2, 1, 3]


if __name__ == "__main__":
    main()
