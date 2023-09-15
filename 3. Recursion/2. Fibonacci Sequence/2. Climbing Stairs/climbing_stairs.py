class Solution(object):
    def climbStairs(self, n):
        if n <= 3:
            return n

        # n1 initially represents the number of ways to climb from step 0 to step 2 (2 ways: 1 + 1 or 2)
        n1 = 2
        # n2 initially represents the number of ways to climb from step 0 to step 3 (3 ways: 1 + 1 + 1, 1 + 2 or 2 + 1)
        n2 = 3

        """
        To climb to the nth stair from step 0, you have two options:
        1) Take a single step from the (n-1)th stair.
        2) Take a two-step leap from the (n-2)th stair.

        Therefore, the total number of distinct ways to reach the nth stair 
        from step 0 is the sum of the distinct ways to reach the (n-1)th and (n-2)th stairs from step 0.
        """

        for i in range(4, n + 1):
            # Calculate the sum of the number of ways to climb from step 0 to the (n-1)th and (n-2)th stairs
            # to find the number of ways to climb from step 0 to the nth stair.
            temp = n1 + n2
            # Update n1 and n2 for the next iteration.
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
