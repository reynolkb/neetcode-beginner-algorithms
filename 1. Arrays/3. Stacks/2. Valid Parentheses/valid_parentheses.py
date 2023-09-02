class Solution(object):
    def isValid(self, s):
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # if character is not a key in map, it's an opening bracket
            if c not in Map:
                # add opening bracket to stack
                stack.append(c)
                continue
            # if `not stack` returns true if the stack is empty
            # if the character at the top of the stack is not the valid open parentheses, return false
            if not stack or Map[c] != stack[-1]:
                return False
            stack.pop()

        return not stack


def main():
    s = "()[]{}"
    solution = Solution()
    result = solution.isValid(s)
    print("Is Valid:", result)


if __name__ == "__main__":
    main()
