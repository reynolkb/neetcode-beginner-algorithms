from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


def deserialize(data):
    if not data:
        return None
    root = TreeNode(data[0])
    queue = deque([root])
    i = 1
    while queue and i < len(data):
        node = queue.popleft()
        if data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1
    return root


def main():
    data = [1, 2, 3, None, 5, None, 4]
    root = deserialize(data)
    solution = Solution()
    output = solution.rightSideView(root)
    print(output)


if __name__ == "__main__":
    main()
