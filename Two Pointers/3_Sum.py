class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sums = []
        r = len(nums) - 1
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            mid = l + 1
            r = len(nums) - 1
            while r > mid:
                currSum = nums[l] + nums[mid] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    mid += 1
                else:
                    sums.append([nums[l], nums[mid], nums[r]])
                    mid -= 1
                    r -= 1
                    while mid < r and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < r and nums[r] == nums[r + 1]:
                        r -= 1
        return sums
