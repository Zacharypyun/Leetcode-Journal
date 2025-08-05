class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(start, total):
            if total == target:
                res.append(temp[:])
            if total > target:
                return
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                backtrack(i, total + candidates[i])
                temp.pop()
        backtrack(0, 0)
        return res