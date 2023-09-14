class Solution(object):
    def climbStairs(self, n):
        if n <= 3:
            return n

        # n1 is set to 2 because there are 2 ways to climb 2 stairs at a time, either 1 + 1 or 2
        n1 = 2
        # n2 is set to 3 because there are 3 ways to climb 3 stairs at a time, either 1 + 1 + 1, 2 + 1 or 1 + 2
        n2 = 3

        """ 
        To climb to the nth stair, you have two options:

        Take a single step from the (n-1)th stair.
        Take a two-step leap from the (n-2)th stair.

        Therefore, the total number of distinct ways to climb to the nth stair is the sum of the distinct ways to climb to the (n-1)th and (n-2)th stairs.
        """
        for i in range(4, n + 1):
            # sum of previous two steps
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2


def main():
    sol = Solution()
    num = 4
    res = sol.climbStairs(num)
    print(
        "There are "
        + str(res)
        + " distinct ways to climb to the top of "
        + str(num)
        + " stairs."
    )


if __name__ == "__main__":
    main()
