class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l += 1
            elif nums[m] > target:
                r -= 1
            else:
                return m
        return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    sol = Solution()
    result = sol.search(nums, target)
    print(f"The target {target} is at index {result}")


if __name__ == "__main__":
    main()
