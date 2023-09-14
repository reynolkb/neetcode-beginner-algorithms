class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 2) + self.fib(n - 1)


def main():
    sol = Solution()
    num = 4
    res = sol.fib(num)
    print("The fib of " + str(num) + " is " + str(res))


if __name__ == "__main__":
    main()
