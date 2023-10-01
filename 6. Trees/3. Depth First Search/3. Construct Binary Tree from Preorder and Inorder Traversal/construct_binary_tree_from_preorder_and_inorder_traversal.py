from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder ALWAYS has the node first. But you don't know the size of either branch.
        # inorder ALWAYS has the left branch to the left of the node, and right branch right of the node. So now you know the size of each branch.
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        # start at 1 for preorder since you want to skip index 0 which is the root_val
        # end at one before mid(exclusive) for inorder since we want to skip root_val
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


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
