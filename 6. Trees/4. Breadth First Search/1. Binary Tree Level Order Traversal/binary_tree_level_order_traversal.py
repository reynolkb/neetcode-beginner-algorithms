from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            current_level = []

            for i in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result


def create_tree(values):
    if not values:
        return None

    root = TreeNode(values.pop(0))
    queue = deque([root])

    while values and queue:
        current = queue.popleft()
        left_val = values.pop(0)
        if left_val is not None:
            current.left = TreeNode(left_val)
            queue.append(current.left)
        if values:
            right_val = values.pop(0)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)

    return root


def main():
    input_values = [3, 9, 20, None, None, 15, 7]
    root = create_tree(input_values)
    solution = Solution()
    output = solution.levelOrder(root)
    print(output)


if __name__ == "__main__":
    main()
