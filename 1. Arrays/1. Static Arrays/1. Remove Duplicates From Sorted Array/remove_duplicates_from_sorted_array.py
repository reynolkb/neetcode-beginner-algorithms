class Solution(object):
    def removeDuplicates(self, nums):
        L = 1

        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print("Remove duplicates:", result)


if __name__ == "__main__":
    main()
