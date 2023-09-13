class Solution(object):
    def factorial(self, n):
        # base case
        if n == 1:
            return 1
        return n * self.factorial(n - 1)


def main():
    sol = Solution()
    num = 5
    res = sol.factorial(num)
    print("The factorial of " + str(num) + " is " + str(res))
    """
    Call stack will be built like this:

    last in, first out
    top of call stack
    factorial(1) <-- base case, resolved first

    factorial(2)
    factorial(3)
    factorial(4)

    bottom of call stack
    factorial(5)
    """


if __name__ == "__main__":
    main()
