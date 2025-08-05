class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, total, temp):
            if total == target:
                res.append(temp[:])
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtrack(i + 1, total + candidates[i], temp)
                temp.pop()
        backtrack(0, 0, [])
        return res
        