class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        # Base case: if the node is null, return False
        if not root:
            return False
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        # If it's a leaf node, return if the targetSum equals 0. if true it means the target sum has been reached
        if not root.left and not root.right:
            return targetSum == 0
        """  
        Recursively check the left and right subtrees.
        If a valid path is found on the left (returns True), the 'or' short-circuits, skipping the right subtree check.
        If no valid path is found on the left (returns False), proceed to check the right subtree.
        The result of checking the right subtree (either True or False) is then returned up the call stack.
        """
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


def array_to_btree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def main():
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    root = array_to_btree(arr)
    solution = Solution()
    result = solution.hasPathSum(root, targetSum)
    print(result)  # Output: True


if __name__ == "__main__":
    main()
