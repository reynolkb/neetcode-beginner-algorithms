from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Found the node
        else:
            # Case 1: Node is a leaf node: Simply remove it.
            # Case 2: Node has one child: Replace the node with its child.
            """
            If a node is a leaf (Case 1), it means both root.left and root.right are None. So when it says if not root.left: return root.right, it effectively returns None, removing the leaf node.

            If the node has only one child (Case 2), one of root.left or root.right will be None, and the other will be the child node. In this case, return root.right or return root.left will return that child, effectively replacing the node with its only child.
            """
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: Node has two children: Find the inorder successor (smallest node in right subtree), replace the node with it, and then recursively delete the inorder successor.
            # Another approach is to find the inorder predecessor (the largest node in the left subtree).
            """ 
            The inorder successor is chosen because it is guaranteed to be larger than all nodes in the left subtree (since it's the smallest node in the right subtree) but smaller than the remaining nodes in the right subtree (since it's the smallest among them). This makes it an ideal candidate to replace the deleted node, while preserving the BST property.
            """
            minRightTree = self.getMin(root.right)
            root.val = minRightTree.val
            # After replacing the value of the node to be deleted with the value of its inorder successor, that inorder successor node itself becomes redundant and must be deleted to maintain the uniqueness of values in the BST.
            # The inorder successor does not have a left node, it might have a right node, but doesn't have a left since it's the smallest value in the right tree.
            root.right = self.deleteNode(root.right, minRightTree.val)

        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node


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
