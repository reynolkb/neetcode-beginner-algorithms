class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution = Solution()
    result = solution.removeElement(nums, val)
    print("Remove element:", result)


if __name__ == "__main__":
    main()
