class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(temp, used):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    temp.append(nums[i])
                    backtracking(temp, used)
                    used[i] = False
                    temp.pop()
        backtracking([], [False] * len(nums))
        return res