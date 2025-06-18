class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in strs:
            sortedStr = ''.join(sorted(i))
            if sortedStr in check:
                check[sortedStr].append(i)
            else:
                check[sortedStr] = [i]
        return list(check.values())
