from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        # Continue as long as there are nodes in the stack or a current node to explore
        while stack or curr:
            # Traverse to the leftmost node and push nodes onto the stack along the way
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop the top node from stack and make it the current node
            curr = stack.pop()
            # Decrement k as we've visited one more node
            k -= 1

            # If k becomes 0, we've reached the kth smallest
            if k == 0:
                return curr.val

            # Move to the right child of the current node for the next iteration
            curr = curr.right


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


def ordinal(n):
    if n == 1:
        return "1st"
    elif n == 2:
        return "2nd"
    elif n == 3:
        return "3rd"
    else:
        return f"{n}th"


def main():
    root = build_tree_from_list([5, 3, 6, 2, 4, None, None, 1])

    # Create the solution object and find the kth smallest element
    sol = Solution()
    k = 4
    result = sol.kthSmallest(root, k)

    # Print the result
    print(f"The {ordinal(k)} smallest element is {result}")


if __name__ == "__main__":
    main()
