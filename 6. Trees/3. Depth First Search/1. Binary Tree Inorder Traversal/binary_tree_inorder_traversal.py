from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        """
        The inorder traversal works as follows:
        1. Traverse the left subtree.
        2. Visit the root node.
        3. Traverse the right subtree.

        For example, consider this tree:
              3
             / \
            2   4

        - The traversal first goes to the leaf node 2 and appends its value.
        - It then unwinds the call stack to visit the root node 3 and appends its value.
        - Finally, it visits the right leaf node 4 and appends its value.

        The recursion enables this behavior, effectively making each 'node' 
        the root of its own subtree during the traversal.
        """
        if node:
            # Traverse the left subtree
            self.helper(node.left, result)
            # Visit the root node
            result.append(node.val)
            # Traverse the right subtree
            self.helper(node.right, result)


def build_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()

        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)

        i += 1

    return root


def main():
    # Create the tree based on list structure
    """ 
        5
       / \
      3   8
     / \ / \
    2  4 6  9
    """
    root = build_tree_from_list([5, 3, 8, 2, 4, 6, 9])

    # Create the solution object and perform inorder traversal
    sol = Solution()
    inorder_result = sol.inorderTraversal(root)

    # Print the result
    print(inorder_result)  # Output should be [1, 3, 2]


if __name__ == "__main__":
    main()
