class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in check:
                current = num + 1
                temp = 1
                while current in check:
                    temp += 1
                    current += 1
                longest = max(longest, temp)
        return longest

