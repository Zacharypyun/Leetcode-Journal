class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = 1
            else:
                answer[i] = answer[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums) - 1, -1 , -1):
            answer[i] = answer[i] * right
            right = right * nums[i]
        return answer