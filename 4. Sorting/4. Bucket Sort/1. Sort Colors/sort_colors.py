class Solution(object):
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        mid = 0

        # use <= so we check all elements
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums


def main():
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    result = sol.sortColors(nums)
    print(f"The sorted result is {result}")


if __name__ == "__main__":
    main()
